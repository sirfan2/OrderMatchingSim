from trade import Trade
import uuid
from datetime import datetime, timezone
# Coordinates order books, matches trades, and sends results to logger
class MatchingEngine:
    def __init__(self, trade_logger):
        self.trade_logger = trade_logger
        self.order_books = {}    # symbol -> OrderBook
    
    def add_order(self, symbol, order):
        if symbol not in self.order_books:
            # from order_book import OrderBook
            # self.order_books[symbol] = OrderBook(symbol)
            from heap_order_book import HeapOrderBook
            self.order_books[symbol] = HeapOrderBook(symbol)

        book = self.order_books[symbol]
        # book.add_order(order)
        book.heap_add_order(order)
        self.match_orders(symbol)

    def match_orders(self, symbol):
        book = self.order_books.get(symbol)
        if not book:
            return

        while True:
            # best_buy = book.get_buy()
            # best_sell = book.get_sell()
            
            best_buy = book.heap_get_buy()
            best_sell = book.heap_get_sell()

            if not best_buy or not best_sell:
                break

            if best_buy.price >= best_sell.price:
                matched_quantity = min(best_buy.quantity, best_sell.quantity)
                trade_price = best_sell.price

                trade = Trade(
                    trade_id=str(uuid.uuid4()),
                    buy_order_id=best_buy.id,
                    sell_order_id=best_sell.id,
                    symbol=symbol,
                    price=trade_price,
                    quantity=matched_quantity,
                    timestamp=datetime.now(timezone.utc).isoformat()
                )

                self.trade_logger.log_trade(trade)

                best_buy.quantity -= matched_quantity
                best_sell.quantity -= matched_quantity

                # Remove fully filled orders
                if best_buy.quantity == 0:
                    # book.remove_order(best_buy)
                    book.heap_remove_order(best_buy)
                if best_sell.quantity == 0:
                    # book.remove_order(best_sell)
                    book.heap_remove_order(best_sell)
            else:
                break