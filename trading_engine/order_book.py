from collections import deque
# Stores list of buy and sell orders organized by price
class OrderBook:
    def __init__(self, symbol):
        self.symbol = symbol
        self.buy_orders = deque()    # highest price first, earliest timestamp
        self.sell_orders = deque()  # lowest price first, earliest timestamp

    def add_order(self, order):
        if order.side == "BUY":
            self.buy_orders.append(order)
            self.buy_orders = deque(sorted(self.buy_orders, key=lambda o: (-o.price, o.timestamp)))
        else:
            self.sell_orders.append(order)
            self.sell_orders = deque(sorted(self.sell_orders, key=lambda o: (o.price, o.timestamp)))

    def get_buy(self):
        if self.buy_orders:
            return self.buy_orders[0]
        return None
    
    def get_sell(self):
        if self.sell_orders:
            return self.sell_orders[0]
        return None

    def remove_order(self, order):
        if order.side == "BUY":
            self.buy_orders.popleft()
        else:
            self.sell_orders.popleft()