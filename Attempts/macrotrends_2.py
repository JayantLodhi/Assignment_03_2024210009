import requests
from bs4 import BeautifulSoup

url = f"https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

all_table = soup.find_all("table", class_ = "historical_data_table")   #fatched table

table_1 = all_table[0]
table_2 = all_table[1]

#table 1 ==>

all_headings_1 = table_1.find_all("th") #all the heading for table 1

#print(all_headings_1)

main_heading_1 = all_headings_1[0].text

#print(main_headings_1)

headings_1 = []   # to store all the headings as text

for i in all_headings_1[1:]:
    headings_1.append(i.text)

#print(headings_1)

all_values_1 = table_1.find_all("td")   #all the values for the headings

#print(all_values_1) 

values_1 = []  # to store all the values as text

for i in all_values_1:
    values_1.append(i.text)

#print(values_1[0:7])

print(f"\n{main_heading_1:_^100}\n")  #print main heading

# Print headings
print(f"{headings_1[0]:^0} {headings_1[1]:^25} {headings_1[2]:^12} {headings_1[3]:^12} {headings_1[4]:^12} {headings_1[5]:^12} {headings_1[6]:^15}")

# Print data
x = 0
while x < len(values_1):
    row_val = values_1[x:x+7]
    print(f"{row_val[0]:^0} {row_val[1]:^25} {row_val[2]:^12} {row_val[3]:^12} {row_val[4]:^12} {row_val[5]:^12} {row_val[6]:^15}")

    x = x + 7

print("-"*100)

#Table 2 ==>

all_headings_2 = table_2.find_all("th")

headings_2 = []

for i in all_headings_2:
	headings_2.append(i.text)
     
#print(headings_2)
	
all_values_2 = table_2.find_all("td")

values_2 = []

for i in all_values_2:
	values_2.append(i.text)
     
#print(values_2)
     
#printing table_2
print(f"\n{headings_2[0]:^30} {headings_2[1]:^30} {headings_2[2]:^15} {headings_2[3]:^15}")
print(f"{values_2[0]:^30} {values_2[1]:^30} {values_2[2]:^15} {values_2[3]:^15}\n")
print("-"*100)


#graphs

from bokeh.plotting import figure, show

list_x = []       #for years
list_y1 = []      #for avg stock price
list_y2 = []      #for annual % change

y = 0
while y < len(values_1):
    list_x.append(values_1[y])
    list_y1.append(values_1[y+1])
    list_y2.append(values_1[y+6].strip("%"))
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
