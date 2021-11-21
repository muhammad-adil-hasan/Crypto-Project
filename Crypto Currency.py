# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf
import plotly.graph_objs as pt

def get_filters():
    """
    Asks user to input code, period and interval for stock

    """
    print ('Let\'s get started!')
    code=input('Please enter Stock Code:').upper()
    period=input('Please enter Period:').lower()
    interval=input('Please enter Interval:').lower()
    return code, period, interval

def finance_data(code, period, interval):
    data = yf.download(tickers=code, period=period, interval=interval)
    print(data)
    return ()

def main():
        code, period, interval = get_filters()
        finance_data(code, period, interval)
      
if __name__ == "__main__":
    main()
