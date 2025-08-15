import heapq

# Order Book class using heaps
class HeapOrderBook:
    def __init__(self, symbol):
        self.symbol = symbol
        self.buy_heap = [] # stores (price, timestamp, order)
        self.sell_heap = []

    def heap_add_order(self, order):
        if order.side == "BUY":
            heapq.heappush(self.buy_heap, (-order.price, order.timestamp, order))
        else:
            heapq.heappush(self.sell_heap, (order.price, order.timestamp, order))
    
    def heap_get_buy(self):
         while self.buy_heap:
            top_price, top_ts, top_order = self.buy_heap[0]
            if top_order.quantity > 0:
                return top_order
            else:
                heapq.heappop(self.buy_heap)
            return None
    
    def heap_get_sell(self):
        while self.sell_heap:
            top_price, top_ts, top_order = self.sell_heap[0]
            if top_order.quantity > 0:
                return top_order
            else: heapq.heappop(self.sell_heap)
        return None
    
    def heap_remove_order(self, order):
        pass