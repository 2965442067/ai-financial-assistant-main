# 资金流量累积指标 (A/D)

技术因子

## 因子公式

资金流量累积指标 (A/D):

$$
A/D\_t = A/D\_{t-1} + VOL\_t \* \frac{2 \* CLOSE\_t - HIGH\_t - LOW\_t}{HIGH\_t - LOW\_t}
$$

A/D指标是每日资金流量的累积值。其中，每日资金流量通过价格区间与收盘价的关系，再乘以成交量得出。

A/D指标的计算基于以下公式：

* $A/D\_t$

  :

  第t日的资金流量累积指标值。
* $A/D\_{t-1}$

  :

  第t-1日的资金流量累积指标值，初始值通常设为0。
* $VOL\_t$

  :

  第t日的成交量。
* $CLOSE\_t$

  :

  第t日的收盘价。
* $HIGH\_t$

  :

  第t日的最高价。
* $LOW\_t$

  :

  第t日的最低价。
* $\frac{2 \* CLOSE\_t - HIGH\_t - LOW\_t}{HIGH\_t - LOW\_t}$

  :

  每日的资金流量乘数 (Money Flow Multiplier), 该值在-1到1之间波动，代表了当日的资金流量方向和强度，当收盘价接近当日最高价时该乘数为正且接近1，表示当日买方力量强劲；反之，当收盘价接近当日最低价时该乘数为负且接近-1，表示当日卖方力量强劲。分子部分(2\*CLOSE\_t - HIGH\_t - LOW\_t)衡量了收盘价在当日价格区间的位置，分母部分(HIGH\_t - LOW\_t)则为当日的价格区间宽度。当HIGH\_t = LOW\_t时，为了避免除0错误，通常将此值设置为0，此时资金流量也为0，对A/D指标不产生影响。

## 因子解释

资金流量累积指标 (A/D) 通过每日的成交量和价格变动来衡量资金流向，从而反映市场买卖双方的力量对比。当A/D指标上升时，表明资金流入，买盘力量占主导，可能预示着价格上涨的潜力；当A/D指标下降时，表明资金流出，卖盘力量占主导，可能预示着价格下跌的风险。A/D指标与价格之间的背离现象，可以作为重要的交易信号参考。例如，当价格创新低而A/D指标没有创新低时（底背离），可能预示着买盘力量正在积聚，价格可能即将反转上涨；反之，当价格创新高而A/D指标没有创新高时（顶背离），可能预示着卖盘力量正在增强，价格可能即将反转下跌。因此，A/D指标不仅可以帮助识别趋势的强度，还可以发现潜在的价格反转点，属于成交量驱动的，领先指标。

## 参考资料

以下学术和行业资源为这个交易因子提供了额外的背景和验证。

* Martin J. Pring. (2008). 技术分析精解. 机械工业出版社

## Related Factors

[### 蔡金资金流向指标](/zh/factors/tech/caijin-currency-flow-indicator)[### 资金流量指标](/zh/factors/tech/money-flow-index)[### 方向性动量离散指标 (Directional Momentum Dispersion Index)](/zh/factors/tech/directional-standard-deviation)[### 动态趋向指标](/zh/factors/tech/dynamic-buy-sell-indicator)[### 阿隆指标](/zh/factors/tech/aroon-index)[### 移动平均汇聚背离指标](/zh/factors/tech/moving-average-convergence-divergence)[### 相对强弱人气指标](/zh/factors/tech/ar-indicator)[### 蔡金资金流量震荡指标](/zh/factors/tech/jiaqing-indicator)[### 累计振荡指标](/zh/factors/tech/accumulated-oscillation-index)