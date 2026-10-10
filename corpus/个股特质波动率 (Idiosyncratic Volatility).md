# 个股特质波动率 (Idiosyncratic Volatility)

波动率因子

## 因子公式

个股特质波动率公式:

$$
\sigma(\epsilon\_{i,t})
$$

资本资产定价模型 (CAPM) 回归:

$$
r\_{i,t} - r\_{f,t} = \alpha\_i + \beta\_i(r\_{m,t} - r\_{f,t}) + \epsilon\_{i,t}
$$

Fama-French三因子模型 (FF3) 回归:

$$
r\_{i,t} = \alpha\_i + \beta\_{1,i}MKT\_t + \beta\_{2,i}SMB\_t + \beta\_{3,i}HML\_t + \epsilon\_{i,t}
$$

公式中:

* $\sigma(\epsilon\_{i,t})$

  :

  为个股 i 在时间 t 的特质波动率，等于残差项 \epsilon\_{i,t} 的标准差，通常基于最近 K 个月的历史数据计算。
* $r\_{i,t}$

  :

  为个股 i 在时间 t 的收益率。
* $r\_{f,t}$

  :

  为时间 t 的无风险收益率。
* $r\_{m,t}$

  :

  为时间 t 的市场收益率，通常使用市场指数的收益率表示。
* $\alpha\_i$

  :

  为个股 i 的截距项，代表个股 i 超出市场或因子模型解释部分的平均收益率，也可视为该模型无法解释的风险补偿。
* $\beta\_i$

  :

  为个股 i 对市场风险溢价的敏感度，即市场风险暴露。
* $\epsilon\_{i,t}$

  :

  为个股 i 在时间 t 的残差项，代表不能被因子模型解释的个股特有收益部分。
* $MKT\_t$

  :

  为时间t的市场风险溢价因子，等于市场收益率减去无风险收益率。
* $SMB\_t$

  :

  为时间t的规模因子（Small Minus Big），代表小型公司股票收益与大型公司股票收益的差。
* $HML\_t$

  :

  为时间t的价值因子（High Minus Low）, 代表高账面市值比公司股票收益与低账面市值比公司股票收益的差。
* $\beta\_{1,i}, \beta\_{2,i}, \beta\_{3,i}$

  :

  分别为个股 i 对市场风险溢价因子、规模因子和价值因子的敏感度，即个股在这三个风险因子上的暴露。

## 因子解释

个股特质波动率反映了股票收益中，与市场或多因子模型无关的个股特有风险，它是一个相对独立的风险度量指标。实证研究表明，个股特质波动率与股票收益率之间存在负相关关系。即，具有较低特质波动率的股票通常具有较高的回报率，这被认为是低风险异象的一种体现。这种异象的存在表明，市场可能并非完全有效，投资者可以通过选择低特质波动率的股票来获得超额收益。然而，这种策略可能也存在一些风险，如策略拥挤和模型失效。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Ang, Andrew, Robert J. Hodrick, Yuhang Xing, and Xiaoyan Zhang. (2006). The cross-section of volatility and expected returns. Journal of Finance

## Related Factors

[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 月度加权特质波动率](/zh/factors/volatility/monthly-idiosyncratic-volatility)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 历史波动率（Total Volatility）](/zh/factors/volatility/total-volatility)[### 残差市值偏离度](/zh/factors/basic-surface/specific-market-capitalization)[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### Fama-French三因子模型残差动量](/zh/factors/tech/residual-momentum-ff3)[### 盈余波动率因子 (Earnings Volatility Factor)](/zh/factors/basic-surface/earnings-predictability)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)