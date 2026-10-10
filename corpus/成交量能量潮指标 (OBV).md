# 成交量能量潮指标 (OBV)

技术因子

## 因子公式

OBV 计算公式:

$$
OBV\_t = OBV\_{t-1} + \begin{cases} VOL\_t & \text{if } CLOSE\_t > CLOSE\_{t-1} \\ -VOL\_t & \text{if } CLOSE\_t < CLOSE\_{t-1} \\ 0 & \text{if } CLOSE\_t = CLOSE\_{t-1} \end{cases}
$$

OBV 初始值:

$$
OBV\_0 = 0
$$

该公式基于当前和前一交易日的收盘价 (CLOSE) 以及当前交易日的成交量 (VOL) 来计算 OBV。当当前收盘价高于前一收盘价时，将当前成交量加到前一期的 OBV 值上；当当前收盘价低于前一收盘价时，则将当前成交量从前一期的 OBV 值中扣除；当当前收盘价等于前一收盘价时，OBV 值保持不变。

* $OBV\_t$

  :

  当前交易日的 OBV 值
* $OBV\_{t-1}$

  :

  前一交易日的 OBV 值
* $VOL\_t$

  :

  当前交易日的成交量
* $CLOSE\_t$

  :

  当前交易日的收盘价
* $CLOSE\_{t-1}$

  :

  前一交易日的收盘价

## 因子解释

成交量能量潮指标 (OBV) 的核心理念是，成交量是价格变动的先行指标，因此通过累积成交量可以反映市场资金的动能。如果价格上升并且伴随OBV的上升，则认为上涨趋势可靠。相反，如果价格上涨但OBV下降，则可能预示着上涨动能不足，存在潜在的反转风险。OBV 可以帮助投资者识别市场趋势的强弱，以及发现价格与成交量之间的背离，从而辅助判断潜在的买卖时机。该指标适用于不同时间周期，可用于股票、期货、外汇等多种金融资产的分析。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance

## Related Factors

[### 价格成交量趋势指标](/zh/factors/tech/price-volume-trend)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 克林格成交量震荡指标](/zh/factors/tech/klinger-volume-oscillator)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)[### 实体K线一致性买入强度因子](/zh/factors/tech/consistent-buy-transaction)[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 成交额变异系数](/zh/factors/volatility/volatility-coefficient-of-turnover)[### 集合竞价成交量占比复合因子](/zh/factors/tech/volume-ratio)