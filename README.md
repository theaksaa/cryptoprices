# cryptoprices
Python script for getting current price of cryptocoins !

Function:
```
getcoin(COIN_NAME, OPTION)
```
COIN_NAME:
```
'usdt_eth'  > convert eth to usdt
'usdt_btc'  > convert btc to usdt
'btc_eth'   > convert eth to btc
...
```
OPTION:
```
'lastPrice' > return last price of coin
'change'    > return change in %
'high'      > return high value in 24h of coin
'low'       > return low value in 24h of coin
'all'       > print last price, change, high, low
```
