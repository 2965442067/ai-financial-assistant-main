# 流通市值（Log）

价值因子

## 因子公式

流通市值 = 当日收盘价 × 当日流通股本；
流通市值因子 = log(流通市值)

$$
\text{流通市值} = \text{当日收盘价} \times \text{当日流通股本} \newline \text{流通市值因子} = \log(\text{流通市值})
$$

该公式首先计算了公司的流通市值，即在市场上可自由交易的股份的总价值。然后，对流通市值取自然对数，以平滑数据，减小极端值的影响。

* $当日收盘价$

  :

  指当日股票在交易结束时的最后成交价格，单位为货币单位（如元，美元等）。该数据反映了市场对公司价值的最终评估。
* $当日流通股本$

  :

  指公司在市场上可自由交易的股份数量。通常不包括受限股，如内部员工持有的期权、管理层持有的股份等。该数据反映了公司股票在市场上的实际可交易规模。
* $流通市值$

  :

  指可供市场自由交易的公司股票的总价值。它是计算股票市场总价值的重要组成部分，反映了市场对公司整体价值的评估。
* $log()$

  :

  指自然对数函数，取对数可以平滑市值数据，减少极端值的影响，使因子分布更符合统计学假设。

## 因子解释

流通市值因子通常与股票收益呈负相关关系，即市值较小的公司往往在长期内产生更高的回报，称为“小市值效应”。但这种效应可能受到市场情绪、经济周期、市场风格轮动等多种因素的影响。使用对数转换可以减小原始市值的极端值影响，使因子更稳健。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Banz, Rolf W.. (1981). The relationship between return and market value of common stocks. Journal of Financial Economics

## Related Factors

[### 对数市值规模](/zh/factors/scale/log-market-cap)[### 对数自由流通市值](/zh/factors/scale/scale-log-market-cap)[### 市值中性化换手率残差](/zh/factors/liquidity/market-cap-adjusted-turnover)[### 市值非线性偏离因子](/zh/factors/value/non-linear-market-value)[### 年度股权发行调整市值增长率](/zh/factors/emotion/comprehensive-equity-offering-annual)[### 相对组合对数价差偏离度](/zh/factors/tech/price-spread-deviation)[### 市场反应滞后因子](/zh/factors/tech/price-delay)[### 自由流通市值](/zh/factors/scale/free-float-market-cap)[### 年度总负债对数增长率](/zh/factors/basic-surface/comprehensive-debt-issuance)