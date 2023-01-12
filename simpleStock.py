import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Apple Stock Price App

Stock Closing **closing price** and **volume** for Apple between Jan 2013 and Jan 2023


""")


#using https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75 as reference to import data
appleTicker = 'AAPL'

#grabbing the data using yfinance
tickerData = yf.Ticker(appleTicker)


#setting date range
appleData = tickerData.history(period='1d', start='2013-1-1', end='2023-1-1')

st.write(""" 
## Closing Price 
""")
st.line_chart(appleData.Close)

st.write(""" ## Total Volume """)
st.line_chart(appleData.Volume)
