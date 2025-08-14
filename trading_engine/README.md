# Trading Engine Project

## Overview 
A Python-based order matching engine simulating a stock exchange order book.
Uses SQLite to log executed trades.

## Features
- Object-oriented design
- Order matching by price-time priority
- Trade logging to SQLite
- Easily extendable to multiple symbols

## Setup

### 1. Install Python
Make sure you have **Python 3.10+** installed.
You can check your version by running:
```bash
python --version
```

### 2. Clone the Repository and Create a Virtual Environment
Clone the repository:
```bash
git clone https://github.com/sirfan2/trading-engine.git
cd trading-engine
```
You can also optionally create a virtual environment. Python venv was used for this project.
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate    # macOS/Linux
```

There are no extra dependencies required to run this project. All used libraries are included in Python's standard library.

### 3. Run the Application
Run the application:

```bash
python trading_engine/main.py
```
### 4. Viewing Trades
To view logged trades in the SQLite database:

```bashw
sqlite3 trades.db
SELECT * FROM trades;
.exit
```

Alternatively, if using VSCode, install the **SQLite Viewer** extension. Then after running the program, click into trades.db to view the existing table.

## How it Works
1. Orders are first added to an order book per symbol.
2. Matching engine matches the best buy and sell orders when prices overlap.
3. Matched trades are logged into a trades.db SQLite database.
