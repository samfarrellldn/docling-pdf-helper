## Deutsche Bank Research

Global

## Foreign Exchange FX Special Report

## Month-end hedging flows and FX returns

- ■ In this report we investigate the impact of month-end hedging demand on FX returns. By looking at the holdings and performance of foreign assets, we estimate monthly hedging demand for eleven major currencies. We then evaluate its impact on spot FX heading into the 4pm London fix on the final trading day of every month.
- ■ We find a significant relationship between equity market outperformance and FX returns at the end of a month. When a region's equity market significantly underperforms in a given month, the net FX demand from equity investors (who need to buy back that regions' currency to remain fully FX-hedged) is large enough to have an impact on spot FX. Our results also suggest divergence across currencies, with EUR, JPY and GBP the most  sensitive  and  AUD,  BRL  and  INR  the  least  sensitive  to  hedging demand.
- ■ The results are also economically significant. A strategy that buys the currency with the highest demand and sells the currency with the lowest demand gives a historical Sharpe ratio of 0.66. A strategy that buys (sells) each currency with positive (negative) demand gives an average historical Sharpe ratio of 0.44.
- ■ For fixed income however, our results are not as strong. The FX-hedging of  long-term  bonds  does  not  appear  to  have  a  significant  impact  on FX returns for any of the eight developed markets we look at, with the exception of the Euro.

Date 29 October 2018

## Rohini Grover

Strategist

+44-20-754-75907

## Shreyas Gopal

Strategist

+44-20-754-51501

| Demand for September   |   Pctile Rank (2000- present) |   Pctile Rank (last three years) |         |
|------------------------|-------------------------------|----------------------------------|---------|
| AUD                    |                            72 |                               81 |         |
| CAD                    |                            51 |                               50 | Highest |
| CHF                    |                            56 |                               47 |         |
| USD                    |                            56 |                               58 |         |
| EUR                    |                            29 |                               25 |         |
| JPY                    |                            36 |                               36 |         |
| KRW                    |                            47 |                               47 |         |
| GBP                    |                            28 |                               11 | Lowest  |
| SEK                    |                            20 |                                0 |         |

Based on our estimated hedging demand, our strategy would be long AUD/SEK

## Regression betas: Sensitivity of FX returns to the hedging of equity exposure

<!-- image -->

7T2se3r0Ot6kwoPa

<!-- image -->

## Introduction

The  US  equity  markets  bottomed  in  2009  but  thereafter  have  consistently outperformed the rest of the world. During this period, US assets have formed a large part of the portfolios of both US and non-US investors. Such a large exposure to US assets implies that foreign investors will have had to sell dollars to keep their portfolios completely FX-hedged.

If such hedging flows were spread out across the month, their impact on spot FX rates would likely be limited. However, the fact that a vast majority of these hedging trades are concentrated on the final business day of the month increases the  price  impact.  In  this  report,  we  investigate  this  month-end  relationship between equity and currency markets using data for eleven regions from January 2000 to September 2018. The markets we cover are the US, Eurozone, UK, Japan, Switzerland,  Sweden,  Canada,  Australia,  South  Korea,  Brazil  and  India.  For  a slightly reduced set of countries we also investigate the relationship between fixed income hedging flows and FX.

Melvin  and  Prins  (2015)  outline  an  institutional  feature  of  the  FX  market  that provides a neat framework to test the impact of hedging demand on exchange rates.  This  institutional  feature  is  the  4pm  London  fix  and  is  when  the  daily benchmark price of each currency is determined. These rates are also used to value international portfolios, with a concentration of hedging trades around the 4pm fix  on  the  last  trading  day  of  each  month.  Focusing  on  the  hedging  of equities, they find that on average a 10% equity market underperformance leads to a 20bp rally in the currency in the hours before the fix.

As an example, in October and November  last year, Eurozone stocks underperformed US stocks by 1.3 and 2.1 percentage points respectively.  1 . Figure 1 shows the intraday moves in EUR/USD for October 31, 2017 and November 30, 2017, with the US dollar selling off against the euro heading into the 4pm fix as predicted by the relative equity performances.

Source: Deutsche Bank. Bloomberg Finance LP

<!-- image -->

<!-- image -->

We  adopt  a  very  similar  framework  to  test  the  price  impact  of  hedging demand on currency returns, differing in only a few regards. First, we estimate this relationship individually for each region and its corresponding USD-cross. Second, we extend the framework to also include larger emerging markets that have consistently held a greater than 1% share in the world equity market in the  sample  period.  We  test  the  economic  significance  of  this  relationship  by backtesting two strategies. Finally, we repeat the exercise for fixed income, using a very similar framework to assess whether there is a relationship between the FX-hedging of bonds and currency returns. 2

