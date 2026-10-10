# 相对强弱人气指标 (AR)

技术因子

## 因子公式

AR(N) = (∑(HIGH - OPEN, N) / ∑(OPEN - LOW, N)) \* 100

$$
\frac{\sum\_{i=1}^{N}(HIGH\_i - OPEN\_i)}{\sum\_{i=1}^{N}(OPEN\_i - LOW\_i)} \times 100
$$

其中：

* $N$

  :

  回溯期参数，表示计算AR指标所使用的历史交易日数量。通常情况下，默认值为20，但也可能根据不同的市场或交易策略进行调整。N值越大，AR指标对市场短期波动越不敏感，反之越敏感。
* $∑(X, N)$

  :

  求和函数，对X值在过去N个交易日的值进行累加。具体来说，它将从当前交易日往前推算N个交易日，并计算这些交易日X值的总和。
* $HIGH$

  :

  当日最高价，指在特定交易日内达到的最高交易价格。
* $OPEN$

  :

  当日开盘价，指在特定交易日开始时的交易价格。
* $LOW$

  :

  当日最低价，指在特定交易日内达到的最低交易价格。
* $HIGH\_i$

  :

  第i个交易日的最高价
* $OPEN\_i$

  :

  第i个交易日的开盘价
* $LOW\_i$

  :

  第i个交易日的最低价

## 因子解释

相对强弱人气指标 (AR) 的计算原理是衡量在特定周期内，股价向上波动（当日最高价减去开盘价）的总和与股价向下波动（开盘价减去当日最低价）总和之间的比率，然后乘以100进行标准化。这个比率反映了市场买方（多方）与卖方（空方）力量的相对强弱。当AR值较高时，意味着买方力量相对较强，市场可能处于超买状态；反之，当AR值较低时，意味着卖方力量相对较强，市场可能处于超卖状态。该指标主要用于辅助判断市场情绪以及可能的反转时机，并非绝对的买卖信号。需要注意的是，AR指标应与其他技术指标和基本面分析结合使用，以提高决策的准确性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 经典技术分析

## Related Factors

[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 区域强度指数](/zh/factors/tech/region-index)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 阿隆指标](/zh/factors/tech/aroon-index)[### 布林买卖意愿比率](/zh/factors/tech/br-indicator)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)[### 平均真实波幅 (Average True Range, ATR)](/zh/factors/tech/average-true-volatility)