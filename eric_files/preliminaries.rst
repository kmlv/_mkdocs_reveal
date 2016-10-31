

==============================================================================
Finance Preliminaries
==============================================================================


Introduction
==============================================================================
Our objective is to learn the theory and application of
time series methods.



- We will focus on financial time series applications.



- The methods in this course are broadly applicable to *any* type of
  time series.



- We will use the `R <http://www.r-project.org/>`_ programming
  environment to work with financial time series data.



- The `quantmod <http://www.quantmod.com/>`_ library will be especially useful:

.. code-block:: r

  > install.packages("quantmod")


Time Series Example
==============================================================================
Let's plot the historical prices for Facebook (FB).

.. code-block:: r

   > library(quantmod)
   > getSymbols("FB",src="google", from="2012-01-01", to="2014-12-31")
   > png(filename="fb.png")
   > chartSeries(FB)
   > dev.off()

Plot of Facebook Price
==============================================================================
.. image:: _static/Preliminaries/fb.png
   :width: 6in
   :align: center

Facebook Returns
==============================================================================
To plot just the closing prices:

.. code-block:: r

  > chartSeries(Cl(FB))
  > chartSeries(FB$FB.Close)



Or daily returns:

.. code-block:: r

  > chartSeries(dailyReturn(Cl(FB)))

Plot of Facebook Returns
==============================================================================
.. image:: _static/Preliminaries/fbRet.png
   :width: 6in
   :align: center

One-Period Return
==============================================================================
Let :math:`P_t` be the price of an asset at time :math:`t`.



- The *gross return* of the asset between dates :math:`t-1` and
  :math:`t` is:

.. math::

    \smash{\begin{align*}
    R_t & = \frac{P_t}{P_{t-1}}
    \,\,\,\, \text{or} \,\,\,\, P_t = P_{t-1} R_t.
    \end{align*}}



- The *net return* is:

.. math::

    \smash{\begin{align*}
    r_t & = R_t - 1 = \frac{P_t}{P_{t-1}} - 1 = \frac{P_t -
    P_{t-1}}{P_{t-1}}.
    \end{align*}}



- Note that the return can be computed between any two dates (i.e.
  daily, weekly, monthly, etc).

Multi-Period Return
==============================================================================
The :math:`k` -period gross return between dates :math:`t-k` and
:math:`t` is:

.. math::

    \begin{align*}
    R_t(k) & =
    \frac{P_t}{P_{t-k}} = \frac{P_t}{P_{t-1}} \times
    \frac{P_{t-1}}{P_{t-2}} \times
    \cdots \times \frac{P_{t-k+1}}{P_{t-k}} \\
    & = R_t R_{t-1} \cdots R_{t-k+1} \\
    & = \prod_{j=0}^{k-1} R_{t-j}.
    \end{align*}



- The :math:`k` -period net return is:

.. math::

   \smash{\begin{align*}
   r_t(k) & = \frac{P_t - P_{t-k}}{P_{t-k}}.
   \end{align*}}

Logarithmic Approximation
==============================================================================
In general, for any small value :math:`\smash{\varepsilon > 0}`:



.. math::

   \begin{align*}
   \ln(1+\varepsilon) & \approx \varepsilon.
   \end{align*}



Thus,

.. math::

   \smash{\begin{align*}
   \ln(R_t) & = \ln(1+r_t) \approx r_t.
   \end{align*}}



Furthermore, by the definition of gross returns,

.. math::

   \smash{\begin{align*}
   r_t & \approx \ln(R_t) = \ln(P_t/P_{t-1}) = \ln(P_t) - \ln(P_{t-1}).
   \end{align*}}

Approximation for Multiperiod Returns
==============================================================================
A similar relationship holds for the :math:`k` -period net return:

.. math::

   \smash{\begin{align*}
   r_t(k) & \approx \ln(P_t) - \ln(P_{t-k}).
   \end{align*}}

Time Intervals
==============================================================================
The interval of time for returns is of vital importance for
understanding the data.



- Daily returns are very different from weekly, monthly, annual,
  etc. returns.



- Intra-day returns at various time scales (millisecond, second,
  minute) are very different from each other.

Aggregating Trading Intervals
==============================================================================
When aggregating returns, we consider the following.



- There are approximately 250 trading days in a year.



- There are approximately 22 trading days in a month.



- There are 5 trading days in a week.



