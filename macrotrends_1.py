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

from bokeh.plotting import figure, show

list_x = []       #for years
list_y1 = []      #for avg stock price
list_y2 = []      #for annual % change

y = 0
while y < len(values):
    list_x.append(values[y])
    list_y1.append(values[y+1])
    list_y2.append(values[y+6].strip("%"))
    y = y + 7

list_x.reverse()
list_y1.reverse()
list_y2.reverse()
#print(list_x)
#print(list_y1)
#print(list_y2)

#for stock price
p = figure(title="Average Stock Price History", x_axis_label = "year", y_axis_label = "average Stock Price")

p.line(list_x, list_y1, color = 'blue', line_width = 2)

# Adjust x and y ranges to center the plot
p.x_range.start = min(list(map(int, list_x))) - 1
p.x_range.end = max(list(map(int, list_x))) + 1
p.y_range.start = min(list(map(float, list_y1))) - 5
p.y_range.end = max(list(map(float, list_y1))) + 5

#show(p)

#for % change
b = figure(x_range=list_x, height=350, title="Annual % Change History", x_axis_label = "year", y_axis_label = "Annual % Change")

b.vbar(x=list_x, top=list_y2, width=0.5)

from math import pi

b.xaxis.major_label_orientation = pi/2

#show(b)

from bokeh.layouts import row

layout = row(p, b)

show(layout)