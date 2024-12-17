# Import the necessary libraries
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt

# Step 2: Function to get the BTC/USDT price from the Binance API
# This function makes a request to the Binance API and returns the current price of the BTC/USDT pair.
def get_binance_btc_usdt_price():
    """
    Retrieves the current price of the BTC/USDT pair from the Binance API.

    Parameters:
    None.

    Returns:
    - dict: A dictionary containing the following information:
        - 'Price': Current BTC/USDT price (float).
        - 'Pair': Currency pair, in this case 'BTC/USDT' (string).
        - 'Exchange': Exchange name, in this case 'Binance' (string).
    - None: Returns None if there is an error accessing the API.

    Exceptions:
    - If the request is unsuccessful (status other than 200), 
      the function displays an error message and returns None.
    """
    # API URL and the BTC/USDT symbol as a parameter
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol': 'BTCUSDT'}

    # Sends a GET request to the Binance API
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Extracts the price and returns the information
        data = response.json()
        price = float(data['price'])
        return {'Price': price, 'Pair': 'BTC/USDT', 'Exchange': 'Binance'}
    else:
        print("Error accessing the Binance API.")
        return None

# Step 3: Function to monitor the BTC/USDT price
# This function collects the BTC/USDT price at regular intervals for a specified period.
def monitor_binance_btc_usdt_price(interval=10, duration=300):
    """
    Monitors the BTC/USDT price at regular intervals over a specified period.

    Parameters:
    - interval (int): Time interval, in seconds, between each API request. Default is 10 seconds.
    - duration (int): Total monitoring duration, in seconds. Default is 300 seconds.

    Returns:
    - No direct return. Data is saved to a CSV file ('/content/binance_prices.csv').

    Exceptions:
    - If the function cannot access the API at any iteration, the error is handled internally, 
      and the loop continues.
    """
    # Initializes a list to store the data
    data = []
    start_time = time.time()

    while (time.time() - start_time) < duration:
        # Retrieves the current BTC/USDT price
        btc_usdt_data = get_binance_btc_usdt_price()
        timestamp = pd.Timestamp.now()

        if btc_usdt_data:
            print(f"{timestamp} - Price: ${btc_usdt_data['Price']} - Pair: {btc_usdt_data['Pair']} - Exchange: {btc_usdt_data['Exchange']}")
            data.append([timestamp, btc_usdt_data['Price'], btc_usdt_data['Pair'], btc_usdt_data['Exchange']])

        time.sleep(interval)

    # Converts the data list to a DataFrame and saves it as CSV
    df = pd.DataFrame(data, columns=['Timestamp', 'Price', 'Pair', 'Exchange'])
    df.to_csv('/content/binance_prices.csv', index=False)
    print("Monitoring completed. Data saved to '/content/binance_prices.csv'.")

# Step 4: Function to visualize the collected data
# This function loads the data from the CSV and generates a price trend chart for BTC/USDT over time.
def plot_binance_prices(file_path='/content/binance_prices.csv'):
    """
    Plots a chart of BTC/USDT price evolution over time, based on data saved in CSV.

    Parameters:
    - file_path (str): Path to the CSV file containing price data. Default is '/content/binance_prices.csv'.

    Returns:
    - No direct return. The chart is displayed on the screen.

    Exceptions:
    - If the CSV file is not found or there is an error reading the data, the error is handled internally.
    """
    # Reads the CSV data, converting the 'Timestamp' column to datetime format
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])

    # Generates a line chart for the BTC/USDT price
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['Price'], marker='o', linestyle='-')
    plt.xlabel('Timestamp')
    plt.ylabel('BTC/USDT Price (USD)')
    plt.title('BTC/USDT Price Over Time on Binance')
    plt.grid()
    plt.show()

# Step 5: Monitoring and visualization execution
# This line of code runs the monitoring for 60 seconds, collecting data every 6 seconds.
monitor_binance_btc_usdt_price(interval=6, duration=60)

# After monitoring, it displays the chart with the collected data.
plot_binance_prices('/content/binance_prices.csv')