- U.S. equities markets are open from 9:30 am to 4:00 pm Eastern time
  - 6.5 hours each day.



- Thus there are approximately 6.5 hours, or 390 minutes or 23,400
  seconds or 23,400,000 milliseconds in a trading day.



- Similarly, there are approximately 1625 trading hours, 97,500
  trading minutes, 5,850,000 trading seconds and 5,850,000,000 trading
  milliseconds in a year.

Aggregating Returns
==============================================================================
To aggregate net returns, we simply add them:

.. math::

   \begin{align*}
   r_t(k) & = \ln(P_t) - \ln(P_{t-k}) \\
   & = \ln(P_t) - \ln(P_{t-1}) +
   \ln(P_{t-1}) - \ln(P_{t-2}) + \ln(P_{t-2}) \\
   & \hspace{2in} - \ldots -
   \ln(P_{t-k+1}) + \ln(P_{t-k+1}) - \ln(P_{t-k}) \\
   & = r_t + r_{t-1} + r_{t-2} + \ldots + r_{t-k+1} \\
   & = \sum_{j=0}^{k-1} r_{t-j}.
   \end{align*}



For example, to annualize daily returns,

.. math::

   \begin{align*}
   r_t(250) & = \sum_{j=0}^{250} r_j.
   \end{align*}

Example of Aggregating Returns
==============================================================================
Get Exxon Mobile equities data for the week of March 23rd, 2015.



.. code-block:: r

  > getSymbols("XOM", from="2015-03-23", to="2015-03-27")
  [1] "XOM"
  > XOM
             XOM.Open XOM.High XOM.Low XOM.Close XOM.Volume XOM.Adjusted
  2015-03-23    85.02    85.78   85.01     85.43   17163200        85.43
  2015-03-24    85.30    85.78   84.50     84.52   10099500        84.52
  2015-03-25    85.05    85.57   84.77     84.86   11816000        84.86
  2015-03-26    85.30    85.57   84.09     84.32   14388500        84.32
  2015-03-27    84.04    84.05   83.33     83.58   11094600        83.58



- What are the daily returns?



- What is the weekly return?

Asset Classes
==============================================================================
There are several broad classes of assets traded in financial markets.



- Equities.



- Futures.



- Options.



- Bonds.



- Currencies.

Indices
==============================================================================
Indices are synthetic portfolios of assets that are not
typically traded.



- The S\&P 500 index is a portfolio of 500 equities *and is not
  traded*.



- To hold the S\&P 500 index, one can:

  - Purchase the 500 component equities in the correct proportions.

  - Purchase shares in a mutual fund that tracks the index.

  - Purchase shares of the SPY exchange traded fund (ETF).

  - Purchase futures contracts on SPX.

Important Indices
==============================================================================
- S\&P 500 (SPX).



- VIX - portfolio of S\&P 500 options which represents the expected
  value of a one-standard deviation move in the S\&P 500 index over
  the next month (in annual terms).



- On March 30th, 2015, the closing value for VIX was 14.51 and the
  closing value for SPX 2086.24.



- Hence, the market expects the standard deviation of the SPX to be
  :math:`14.51/\sqrt{12} = 4.19` percent or  :math:`\smash{0.0419\times
  2086.24 = 87.39}` index points.
	  

Important Assets
==============================================================================
- SPY - SPX ETF.



- E-mini - Futures contract on the SPX.



- SPX Options.



- SPY Options.



- VIX Options.



- VIX Futures.

VIX
==============================================================================
.. code::

  > getSymbols("^VIX", from="2014-01-01", to="2015-03-27")
  > chartSeries(Cl(VIX))

.. image:: _static/Preliminaries/vix.png
   :width: 6in
   :align: center

Near-Month VX Futures
==============================================================================
.. code::

  > install.packages("Quandl")
  > library(Quandl)
  > VX1 = Quandl("OFDP/FUTURE_VX1",type="xts")
  > chartSeries(VX1)

.. image:: _static/Preliminaries/vx1.png
   :width: 6in
   :align: center

E-mini Near-Month Returns
==============================================================================
.. code::

  > ES1 = Quandl("OFDP/FUTURE_ES1",start_date="2007-01-01",end_date="2015-03-27",type="xts")
  > chartSeries(dailyReturn(ES1$Open))

.. image:: _static/Preliminaries/es1.png
   :width: 6in
   :align: center

Important Features of Returns
==============================================================================
What do you notice about the E-mini returns?
