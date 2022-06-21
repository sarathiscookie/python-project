from twilio.rest import Client
from decouple import config
import requests

company_name = "Tesla"

stock_status = None

stock_name = "TSLA"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": config('STOCK_API_KEY')
}

news_params = {
    "q": company_name,
    "apiKey": config('NEWS_API_KEY'),
    #"pageSize": 3
}

# Get stock details from API.
url_stock_request = requests.get(config('STOCK_ENDPOINT'), params=stock_params)

data = url_stock_request.json()["Time Series (Daily)"]

data_list = [val for (key, val) in data.items()]

# Get yesterday closing stock price.
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
url_news_request = requests.get(config('NEWS_ENDPOINT'), params=news_params)
articles = url_news_request.json()["articles"]
sliced_articles = articles[:3]

client = Client(config('TWILIO_ACCOUNT_SID'), config('TWILIO_AUTH_TOKEN'))

for article in sliced_articles:
    content = f"{stock_name}: {stock_status}{round(percentage_of_stock_difference, 2)}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
    message = client.messages \
                .create(
                     body=content,
                     from_='+17348227044',
                     to=config('TWILIO_RECEIVER_MOBILE')
                 )

print ("SMS Sent")                 