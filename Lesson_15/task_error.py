class UserExeption (Exception):
    '''Базовое исключение с имплементацией от Exception'''
    pass

class aa01ValueInputError(UserExeption):
    '''Исключение ошибки ввода базового значения символа дисплея калькулятора'''

    def __str__ (self):
        return f"Этот символ  на экране калькулятора при старте - неуместен"



class aa02ValuePozitionError(UserExeption):
    '''Исключение ошибки ввода базового значения символа дисплея калькулятора по оси Х'''

    def __init__(self,name,lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        if self.lower < self.name < self.upper:
            return ("Символ находится в пределах окна, но далеко от левой стороны")



class aa02ValueMaxPozitionError(UserExeption):
    '''Исключение максимальной ошибки ввода базового значения символа дисплея калькулятора по оси Х'''

    def __init__(self,name, upper):
        self.name = name
        self.upper = upper

    def __str__(self):
        if self.upper < self.name:
            return ("Символ вышел за пределы правой границы окна")


class aa03ValuePozitionError(UserExeption):
    '''Исключение ошибки ввода базового значения символа дисплея калькулятора по оси У'''

    def __init__(self,name,lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        if  self.name < self.lower:
            return ("Символ находится выше верхней границы окна калькулятора, он вне поля программы")
        if  self.name > self.upper:
            return ("Символ находится ниже нижней границы окна калькулятора, его не видно за кнопками")
