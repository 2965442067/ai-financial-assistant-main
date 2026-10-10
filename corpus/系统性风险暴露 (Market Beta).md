# 系统性风险暴露 (Market Beta)

波动率因子

## 因子公式

Beta 系数计算公式:

$$
\beta\_i = \frac{cov (r\_i, r\_m)}{var (r\_m)}
$$

CAPM 模型:

$$
E(r\_i) = r\_f + \beta\_i (E(r\_m) - r\_f)
$$

其中：

* $$
  r\_i
  $$

  :

  股票i在过去K个月的月度收益率，计算公式为：$r\_{i,t} = (P\_{i,t} - P\_{i,t-1})/P\_{i,t-1}$，其中$P\_{i,t}$为股票i在t月末的收盘价。
* $$
  r\_m
  $$

  :

  市场在过去K个月的月度收益率，通常使用市场指数（如沪深300指数，标普500指数等）的收益率作为代理。计算公式为：$r\_{m,t} = (I\_{t} - I\_{t-1})/I\_{t-1}$，其中$I\_{t}$为市场指数在t月末的收盘价。
* $$
  E(r\_i)
  $$

  :

  股票i的预期收益率。
* $$
  E(r\_m)
  $$

  :

  市场组合的预期收益率。
* $$
  r\_f
  $$

  :

  无风险利率，通常使用短期国债收益率作为代理。例如，可以使用同期国债的年化到期收益率，然后将其换算为月度收益率。
* $$
  cov(r\_i, r\_m)
  $$

  :

  股票i的月度收益率$r\_i$和市场月度收益率$r\_m$的协方差，衡量两者的同向变动关系强度。
* $$
  var(r\_m)
  $$

  :

  市场月度收益率$r\_m$的方差，衡量市场收益率的波动程度。

## 因子解释

系统性风险暴露 (市场Beta) 反映了个股收益率对市场整体收益率波动的敏感性，是衡量股票系统性风险的重要指标。Beta值大于1的股票，其收益率波动幅度通常大于市场平均水平，属于高风险高收益类型；Beta值小于1的股票，其收益率波动幅度通常小于市场平均水平，属于低风险低收益类型；Beta值等于1的股票，其收益率波动幅度与市场平均水平一致。 CAPM模型假设，市场Beta与股票的预期收益率呈正相关关系，即Beta值越高，股票的预期收益率也越高，反之亦然。在实际应用中，可以通过滚动计算的方式，动态跟踪股票的Beta值变化。需要注意的是，CAPM模型是理论模型，实际市场中可能存在各种因素影响，例如，个股的特质风险，投资者情绪等等，使得实际收益率与CAPM模型预测值存在偏差。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Fama, Eugene F., and James D. MacBeth. (1973). Risk, return, and equilibrium: Empirical tests. Journal of Political Economy

## Related Factors

[### 下行风险贝塔](/zh/factors/tech/downside-beta)[### 下尾风险贝塔](/zh/factors/tech/tail-beta)[### Frazzini-Pedersen 调整贝塔](/zh/factors/volatility/frazzini-pedersen-beta)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 系统偏度风险溢价因子](/zh/factors/emotion/covariance-skewness2)[### 个股特质波动率](/zh/factors/volatility/idiosyncratic-volatility)[### 市场收益率协偏度因子](/zh/factors/tech/covariance-skewness1)[### Dimson调整贝塔](/zh/factors/tech/dimson-beta)