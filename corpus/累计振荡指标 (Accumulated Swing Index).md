# 累计振荡指标 (Accumulated Swing Index)

技术因子

## 因子公式

A =

$$
A = |HIGH - CLOSE\_{t-1}|
$$

A 表示当日最高价与前一日收盘价之差的绝对值，衡量了当日最高价相对于前一日收盘价的波动幅度。

B =

$$
B = |LOW - CLOSE\_{t-1}|
$$

B 表示当日最低价与前一日收盘价之差的绝对值，衡量了当日最低价相对于前一日收盘价的波动幅度。

C =

$$
C = |HIGH - LOW\_{t-1}|
$$

C 表示当日最高价与前一日最低价之差的绝对值，用于衡量当日的潜在波动范围，考虑到可能存在的跳空缺口。

D =

$$
D = |CLOSE\_{t-1} - OPEN\_{t-1}|
$$

D 表示前一日收盘价与前一日开盘价之差的绝对值，衡量了前一日的价格波动幅度。

E =

$$
E = CLOSE\_t - CLOSE\_{t-1}
$$

E 表示当日收盘价与前一日收盘价之差，衡量了价格的净变化。

F =

$$
F = CLOSE\_t - OPEN\_t
$$

F 表示当日收盘价与当日开盘价之差，衡量了当日价格的净变化。

G =

$$
G = CLOSE\_{t-1} - OPEN\_{t-1}
$$

G 表示前一日收盘价与前一日开盘价之差，衡量了前一日的价格净变化。

X =

$$
X = E + 0.5F + G
$$

X 是一个综合价格变化指标，它结合了当日收盘价相对于前一日收盘价的变化 (E)，当日收盘价相对于当日开盘价的变化 (F) 的一半权重，以及前一日收盘价相对于前一日开盘价的变化 (G)，用于衡量综合的价格动量。

K =

$$
K = MAX(A, B)
$$

K 取 A 和 B 中的最大值，代表当日最高价和最低价相对于前一日收盘价的最大波动幅度。

R =

$$
R = \begin{cases} A + 0.5B + 0.25D, & \text{if } A > B \text{ and } A > C \\ B + 0.5A + 0.25D, & \text{if } B > A \text{ and } B > C \\ C + 0.25D, & \text{otherwise} \end{cases}
$$

R 是一个加权价格波动范围，根据 A、B 和 C 的大小关系来决定计算方式。当 A > B 且 A > C 时，使用 A 权重最高；当 B > A 且 B > C 时，使用 B 权重最高；否则，使用 C 和前一日的波动范围 D。R 用于衡量价格的整体波动幅度，并且能够捕捉不同情况下价格波动的特性，是计算SI的一个标准化参数。

SI =

$$
SI = 16 \* X / (R \* K)
$$

SI (Swing Index) 是当日的振荡指数，它通过 X 除以 R 和 K 的乘积，并乘以 16 进行缩放。这个公式综合考虑了价格变化方向 (X)、价格波动范围 (R) 以及相对于前一日收盘价的最大波动幅度 (K)，从而衡量了当日价格的振荡强度，并进行标准化处理。SI 的取值可能为正也可能为负，正值表明价格向有利方向波动，负值表明价格向不利方向波动。

ASI(N) =

$$
ASI(N) = \sum\_{i=t-N+1}^{t} SI\_i
$$

ASI (Accumulated Swing Index) 是 N 日累计振荡指数，通过累加过去 N 个交易日的 SI 值得到。该指标平滑了单日的振荡，更能清晰地显示价格的长期趋势，并且能够反映市场整体的动能。

其中:

* $HIGH$

  :

  当日的最高价，表示该交易日内达到的最高价格。
* $LOW$

  :

  当日的最低价，表示该交易日内达到的最低价格。
* $CLOSE$

  :

  当日的收盘价，表示该交易日结束时的最后成交价格。
* $OPEN$

  :

  当日的开盘价，表示该交易日开始时的第一笔成交价格。
* $[t-1]$

  :

  表示前一个交易日的数据，例如 CLOSE[t-1] 表示前一个交易日的收盘价。
* $ABS()$

  :

  表示绝对值函数，返回一个数值的非负值。
* $MAX(A,B)$

  :

  表示取 A 和 B 两个数值中的最大值。
* $\sum\_{i=t-N+1}^{t} SI\_i$

  :

  表示从 t-N+1 到 t 这 N 个交易日的 SI 值之和，即过去 N 天的振荡指数的累加和。
* $N$

  :

  计算 ASI 的周期参数，表示累加 SI 的天数。默认情况下，N 的常用值为 14 或 20，具体数值可根据交易策略和市场情况调整。

## 因子解释

累计振荡指标 (ASI) 通过分析一段时间内的价格波动，评估市场趋势的强度和可能的反转点。正的 ASI 值通常表明当前趋势仍在持续，市场动能较强；负的 ASI 值则可能预示趋势减弱或反转的出现。当 ASI 值从负转正时，可能代表着潜在的买入机会；反之，当 ASI 值从正转负时，可能代表着潜在的卖出机会。ASI 还可以用来识别背离现象，即当价格创新高 (低) 而 ASI 指标并未同步创新高 (低) 时，可能预示着趋势的反转。该指标需要与其他技术分析工具结合使用，以提高交易决策的准确性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). 技术分析指标大全. Technical Analysis of the Financial Markets

## Related Factors

[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 区域强度指数](/zh/factors/tech/region-index)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 日内强度指标 (Intraday Momentum Index, IMI)](/zh/factors/tech/intraday-momentum)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 阿隆指标](/zh/factors/tech/aroon-index)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)