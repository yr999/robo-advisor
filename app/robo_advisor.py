# this is the "app/robo_advisor.py" file

#IMPORTS

import csv
import json 

import os 

from dotenv import load_dotenv 

import requests 

import re 

from datetime import datetime as dt

load_dotenv()


#FORMATS PRICES 

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#SECURITY

api_key=os.environ.get("ALPHAVANTAGE_API_KEY")       #"demo"

#INPUTS 

risk=input("PLEASE PICK YOUR RISK TOLERRANCE: HIGH, MEDIUM and LOW: ")

risk=risk.upper()

if  risk == "HIGH" or (risk == "MEDIUM") or (risk == "LOW"):
    print("VALID RISK")
else:
    print("OOPS, INVALID RISK, PLEASE TRY AGAIN")
    exit()


symbol=input("PLEASE INPUT ONE STOCK OR CRYPTOCURRENCY SYMBOL: ")
symbol=symbol.upper()

#PRELIMINARY VALIDATIONS

def validate(): 
    while True:
        if (len(symbol)<1 or len(symbol)>5):
            print("OOPS, PLEASURE ENSURE YOUR SYMBOL HAS BETWEEN 1 and 5 CHARACTERS")
        elif re.search("[0-9]",symbol):
            print("OOPS, PLEASURE ENSURE YOUR SYMBOL DOESN'T CONTAIN A NUMBER")
        elif re.search("[$#@]",symbol):
            print("OOPS, PLEASURE ENSURE YOUR SYMBOL DOESN'T CONTAIN $#@")
        else:
            print("VALID VALUE")
        break
validate() 


#REQUEST DATA FROM URL

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response=requests.get(request_url)
   
parsed_response = json.loads(response.text)

#VALIDATIONS

response_keys=list(parsed_response.keys())

#print(response_keys)

if "Error Message" in response_keys:
    print("OOPS, COULDN'T FIND ANY TRADING DATA FOR THAT STOCK SYMBOL. PLEASE TRY AGAIN")
    exit()

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


#CALCULATIONS 

tsd = parsed_response["Time Series (Daily)"]

dates=list(tsd.keys()) 
latest_day = dates[0] #2021-07-26
latest_close = tsd[latest_day]["4. close"]

high_prices=[]
low_prices=[]

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low =min(low_prices)

#breakpoint() 

#csv_file_path = "app/prices.csv" # a relative filepath

#WRITE HISTORICAL PRICES TO CVS FILE

csv_file_path = os.path.join(os.path.dirname(__file__),"..","data","pices.csv")

csv_headers=["timestamp","open","high","low","close","volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    for date in dates:
        daily_prices=tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": to_usd(float(daily_prices["1. open"])),
            "high": to_usd(float(daily_prices["2. high"])),
            "low": to_usd(float(daily_prices["3. low"])),
            "close": to_usd(float(daily_prices["4. close"])),
            "volume": daily_prices["5. volume"]
            })
    

#BONUS FOR FORMATING DATES

current_date = dt.today()
current_time=dt.now()

run_date=current_date.strftime("%B %d,%Y")
run_time=current_time.strftime("%I:%m %p")


#sometimes last_refreshed date includes date and time if so, please use below: 

#last_ref_date_obj=dt.strptime(last_refreshed,'%Y-%m-%d %H:%M:%S').date() 

last_ref_date_obj=dt.strptime(last_refreshed,'%Y-%m-%d').date() 

last_ref_date=last_ref_date_obj.strftime("%B %d,%Y")

#RECOMMENDATION 

#if the risk tolerance is high, then 

#if risk=="HIGH" and ""

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", run_time, "on", run_date)   #Run at: 11:52pm on June 5th, 2018
print("-------------------------")
print(f"LATEST DAY: {last_ref_date}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA to CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

