# 基于CAPM的残差动量因子

技术因子

## 因子公式

计算CAPM回归残差：

$$
r\_{i,t} - r\_{f,t} = \alpha\_i + \beta\_i (r\_{m,t} - r\_{f,t}) + \epsilon\_{i,t}
$$

计算残差动量：

$$
IMOM\_{i,t} = \prod\_{j=1}^{11} (1 + \epsilon\_{i,t-j})
$$

其中：

* $$
  r\_{i,t}
  $$

  :

  股票 i 在 t 时刻的收益率，计算方式通常为（当前价格 - 上一时刻价格）/上一时刻价格。
* $$
  r\_{f,t}
  $$

  :

  在 t 时刻的无风险利率，通常使用短期国债利率作为近似值。
* $$
  r\_{m,t}
  $$

  :

  在 t 时刻的市场收益率，通常使用代表整体市场的指数（如沪深300指数）的收益率作为近似值。
* $$
  \alpha\_i
  $$

  :

  股票 i 的 CAPM 回归截距项，表示股票 i 相对于市场的超额收益（在市场收益率为零的情况下）的预期值。
* $$
  \beta\_i
  $$

  :

  股票 i 的 Beta 值，衡量股票 i 的收益率对市场收益率变动的敏感程度，β > 1 表明股票波动性大于市场，β < 1 表明股票波动性小于市场，β = 1 表明股票波动性与市场一致。
* $$
  \epsilon\_{i,t}
  $$

  :

  股票 i 在 t 时刻的 CAPM 回归残差，表示模型无法解释的，股票 i 的特有收益部分，即股票 i 的收益率偏离 CAPM 模型预测值的程度。残差越大，表示股票受特有因素的影响越大。
* $$
  IMOM\_{i,t}
  $$

  :

  股票 i 在 t 时刻的残差动量，表示过去 11 个周期（通常为月度）的残差累计收益率。这里采用的是累乘形式，更精确的捕捉了收益率复利累积的效果。

## 因子解释

该残差动量因子基于渐进信息扩散假说，认为投资者对公司特有信息的反应存在滞后性，从而导致残差项中蕴含着持续的收益信号。具体来说，在利用CAPM模型剔除了市场整体波动的影响后，残差项反映的是个股特有的信息影响，投资者对这些信息的反应通常较慢，这便导致了残差动量效应：如果某只股票的残差项在过去一段时间内持续为正，则该股票在未来一段时间内可能继续上涨，反之亦然。因此，我们可以通过计算过去一段时间的残差累积收益率来构建残差动量因子，以此来捕捉这种信息反应滞后带来的投资机会。

值得注意的是，因子公式中残差动量采用了累乘计算方式，相比于累加方式，累乘更能体现收益率的复利效应，并对累积收益率进行更精确的衡量。同时，公式中的计算周期为11，而非原始数据中的12，这是为了与业内常见的动量计算周期保持一致，并避免收益率计算中可能出现的‘幸存者偏差’问题。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* [Chaves, Denis B. (2012). Eureka! A Momentum Strategy that Also Works in Japan. Social Science Electronic Publishing](https://ssrn.com/abstract=1982100)

## Related Factors

[### Fama-French三因子模型残差动量](/zh/factors/tech/residual-momentum-ff3)[### 过去K个月累计收益率动量因子](/zh/factors/momentum/momentum)[### 残差资金流强度](/zh/factors/tech/residual-fund-flow-intensity)[### 时间序列动量 (TSMOM)](/zh/factors/momentum/time-series-momentum)[### 多时域移动平均动量因子](/zh/factors/tech/trend-factor)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 残差市值偏离度](/zh/factors/basic-surface/specific-market-capitalization)[### 行业领头羊动量溢价因子](/zh/factors/emotion/industry-momentum-factor)[### 排序动量因子](/zh/factors/momentum/momentum-based-on-ranking)