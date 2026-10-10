# 母公司股东权益环比增长率（Quarter-on-Quarter Growth Rate of Parent Company's Equity）

基础面因子

## 因子公式

母公司股东权益环比增长率:

$$
\frac{EQ\_{t} - EQ\_{t-1}}{|EQ\_{t-1}|}
$$

公式说明:

* $EQ\_t$

  :

  最近报告期归属于母公司股东的权益。该数值直接来源于公司定期财务报告，通常是资产负债表中的所有者权益（或股东权益）的归属于母公司的部分。注意，此处选取的是单季度数据，而非滚动12个月(TTM)数据。
* $EQ\_{t-1}$

  :

  上一报告期归属于母公司股东的权益，选取与最近报告期相邻的前一报告期数据。同样，该数值来源于公司定期财务报告，且选取单季度数据。
* $|EQ\_{t-1}|$

  :

  上一报告期归属于母公司股东权益的绝对值。使用绝对值的目的是为了避免上一期权益为负数时导致增长率计算出现异常情况，使增长率的意义更为直观。

## 因子解释

该因子通过计算公司最近报告期与上一报告期归属于母公司股东权益的变化率，来衡量企业短期内的成长性。该指标选取单季度数据计算环比增长率，侧重考察企业短期经营状况和权益扩张速度。环比增长率能够反映企业最近一个季度相较于上一季度的增长情况，较同比增长率更能捕捉短期变化。增长率相较于增量更具可比性，便于跨公司和跨时间的比较，但对基数较小的公司，增长率可能出现波动较大的情况。使用上一期权益的绝对值作为分母可以避免分母为负数导致的增长率计算错误。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Stephen Penman. (2010). 企业财务报表分析. Business Expert Press
* 李明镜. (2015). 财务报表分析与证券投资. 清华大学出版社

## Related Factors

[### 单季度净利润同比增速](/zh/factors/growth/single-quarter-net-profit-yoy)[### 单季度摊薄净资产收益率同比变动](/zh/factors/basic-surface/change-in-return-on-diluted-net-assets-for-a-single-quarter)[### TTM基本每股收益同比增长率](/zh/factors/basic-surface/earnings-growth-rate)[### 归母净利润加速增长动量因子](/zh/factors/basic-surface/performance-trend)[### 归母净利润同比增长率](/zh/factors/tech/net-profit-growth-rate)[### 单季度经营活动净现金流同比增速](/zh/factors/basic-surface/growth-rate-of-net-cash-flow)[### 季度同比销售收入增长率](/zh/factors/growth/quarter-over-quarter-sales-revenue-growth)[### 有形资本回报率环比增长率 (TTM)](/zh/factors/growth/return-on-tangible-capital-rotc-mom-growth-rate)[### 单季度营业利润同比增速](/zh/factors/basic-surface/1q-operating-profit-yoy-growth-rate)