from http.client import USE_PROXY
import smtplib, ssl
import requests
import lxml
from bs4 import BeautifulSoup
from decouple import config
from smtplib import SMTP
from socket import gaierror

def outerClosureFunction(price_with_currency):
    # this is the enclosing function
    price_without_currency = price_with_currency.split("$")[1]

    def innerClosureFunction():
        # this is the enclosed function
        # the inner function accessing the outer function's variable 'text'
        return float(price_without_currency)

    return innerClosureFunction
    
url = config('URL')

headers = {
    "User-Agent": config('USER_AGENT'),
    "Accept-Language": config('ACCEPT_LANGUAGE')
}

response = requests.get(url, headers=headers)
#print(response) #200

soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())

price_with_currency = soup.find(class_ ="a-offscreen").get_text()
#print(price_with_currency) #$36.38

product_title = soup.find(id = "productTitle").get_text()
#product_title.strip() #BELLA Classic Rotating Non-Stick Belgian Waffle Maker, Perfect 1" Thick Waffles, PFOA Free Non Stick Coating & Removable Drip Tray for Easy Clean Up, Browning Control, Black

price_as_float = outerClosureFunction(price_with_currency)
       
if price_as_float() < float(config('TARGET_PRICE')):
    print(f"Amount is less than target price. Product title: {product_title.strip()}. Todays price is {price_as_float()}.")
    """
    message = f"""\
    """
        Subject: Python Bot Price Tracking...
        To: {config('RECEIVER')}
        From: {config('SENDER')}

        Amount is less than target price. Product title: {product_title.strip()}.Todays price is {price_as_float}."""
    """
    try:
        with smtplib.SMTP('localhost') as server:
            server.login(config('USERNAME'), config('PASSWORD'))
            server.sendmail(config('SENDER'), config('RECEIVER'), message)

        print("Email Sent!")    
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')    
    except smtplib.SMTPServerDisconnected:
        print("Failed to connect to the server. Wrong user/password?")        
    except smtplib.SMTPException as e:
        print("SMTP error occured: " + str(e))    
    """     

