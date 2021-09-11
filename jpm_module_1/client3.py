import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
	""" Produce all of the needed values to generate a datapoint """
	""" ------------- Update this function ------------- """
	stock = quote['stock']
	bid_price = float(quote['top_bid']['price'])
	ask_price = float(quote['top_ask']['price'])
	price = (bid_price+ask_price)/2
	return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
  if (price_b==0) :
    return
  return price_a/price_b

# Main
if __name__ == "__main__":

	# Query the price once every N seconds.
  for _ in iter(range(N)):
      quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
	
	 """" ----------- Update to get the ratio --------------- """
     for quote in quotes:
      	stock, bid_price, ask_price, price = getDataPoint(quote)
			print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

		print ("Ratio %s" % getRatio(price['ABC'], price['DEF']))