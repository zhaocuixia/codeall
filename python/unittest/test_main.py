from module import calculate
import unittest

class TestMath(unittest.TestCase):

    def setUp(self):
       print("test start")

    def test_0add(self):
       j = calculate.Math(5,10)
       self.assertEqual(j.add(),15)
       print('1')
       # self.assertEquals(j.add(),12)

    def test_1add1(self):
       j = calculate.Math(55,100)
       self.assertNotEqual(j.add(),145)
       print('2')
    def test_3add2(self):
       j = calculate.Math(5,10)
       self.assertTrue(j.add() > 10)
       print('3')

   @unittest.skip("skipping")#无条件忽略此测试方法   
    def test_4assertIs(self):
       self.assertIs("abc","abc")
       # self.assertIs("ab","abc")
       print('4')
    def test_5assertIn(self):
       self.assertIn("python","hello python")
       # self.assertIn("abc","hello python")
       print('5')
    def tearDown(self):
       print("test end")

if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suit = unittest.TestSuite()
   #suit.addTest(TestMath("test_case")) #写这个就可以，但是只能识别到以test开头的全部方法
   suit.addTest(TestMath("test_add1")) #写这个也是全部的case呢
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suit)
