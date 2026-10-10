# Dimson调整贝塔

技术因子

## 因子公式

Dimson回归模型:

$$
r\_{i,t} - r\_{f,t} = \alpha\_i + \beta\_{i,lag} (r\_{m,t-1} - r\_{f,t-1}) + \beta\_{i,current} (r\_{m,t} - r\_{f,t}) + \beta\_{i,lead} (r\_{m,t+1} - r\_{f,t+1}) + \epsilon\_{i,t}
$$

Dimson调整贝塔:

$$
\beta\_{Dimson} = \hat{\beta}\_{i,lag} + \hat{\beta}\_{i,current} + \hat{\beta}\_{i,lead}
$$

其中:

* $$
  r\_{i,t}
  $$

  :

  在时间 $t$ 时刻，股票 $i$ 的收益率。
* $$
  r\_{m,t}
  $$

  :

  在时间 $t$ 时刻，市场组合的收益率。
* $$
  r\_{f,t}
  $$

  :

  在时间 $t$ 时刻，无风险利率。
* $$
  r\_{i,t-1}
  $$

  :

  在时间 $t-1$ 时刻，股票 $i$ 的收益率。
* $$
  r\_{m,t-1}
  $$

  :

  在时间 $t-1$ 时刻，市场组合的收益率。
* $$
  r\_{f,t-1}
  $$

  :

  在时间 $t-1$ 时刻，无风险利率。
* $$
  r\_{i,t+1}
  $$

  :

  在时间 $t+1$ 时刻，股票 $i$ 的收益率。
* $$
  r\_{m,t+1}
  $$

  :

  在时间 $t+1$ 时刻，市场组合的收益率。
* $$
  r\_{f,t+1}
  $$

  :

  在时间 $t+1$ 时刻，无风险利率。
* $$
  \alpha\_i
  $$

  :

  股票 $i$ 的截距项，表示市场风险溢价为0时，股票的期望收益率。
* $$
  \beta\_{i,lag}
  $$

  :

  股票 $i$ 收益率对市场收益率滞后一期的敏感度（回归系数），反映了市场收益率前一期变动对股票当前收益率的影响。
* $$
  \beta\_{i,current}
  $$

  :

  股票 $i$ 收益率对当前市场收益率的敏感度（回归系数），表示当前市场收益率变动对股票当前收益率的影响。
* $$
  \beta\_{i,lead}
  $$

  :

  股票 $i$ 收益率对市场收益率超前一期的敏感度（回归系数），反映了市场收益率后一期变动对股票当前收益率的影响。
* $$
  \epsilon\_{i,t}
  $$

  :

  回归模型的残差项，代表了模型无法解释的股票收益率波动。
* $$
  {\beta}\_{Dimson}
  $$

  :

  Dimson调整贝塔，是对滞后、当前和超前市场风险溢价的贝塔系数之和，用于度量股票的系统性风险。

## 因子解释

Dimson调整贝塔旨在解决传统贝塔计算中，由于股票交易不频繁（或非同步交易）而导致的估计偏差。传统贝塔通常基于股票的日度收益率和市场日度收益率进行回归，但当股票交易不活跃时，这种方法可能无法准确反映股票对市场风险的敏感性。Dimson方法通过在回归模型中引入市场收益率的滞后项和超前项，来捕捉股票价格可能因交易不频繁而产生的延迟反应。通过对回归系数求和得到Dimson调整贝塔，它可以更好地反映股票在一段时间内的系统性风险暴露，尤其适用于交易不活跃或流动性较差的股票。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Dimson, Elroy. (1979). Risk measurement when shares are subject to infrequent trading. Journal of Financial Economics

## Related Factors

[### Frazzini-Pedersen 调整贝塔](/zh/factors/volatility/frazzini-pedersen-beta)[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### 下尾风险贝塔](/zh/factors/tech/tail-beta)[### 下行风险贝塔](/zh/factors/tech/downside-beta)[### 市场反应滞后因子](/zh/factors/tech/price-delay)[### Fama-French三因子模型残差动量](/zh/factors/tech/residual-momentum-ff3)[### 情绪敏感度因子](/zh/factors/emotion/sentiment-beta)[### 残差市值偏离度](/zh/factors/basic-surface/specific-market-capitalization)[### 系统性尾部风险暴露](/zh/factors/emotion/tail-risk)