import time
import random
from main import engine, Order
from trade_logger import TradeLogger
from matching_engine import MatchingEngine
from datetime import datetime
import uuid
import os

# Regular Order Book
# DB_PATH = os.path.join(os.path.dirname(__file__), "trades.db")
# logger = TradeLogger(db_name=DB_PATH)
# engine = MatchingEngine(logger)

# symbols = ["AAPL", "GOOG", "TSLA", "MSFT"]

# def benchmark(num_orders=100_000):
#     start = time.time()

#     for _ in range(num_orders):
#         symbol = random.choice(symbols)
#         price = round(random.uniform(95, 105), 2)
#         quantity = random.randint(1, 100)
        
#         buy_order = Order(
#             id=str(uuid.uuid4()),
#             symbol=symbol,
#             side="BUY",
#             price=price,
#             quantity=quantity,
#             timestamp=datetime.now()
#         )
#         sell_order = Order(
#             id=str(uuid.uuid4()),
#             symbol=symbol,
#             side="SELL",
#             price=price,
#             quantity=quantity,
#             timestamp=datetime.now()    
#         )

#         engine.add_order(symbol, buy_order)
#         engine.add_order(symbol, sell_order)
    
#     elapsed = time.time() - start

#     print(f"Processed {num_orders:,} orders in {elapsed:.4f} sec")
#     print(f"Throughput {num_orders / elapsed:,.2f} orders/sec")
#     print("Benchmark complete!")

# Heap Order Book
class InMemoryLogger():
    def __init__(self):
        self.trades = []
        self.trade_count = 0

    def log_trade(self, trade):
        self.trades.append(trade)
        self.trade_count += 1
    
def benchmark(num_orders=100_000):
    logger = InMemoryLogger()
    engine = MatchingEngine(logger)

    symbols = ["AAPL", "GOOG", "TSLA", "MSFT"]
    orders = []

    for i in range(1, num_orders + 1):
        order = Order(
            id=str(uuid.uuid4()),
            symbol=random.choice(symbols),
            side=random.choice(["BUY", "SELL"]),
            price=round(random.uniform(95, 105), 2),
            quantity=random.randint(1, 100),
            timestamp=datetime.now()
        )
        orders.append(order)

    start_time = time.time()

    for order in orders:
        engine.add_order(order.symbol, order)

    elapsed = time.time() - start_time
    throughput = num_orders / elapsed

    print(f"Processed { num_orders } orders in { elapsed } seconds.")
    print(f"Total trades executed: { logger.trade_count }.")
    print(f"Throughput{ throughput } orders/sec.")
    print("Benchmark complete!")
