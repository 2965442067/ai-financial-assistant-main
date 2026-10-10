# 平均真实波幅 (Average True Range, ATR)

技术因子

## 因子公式

真实波幅 (TR) =

$$
TR = \max(HIGH - LOW, |HIGH - CLOSE\_{prev}|, |LOW - CLOSE\_{prev}|)
$$

平均真实波幅 (ATR) =

$$
ATR = EMA(TR, N)
$$

默认:

$$
N = 20
$$

公式中的符号解释：

* $HIGH$

  :

  当日最高价
* $LOW$

  :

  当日最低价
* $CLOSE$

  :

  当日收盘价
* $CLOSE\_{prev}$

  :

  前一日收盘价
* $| |$

  :

  绝对值
* $max( )$

  :

  取最大值
* $EMA(TR, N)$

  :

  对真实波幅 (TR) 进行 N 日的指数移动平均
* $N$

  :

  计算 ATR 使用的窗口期，默认值为20。

## 因子解释

ATR 通过计算当日价格波动相对于前一日收盘价的最大变动幅度，有效解决了跳空缺口对波动性度量带来的干扰。具体而言，首先计算每日的真实波幅 (TR)，它是当日最高价与最低价之差、当日最高价与前一日收盘价之差的绝对值、以及当日最低价与前一日收盘价之差的绝对值三者中的最大值。然后，对 TR 进行指定周期（通常为20日）的指数移动平均，得到最终的平均真实波幅 (ATR)。指数移动平均相比简单移动平均，赋予近期数据更高的权重，使其能够更快地捕捉到价格波动性的变化。ATR 可以用来判断当前市场的波动性大小，辅助制定交易策略。例如，ATR 较高时，说明市场波动剧烈，可以考虑采用更宽的止损或止盈设置；而 ATR 较低时，说明市场波动较小，则可以采用相对紧凑的止损或止盈设置。此外，ATR 还可以与其他技术指标结合使用，以提升交易决策的准确性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* (1978). J. Welles Wilder, Jr. 原著. New Concepts in Technical Trading Systems

## Related Factors

[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 区域强度指数](/zh/factors/tech/region-index)[### 成交额变异系数](/zh/factors/volatility/volatility-coefficient-of-turnover)[### 日均负向成交额占比相对强度](/zh/factors/emotion/average-single-transaction-outflow-ratio)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 振幅切割动量累积因子](/zh/factors/tech/amplitude-cutting-momentum)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 佳庆波动率离散指标](/zh/factors/tech/jiaqing-discrete-index)[### 阿隆指标](/zh/factors/tech/aroon-index)