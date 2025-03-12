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

#print(main_headings)

headings = []   # to store all the headings as text

for i in all_headings[1:]:
    headings.append(i.text)

#print(headings)

all_values = table.find_all("td")   #all the values for the headings

#print(all_values) 

values = []  # to store all the values as text

for i in all_values:
    values.append(i.text)

#print(values[0:7])

print(f"\n{main_headings:_^100}\n")
# Print header
print(f"{headings[0]:^0} {headings[1]:^25} {headings[2]:^12} {headings[3]:^12} {headings[4]:^12} {headings[5]:^12} {headings[6]:^15}")

# Print data
x = 0
while x < len(values):
    row_val = values[x:x+7]
    print(f"{row_val[0]:^0} {row_val[1]:^25} {row_val[2]:^12} {row_val[3]:^12} {row_val[4]:^12} {row_val[5]:^12} {row_val[6]:^15}")

    x = x + 7