# 资本支出增长率-N年（CAGR-N）

基础面因子

## 因子公式

资本支出增长率-N年 (CAGR-N):

$$
\frac{CapitalExpenditure\_{TTM} - CapitalExpenditure\_{TTM-N}}{CapitalExpenditure\_{TTM-N}}
$$

其中：

* $CapitalExpenditure\_{TTM}$

  :

  最近12个月滚动计算的资本性支出 (Trailing Twelve Months Capital Expenditure)。资本性支出指公司为维持或扩大其生产能力、业务规模而进行的长期资产投资，具体计算方法为：购建固定资产、无形资产和其他长期资产支付的现金 - 处置固定资产、无形资产和其他长期资产收回的现金。
* $CapitalExpenditure\_{TTM-N}$

  :

  N年前同期（当前时间点的前N年）的12个月滚动资本性支出。例如，如果N=2，则为两年前同一时间点开始的12个月滚动资本性支出。
* $N$

  :

  时间跨度，以年为单位。常用取值包括2年 (N=2) 和 3年 (N=3)，分别对应24个月和36个月的比较基准。

## 因子解释

资本支出增长率反映了公司在固定资产、无形资产等长期资产方面的投资扩张力度。 一般而言，较高的资本支出增长率可能暗示公司正在积极扩张业务，为未来发展奠定基础，但也需要结合公司的行业特点、经营情况等进行综合分析。

实证研究表明，资本支出增长率与股票未来收益呈负相关关系，这可能反映了过度投资或者市场对未来增长的预期已在股价中得到体现。 此外，公司资本支出行为还会影响诸如市值、账面市值比等传统基本面因子与股票收益之间的关系，并且可能降低因子的风险暴露。

此因子的逻辑基于以下考虑：

* **过度投资理论:** 高资本支出增长率可能预示着公司过度投资，导致资源错配，降低未来回报。
* **预期透支:** 高资本支出增长可能意味着市场已经对公司未来的成长性抱有较高预期，并将这种预期反映在股价中，从而降低了未来超额收益的可能性。
* **风险调整:** 将资本支出增长纳入因子组合，可以在一定程度上对冲因过度投资等风险因素暴露，提高因子组合的稳定性。

**风险提示：** 该因子仅为量化分析中的一个参考指标，不构成任何投资建议。投资决策应基于充分的尽职调查和风险评估。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Anderson, C., and L. Garcia-Feijoo. (2006). Empirical evidence on capital investment, growth options, and security returns. Journal of Finance 61, 171-194

## Related Factors

[### 资本支出异常增长率](/zh/factors/basic-surface/abnormal-capital-investment)[### 季度总资产环比增长率](/zh/factors/basic-surface/asset-growth-single-quarter)[### 发行股本增长率](/zh/factors/basic-surface/growth-rate-of-number-of-shares-issued)[### TTM基本每股收益同比增长率](/zh/factors/basic-surface/earnings-growth-rate)[### 单季度账面价值增长率](/zh/factors/basic-surface/book-value-growth-rate-single-quarter)[### 年度员工总数增长率](/zh/factors/growth/employee-growth-rate)[### 年度总负债对数增长率](/zh/factors/basic-surface/comprehensive-debt-issuance)[### 单季度营业总成本同比增速](/zh/factors/basic-surface/single-quarter-revenue-cost-growth-rate)[### 单季度经营活动净现金流同比增速](/zh/factors/basic-surface/growth-rate-of-net-cash-flow)