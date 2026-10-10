# 标准化意外盈余 (Standardized Unexpected Earnings, SUE)

基础面因子

## 因子公式

标准化意外盈余 (SUE) =

$$
\frac{UE\_t}{std(UE\_{t-7}, ..., UE\_t)}
$$

盈余意外值 (UE) =

$$
EPS\_t - EPS\_{t,expected}
$$

其中：

* $SUE$

  :

  标准化意外盈余（Standardized Unexpected Earnings）。
* $UE\_t$

  :

  当前第t季度的盈余意外值（Unexpected Earnings），即实际每股收益与市场预期每股收益之差。
* $std(UE\_{t-7}, ..., UE\_t)$

  :

  过去八个季度（包括当前季度）的盈余意外值 (UE) 的标准差，用于衡量公司盈利预测偏差的波动程度。
* $EPS\_t$

  :

  当前第t季度的实际每股收益 (Earnings Per Share).
* $EPS\_{t,expected}$

  :

  当前第t季度的市场预期每股收益 (Expected Earnings Per Share).

## 因子解释

标准化意外盈余（SUE）是衡量盈余公告后价格漂移效应（Post-Earnings Announcement Drift, PEAD）的经典指标。该效应是指，当公司实际盈利显著高于（或低于）市场预期盈利时，在盈余公告发布后的一段时间内（通常为3-6个月），其股票价格会持续出现正向（或负向）的超额回报。SUE可以用于识别这种盈余意外带来的投资机会，高SUE值通常预示着股票价格的潜在上行空间，反之亦然。需要注意的是，SUE的有效性可能受到市场情绪、行业特性以及公司具体情况等多种因素的影响，不宜作为单一投资决策依据。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Foster, George, Chris Olsen, and Terry Shevlin. (1984). Earnings releases, anomalies, and the behavior of security returns. Accounting Review

## Related Factors

[### 标准化季度营收意外](/zh/factors/emotion/standardized-unexpected-revenue)[### 标准化盈利超预期因子](/zh/factors/basic-surface/earning-surprise)[### 盈余公告超额收益率](/zh/factors/emotion/earnings-announcement-return)[### 每股盈余公积金](/zh/factors/basic-surface/surplus-reserve-per-share)[### 预期市盈率调整幅度](/zh/factors/growth/pe-adjustment)[### 分析师一致预期EPS修正比率](/zh/factors/emotion/eps-revision-ratio)[### 分析师预期EPS调整幅度](/zh/factors/emotion/expected-eps-adjustment)[### 每股留存收益](/zh/factors/value/value-retained-earnings-per-share)[### 盈余波动率因子 (Earnings Volatility Factor)](/zh/factors/basic-surface/earnings-predictability)