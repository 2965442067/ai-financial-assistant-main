# 最小收益率 (MinReturn)

动量因子

## 因子公式

MinReturn = -min(R\_t, R\_{t-1}, ..., R\_{t-K+1})

$$
MinReturn = - \min(R\_t, R\_{t-1}, ..., R\_{t-K+1})
$$

该公式计算的是过去K个月每日收益率序列的最小值，并取负数。取负数是为了让最小收益率的值越大，代表的极端负向风险越小，使得因子含义更直观。

* $MinReturn$

  :

  最小收益率因子
* $R\_t$

  :

  第t日的资产收益率
* $K$

  :

  回溯窗口期，代表过去K个月，通常以自然月为单位，例如3个月，6个月，12个月等
* $min()$

  :

  取最小值函数

## 因子解释

最小收益率因子旨在捕捉资产在过去K个月内的最差表现，它与传统的波动率指标不同，侧重于极端负向收益的风险。研究表明，最小收益率较高的资产可能意味着其尾部风险较低，即在不利市场条件下遭受极端损失的可能性较小。 该因子可以被视为投资者对极端风险偏好的一个代理指标。投资者往往会为承担极端负向收益风险的资产要求更高的预期回报，而最小收益率较高的资产可能具有较低的预期回报。因此，最小收益率可以用于构建风险调整后的投资组合，以更好地适应投资者的风险偏好。此外，此因子在风险管理中也具有应用价值，可以通过对最小收益率的监控来及时识别可能面临极端风险的资产。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Bali, Turan G., Nusret Cakici, and Robert F. Whitelaw. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. Journal of Financial Economics

## Related Factors

[### 最大日收益率（Max Daily Return）](/zh/factors/tech/max-yield)[### 尾部非对称概率差](/zh/factors/emotion/tail-probability-E)[### 负收益成交额加权非流动性因子](/zh/factors/emotion/negative-return-illiquidity)[### 滚动收益率偏度因子](/zh/factors/tech/skewness)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)[### 系统偏度风险溢价因子](/zh/factors/emotion/covariance-skewness2)[### 下行风险贝塔](/zh/factors/tech/downside-beta)[### 特异性收益波动因子](/zh/factors/emotion/specificity)