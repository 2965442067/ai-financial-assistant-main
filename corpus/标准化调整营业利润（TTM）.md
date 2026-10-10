# 标准化调整营业利润（TTM）

基础面因子

## 因子公式

标准化调整营业利润（TTM）:

$$
\frac{AdjustedOperatingProfit\_{TTM,t} - mean(AdjustedOperatingProfit\_{TTM,t-T:t-1})}{std(AdjustedOperatingProfit\_{TTM,t-T:t-1})}
$$

调整后营业利润（TTM）:

$$
AdjustedOperatingProfit\_{TTM} = OperatingProfit\_{TTM} + AdvancesFromCustomers\_{TTM}
$$

公式中：

* $AdjustedOperatingProfit\_{TTM,t}$

  :

  t期调整后营业利润（TTM）值，其中TTM表示滚动12个月的累计值。
* $mean(AdjustedOperatingProfit\_{TTM,t-T:t-1})$

  :

  过去T期调整后营业利润（TTM）的均值。计算时，使用t-T期到t-1期的AdjustedOperatingProfit\_{TTM}数据。
* $std(AdjustedOperatingProfit\_{TTM,t-T:t-1})$

  :

  过去T期调整后营业利润（TTM）的标准差。计算时，使用t-T期到t-1期的AdjustedOperatingProfit\_{TTM}数据。
* $T$

  :

  回溯期数，表示计算均值和标准差时所使用的时间跨度，默认T=6，即回溯6个季度的数据。
* $OperatingProfit\_{TTM}$

  :

  滚动12个月的累计营业利润。
* $AdvancesFromCustomers\_{TTM}$

  :

  滚动12个月的累计预收账款，反映公司未来确认收入的潜力。

## 因子解释

标准化调整营业利润（TTM）因子通过对调整后的营业利润进行标准化处理，能够有效消除不同公司之间由于规模差异、行业属性等因素导致的盈利能力差异，从而更准确地比较和评估不同公司之间的真实盈利增长水平。具体来说，我们首先计算调整后的营业利润（TTM），其中预收账款被视为未来收入的潜在来源，并被加回到营业利润中。随后，我们计算过去T期调整后营业利润（TTM）的均值和标准差，并将其用于对当期调整后营业利润进行标准化。该因子的标准化处理使得不同公司之间的盈利增长具有可比性，并消除了量纲差异，便于后续的因子组合与模型构建。该因子可以被视为一个另类成长因子，但由于与传统的盈利能力和成长因子存在一定的相关性，建议在多因子模型中与其他因子结合使用时，通过回归或其他方法剔除其相关性，以提升因子的独立性和有效性。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 曹春晓. (2018). 基本面因子之经营性标准化成长因子. 申万宏源

## Related Factors

[### 标准化营业利润(TTM)](/zh/factors/basic-surface/standardized-operating-profit)[### 单季度营业利润率同比变动率](/zh/factors/basic-surface/1q-operating-margin-yoy-growth)[### 单季度营业利润同比增速](/zh/factors/basic-surface/1q-operating-profit-yoy-growth-rate)[### 经营利润率（TTM）](/zh/factors/basic-surface/operating-profit-ratio)[### 每股营业收入(TTM)](/zh/factors/basic-surface/earnings-per-share1)[### 经营效率变动因子 (Operating Efficiency Change Factor)](/zh/factors/basic-surface/operating-capacity-improvement)[### 单季度摊薄净资产收益率同比变动](/zh/factors/basic-surface/change-in-return-on-diluted-net-assets-for-a-single-quarter)[### 运营成本利润率 (Operating Cost Profit Margin)](/zh/factors/basic-surface/cost-profit-margin)[### 摊薄扣非净资产收益率（TTM）](/zh/factors/basic-surface/roe-diluted-non-recurring)