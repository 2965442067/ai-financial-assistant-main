# 最大日收益率（Max Daily Return）

技术因子

## 因子公式

最大日收益率 (Max Daily Return):

$$
\max\_{t \in [T-K, T]} {R\_t}
$$

公式计算的是在过去K个月内，股票每日收益率序列中的最大值。

* $R\_t$

  :

  股票在第t日的收益率
* $K$

  :

  回溯期，表示计算最大日收益率所考虑的过去月份数。
* $T$

  :

  当前日期

## 因子解释

最大日收益率反映了股票在特定时间窗口内可能出现的极端正向收益。该因子可以被视为一种衡量股票投机性和潜在爆发力的指标，其数值越高，表明股票在过去一段时间内经历过更大的单日上涨幅度。实证研究表明，最大日收益率与未来股票收益之间存在显著的负相关关系，这表明过去出现极端正向回报的股票，未来可能会出现收益回撤或波动加剧的风险，因此可以作为风险因子进行考量。该因子的应用场景包括：风险管理、高波动股票筛选、以及与其他动量类因子的组合使用等。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Turan G. Bali, Nusret Cakici, and Robert F. Whitelaw. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. Journal of Financial Economics

## Related Factors

[### 最小收益率 (MinReturn)](/zh/factors/momentum/minimum-yield)[### 52周最高价逼近度](/zh/factors/momentum/52-week-high)[### 20日区间收益率动量/反转因子](/zh/factors/tech/momentum-or-reversal)[### 月度收益季节性动量因子](/zh/factors/emotion/seasonal-returns)[### 排序动量因子](/zh/factors/momentum/momentum-based-on-ranking)[### 中期反转因子 (Medium-Term Reversal Factor)](/zh/factors/emotion/long-term-reversal)[### 过去K个月累计收益率动量因子](/zh/factors/momentum/momentum)[### 月度超额收益季节性反转因子](/zh/factors/momentum/seasonal-return-reversal)[### 时间序列动量 (TSMOM)](/zh/factors/momentum/time-series-momentum)