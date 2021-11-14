import pandas
# url = ''
import finviz
from finviz.screener import Screener

stock_list = Screener()
print(type(stock_list))
stock_list.to_csv('finviz_stocks_list.csv')

filters = ['exch_nasd', 'idx_sp500']
stock_list = Screener(filters=filters, table='Performance', order='price')

stock = finviz.get_stock('TSLA')
print(stock)
