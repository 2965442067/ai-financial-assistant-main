# 商品通道指数 (Commodity Channel Index)

技术因子

## 因子公式

典型价格 (TP):

$$
TP = \frac{HIGH + LOW + CLOSE}{3}
$$

商品通道指数 (CCI(N)):

$$
CCI(N) = \frac{TP - SMA(TP, N)}{0.015 \times MAD(TP, N)}
$$

平均绝对偏差 (MAD):

$$
MAD(X, N) = \frac{1}{N}\sum\_{i=1}^{N}|X\_i - SMA(X,N)|
$$

其中:

* $TP$

  :

  典型价格 (Typical Price), 代表一个交易日内的高、低、收盘价的均值，用于捕捉该交易日的中心价格水平。计算公式为：(最高价 + 最低价 + 收盘价) / 3。
* $SMA(TP, N)$

  :

  N日简单移动平均线 (Simple Moving Average) 指的是对过去N个周期的典型价格(TP)进行算术平均。 它平滑了价格波动，提供了一个价格趋势的基准线。N值通常设置为20，可根据具体交易标的和时间周期进行调整。
* $MAD(TP, N)$

  :

  N日平均绝对偏差 (Mean Absolute Deviation) 是衡量典型价格(TP)在N个周期内波动幅度的指标。它计算每个TP与其N日简单移动平均值(SMA(TP,N))之间差的绝对值的平均值。MAD值越大表示价格波动越大，反之亦然。
* $N$

  :

  计算周期参数，表示用于计算移动平均和平均绝对偏差的时间窗口大小。通常设置为20个交易日，但可以根据交易标的特性和交易策略进行调整。 较小的N值会导致CCI更敏感，而较大的N值会导致CCI更平滑。

## 因子解释

商品通道指数 (CCI) 是一种动量振荡器，用于衡量当前价格相对于其统计平均水平的偏差程度。 计算方法是当前典型价格(TP)与其N日简单移动平均值(SMA(TP,N))之差，再除以一个缩放因子(0.015乘以N日平均绝对偏差(MAD(TP,N)))。缩放因子用于将CCI的数值标准化，使其大约70%到80%的时间都在 -100 到 +100 的范围内。当CCI高于+100时，通常被视为超买区域，表示价格可能回调；当CCI低于-100时，通常被视为超卖区域，表示价格可能反弹。 CCI 还可以用来识别价格与指标之间的背离，以此来预测潜在的价格趋势反转。例如，当价格创出新高，而CCI没有创出新高时，可能预示着价格上涨动能的减弱。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 约翰·墨菲. (2018). 技术分析指标手册. 上海财经大学出版社

## Related Factors

[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 价格偏离移动均线百分比 (Price Deviation from Moving Average Percentage)](/zh/factors/tech/bias)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 蔡金波动率指标 (Chaikin Volatility Index)](/zh/factors/tech/cvi)[### 钱德动量振荡器](/zh/factors/tech/chande-momentum-oscillator)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)[### 异同离差乖离率振荡器](/zh/factors/tech/deviation-rate)[### 多空意愿指标 (Bull-Bear Index, BBI)](/zh/factors/tech/long-void-index)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)