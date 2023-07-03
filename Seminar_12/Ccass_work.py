"""Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать
последние k значений. Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых
чисел и их факториалов."""


class Fact:
    def __init__(self, k: int):
        self.k = k
        self.save_list = list()

    def __call__(self, value):
        res = 1
        for i in range(2, value + 1):
            res *= i
        self.save_list.append(res)
        if len(self.save_list) > self.k:
            self.save_list.pop(0)
        return self.save_list[-1]

    def __str__(self):
        return f'{self.save_list}'

if __name__ == '__main__':
    fact = Fact(5)
    print(fact(5))
    print(fact(6))
    print(fact(7))
    print(fact(8))
    print(fact(9))
    print(fact(10))
    print(fact)

"""Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл."""
    mport
    json


    class Fact:
        _context_dict = dict()

        def __init__(self, k: int):
            self.k = k
            self.save_list = list()

        def __call__(self, value):
            res = 1
            for i in range(2, value + 1):
                res *= i
            self.save_list.append(res)
            if len(self.save_list) > self.k:
                self.save_list.pop(0)
            return self.save_list[-1]

        def __enter__(self):
            return self

        def mapper(self):
            for i, value in enumerate(self.save_list, start=1):
                self._context_dict[i] = value

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.mapper()
            with open('json_res.json', 'w') as f:
                json.dump(self._context_dict, f, indent=2)

        def __str__(self):
            return f'{self.save_list}'


    if __name__ == '__main__':
        with Fact(5) as fact:
            # fact = Fact(5)
            print(fact(5))
            print(fact(6))
            print(fact(7))
            print(fact(8))
            print(fact(9))
            print(fact(10))
            print(fact)

 """Создайте класс-генератор. Экземпляр класса должен генерировать факториал числа в диапазоне от start 
до stop с шагом step. Если переданы два параметра, считаем step=1. Если передан один параметр, также 
 считаем start=1."""
lass FactGenerator():

    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            result = 1
            for j in range(2, self.start + 1):
                result *= j
            self.start += self.step
            return result
        raise StopIteration


fg = FactGenerator(5)
for i in fg:
    print(i)

    """Доработайте класс прямоугольник из прошлых семинаров. Добавьте возможность изменять длину и 
    ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). Используйте декораторы свойств."""


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


    if __name__ == '__main__':
        rect_1 = Rectangle(2, 5)
        rect_2 = Rectangle(5, 10)
        print(rect_2)
        # print(f'{rect.perimeter()= } {rect.area()= }')
        # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
        res_sum = rect_1 + rect_2
        print(res_sum.a, res_sum.b)
        res_sub = rect_1 - rect_2
        print(res_sub.a, res_sub.b)

class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self._a = a
        self._b = b if b is not None else a

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('a не может быть отрицательной')

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError('b не может быть отрицательной')

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


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    # rect_2 = Rectangle(5, 10)
    print(rect_1.a)
    print(rect_1.b)
    #rect_1.a = -1
    rect_1.a = 10
    print(rect_1)
    # print(rect_2)
    # # print(f'{rect.perimeter()= } {rect.area()= }')
    # # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
    # res_sum = rect_1 + rect_2
    # print(res_sum.a, res_sum.b)
    # res_sub = rect_1 - rect_2
    # print(res_sub.a, res_sub.b)

    __slots__ = ('_a', '_b')

