from urllib.request import Request, urlopen
import pandas as pd
from matplotlib import pyplot as plt
url1 = "https://finviz.com/insidertrading.ashx"
import numpy as np
req = Request(url1,headers = {'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()

df = pd.read_html(webpage)
#print(df[-1])

print ("*****************************************")



def calculate_correlation_graph(url, ticker):

    entire_url = url+ticker
    req = Request(entire_url,headers = {'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()

    df_1 = pd.read_html(webpage)
    df_final = df_1[-2]
    # new_header = df_final.iloc[0]
    # df_final = df_final[1:]
    # df_final.columns = new_header
    #df_final.rename(columns=df_final.iloc[0])
    # headers = df_final.iloc[0]
    # new_df  = pd.DataFrame(df_final.values[1:], columns=headers)

    df_final.rename(columns=df_final.iloc[0], inplace = True)
    df_final.drop(df_final.index[0], inplace = True)
    df_final = df_final[df_final['Transaction']!='Sale']
    data = df_final[[]]
    prices = df_final[['Value ($)']].values.tolist()
    y = [z[0] for z in prices]
    time = df_final[['SEC Form 4']].values.tolist()
    x = [z[0][:7] for z in time]
    y.reverse()
    x.reverse()
    length = len(y)
    #sort = y.sorted()
    indx = range(length)
    y = np.array(y)
    x = np.array(x)

    plt.figure(figsize=(7,8))
    plt.title("Corelation graph of the Investor Holdings with Time")
    print (prices)
    plt.plot(x,y,marker="o")
    plt.xlabel("Time (days)")
    plt.ylabel("Price ($)")
    plt.yticks(indx,y)
    plt.xticks(rotation=20)

    #plt.show()
    png = ticker+'_2'+'.png'
    plt.savefig(png)
    #print (df)
    return df_final

def stock_of_ticker (url,ticker):
    entire_url = url+ticker


    import yfinance as yf

    # stock = yf.Ticker(ticker)
    #
    # stock.info
    #
    # # get historical market data
    # hist = stock.history(period="max")
    #
    # hist = hist[['Open','High','Low','Close']]

    # stock = yf.download(ticker,
    #                   start='2019-01-01',
    #                   end='2021-06-12',
    #                   progress=False,
    #                   )
    # stock.head()
    #aapl_df = yf.download('AAPL')
    ticker_1 = yf.Ticker(ticker)
    stock = ticker_1.history(period="1y")
    stock.reset_index(inplace =True)
    #print (stock)
    df = stock[['Date','Close']]
    #df.set_index('Date', inplace=True)
    df.plot(x ='Date', y='Close', kind = 'scatter')
    #plt.plot(stock['Close'])
    #plt.show()
    png = ticker+'_1'+'.png'
    plt.savefig(png)
    return df
    #print (hist)
    #
    # import requests
    #
    #
    # companies = []
    # companies.append(ticker)
    # listofdf = []
    # for item in companies:
    #     histprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{item}?serietype=line")
    #
    #     # decide how to handle a server that's misbehaving to this extent
    #     histprices = histprices.json()
    #
    # #Parse the API response and select only last 600 days of prices
    #     histprices = histprices['historical'][-600:]
    #
    # #Convert from dict to pandas datafram
    #
    #     histpricesdf = pd.DataFrame.from_dict(histprices)
    #
    # #rename column
    #     histpricesdf = histpricesdf.rename({'close': item}, axis=1)
    #
    # #append all dfs to list
    #     listofdf.append(histpricesdf)
    #
    # #set index of each DataFrame by common column before concatinatinghtem
    # dfs = [df.set_index('date') for df in listofdf]
    #
    # histpriceconcat = pd.concat(dfs,axis=1)
    #
    # #divide all dataframe by first line of data to enable comparison
    # histpriceconcat = histpriceconcat/histpriceconcat.iloc[0]
    #
    #
    #
    #
    # for i, col in enumerate(histpriceconcat.columns):
    #     histpriceconcat[col].plot()
    #
    # plt.title('Price Evolution Comparison')
    #
    # plt.xticks(rotation=70)
    # plt.legend(histpriceconcat.columns)
    # plt.savefig('foo1.png', bbox_inches='tight')
    #
    # from iexfinance.stocks import Stock
    # from datetime import datetime
    # from iexfinance.stocks import get_historical_data
    # #Pulling and Plotting Historical Prices
    # start = datetime(2017, 1, 1)
    # end = datetime(2020, 8, 1)
    # df = get_historical_data(ticker, start, end, output_format='pandas')
    # plt.figure(figsize=(10,10))
    # plt.plot(df.index, df['close'])
    # plt.xlabel("date")
    # plt.ylabel("$ price")
    # plt.title(ticker+"Stock Price 1/1/17 - 8/1/19")
    # #Creating and Plotting Moving Averages
    # df["SMA1"] = df['close'].rolling(window=50).mean()
    # df["SMA2"] = df['close'].rolling(window=200).mean()
    # df['ewma'] = df['close'].ewm(halflife=0.5, min_periods=20).mean()
    # plt.figure(figsize=(10,10))
    # plt.plot(df['SMA1'], 'g--', label="SMA1")
    # plt.plot(df['SMA2'], 'r--', label="SMA2")
    # plt.plot(df['close'], label="close")
    # plt.legend()
    # plt.show()
    # #Creating and Plotting Bollinger Bands
    # df['middle_band'] = df['close'].rolling(window=20).mean()
    # df['upper_band'] = df['close'].rolling(window=20).mean() + df['close'].rolling(window=20).std()*2
    # df['lower_band'] = df['close'].rolling(window=20).mean() - df['close'].rolling(window=20).std()*2
    # plt.figure(figsize=(10,10))
    # plt.plot(df['upper_band'], 'g--', label="upper")
    # plt.plot(df['middle_band'], 'r--', label="middle")
    # plt.plot(df['lower_band'], 'y--', label="lower")
    # plt.plot(df['close'], label="close")
    # plt.legend()
    # plt.show()
    # plt.figure(figsize=(10,10))
    # plt.plot(df['upper_band'].iloc[-200:], 'g--', label="upper")
    # plt.plot(df['middle_band'].iloc[-200:], 'r--', label="middle")
    # plt.plot(df['lower_band'].iloc[-200:], 'y--', label="lower")
    # plt.plot(df['close'].iloc[-200:], label="close")
    # plt.legend()
    # plt.show()



ticker = 'TSLA'

url = 'https://finviz.com/quote.ashx?t='
print (calculate_correlation_graph(url,'TSLA'))
print (stock_of_ticker(url,'TSLA'))
