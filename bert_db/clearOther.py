import re
from pathlib import Path


def remove_risk_warning(content: str) -> str:
    """
    删除从 '⚠️ 因子风险警告' 开始，到其后的三行内容（即整个风险声明段落）
    匹配格式：
    ⚠️ 因子风险警告
    本量化因子仅供教育和研究目的使用。历史表现不保证未来收益。用户须独立验证并承担所有风险。
    """
    # 匹配警告符号行 + 紧接着的一行说明文本（可能跨行，但示例中是两行）
    # 使用 DOTALL 让 . 匹配换行，匹配两行内容
    pattern = r'⚠️ 因子风险警告\s*\n\s*本量化因子仅供教育和研究目的使用。历史表现不保证未来收益。用户须独立验证并承担所有风险。\s*\n?'
    result = re.sub(pattern, '', content, flags=re.DOTALL)
    # 清理可能产生的多余空行
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result


def process_file(file_path: Path, dry_run: bool = False):
    original = file_path.read_text(encoding='utf-8')
    modified = remove_risk_warning(original)

    if modified == original:
        print(f"跳过（无变化）: {file_path.name}")
        return

    if dry_run:
        print(f"\n--- 预览修改: {file_path.name} ---")
        print("原文件中风险警告附近的内容:")
        # 找到原文件中包含警告的部分并打印
        match = re.search(r'⚠️ 因子风险警告.*?用户须独立验证并承担所有风险。', original, re.DOTALL)
        if match:
            print(match.group(0))
        print("\n修改后该位置变为空，相关因子部分保留。")
    else:
        file_path.write_text(modified, encoding='utf-8')
        print(f"已更新: {file_path.name}")


def batch_remove(directory: str = ".", dry_run: bool = False):
    md_files = Path(directory).glob("*.md")
    for md_file in md_files:
        process_file(md_file, dry_run)


if __name__ == "__main__":
    import sys

    dry = "--dry-run" in sys.argv
    target_dir = "../corpus"
    if len(sys.argv) > 1 and sys.argv[1] != "--dry-run":
        target_dir = sys.argv[1]
    batch_remove(target_dir, dry_run=dry)