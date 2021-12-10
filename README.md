Python Tools for Finance Project.

An experiment in using tools to track financial index using yfinance api.

Using indicies such as Simple Moving Average and Adjusted Close to back test financial strategies using archived data.

Shotout to Richard Moglen for illustrated original build.

Running using python python-finance.py in MS cmd shell.


imported tools:import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
yf.pdr_override()

CURRENT VERSION:
Can ask for ticker and show and compare SMA and Adjusted Close Price in a stated time frame and state which ones were more frequent.

TO DO:
Apply backtest strat
Visual elements