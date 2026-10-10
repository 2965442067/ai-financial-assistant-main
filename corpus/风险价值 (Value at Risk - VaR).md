# 风险价值 (Value at Risk - VaR)

波动率因子

## 因子公式

在给定置信水平 α 下，资产组合损失超过 VaR 的概率为 (1 - α):

$$
P(\Delta P < -VaR) = 1 - \alpha
$$

公式中：

* $\Delta P$

  :

  代表在特定持有期 (\Delta t) 内，金融资产或投资组合价值的变动量 (收益或损失)。 (\Delta P) 为负值表示损失，正值表示收益。
* $VaR$

  :

  表示在给定的置信水平 ( \alpha ) 下，资产组合在持有期 (\Delta t) 内可能遭受的最大损失金额。这是一个绝对值，表示损失的上限。
* $\alpha$

  :

  代表置信水平，表示我们对 VaR 预测准确性的信心程度。通常情况下，( \alpha ) 的取值范围在 90% 到 99% 之间，常见的取值为 95% 或 99%。例如，如果 ( \alpha = 95% )，则表示在 100 个持有期中，我们预期只有 5 个持有期的损失会超过 VaR 值。

## 因子解释

风险价值 (VaR) 是一种衡量市场风险的工具，它量化了在给定置信水平 (( \alpha ) ) 下，金融资产或投资组合在特定持有期 (( \Delta t) ) 内可能出现的最大损失。更具体地说，VaR 回答了这样一个问题：在未来一段时间内，我们有多大概率（1 - α）会损失超过多少金额？例如，一个95%置信水平下的100万元VaR意味着，在未来一段时间内，我们有95%的把握不会损失超过100万元，但也意味着有5%的概率会损失超过100万元。VaR 模型的计算通常需要考虑资产收益率的分布，例如，可以通过历史数据模拟、蒙特卡洛模拟或参数化方法（如正态分布假设）来估算。值得注意的是，VaR 是一种尾部风险度量，它关注的是损失分布的尾部，而没有描述超过 VaR 的损失大小。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* G30, G. D. S. G.. (1993). Derivatives: Practices and Principles

## Related Factors

[### 条件风险价值 (CVaR)](/zh/factors/volatility/conditional-value-at-risk)[### 下尾风险贝塔](/zh/factors/tech/tail-beta)[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### 下行/上行波动率比率](/zh/factors/volatility/up-down-volatility-ratio)[### 平均真实波幅 (Average True Range, ATR)](/zh/factors/tech/average-true-volatility)[### 下行风险贝塔](/zh/factors/tech/downside-beta)[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)[### 盈余波动率因子 (Earnings Volatility Factor)](/zh/factors/basic-surface/earnings-predictability)