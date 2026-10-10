# TTM基本每股收益同比增长率

基础面因子

## 因子公式

TTM基本每股收益同比增长率:

$$
\frac{EPS\_{TTM,current} - EPS\_{TTM,previousYear}}{abs(EPS\_{TTM,previousYear})}
$$

公式解释:

* $EPS\_{TTM,current}$

  :

  当前报告期（最近12个月滚动）的基本每股收益（EPS）。该值通过将公司最近四个季度的净利润相加，然后除以总股本计算得到。
* $EPS\_{TTM,previousYear}$

  :

  上年同期（与当前报告期相对应的前一年同期）的最近12个月滚动基本每股收益（EPS）。
* $abs()$

  :

  绝对值函数，用于避免上年同期基本每股收益为负值时，增长率计算产生歧义。

## 因子解释

该因子使用最近12个月滚动(TTM)的每股收益计算同比增长率，相较于单季度数据，TTM数据能够平滑短期波动，更稳定地反映公司盈利的长期趋势。同比增长率指标避免了不同时间点、不同规模公司之间绝对值的不可比性，使不同公司之间的盈利增长更具可比性。当上年同期基本每股收益接近于零时，该因子数值波动会较大，使用绝对值函数可以有效避免该问题。需要注意的是，该因子值过高时，可能需要结合其他基本面信息进行进一步分析，例如考察收入增长，以确认增长的持续性。同时，部分周期性行业，其盈利波动较大，需要结合行业特点来分析该因子。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Stephen H. Penman. (2013). 财务报表分析与估值. McGraw-Hill Education
* Zvi Bodie, Alex Kane, Alan J. Marcus. (2017). 投资学. McGraw-Hill Education

## Related Factors

[### 稀释每股收益同比增长率 (TTM)](/zh/factors/growth/diluted-eps-yoy-growth-rate)[### 单季度摊薄净资产收益率同比变动](/zh/factors/basic-surface/change-in-return-on-diluted-net-assets-for-a-single-quarter)[### 分析师预期EPS调整幅度](/zh/factors/emotion/expected-eps-adjustment)[### 母公司股东权益环比增长率](/zh/factors/basic-surface/growth-rate-of-shareholders-equity-attributable-to-the-parent-company)[### 每股净资产同比增速](/zh/factors/growth/yoy-growth-rate-of-net-assets-per-share)[### 有形资本回报率环比增长率 (TTM)](/zh/factors/growth/return-on-tangible-capital-rotc-mom-growth-rate)[### 60日盈利市值比率变动](/zh/factors/growth/profit-market-cap-ratio-60d)[### 市盈率相对盈利增长率](/zh/factors/growth/p-e-growth)[### 单季度成本费用利润率同比增速](/zh/factors/basic-surface/year-over-year-growth-in-single-quarter-cost-expense-margins)