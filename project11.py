import tkinter as tk #Импорт модуля tkinter

def convert_temperature(): #Определение функции convert_temperature()
    try:
        input_value = float(entry_input.get())
        from_unit = var_from.get()
        to_unit = var_to.get()

        if from_unit == to_unit: #Условие проверки, что исходная и целевая единицы измерения одинаковы.
            result = input_value #Если условие истинно, результат равен введенному значению.
        elif from_unit == "Цельсий": #Условие проверки, что исходная температура указана в градусах Цельсия.
            if to_unit == "Фаренгейт": #Условие проверки, что целевая температура указана в градусах Фаренгейта.
                result = (input_value * 9/5) + 32 #Формула для перевода градусов Цельсия в градусы Фаренгейта.
            elif to_unit == "Кельвин":
                result = input_value + 273.15
        elif from_unit == "Фаренгейт":
            if to_unit == "Цельсий":
                result = (input_value - 32) * 5/9
            elif to_unit == "Кельвин":
                result = (input_value - 32) * 5/9 + 273.15
        elif from_unit == "Кельвин":
            if to_unit == "Цельсий":
                result = input_value - 273.15
            elif to_unit == "Фаренгейт":
                result = (input_value - 273.15) * 9/5 + 32

        label_result.config(text=f"{result:.2f} {to_unit}") #Настройка текстового поля label_result для отображения результата преобразования.
    except ValueError: #Проверка на нечисловое значение
        label_result.config(text="Ошибка: введите число")

def button_click(number): #Определение функции, которая добавляет нажатый номер кнопки к текущему значению ввода.
    current = entry_input.get() #Получение текущего значения из поля ввода.
    entry_input.delete(0, tk.END) #Очистка поля ввода.
    entry_input.insert(0, current + str(number)) #Добавление нажатого числа к текущему значению ввода.

def clear_display(): #Определение функции, которая очищает поле ввода.
    entry_input.delete(0, tk.END)

root = tk.Tk() #Создание основного окна приложения.
root.title("Конвертер температур и калькулятор") #Задание заголовка окна приложения.

var_from = tk.StringVar(value="Цельсий")
var_to = tk.StringVar(value="Фаренгейт")

# Блок для конвертора температур
label_input = tk.Label(root, text="Введите температуру:") #Создание метки для инструкции ввода температуры.
entry_input = tk.Entry(root) #Создание поля для ввода температуры.
label_from = tk.Label(root, text="Из:") #Создание метки для указания исходной единицы измерения.
option_from = tk.OptionMenu(root, var_from, "Цельсий", "Фаренгейт", "Кельвин") #оздание выпадающего списка для выбора исходной единицы измерения.
label_to = tk.Label(root, text="В:") #Создание метки для указания целевой единицы измерения.
option_to = tk.OptionMenu(root, var_to, "Цельсий", "Фаренгейт", "Кельвин") #Создание выпадающего списка для выбора целевой единицы измерения.
button_convert = tk.Button(root, text="Конвертировать", command=convert_temperature) #Создание кнопки для запуска процесса конвертации.
label_result = tk.Label(root, text="") #Создание метки для отображения результата конвертации.

# Блок для калькулятора
button_7 = tk.Button(root, text="7", command=lambda: button_click(7)) #Создание кнопок для ввода чисел с помощью клавиатуры.
button_8 = tk.Button(root, text="8", command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", command=lambda: button_click(9))
button_4 = tk.Button(root, text="4", command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", command=lambda: button_click(6))
button_1 = tk.Button(root, text="1", command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", command=lambda: button_click(3))
button_0 = tk.Button(root, text="0", command=lambda: button_click(0))
button_clear = tk.Button(root, text="C", command=clear_display) #Создание кнопки для очистки поля ввода.

# Расположение элементов на сетке с заданными параметрами отступов.
label_input.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
entry_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
label_from.grid(row=2, column=0, padx=5, pady=5)
option_from.grid(row=2, column=1, padx=5, pady=5)
label_to.grid(row=3, column=0, padx=5, pady=5)
option_to.grid(row=3, column=1, padx=5, pady=5)
button_convert.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
label_result.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

button_7.grid(row=6, column=0, padx=5, pady=5)
button_8.grid(row=6, column=1, padx=5, pady=5)
button_9.grid(row=6, column=2, padx=5, pady=5)
button_4.grid(row=7, column=0, padx=5, pady=5)
button_5.grid(row=7, column=1, padx=5, pady=5)
button_6.grid(row=7, column=2, padx=5, pady=5)
button_1.grid(row=8, column=0, padx=5, pady=5)
button_2.grid(row=8, column=1, padx=5, pady=5)
button_3.grid(row=8, column=2, padx=5, pady=5)
button_0.grid(row=9, column=0, padx=5, pady=5)
button_clear.grid(row=9, column=1, padx=5, pady=5)

root.mainloop() #Запуск главного цикла обработки событий Tkinter
