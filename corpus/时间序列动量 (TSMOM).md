# 时间序列动量 (TSMOM)

动量因子

## 因子公式

时间序列动量因子 (TSMOM):

$$
TSMOM\_{m,i} = sign\left(\frac{1}{N}\sum\_{j=1}^{12}\hat{r}\_{m-j,i}\right) \* \frac{\hat{r}\_{m,i}}{\hat{\sigma}\_{m,i}}
$$

个股超额收益:

$$
\hat{r}\_{m,i} = r\_{m,i} - \bar{r}\_{m,i}
$$

收益率指数移动平均:

$$
\bar{r}\_{m,i} = \sum\_{j=0}^{\infty}(1 - \delta) \* \delta^{j} \* r\_{m-j,i}
$$

收益率波动率:

$$
\hat{\sigma}\_{m,i} = \sqrt{\sum\_{j=0}^{\infty}(1-\delta) \* \delta^{j} \* (r\_{m-1-j,i} - \bar{r}\_{m-1-j,i})^2}
$$

其中：

* $$
  m
  $$

  :

  表示月份，用于标识时间序列数据中的特定时间点。
* $$
  i
  $$

  :

  表示特定的股票，用于标识横截面数据中的特定个体。
* $$
  \hat{r}\_{m,i}
  $$

  :

  表示股票 $i$ 在第 $m$ 个月相对其自身历史收益的超额收益。它是当月实际收益 $r\_{m,i}$ 与过去收益的指数移动平均值 $\bar{r}\_{m,i}$ 的差值。超额收益旨在捕捉个股收益相对于自身历史水平的偏差。
* $$
  r\_{m,i}
  $$

  :

  表示股票 $i$ 在第 $m$ 个月的收益率，通常定义为该月股票价格变动的百分比。
* $$
  \bar{r}\_{m,i}
  $$

  :

  表示股票 $i$ 在第 $m$ 个月之前月份收益率的指数移动平均值，用于平滑收益率的时间序列，并消除噪音，捕捉潜在的趋势。其计算方法是对历史收益率进行加权平均，权重随着时间推移呈指数衰减，使得近期收益率对当前移动平均值的影响更大。
* $$
  \hat{\sigma}\_{m,i}
  $$

  :

  表示股票 $i$ 在第 $m$ 个月的收益率波动率，它是过去收益率与指数移动平均值偏差的加权平均的平方根，其中权重随着时间推移呈指数衰减。该指标衡量了收益率在一段时间内的变动程度，反映了股票的风险水平。
* $$
  \delta
  $$

  :

  表示指数衰减系数，它是一个介于 0 和 1 之间的参数，决定了历史收益率对指数移动平均值的影响程度。越小的 $\delta$ 值表示历史收益率的衰减速度更快，使得移动平均值更关注近期收益率。
* $$
  N
  $$

  :

  表示用于计算过去收益均值的月数，此处为 12个月。$\frac{1}{N}\sum\_{j=1}^{12}\hat{r}\_{m-j,i}$ 代表了过去12个月的超额收益均值。

## 因子解释

时间序列动量 (TSMOM) 因子通过分析个股自身历史收益率的趋势来预测未来收益。其核心思想是，如果过去一段时间内个股表现出正（负）的超额收益，那么该趋势在未来有可能会持续（尽管研究表明通常是反向的）。该因子首先计算过去12个月的超额收益的均值，并取其符号作为方向性指标。然后，使用当月的超额收益除以当月的波动率，进行标准化处理。这样做的目的是使动量信号更加稳健，并且降低了高波动股票的权重。因此，TSMOM 因子可以用于捕捉股票价格的短期反转效应，并构建相应的投资组合。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H.. (2012). Time series momentum. Journal of Financial Economics
* 朱剑涛. (2017). 技术类新 Alpha 因子的批量测试. 东方证券

## Related Factors

[### 月度收益季节性动量因子](/zh/factors/emotion/seasonal-returns)[### 多时域移动平均动量因子](/zh/factors/tech/trend-factor)[### 过去K个月累计收益率动量因子](/zh/factors/momentum/momentum)[### 排序动量因子](/zh/factors/momentum/momentum-based-on-ranking)[### CAPM残差动量因子](/zh/factors/tech/residual-momentum-capm)[### 月度超额收益季节性反转因子](/zh/factors/momentum/seasonal-return-reversal)[### 多周期标准化移动平均动量因子](/zh/factors/tech/momentum-factor)[### 系统偏度风险溢价因子](/zh/factors/emotion/covariance-skewness2)[### Fama-French三因子模型残差动量](/zh/factors/tech/residual-momentum-ff3)