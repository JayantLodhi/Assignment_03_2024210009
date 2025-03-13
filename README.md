# 📈 Stock Data Scraper and Plotter  

This Python script fetches historical stock price data from **MacroTrends** and generates two plots using the **Bokeh** library:  
- **Average Stock Price History** (line graph)  
- **Annual % Change History** (bar graph)  

---

## 📝 Code Overview
**stock_info(ticker)**
- Fetches stock data from MacroTrends using requests.
- Parses the HTML using BeautifulSoup.
- Extracts tabular data and formats it for display.
  
**plot_stock_data(values_1)**
- Extracts and formats data for plotting.
- Uses Bokeh to generate:
- Line plot for average stock price history.
- Bar chart for annual percentage change.
  
**main()**
- Accepts user input for the ticker symbol.
- Handles invalid ticker symbols.
- Calls the stock_info() function.
- Calls the plot_stock_data() function.  

---

## 🚀 Requirements  
Make sure you have Python and the following libraries installed:  

```
pip install requests beautifulsoup4 bokeh
```

---

## 🏗️ How It Works
1) The script prompts the user to enter a stock ticker symbol (e.g., AAPL for Apple, NVDA for Nvidia, TM for Toyota Motors).
2) It scrapes data from MacroTrends using the requests and BeautifulSoup libraries.
3) Displays the scraped data in a tabular format in the terminal.
4) Plots two graphs using the Bokeh library:
    - **Average Stock Price History** – Line chart
    - **Annual % Change History** – Bar chart
  
---

## 📌 Notes
- This script is for educational purposes only.
- The data source (MacroTrends) may change its structure, which could break the script.

---

## 👨‍💻 Author
**Jayant Lodhi** (2024210009)


