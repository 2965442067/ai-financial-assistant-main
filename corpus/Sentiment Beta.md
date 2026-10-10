# Sentiment Beta

情绪因子

## 因子公式

个股收益率与市场情绪指数回归模型：

$$
r\_i^t = \alpha\_i + \beta\_i \cdot (\frac{CSMS\_t}{CSMS\_{t-1}} - 1) + \epsilon\_i^t
$$

情绪敏感度因子计算公式：

$$
SentimentSensitivity = -1 \cdot |\beta\_i|
$$

公式中：

* $$
  r\_i^t
  $$

  :

  股票 i 在 t 日的日度收益率，计算方法通常为 (当日收盘价 - 前一日收盘价) / 前一日收盘价。
* $$
  CSMS\_t
  $$

  :

  t 日的市场情绪指数值，该指数可以由多个市场情绪指标合成，例如，换手率、成交量、涨跌停比例、舆情指数等。
* $$
  CSMS\_{t-1}
  $$

  :

  t-1 日的市场情绪指数值。
* $$
  \alpha\_i
  $$

  :

  股票 i 的回归截距项，代表在市场情绪指数不变的情况下，股票的预期收益。
* $$
  \beta\_i
  $$

  :

  股票 i 的情绪贝塔值，通过时序回归得到，衡量市场情绪指数变动对股票收益率的影响程度。正值表示市场情绪上升时股票收益率也倾向于上升，负值则表示相反。
* $$
  \epsilon\_i^t
  $$

  :

  回归模型的残差项，代表模型无法解释的股票 i 在 t 日的收益率部分。

## 因子解释

情绪敏感度因子通过时序回归模型衡量市场情绪变化对个股收益率的影响，并使用回归得到的 Beta 系数的绝对值取反作为最终的因子值。绝对值取反的目的是使得因子值与风险偏好保持一致，即值越小代表个股受市场情绪负面影响的可能性越大，风险越高，反之，因子值越大，则代表个股越不易受市场情绪的负面影响，风险越低。因此，该因子可用于量化投资中对风险进行预估和对股票进行选择。在实际应用中，可以考虑使用更长的回溯窗口（如60个交易日以上）进行时序回归，以提高模型稳定性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* (2021). Sentiment Beta: Risk or Alpha?. 量化投资与机器学习

## Related Factors

[### 隔夜新闻情感偏向因子](/zh/factors/emotion/overnight-news-sentiment)[### Fama-French三因子模型残差动量](/zh/factors/tech/residual-momentum-ff3)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 市场收益率协偏度因子](/zh/factors/tech/covariance-skewness1)[### 市场反应滞后因子](/zh/factors/tech/price-delay)[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 散户同步性因子](/zh/factors/emotion/herd-effect)[### 双向价格差分自相关性标准化因子](/zh/factors/tech/price-auto-correlation)