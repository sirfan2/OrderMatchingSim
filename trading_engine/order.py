# Represents single buy or sell order
class Order:
    def __init__(self, id, symbol, side, price, quantity, timestamp):
        self.id = id    # unique id
        self.symbol = symbol    # stock or asset symbol
        self.side = side    # buy or sell
        self.price = price  # limit price
        self.quantity = quantity    # total units
        self.timestamp = timestamp  # time order was placed

        