# 三重指数移动平均 (TEMA) 指标

技术因子

## 因子公式

第一层指数移动平均 (EMA1) 计算公式：

$$
EMA\_1(t) = EMA(REAL, N)
$$

第二层指数移动平均 (EMA2) 计算公式：

$$
EMA\_2(t) = EMA(EMA\_1(t), N)
$$

第三层指数移动平均 (EMA3) 计算公式：

$$
EMA\_3(t) = EMA(EMA\_2(t), N)
$$

三重指数移动平均 (TEMA) 计算公式：

$$
TEMA(t) = 3 \times EMA\_1(t) - 3 \times EMA\_2(t) + EMA\_3(t)
$$

其中：

* $$
  N
  $$

  :

  时间周期参数，通常为正整数，表示计算移动平均所采用的时间窗口长度。例如，N=5 表示使用过去5个时间单位的数据进行计算。该参数决定了指标对价格变动的敏感程度，较小的N值对近期价格变化更敏感，但可能产生更多噪音；较大的N值平滑效果更好，但对价格变化的反应相对滞后。常用默认值为5，但可以根据交易策略和资产波动性进行调整。
* $$
  REAL(t)
  $$

  :

  在t时刻的输入序列值，通常是资产的价格序列（如收盘价：CLOSE(t)），也可以是其他时间序列数据（如成交量：VOL(t)）。这里时间t可以理解为交易时间点、交易日或其它时间单位，取决于数据频率。
* $$
  EMA\_1(t)
  $$

  :

  第一层指数移动平均，表示在t时刻，对输入序列$REAL(t)$进行指数平滑后的值。
* $$
  EMA\_2(t)
  $$

  :

  第二层指数移动平均，表示在t时刻，对$EMA\_1(t)$进行指数平滑后的值。
* $$
  EMA\_3(t)
  $$

  :

  第三层指数移动平均，表示在t时刻，对$EMA\_2(t)$进行指数平滑后的值。
* $$
  EMA(x, N)
  $$

  :

  指数移动平均函数，表示对时间序列 x 使用时间周期 N 进行指数平滑处理，返回结果序列。 其计算公式为：$EMA(x,N)*t = \alpha \* x\_t + (1 - \alpha) \* EMA(x,N)*{t-1} $, 其中 $ \alpha = \frac{2}{N + 1} $ 。初始值 $EMA(x,N)\_0$ 通常取x的第一个值或者取前N个值的简单平均值。

## 因子解释

三重指数移动平均 (TEMA) 指标通过对原始数据进行三次指数平滑，并使用加权平均方法减少移动平均线的滞后性。相比单一和双重指数移动平均，TEMA 在捕捉短期趋势反转方面更为灵敏，能够更早地发出交易信号。然而，需要注意的是，由于其敏感性，TEMA 可能会产生较多的噪音，导致误判。因此，在实际应用中，建议与其他技术指标结合使用，以提高交易信号的可靠性。此外，TEMA 的参数 N 也需要根据具体情况进行调整，以达到最佳效果。TEMA 主要应用于短线交易策略中，例如日内交易或波段交易。其关键在于识别趋势的加速和减速，辅助判断买入和卖出时机。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John Murphy. (1999). 技术分析经典. Technical Analysis of the Financial Markets
* Steven Achelis. (2000). 移动平均线指标. Technical Analysis from A to Z

## Related Factors

[### 时间序列动量 (TSMOM)](/zh/factors/momentum/time-series-momentum)[### 多时域移动平均动量因子](/zh/factors/tech/trend-factor)[### 多周期标准化移动平均动量因子](/zh/factors/tech/momentum-factor)[### 梅斯指数](/zh/factors/tech/mass-index)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 异同离差乖离率振荡器](/zh/factors/tech/deviation-rate)[### 成交量异同移动平均线 (VMACD)](/zh/factors/tech/volume-moving-average-convergence-divergence)[### 移动平均汇聚背离指标](/zh/factors/tech/moving-average-convergence-divergence)[### 价格偏离移动均线百分比 (Price Deviation from Moving Average Percentage)](/zh/factors/tech/bias)