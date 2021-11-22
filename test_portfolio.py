from potfolio import Portfolio

p = Portfolio()
print(f"Empty portfolio cost: {p.cost()}, should be 0.0")
p.buy("IBM", 100, 176.48)
print(f"With 100 IBM @ 176.48: {p.cost()}, should be 17648.0")
p.buy("HPQ", 100, 36.15)
print(f"With 100 HPQ @ 36.15: {p.cost()}, should be 21263.0")

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM",100, 176.48)
    assert p.cost() == 17648.0

def test_buy_two_stocks():
    p = Portfolio()
    p.buy("IBM",100,176.48)
    p.buy("HPQ",100,36.15)
    assert p.cost() == 21263.00

def test_not_enough_arguments_to_buy():
    p = portfolio()
    with pytest.raises(TypeError):
        p.buy("IBM")
    


