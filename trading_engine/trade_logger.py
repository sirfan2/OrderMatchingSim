import sqlite3
# Saves trades to SQLite database
class TradeLogger:
    def __init__(self, db_name="trades.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    # Create table if doesn't exist
    def create_table(self):
        with self.conn:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trades (
                trade_id INTEGER NOT NULL,
                buy_order_id TEXT NOT NULL,
                sell_order_id TEXT NOT NULL,
                symbol TEXT NOT NULL,
                price REAL NOT NULL,
                quantity REAL NOT NULL,
                timestamp TEXT
            )
            """)

    def log_trade(self, trade):
        with self.conn:
            self.cursor.execute("""
            INSERT INTO trades (trade_id, buy_order_id, sell_order_id, symbol, price, quantity, timestamp)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """, ( 
                trade.trade_id, 
                trade.buy_order_id,
                trade.sell_order_id, 
                trade.symbol, 
                trade.price, 
                trade.quantity, 
                trade.timestamp 
            ))
            self.conn.commit()

    def get_all_trades(self):
        with self.conn:
            return self.cursor.execute("SELECT * FROM trades")
        
    def drop_table(self):
        with self.conn:
            self.cursor.execute(f"DROP TABLE IF EXISTS {"trades"}")

            self.conn.commit()
        print(f"Table trades has been deleted")