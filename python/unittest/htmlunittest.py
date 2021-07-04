import unittest
from HtmlTestRunner.HTMLTestRunner import HTMLTestRunner
def calc(x,y):
    return x+y

class TestCalc(unittest.TestCase):
    def test_pass_case(self):
        print('这是一条通过的用例')
        res = calc(1, 2)
        self.assertEqual(3, res)
    # def test_fail_case(self):
    #     print('这是一条失败的用例')
    #     res = calc(1, 2)
    #     self.assertEqual(5, res)

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestCalc))
    f = open('report0304.html','w')  #打开一个测试报告文件
    runner = HTMLTestRunner(stream=f,title='mpp0304测试结果',description='mpp0304的测试报告描述')
    runner.run(suite) #运行测试套件中的用例，
