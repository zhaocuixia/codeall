import pytest


def add(x):
    return x + 2

class TestClass(object):

    def setup_class(self):
        print("setup_class(self)：每个类之前执行一次")

    def teardown_class(self):
        print("teardown_class(self)：每个类之后执行一次")

    def setup_method(self):
        print("setup_method(self):在每个方法之前执行")

    def teardown_method(self):
        print("teardown_method(self):在每个方法之后执行\n")

    @pytest.mark.run(order=1)  # 控制执行顺序
    def test_add(self):
        print('1')
        assert add(3) == 5


    #  @pytest.mark.zcx  只运行某个标记的用例
    def test_add2(self):
        print('3')
        assert add(2) == 4

    @pytest.mark.run(order=2)  # 要安装 pip3 install pytest-ordering

    def test_add3(self):
        print('2')
        assert add(4) == 6



if __name__ == "__main__":
    pytest.main(["-s", "test_demo.py"])
