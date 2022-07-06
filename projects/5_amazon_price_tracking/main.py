from http.client import USE_PROXY
import smtplib, ssl
import requests
import lxml
from bs4 import BeautifulSoup
from decouple import config
from smtplib import SMTP
from socket import gaierror

url = config('URL')

headers = {
    "User-Agent": config('USER_AGENT'),
    "Accept-Language": config('ACCEPT_LANGUAGE')
}


response = requests.get(url, headers=headers)
#print(response) #200

soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())

result = soup.find(class_ ="a-offscreen").get_text()
#print(result) #$36.38

price_without_currency = result.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < float(config('TARGET_PRICE')):

    message = f"""\
        Subject: Python Bot Price Tracking...
        To: {config('RECEIVER')}
        From: {config('SENDER')}

        Amount is less than target price. Todays price is {price_as_float}."""

    try:
        with smtplib.SMTP(config('HOST'), config('PORT')) as server:
            server.login(config('USERNAME'), config('PASSWORD'))
            server.sendmail(config('SENDER'), config('RECEIVER'), message)

        print("Email Sent!")    
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')    
    except smtplib.SMTPServerDisconnected:
        print("Failed to connect to the server. Wrong user/password?")        
    except smtplib.SMTPException as e:
        print("SMTP error occured: " + str(e))       
       
    

