# 过去K个月累计收益率动量因子

动量因子

## 因子公式

MOM(K) = ∑\_{t=1}^{K} r\_{t}

$$
MOM(K) = \sum\_{t=1}^{K} r\_{t}
$$

其中:

* $MOM(K)$

  :

  过去K个月的累计收益率动量因子
* $K$

  :

  动量计算的回溯期，以月为单位。例如，K=6 表示计算过去6个月的累计收益率。
* $r\_t$

  :

  第t个月的月度收益率，等于该月月末收盘价除以该月月初收盘价减1，即 (P\_end - P\_begin) / P\_begin 。

## 因子解释

该动量因子旨在捕捉股票价格的惯性趋势。具体来说，如果一只股票在过去K个月内积累了较高的正收益率，则认为其具有较强的上涨动量，未来一段时间内可能继续上涨。反之，如果一只股票在过去K个月内积累了较高的负收益率，则认为其具有较强的下跌动量，未来一段时间内可能继续下跌。 该因子可以作为选股策略中的一个重要组成部分，配合其他因子使用，以提高投资组合的收益和风险调整后的表现。需要注意的是，动量效应并非在所有市场环境下都有效，且可能存在反转风险。因此，在使用该因子时，需要结合市场情况和风险偏好进行综合考虑。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Jegadeesh, Narasimhan, and Sheridan Titman. (1993). Returns to buying winners and selling losers: Implications for stock market efficiency. Journal of Finance 48, 65-91

## Related Factors

[### 动量加速度因子](/zh/factors/momentum/momentum-acceleration)[### CAPM残差动量因子](/zh/factors/tech/residual-momentum-capm)[### 月度收益季节性动量因子](/zh/factors/emotion/seasonal-returns)[### 时间序列动量 (TSMOM)](/zh/factors/momentum/time-series-momentum)[### 排序动量因子](/zh/factors/momentum/momentum-based-on-ranking)[### 多周期标准化移动平均动量因子](/zh/factors/tech/momentum-factor)[### 多时域移动平均动量因子](/zh/factors/tech/trend-factor)[### 20日区间收益率动量/反转因子](/zh/factors/tech/momentum-or-reversal)[### 行业领头羊动量溢价因子](/zh/factors/emotion/industry-momentum-factor)