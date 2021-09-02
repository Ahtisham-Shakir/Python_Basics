
import requests

# get request is used to read the content in the url
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# post request take data towards the server and give response
# r2 = requests.post(url=url, data=data)
