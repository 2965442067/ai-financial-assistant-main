# 成交量相对强度指标（Volume Ratio, VR）

技术因子

## 因子公式

上涨成交量（A）计算公式：

$$
A = \begin{cases} VOL & \text{if } CLOSE > CLOSE[1] \\ 0 & \text{otherwise} \end{cases}
$$

下跌成交量（B）计算公式：

$$
B = \begin{cases} VOL & \text{if } CLOSE < CLOSE[1] \\ 0 & \text{otherwise} \end{cases}
$$

成交量相对强度指标（VR）计算公式：

$$
VR = \frac{\sum\_{i=1}^{N} A\_i}{\sum\_{i=1}^{N} B\_i} \times 100
$$

其中:

* $CLOSE$

  :

  当日收盘价：表示当前交易日结束时的股票价格。
* $CLOSE[1]$

  :

  前一日收盘价：表示前一个交易日结束时的股票价格。用于比较当日收盘价的变化方向。
* $VOL$

  :

  当日成交量：表示当前交易日内完成的股票交易总手数或总股数，是衡量市场活跃度的重要指标。
* $A\_i$

  :

  第i个交易日的上涨成交量：当天的收盘价高于前一天的收盘价时，A\_i等于当天的成交量，否则为0。
* $B\_i$

  :

  第i个交易日的下跌成交量：当天的收盘价低于前一天的收盘价时，B\_i等于当天的成交量，否则为0。
* $\sum\_{i=1}^{N} X\_i$

  :

  X值在N个周期内的总和：表示对X值在过去N个交易日内的数值进行累加求和。
* $N$

  :

  计算周期：表示计算VR指标时所使用的历史交易日数量。默认值为20，可以根据不同的交易策略和市场情况进行调整。较短的周期通常对价格变动更敏感，而较长的周期则更平滑，能减少噪音。

## 因子解释

成交量相对强度指标（VR）通过比较N个周期内股价上涨日的成交量总和与股价下跌日的成交量总和的比率，来衡量市场买卖双方力量的对比。当VR值较高时，表明市场买方力量较强，股价可能处于超买状态，反之，当VR值较低时，表明市场卖方力量较强，股价可能处于超卖状态。投资者可以通过VR指标的变化辅助判断市场的潜在趋势，并结合其他技术指标和基本面分析来制定更有效的交易策略。该指标尤其适用于中期趋势分析，帮助投资者识别股票的潜在买入和卖出时机。需要注意的是，成交量数据本身存在一定噪音，使用时需要结合其他分析手段进行验证。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 佚名. (2023). 常用技术分析指标详解. 金融技术分析教程

## Related Factors

[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 区域强度指数](/zh/factors/tech/region-index)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 个股相对点击量因子](/zh/factors/emotion/stock-click-ratio)[### 实体K线一致性买入强度因子](/zh/factors/tech/consistent-buy-transaction)[### 价格成交量趋势指标](/zh/factors/tech/price-volume-trend)