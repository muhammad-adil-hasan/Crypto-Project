# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

# Get Bitcoin data
data = yf.download(tickers='ADA-USD', period = '1d', interval = '15m')
print(data)
