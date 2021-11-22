

class Portfolio:
    def _init_(self):
        self._stocks = []

    def buy(self,name,shares,price):
        self._stocks.append((name,shares,price))

    def cost(self):
        return sum(shares * price for _, shares, price in self._stocks) #dont care about the name so using _