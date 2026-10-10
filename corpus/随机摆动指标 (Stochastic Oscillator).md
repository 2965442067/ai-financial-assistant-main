# 随机摆动指标 (Stochastic Oscillator)

技术因子

## 因子公式

未成熟随机值 (RSV):

$$
RSV\_t = 100 \* \frac{CLOSE\_t - MIN(LOW\_{t-N+1:t})}{MAX(HIGH\_{t-N+1:t}) - MIN(LOW\_{t-N+1:t})}
$$

快速随机值 (K):

$$
K\_t = SMA(RSV\_t, M1, 1)
$$

慢速随机值 (D):

$$
D\_t = SMA(K\_t, M2, 1)
$$

发散值 (J):

$$
J\_t = 3 \* K\_t - 2 \* D\_t
$$

加权移动平均 (SMA):

$$
SMA(X\_t, N, M) = \frac{(X\_t \* M + SMA\_{t-1} \* (N-M))}{N}
$$

参数解释:

* $N$

  :

  回溯周期数，用于计算过去N个周期内的最高价和最低价，默认值为9。
* $M1$

  :

  快速随机值K的平滑周期数，默认值为3，一般用于控制K值对RSV的敏感程度。
* $M2$

  :

  慢速随机值D的平滑周期数，默认值为3，一般用于控制D值对K值的敏感程度。
* $t$

  :

  表示当前时间。
* $CLOSE\_t$

  :

  表示当前周期的收盘价。
* $LOW\_{t-N+1:t}$

  :

  表示从当前周期向前回溯N个周期内的最低价。
* $HIGH\_{t-N+1:t}$

  :

  表示从当前周期向前回溯N个周期内的最高价。
* $RSV\_t$

  :

  表示当前周期的未成熟随机值。
* $K\_t$

  :

  表示当前周期的快速随机值。
* $D\_t$

  :

  表示当前周期的慢速随机值。
* $J\_t$

  :

  表示当前周期的发散值。
* $SMA\_{t-1}$

  :

  表示前一个周期的加权移动平均值。

## 因子解释

随机摆动指标通过计算未成熟随机值（RSV），并对其进行平滑处理，得到快速随机值K和慢速随机值D，以此来衡量市场动量和超买超卖状态。RSV反映了当前收盘价在过去一段时间的价格波动区间中的相对位置；K值是对RSV的平滑，更加稳定；D值是对K值的平滑，进一步降低了噪音，提供了更平稳的信号。J值则是通过放大K值和D值的差值，提供更敏感的短期动量信号，用于辅助判断潜在的反转点。该指标常用于短期交易策略，辅助交易者识别市场的短期顶部和底部，但应结合其他技术分析工具进行综合判断，以提高信号的准确性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 常规通用技术指标

## Related Factors

[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 区域强度指数](/zh/factors/tech/region-index)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 价格变动速率因子](/zh/factors/tech/rate-of-change)[### 佳庆波动率离散指标](/zh/factors/tech/jiaqing-discrete-index)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 克林格成交量震荡指标](/zh/factors/tech/klinger-volume-oscillator)