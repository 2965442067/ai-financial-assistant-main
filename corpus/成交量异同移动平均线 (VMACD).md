# 成交量异同移动平均线 (VMACD)

技术因子

## 因子公式

短期成交量指数移动平均线 (SHORT)

$$
SHORT = EMA(VOL, N1)
$$

计算过去 N1 个周期的成交量 (VOL) 的指数移动平均线 (EMA)。N1 是一个较小的参数，用于捕捉较短期的成交量变化。

长期成交量指数移动平均线 (LONG)

$$
LONG = EMA(VOL, N2)
$$

计算过去 N2 个周期的成交量 (VOL) 的指数移动平均线 (EMA)。N2 是一个较大的参数，用于捕捉较长期的成交量变化。

差离值 (DIFF)

$$
DIFF = SHORT - LONG
$$

计算短期成交量指数移动平均线 (SHORT) 与长期成交量指数移动平均线 (LONG) 的差值。DIFF 值反映了短期成交量动量相对于长期成交量动量的强弱。

异同平均值 (DEA)

$$
DEA = EMA(DIFF, M)
$$

计算差离值 (DIFF) 过去 M 个周期的指数移动平均线 (EMA)。DEA 值是对 DIFF 值的平滑，可以减少短期波动，并突出趋势的延续。

成交量异同移动平均线 (VMACD)

$$
VMACD = DIFF - DEA
$$

计算差离值 (DIFF) 与异同平均值 (DEA) 的差值。VMACD 值是最终的指标值，反映了成交量动能的相对强弱，并通过正负值和穿越零轴来识别买卖信号。

参数说明:

* $VOL$

  :

  表示成交量数据，用于计算指数移动平均线。
* $N1$

  :

  短期 EMA 周期，用于计算短期成交量指数移动平均线（SHORT）。默认值为 12，通常设置为较小的数值以反映短期成交量变化。该参数的调整会影响 VMACD 指标对短期成交量波动的敏感程度。较小的 N1 值会导致指标更敏感，而较大的 N1 值会导致指标更平滑。
* $N2$

  :

  长期 EMA 周期，用于计算长期成交量指数移动平均线（LONG）。默认值为 26，通常设置为较大的数值以反映长期成交量变化。该参数的调整会影响 VMACD 指标对长期成交量趋势的敏感程度。较小的 N2 值会导致指标对长期趋势的反应更迅速，而较大的 N2 值则会使指标对长期趋势更平稳。
* $M$

  :

  DEA 计算的周期，用于平滑差离值（DIFF）。默认值为 9，通常设置为一个较小的数值。调整 M 值会影响 DEA 对 DIFF 变化的敏感程度。较小的 M 值会导致 DEA 对 DIFF 的变化反应更快速，而较大的 M 值会导致 DEA 更平稳。

## 因子解释

成交量异同移动平均线 (VMACD) 通过比较不同时间周期的成交量动能，来判断市场参与度的变化趋势。当 VMACD 值由负转正或上穿零轴时，表明成交量动能增强，可能预示着价格上涨；当 VMACD 值由正转负或下穿零轴时，则表明成交量动能减弱，可能预示着价格下跌。此外，DIFF 和 DEA 的交叉也可能提供买入或卖出信号，但需要与其他技术指标或基本面分析结合使用，以提高判断的准确性。该指标特别适用于分析市场对价格走势的确认程度，并有助于识别成交量驱动的趋势反转。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John J. Murphy. (1999). Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications. New York Institute of Finance

## Related Factors

[### 移动平均汇聚背离指标](/zh/factors/tech/moving-average-convergence-divergence)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)[### 异同离差乖离率振荡器](/zh/factors/tech/deviation-rate)[### 克林格成交量震荡指标](/zh/factors/tech/klinger-volume-oscillator)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 蔡金波动率指标 (Chaikin Volatility Index)](/zh/factors/tech/cvi)[### 简易波动指标 (Easy of Movement Value, EMV)](/zh/factors/tech/easy-movement-value)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)