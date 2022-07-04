import requests

import lxml

from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B004Y6AJP2/ref=syn_sd_onsite_desktop_60?psc=1&pd_rd_plhdr=t&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRlhWS0pINFE3TTFHJmVuY3J5cHRlZElkPUEwNDY5Mjk3RVpBNldQOVBIQ1JDJmVuY3J5cHRlZEFkSWQ9QTA2MTA1NTcyUDlVTEs3VU5CSlM3JndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get(url, headers=headers)
#print(response) #200

soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())

result = soup.find(class_ ="a-offscreen").get_text()

print(result)

#TODO: Split value
#TODO: SMTP to send email (Refer -> https://wipro.udemy.com/course/100-days-of-code/learn/lecture/21710354#overview)