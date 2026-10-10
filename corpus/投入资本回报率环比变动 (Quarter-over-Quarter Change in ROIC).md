# 投入资本回报率环比变动 (Quarter-over-Quarter Change in ROIC)

质量因子

## 因子公式

ROIC\_Q(t) - ROIC\_Q(t-4)

$$
ROIC\_{Q(t)} - ROIC\_{Q(t-4)}
$$

该公式计算最近报告期单季度投入资本回报率与上年同期单季度投入资本回报率之差。

* $ROIC\_Q(t)$

  :

  t 时刻的单季度投入资本回报率（Return on Invested Capital），其中 t 代表最近报告期。
* $ROIC\_Q(t-4)$

  :

  t-4 时刻的单季度投入资本回报率（Return on Invested Capital），其中 t-4 代表上年同期报告期（假设每季度报告一次）。

## 因子解释

该因子属于质量成长类因子，旨在捕捉公司投入资本回报效率的短期变化趋势。

1. **因子逻辑:** 投入资本回报率（ROIC）是衡量公司运用资本创造收益能力的核心指标。ROIC的环比变动，能够反映公司在短期内经营效率和盈利能力的提升或下降。正的变动表明公司在投入资本的使用上变得更有效率，可能预示着未来增长潜力，而负的变动则可能意味着经营效率的下降。
2. **因子意义:**

   * **质量维度:** ROIC本身是衡量企业经营质量的重要指标，ROIC的环比提升反映了企业运营质量的改善。
   * **成长维度:** ROIC的提升通常与盈利增长和价值创造相关联，因此该指标也具有成长性特征。
   * **短期视角:** 与同比增长相比，环比变动更关注公司短期内的经营变化，可以更及时地捕捉到公司经营状况的动态。
3. **计算选择:**

   * **单季度数据:** 使用单季度数据而非TTM（滚动12个月）数据，能够更好地反映公司短期内的经营变化，避免因历史数据平滑掉近期的变化趋势。
   * **环比变动:** 环比变动更敏感地反映了公司在相邻报告期内的变化，能够更及时地捕捉到经营状况的拐点。

* **增量而非增长率**: 使用增量而非增长率，避免了ROIC绝对值较低时，增长率出现较大波动的情况，使得因子表现更加稳定。

4. **潜在应用:**

   * 该因子可以与其他质量或成长类因子结合使用，构建多因子选股模型。
   * 可以作为分析师在评估公司短期经营变化趋势时的参考指标。
   * 可以用来识别那些运营效率正在改善，可能具有投资潜力的公司。
5. **注意事项:**

   * 受季节性因素影响较大的行业，其ROIC的环比变动可能也会有较大的季节性波动，应进行适当调整或与其他指标结合分析。
   * 需要结合行业特点和公司自身情况进行综合分析，避免过度依赖单一指标。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 投入资本回报率（ROIC）的运用与分析

## Related Factors

[### 季度投入资本回报率 (Quarterly ROIC)](/zh/factors/quality/single-return-on-invested-capital)[### 投入资本回报率(ROIC)](/zh/factors/basic-surface/return-on-invested-capital)[### 单季度投入资本回报率 (QoQ ROIC)](/zh/factors/basic-surface/basic-surface-return-on-invested-capital)[### 有形资本回报率环比增长率 (TTM)](/zh/factors/growth/return-on-tangible-capital-rotc-mom-growth-rate)[### 单季度总资产净利率同比变动](/zh/factors/growth/changes-in-the-net-profit-margin-of-total-assets-in-a-single-quarter)[### 单季度总资产报酬率同比变动](/zh/factors/basic-surface/single-quarter-asset-return-rate)[### 单季度摊薄净资产收益率同比变动](/zh/factors/basic-surface/change-in-return-on-diluted-net-assets-for-a-single-quarter)[### 单季度营业利润率同比变动率](/zh/factors/basic-surface/1q-operating-margin-yoy-growth)[### 单季度经营活动净现金流同比增速](/zh/factors/basic-surface/growth-rate-of-net-cash-flow)