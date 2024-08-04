from nselib import capital_market
from nselib import derivatives
#import nselib 
import streamlit as st    
#from datetime import datetime
#from streamlit_extras.no_default_selectbox import selectbox
#from us_stocks import ticker
#import from st_btn_select import st_btn_select
#select= st_btn_select(('Pedestrians','Cyclists','Motorists'))

st.markdown("<h2 style = 'text-align:center'>Indian Stock Market Financial Dashboard</h2>",unsafe_allow_html=True)

instrument = st.sidebar.selectbox('Instrument Type',options = ('NSE Equity Market','NSE Derivatives Market'))

if instrument == 'NSE Equity Market':
    data_info = st.sidebar.selectbox('Data to Extract',options=('bhav_copy_equities','bhav_copy_with_delivery',
                                                             'equity_list','market_watch_all_indices','nifty50_equity_list',
                                                             'block_deals_data','bulk_deal_data','deliverable_position_data',
                                                             'price_volume_data','fno_equity_list','india_vix_data',
                                                             'market_watch_all_indices','fii_dii_trading_activity','short_selling_data','price_volume_and_deliverable_position_data'))
    
    if (data_info == 'equity_list') or (data_info =='fno_equity_list') or (data_info == 'nifty50_equity_list') or (data_info == 'market_watch_all_indices'):
       data = getattr(capital_market,data_info)()
    
    if (data_info == 'bhav_copy_equities') or (data_info == 'bhav_copy_with_delivery'):
        date = st.sidebar.text_input('Date','02-08-2024')
        data = getattr(capital_market,data_info)(date)
        
    if (data_info == 'block_deals_data') or (data_info == 'bulk_deal_data') or (data_info == 'short_selling_data') or (data_info == 'india_vix_data'):
        period_ = st.sidebar.text_input('Period','1M')
        data =getattr(capital_market,data_info)(period  = period_)
        
    if(data_info== 'price_volume_data'):#capital_market.price_volume_data('INFY',period='1M')
        #data = capital_market.price_volume_and_deliverable_position_data()
        sym = st.sidebar.text_input('Symbol',value = None)
        d1 = st.sidebar.date_input('Date from',format="DD-MM-YYYY")
        d2 = st.sidebar.date_input('Date to',format="DD-MM-YYYY")
        pre  = st.sidebar.text_input('Period','1W')
        data = capital_market.price_volume_data(symbol=sym, from_date=d1, to_date=d2,period = pre)
   
    if (data_info == 'deliverable_position_data'):
        #capital_market.price_volume_and_deliverable_position_data(symbol='SBIN')
        sym = st.sidebar.text_input('Symbol',value = None)
        #da = derivatives.future_price_volume_data(symbol=symbol, instrument='', from_date='', to_date='')
        dt1 = st.sidebar.date_input('Date from',format="DD-MM-YYYY")
        dt2 = st.sidebar.date_input('Date to',format="DD-MM-YYYY")
        pre1  = st.sidebar.text_input('Period','1W')
        data = capital_market.deliverable_position_data(symbol=sym, from_date=dt1, to_date=dt2,period=pre1)
    
    if (data_info =='price_volume_and_deliverable_position_data'):
        sym4 = st.sidebar.text_input('Symbol','TCS')
        pre4 = st.sidebar.text_input('Period','1W')

        data = capital_market.price_volume_and_deliverable_position_data(symbol=sym4, period=pre4)




    if  (data_info == 'fii_dii_trading_activity'):
        sym2 = st.sidebar.text_input('Symbol',value = None)
        d11 = st.sidebar.date_input('Date from',format="DD-MM-YYYY")
        d22 = st.sidebar.date_input('Date to',format="DD-MM-YYYY")
        pre3  = st.sidebar.text_input('Period','1W')
        data = capital_market.deliverable_position_data(symbol=sym2, from_date=d11, to_date=d22,period=pre3)    
        
if instrument == 'NSE Derivatives Market':
    data_info = st.sidebar.selectbox('Data to Extract',options=('expiry_dates_future','expiry_dates_option_index',
                                                                'option_price_volume_data','future_price_volume_data',
                                                                'participant_wise_open_interest',
                                                                'participant_wise_trading_volume','fno_bhav_copy',
                                                                'nse_live_option_chain','fii_derivatives_statistics'))                                        
    if (data_info == 'expiry_dates_future') or (data_info == 'expiry_dates_option_index'):
        #date=st.sidebar.date_input('Date',format= 'DD-MM-YYYY')
        #data = derivatives.expiry_dates_future()()
        data = getattr(derivatives,data_info)()
 

        
    if (data_info == 'fii_derivatives_statistics')  or (data_info == 'fno_bhav_copy') or (data_info == 'participant_wise_open_interest') or (data_info == 'participant_wise_trading_volume'):
        date= st.sidebar.text_input('Date','02-08-2024')
        data = getattr(derivatives,data_info)(date)
    
    if (data_info == 'future_price_volume_data'):
        ticker = st.sidebar.text_input('Ticker','SBIN')
        type_ = st.sidebar.text_input('Instrument Type','FUTSTK')
        period_ = st.sidebar._text_input('Period','1M')
        data = derivatives.future_price_volume_data(ticker,type_,period= period_)
        
    if (data_info == 'option_price_volume_data'):
        ticker = st.sidebar.text_input('Ticker','BANKNIFTY')
        type_ = st.sidebar.text_input('Instrument Type','OPTIDX')
        period_ = st.sidebar._text_input('Period','1M')
        data = derivatives.option_price_volume_data(ticker,type_,period= period_)
        
    if (data_info == 'nse_live_option_chain'):
        ticker = st.sidebar.text_input('Ticker','NIFTY')
        exp_date = st.sidebar.text_input('Expiry Date','08-08-2024')
        data = derivatives.nse_live_option_chain(ticker,expiry_date= exp_date)
    
    
st.write(data)                 

