import requests

url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/TATN.json?iss.meta=off&iss.only=marketdata&securities.columns=LAST"
response = requests.get(url)
data = response.json()

data_size = len(str(data))
data_size_mb = data_size/ 1024 
print(data_size_mb)