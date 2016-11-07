 
# Basic Environment
 
## Budish, Cramton, Shim (2015)

---------------------------------------------------------

## Primitives: Security, Information

* One security $ x $ traded in continuous time.

* $ x $ can be costlessly liquidated at fundamental value $ V(t) $. 

* There is publicly observable signal of the $ V(t) $.  
 <!--no asymmetric information, costs of inventory, etc "best case scenario for price discovery"-->

* $ V(t) $ evolves with compound Poisson with jump rate $ \lambda_V $ and jump distribution $ F_V $ 
<!--  Finite support; Symmetric with mean zero-->

* $ J $ distribution of the jump size.  
<!--abs value of F_v realizations-->

---------------------------------------------------------

## Primitives: Investors and Trading Firms

<!--end users of financial markets: mutual funds, pension funds, hedge funds, etc. -->

* Investors (liquidity/noise traders):
    * Arrive randomly with fixed need to buy/sell 1 unit at a Poisson arrival rate of $ λ_I $. 
    * Trade immediately upon arrival: they are only takers  of liquidity. 

* Trading Firms (HFTs, algorithmic traders, makers):
    * No intrinsic demand: profit/lose from trading at prices $ p \neq V(t) $.
    * Entry is endogenous.
    
* Latency. firms observe V with a small delay, $ \delta_{slow} > 0 $. At a cost $ c_{speed} $, they can reduce latency by $ \Delta\delta = \delta_{slow} - \delta_{fast} > 0 $. 
      
---------------------------------------------------------

## Equilibrium in CDA: General
 
* No asymmetric info, no inventory costs, everyone risk neutral. Yet, Bertrand competition (zero bid-ask spread) does not happen. 
  
* This is due to sniping incentives:
    
    * When V jumps, the maker sends a replace order, and everyone else tries to buy (sell) the stale quote and liquidate at new fundamental ("snipe").
    
    * Sniping probability $ \frac{N-1}{N} $
    
    * Sniping generates arbitrage rents paid by investors.

---------------------------------------------------------

## Equilibrium in CDA: Complete Statement 
 
* Unique Nash Equilibrium

* Investors trade immediately upon arrival.
 
* One trading firm is market maker: sets spread $ s^{*} $, orders tracking V(t)
 
* N − 1 trading firms are stale-quote snipers: submit IOC orders when V(t) jumps.
  
* Zero profit for market makers: 
$$ λ_I . \frac{s^\*}{2} - λ_V.\Pr\[J>\frac{s^\*}{2}\].\mathbb{E}( J-\frac{s^\*}{2}|J>\frac{s^\*}{2} ). \frac{N^\*-1}{N^\*} = c_{speed} $$

* Zero profit for snipers: 
$$ λ_V.\Pr\[J>\frac{s^\*}{2}\].\mathbb{E}( J-\frac{s^\*}{2}|J>\frac{s^\*}{2} ). \frac{1}{N^\*} = c_{speed} $$


<!--

    Simplifies to lambda_I s*/2 = N* c_speed:     
    "all of the expenditure by trading  rms on speed technology ultimately is borne by investors, via the bid-ask spread."..."Arms-race prize = expenditures on speed = cost to investors"
  
  
    * Equilibrium Condition Exo Entry: Revenue from investors = rents to trading firms. 
    $$ λ_I . \frac{s}{2} = λ_V.\Pr\[J>\frac{s}{2}\].\mathbb{E}( J-\frac{s}{2}|J>\frac{s}{2} ) $$

-->

---------------------------------------------------------

## Equilibrium in FBA
 
* Bertrand competition: Zero bid-ask spread.

    * For any $ \tau $ (batching length) > 0 (discont. between continuous/serial & discrete/batch).

* (Slow) trading firms supply $ \bar{Q} $ units of liquidity at zero spread.

* If $ \tau $ sufficiently larger than speed differential $ \Delta δ $ => no one invests in speed:

$$ \frac{\Delta\delta .\lambda_V}{\tau}.\mathbb{E}(J).\bar{Q} < c_{speed}  $$

<!--The fraction Deltaδ*λjump/tau  is the proportion of time which the fast trader has a profitable sniping opportunity. For finite Q, the condition is satisfied for long enough τ.-->