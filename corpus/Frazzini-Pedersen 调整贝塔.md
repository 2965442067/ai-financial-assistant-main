# Frazzini-Pedersen 调整贝塔

波动率因子

## 因子公式

Frazzini-Pedersen 调整贝塔:

$$
\beta\_{FP} = \hat{\rho}\_{im} \frac{\hat{\sigma}\_i}{\hat{\sigma}\_m}
$$

其中：

* $$
  \hat{\sigma}\_i
  $$

  :

  过去 K 个月股票 *i* 的对数收益率标准差，衡量股票收益率的波动性。较高的值表示股票波动性较大，风险较高。通常使用过去12个月的数据。
* $$
  \hat{\sigma}\_m
  $$

  :

  过去 K 个月市场基准的对数收益率标准差，衡量市场收益率的波动性。较高的值表示市场波动性较大，系统性风险较高。通常使用过去12个月的数据。
* $$
  \hat{\rho}\_{im}
  $$

  :

  过去 Y 年股票 *i* 和市场基准日度收益率的相关系数。用于衡量股票收益率与市场收益率的线性相关程度。正值表示同向变动，负值表示反向变动。日度收益率采用三天重叠收益率计算，$\hat{r}*{it} = \frac{1}{3} \sum*{k=0}^{2} \log(1+R\_{t+k})$，其中 *R* 为日度收益率。使用重叠收益率可以提高相关性估计的稳定性，减轻单一日期收益率的噪声影响。一般情况下，Y取5年，以保证至少有750个有效日度收益率，从而得到更可靠的相关性估计。
* $K$

  :

  计算股票和市场收益率标准差所使用的时间窗口长度（以月为单位）。一般情况下，K 取 12 个月，以保证至少包含 120 个有效日度收益率，从而获得相对稳定的波动率估计。
* $Y$

  :

  计算股票和市场收益率相关系数所使用的时间窗口长度（以年为单位）。一般情况下，Y取5年，以保证至少有750个有效日度收益率。

## 因子解释

Frazzini-Pedersen 调整贝塔是对传统 CAPM 模型中贝塔系数的改进。传统贝塔的计算方法容易受到波动率估计误差的影响，尤其是在波动率较高或波动率变化频繁的股票上。该调整贝塔通过使用股票和市场收益率的标准差之比乘以二者的相关系数，来更准确地衡量股票的系统性风险。它不仅考虑了股票和市场之间的相关性，还考虑了它们各自的波动率。该因子试图解决传统贝塔在量化股票风险时可能存在的偏差，并提供更可靠的风险度量，从而提高投资组合构建和风险管理的有效性。特别地，该方法缓解了在波动率估计中存在的均值回归问题，使得高波动股票的贝塔值被低估，低波动股票的贝塔值被高估的现象得到改善，从而使得风险收益关系更加合理。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* [Frazzini, Andrea, and Lasse Heje Pedersen. (2014). Betting against beta. Journal of Financial Economics](https://doi.org/10.1016/j.jfineco.2013.10.005)

## Related Factors

[### 系统性风险暴露 (Market Beta)](/zh/factors/volatility/market-beta)[### Dimson调整贝塔](/zh/factors/tech/dimson-beta)[### 下行风险贝塔](/zh/factors/tech/downside-beta)[### 特异性收益波动因子](/zh/factors/emotion/specificity)[### 下尾风险贝塔](/zh/factors/tech/tail-beta)[### 个股特质波动率](/zh/factors/volatility/idiosyncratic-volatility)[### 高频价量相关性趋势因子](/zh/factors/tech/price-volume-correlation-trend)[### 残差偏度因子](/zh/factors/tech/idiosyncratic-skewness)[### 月度加权特质波动率](/zh/factors/volatility/monthly-idiosyncratic-volatility)