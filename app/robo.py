
import os
import json
from dotenv import load_dotenv
import requests
from pandas import DataFrame
import plotly.express as px

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="abc123")

def fetch_data(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    return json.loads(response.text)

def process_data(parsed_response):
    if "Time Series (Daily)" not in list(parsed_response.keys()):
        return None

    records = []
    for date, daily_data in parsed_response["Time Series (Daily)"].items():
        records.append({
            "date": date,
            "open": float(daily_data["1. open"]),
            "high": float(daily_data["2. high"]),
            "low": float(daily_data["3. low"]),
            "close": float(daily_data["4. close"]),
            "volume": int(daily_data["5. volume"]),
        })
    return DataFrame(records)

def summarize_data(prices_df):
    """ Param : prices_df (pandas.DataFrame) """
    return {
        "latest_close": prices_df.iloc[0]["close"],
        "recent_high": prices_df["high"].max(),
        "recent_low": prices_df["low"].min(),
    }

def prepare_data_for_charting(prices_df):
    """ Sorts the data by date ascending, so it can be charted """
    chart_df = prices_df.copy()
    chart_df.sort_values(by="date", ascending=True, inplace=True)
    #chart_df.index.reset_index(inplace=True)
    return chart_df


if __name__ == '__main__':

    # FETCH DATA

    symbol = input("Please input a stock symbol (e.g. 'MSFT'): ")
    parsed_response = fetch_data(symbol)

    # PROCESS DATA

    df = process_data(parsed_response)

    if isinstance(df, DataFrame):
    
        # DISPLAY RESULTS
        summary = summarize_data(df)

        print("LATEST CLOSING PRICE: ", summary["latest_close"])
        print("RECENT HIGH: ", summary["recent_high"])
        print("RECENT LOW: ", summary["recent_low"])

        # EXPORT PRICES TO CSV
        csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", f"{symbol.lower()}_prices.csv")
        df.to_csv(csv_filepath)

        # CHART PRICES OVER TIME
        chart_df = prepare_data_for_charting(df)
        fig = px.line(chart_df, x="date", y="close", title=f"Closing Prices for {symbol.upper()}") # see: https://plotly.com/python-api-reference/generated/plotly.express.line
        fig.show()
        