Our results suggest that there is indeed a significant relationship between equity market outperformance and FX returns at the end of a month. When a region's equity market significantly underperforms in a given month, the net FX demand from equity investors (who need to buy back that regions' currency to remain fully FX-hedged) is large enough to have an impact on spot FX. Our results also suggest divergence across currencies, with EUR, JPY and GBP the most sensitive, while AUD, BRL and INR appear the least sensitive to hedging demand (all vs. USD). On the fixed income side however, we only find a significant price impact of bond market outperformance for one currency, EUR.

## Measuring currency demand from the hedging of equities

Institutional investors are often restricted in the amount of FX-risk they can take. When a foreign equity market outperforms their domestic market, this brings with it fresh, unhedged FX exposure. To reduce transaction costs, portfolio managers reduce this FX risk at discrete intervals such as the end of every month, rather than continuously. Strictly speaking, these portfolio managers can eliminate fresh FX-risk indirectly by selling some of their foreign equities, rather than re-hedging in the FX market directly. But if we assume the money from selling equities is then converted back to domestic currency, then the two should be equivalent in terms of FX impact.

In this report we therefore assume that relative equity market outperformance during a month leads to a direct re-hedging of FX risk (through FX forwards) rather than indirectly through transactions in the equity market. The question we are addressing in this report is to what extent this currency demand impacts spot FX rates heading into the 4pm London fix on the final business day of each month. This section lays out our framework for estimating this price impact, and very closely follows the work of Melvin and Prins (2015).

An initial starting point would be to look at the direct relationship between monthend  FX  returns  and  the  equity  performance  in  that  month.  For  example,  it  is reasonable to assume that as the S&amp;P 500 outperforms the Euro Stoxx by an increasing margin, EUR/USD should rally further on the final day of the month, as portfolio managers have to sell more dollars. But a regression of FX returns on equity performance is too simplistic, as this relationship will also be dependent on the amount of foreign asset investment. For example, in the extreme scenario where US investors hold no European assets, and European investors hold no US assets, then there will be no end-of-month FX hedging required, and thus no

2 Here we only include the following bond markets and FX returns: Germany (proxy for Eurozone), United States, Japan, United Kingdom, Canada, Australia, Switzerland, and Sweden.

<!-- image -->

impact on spot FX returns. Our analysis therefore controls for each country's level of foreign equity holdings (see below).

Our next consideration is which equity markets and currencies to include in our analysis.  We  choose  to  include  any  regions  whose  equity  markets  constitute around 1% or more of the MSCI World Index, since regions with less than this share are unlikely to see their currencies impacted through the hedging of their equities for two reasons. Firstly, foreigners, almost by definition, will hold very little  of  these  stocks  in  their  portfolios  and  as  such  the  absolute  amount  of its currency that could be demanded is limited. Secondly, the countries whose equities  markets  are  this  small  are  in  general  unlikely  to  themselves  hold  a significant amount of foreign equities, and thus we can exclude them without much loss.

All  of  the  G10  regions  apart  from  Norway  and  New  Zealand  satisfy  our  1% criterion.  Including  emerging  market  currencies  however  brings  with  it  some tradeoffs.  The  four  largest  EM  players  in  equity  space  this  century  have  been China, India, Brazil and South Korea. We exclude China from our analysis due to limited data availability. 3  Since India and Brazil only reached the 1% threshold in the mid 2000s, our sample and analysis for these countries starts in 2005 rather than 2000 ( Figure 2 ).

Figure 2: In EM space only South Korea has consistently formed &gt;1% of world equity markets since 2000

<!-- image -->

Our final set of chosen equities therefore includes the following regions: Australia, Brazil, Canada, Eurozone, India, Japan, Sweden, Switzerland, South Korea, United Kingdom, and United States. Since the start of the century these eleven regions have on average constituted 85% of the total world equity market and our sample contains monthly data from January 2000 until September 2018. 4

The next step is to find out how many foreign equities are held by each of our chosen regions. Using December 2017 Coordinated Portfolio Investment Survey data we estimate, for each of the eleven countries in our sample, the dollar value

3 CNH data is only available from 2010 onwards

4 From January 2005 for Brazil and India

<!-- image -->

of holdings of equities from the other ten regions. As Table 1 shows, the total holdings of foreign equities across our nine regions sums to $14 trillion.

So out of the US' $5.6 trillion of foreign equities, how much is allocated to each country? Rather than just using the bilateral CPIS data that is both noisy (largely due to FX moves) and infrequent (only reported twice a year), we assume that the  US'  foreign  equities  are  invested  in  proportion  to  the  market  cap  of  that region at that point in time. To be clear, if Japan's share of world equity market capitalisation (excluding US) was 20% in March 2015 and 10% in March 2018, we estimate that US holdings of Japanese equities were $1.12 trillion and $0.56 trillion respectively.

Table 1: Canadian investors invest abroad the most relative to the size of their domestic market; Korean the least

