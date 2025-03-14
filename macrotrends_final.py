import requests
from bs4 import BeautifulSoup
from bokeh.plotting import figure, show
from bokeh.layouts import row
from math import pi

def stock_info(ticker):
    url = f"https://www.macrotrends.net/stocks/charts/{ticker}/{ticker.lower()}/stock-price-history"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
            print("Failed to fetch data. Please check the ticker symbol.")
            return None

    soup = BeautifulSoup(response.text, "html.parser")

    all_table = soup.find_all("table", class_="historical_data_table")
    
    # Table 1 ==>
    table_1 = all_table[0]

    all_headings_1 = table_1.find_all("th")
    all_values_1 = table_1.find_all("td")

    main_heading_1 = all_headings_1[0].text
    headings_1 = [h.text for h in all_headings_1[1:]]
    values_1 = [v.text for v in all_values_1]

    if not values_1:
        print(f"No data found for {ticker}")
        return

    print(f"\n{main_heading_1:_^100}\n")
    print(f"{headings_1[0]:^0} {headings_1[1]:^25} {headings_1[2]:^12} {headings_1[3]:^12} {headings_1[4]:^12} {headings_1[5]:^12} {headings_1[6]:^15}")

    for x in range(0, len(values_1), 7):
        row_val = values_1[x:x+7]
        print(f"{row_val[0]:^0} {row_val[1]:^25} {row_val[2]:^12} {row_val[3]:^12} {row_val[4]:^12} {row_val[5]:^12} {row_val[6]:^15}")

    print("-" * 100)

    # Table 2 ==>
    table_2 = all_table[1]

    all_headings_2 = table_2.find_all("th")
    all_values_2 = table_2.find_all("td")

    headings_2 = [h.text for h in all_headings_2]
    values_2 = [v.text for v in all_values_2]

    print(f"\n{headings_2[0]:^30} {headings_2[1]:^30} {headings_2[2]:^15} {headings_2[3]:^15}")
    print(f"{values_2[0]:^30} {values_2[1]:^30} {values_2[2]:^15} {values_2[3]:^15}\n")
    print("-" * 100)

    for_plot = [main_heading_1] + values_1

    return for_plot

def plot_stock_data(for_plot):
    list_x = [for_plot[i] for i in range(1, len(for_plot), 7)]  #years
    list_y1 = [for_plot[i+1] for i in range(1, len(for_plot), 7)]  #avg stock price
    list_y2 = [for_plot[i+6].strip('%') for i in range(1, len(for_plot), 7)]  #annual % change

    list_x.reverse()
    list_y1.reverse()
    list_y2.reverse()

    stock_name = for_plot[0].replace(" Historical Annual Stock Price Data", "")

    # For stock price
    p = figure(title=f"{stock_name}'s Average Stock Price History", x_axis_label="Year", y_axis_label="Average Stock Price")
    p.line(list_x, list_y1, color='blue', line_width=2)

    p.x_range.start = min(map(int, list_x)) - 1
    p.x_range.end = max(map(int, list_x)) + 1
    p.y_range.start = min(map(float, list_y1)) - 5
    p.y_range.end = max(map(float, list_y1)) + 5

    # For annual % change
    b = figure(x_range=list_x, height=350, title=f"{stock_name}'s Annual % Change History", x_axis_label="Year", y_axis_label="Annual % Change")
    b.vbar(x=list_x, top=list_y2, width=0.5)

    b.xaxis.major_label_orientation = pi/2

    #plotting
    layout = row(p, b)
    show(layout)

# main function
def main():
    while True:
        ticker = input("Enter stock ticker symbol: ").strip().upper()
        if ticker == "":
            print("Ticker cannot be empty. Please try again.\n")
        else:
            break

    values_1 = stock_info(ticker)
    if values_1:
        plot_stock_data(values_1)

# Run
if __name__ == "__main__":
    main()