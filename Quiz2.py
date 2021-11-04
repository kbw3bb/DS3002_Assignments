import requests
import json
import time
import numpy as np
import csv
api_key = "6HZNsrM37K5VKpexAaoe2aZg0P3GmDCU7LjBsX0D"
url = "https://yfapi.net/v6/finance/quote"
def stock_in():
    TICK = str(input("Enter stock ticker"))
    querystring = {"symbols": TICK}
    headers = {'x-api-key': api_key}
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code != 204:
        stock_name = TICK
        json_stock = response.json()
        STOCK_P = json_stock['quoteResponse']['result'][0]["regularMarketPrice"]
        time_S = json_stock['quoteResponse']['result'][0]["regularMarketTime"]
        time_S = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time_S))
        final = TICK + ", " + str(time_S) + ", " + str(STOCK_P)
        return [stock_name, time_S, STOCK_P]
import csv
df = stock_in()
with open('stock.csv', mode='a') as stock_df:
    stock_writer = csv.writer(stock_df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    stock_writer.writerow(df)