|       | Holdings of foreign equities   | Market capitalisation of home equity index   | Share of total foreign holdings   | Domestic market size (fraction of MSCI world)   |
|-------|--------------------------------|----------------------------------------------|-----------------------------------|-------------------------------------------------|
| US    | 5,559,984                      | 25,174,080                                   | 40%                               | 44%                                             |
| EU    | 3,143,104                      | 6,754,642                                    | 22%                               | 12%                                             |
| UK    | 1,798,188                      | 2,824,520                                    | 13%                               | 5%                                              |
| CA    | 1,119,267                      | 1,654,625                                    | 8%                                | 3%                                              |
| JN    | 879,123                        | 4,797,575                                    | 6%                                | 8%                                              |
| SZ    | 605,283                        | 1,361,292                                    | 4%                                | 2%                                              |
| SW    | 266,403                        | 494,033                                      | 2%                                | 1%                                              |
| AU    | 386,373                        | 1,118,120                                    | 3%                                | 2%                                              |
| KR    | 199,578                        | 1,302,709                                    | 1%                                | 2%                                              |
| BR    | 17,570                         | 703,224                                      | 0%                                | 1%                                              |
| IN    | 1,111                          | 1,288,185                                    | 0%                                | 2%                                              |
| Total |                                |                                              | All figures USD mlns, Dec 2017    | All figures USD mlns, Dec 2017                  |

Source: Deutsche Bank, Haver Analytics, Bloomberg Finance LP

We assume that on the final business day of every month equity investors transact in the foreign exchange market to remain fully FX-hedged. In other words, we assume their mandates only allow for equity-market risk. Now we can translate foreign  equity  market  outperformance into a "hedging flow" variable for each currency. This flow variable is composed of demand from domestic investors and supply from foreigners. The following example shows how net flow for Euros is calculated, assuming the Eurozone as the domestic region:

1. Domestic investors: Firstly, given a positive return in the non-European markets  (S&amp;P  500,  FTSE  100  etc),  domestic  investors  will  need  to buyback Euros and sell more foreign currency to fully hedge their nonEuro denominated stocks. This generates demand for Euros.
2. Foreign investors: However, when Euro-denominated stocks have also generated a positive return, foreign investors will have to sell Euros to re-hedge their FX exposure to these stocks. This happens for all nonEurozone investors who hold Eurozone stocks, and generates a supply of Euros on the final day.

Therefore the net Euro flow on the final day of the month will be the net of the demand and supply of Euros: (1) - (2).

To make this clearer, consider a three region example where the respective equity market returns up to the final day of the month have been +5% for US, +2% for UK, and -5% for Eurozone stocks. On the domestic side, Eurozone investors will need to sell GBP and USD on account of the positive equity returns in these regions.

<!-- image -->

Since they will be swapping these currencies in exchange for Euros, this leads to positive euro demand. On the foreign side, since there has been a negative return on the Eurozone stocks, both UK and US investors will need to buy back Euros to avoid being over-hedged. Hence, in this extreme case there will be a large positive net hedging flow in EUR (and large negative flow in USD).

In  practice,  we  look  at  the  return  of  each  country's  equity  index  relative  to the MSCI world index rather than on a bilateral basis. For example, in August 2018, the MSCI Europe underperformed the MSCI world index by 4.7 percentage points 5 . We also know that Eurozone holdings in the other 10 markets amounts to roughly $3.1 trillion. Using formulae from Melvin and Prins, we estimate that, total net demand for Euros for the purpose of FX-hedging equity exposure on 31st August will have been $75 billion.  6

Indeed, since the start of the century, our basket of Eurozone stocks is actually down ten percent while the US stock market has almost doubled. The Japanese market is broadly unchanged. The consequence of this US outperformance has been a glut of dollars, supplied at the end of the months as both US and nonUS portfolio managers sell the greenback in order to rehedge their FX exposure. ( Figure 3 and Figure 4 )

<!-- image -->

<!-- image -->

Source: Deutsche Bank, Bloomberg Finance LP

Source: Deutsche Bank, Bloomberg Finance LP

<!-- image -->

<!-- image -->

Now that we've estimated the net flow for each currency at the end of the month based on portfolio holdings and relative equity market performance, the question is  then  whether  these  flows  have  a  statistically  and  economically  significant impact on spot FX. In other words, what is the price impact of this month end hedging?

Of course, the price impact will depend not only on the net demand, but also the liquidity of that currency. For example, a month-end net flow of $75 billion will have more of a price impact in say, KRW, than in EUR. We control for these liquidity differences using data from the BIS triennial surveys (from 2001-2016), scaling net demand by the estimated daily turnover (in spot and forwards) in that currency.

This final "liquidity-adjusted net demand" or " LAND " is now the key variable with which we can estimate the spot FX impact of month-end equity portfolio hedging. As shown by Figure 9 , once adjusting the superior liquidity in US dollars, the cumulative supply of USD at month's end looks less extreme than in Figure 4 .

Source: Deutsche Bank, Haver Analytics

Figure 9: Relative to its liquidity, sterling has seen the highest demand and the ends of months among the majors

Source: Deutsche Bank, Haver Analytics

Figure 11: Relative to its liquidity, INR has been by far the most offered currency from an equity-hedging perspective

<!-- image -->

