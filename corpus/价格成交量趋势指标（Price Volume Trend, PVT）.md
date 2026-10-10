# 价格成交量趋势指标（Price Volume Trend, PVT）

技术因子

## 因子公式

PVT:

$$
PVT\_t = PVT\_{t-1} + \frac{CLOSE\_t - CLOSE\_{t-1}}{CLOSE\_{t-1}} \times VOL\_t
$$

PVT 初始值:

$$
PVT\_1 = \frac{CLOSE\_1 - CLOSE\_0}{CLOSE\_0} \times VOL\_1
$$

该公式的核心思想是，根据当日价格变动幅度（与前一日收盘价相比）对当日成交量进行加权，然后累加到前一日的 PVT 值上。这样做的目的是捕捉价格变动幅度与成交量之间的关系，进而判断市场的潜在动能。

* $PVT\_t$

  :

  当日 (t) 的价格成交量趋势指标值。
* $PVT\_{t-1}$

  :

  前一日 (t-1) 的价格成交量趋势指标值。
* $CLOSE\_t$

  :

  当日 (t) 的收盘价。
* $CLOSE\_{t-1}$

  :

  前一日 (t-1) 的收盘价。
* $VOL\_t$

  :

  当日 (t) 的成交量。

## 因子解释

价格成交量趋势指标 (PVT) 通过将价格变动幅度与成交量相乘，从而更好地反映了成交量在价格上涨或下跌过程中的动态变化。相较于仅累加成交量的 OBV 指标，PVT 更能体现价格变动对成交量累加的加权影响。具体而言，当收盘价上涨时，成交量会根据涨幅大小被加权，涨幅越大，则累加到 PVT 的成交量越多；反之亦然。因此，PVT 可以更准确地揭示市场参与者在不同价格水平下的活跃程度，以及潜在的市场趋势和动能。PVT 的上升可能暗示市场处于累积阶段，而 PVT 的下降可能暗示市场处于派发阶段。通过观察 PVT 的走势，投资者可以尝试识别市场中的买卖压力，以及价格趋势可能发生的变化。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance
* Thomas N. Bulkowski. (2005). Encyclopedia of Chart Patterns. John Wiley & Sons

## Related Factors

[### 成交量能量潮指标 (On-Balance Volume)](/zh/factors/tech/energy-metrics)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 高频价量相关性趋势因子](/zh/factors/tech/price-volume-correlation-trend)[### 成交额变异系数](/zh/factors/volatility/volatility-coefficient-of-turnover)[### 实体K线一致性买入强度因子](/zh/factors/tech/consistent-buy-transaction)[### 尾盘成交量比率因子](/zh/factors/emotion/tail-volume-ratio)