import string


def remove_chars(text: str) -> str:
    alpha = string.ascii_letters + ' '
    print(alpha)
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    print(remove_chars('sDDsdsd вывывывывы  выввы1323232'))

"""Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
●	возврат строки без изменений
●	возврат строки с преобразованием регистра без потери символов
●	возврат строки с удалением знаков пунктуации
●	возврат строки с удалением букв других алфавитов
●	возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

import string
import doctest


def remove_chars(text: str) -> str:
    '''
    text
    >>> remove_chars('dddddd dddd')
    'dddddd dddd'
    >>> remove_chars('AAA AA')
    'aaa aa'
    >>> remove_chars('a,a,n: v.v;')
    'aan vv'
    >>> remove_chars('БВАОПоаоваов')
    ''
    >>> remove_chars('WWW,3322,ГГ:')
    'www'
    '''
    alpha = string.ascii_letters + ' '
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    # print(remove_chars('sDDsdsd вывывывывы  выввы1323232'))
    doctest.testmod(verbose=True)


class TestChars(ut.TestCase):
    def test_no_change(self):
        self.assertEqual(remove_chars('dddddd dddd'), 'dddddd dddd')

    def test_lover(self):
        self.assertEqual(remove_chars('AAA AA'), 'aaa aa')

    def test_sign(self):
        self.assertEqual(remove_chars('a,a,n: v.v;'), 'aan vv')

    def test_cyrillic(self):
        self.assertEqual(remove_chars('БВАОПоао ваов'), '')

    def test_upper(self):
        self.assertEquals(remove_chars('WWW,3322,ГГ:'), 'www')


if __name__ == '__main__':
    unit_test = TestChars()
    unit_test.main(verbosity=True)


    def test_remove_chars_no_change():
        assert remove_chars('dddddd dddd') == 'dddddd dddd'


    def test_remove_chars_lower():
        assert remove_chars('AAA AA') == 'aaa aa'


    def test_remove_chars_remove_chars():
        assert remove_chars('a,a,n: v.v;') == 'aan vv'


    def test_remove_chars_remove_rus_alpha():
        assert remove_chars('БВАОПоаоваов') == ''


    def test_remove_chars_remove_all():
        assert remove_chars('WWW,3322,ГГ:') == 'www'


    if __name__ == '__main__':
        pytest.main(['-v'])


        class Rectangle:
            '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

            def __init__(self, a: int, b: int = None):
                '''Метод инициализации прямоугольника со сторонами a и b.'''
                self.a = a
                self.b = b if b is not None else a

            def perimeter(self):
                '''Метод расчета периметра прямоугольника.'''
                return 2 * (self.a + self.b)

            def area(self):
                '''Метод расчета площади прямоугольника.'''
                return self.a * self.b

            def __add__(self, other):
                '''Переопределенный дандер метод сложения двух прямоугольников.'''
                new_perimeter = self.perimeter() + other.perimeter()
                new_a = self.a
                new_b = new_perimeter / 2 - new_a
                return Rectangle(new_a, new_b)

            def __sub__(self, other):
                '''Переопределенный дандер метод вычетания двух прямоугольников.'''
                new_perimeter = abs(self.perimeter() - other.perimeter())
                new_a = min([self.a, self.b, other.a, other.b])
                new_b = new_perimeter / 2 - new_a
                return Rectangle(new_a, new_b)

            def __str__(self):
                '''Переопределенный дандер метод строчного выведения экземпляра класса'''
                return f'Прямоугольник {self.a} x {self.b}'


        class TestRectangle(unittest.TestCase):

            def setUp(self) -> Rectangle:
                self.rectangle_1 = Rectangle(2, 3)
                self.rectangle_2 = Rectangle(5, 10)
                self.rectangle_3 = Rectangle(5)

            def test_perimeter(self):
                self.assertEqual(self.rectangle_1.perimeter(), 10)

            def test_area(self):
                self.assertEqual(self.rectangle_2.area(), 50)

            def test_sum_rect(self):
                self.assertEqual((self.rectangle_1 + self.rectangle_2).perimeter(), 40)

            def test_str(self):
                self.assertEqual(self.rectangle_1.__str__(), 'Прямоугольник 2 x 3')


        if __name__ == '__main__':
            # rect_1 = Rectangle(2, 5)
            #
            # rect_2 = Rectangle(5, 10)
            # print(rect_2)
            # # print(f'{rect.perimeter()= } {rect.area()= }')
            # # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
            # res_sum = rect_1 + rect_2
            # print(res_sum.a, res_sum.b)
            # res_sub = rect_1 - rect_2
            # print(res_sub.a, res_sub.b)
            unittest.main(verbosity=True)

        23: 19


        class Bank:
            _BALANCE = 0
            _MIN = 50
            _MAX = 5000000
            _COMMISSION = 0.015
            _BONUS = 0.03
            _TAX = 0.10
            _OPERATION: int
            _OPERATIONS: list[str]

            def __init__(self):
                self._OPERATION = 0
                self._OPERATIONS = dict()

            def _in(self, cash: int, tax: int) -> tuple[int, int] | None:
                if cash % self._MIN == 0:
                    self._BALANCE += cash + tax
                    self._OPERATION += 1
                    self._OPERATIONS[f'+ {cash + tax}'] = 'Пополнение'
                    return self._BALANCE, self._OPERATION
                else:
                    return None

            def _out(self, cash: int, commission: int, tax: int) -> tuple[int, int] | None:
                if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission + tax) >= 0:
                    self._BALANCE -= cash + commission + tax
                    self._OPERATION += 1
                    self._OPERATIONS[f'- {cash + commission + tax}'] = 'Снятие'
                    return self._BALANCE, self._OPERATION
                else:
                    return None

            def _check_commission(self, cash: int) -> int:
                sum_commission = cash * self._COMMISSION
                _MAX = 600
                _MIN = 30
                if sum_commission > _MAX:
                    sum_commission = _MAX
                elif sum_commission < _MIN:
                    sum_commission = _MIN
                else:
                    sum_commission = int(sum_commission)
                return sum_commission

            def _check_tax(self, cash: int) -> int:
                if cash >= self._MAX:
                    print(f'\nВнимание был снят налог на богатство в размере {cash * self._TAX}')
                    return cash * self._TAX
                else:
                    return 0

            def _exit(self):
                return "Всего доброго, приходите к нам еще"

            def add_bonus(self):
                self._BALANCE += self._BALANCE * self._BONUS
                return f'Поздравляем, вы получили бонус за каждую 3-юю операцию в нашем банке . ' \
                       f'На ваш счет было зачислено: {int(self._BALANCE * self._BONUS)}\n'

            def _show_operations(self) -> None:
                for summ, op in self._OPERATIONS.items():
                    print(f'{summ} - {op}')

            def start(self, mode: str, cash: int = 0) -> str:
                if self._OPERATION % 3 == 0:
                    print(self.add_bonus())
                tax = self._check_tax(cash)
                match mode:
                    case "in":
                        self._in(cash=cash, tax=tax)
                        return f"Средства были зачислены сумма: {cash}, баланс: {int(self._BALANCE)}"
                    case "out":
                        commission = self._check_commission(cash=cash)
                        data = self._out(cash=cash, commission=commission, tax=tax)
                        if data:
                            return f"Операция осуществлена успешно, сумма: {cash}, коммисия: {commission}, " \
                                   f"баланс: {int(self._BALANCE)}"
                        else:
                            return "Нехватает средств"

                    case "show":
                        self._show_operations()

                    case "exit":
                        return self._exit()


        bank = Bank()
        print(bank.start(mode='in', cash=4000000))
        print(bank.start(mode='in', cash=100000))
        print(bank.start(mode='out', cash=100000))
        print(bank.start(mode='in', cash=100000))
        print(bank.start(mode='in', cash=1000000))
        print(bank.start(mode='in', cash=2000000))
        print(bank.start(mode='out', cash=5000000))
        print(bank.start(mode='show'))

        2
