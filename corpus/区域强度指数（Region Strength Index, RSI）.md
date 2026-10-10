# 区域强度指数（Region Strength Index, RSI）

技术因子

## 因子公式

真实波幅 (TR) =

$$
TR = \max(HIGH - LOW, |CLOSE\_{t-1} - HIGH|, |CLOSE\_{t-1} - LOW|)
$$

波动幅度权重 (W) =

$$
W = \begin{cases} \frac{TR}{CLOSE\_t - CLOSE\_{t-1}} & CLOSE\_t > CLOSE\_{t-1} \\ TR & CLOSE\_t \le CLOSE\_{t-1} \end{cases}
$$

标准化波动幅度 (SR(N1)) =

$$
SR(N1) = \begin{cases} \frac{W - \min(W\_{t-N1+1}, ..., W\_t)}{\max(W\_{t-N1+1}, ..., W\_t) - \min(W\_{t-N1+1}, ..., W\_t)} \times 100 & \text{if} \; \max(W\_{t-N1+1}, ..., W\_t) - \min(W\_{t-N1+1}, ..., W\_t) > 0 \\ (W - \min(W\_{t-N1+1}, ..., W\_t)) \times 100 & \text{otherwise} \end{cases}
$$

区域强度指数 (RSI(N1, N2)) =

$$
RSI(N1, N2) = EMA(SR(N1), N2)
$$

公式中：

* $TR$

  :

  真实波幅（True Range），衡量当日价格的波动范围，取当日最高价与最低价之差、前一日收盘价与当日最高价之差的绝对值、前一日收盘价与当日最低价之差的绝对值三者中的最大值。公式中下标t表示当前时刻，下标t-1表示前一个时刻。
* $HIGH$

  :

  当日最高价
* $LOW$

  :

  当日最低价
* $CLOSE\_t$

  :

  当日收盘价
* $CLOSE\_{t-1}$

  :

  前一日收盘价
* $W$

  :

  波动幅度权重，当今日收盘价高于前一日收盘价时，W为真实波幅TR除以今日与前一日收盘价之差；否则，W等于真实波幅TR。该权重体现了价格波动幅度相对于收盘价变化的强度。
* $W\_{t-N1+1}, ..., W\_t$

  :

  表示从当前时间 t 回溯 N1 个时间单位的 W 值序列。
* $N1$

  :

  计算标准化波动幅度（SR）的周期长度，表示在计算SR时，所考虑的历史W值的窗口长度。默认值为20。
* $N2$

  :

  计算区域强度指数（RSI）的指数移动平均（EMA）平滑周期，用于平滑标准化波动幅度SR。默认值为5。
* $SR(N1)$

  :

  标准化波动幅度，用于将波动幅度权重W标准化到0-100之间。当N1周期内的W值的最大值与最小值不相等时，SR为（W - N1周期内W的最小值）除以（N1周期内W的最大值-N1周期内W的最小值）再乘以100；否则，SR为（W-N1周期内W的最小值）乘以100。目的是将波动幅度权重值归一化到固定区间。
* $RSI(N1, N2)$

  :

  区域强度指数，是标准化波动幅度SR(N1)的N2周期指数移动平均值。它结合了波动幅度和收盘价变动，以识别潜在的趋势转折点。该指标能够更敏感地捕捉价格波动，并平滑波动，更好地指示趋势的潜在转变。

## 因子解释

区域强度指数（RSI）通过分析真实波幅与收盘价变动之间的关系来识别趋势的开始与结束。指标值较高意味着价格波动幅度相对于收盘价变动幅度较大，可能预示趋势的反转。RSI是一个振荡指标，通过结合真实波幅和收盘价的波动，可以识别潜在的买入或卖出信号，尤其是在指标值达到极端高位或低位时。该指标结合了真实波幅的概念，并使用指数移动平均（EMA）进行平滑，以减少噪音并识别潜在的趋势性变动。高RSI值通常表示市场处于超买状态，可能出现回调；低RSI值则可能表示市场处于超卖状态，可能出现反弹。RSI主要用于辅助判断趋势和识别潜在的超买超卖区域。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance

## Related Factors

[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 随机摆动指标](/zh/factors/tech/stochastic-indicator)