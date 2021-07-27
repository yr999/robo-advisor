# this is the "app/robo_advisor.py" file

import csv
import json 

import os 

import requests 


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#info inputs

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response=requests.get(request_url)
#print(type(response))  #<class 'requests.models.Response'>
#print(response.status_code) #200
#print(response.text)   

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates=list(tsd.keys()) 
latest_day = dates[0] #2021-07-26
latest_close = tsd[latest_day]["4. close"]

#max of all high prices

#get high price from each day 
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

csv_file_path = os.path.join(os.path.dirname(__file__),"..","data","pices.csv")

csv_headers=["timestamp","open","high","low","close","volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    writer.writerow({
        "timestamp": "todo",
        "open": "todo",
        "high": "todo",
        "low": "todo",
        "close": "todo",
        "volume": "todo"
    })
    
    writer.writerow({
        "timestamp": "todo",
        "open": "todo",
        "high": "todo",
        "low": "todo",
        "close": "todo",
        "volume": "todo"
    })

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
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

