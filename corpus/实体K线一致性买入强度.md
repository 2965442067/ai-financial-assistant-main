# 实体K线一致性买入强度

技术因子

## 因子公式

定义实体K线:

$$
|close - open| \leq a \cdot |high - low|
$$

实体K线一致性买入强度因子(Consistent Buy Volume Ratio, CBVR):

$$
CBVR\_t = \frac{1}{d} \sum\_{i=1}^{d} (\frac{ConsistentVolume\_{rise,t-i}}{Volume\_{t-i}})
$$

其中：

* $$
  a
  $$

  :

  实体K线阈值参数，取值范围通常为[0,1]。$a$ 值越小，实体K线定义越严格，即开盘价和收盘价的差距需要更小，K线实体部分更长，上下影线更短。该参数反映了对实体K线一致性程度的敏感性。
* $$
  ConsistentVolume\_{rise,t-i}
  $$

  :

  在第t-i个交易日，所有满足实体K线定义的且收盘价高于开盘价的5分钟K线的总成交量之和，代表了该交易日内实体K线的买入成交量。此指标的目的是捕捉在短期内，具有明显买入意愿的实体K线成交量。
* $$
  Volume\_{t-i}
  $$

  :

  在第t-i个交易日，所有的5分钟K线的总成交量，代表了该交易日总的成交活跃度。
* $$
  d
  $$

  :

  移动平均窗口期，表示计算均值的历史交易日数量。通过调整 $d$ 可以控制因子对短期和长期趋势的敏感度。$d$ 越大，因子对短期交易波动越不敏感，更关注长期趋势；$d$ 越小，因子对短期交易波动越敏感，更关注短期市场行为。

## 因子解释

实体K线一致性买入强度因子（CBVR）旨在量化市场中集体买入行为的强度。当股票的CBVR值在一段时间内较高时，表示该股票的实体K线买入成交量占比相对较大，这意味着市场参与者在这些时间段内买入意愿较强，且价格变动较为一致，这可能预示着潜在的市场趋势或价格突破机会。这种一致性行为往往与市场情绪、信息披露或基本面因素的变化有关。该因子能够帮助交易者识别那些可能存在显著趋势性或突破性机会的股票，辅助量化交易策略的制定。与单纯的价格波动相比，该因子更能有效地捕捉市场情绪的变动和集体行为的共性。需要注意的是，该因子并非绝对的买入信号，需要结合其他因子和市场情况进行综合分析判断。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 刘均伟. (2018). 一致交易因子:挖掘集体行为背后的收益. 光大证券

## Related Factors

[### 一致性下跌成交量比率因子](/zh/factors/tech/consistent-sell-trade)[### 实体K线一致性交易强度因子](/zh/factors/tech/consistent-trading)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 开盘后主动买入强度标准化均值](/zh/factors/tech/net-buyer-intensity-after-opening)[### 开盘时段大单净额占比](/zh/factors/emotion/large-order-net-buy-ratio)[### 开盘时段主动净买额占比](/zh/factors/emotion/net-buy-ratio)[### 大单成交量价动量](/zh/factors/tech/large-order-momentum)[### 成交量价背离度](/zh/factors/tech/price-volume-divergence)[### 成交额波动率](/zh/factors/volatility/trading-volume-fluctuation)