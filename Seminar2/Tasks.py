"Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные"
 a = 1
 b = 'строка'
 с = 0,3
 d = (1, 1)
 e = {1: 3}
 print(f'a - {type(a)}, b - {type(b)}, c - {type(c)}, d - {type(d)}, e - {type(e)} ')

"Создайте в переменной data список значений разных типов"
"перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:"
"порядковый номер начиная с единицы значение адрес в памяти размер в памяти"
"хэш объекта результат проверки на целое число только если он положительный"
"результат проверки на строку только если он положительный"
"*Добавьте в список повторяющиеся элементы и сравните на результаты"

 data = [a, b, c, d, e]
 for i, el in enumerate(data):
     print(1, el id(el), __sizof__(), hash (el))
     if isinstance(el, int):
         print('это целое число')
         elif


"Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление."
"Функции bin и oct используйте для проверки своего результата, а не для решения."
"*Дополнительно Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления"
"Избегайте магических чиселДобавьте аннотацию типов где это возможно"

def task3(num: int, mode: str) -> str:
    result = ''
    convert: int = 2

    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8

    while num >= 1:
        res = num % convert

        result += str(res)
        num = num // convert

    return result[::-1]


print(task3(21, mode="bin"), f"assert: {bin(21)}")
print(task3(21, mode="oct"), f"assert: {oct(21)}")

# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
#
# ✔ Диаметр не превышает 1000 у.е.
#
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
from math import pi
import decimal


def circle(d: decimal) -> tuple[decimal, decimal]:
    decimal.getcontext().prec = 42
    _pi = decimal.Decimal(pi)
    if d <= 1000:
        s = (_pi * d**2) / 4
        l = _pi * d

    return decimal.Decimal(s), decimal.Decimal(l)

# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
#
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

# 6) Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
class Bank:

    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _out(self, cash: int, commission: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission) >= 0:
            self._BALANCE -= cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION

        _MAX = 600
        _MIN = 30

        if sum_commission > _MAX:
            return _MAX
        elif sum_commission < _MIN:
            return _MIN
        else:
            return int(sum_commission)

    def _check_operation(self):
        return (False, True)[self._OPERATION % 3]

    def _exit(self):
        return "Всего доброго, приходите к нам еще"

    def start(self, mode: str, cash: int = 0) -> str:

        check_operation = self._check_operation()

        if check_operation:
            self._BALANCE += self._BALANCE * self._BONUS

        match mode:
            case "in":
                data = self._in(cash=cash)

                com_data = self._check_commission(cash=cash)

                return f"Средства были зачислены сумма: {cash}, баланс: {self._BALANCE}"

            case "out":
                com_data = self._check_commission(cash=cash)

                data = self._out(cash=cash, commission=com_data)

                if data:
                    return f"Операция осуществлена успешно, сумма: {cash}, коммисия: {com_data}, баланс: {self._BALANCE}"
                else:
                    return "Нехватает средств"

            case "exit":
                return self._exit()

2