# main.py
from order import Order
from matching_engine import MatchingEngine
from trade_logger import TradeLogger
from datetime import datetime
import os
import time

DB_PATH = os.path.join(os.path.dirname(__file__), "trades.db")
logger = TradeLogger(db_name=DB_PATH)
engine = MatchingEngine(logger)

def main():

    from benchmark import benchmark
    benchmark()

    # start_time = time.time()

    # logger = TradeLogger()
    # engine = MatchingEngine(logger)

    # buy_order = Order(
    #     id="1",
    #     symbol="AAPL",
    #     side="BUY",
    #     price=150.00,
    #     quantity=10,
    #     timestamp=datetime.now()
    # )

    # sell_order = Order(
    #     id="2",
    #     symbol="AAPL",
    #     side="SELL",
    #     price=149.50,
    #     quantity=5,
    #     timestamp=datetime.now()
    # )

    # engine.add_order("AAPL", buy_order)
    # engine.add_order("AAPL", sell_order)

    # trades = logger.get_all_trades()
    # for t in trades:
    #     print(t)

    # logger.drop_table()

    # elapsed = time.time() - start_time

    # print(f"Total time elapsed: {elapsed:,.4f} sec")

if __name__== "__main__":
    main()