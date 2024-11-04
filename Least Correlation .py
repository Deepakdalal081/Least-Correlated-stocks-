# Import necessary libraries
import yfinance as yf  
import numpy as np  
import pandas as pd  
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns 

# Define date range for stock data
end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=600)

# List of Nifty 100 stocks
data = ["^NSEI",'ABB.NS','ADANIENSOL.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ADANIPOWER.NS','ATGL.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANKBARODA.NS','BEL.NS','BHEL.NS','BPCL.NS','BHARTIARTL.NS','BOSCHLTD.NS','BRITANNIA.NS','CANBK.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','GAIL.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','IRFC.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWENERGY.NS','JSWSTEEL.NS','JINDALSTEL.NS','JIOFIN.NS','KOTAKBANK.NS','LTIM.NS','LT.NS','LICI.NS','LODHA.NS','M&M.NS','MARUTI.NS','NHPC.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PIDILITIND.NS','PFC.NS','POWERGRID.NS','PNB.NS','RECLTD.NS','RELIANCE.NS','SBILIFE.NS','MOTHERSON.NS','SHREECEM.NS','SHRIRAMFIN.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TVSMOTOR.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','TRENT.NS','ULTRACEMCO.NS','UNIONBANK.NS','UNITDSPR.NS','VBL.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS','ZYDUSLIFE.NS']
        
        
        
# DataFrame to store values
stock_close = pd.DataFrame()

# Download stock data
for ticker in data:
    stocks_data = yf.download(ticker, start=start_date, end=end_date)
    stock_close[ticker] = stocks_data["Close"].pct_change()

# Drop rows with NaN values
stock_close = stock_close.dropna()

# Calculate correlation matrix
stock_corr = stock_close.corr()

# Convert correlation matrix to DataFrame
stock_corr_long = stock_corr.stack().reset_index()
stock_corr_long.columns = ("Stock1", "Stock2", "Correlation")

#Removing the dupilcate values 
stock_corr_long = stock_corr_long[stock_corr_long["Stock1"].iloc[0] != stock_corr_long["Stock2"]]

# Sort correlations by value
corr_by_values = stock_corr_long.sort_values(by="Correlation")

#finding the Least correalted stocks with respect to NIFTY 50 index 
print(corr_by_values[(corr_by_values["Stock1"] == "^NSEI")])

# Identify the pair of stocks with the least correlation
least_corr = corr_by_values.iloc[0]
#print(least_corr)

# Print the least correlated stocks
#print(f"{least_corr['Stock1']} and {least_corr['Stock2']} have correlations of {least_corr['Correlation']:}")

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(12, 8))  
sns.heatmap(stock_corr, cmap="RdBu", annot=True, fmt=".2f", square=True)
plt.title("Correlation Between Stocks")
plt.show()


