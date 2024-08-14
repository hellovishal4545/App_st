import streamlit as st
import pandas as pd
import numpy as np 
import yfinance as yf
import plotly.express as px 
#from timeseries import TimeSeries 
#from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from stocknews import StockNews  
import streamlit.components.v1 as com
#from streamlit_lottie import st_lottie
com.iframe("https://lottie.host/embed/5cfc1a3d-76ad-400b-9db0-023947afae57/lvgGWjs49p.json")

st.title("Stock Dashboard")
ticker = st.sidebar.text_input("Ticker",value = 'AAPL')
start_date = st.sidebar.date_input("Start Date",value = pd.to_datetime('2024-05-25'))
end_date = st.sidebar.date_input("End Date")


data = yf.download(ticker,start=start_date,end = end_date)
fig = px.line(data,x = data.index,y = data['Adj Close'],title = ticker)
st.plotly_chart(fig)

pricing_data,fundamental_data,news = st.tabs(["Pricing Data","Fundamental Data","Top News"])

with pricing_data:
    st.header('Price Movements')
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data)
    annual_return = data2['% Change'].mean()*252*100 #market on 252 
    st.write('Annual Return is',annual_return,'%')
    stdev = np.std(data2['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is',stdev*100,'%')
    st.write('Risk Adj. Return is',annual_return/(stdev*100))
        

with fundamental_data:
    key = '6XRX4F4BGVMDPLAQ'    #'OW1639L6385UCYYL'
    fd= FundamentalData(key,output_format = 'pandas')
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns  = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cash Flow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)      

with news:
    st.header(f'Nes of {ticker}')
    sn = StockNews(ticker,save_news = False)
    df_news = sn.read_rss()
    for i in range(20):
        st.subheader(f'News {i + 1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
        