Source: Deutsche Bank, Haver Analytics

<!-- image -->

## How to measure net currency demand from hedging bonds

Our  approach  for  fixed-income  is  very  similar  to  the  method  outlined  above for  equities,  but  with  one  key  difference.  Due  to  limited  data  availability  for aggregate  bond  indices,  we  focus  on  the  price  performance  of  a  constant maturity, 10 year government bond for each country. This is consistent with the methodology  used  in  our  capital-based  FX  valuation  model  .  Specifically,  we estimate  bilateral  hedging  flows  between  a  domestic  country  and  each  of  its foreign  counterparts  (based  on  CPIS  data).  This  time,  we  focus  solely  on  the following economies and currencies: US, Eurozone, Japan, UK, Canada, Australia, Sweden and Switzerland.  7

7 The major difference between our equity and fixed-income methodology is that for the former we are able to adjust the CPIS holding data by the relative market capitalisations at that point in time , providing a more robust estimate of cross-border asset holdings. For fixed income, we must be content with simply using the most recent CPIS data at a given point in time, which can be many months out of date.

Figure 10: While CHF has seen least net selling or buying pressure relative to its liquidity

<!-- image -->

Source: Deutsche Bank, Haver Analytics

<!-- image -->

We  return  to  August  2018  to  provide  an  example.  We  use  Germany  as  a (imperfect)  proxy  for  Eurozone  fixed  income  performance.  In  this  month,  the return on a 10 year German government bond was 0.95%, compared to 0.9% for the equivalent US bond. Furthermore, we know that as of December last year, Eurozone investors' holdings of USTs was roughly $1.6 trillion and US investors holdings of Euro-denominated bonds was $0.6 trillion. Using these figures we can estimate the demand for Euros coming from the hedging of foreign bonds between the two regions.

Firstly, European investors will need to buy back Euros and sell dollars due to the positive return on their holdings of US bonds. We estimate this amount to be €12.5 billion (0.9% * 1,600,000,000 * 0.862). On the flipside, US investors will be selling Euros to the tune of €5 billion (0.95% * 600,000,000 * 0.862). 8 Hence, if the US and the Eurozone were the only regions included in our universe, we estimate that the total net hedging flow for Euros at the end of August, coming from the hedging of long-term fixed income securities, was +€5 billion. Repeating the exercise for Eurozone and the other countries in our universe (listed above) gives us the total net hedging flow for Euros. Once we have our estimates for month-end net hedging flows in each of our currencies, the final step is to once again adjust them for liquidity.

Figure 12 to Figure 15  show the cumulative net demand for each currency since 2000  (both  raw  and  liquidity-adjusted),  based  on  the  respective  bond  market performances. For example, the persistent end-of-month net selling pressure seen for EUR is a result of the historically low German bond yields.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Results: US equity outperformance has led to a weaker dollar versus euro, yen and sterling

## How does liquidity-adjusted net demand (LAND) affect exchange rates?

After computing our net demand variable for each currency as described above, we check whether it can be used to predict currency returns on the last day of the month. We regress the pre-fix (London open to 4pm fix) returns for each currency (against the dollar)  on  the  last  trading  day  of  the  month  against  the  liquidityadjusted net demand for the currency derived from relative moves in country equity returns up until the second last day of the month.

The regression betas in Figure 15 represent the change in the underlying currency from London morning to 4pm fix, in basis points (bps), for a 10% increase in LAND. For example, a 10% increase in demand for euro would be associated with a 49 bps rally in the euro against the dollar.

The  results  show  a  consistent  pattern  whereby  LAND  positively  leads  pre-fix currency  returns  for  a  majority  of  currencies.  This  suggests  that  currencies demanded by hedgers tend to appreciate in the pre-fix period on the last trading day of the month. Most bars are coloured in to show their betas are statistically significant at the 1% level.

Among the major economies, EUR tends to appreciate the most at around 49 bps followed by JPY and GBP that appreciate by 39 and 33 bps respectively. Among the other markets, SEK tends to appreciate the most by around 25 bps, CAD by 10 bps, CHF by 6 bps and KRW by 3 bps. AUD, BRL and INR are the three currencies that depreciate in the pre-fix period but the impact is not statistically significant. This is broadly consistent with existing studies that find EUR, JPY, GBP and CHF returns exhibit a negative relationship with relative equity returns and other smaller currencies (including AUD and CAD) exhibit a positive relationship.

One thing to consider from these results is why EUR, JPY and GBP appear the most sensitive to their equity markets underperformance. Figure 3 &amp; Figure 4 in conjunction may go some way to explain this result. Not only have these equity markets underperformed the world since 2000, driving month-end EUR, JPY and

GBP demand, but at the same time US outperformance has concurrently led to a net selling pressure in USD. Not only did portfolio managers need to buy EUR, JPY and GBP, but they also often needed to sell USD (probably often versus EUR, JPY and GBP given their larger financial openness), possibly accentuating the price impact in these FX pairs.

