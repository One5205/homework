import pytest
import allure
# from python import calc
import self as self

from  python.calc import *


class TestCalcAdd:
    c=Calc()
    @allure.testcase('测试两个小数相加')
    def test_add_float(self):

        result=Calc.add(self,1.5,2.5)
        assert 4==result
        print(result)

    @allure.testcase('测试两个整数相加')
    def test_add_int(self):

        result=Calc.add(self,1,2)
        assert result ==3
        print(result)

    @allure.testcase('测试两个负数相加')
    def test_add_negative(self):

        result=Calc.add(self,-1,-2)
        assert -3==result
        print(result)

    @allure.testcase('测试负数和整数相加')
    def test_add_positiveandnegative(self):

        result=Calc.add(self,-1,2)
        assert 1==result
        print(result)

    @allure.testcase('测试整数和小数相加')
    def test_add_intandfloat(self):
        result=Calc.add(self,1,2.88)
        assert 3.88==result
        print(result)

    @allure.testcase('测试0和0相加')
    def test_add_zeroandzero(self):
        result=Calc.add(self,0,0)
        assert 0==result
        print(result)

    @allure.testcase('测试含有字符')
    def test_add_containstring(self):
        try:
            result=Calc.add(self,'d','ewjqoe')
        except:
            result='输入的值不合法'
        assert 'dewjqoe'==result

class TestCalcDiv:

    @allure.testcase('测试整数除以整数')
    def test_div_intandint(self):
        result=Calc.div(self,10,2)
        print(result)
        assert 5==result

    @allure.testcase('测试整数除以浮点数')
    def test_div_intandfloat(self):
        result=Calc.div(self,10,2.5)
        assert 4==result

    @allure.testcase('测试正数除以负数')
    def test_div_positiveandnegative(self):
        result=Calc.div(self,5,-1)
        assert -5==result

    @allure.testcase('测试0除以其它数')
    def test_div_zerodiv(self):
        result=Calc.div(self,0,-23)
        assert 0==result

    @allure.testcase('测试除以0')
    def test_div_divzero(self):
        try:
            result=Calc.div(self,5,0)
        except:
            result='被除数不能为0'
        assert '被除数不能为0' == result

    @allure.testcase('测试包含有字符类型')
    def test_div_containstring(self):
        try:
            result=Calc.div(self,'qwe','asd')
        except:
            result ='输入值不合法'
        assert '输入值不合法'==result
