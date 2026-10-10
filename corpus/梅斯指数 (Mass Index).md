# 梅斯指数 (Mass Index)

技术因子

## 因子公式

梅斯指数计算公式：

$$
MassIndex\_t = \frac{EMA\_9(HIGH\_t - LOW\_t)}{EMA\_9(EMA\_9(HIGH\_t - LOW\_t))}
$$

公式说明:

* $HIGH\_t$

  :

  第t个交易日的最高价
* $LOW\_t$

  :

  第t个交易日的最低价
* $EMA\_9(X)$

  :

  以X为输入，计算周期为9的指数移动平均。其中X可以是(HIGH\_t - LOW\_t) 或者 EMA\_9(HIGH\_t - LOW\_t)

## 因子解释

梅斯指数通过分析价格波动范围（当日最高价与最低价之差）的变化来识别潜在的趋势反转点。 具体而言，该指标首先计算当日最高价与最低价之差，然后对其进行两次指数移动平均平滑处理（首次平滑处理和二次平滑处理）; 再通过第一次平滑后的结果除以第二次平滑后的结果,得到最终的梅斯指数值。 当梅斯指数值出现显著上升或下降，并伴随着价格波幅的扩张或收缩时，通常被视为潜在趋势反转的信号。例如，当梅斯指数先下降后反弹，并且同时价格波动幅度开始收缩时，可能预示着先前趋势的结束和新趋势的开始。该指标主要应用于寻找超买或超卖区域后的价格反转，特别是在价格出现快速上涨或下跌之后, 可以辅助判断趋势的持续性或反转可能性。与单纯的价格波动幅度相比，梅斯指数通过指数移动平均降低了噪音，更加关注价格波动幅度的趋势变化，从而提供更清晰的趋势反转信号。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* John Murphy. (1999). 技术分析指标大全. Technical Analysis of the Financial Markets

## Related Factors

[### 区域强度指数](/zh/factors/tech/region-index)[### 移动平均汇聚背离指标](/zh/factors/tech/moving-average-convergence-divergence)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)[### 商品通道指数](/zh/factors/tech/commodity-channel-index)[### 三重指数移动平均 (TEMA)](/zh/factors/tech/triple-exponential-moving-average)[### 多周期标准化移动平均动量因子](/zh/factors/tech/momentum-factor)[### 成交量异同移动平均线 (VMACD)](/zh/factors/tech/volume-moving-average-convergence-divergence)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)