Figure 15: Regression betas (statistically significant betas are shaded)

<!-- image -->

Source: Deutsche Bank. Shaded bars indicate statistical significance at the 1% level (p-value ≤ 0.01).

## Is this relationship economically significant?

Having  established  that  demand  for  hedging  flows  is  informative  for  future currency  returns,  we  now  check  its  economic  significance.  We  use  both  a sorted portfolio approach and a single currency approach for our analysis. For the portfolio approach, we sort the currencies 9 in ascending order based on the month-end demand variable (computed from equity returns up until the second to last day of the month) ranging from P1 to P9, and go long (versus the dollar) the currency at the top (P(9), and short the currency at the bottom (P1).  10  The position is held from London morning until the 4 pm fix on the last trading day of each month. Figure 16 shows the returns for the strategy before transaction costs. The strategy implies a Sharpe ratio of 0.66 and has a hit rate of 59%.

9 We exclude both INR and BRL since their demand variables can only be estimated for a much shorter time period and therefore may not be very robust.

10Note that we include the demand for dollar in our strategy and if the demand for dollar is highest/ lowest we buy or sell only a single currency against the dollar.

<!-- image -->

<!-- image -->

For the single currency approach, we go long a given currency when its monthend  hedging  demand  is  positive  (&gt;=0)  and  go  short  the  currency  when  this demand is negative (&lt;0). The position is taken from London morning of the last trading  day  of  the  month  until  the  4pm  fix  later  that  day.  Figure  17  &amp;  Figure 18 show the cumulative returns and Sharpe ratios across all currencies before transaction costs. The results from both the above analysis and strategies suggest that the regression coefficients have economic as well as statistical significance.

Source: Deutsche Bank.

<!-- image -->

<!-- image -->

<!-- image -->

## Results: Only the EU bond market performance has a significant impact

We replicate our analysis for the bond market with a few modifications to the computation of our demand variable . We find that bond market outperformance does not have a significant impact on the FX market, with the exception of the European bond market. We find that EUR is the only currency that appreciates significantly, by around 25 bps ( Figure 19 ). For a much smaller set of countries, 11 we  look  at  the  performance  of  their  corresponding  aggregate  bond  indices and repeat our analysis using the methodology outlined for equity markets. In line  with  our  previous  results,  we  do  not  find  any  significant  impact  of  bond outperformance on FX markets.

Figure 19: Regression betas (statistically significant betas are shaded)

<!-- image -->

<!-- image -->

## Conclusion

In this report we have outlined a framework for explaining some of the month-end dynamics that we observe in the FX market. Specifically, we have investigated the impact of the hedging of equity and bond exposure upon spot FX rates in the hours before the 4pm WM London fix. Our results show that since the turn of the century hedging demand from equity exposure has had the greatest price impact on EUR/USD, USD/JPY and GBP/USD - in spite of the high liquidity in these pairs. By contrast, there appears to be no significant impact on spot FX from the hedging of fixed income exposure for the majority of currencies we investigated. Going forward we aim to predict which currencies are most likely to strengthen or weaken versus the US dollar heading into the fix on the final day of every month, based on that month's equity market returns.

We would like to thank George Saravelos, Robin Winkler and Oliver Harvey for their  comments  and  suggestions.  We  would  also  like  to  thank  Jalaj  Singh  for infrastructure support.

<!-- image -->

## References

Fidora, M., Fratscher M., and Thimann, C., (2007) Home bias in global bond and equity markets: The role of real exchange rate volatility, Journal of International Money and Finance, 26(4), pp. 631-655

Melvin, M. and Prins, J. (2015) Equity hedging and exchange rates at the london 4 p.m. fix,Journal of Financial Markets 22, 50-72.

<!-- image -->

## Appendix 1

## Important Disclosures

## *Other information available upon request

*Prices  are  current  as  of  the  end  of  the  previous  trading  session  unless  otherwise  indicated  and  are  sourced  from local exchanges via Reuters, Bloomberg and other vendors . Other information is sourced from Deutsche Bank, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/CompanySearch. Aside from within this report,  important  risk  and  conflict  disclosures  can  also  be  found  at  https://research.db.com/Research/Topics/Equities? topicId=RB0002. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Rohini Grover, Shreyas Gopal

<!-- image -->

## Additional Information

The information and opinions in this report were prepared by Deutsche Bank AG or one of its affiliates (collectively "Deutsche Bank"). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, Deutsche Bank makes no representation as to its accuracy or completeness. Hyperlinks to thirdparty websites in this report are provided for reader convenience only. Deutsche Bank neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of Deutsche Bank in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a Deutsche Bank analyst, Deutsche Bank may act as principal for its own account or as agent for another person.

Deutsche Bank may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within Deutsche Bank, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. Deutsche Bank issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. Deutsche Bank and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of Deutsche Bank AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of Deutsche Bank and are subject to change without notice. Deutsche Bank provides liquidity for buyers and sellers of securities issued by the companies it covers. Deutsche Bank research analysts sometimes have shorter-term trade ideas that may be inconsistent with Deutsche Bank's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website ( https://research.db.com/Research/ ) , and can be found on the general coverage list and also on the covered company ' s page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with Deutsche Bank salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. Deutsche Bank has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals. Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently imprecise and a product of the analyst ' s judgment. The financial instruments discussed in this report may not be suitable for all investors, and investors must make their own informed investment decisions. Prices and availability of financial instruments are subject to change without notice, and investment transactions can lead to losses as a result of price fluctuations and other factors. If a financial instrument is denominated in a currency other than an investor's currency, a change in exchange rates may adversely affect the investment. Past performance is not necessarily indicative of future results. Performance calculations exclude transaction costs, unless otherwise indicated. Unless otherwise indicated, prices are current as of the end of the previous trading session and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Data is also sourced from Deutsche Bank, subject companies, and other parties.

The Deutsche Bank Research Department is independent of other business divisions of the Bank. Details regarding our organizational arrangements and information barriers we have to prevent and avoid conflicts of interest with respect to our research are available on our website ( https://research.db.com/Research/ ) under Disclaimer.

<!-- image -->

<!-- image -->

Macroeconomic fluctuations often account for most of the risks associated with exposures to instruments that promise to  pay  fixed  or  variable  interest  rates.  For  an  investor  who  is  long  fixed-rate  instruments  (thus  receiving  these  cash flows),  increases  in  interest  rates  naturally  lift  the  discount  factors  applied  to  the  expected  cash  flows  and  thus cause  a  loss.  The  longer  the  maturity  of  a  certain  cash  flow  and  the  higher  the  move  in  the  discount  factor,  the higher will  be  the  loss.  Upside  surprises  in  inflation,  fiscal  funding  needs,  and  FX  depreciation  rates  are  among  the most common adverse macroeconomic shocks to receivers. But counterparty exposure, issuer creditworthiness, client segmentation, regulation (including  changes  in  assets  holding  limits  for  different  types  of  investors),  changes  in  tax policies, currency convertibility (which may constrain currency conversion, repatriation of profits and/or liquidation of positions), and settlement issues related to local clearing houses are also important risk factors. The sensitivity of fixedincome instruments to macroeconomic shocks may be mitigated by indexing the contracted cash flows to inflation, to FX depreciation, or to specified interest rates - these are common in emerging markets. The index fixings may - by construction - lag or mis-measure the actual move in the underlying variables they are intended to track. The choice of the proper fixing (or metric) is particularly important in swaps markets, where floating coupon rates (i.e., coupons indexed to a typically short-dated interest rate reference index) are exchanged for fixed coupons. Funding in a currency that differs from the currency in which coupons are denominated carries FX risk. Options on swaps (swaptions) the risks typical to options in addition to the risks related to rates movements.

Derivative transactions  involve numerous  risks  including  market,  counterparty  default  and  illiquidity risk.  The appropriateness of these products for use by investors depends on the investors' own circumstances, including their tax position, their regulatory environment and the nature of their other assets and liabilities; as such, investors should take expert legal and financial advice before entering into any transaction similar to or inspired by the contents of this publication. The risk of loss in futures trading and options, foreign or domestic, can be substantial. As a result of the high  degree  of  leverage  obtainable  in  futures  and  options  trading,  losses  may  be  incurred  that  are  greater  than  the amount of funds initially deposited - up to theoretically unlimited losses. Trading in options involves risk and is not suitable for all investors. Prior to buying or selling an option, investors must review the "Characteristics and Risks of Standardized Options', at http://www.optionsclearing.com/about/publications/character-risks.jsp . If you are unable to access the website, please contact your Deutsche Bank representative for a copy of this important document.

Participants in foreign exchange transactions may incur risks arising from several factors, including the following: (i) exchange rates can be volatile and are subject to large fluctuations; (ii) the value of currencies may be affected by numerous market factors, including world and national economic, political and regulatory events, events in equity and debt markets and changes in interest rates; and (iii) currencies may be subject to devaluation or government-imposed exchange controls, which could affect the value of the currency. Investors in securities such as ADRs, whose values are affected by the currency of an underlying security, effectively assume currency risk.

Unless  governing  law  provides  otherwise,  all  transactions  should  be  executed  through  the  Deutsche  Bank  entity  in the  investor's  home  jurisdiction.  Aside  from  within  this  report,  important  conflict  disclosures  can  also  be  found  at https://research.db.com/Research/ on each company ' s research page. Investors are strongly encouraged to review this information before investing.

Deutsche Bank (which includes Deutsche Bank AG, its branches and affiliated companies) is not acting as a financial adviser, consultant or fiduciary to you or any of your agents (collectively, 'You' or 'Your') with respect to any information provided in this report. Deutsche Bank does not provide investment, legal, tax or accounting advice, Deutsche Bank is not acting as your impartial adviser, and does not express any opinion or recommendation whatsoever as to any strategies, products or any other information presented in the materials. Information contained herein is being provided solely on the basis that the recipient will make an independent assessment of the merits of any investment decision, and it does not constitute a recommendation of, or express an opinion on, any product or service or any trading strategy.

The information presented is general in nature and is not directed to retirement accounts or any specific person or account type, and is therefore provided to You on the express basis that it is not advice, and You may not rely upon it in making Your decision. The information we provide is being directed only to persons we believe to be financially sophisticated, who are capable of evaluating investment risks independently, both in general and with regard to particular transactions and investment strategies, and who understand that Deutsche Bank has financial interests in the offering of its products

<!-- image -->

and services. If this is not the case, or if You are an IRA or other retail investor receiving this directly from us, we ask that you inform us immediately.

In July 2018, Deutsche Bank revised its rating system for short term ideas whereby the branding has been changed to Catalyst Calls ('CC') from SOLAR ideas; the rating categories for Catalyst Calls originated in the Americas region have been made consistent with the categories used by Analysts globally; and the effective time period for CCs has been reduced from a maximum of 180 days to 90 days.

United States : Approved and/or distributed by Deutsche Bank Securities Incorporated, a member of FINRA, NFA and SIPC. Analysts located outside of the United States are employed by non-US affiliates that are not subject to FINRA regulations.

Germany : Approved and/or distributed by Deutsche Bank AG, a joint stock corporation with limited liability incorporated in the Federal Republic of Germany with its principal office in Frankfurt am Main. Deutsche Bank AG is authorized under German Banking Law and is subject to supervision by the European Central Bank and by BaFin, Germany ' s Federal Financial Supervisory Authority.

United Kingdom : Approved and/or distributed by Deutsche Bank AG acting through its London Branch at Winchester House, 1 Great Winchester Street, London EC2N 2DB. Deutsche Bank AG in the United Kingdom is authorised by the Prudential Regulation Authority and is subject to limited regulation by the Prudential Regulation Authority and Financial Conduct Authority. Details about the extent of our authorisation and regulation are available on request.

Hong Kong : Distributed by Deutsche Bank AG, Hong Kong Branch or Deutsche Securities Asia Limited (save that any research relating to futures contracts within the meaning of the Hong Kong Securities and Futures Ordinance Cap. 571 shall be distributed solely by Deutsche Securities Asia Limited). The provisions set out above in the "Additional Information" section shall apply to the fullest extent permissible by local laws and regulations, including without limitation the Code of Conduct for Persons Licensed or Registered with the Securities and Futures Commission.

India : Prepared by Deutsche Equities India Private Limited (DEIPL) having CIN: U65990MH2002PTC137431 and registered office  at  14th  Floor,  The  Capital,  C-70,  G  Block,  Bandra  Kurla  Complex  Mumbai  (India)  400051.  Tel:  +  91  22  7180 4444.  It  is  registered  by  the  Securities  and  Exchange  Board  of  India  (SEBI)  as  a  Stock  broker  bearing  registration nos.: NSE (Capital Market Segment) - INB231196834, NSE (F&amp;O Segment) INF231196834, NSE (Currency Derivatives Segment) INE231196834, BSE (Capital Market Segment) INB011196830; Merchant Banker bearing SEBI Registration no.:  INM000010833  and  Research  Analyst  bearing  SEBI  Registration  no.:  INH000001741.  DEIPL  may  have  received administrative warnings from the SEBI for breaches of Indian regulations. The transmission of research through DEIPL is Deutsche Bank's determination and will not make a recipient a client of DEIPL. Deutsche Bank and/or its affiliate(s) may have debt holdings or positions in the subject company. With regard to information on associates, please refer to the 'Shareholdings' section in the Annual Report at: https://www.db.com/ir/en/annual-reports.htm .

Japan :  Approved and/or distributed by Deutsche Securities Inc.(DSI). Registration number - Registered as a financial instruments dealer by the Head of the Kanto Local Finance Bureau (Kinsho) No. 117. Member of associations: JSDA, Type II Financial Instruments Firms Association and The Financial Futures Association of Japan. Commissions and risks involved in stock transactions - for stock transactions, we charge stock commissions and consumption tax by multiplying the transaction amount by the commission rate agreed with each customer. Stock transactions can lead to losses as a result of share price fluctuations and other factors. Transactions in foreign stocks can lead to additional losses stemming from foreign exchange fluctuations. We may also charge commissions and fees for certain categories of investment advice, products and services. Recommended investment strategies, products and services carry the risk of losses to principal and other losses as a result of changes in market and/or economic trends, and/or fluctuations in market value. Before deciding on the purchase of financial products and/or services, customers should carefully read the relevant disclosures, prospectuses and other documentation. "Moody's", "Standard &amp; Poor's", and "Fitch" mentioned in this report are not registered credit rating agencies in Japan unless Japan or "Nippon" is specifically designated in the name of the entity. Reports on Japanese listed companies not written by analysts of DSI are written by Deutsche Bank Group's analysts with the coverage companies specified by DSI. Some of the foreign securities stated on this report are not disclosed according to the Financial Instruments and Exchange Law of Japan. Target prices set by Deutsche Bank's equity analysts are based on a 12-month forecast period..

Korea : Distributed by Deutsche Securities Korea Co.

South Africa :  Deutsche Bank AG Johannesburg is incorporated in the Federal Republic of Germany (Branch Register Number in South Africa: 1998/003298/10).

Singapore : This report is issued by Deutsche Bank AG, Singapore Branch or Deutsche Securities Asia Limited, Singapore Branch (One Raffles Quay #18-00 South Tower Singapore 048583, +65 6423 8001), which may be contacted in respect of any matters arising from, or in connection with, this report. Where this report is issued or promulgated by Deutsche Bank in Singapore to a person who is not an accredited investor, expert investor or institutional investor (as defined in the applicable Singapore laws and regulations), they accept legal responsibility to such person for its contents.

Taiwan :  Information  on  securities/investments  that  trade  in  Taiwan  is  for  your  reference  only.  Readers  should independently evaluate investment risks and are solely responsible for their investment decisions. Deutsche Bank research may not be distributed to the Taiwan public media or quoted or used by the Taiwan public media without written consent. Information on securities/instruments that do not trade in Taiwan is for informational purposes only and is not to be construed as a recommendation to trade in such securities/instruments. Deutsche Securities Asia Limited, Taipei Branch may not execute transactions for clients in these securities/instruments.

Qatar : Deutsche Bank AG in the Qatar Financial Centre (registered no. 00032) is regulated by the Qatar Financial Centre Regulatory Authority. Deutsche Bank AG - QFC Branch may undertake only the financial services activities that fall within the scope of its existing QFCRA license. Its principal place of business in the QFC: Qatar Financial Centre, Tower, West Bay, Level 5, PO Box 14928, Doha, Qatar. This information has been distributed by Deutsche Bank AG. Related financial products or services are only available only to Business Customers, as defined by the Qatar Financial Centre Regulatory Authority.

Russia : The information, interpretation and opinions submitted herein are not in the context of, and do not constitute, any appraisal or evaluation activity requiring a license in the Russian Federation.

Kingdom of Saudi Arabia : Deutsche Securities Saudi Arabia LLC Company (registered no. 07073-37) is regulated by the Capital Market Authority. Deutsche Securities Saudi Arabia may undertake only the financial services activities that fall within the scope of its existing CMA license. Its principal place of business in Saudi Arabia: King Fahad Road, Al Olaya District, P .O. Box 301809, Faisaliah Tower - 17th Floor, 11372 Riyadh, Saudi Arabia.

United Arab Emirates : Deutsche Bank AG in the Dubai International Financial Centre (registered no. 00045) is regulated by the Dubai Financial Services Authority. Deutsche Bank AG - DIFC Branch may only undertake the financial services activities that fall within the scope of its existing DFSA license. Principal place of business in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by Deutsche Bank AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority.

Australia  and  New  Zealand :  This  research  is  intended  only  for  "wholesale  clients"  within  the  meaning  of  the Australian  Corporations  Act  and  New  Zealand  Financial  Advisors  Act,  respectively.  Please  refer  to  Australia-specific research  disclosures  and  related  information  at  https://australia.db.com/australia/content/research-information.html Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ('ABC') team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

<!-- image -->

<!-- image -->

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without Deutsche Bank's prior written consent.

Copyright © 2018 Deutsche Bank AG

## David Folkerts-Landau

Group Chief Economist and Global Head of Research

| Pam Finelli Global Chief Operating Officer Research   | Michael Spencer Head of APAC Research       | Michael Spencer Head of APAC Research                         | Steve Pollard Head of Americas Research Global Head of Equity Research   |
|-------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------|
| Anthony Klarman Global Head of Debt Research          | Kinner Lakhani Head of EMEA Equity Research | Kinner Lakhani Head of EMEA Equity Research                   | Joe Liew Head of APAC Equity Research                                    |
| Jim Reid Global Head of Thematic Research             | Francis Yared Global Head of Rates Research | George Saravelos Head of FX Research                          | Peter Hooper Global Head of Economics Research                           |
|                                                       | Andreas Neubauer Head of Germany Research   | Spyros Mesomeris Global Head of Quantitative and QIS Research |                                                                          |

## International Production Locations

| Deutsche Bank AG Deutsche Bank Place Level 16 Corner of Hunter & Phillip Streets Sydney, NSW 2000 Australia Tel: (61) 2 8258 1234   | Deutsche Bank AG Mainzer Landstrasse 11-17 60329 Frankfurt am Main Germany Tel: (49) 69 910 00                 |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Deutsche Bank AG London 1 Great Winchester Street London EC2N 2EQ United Kingdom Tel: (44) 20 7545 8000                             | Deutsche Bank Securities Inc. 60 Wall Street New York, NY 10005 United States of America Tel: (1) 212 250 2500 |

<!-- image -->