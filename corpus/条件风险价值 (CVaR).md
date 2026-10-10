# 条件风险价值 (CVaR)

波动率因子

## 因子公式

条件风险价值（基于VaR积分）公式:

$$
CVaR\_{\alpha} = \frac{1}{\alpha} \int\_{0}^{\alpha} VaR\_p(X) dp
$$

条件风险价值（基于条件期望）公式:

$$
CVaR\_{\alpha} = E[X | X \leq VaR\_{\alpha}]
$$

其中：

* $$
  \alpha
  $$

  :

  置信水平，表示我们关注损失超过VaR的概率，通常取值较高，如0.05、0.01等。例如，当 α = 0.05 时，表示在 5% 的最坏情况下，资产组合损失的平均期望值。注意，这里 α 通常表示的是损失尾部的概率，因此在公式中，α通常是较小的数值。
* $$
  VaR\_p(X)
  $$

  :

  在概率 p 下，资产组合 X 的风险价值 VaR。VaR\_p(X) 表示资产组合 X 的损失在概率 p 下的上限。 即在置信水平为 (1-p) 时，资产组合的最大损失额。
* $$
  X
  $$

  :

  资产组合的损失（或收益的负值），这里需要注意的是，损失通常定义为负值，所以当X小于等于VaR时，代表更大的损失
* $$
  E[X | X \leq VaR\_{\alpha}]
  $$

  :

  资产组合损失 X 在损失小于等于 VaR\_{\alpha} 时的条件期望。即在损失已经超出VaR\_{α} 的条件下，损失 X 的平均期望值。

## 因子解释

条件风险价值 (CVaR) 是在给定置信水平 α 下，当损失超过风险价值 (VaR) 时，损失的平均期望值。CVaR 能够更全面地度量风险，因为其不仅考虑了损失超出VaR的可能性，还考虑了超出VaR后的损失程度。与VaR 相比，CVaR 具有更好的数学特性，如次可加性，因此在风险管理和优化问题中更为有效。尤其在处理非正态分布和厚尾分布时，CVaR 相较于 VaR 更加稳健。CVaR 可以看作是 VaR 的一种补充，能够更有效地管理极端风险，为决策者提供更为全面的风险信息。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* R. T. Rockafellar, S. Uryasev. (2000). Optimization of conditional value-at-risk. Journal of Risk

## Related Factors

[### 风险价值 (Value at Risk - VaR)](/zh/factors/volatility/value-at-risk)[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### 下行风险贝塔](/zh/factors/tech/downside-beta)[### 下行/上行波动率比率](/zh/factors/volatility/up-down-volatility-ratio)[### 下尾风险贝塔](/zh/factors/tech/tail-beta)[### 估值偏离度(误差修正模型)](/zh/factors/tech/valuation-deviation)[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 盈余波动率因子 (Earnings Volatility Factor)](/zh/factors/basic-surface/earnings-predictability)[### 残差市值偏离度](/zh/factors/basic-surface/specific-market-capitalization)