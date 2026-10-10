# 相对强弱指标 (RSI)

技术因子

## 因子公式

计算相对强度 (RS):

$$
RS = \frac{\text{Average Gain}}{\text{Average Loss}}
$$

相对强度 (RS) 是指定周期内所有价格上涨幅度的平均值与所有价格下跌幅度的平均值之比。其中，平均涨幅 (Average Gain) 和平均跌幅 (Average Loss) 通常采用指数移动平均 (EMA) 或简单移动平均 (SMA) 计算。初始平均值可以用简单的平均值计算，后续的平均值通过移动平均的方式进行更新，以反映近期价格变动的影响。

计算相对强弱指标 (RSI):

$$
RSI = 100 - \frac{100}{1 + RS}
$$

相对强弱指标 (RSI) 是通过将相对强度 (RS) 转换为0到100之间的标准化值得到的。这个转换使得指标更容易理解和应用。该公式将RS值映射到一个0到100的区间，使得RSI指标的波动范围更为明确。

公式中的关键参数及其解释：

* $Average Gain$

  :

  指定周期内价格上涨幅度的平均值。通常用指数移动平均 (EMA) 或简单移动平均 (SMA) 计算。计算时，仅考虑价格上涨的情况，下跌情况按0处理。
* $Average Loss$

  :

  指定周期内价格下跌幅度的平均值。通常用指数移动平均 (EMA) 或简单移动平均 (SMA) 计算。计算时，仅考虑价格下跌的情况，上涨情况按0处理。注意，该值通常是正数，尽管代表的是价格的下跌幅度。
* $RS$

  :

  相对强度，是平均涨幅与平均跌幅的比值，反映了价格上涨力量与下跌力量的相对强弱。
* $RSI$

  :

  相对强弱指标，是标准化后的动量指标，其值介于0到100之间，用于评估价格变动的强度和速度。

## 因子解释

RSI 的取值范围在 0 到 100 之间。通常，RSI 值接近 70 或更高时，表示资产可能处于超买状态，即价格可能被高估，存在回调风险；RSI 值接近 30 或更低时，表示资产可能处于超卖状态，即价格可能被低估，存在反弹机会。然而，需要注意的是，RSI 的阈值并非绝对，不同的资产或市场可能会有不同的适用范围。同时，RSI 应该结合其他技术指标和基本面分析一起使用，才能更准确地判断市场趋势和交易机会。需要使用多个样本（多只股票）并进行回测来验证不同参数和阈值设置下该指标的有效性。此外，RSI 的背离现象（价格创新高/低，而RSI指标没有同步创新高/低）也是一个重要的信号，可能预示着趋势的反转。

## Related Factors

[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 区域强度指数](/zh/factors/tech/region-index)[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 日内强度指标 (Intraday Momentum Index, IMI)](/zh/factors/tech/intraday-momentum)