import pytest

@pytest.fixture()  # 被这个标注的不是test测试用例了
def test1():
    a = 'zcx'
    return a  # 肯定有返回值，没有默认是null

def test2(test1):
    assert test1 == 'zcx'

@pytest.fixture()
def test3():
    a = 'leo'
    b = '123456'
    print('传出a,b')
    return (a, b)

def test4(test3):
    u = test3[0]
    p = test3[1]
    assert u == 'leo'
    assert p == '123456'
    print('元祖形式正确')

def test5(test1, test3):
    u = test1
    p = test3
    assert u == 'zcx'
    assert p == ('leo', '123456')


if __name__ == "__main__":
    pytest.main(["-s", "test_fixture.py"])
