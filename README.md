
# Bitcoin Price Monitoring

This project aims to monitor the BTC/USDT price using the Binance API, save the data to a CSV file, and visualize the price trend over time.

## Project Structure

- **binance_btc_usdt_price_monitor.py**: The main script that contains all steps for data collection, monitoring, and visualization.
- **requirements.txt**: Contains the necessary Python packages to run the project.
- **README.md**: Project documentation.

---

## Requirements

To run this project, you need the following Python packages:

- `requests` - For accessing the Binance API.
- `pandas` - For data storage and manipulation.
- `matplotlib` - For plotting the price trend.

Install the packages using:

```bash
pip install -r requirements.txt
```

---

## Steps

### 1. API Integration

The script connects to the Binance API and fetches real-time BTC/USDT prices using a GET request.

### 2. Data Collection

Collected data includes:

- Timestamp
- BTC/USDT Price
- Trading Pair
- Exchange Name

### 3. Data Logging

The data is stored in a CSV file named `binance_prices.csv`.

### 4. Visualization

The script generates a time-series chart showing price variations over time.

---

## Usage

1. **Run the Script:**

   ```bash
   python binance_btc_usdt_price_monitor.py
   ```

2. **Monitoring and Visualization:**

   - The script monitors BTC/USDT prices for 60 seconds, collecting data every 6 seconds.
   - After monitoring, it generates a time-series plot showing price variations.

---

## Results

The script outputs:

- Real-time prices displayed in the console.
- A CSV file containing all recorded prices.
- A time-series chart showing BTC/USDT price fluctuations.

---

## Directory Structure

```
project-folder/
│
├── binance_btc_usdt_price_monitor.py    # Main script for monitoring
├── requirements.txt                     # Dependencies list
└── binance_prices.csv                   # Collected price data
```
