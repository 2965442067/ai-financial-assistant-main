# 基于Fama-French三因子模型的残差动量

技术因子

## 因子公式

Fama-French 三因子模型:

$$
r\_{i,t} = \alpha\_{i} + \beta\_{1,i}RMRF\_{t} + \beta\_{2,i}SMB\_{t} + \beta\_{3,i}HML\_{t} + \epsilon\_{i,t}
$$

残差动量计算公式:

$$
residualmom\_{i,t} = \frac{\sum\_{t=T-12}^{T-2} \epsilon\_{i,t}}{\sqrt{\sum\_{t=T-12}^{T-2}(\epsilon\_{i,t} - \overline{\epsilon})^2}}
$$

其中：

* $$
  r\_{i,t}
  $$

  :

  资产i在t时刻的收益率。代表特定时间段内，资产i的价格变化幅度。
* $$
  \alpha\_{i}
  $$

  :

  资产i的截距项，表示在市场风险、规模和价值因子均为0时，资产i的预期收益率。该项反映了资产i的基准收益水平，也是一个衡量选股能力的重要指标。
* $$
  \beta\_{1,i}
  $$

  :

  资产i对市场风险溢价RMRF的敏感度（或称斜率系数）。表示市场风险溢价变动一个单位时，资产i收益率的预期变动幅度。也称为市场Beta，衡量了资产i的系统性风险暴露。
* $$
  \beta\_{2,i}
  $$

  :

  资产i对规模溢价SMB的敏感度。表示规模溢价变动一个单位时，资产i收益率的预期变动幅度。该值衡量了资产i受规模因子影响的程度。
* $$
  \beta\_{3,i}
  $$

  :

  资产i对价值溢价HML的敏感度。表示价值溢价变动一个单位时，资产i收益率的预期变动幅度。该值衡量了资产i受价值因子影响的程度。
* $$
  \epsilon\_{i,t}
  $$

  :

  资产i在t时刻的残差，即实际收益率与由Fama-French三因子模型预测的收益率之间的差异。该残差项代表了在市场、规模和价值因子影响之外，由公司特有信息驱动的收益部分，是残差动量因子的核心组成部分。
* $$
  \overline{\epsilon}
  $$

  :

  在计算动量窗口期（T-12至T-2）内，资产i残差的平均值。用于计算残差的标准差，从而实现残差动量的标准化。

## 因子解释

该因子基于行为金融学中的渐进信息扩散假说。该假说认为，市场信息，特别是公司特有信息，在投资者之间传播需要时间，并非瞬间完成。这导致投资者对这些信息的反应存在滞后性。通过Fama-French三因子模型剥离市场风险、规模和价值因素的影响，残差序列可以更纯粹地反映公司特有信息的价值效应。因此，如果过去一段时间残差表现较好，说明投资者可能尚未充分反应相关信息，在未来一段时间内，该股票仍然有持续上涨的可能性，反之亦然。此因子捕捉到的即是由公司特有信息驱动的，且未被市场充分定价的动量效应。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Blitz, David, Joop, Huij, and Martin Martens. (2011). Residual Momentum. Journal of Empirical Finance
* Blitz, D., M. X. Hanauer, and M. Vidojevic. (2020). The idiosyncratic momentum anomaly. International Review of Economics & Finance

## Related Factors

[### CAPM残差动量因子](/zh/factors/tech/residual-momentum-capm)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 残差市值偏离度](/zh/factors/basic-surface/specific-market-capitalization)[### 残差资金流强度](/zh/factors/tech/residual-fund-flow-intensity)[### 基本面趋势预期收益率](/zh/factors/basic-surface/fundamentals-implied-benefits)[### 多时域移动平均动量因子](/zh/factors/tech/trend-factor)[### 市场反应滞后因子](/zh/factors/tech/price-delay)[### 日内信息不对称强度因子](/zh/factors/tech/apm-factor)