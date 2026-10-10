# 多空意愿指标 (Bull-Bear Index, BBI)

技术因子

## 因子公式

BBI = (MA(CLOSE, M1) + MA(CLOSE, M2) + MA(CLOSE, M3) + MA(CLOSE, M4)) / 4

$$
\frac{MA(CLOSE,M1)+MA(CLOSE,M2)+MA(CLOSE,M3)+MA(CLOSE,M4)}{4}
$$

其中:

* $MA(CLOSE, N)$

  :

  N日简单移动平均线，表示过去N个交易日收盘价的算术平均值。
* $M1$

  :

  短期移动平均线周期，通常设置为 3 个交易日。
* $M2$

  :

  中短期移动平均线周期，通常设置为 6 个交易日。
* $M3$

  :

  中期移动平均线周期，通常设置为 12 个交易日。
* $M4$

  :

  中长期移动平均线周期，通常设置为 20 个交易日。

## 因子解释

多空意愿指标 (BBI) 通过对不同周期的简单移动平均线进行平均，旨在综合评估市场多空双方的力量。其设计思路在于，短期移动平均线对价格波动更加敏感，能够更快地反映市场情绪，而长期移动平均线则更加平滑，反映了市场的中长期趋势。BBI 通过将不同周期的移动平均线结合起来，可以有效地过滤掉短期噪音，同时捕捉到中长期趋势的变化。当BBI向上运行时，表明市场整体多方力量较强，反之则为空方力量较强。投资者可以结合价格走势和BBI的相对位置，来辅助判断市场趋势，发现潜在的买卖时机。此外，BBI 的参数（M1, M2, M3, M4）可以根据不同的市场和投资偏好进行调整，但通常保持短、中、长期周期的组合。请注意，任何技术指标都应与其他分析工具结合使用，不能单独作为投资决策的依据。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Martin J. Pring. (2002). 技术分析精论. McGraw-Hill
* Steve Nison. (2001). 日本蜡烛图技术. John Wiley & Sons

## Related Factors

[### 价格偏离移动均线百分比 (Price Deviation from Moving Average Percentage)](/zh/factors/tech/bias)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 随机动量指标 (SMI)](/zh/factors/tech/stochastic-momentum-indicator)[### 布林买卖意愿比率](/zh/factors/tech/br-indicator)[### 方向性动量离散指标 (Directional Momentum Dispersion Index)](/zh/factors/tech/directional-standard-deviation)[### 异同离差乖离率振荡器](/zh/factors/tech/deviation-rate)[### 相对波动性指标](/zh/factors/tech/relative-volatility-index)[### 梅斯指数](/zh/factors/tech/mass-index)