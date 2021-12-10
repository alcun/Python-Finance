Python Tools for Finance Project.

An experiment in using tools to track financial index and backtest trading strategies using SMA, EMA and Adj Close via yfinance api.

Shoutout to Richard Moglen for illustrated original build.

Running using python python-finance.py in MS cmd shell.


imported tools:

import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
yf.pdr_override()

CURRENT VERSION:
Can backtest strategies of selected ticker and present user with %gain or loss based on trades

TO DO:
