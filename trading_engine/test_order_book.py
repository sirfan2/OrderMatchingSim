from order import Order
from trade import Trade
from order_book import OrderBook
import datetime

book = OrderBook(symbol="AAPL")

o1 = Order(id=1, symbol="AAPL", side="BUY", price=150.00, quantity=10, timestamp=datetime.datetime.now())
o2 = Order(id=2, symbol="AAPL", side="BUY", price=151.00, quantity=5, timestamp=datetime.datetime.now())
o3 = Order(id=3, symbol="AAPL", side="BUY", price=149.50, quantity=20, timestamp=datetime.datetime.now())

o4 = Order(id=4, symbol="AAPL", side="SELL", price=152.00, quantity=8, timestamp=datetime.datetime.now())
o5 = Order(id=5, symbol="AAPL", side="SELL", price=150.50, quantity=15, timestamp=datetime.datetime.now())

book.add_order(o1)
book.add_order(o2)
book.add_order(o3)
book.add_order(o4)
book.add_order(o5)

best_buy = book.get_buy()
best_sell = book.get_sell()

print("Best BUY:", best_buy.price, "Quantity:", best_buy.quantity)  # Expect 151.00
print("Best SELL:", best_sell.price, "Quantity:", best_sell.quantity)  # Expect 150.50

book.remove_order(best_buy)
best_buy = book.get_buy()
print("New Best BUY after removal:", best_buy.price)    # Expect 150.00