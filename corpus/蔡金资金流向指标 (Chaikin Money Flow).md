# 蔡金资金流向指标 (Chaikin Money Flow)

技术因子

## 因子公式

计算每日的资金流量乘数（Money Flow Multiplier, MFM），又称每日资金流向强度系数，反映了当日收盘价在价格区间内的相对位置，并根据成交量加权。

$$
MFM = \frac{(CLOSE-LOW)-(HIGH-CLOSE)}{(HIGH-LOW)}
$$

计算每日资金流量量（Money Flow Volume, MFVOL），等于每日资金流量乘数(MFM)乘以当日成交量。

$$
MFVOL = MFM \* VOL
$$

计算N周期蔡金资金流向指标 (Chaikin Money Flow, CMF)，即N周期内的资金流量总和除以N周期内的成交量总和，并乘以100进行标准化。

$$
CMF(N) = \frac{\sum\_{i=1}^{N} MFVOL\_i}{\sum\_{i=1}^{N} VOL\_i} \* 100
$$

默认 N = 20，表示计算过去20个周期的资金流向。

* $CLOSE$

  :

  当日收盘价
* $LOW$

  :

  当日最低价
* $HIGH$

  :

  当日最高价
* $VOL$

  :

  当日成交量
* $MFM$

  :

  每日资金流量乘数
* $MFVOL$

  :

  每日资金流量量
* $N$

  :

  计算CMF的周期长度

## 因子解释

蔡金资金流向指标 (CMF) 通过量价关系衡量资金流入流出的强弱。其核心理念是，当价格收盘于当日价格区间的上半部分时，表示买方力量较强；反之，当价格收盘于当日价格区间的下半部分时，表示卖方力量较强。通过结合成交量，CMF 可以更好地反映市场参与者的真实交易行为和资金流向。具体来说，正的 CMF 值表示资金流入较强，可能预示着价格上涨的动力；而负的 CMF 值则表示资金流出较强，可能预示着价格下跌的压力。该指标通常用于辅助判断市场趋势、识别潜在的买入或卖出机会，以及验证其他技术指标的信号。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Marc Chaikin. (1992). The Chaikin Money Flow. Technical Analysis of the Financial Markets

## Related Factors

[### 资金流量指标](/zh/factors/tech/money-flow-index)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 资金流量累积指标 (Accumulation/Distribution Line, A/D)](/zh/factors/tech/accumulative-distribution-line)[### 钱德动量振荡器](/zh/factors/tech/chande-momentum-oscillator)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 经营性现金流市值比](/zh/factors/basic-surface/cash-flow-to-market-value)[### 开盘时段大单净额占比](/zh/factors/emotion/large-order-net-buy-ratio)[### 北向资金交易行为量化因子](/zh/factors/emotion/northbound-trading-factors)[### 陆股通净流入强度比率](/zh/factors/emotion/net-inflow-strength)