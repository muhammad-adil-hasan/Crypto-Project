# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Ask for which input 
print ('Let\'s get started!')
stock_code=input('Please enter Stock Code:').upper()

# Get dataADA-
data = yf.download(tickers=stock_code, period = '1d', interval = '15m')
print(data)
