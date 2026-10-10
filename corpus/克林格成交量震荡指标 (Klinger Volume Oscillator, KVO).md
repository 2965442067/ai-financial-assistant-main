# 克林格成交量震荡指标 (Klinger Volume Oscillator, KVO)

技术因子

## 因子公式

真实范围方向 (TR):

$$
TR = IF(HIGH\_t + LOW\_t + CLOSE\_t > HIGH\_{t-1} + LOW\_{t-1} + CLOSE\_{t-1}, 1, -1)
$$

每日价格变动 (DM):

$$
DM = HIGH\_t - LOW\_t
$$

累积动量 (CM):

$$
CM\_t = IF(TR\_t = TR\_{t-1}, CM\_{t-1} + DM\_t, DM\_t + DM\_{t-1})
$$

成交量波动 (VF):

$$
VF\_t = VOL\_t \* ABS(2 \* (\frac{DM\_t}{CM\_t} - 1)) \* TR\_t \* 100
$$

克林格成交量震荡指标 (KVO):

$$
KVO(N\_1, N\_2)\_t = EMA(VF\_t, N\_1) - EMA(VF\_t, N\_2)
$$

公式中：

* $TR\_t$

  :

  t 时刻的真实范围方向，若当前价格之和大于前一期则为 1，反之则为 -1。用于衡量价格趋势方向。
* $DM\_t$

  :

  t 时刻的每日价格变动，即当日最高价与最低价之差。反映当日价格波动幅度。
* $CM\_t$

  :

  t 时刻的累积动量，当期真实范围方向与上一期相同时，为上一期累积动量加上当期价格变动，否则为上一期和当期价格变动之和，体现价格动量的累积。
* $VF\_t$

  :

  t 时刻的成交量波动，经成交量加权后的价格动量变化。放大成交量对价格趋势的影响。
* $VOL\_t$

  :

  t 时刻的成交量。
* $EMA(VF\_t, N)$

  :

  对成交量波动 (VF) 进行指数移动平均 (EMA) 计算，N 代表时间窗口。
* $N1$

  :

  短期时间窗口，用于计算短期 EMA，默认值为 34。较小的值可以更快地捕捉短期波动。
* $N2$

  :

  长期时间窗口，用于计算长期 EMA，默认值为 55。较大的值可以提供更平滑的长期趋势。

## 因子解释

克林格成交量震荡指标 (KVO) 通过比较短期和长期成交量动量的指数移动平均值 (EMA) 来衡量资金流入流出的强度和方向。正的 KVO 值表示资金流入占主导地位，可能预示价格上涨趋势；负的 KVO 值表示资金流出占主导地位，可能预示价格下跌趋势。KVO 值的大小反映了趋势的强度。该指标主要用于趋势确认和识别潜在的趋势反转点，而非提供直接的交易信号。此外，KVO 可以与价格图表结合使用，观察背离现象，以捕捉潜在的价格反转。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 常规通用技术指标

## Related Factors

[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 成交量异同移动平均线 (VMACD)](/zh/factors/tech/volume-moving-average-convergence-divergence)[### 成交量能量潮指标 (On-Balance Volume)](/zh/factors/tech/energy-metrics)[### 简易波动指标 (Easy of Movement Value, EMV)](/zh/factors/tech/easy-movement-value)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 随机摆动指标](/zh/factors/tech/stochastic-indicator)[### 实体K线一致性买入强度因子](/zh/factors/tech/consistent-buy-transaction)