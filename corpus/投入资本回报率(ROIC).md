# 投入资本回报率(ROIC)

基础面因子

## 因子公式

投入资本回报率 (ROIC):

$$
\frac{EBIT\_{TTM} \* (1-TaxRate)}{InvestedCapital}
$$

税后息税前利润 (EBIT\_{TTM} \* (1-TaxRate)):

$$
EBIT\_{TTM}\*(1-TaxRate)
$$

息税前利润 (EBIT\_{TTM}):

$$
OperatingProfit\_{TTM} + InterestExpense\_{TTM}
$$

投入资本 (InvestedCapital):

$$
TotalShareholdersEquity + InterestBearingDebt
$$

有息负债 (InterestBearingDebt):

$$
ShortTermBorrowings + LongTermBorrowings + BondsPayable + CurrentPortionOfLongTermDebt
$$

其中：

* $EBIT\_{TTM}$

  :

  最近12个月的息税前利润（Earnings Before Interest and Taxes），通常使用TTM (Trailing Twelve Months) 数据，代表过去12个月的累计值。
* $OperatingProfit\_{TTM}$

  :

  最近12个月的营业利润，也使用TTM数据。
* $InterestExpense\_{TTM}$

  :

  最近12个月的利息费用，也使用TTM数据。
* $TaxRate$

  :

  公司的有效税率，可以是实际税率或者行业平均税率，公式中使用简化税率0.25，在实际使用中，应该替换为企业真实税率。
* $InvestedCapital$

  :

  投入资本，即公司用于经营活动的总资本，包括股东权益和有息负债。
* $TotalShareholdersEquity$

  :

  股东权益合计，代表股东在公司中的所有权。
* $InterestBearingDebt$

  :

  有息负债，即公司需要支付利息的债务，包括短期借款、长期借款、应付债券和一年内到期的长期负债。
* $ShortTermBorrowings$

  :

  短期借款，是指需要在一年内偿还的借款。
* $LongTermBorrowings$

  :

  长期借款，是指需要在一年以上偿还的借款。
* $BondsPayable$

  :

  应付债券，是指公司发行的，需要在未来某个时间点偿还的债券。
* $CurrentPortionOfLongTermDebt$

  :

  一年内到期的长期负债，是指长期债务中需要在一年内偿还的部分。

## 因子解释

投入资本回报率(ROIC)是一个关键的盈利能力和资本效率指标。它衡量公司利用所有投入资本（包括股东权益和有息负债）产生税后经营利润的能力。该指标越高，表明公司在管理和利用其资本方面越有效率，能够为投资者创造更多的价值。ROIC不仅可以用于评估公司的盈利能力，还可以用于比较不同公司之间的资本效率，以及评估公司长期价值创造能力。投资者通常会将ROIC与公司的加权平均资本成本(WACC)进行比较，如果ROIC大于WACC，则说明公司正在为投资者创造价值，否则则可能是在消耗价值。 需要注意的是，在计算ROIC时，EBIT通常使用TTM(Trailing Twelve Months)数据，以反映公司最近的经营表现，而投入资本则通常使用期末值。此外，在计算税后EBIT时，应该使用公司实际的税率，而不是固定的税率。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* CFA Institute. 财务报表分析. CFA Curriculum

## Related Factors

[### 季度投入资本回报率 (Quarterly ROIC)](/zh/factors/quality/single-return-on-invested-capital)[### 单季度投入资本回报率 (QoQ ROIC)](/zh/factors/basic-surface/basic-surface-return-on-invested-capital)[### 投入资本回报率环比变动](/zh/factors/quality/quality-return-on-invested-capital)[### 滚动扣非净资产收益率](/zh/factors/basic-surface/non-net-asset-return)[### 总资产报酬率 (ROA)](/zh/factors/basic-surface/total-asset-net-profit-margin)[### 期末摊薄净资产收益率 (Trailing Twelve Months ROE - TTM ROE)](/zh/factors/basic-surface/roe-factor)[### 有形资本回报率](/zh/factors/basic-surface/tangible-capital-return-rate)[### 总资产报酬率（TTM）](/zh/factors/basic-surface/total-asset-operating-profit)[### 有形资本回报率环比增长率 (TTM)](/zh/factors/growth/return-on-tangible-capital-rotc-mom-growth-rate)