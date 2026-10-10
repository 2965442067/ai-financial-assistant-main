# Amihud 非流动性指标

流动性因子

## 因子公式

Amihud 非流动性指标 (ILLIQ):

$$
ILLIQ\_{i,t} = \frac{1}{D\_t} \sum\_{d=1}^{D\_t} \frac{|R\_{i,d}|}{VOLD\_{i,d}}
$$

其中：

* $$
  ILLIQ\_{i,t}
  $$

  :

  为股票i在t月的Amihud非流动性指标。
* $$
  R\_{i,d}
  $$

  :

  为股票i在t月内第d个交易日的收益率。
* $$
  VOLD\_{i,d}
  $$

  :

  为股票i在t月内第d个交易日的成交额 (通常以货币单位表示)。
* $$
  D\_t
  $$

  :

  为t月内股票i的有效交易日总数。通常要求月内有效交易日天数不少于15天。

## 因子解释

Amihud 非流动性指标旨在捕捉市场冲击成本，即单位交易量引起的资产价格变动。该指标基于一个核心假设：流动性较差的资产，其价格对交易量的波动更为敏感。因此，该指标数值越高，意味着资产的价格变动需要更大的交易量推动，反映出更高的流动性风险，投资者会要求更高的预期回报作为风险补偿，从而产生流动性溢价。该指标常被用于量化投资中的风险建模和选股策略。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Amihud, Yakov. (2002). Illiquidity and stock returns: Cross-section and time-series effects. Journal of Financial Markets 5, 31-56

## Related Factors

[### Amihud非流动性冲击因子](/zh/factors/emotion/liquidity-shock)[### 非流动性变异系数](/zh/factors/volatility/illiquidity-coefficient-of-variation)[### 条件流动性冲击因子](/zh/factors/liquidity/conditional-liquidity-shock)[### 负收益成交额加权非流动性因子](/zh/factors/emotion/negative-return-illiquidity)[### 平均月度成交额](/zh/factors/liquidity/trading-volume)[### 高频波动率路径长度加权非流动性因子](/zh/factors/liquidity/illiquidity)[### 成交额波动率](/zh/factors/volatility/trading-volume-fluctuation)[### 流动性调整成交量零值天数比率](/zh/factors/liquidity/liquidity-adjusted-volume)[### 资金流量累积指标 (Accumulation/Distribution Line, A/D)](/zh/factors/tech/accumulative-distribution-line)