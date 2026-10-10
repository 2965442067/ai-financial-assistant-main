# Amihud非流动性冲击

情绪因子

## 因子公式

Amihud非流动性冲击因子计算公式如下：

$$
LIQU\_{i,t} = - (ILLIQ\_{i,t} - AVGILLIQ\_{i,t-12,t-1})
$$

其中：

* $$
  ILLIQ\_{i,t}
  $$

  :

  为股票 i 在 t 月的 Amihud 非流动性因子。Amihud 非流动性因子 ($ILLIQ\_{i,t}$) 通常定义为股票 i 在 t 月的每日绝对收益与每日成交量的比率的平均值。其公式为：$ILLIQ\_{i,t} = \frac{1}{D} \sum\_{d=1}^{D} \frac{|R\_{i,d}|}{V\_{i,d}}$, 其中 $R\_{i,d}$ 代表股票 i 在 t 月第 d 天的收益， $V\_{i,d}$ 代表股票 i 在 t 月第 d 天的成交量（通常以金额或股数计量），D代表t月总交易天数。 该值越高，表明该股票的流动性越差。
* $$
  AVGILLIQ\_{i,t-12,t-1}
  $$

  :

  为股票 i 的Amihud非流动性因子在过去12个月的平均值。计算方式是将股票 i 在 t-12月到 t-1月这12个月的每个月的Amihud非流动性因子 ($ILLIQ\_{i,m}$) 求和，然后除以12。 公式为：$AVGILLIQ\_{i,t-12,t-1} = \frac{1}{12} \sum\_{m=t-12}^{t-1} ILLIQ\_{i,m}$ 。该值反映了过去一年该股票流动性的平均水平。

## 因子解释

Amihud非流动性冲击因子 (LIQU) 的计算方式为当前Amihud非流动性因子减去过去12个月Amihud非流动性因子的平均值，取负号。 该因子的核心思想是，当流动性冲击为负值（即 $LIQU\_{i,t}$ 为负），表示当前非流动性水平高于过去一年的平均水平，即市场流动性下降，投资者会要求更高的风险溢价，从而股票的未来收益可能会上升。 反之，当流动性冲击为正值（即 $LIQU\_{i,t}$ 为正），表示当前非流动性水平低于过去一年的平均水平，即市场流动性上升，投资者承担的流动性风险降低，因此可能导致资产的未来收益下降。因此，该因子可以用于捕捉由流动性变化所带来的潜在投资机会。此外，由于市场对流动性冲击的反应不足，短期内价格往往未能完全反映流动性变化的影响，这也为使用该因子构建量化交易策略提供了机会。 需要注意的是，此因子是具有反转性质的，即当流动性冲击为负时，股票未来收益预期为正，反之亦然。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Turan G. Bali, Lin Peng, Yannan Shen, Yi Tang. (2014). Liquidity Shocks and Stock Market Reactions. The Review of Financial Studies

## Related Factors

[### 条件流动性冲击因子](/zh/factors/liquidity/conditional-liquidity-shock)[### Amihud 非流动性指标](/zh/factors/liquidity/amihud-illiquidity)[### 负收益成交额加权非流动性因子](/zh/factors/emotion/negative-return-illiquidity)[### 非流动性变异系数](/zh/factors/volatility/illiquidity-coefficient-of-variation)[### 高频波动率路径长度加权非流动性因子](/zh/factors/liquidity/illiquidity)[### 流动性调整成交量零值天数比率](/zh/factors/liquidity/liquidity-adjusted-volume)[### 成交额波动率](/zh/factors/volatility/trading-volume-fluctuation)[### 平均月度成交额](/zh/factors/liquidity/trading-volume)[### 非对称价格冲击偏度](/zh/factors/tech/price-impact-bias)