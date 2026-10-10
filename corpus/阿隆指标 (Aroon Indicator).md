# 阿隆指标 (Aroon Indicator)

技术因子

## 因子公式

阿隆上升线 (Aroon Up):

$$
AroonUp = \frac{N - DaysSinceHigh}{N} \* 100
$$

阿隆下降线 (Aroon Down):

$$
AroonDown = \frac{N - DaysSinceLow}{N} \* 100
$$

阿隆指标 (Aroon Indicator):

$$
Aroon = AroonUp - AroonDown
$$

参数解释:

* $N$

  :

  计算周期，即回溯的时间窗口长度，表示用于计算阿隆指标的时间周期。默认值通常为25个交易日，但也可以根据具体的交易策略和市场情况进行调整。较短的周期能更快地反映价格变化，但可能产生更多噪音；较长的周期则更平滑，但可能延迟信号的出现。
* $DaysSinceHigh$

  :

  自最近一个周期内最高价出现以来经过的交易日天数。这个值越小，表示近期价格越容易创出新高，也表明上升趋势可能较强。
* $DaysSinceLow$

  :

  自最近一个周期内最低价出现以来经过的交易日天数。这个值越小，表示近期价格越容易创出新低，也表明下降趋势可能较强。

## 因子解释

阿隆指标通过计算价格在特定周期内创出新高和新低的时间间隔，来衡量趋势的强度和方向。阿隆上升线衡量价格创出新高的速度，数值越高，表示上升动能越强；阿隆下降线衡量价格创出新低的速度，数值越高，表示下降动能越强。阿隆指标的数值是阿隆上升线减去阿隆下降线，其数值的正负和大小可以帮助判断趋势的方向和强度：正值越大表示上升趋势越强，负值越大表示下降趋势越强，接近于零表示市场处于横盘或趋势不明朗的状态。通常，阿隆指标与阿隆上升线和阿隆下降线结合使用，可以更好地识别趋势反转的信号。例如，当阿隆上升线穿越阿隆下降线时，可能预示着上升趋势的开始。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* [Investopedia Team. The Aroon Indicator: How to Use the Aroon Indicator for Trading. Investopedia](https://www.investopedia.com/trading/aroon-indicator/)

## Related Factors

[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 价格变动速率因子](/zh/factors/tech/rate-of-change)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)[### 资金流量累积指标 (Accumulation/Distribution Line, A/D)](/zh/factors/tech/accumulative-distribution-line)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 区域强度指数](/zh/factors/tech/region-index)[### 方向性动量离散指标 (Directional Momentum Dispersion Index)](/zh/factors/tech/directional-standard-deviation)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)