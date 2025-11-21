from app.main import add
from app.calculate import calculate

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_three_args():
    assert add(2, 3, 4) == 9
    assert add(-1, 1, 1) == 1
    assert add(0, 0, 0) == 0

def test_calculate():
    result = calculate(1, 2, 3, 4)
    assert result == 10     # 1+2+3+4