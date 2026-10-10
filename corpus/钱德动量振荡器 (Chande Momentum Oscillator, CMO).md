# 钱德动量振荡器 (Chande Momentum Oscillator, CMO)

技术因子

## 因子公式

正向变动值 (CZ1) =

$$
CZ1 = \begin{cases} CLOSE - CLOSE[1] & \text{if } CLOSE - CLOSE[1] > 0 \\ 0 & \text{otherwise} \end{cases}
$$

CZ1 代表当日价格的正向变动。如果当日收盘价高于前一日收盘价，则等于两者的差值；否则为 0。该值捕捉了价格上涨的强度。

负向变动值 (CZ2) =

$$
CZ2 = \begin{cases} |CLOSE - CLOSE[1]| & \text{if } CLOSE - CLOSE[1] < 0 \\ 0 & \text{otherwise} \end{cases}
$$

CZ2 代表当日价格的负向变动。如果当日收盘价低于前一日收盘价，则等于两者差的绝对值；否则为 0。该值捕捉了价格下跌的强度。

N日正向变动总和 (SU(N)) =

$$
SU(N) = \sum\_{i=0}^{N-1} CZ1\_i
$$

SU(N) 代表过去 N 日的 CZ1 总和，即过去 N 日价格上涨的总和。它反映了这段时期内多头力量的累积。

N日负向变动总和 (SD(N)) =

$$
SD(N) = \sum\_{i=0}^{N-1} CZ2\_i
$$

SD(N) 代表过去 N 日的 CZ2 总和，即过去 N 日价格下跌的总和。它反映了这段时期内空头力量的累积。

钱德动量振荡器 (CMO) =

$$
CMO = \frac{SU(N) - SD(N)}{SU(N) + SD(N)} \* 100
$$

CMO 的计算方法是将过去 N 日价格上涨的总和 (SU(N)) 与过去 N 日价格下跌的总和 (SD(N)) 的差值除以它们的总和，再乘以 100，从而将结果缩放到 -100 到 100 的范围内。该值反映了多空力量的相对强弱。

默认参数值：

$$
N = 20
$$

N 代表计算 CMO 时所使用的回溯期，默认值为 20。投资者可以根据自身的需求和市场的特点调整回溯期。

其中，CLOSE 表示当日收盘价，CLOSE[1] 表示前一日收盘价，ABS() 表示绝对值，SUM() 表示求和函数。

* $CLOSE$

  :

  当日收盘价
* $CLOSE[1]$

  :

  前一日收盘价
* $ABS()$

  :

  绝对值函数
* $SUM()$

  :

  求和函数

## 因子解释

钱德动量振荡器 (CMO) 的取值范围在 -100 到 100 之间。当 CMO 值接近 100 时，表明市场处于超买状态，价格可能出现回调；当 CMO 值接近 -100 时，表明市场处于超卖状态，价格可能出现反弹。一般来说，CMO 大于 50 被认为是超买信号，CMO 小于 -50 被认为是超卖信号。然而，在实际应用中，投资者应该根据具体情况和市场的特点，灵活调整超买超卖的阈值，并结合其他技术指标和分析方法进行综合判断。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). 技术分析指标详解. Technical Analysis of the Financial Markets

## Related Factors

[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 价格变动速率因子](/zh/factors/tech/rate-of-change)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 蔡金资金流向指标](/zh/factors/tech/caijin-currency-flow-indicator)[### 随机摆动指标](/zh/factors/tech/stochastic-indicator)[### 日内强度指标 (Intraday Momentum Index, IMI)](/zh/factors/tech/intraday-momentum)