from conftest import mock_msft_response, mock_amzn_response #, mock_error_response, mock_rate_limit_response
from pandas import DataFrame

from app.robo import process_data, summarize_data, prepare_data_for_charting

# SKIP CI
def test_fetch(parsed_googl_response):
    # it should fetch data containing certain expected characteristics:
    response_keys = list(parsed_googl_response.keys()) # we are testing the fetch_data function indirectly through our fixture (see conftest.py)
    assert "Meta Data" in response_keys
    assert "Time Series (Daily)" in response_keys
    # ... including time series data with daily prices:
    daily_prices = list(parsed_googl_response["Time Series (Daily)"].values())[0] #> {'1. open': '2068.4700', '2. high': '2099.0000', '3. low': '2044.1218', '4. close': '2082.2200', '5. volume': '1319126'}
    price_keys = list(daily_prices.keys())
    assert price_keys == ["1. open", "2. high", "3. low", "4. close", "5. volume"]

# SKIP CI
def test_process(parsed_googl_response, parsed_oops_response):
    # it should process the nested response data:
    googl_df = process_data(parsed_googl_response)
    assert isinstance(googl_df, DataFrame)
    assert len(googl_df) == 100
    assert list(googl_df.columns) == ["date", "open", "high", "low", "close", "volume"]

    # it should gracefully handle response errors:
    assert process_data(parsed_oops_response) is None


def test_summarize():
    # it should summarize and aggregate the data:
    assert summarize_data(process_data(mock_msft_response)) == {
        'latest_close': 237.71,
        'recent_high': 240.055,
        'recent_low': 231.81
    }
    assert summarize_data(process_data(mock_amzn_response)) == {
        'latest_close': 3091.86,
        'recent_high': 3131.7843,
        'recent_low': 3030.05
    }

def test_charting():
    # it should sort dates in the proper order (ascending) for charting:
    df = process_data(mock_amzn_response)
    chart_df = prepare_data_for_charting(df)
    assert chart_df["date"].tolist() == ['2030-03-10', '2030-03-11', '2030-03-12', '2030-03-15', '2030-03-16']

