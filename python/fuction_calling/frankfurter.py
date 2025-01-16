import requests

url = "https://api.frankfurter.app/latest?base=USD&symbols=USD,CAD,EUR"
response = requests.get(url)
print(response.text)
