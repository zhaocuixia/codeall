import pytest


@pytest.fixture(scope='function')   # 被这个标注的不是test测试用例了
def test3():  # 你什么时候执行
    print('test3')


def test4(test3):
    print('test4')

@pytest.mark.usefixtures('test3')  # 写这个相当于在test5放test3了,这个还算测试用例
def test5():
   print('test5')

@pytest.fixture(scope='function',autouse='true')  # 不算测试用例了
def test6():
    print('test6')

class TestClass(object):

    def testa(self):
        print('testa')

    def testb(self):
        print('testb')



if __name__ == "__main__":
    pytest.main(["-s", "test_scope.py"])
