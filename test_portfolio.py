from portfolio import Portfolio

def test_empty_portfolio():
    p=Portfolio()
    assert p.cost()== 10000.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

