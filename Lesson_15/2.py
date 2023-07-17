# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from task_error import aa01ValueInputError, aa02ValuePozitionError, aa02ValueMaxPozitionError,  aa03ValuePozitionError

from tkinter import *

class Main(Frame):

    MIN_aa02 = 0
    MAX_aa02 = 100
    HALF_LIFE = 50

    MIN_aa03 = 0
    MAX_aa03 = 40

    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()


    def build(self, aa01= input(" Введите '0', это будет исходное значение на экране калькулятора\n"),
              aa02= int (input (" Введите '2', это будет отступ слева для размещения исходного значения '0' на экране калькулятора\n")),
              aa03= int (input (" Введите '10', это будет отступ сверху для размещения значения '0' на экране калькулятора\n"))):

        if aa01 == '0':
            self.formula = aa01 # исходное значение на табло
        else:
            raise aa01ValueInputError  # ошибка ввода исходного значения


        self.lbl = Label(text=self.formula, font=(
            "https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Roboto:ital,wght@1,100&family=Secular+One&display=swap" ,
            21, "bold"), bg="#72cced", foreground="#0b0514")


        if self.MIN_aa02 < aa02 < self.MAX_aa02:
            print(aa02,"Символ находится в пределах окна, но уже слишком далеко от левой стороны")  # это не ошибка,
            # тут мы показываем пользователю
            # где будет находиться символ
        else:
            self.lbl.place(x=aa02, y=0)



        if self.HALF_LIFE < aa02 < self.MAX_aa02:
            raise aa02ValuePozitionError (aa02, self.HALF_LIFE, self.MAX_aa02) # ошибка позиционирования символа в пределах окна калькулятора
        else:
            self.lbl.place(x=aa02, y=0)


        if aa02 > self.MAX_aa02 :
            raise aa02ValueMaxPozitionError (aa02, self.MAX_aa02) # ошибка выхода за правую границу окна калькулятора
        else:
            self.lbl.place(x=aa02, y=0)



        if self.MIN_aa03 < aa03 < self.MAX_aa03:
            self.lbl.place(x=aa02, y=aa03)
        else:
            raise aa03ValuePozitionError (aa03, self.MIN_aa03, self.MAX_aa03)  # ошибка позиционирования по нижней границе окна

        btns = [
            "%", "CE", "C", "⌫",
            "1/x", "x²", "√x", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "2", "+",
            "+/-", "0", ".", "="
        ]

        x = 3 # отступ блока кнопок слева
        y = 70 # отступ блока кнопок сверху
        for bt in btns:
            def com(x=bt): return self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Roboto:ital,wght@1,100&family=Secular+One&display=swap", 10),
                   command=com).place(x=x, y=y,
                                      width=35, # ширина клавиш
                                      height=35) # высота клавиш
            x += 36   # расстояние от начала первой кнопки до начала следующей
            if x > 144: # условие отступа при достижении правого поля
                x = 3  # отступ справа ( для нового ряда)
                y += 36  # отступ сверху ( для нового ряда)

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "⌫":
            self.formula = self.formula[0:-1]
        elif operation == "x²":
            self.formula = str((eval(self.formula))**2)
        elif operation == "1/x":
            self.formula = str(eval(1/(self.formula)))
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)




if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#72cced" # Цвет фона
    root.geometry("148x287-50-100") # Размер внешний и место появления программы на мониторе
    root.title("Калькулятор")
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()
