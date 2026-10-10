# 成交量相对强度指标 (Volume Relative Strength Index)

技术因子

## 因子公式

U (当日向上成交量):

$$
U\_t = \begin{cases} V\_t & \text{if } P\_t > P\_{t-1} \\ V\_t / 2 & \text{if } P\_t = P\_{t-1} \\ 0 & \text{if } P\_t < P\_{t-1} \end{cases}
$$

当日向上成交量。如果当日收盘价高于前一日，则当日成交量计为向上成交量；如果相等，则计为一半；如果低于前一日，则计为0。 其中，$V\_t$ 代表当日成交量，$P\_t$ 代表当日收盘价，$P\_{t-1}$代表前一日收盘价。

D (当日向下成交量):

$$
D\_t = \begin{cases} V\_t & \text{if } P\_t < P\_{t-1} \\ V\_t / 2 & \text{if } P\_t = P\_{t-1} \\ 0 & \text{if } P\_t > P\_{t-1} \end{cases}
$$

当日向下成交量。如果当日收盘价低于前一日，则当日成交量计为向下成交量；如果相等，则计为一半；如果高于前一日，则计为0。 其中，$V\_t$ 代表当日成交量，$P\_t$ 代表当日收盘价，$P\_{t-1}$代表前一日收盘价。

UU (向上成交量平均值):

$$
UU\_t = \frac{(N-1) \times UU\_{t-1} + U\_t}{N}
$$

向上成交量的指数移动平均值(EMA)。其中，N 为计算周期，通常设置为20。$UU\_{t-1}$ 代表前一日的向上成交量平均值，$U\_t$ 代表当日的向上成交量。

DD (向下成交量平均值):

$$
DD\_t = \frac{(N-1) \times DD\_{t-1} + D\_t}{N}
$$

向下成交量的指数移动平均值(EMA)。其中，N 为计算周期，通常设置为20。$DD\_{t-1}$ 代表前一日的向下成交量平均值，$D\_t$ 代表当日的向下成交量。

VRSI (成交量相对强度指标):

$$
VRSI\_t = 100 \times \frac{UU\_t}{UU\_t + DD\_t}
$$

成交量相对强度指标，表示向上成交量平均值在总成交量平均值中的占比，以百分比形式呈现。$UU\_t$ 代表当日的向上成交量平均值，$DD\_t$ 代表当日的向下成交量平均值。

参数说明:

* $N$

  :

  计算VRSI的周期长度，通常设置为20。该参数决定了指标的敏感程度，较小的N值会使指标更敏感，较大的N值则会使指标更平滑。
* $V\_t$

  :

  t日的成交量。
* $P\_t$

  :

  t日的收盘价格。
* $P\_{t-1}$

  :

  t-1日的收盘价格。

## 因子解释

成交量相对强度指标 (VRSI) 是一种用于衡量市场成交量动能的技术指标。它通过计算一段时间内向上成交量平均值与总成交量平均值的比率，来反映市场买卖力量的相对强弱。VRSI 的高低可以辅助投资者判断市场趋势，识别潜在的超买或超卖区域。一般来说，当VRSI较高时，表明市场向上成交量较强，可能预示着价格上涨的动能；当VRSI较低时，表明市场向下成交量较强，可能预示着价格下跌的动能。该指标的优点在于它能够将成交量信息与价格变动相结合，从而更准确地反映市场参与者的交易行为，避免了单纯依赖价格变动带来的误判。需要注意的是，VRSI 并非万能指标，应结合其他技术指标和基本面分析进行综合判断，以提高交易决策的准确性。尤其要注意避免将 VRSI 指标单独使用，应结合其他指标和市场背景进行综合分析。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). 技术分析指标大全. Prentice Hall

## Related Factors

[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 区域强度指数](/zh/factors/tech/region-index)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 价格成交量趋势指标](/zh/factors/tech/price-volume-trend)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)[### 成交量能量潮指标 (On-Balance Volume)](/zh/factors/tech/energy-metrics)