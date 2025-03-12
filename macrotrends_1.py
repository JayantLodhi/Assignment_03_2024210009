import requests
from bs4 import BeautifulSoup

url = f"https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_ = "historical_data_table")   #fathed table

#print(table) 

all_headings = table.find_all("th") #all the heading

#print(all_headings)

main_headings = all_headings[0].text

print(main_headings)

headings = []   # to store all the headings as text

for i in all_headings[1:]:
    headings.append(i.text)

print(headings)

all_values = table.find_all("td")   #all the values for the headings

#print(all_values) 

values = []  # to store all the values as text

for i in all_values:
    values.append(i.text)

print(values)