# 动态趋向指标 (Dynamic Trend Momentum Indicator, DTMI)

技术因子

## 因子公式

DTM:

$$
DTM = \begin{cases} 0 & OPEN < OPEN[1] \\ \max(HIGH - OPEN, OPEN - OPEN[1]) & OPEN \geq OPEN[1] \end{cases}
$$

DBM:

$$
DBM = \begin{cases} 0 & OPEN \geq OPEN[1] \\ \max(OPEN - LOW, OPEN[1] - OPEN) & OPEN < OPEN[1] \end{cases}
$$

STM:

$$
STM = \sum\_{i=0}^{N-1} DTM\_i
$$

SBM:

$$
SBM = \sum\_{i=0}^{N-1} DBM\_i
$$

DTMI:

$$
DTMI = \begin{cases} \frac{STM - SBM}{STM} & STM > SBM \\ 0 & STM = SBM \\ \frac{STM - SBM}{SBM} & STM < SBM \end{cases}
$$

DTMIMA:

$$
DTMIMA = SMA(DTMI, M)
$$

其中：

* $$
  OPEN
  $$

  :

  当日开盘价。该价格反映了市场对该股票在当日开盘时的初始估值。
* $$
  OPEN[1]
  $$

  :

  前一日的开盘价。该价格作为基准，用于比较当日开盘价的波动方向。
* $$
  HIGH
  $$

  :

  当日最高价。该价格反映了当日市场情绪推动下，股票达到的最高成交价格。
* $$
  LOW
  $$

  :

  当日最低价。该价格反映了当日市场情绪推动下，股票达到的最低成交价格。
* $$
  DTM
  $$

  :

  当日向上动能。若当日开盘价低于前一日开盘价，则DTM为0；否则，取当日最高价与开盘价之差或当日开盘价与前一日开盘价之差的最大值，表示当日向上波动的最大幅度。
* $$
  DBM
  $$

  :

  当日向下动能。若当日开盘价高于等于前一日开盘价，则DBM为0；否则，取当日开盘价与最低价之差或前一日开盘价与当日开盘价之差的最大值，表示当日向下波动的最大幅度。
* $$
  STM
  $$

  :

  过去N个交易日DTM的总和，表示一段时间内的向上动能累计。
* $$
  SBM
  $$

  :

  过去N个交易日DBM的总和，表示一段时间内的向下动能累计。
* $$
  N
  $$

  :

  计算STM和SBM的窗口大小，表示累计动能的时间周期。默认值为23，通常可根据不同交易周期和策略进行调整。N值越大，指标的敏感度越低，反之则越高。
* $$
  DTMI
  $$

  :

  动态趋向指标。表示多空力量的相对强弱。当STM大于SBM时，DTMI为多头力量占比；当STM小于SBM时，DTMI为空头力量占比；当STM等于SBM时，DTMI为0，表示多空平衡。
* $$
  M
  $$

  :

  计算DTMIMA的窗口大小，表示移动平均线平滑的周期。默认值为8，通常可根据不同交易周期和策略进行调整。M值越大，移动平均线越平滑，对价格波动不敏感。
* $$
  DTMIMA
  $$

  :

  DTMI的简单移动平均线。通过对DTMI进行平滑处理，可以降低其波动性，从而更清晰地反映趋势方向。

## 因子解释

动态趋向指标(DTMI)通过对比开盘价的向上波动幅度与向下波动幅度，来衡量市场情绪和买卖压力。指标的核心在于使用当日开盘价与前一日开盘价的相对位置及当日最高价、最低价来计算多空动能，并据此构建买卖信号。DTMI的取值范围在-1到+1之间，数值越接近+1表示市场做多情绪越强，越接近-1表示市场做空情绪越强。当DTMI低于-0.5时，可视为低风险区域，表明市场可能处于超卖状态，未来上涨的可能性较高；当DTMI高于+0.5时，可视为高风险区域，表明市场可能处于超买状态，未来下跌的可能性较高。交易策略上，当DTMI线向上突破其移动平均线(DTMIMA)时，视为买入信号，表明市场买盘力量增强；当DTMI线向下突破其移动平均线时，视为卖出信号，表明市场卖盘力量增强。该指标适合于短线操作和趋势跟踪策略，需要注意的是，DTMI指标也可能出现钝化现象，因此在实际使用时应与其他指标或分析方法结合使用，以提高交易决策的准确性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 常规通用技术指标

## Related Factors

[### 方向性动量离散指标 (Directional Momentum Dispersion Index)](/zh/factors/tech/directional-standard-deviation)[### 日内强度指标 (Intraday Momentum Index, IMI)](/zh/factors/tech/intraday-momentum)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 多空意愿指标 (Bull-Bear Index, BBI)](/zh/factors/tech/long-void-index)[### 资金流量指标](/zh/factors/tech/money-flow-index)[### 资金流量累积指标 (Accumulation/Distribution Line, A/D)](/zh/factors/tech/accumulative-distribution-line)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 区域强度指数](/zh/factors/tech/region-index)