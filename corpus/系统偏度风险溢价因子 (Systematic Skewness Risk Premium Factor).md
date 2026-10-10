# 系统偏度风险溢价因子 (Systematic Skewness Risk Premium Factor)

情绪因子

## 因子公式

系统偏度风险溢价因子公式:

$$
CS = \frac{E[\epsilon\_i \epsilon\_m^2]}{\sqrt{E[\epsilon\_i^2]E[\epsilon\_m^2]}}
$$

其中:

* $$
  \epsilon\_i
  $$

  :

  为过去 K 个月内，股票 i 的日度超额收益对市场日度超额收益进行线性回归后的残差项。这个残差项代表了股票 i 收益中无法被市场收益解释的部分，即股票 i 特有的收益波动。
* $$
  \epsilon\_m
  $$

  :

  为同一时期内，通过均值中心化后的市场日度超额收益。计算方法为：$\epsilon\_m = r\_m - \bar{r\_m}$，其中 $r\_m$ 为市场日度超额收益，$\bar{r\_m}$ 为过去 K 个月市场日度超额收益的平均值。 中心化处理确保了市场的波动围绕均值展开。
* $K$

  :

  为回溯期长度，单位为月。常用的 K 值包括 1、6 和 12。为保证计算结果的稳健性，计算窗口内至少需要 15 个有效的日度收益率数据。
* $E[.]$

  :

  期望值或平均值运算符，表示对时间序列数据进行平均计算。 例如 E[$\epsilon\_i \epsilon\_m^2$]表示过去K个月内，股票i的日度残差与市场日度残差平方的乘积的平均值。

## 因子解释

该因子衡量股票收益相对于市场收益的系统性偏度风险。其背后的逻辑是，投资者普遍厌恶负偏度的资产，即收益分布左偏的资产，因为这类资产可能会带来更高的损失风险。因此，低系统偏度的股票，由于负偏度风险较小，可能会有较高的溢价，从而产生超额收益。动量效应与这种系统偏度风险紧密相关。低预期回报的动量组合往往负偏度较高，这可以解释为什么高动量股票通常比低动量股票表现更差。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Harvey, Campbell R., and Akhtar Siddique. (2000). Conditional skewness in asset pricing tests. Journal of Finance

## Related Factors

[### 市场收益率协偏度因子](/zh/factors/tech/covariance-skewness1)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 滚动收益率偏度因子](/zh/factors/tech/skewness)[### 非对称价格冲击偏度](/zh/factors/tech/price-impact-bias)[### 负收益偏度系数](/zh/factors/emotion/negative-skewness-coefficient)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)[### 月度收益季节性动量因子](/zh/factors/emotion/seasonal-returns)[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### 异常尾部不对称度](/zh/factors/emotion/abnormal-tail-probability)