# 蔡金资金流量震荡指标 (Chaikin Money Flow Oscillator)

技术因子

## 因子公式

中间价 (Money Flow Volume, MV):

$$
MV\_t = VOL\_t \* \frac{2 \* CLOSE\_t - HIGH\_t - LOW\_t}{HIGH\_t + LOW\_t}
$$

累积中间价 (Money Flow Accumulation, MFA):

$$
MFA\_t = \sum\_{i=0}^{t} MV\_i
$$

蔡金资金流量震荡指标 (Chaikin Money Flow Oscillator, CMO):

$$
CMO\_t = EMA(MFA, N\_1)\_t - EMA(MFA, N\_2)\_t
$$

默认值:

$$
默认: N\_1 = 10, N\_2 = 3
$$

其中：

* $MV\_t$

  :

  第t日的中间价 (Money Flow Volume)，是成交量加权的当日价格波动。 当日收盘价越接近当日高点，此值为正；反之，收盘价越接近当日低点，此值为负。
* $MFA\_t$

  :

  第t日的累积中间价 (Money Flow Accumulation), 是从初始到第t日所有中间价之和。
* $VOL\_t$

  :

  第t日的成交量。
* $CLOSE\_t$

  :

  第t日的收盘价。
* $HIGH\_t$

  :

  第t日的最高价。
* $LOW\_t$

  :

  第t日的最低价。
* $EMA$

  :

  指数移动平均线(Exponential Moving Average), EMA(X, N) 表示对变量 X 计算周期为 N 的指数移动平均值。相对于简单移动平均线，EMA给予近期数据更高的权重，对价格变动更敏感。
* $N\_1$

  :

  较长周期的EMA参数，通常用于平滑数据，默认值为10。更大的N1值将使指标对价格变化不敏感，更平滑。
* $N\_2$

  :

  较短周期的EMA参数，通常用于捕捉动量，默认值为3。更小的N2值将使指标对价格变化更敏感，波动更剧烈。

## 因子解释

蔡金资金流量震荡指标 (Chaikin Money Flow Oscillator, CMO) 是由马克·蔡金（Marc Chaikin）开发的动量指标，用于衡量资金流入和流出的强度。它是对累积/派发线 (AD Line) 的改进，通过计算中间价（Money Flow Volume, MV）的累积值（Money Flow Accumulation, MFA），然后取MFA的两个不同周期的指数移动平均（EMA）之差来得到。CMO指标旨在识别潜在的价格反转，当CMO曲线快速上升时，可能预示着买盘力量增强，反之，CMO曲线快速下降时，可能预示着卖盘力量增强。该指标通常与股价的移动平均线结合使用，以提高交易信号的准确性。例如，当股价高于其90天移动平均线，并且CMO指标由负值转为正值时，这可能被视为买入信号；相反，当股价低于其90天移动平均线，并且CMO指标由正值转为负值时，则可能被视为卖出信号。需要注意的是，CMO指标并不能单独使用，需要结合其他技术分析工具和市场情况进行综合分析，以提高交易决策的可靠性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* [Marc Chaikin. Chaikin Money Flow Oscillator. Technical Analysis of the Financial Markets](https://www.investopedia.com/terms/c/chaikinmoneyflow.asp)

## Related Factors

[### 钱德动量振荡器](/zh/factors/tech/chande-momentum-oscillator)[### 蔡金资金流向指标](/zh/factors/tech/caijin-currency-flow-indicator)[### 成交量动量摆动指标](/zh/factors/tech/kvo-indicator)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 克林格成交量震荡指标](/zh/factors/tech/klinger-volume-oscillator)[### 价格变动速率因子](/zh/factors/tech/rate-of-change)[### 资金流量指标](/zh/factors/tech/money-flow-index)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 成交量异同移动平均线 (VMACD)](/zh/factors/tech/volume-moving-average-convergence-divergence)