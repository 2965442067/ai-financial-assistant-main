# 标准化营业利润(TTM)

基础面因子

## 因子公式

标准化营业利润(TTM):

$$
\frac{OperatingProfit\_{TTM,t} - \mu(OperatingProfit\_{TTM,t-T:t-1})}{\sigma(OperatingProfit\_{TTM,t-T:t-1})}
$$

其中:

* $OperatingProfit\_{TTM,t}$

  :

  t 时刻的滚动过去12个月(Trailing Twelve Months, TTM)营业利润。
* $\mu(OperatingProfit\_{TTM,t-T:t-1})$

  :

  过去 T 个季度 (不包含 t 时刻)的滚动过去12个月营业利润的均值。
* $\sigma(OperatingProfit\_{TTM,t-T:t-1})$

  :

  过去 T 个季度 (不包含 t 时刻)的滚动过去12个月营业利润的标准差。
* $T$

  :

  回溯历史窗口期，表示回溯的季度数量，默认为6个季度。

## 因子解释

该因子衡量当前滚动12个月营业利润相对于其过去T个季度均值的偏离程度，并以过去T个季度的标准差进行标准化。正值表示当前营业利润高于其历史平均水平，负值则表示低于历史平均水平。该因子可以反映公司营业利润的短期波动及增长趋势，并用于衡量公司经营状况的相对变化。在多因子模型中，该因子可以和其他基本面因子组合使用，提高模型对股票收益的解释能力。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 曹春晓. (2018). 基本面因子之经营性标准化成长因子. 申万宏源

## Related Factors

[### 标准化调整营业利润（TTM）](/zh/factors/basic-surface/standardized-adjusted-operating-profit)[### 单季度营业利润率同比变动率](/zh/factors/basic-surface/1q-operating-margin-yoy-growth)[### 单季度营业利润同比增速](/zh/factors/basic-surface/1q-operating-profit-yoy-growth-rate)[### 经营利润率（TTM）](/zh/factors/basic-surface/operating-profit-ratio)[### 有形资本回报率环比增长率 (TTM)](/zh/factors/growth/return-on-tangible-capital-rotc-mom-growth-rate)[### 经营效率变动因子 (Operating Efficiency Change Factor)](/zh/factors/basic-surface/operating-capacity-improvement)[### 单季度摊薄净资产收益率同比变动](/zh/factors/basic-surface/change-in-return-on-diluted-net-assets-for-a-single-quarter)[### 运营成本利润率 (Operating Cost Profit Margin)](/zh/factors/basic-surface/cost-profit-margin)[### 单季度成本费用利润率同比增速](/zh/factors/basic-surface/year-over-year-growth-in-single-quarter-cost-expense-margins)