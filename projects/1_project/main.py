import os

from twilio.rest import Client

import requests

company_name = "Tesla"

stock_status = None

stock_endpoint = "https://www.alphavantage.co/query"

stock_api_key = "MZYRHTL7NZ10JOXU"

stock_name = "TSLA"

news_api_key = "ae01ed1470c241a48f7bab0782c51ccd"

news_endpoint = "https://newsapi.org/v2/everything"

twilio_account_sid = "ACac227df357a6a41b5bca9cab3a06f677"

twilio_auth_token = "0f8fb3cebc833cf30bac6ef182a68fe1"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": stock_api_key
}

news_params = {
    "q": company_name,
    "apiKey": news_api_key,
    #"pageSize": 3
}

url_stock_request = requests.get(stock_endpoint, params=stock_params)

# Get yesterday closing stock price.
data = url_stock_request.json()["Time Series (Daily)"]

data_list = [val for (key, val) in data.items()]
 
yesterday_closing_stock_price = data_list[0]["4. close"]

# Get day before yesterday's closing stock price.
day_before_yesterday_closing_stock_price = data_list[1]["4. close"]

# Find the difference of closing stock.
difference_of_stock_price = float(yesterday_closing_stock_price) - float(day_before_yesterday_closing_stock_price)

if difference_of_stock_price > 0:
    stock_status = "🔺"
else:
    stock_status = "🔻"

# Calculate percentage
# Formulae: ((a - b) / (a + b / 2)) * 100
add_of_stock_price = float(yesterday_closing_stock_price) + float(day_before_yesterday_closing_stock_price)

percentage_of_stock_difference = (difference_of_stock_price / (add_of_stock_price / 2)) * 100

# Get relevant news (max 2 news) from API and send SMS.
url_news_request = requests.get(news_endpoint, params=news_params)
articles = url_news_request.json()["articles"]
sliced_articles = articles[:3]

client = Client(twilio_account_sid, twilio_auth_token)

for article in sliced_articles:
    content = f"{stock_name}: {stock_status}{round(percentage_of_stock_difference, 2)}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
    message = client.messages \
                .create(
                     body=content,
                     from_='+17348227044',
                     to='+919562903203'
                 )

print ("SMS Sent")                 