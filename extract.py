from config import key
import requests
import datetime
import csv
Stocks = ["GOOGL", "AMZN", "COUR", "ADBE", "CRM"]

for s in Stocks:

    URL = f"https://api.polygon.io/v2/aggs/ticker/{s}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"

    Data = requests.get(URL)
    #print(Data)
    jData  = Data.json()
    #print(jData["results"])
    DJ = jData["results"]


    list_Data = []
    for day in DJ:
        #print(day)

# [{date, closing price}]
        CP = day["c"]
        T = day["t"]
        date_time = datetime.datetime.fromtimestamp(T/1000)
        #print(CP, date_time)
        # [{date, closing price}]
        Dict_Data = {}
        Dict_Data["Date"] = date_time
        Dict_Data["Closing"] = CP

        list_Data.append(Dict_Data) 
    with open(f"{s}.csv", "w",newline = "") as outfile:
        #load in data as DictReader
        Dict_writer = csv.DictWriter(outfile,fieldnames=["Date", "Closing"])
  
        Dict_writer.writeheader()
        Dict_writer.writerows(list_Data)
    
    