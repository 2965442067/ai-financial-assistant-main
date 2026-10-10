# 成交量动量摆动指标 (Klinger Volume Oscillator)

技术因子

## 因子公式

TR:

$$
TR = IF(HIGH+LOW+CLOSE>HIGH[1]+LOW[1]+CLOSE[1],1,-1)
$$

真实范围（Trend Reversal）：用于判断当日价格相对前一日的动向。如果当日价格中位值（最高价、最低价和收盘价之和）高于前一日，则赋值为1，否则赋值为-1。这个变量表示了价格趋势的方向性变化。

DM:

$$
DM = HIGH-LOW
$$

当日动量（Daily Momentum）：表示当日最高价与最低价之间的差值，反映了当日价格的波动幅度。该值的大小直接体现了当日价格的活跃程度。

CM:

$$
CM = IF(TR=TR[1],CM[1]+DM,DM[1]+DM)
$$

累积动量（Cumulative Momentum）：根据当日和前一日的真实范围 (TR) 的变化，累积当日的动量 (DM)。如果今日和昨日的 TR 值相同，则将昨日的 CM 值加上今日的 DM 值；否则，将前一日的 DM 值加上今日的 DM 值。该变量旨在捕获价格动量的持续性。

VF:

$$
VF = VOL\*ABS(2\*(DM/CM-1))\*TR\*100
$$

成交量波动（Volume Force）：基于成交量、价格动量和趋势方向计算得出的量化值。通过将当日成交量 (VOL) 乘以一个基于 DM 与 CM 比率计算的系数，并结合趋势方向 (TR)，得到最终的成交量波动值。此步骤有效地放大了价格动量与成交量之间的关系。

KVO(N1,N2):

$$
KVO(N1,N2) = EMA(VF,N1)-EMA(VF,N2)
$$

成交量动量摆动指标（Klinger Volume Oscillator）：计算成交量波动 (VF) 的短期 (N1) 和长期 (N2) 指数移动平均 (EMA) 的差值。通过比较短期和长期成交量动量，反映资金流入流出的加速或减速状态，从而识别潜在的趋势反转。

公式中各参数含义：

* $TR$

  :

  真实范围 (Trend Reversal)：一个二元指标，当今日价格中位值大于昨日时为1，否则为-1。用于表示价格趋势变化的方向。
* $DM$

  :

  当日动量 (Daily Momentum)：当日最高价和最低价之差，体现了当日价格的波动幅度。
* $CM$

  :

  累积动量 (Cumulative Momentum)：根据TR的变化累积当日的动量。如果TR值不变则连续累加，否则累加前一日动量。用于衡量价格动量的持续性。
* $VF$

  :

  成交量波动 (Volume Force)：成交量乘以一个基于动量比率的系数，并结合趋势方向，用于量化成交量的波动强度。
* $VOL$

  :

  当日成交量 (Volume)： 指在指定时间段内，特定证券或资产交易的股数或合约数量。
* $N1$

  :

  较短的指数移动平均周期 (Short EMA Period)：用于计算VF的短期EMA，默认值通常为34，用于捕获短期内的成交量动量变化。
* $N2$

  :

  较长的指数移动平均周期 (Long EMA Period)：用于计算VF的长期EMA，默认值通常为55，用于平滑VF的波动，揭示长期趋势动量。
* $EMA$

  :

  指数移动平均 (Exponential Moving Average)：一种加权平均方法，最近的数据点赋予更大的权重，对新数据反应更灵敏。用于平滑时间序列数据并识别趋势。
* $IF(condition, value\_if\_true, value\_if\_false)$

  :

  条件函数 (Conditional Function)： 根据条件判断返回不同的值。用于根据特定的逻辑规则执行不同的计算。
* $ABS$

  :

  绝对值函数 (Absolute Value Function)：返回数值的绝对值。确保计算中相关数值均为正值，方便衡量波动幅度。

## 因子解释

成交量动量摆动指标 (KVO) 通过计算成交量波动 (VF) 的短期和长期指数移动平均的差值来衡量市场资金流的动量。正的KVO值表示短期资金流入强于长期，可能预示价格上升趋势；负的KVO值则表示短期资金流出强于长期，可能预示价格下降趋势。KVO指标的零轴交叉点通常被认为是潜在的买卖信号。该指标结合了价格动量和成交量信息，因此可以提供比单独分析价格或成交量更全面的市场视角。高波动性的KVO值表明趋势较强，而低波动性则可能预示趋势的减弱或潜在的反转。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Stephen Klinger. (1997). Klinger Volume Oscillator. Technical Analysis of Stocks and Commodities

## Related Factors

[### 克林格成交量震荡指标](/zh/factors/tech/klinger-volume-oscillator)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 成交量异同移动平均线 (VMACD)](/zh/factors/tech/volume-moving-average-convergence-divergence)[### 成交量能量潮指标 (On-Balance Volume)](/zh/factors/tech/energy-metrics)[### 简易波动指标 (Easy of Movement Value, EMV)](/zh/factors/tech/easy-movement-value)[### 随机摆动指标](/zh/factors/tech/stochastic-indicator)[### 成交额变异系数](/zh/factors/volatility/volatility-coefficient-of-turnover)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)