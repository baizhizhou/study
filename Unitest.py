import unittest

class  fortest(unittest.TestSuite):

    @classmethod
     # 测试用例
    def setUp(cls) -> None:
         print('setuo')
    @classmethod
    def teardown(cls) -> None:
         print('teardown')
    def pus(self, a, b):
         return a+b
    def test_a(self):
         print('a')
    def test_b(self):
         self.pus(1,2)
         
         print('c')

if __name__=='__main__':
    unittest.main()