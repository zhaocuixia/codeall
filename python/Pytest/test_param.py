import pytest
import random


@pytest.mark.parametrize('x', [1, 2, 6])
def test_add(x):
    print(x)
    assert x == random.randrange(1, 7)


#  多个参数
@pytest.mark.parametrize('x,y', [
    (1+2, 3),
    (2-0, 1),
    (6*2, 12),
    (10*2, 3),
    ("test", "test"),
])
def test_add(x, y):  # 必须与上面保持一致，只能用x,y不能用其他字母
    assert x == y



if __name__ == "__main__":
    pytest.main(["-s", "test_param.py"])
