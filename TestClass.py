import unittest
from AutoTestLesson import Culc, Calendary, Fraction
@unittest.skip
class TestCulc(unittest.TestCase):

    def setUp(self) -> None:
        self.arr_obj_add = {
            Culc(3,2): 5,
            Culc(0,0): 0,
            Culc(-3,-2): -5,
            Culc(-3,2): -1,           
                            }
        return super().setUp()    
    def test_add(self):
        for couple in self.arr_obj_add:
            self.assertEqual(couple.add(), self.arr_obj_add[couple], 'Ошибка в ответе')

    @unittest.skip
    def test_not_None(self):
        for couple in self.arr_obj_add:
            self.assertIsNotNone(couple.mult(), 'Функция ничего не возвращает')

class TestFraction(unittest.TestCase):
    def setUp(self):
        self.test_obj = Fraction(3,4)
        self.arr_reduce = {
            Fraction(45, 90):'1/2',
            Fraction(12,3):'4/1',
            Fraction(11,17):'11/17'
        }
        self.arr_add = {
            '1/1': [Fraction(1,2),Fraction(4,8)],
            '5/2': [Fraction(1,2), Fraction(8,4)],
            '53/77':[Fraction(1,7), Fraction(6,11)]
        }
        self.arr_sub = {
            '1/2': [Fraction(2,2),Fraction(4,8)],
            '3/2': [Fraction(8,4), Fraction(1,2)],
            '31/77':[Fraction(6,11), Fraction(1,7)]
        }


        self.arr_mult = {
            '1/4': [Fraction(1,2),Fraction(4,8)],
            '1/1': [Fraction(1,2), Fraction(8,4)],
            '6/77':[Fraction(1,7), Fraction(6,11)]
        }
        self.arr_div = {
            '1/1': [Fraction(1,2),Fraction(4,8)],
            '1/4': [Fraction(1,2), Fraction(8,4)],
            '11/42':[Fraction(1,7), Fraction(6,11)]
        }
        return super().setUp()

    def test_output(self):
        self.assertIsNone(self.test_obj.output(), 'Функция не должна ничего возвращать')
    
    def test_get_numerator(self):
        self.assertEqual(self.test_obj.get_numerator(), 3, 'Числитель не соответствует вывода')

    def test_get_denominator(self):
        self.assertEqual(self.test_obj.get_denominator(), 4, 'Числитель не соответствует вывода')

    def test_reduce(self):
        for fr in self.arr_reduce:
            fr.com_numenator = fr.numerator
            fr.com_denominator = fr.denominator
            self.assertEqual(fr.reduce(),self.arr_reduce[fr], 'Произашла ошибка')
    
    def test_add(self):
        for answer in self.arr_add:
            self.assertEqual(self.arr_add[answer][0] + self.arr_add[answer][1], answer)

    def test_sub(self):
        for answer in self.arr_sub:
            self.assertEqual(self.arr_sub[answer][0] - self.arr_sub[answer][1], answer)

    def test_mul(self):
        for answer in self.arr_mult:
            self.assertEqual(self.arr_mult[answer][0] * self.arr_mult[answer][1], answer)

    def test_truediv(self):
        for answer in self.arr_div:
            self.assertEqual(self.arr_div[answer][0] / self.arr_div[answer][1], answer)


    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.testData ={Calculator(10,5):[15,5,50,2,5,10,10**5,0]}
    def test_cal(self):
        for num in self.testData:
    	    self.assertEqual(num.plus(),self.testDate[num][0])
            self.assertEqual(num.minus(),self.testDate[num][1])

unittest.main()