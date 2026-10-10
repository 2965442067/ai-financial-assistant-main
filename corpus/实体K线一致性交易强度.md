# 实体K线一致性交易强度

技术因子

## 因子公式

实体K线定义:

$$
|close - open| \le \alpha |high - low|
$$

实体K线一致性交易强度因子(CTSI):

$$
CTSI\_t = \frac{1}{d}\sum\_{i=1}^{d} \left(\frac{ConsistentVolume\_i}{Volume\_i} \right)\_{t-i}
$$

其中：

* $$
  \alpha
  $$

  :

  为一致性参数，控制实体K线的定义标准。$\alpha$ 值越大，表示实体K线定义越宽松，即允许更大的影线长度；$\alpha$ 值越小，表示实体K线定义越严格，影线长度需要更短。通常 (\alpha) 取值在 0.2 到 0.5 之间。
* $$
  ConsistentVolume\_i
  $$

  :

  为第i个5分钟周期内，被判定为实体K线的成交量之和。该值代表该周期内市场一致性交易的强度，数值越大，表示一致性交易越强。
* $$
  Volume\_i
  $$

  :

  为第i个5分钟周期的总成交量。该值代表该周期内市场整体的交易活跃度。
* $$
  d
  $$

  :

  为移动平均的周期参数。它决定了计算CTSI时使用的历史数据窗口长度，较小的d值对市场变化更为敏感，而较大的d值则更加平滑。该参数通常选取为5到20之间。

## 因子解释

本因子假设市场集体一致性交易行为预示着潜在的趋势性机会。当一段时间内，股票的交易呈现较高的一致性（即CTSI值较高）时，表明市场可能正在经历信息吸收和价格调整的过程。这种一致性通常是市场情绪或特定消息驱动的结果，并可能预示着股价未来可能出现显著的波动。通过跟踪和分析CTSI值，交易者可以识别出趋势形成或加速的潜在机会。同时，该因子也可以作为风险预警信号，当CTSI值异常高时，可能意味着市场情绪过热，需要警惕价格反转的风险。需要注意的是，该因子的有效性受到市场结构和交易标的特性的影响，可能需要根据实际情况进行调整和优化。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 刘均伟. (2018). 一致交易因子：挖掘集体行为背后的收益. 光大证券

## Related Factors

[### 一致性下跌成交量比率因子](/zh/factors/tech/consistent-sell-trade)[### 实体K线一致性买入强度因子](/zh/factors/tech/consistent-buy-transaction)[### 大单成交量价动量](/zh/factors/tech/large-order-momentum)[### 主力成交同步性因子](/zh/factors/tech/main-force-trading-strength)[### 开盘时段主动净买额占比](/zh/factors/emotion/net-buy-ratio)[### 成交额波动率](/zh/factors/volatility/trading-volume-fluctuation)[### 主力成交额-价格相关性因子](/zh/factors/emotion/main-force-trading-sentiment)[### 收益动量一致性因子](/zh/factors/tech/information-dispersion)[### 开盘时段大单净买入强度标准化均值](/zh/factors/tech/large-order-net-buying-strength)