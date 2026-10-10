# 垂直水平滤波指标 (Vertical Horizontal Filter, VHF)

技术因子

## 因子公式

最高价区间的最高价 (Highest Close Price, HCP):

$$
HCP = MAX(HIGH\_i, ..., HIGH\_{i-N+1})
$$

在过去N个周期内，最高价(HIGH)的最大值。该值代表了价格在给定时间段内向上波动的上界。

最低价区间的最低价 (Lowest Close Price, LCP):

$$
LCP = MIN(LOW\_i, ..., LOW\_{i-N+1})
$$

在过去N个周期内，最低价(LOW)的最小值。该值代表了价格在给定时间段内向下波动的下界。

价格区间总波动幅度 (Absolute Price Range, A):

$$
A = |HCP - LCP|
$$

最高价区间的最高价（HCP）与最低价区间的最低价（LCP）的绝对差值。该值衡量了在指定周期内价格的最大垂直波动幅度，即价格区间的总宽度。

价格变动总和 (Price Summation, B):

$$
B = \sum\_{i=1}^{N} |CLOSE\_i - CLOSE\_{i-1}|
$$

在过去N个周期内，每日收盘价(CLOSE)与前一日收盘价之差的绝对值之和。该值衡量了在指定周期内价格的水平变动幅度，即所有价格变化的总和。

垂直水平滤波指标 (Vertical Horizontal Filter, VHF):

$$
VHF = \frac{A}{B}
$$

价格区间总波动幅度（A）与价格变动总和（B）的比率。该值反映了价格波动的主导方向，即是趋势性还是震荡性。VHF值越高，表明价格波动的垂直分量较大，更倾向于趋势性行情；VHF值越低，表明价格波动的水平分量较大，更倾向于震荡行情。

若分母为零则设为零:

$$
若 B = 0, 则 VHF = 0
$$

为避免分母为零的情况，当价格变动总和（B）为0时，将VHF值设为0。

默认周期 (Default Period, N):

$$
默认: N = 20
$$

VHF 计算所使用的默认周期，即计算HCP、LCP、A 和 B 所参考的时间窗口。N 的值通常取 20，但可以根据不同的市场或交易策略进行调整。较小的 N 值会使 VHF 对价格的短期变化更加敏感，较大的 N 值会使 VHF 对价格的长期趋势更加敏感。

VHF 指标通过比较价格在指定周期内的垂直波动幅度与水平波动幅度来判断当前市场的状态。当价格波动倾向于垂直方向时，VHF 值会增大，表明市场处于趋势性行情。当价格波动倾向于水平方向时，VHF 值会减小，表明市场处于震荡行情。因此，该指标可以辅助投资者选择合适的交易策略和技术指标。

## 因子解释

垂直水平滤波指标（VHF）是一种用来判断市场是处于趋势阶段还是震荡阶段的技术指标。它通过比较价格的垂直方向波动（价格区间）与水平方向波动（价格变化的总和）的比率来完成判断。与传统趋势指标（如MACD）和震荡指标（如RSI）不同，VHF 的优势在于它能够根据市场的不同阶段，帮助投资者选择合适的指标。当VHF值较高时，表明市场趋势性较强，适合使用趋势跟踪指标；当VHF值较低时，表明市场波动较为震荡，适合使用震荡指标。因此，VHF 可以作为一个有效的市场状态过滤器，提升交易策略的鲁棒性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 常规通用技术指标

## Related Factors

[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 佳庆波动率离散指标](/zh/factors/tech/jiaqing-discrete-index)[### 价格成交量趋势指标](/zh/factors/tech/price-volume-trend)[### 蔡金资金流向指标](/zh/factors/tech/caijin-currency-flow-indicator)[### 区域强度指数](/zh/factors/tech/region-index)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 资金流量指标](/zh/factors/tech/money-flow-index)