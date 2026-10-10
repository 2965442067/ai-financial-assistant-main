# 移动平均汇聚背离指标 (MACD)

技术因子

## 因子公式

差离值 (DIF):

$$
DIF = EMA(CLOSE, N\_1) - EMA(CLOSE, N\_2)
$$

讯号线 (DEA):

$$
DEA = EMA(DIF, N\_3)
$$

柱状图 (MACD Histogram):

$$
MACD\_{Histogram} = 2 \* (DIF - DEA)
$$

其中：

* $N\_1$

  :

  快线EMA的时间窗口长度，表示计算快速指数移动平均线时所使用的历史数据周期数。通常设置为12，该参数决定了快线对近期价格变化的敏感程度，较小的值意味着对价格变化更敏感。
* $N\_2$

  :

  慢线EMA的时间窗口长度，表示计算慢速指数移动平均线时所使用的历史数据周期数。通常设置为26，该参数决定了慢线对价格变化的敏感程度，较大的值意味着对价格变化相对不敏感，主要反映长期趋势。
* $N\_3$

  :

  DEA平滑的时间窗口长度，表示对DIF值进行平滑计算时所使用的历史数据周期数。通常设置为9，该参数决定了DEA线对DIF变化的敏感程度，较小的值意味着对DIF的变化更敏感。

## 因子解释

MACD指标通过计算快慢两条指数移动平均线（EMA）的差值（DIF），并对该差值进行平滑处理（DEA）来实现对价格动量的分析。

**具体来说：**

* **差离值 (DIF):** DIF线是快线EMA与慢线EMA的差值，它反映了短期和长期价格趋势之间的差异。DIF向上穿越零轴被视为潜在的买入信号，反之，向下穿越零轴则为潜在的卖出信号。DIF值的变化代表了短期趋势相对于长期趋势的强弱变化。
* **讯号线 (DEA):** DEA线是对DIF值进行平滑后的结果，它通常作为DIF线的信号线。当DIF线上穿DEA线时，通常被认为是买入信号；当DIF线下穿DEA线时，则被认为是卖出信号。DEA线可以减少DIF线的虚假信号，提供更稳定的交易信号。
* **柱状图 (MACD Histogram):** 柱状图是DIF线和DEA线之间的差值，并乘以2进行放大，用于更清晰地观察DIF线和DEA线的交叉和背离。柱状图的正负值和大小变化，可以帮助交易者判断价格动能的变化。柱状图由负转正，表示价格动能增强，可能形成买入机会；柱状图由正转负，表示价格动能减弱，可能形成卖出机会。

**MACD的交易信号：**

* **金叉：** 当DIF线从下向上穿越DEA线时，称为金叉，通常被视为买入信号。
* **死叉：** 当DIF线从上向下穿越DEA线时，称为死叉，通常被视为卖出信号。
* **零轴穿越：** 当DIF线穿越零轴时，可以视为更强的趋势确认信号。
* **顶背离：** 当价格创出新高，但MACD指标没有创出新高时，可能预示着趋势即将反转。
* **底背离：** 当价格创出新低，但MACD指标没有创出新低时，可能预示着趋势即将反转。

**重要提示:**
MACD指标是一种滞后指标，不能单独使用。在实际应用中，需要结合其他技术指标和基本面分析进行综合判断，并进行风险管理。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 约翰·墨菲. (2019). 技术分析大全. 海南出版社

## Related Factors

[### 成交量异同移动平均线 (VMACD)](/zh/factors/tech/volume-moving-average-convergence-divergence)[### 异同离差乖离率振荡器](/zh/factors/tech/deviation-rate)[### 梅斯指数](/zh/factors/tech/mass-index)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)[### 资金流量累积指标 (Accumulation/Distribution Line, A/D)](/zh/factors/tech/accumulative-distribution-line)[### 方向性动量离散指标 (Directional Momentum Dispersion Index)](/zh/factors/tech/directional-standard-deviation)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 三重指数移动平均 (TEMA)](/zh/factors/tech/triple-exponential-moving-average)