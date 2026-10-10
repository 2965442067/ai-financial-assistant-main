# 相对波动性指标（RVI）

技术因子

## 因子公式

计算上涨动量 UM，若当日价格高于前一日价格，则为过去 N1 日价格的标准差，否则为 0。

$$
UM(PRICE,N1) = IF(PRICE>PRICE[1], STD(PRICE,N1),0)
$$

计算下跌动量 DM，若当日价格低于前一日价格，则为过去 N1 日价格的标准差，否则为 0。

$$
DM(PRICE,N1) = IF(PRICE<PRICE[1],STD(PRICE,N1),0)
$$

计算平均上涨动量 UA，对当前上涨动量 UM 进行指数移动平均（EMA）平滑，N2 为平滑窗口大小。

$$
UA(N2) = (UA[1]\*(N2-1)+UM)/N2
$$

计算平均下跌动量 DA，对当前下跌动量 DM 进行指数移动平均（EMA）平滑，N2 为平滑窗口大小。

$$
DA(N2) = (DA[1]\*(N2-1)+DM)/N2
$$

计算相对强度 RS，为平均上涨动量 UA 在总动量（UA+DA）中所占的百分比。

$$
RS(PRICE) = 100\*UA/(UA+DA)
$$

计算相对波动性指标 RVI，为高价相对强度 RS 和低价相对强度 RS 的平均值。

$$
RVI = (RS(HIGH)+RS(LOW))/2
$$

计算 UA 的初始值，对 UM 进行简单移动平均（SMA）平滑，N 为平滑窗口大小。

$$
UA初始值 = SMA(UM,N)
$$

计算 DA 的初始值，对 DM 进行简单移动平均（SMA）平滑，N 为平滑窗口大小。

$$
DA初始值 = SMA(DM,N)
$$

若平均上涨动量 UA 和平均下跌动量 DA 之和为零，为避免除零错误，则令 RVI = 0。

其中:

* $PRICE$

  :

  当前交易周期的收盘价格，可以是日线、小时线等。
* $PRICE[1]$

  :

  前一个交易周期的收盘价格。
* $STD(PRICE,N1)$

  :

  过去 N1 个交易周期价格的标准差，用于衡量价格的波动程度，N1 通常取10。
* $N$

  :

  计算 UA 和 DA 初始值时所用的简单移动平均（SMA）窗口大小，表示平均动量的初始平滑周期，通常取 5。
* $N1$

  :

  计算价格标准差的窗口大小，表示衡量价格波动性的周期长度，通常取 10。
* $N2$

  :

  计算平均动量 UA/DA 的指数移动平均（EMA）平滑窗口大小，表示平均动量的平滑周期，通常取 20。
* $UM$

  :

  上涨动量（Upward Momentum），当价格上涨时，使用标准差来表征上涨的力度；否则为 0。
* $DM$

  :

  下跌动量（Downward Momentum），当价格下跌时，使用标准差来表征下跌的力度；否则为 0。
* $UA$

  :

  平均上涨动量（Average Upward Momentum），是对上涨动量 UM 的平滑处理，采用指数移动平均 EMA 方式计算，反映上涨力度的持续性。
* $DA$

  :

  平均下跌动量（Average Downward Momentum），是对下跌动量 DM 的平滑处理，采用指数移动平均 EMA 方式计算，反映下跌力度的持续性。
* $RS$

  :

  相对强度（Relative Strength），表示平均上涨动量在总动量中所占的比例，体现多头力量的相对强弱。
* $RVI$

  :

  相对波动性指标（Relative Volatility Index），通过高低价的相对强度计算得出，用于判断价格波动方向和潜在的趋势反转。
* $SMA$

  :

  简单移动平均（Simple Moving Average），用于平滑数据，计算方法为指定窗口期内数据的算术平均值。

## 因子解释

RVI 指标的计算方法借鉴了相对强弱指标（RSI）的思路，但核心区别在于 RVI 使用价格的标准差而非价格本身来衡量动量。RVI 通过分析价格波动（而非价格水平）来判断市场的多空力量，当 RVI 值较高时，表明上涨动量增强，可能预示着价格上涨；反之，当 RVI 值较低时，表明下跌动量增强，可能预示着价格下跌。RVI 通常与移动平均线等趋势指标结合使用，以增强交易决策的准确性，避免在震荡行情中产生过多无效信号，RVI指标能够更加灵敏地捕捉价格的波动和趋势变化。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* 佚名. 相对波动性指数(RVI)的计算方法和交易策略. 互联网资源

## Related Factors

[### 成交量相对强度指标](/zh/factors/tech/volume-relative-strength)[### 区域强度指数](/zh/factors/tech/region-index)[### 成交量相对强度指标](/zh/factors/tech/volume-ratio-indicator)[### 相对强弱指标 (Relative Strength Index)](/zh/factors/tech/rsi)[### 相对强弱指标 (RSI)](/zh/factors/tech/relative-strength-index)[### 佳庆波动率离散指标](/zh/factors/tech/jiaqing-discrete-index)[### 蔡金波动率指标 (Chaikin Volatility Index)](/zh/factors/tech/cvi)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 随机摆动指标](/zh/factors/tech/stochastic-indicator)