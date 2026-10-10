# 下行风险贝塔 (Downside Beta)

技术因子

## 因子公式

下行风险贝塔：

$$
\beta^{-} = \frac{Cov(r\_i, r\_m | r\_m < \mu\_m)}{Var(r\_m | r\_m < \mu\_m)}
$$

其中：

* $$
  r\_i
  $$

  :

  股票 *i* 在过去 *K* 个月内的月度收益率序列。月度收益率由该月每日收益率复合计算得到。
* $$
  r\_m
  $$

  :

  市场指数（例如沪深300或标普500）在过去 *K* 个月内的月度收益率序列。月度收益率由该月每日收益率复合计算得到。
* $$
  \mu\_m
  $$

  :

  市场指数在过去 *K* 个月内每日收益率的算术平均值，用于区分市场上涨和下跌的边界。
* $$
  K
  $$

  :

  回溯计算下行风险贝塔的时间窗口，通常设置为12个月。为保证计算的稳健性，时间窗口内的交易日数量应不少于50个。
* $$
  Cov(r\_i, r\_m | r\_m < \mu\_m)
  $$

  :

  在市场月度收益率小于其过去 *K* 个月每日收益率均值 $\mu\_m$ 的前提下，股票 *i* 的月度收益率与市场月度收益率的协方差。这代表了市场下跌时股票和市场收益率的联动性。
* $$
  Var(r\_m | r\_m < \mu\_m)
  $$

  :

  在市场月度收益率小于其过去 *K* 个月每日收益率均值 $\mu\_m$ 的前提下，市场月度收益率的方差。这代表了市场下跌时的波动程度。

## 因子解释

下行风险贝塔着重于衡量市场下跌时，个股收益率对市场收益率的敏感度，它比传统贝塔更能捕捉投资者关注的下行风险。具体而言，它计算的是在市场月度收益率小于其历史日均收益率的条件下，个股月度收益率与市场月度收益率之间的协方差，并除以市场月度收益率的方差。通过剔除市场上涨的月份，下行风险贝塔能够更准确地反映股票在市场下行时的系统性风险暴露。因此，该因子通常被用于构建风险管理和对冲策略，并已被实证研究证实具有显著的下行风险溢价。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Ang, A., Chen, J., & Xing, Y.. (2006). Downside risk. Review of Financial Studies

## Related Factors

[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### 下尾风险贝塔](/zh/factors/tech/tail-beta)[### 市场收益率协偏度因子](/zh/factors/tech/covariance-skewness1)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)[### Frazzini-Pedersen 调整贝塔](/zh/factors/volatility/frazzini-pedersen-beta)[### 下行/上行波动率比率](/zh/factors/volatility/up-down-volatility-ratio)[### 系统偏度风险溢价因子](/zh/factors/emotion/covariance-skewness2)[### 个股特质波动率](/zh/factors/volatility/idiosyncratic-volatility)[### 特异性收益波动因子](/zh/factors/emotion/specificity)