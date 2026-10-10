# 资金流量指标 (Money Flow Index, MFI)

技术因子

## 因子公式

典型价格 TP:

$$
TP = \frac{HIGH + LOW + CLOSE}{3}
$$

典型价格（TP）是当日最高价、最低价和收盘价的算术平均值，用于代表该交易日的平均价格水平。

货币流量 MF:

$$
MF = TP \times VOL
$$

货币流量（MF）是典型价格（TP）与成交量（VOL）的乘积，代表该交易日流入或流出该资产的总资金量。当TP上升时，MF是正向的，反之则为负向的。这里将成交量乘以典型价格，代表的是该交易日“平均”成交价格下的资金量。

正向货币流量 PF(N):

$$
PF(N) = \sum\_{i=1}^{N} IF(TP\_i > TP\_{i-1}, MF\_i, 0)
$$

N日内正向货币流量之和（PF(N)）是过去N个交易日中，当当日典型价格（TP）高于前一日典型价格时，所对应的货币流量（MF）的累计值。它表示在价格上涨期间流入该资产的资金量总和，可以理解为买方力量的累积。

负向货币流量 NF(N):

$$
NF(N) = \sum\_{i=1}^{N} IF(TP\_i \leq TP\_{i-1}, MF\_i, 0)
$$

N日内负向货币流量之和（NF(N)）是过去N个交易日中，当当日典型价格（TP）小于等于前一日典型价格时，所对应的货币流量（MF）的累计值。它表示在价格下跌或不变期间流出该资产的资金量总和，可以理解为卖方力量的累积。

货币比率 MR(N):

$$
MR(N) = \frac{PF(N)}{NF(N)}
$$

货币比率（MR(N)）是正向货币流量之和（PF(N)）与负向货币流量之和（NF(N)）的比值，用于衡量特定时期内买方和卖方力量的相对强弱。当MR(N)值大于1，则代表买方力量大于卖方力量，反之，则卖方力量大于买方力量。

资金流量指标 MFI:

$$
MFI(N) = 100 - \frac{100}{1 + MR(N)}
$$

资金流量指标（MFI(N)）是根据货币比率（MR(N)）计算得出的标准化指标，其取值范围在0到100之间。MFI值接近100时，代表市场处于超买状态，MFI值接近0时，代表市场处于超卖状态。

其中：

* $$
  HIGH
  $$

  :

  最高价 (High Price)，表示在特定交易日内达到的最高成交价格。
* $$
  LOW
  $$

  :

  最低价 (Low Price)，表示在特定交易日内达到的最低成交价格。
* $$
  CLOSE
  $$

  :

  收盘价 (Close Price)，表示在特定交易日结束时最后一次的成交价格。
* $$
  VOL
  $$

  :

  成交量 (Volume)，表示在特定交易日内该资产的总成交量。
* $$
  TP
  $$

  :

  典型价格 (Typical Price)，是最高价、最低价和收盘价的平均值，用于代表该交易日的价格水平。
* $$
  MF
  $$

  :

  货币流量 (Money Flow)，是典型价格与成交量的乘积，表示该交易日的资金流动量。
* $$
  PF(N)
  $$

  :

  N日内正向货币流量之和 (Positive Money Flow over N days)，表示在过去N个交易日内，当典型价格上涨时流入该资产的资金总和。这里用累加符号$\sum$表示求和。
* $$
  NF(N)
  $$

  :

  N日内负向货币流量之和 (Negative Money Flow over N days)，表示在过去N个交易日内，当典型价格下跌或持平时流出该资产的资金总和。这里用累加符号$\sum$表示求和。
* $$
  MR(N)
  $$

  :

  货币比率 (Money Ratio)，是正向货币流量之和与负向货币流量之和的比值，用于衡量资金流入和流出的相对强度。
* $$
  MFI(N)
  $$

  :

  N日资金流量指标 (Money Flow Index over N days)，是根据货币比率计算得出的标准化指标，用于评估市场超买超卖状态，取值范围为 0-100。
* $$
  N
  $$

  :

  时间周期 (Time Period)，通常默认为14，可以根据不同的市场和策略进行调整，表示计算MFI指标所用的时间跨度。

## 因子解释

资金流量指标（MFI）通过综合考虑价格和成交量来评估市场的超买超卖状态。当MFI值高于80时，通常被认为是超买区域，此时市场可能面临价格回调的风险，当MFI值向下突破80时，可能预示着短线卖出机会。相反，当MFI值低于20时，通常被认为是超卖区域，此时市场可能面临价格反弹的机会，当MFI值向上突破20时，可能预示着短线买入机会。需要注意的是，MFI指标的超买超卖阈值（80和20）并非固定不变，可以根据具体的市场情况和交易策略进行调整。此外，MFI指标应与其他技术分析工具结合使用，以提高交易决策的准确性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Martin J. Pring. (1991). 技术分析精论. McGraw-Hill

## Related Factors

[### 蔡金资金流向指标](/zh/factors/tech/caijin-currency-flow-indicator)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 资金流量累积指标 (Accumulation/Distribution Line, A/D)](/zh/factors/tech/accumulative-distribution-line)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 区域强度指数](/zh/factors/tech/region-index)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)