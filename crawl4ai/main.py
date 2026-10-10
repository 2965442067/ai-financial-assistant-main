# import asyncio
# import re
# from pathlib import Path
#
# from bs4 import BeautifulSoup
# from markdownify import markdownify
# from playwright.async_api import async_playwright
#
#
# def sanitize_filename(name: str) -> str:
#     return re.sub(r'[\\/:*?"<>|]', "_", name)
#
#
# async def crawl_factor(url: str):
#
#     async with async_playwright() as p:
#
#         browser = await p.chromium.launch(
#             headless=True
#         )
#
#         page = await browser.new_page()
#
#         await page.goto(
#             url,
#             wait_until="networkidle"
#         )
#
#         await page.wait_for_timeout(3000)
#
#         html = await page.content()
#
#         await browser.close()
#
#     soup = BeautifulSoup(
#         html,
#         "html.parser"
#     )
#
#     article = soup.select_one(
#         "article.max-w-4xl.mx-auto.px-4.sm\\:px-6.py-8"
#     )
#
#     if not article:
#         raise Exception("未找到 article")
#
#     title_tag = article.find("h1")
#
#     if not title_tag:
#         raise Exception("未找到标题")
#
#     title = title_tag.get_text(
#         strip=True
#     )
#
#     # ===== 块级公式 =====
#
#     for display in article.select(
#         ".katex-display"
#     ):
#
#         annotation = display.select_one(
#             "annotation[encoding='application/x-tex']"
#         )
#
#         if annotation:
#
#             tex = annotation.get_text(
#                 strip=True
#             )
#
#             display.replace_with(
#                 f"\n\n$$\n{tex}\n$$\n\n"
#             )
#
#     # ===== 行内公式 =====
#
#     for katex in article.select(".katex"):
#
#         annotation = katex.select_one(
#             "annotation[encoding='application/x-tex']"
#         )
#
#         if annotation:
#
#             tex = annotation.get_text(
#                 strip=True
#             )
#
#             katex.replace_with(
#                 f"${tex}$"
#             )
#
#     md = markdownify(
#         str(article),
#         heading_style="ATX"
#     )
#
#     md = re.sub(
#         r"\n{3,}",
#         "\n\n",
#         md
#     )
#
#     filename = (
#         sanitize_filename(title)
#         + ".md"
#     )
#
#     Path(filename).write_text(
#         md,
#         encoding="utf-8"
#     )
#
#     print(f"保存成功: {filename}")
#
#     return title, md
#
#
# async def main():
#
#     await crawl_factor(
#         "https://factors.directory/zh/factors/tech/price-volume-divergence"
#     )
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from playwright.async_api import async_playwright


SITEMAP = "https://factors.directory/sitemap.xml"


def sanitize_filename(name):
    return re.sub(r'[\\/:*?"<>|]', "_", name)


def get_factor_urls():
    xml = requests.get(SITEMAP, timeout=30).text

    soup = BeautifulSoup(xml, "xml")

    urls = []

    for loc in soup.find_all("loc"):
        url = loc.text.strip()

        if "/en/factors/" in url:
            url = url.replace("/en/", "/zh/")
            urls.append(url)

    urls = sorted(set(urls))

    print("共发现", len(urls), "个因子")

    return urls


def article_to_markdown(article):
    formulas = []

    # 块公式
    for display in article.select(".katex-display"):
        annotation = display.select_one(
            "annotation[encoding='application/x-tex']"
        )

        if annotation:
            tex = annotation.get_text(strip=True)

            formulas.append(tex)

            display.replace_with(
                f"\n\n$$\n{tex}\n$$\n\n"
            )

    # 行内公式
    for katex in article.select(".katex"):
        annotation = katex.select_one(
            "annotation[encoding='application/x-tex']"
        )

        if annotation:
            tex = annotation.get_text(strip=True)

            formulas.append(tex)

            katex.replace_with(
                f"${tex}$"
            )

    md = markdownify(
        str(article),
        heading_style="ATX"
    )

    md = re.sub(r"\n{3,}", "\n\n", md)

    return md, formulas
CONCURRENT = 10
async def worker(
    semaphore,
    browser,
    url,
    save_dir,
    index,
    total
):
    async with semaphore:
        print(f"[{index}/{total}] {url}")

        await crawl_one(
            browser,
            url,
            save_dir
        )

async def crawl_one(browser, url, save_dir):
    page = await browser.new_page()

    try:
        await page.goto(
            url,
            wait_until="networkidle",
            timeout=60000
        )

        await page.wait_for_timeout(2000)

        html = await page.content()

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        article = soup.find("article")

        if article is None:
            print("未找到article:", url)
            return

        h1 = article.find("h1")

        if h1 is None:
            print("未找到标题:", url)
            return

        title = h1.get_text(strip=True)

        md, formulas = article_to_markdown(article)

        filename = sanitize_filename(title) + ".md"

        (save_dir / filename).write_text(
            md,
            encoding="utf-8"
        )

        print(
            f"√ {title} 公式:{len(formulas)}"
        )

    except Exception as e:
        print("×", url, e)

    finally:
        await page.close()

async def main():

    urls = get_factor_urls()

    save_dir = Path("../bert_db/factors_md")
    save_dir.mkdir(exist_ok=True)

    semaphore = asyncio.Semaphore(
        CONCURRENT
    )

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        tasks = []

        total = len(urls)

        for i, url in enumerate(urls, 1):

            tasks.append(
                worker(
                    semaphore,
                    browser,
                    url,
                    save_dir,
                    i,
                    total
                )
            )

        await asyncio.gather(*tasks)

        await browser.close()

    print("全部完成")

if __name__ == "__main__":
    asyncio.run(main())