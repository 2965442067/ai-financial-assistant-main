# 单季度投入资本回报率 (QoQ ROIC)

基础面因子

## 因子公式

单季度投入资本回报率 (QoQ ROIC):

$$
\frac{EBIT\_{adj,Q} \* (1 - TaxRate\_{assumed})}{InvestedCapital\_{end}}
$$

调整后单季度息税前利润 (EBIT\_{adj,Q}):

$$
EBIT\_{adj,Q} = OperatingProfit\_Q + InterestExpense\_Q
$$

期末投入资本 (InvestedCapital\_{end}):

$$
InvestedCapital\_{end} = TotalShareholdersEquity\_{end} + InterestBearingDebt\_{end}
$$

期末有息负债 (InterestBearingDebt\_{end}):

$$
InterestBearingDebt\_{end} = ShortTermBorrowings\_{end} + LongTermBorrowings\_{end} + BondsPayable\_{end} + CurrentPortionOfLongTermDebt\_{end}
$$

各参数解释如下:

* $EBIT\_{adj,Q}$

  :

  调整后单季度息税前利润，代表公司在特定季度内，未扣除利息和税收的营业利润。使用调整后EBIT旨在排除非经常性损益的干扰，更好地反应公司的可持续盈利能力。
* $OperatingProfit\_Q$

  :

  单季度营业利润，即公司在特定季度内，主营业务所产生的利润。
* $InterestExpense\_Q$

  :

  单季度利息费用，即公司在特定季度内，因借款而产生的利息支出。
* $TaxRate\_{assumed}$

  :

  假设税率，此处使用 25% 作为假设税率，这是一个常见的假设税率。实际使用时，可以使用公司实际的有效税率或根据行业平均税率进行调整。
* $InvestedCapital\_{end}$

  :

  期末投入资本，即公司在报告期末投入的用于经营的全部资本，包括股东权益和有息负债。
* $TotalShareholdersEquity\_{end}$

  :

  期末股东权益合计，代表报告期末股东在公司中所拥有的权益。
* $InterestBearingDebt\_{end}$

  :

  期末有息负债，指公司在报告期末需要支付利息的债务，包括短期借款、长期借款、应付债券和一年内到期的长期负债。
* $ShortTermBorrowings\_{end}$

  :

  期末短期借款，指公司在报告期末的短期借款余额。
* $LongTermBorrowings\_{end}$

  :

  期末长期借款，指公司在报告期末的长期借款余额。
* $BondsPayable\_{end}$

  :

  期末应付债券，指公司在报告期末发行的债券余额。
* $CurrentPortionOfLongTermDebt\_{end}$

  :

  期末一年内到期的非流动负债，指公司在报告期末一年内需要偿还的长期债务。

## 因子解释

单季度投入资本回报率 (QoQ ROIC) 是衡量公司在单季度内，投入资本产生利润效率的指标。它通过将调整后的息税前利润（扣除假设税率影响）与期末投入资本的比率，反映了公司利用资本进行盈利的能力。相较于年度ROIC，QoQ ROIC能够提供更及时、更具动态性的公司盈利能力评估，有助于投资者把握公司短期经营状况的变化趋势。高QoQ ROIC通常意味着公司资本运用效率高，盈利能力强劲。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Aswath Damodaran. (2012). 投资估值：工具与技巧. Wiley

## Related Factors

[### 季度投入资本回报率 (Quarterly ROIC)](/zh/factors/quality/single-return-on-invested-capital)[### 投入资本回报率(ROIC)](/zh/factors/basic-surface/return-on-invested-capital)[### 投入资本回报率环比变动](/zh/factors/quality/quality-return-on-invested-capital)[### 单季度营业成本率](/zh/factors/basic-surface/single-quarter-cost-rate)[### 有形资本回报率环比增长率 (TTM)](/zh/factors/growth/return-on-tangible-capital-rotc-mom-growth-rate)[### 单季度总资产净利率同比变动](/zh/factors/growth/changes-in-the-net-profit-margin-of-total-assets-in-a-single-quarter)[### 单季度总资产报酬率同比变动](/zh/factors/basic-surface/single-quarter-asset-return-rate)[### 滚动扣非净资产收益率](/zh/factors/basic-surface/non-net-asset-return)[### 有形资本回报率](/zh/factors/basic-surface/tangible-capital-return-rate)