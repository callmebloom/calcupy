import math
while True:
    try:
        op = int (input("Выберите операцию :)\n " 
                             "1: Найти сумму чисел\n "  
                             "2: Найти разность чисел\n " 
                             "3: Найти произведение\n " 
                             "4: Найти частное от деления\n " 
                             "5: Возвести число в степень\n " 
                             "6: Извлечь квадратный корень из числа\n " 
                             "7: Найти факториал от числа\n " 
                             "8: Найти синус\n " 
                             "9: Найти косинус\n " 
                             "10: Найти тангенс\n " 
                             "0: Выйти из программы."))  
    except ValueError:
                print(':(')
                continue
    if op == 1:
            try:
                a = float(input('Введите 1 число: '))
                b = float(input('Введите 2 число: '))
            except ValueError:
                print(':(')
            else:
                print('Ответ: ', a + b)
            continue
    if op == 2:
            try:
                a = float(input('Введите 1 число: '))
                b = float(input('Введите 2 число: '))
            except ValueError:
                print(':(')
            else:
                print('Ответ: ', a - b)
            continue
    if op == 3:
            try:
                a = float(input('Введите 1 число: '))
                b = float(input('Введите 2 число: '))
            except ValueError:
                print(':(')
            else:
                print('Ответ: ', a * b)
            continue
    if op == 4:
            try:
                a = float(input('Введите 1 число: '))
                b = float(input('Введите 2 число: '))
            except ValueError:
                print(':(')
            else:
                if (b != 0):
                    print('Ответ: ', a/b)
                else:
                    print('На 0 делить нелья!')
            continue
    if op == 5:
            try:
                a = float(input('Введите 1 число: '))
                b = float(input('Введите 2 число: '))
            except ValueError:
                print(':(')
            else:
                print('Ответ: ', a ** b)
            continue
    if op == 6:
            try:
                 a = float(input('Введите число: '))
                 if a > 0:
                      print(math.sqrt(a)) 
                 else:
                      print('Введите число больше 0, пж')
            except ValueError:
                print(':(')
            continue
    if op == 7:
        try:
                a = int(input('Введите число: '))
                if a > 0:
                    print(math.factorial(a))
                else: 
                     print('Введите число больше 0, пж')
        except ValueError:
                print(':(')
        continue
    if op == 8:
        try:
            a = int(input('Введите число: '))
            print(math.sin(a))
        except ValueError:
                print(':(')
    if op == 9:
        try:
            a = int(input('Введите число: '))
            print(math.cos(a))
        except ValueError:
            print(':(')
    if op == 10:
        try:
            a = int(input('Введите число: '))
            print(math.tan(a))
        except ValueError:
            print(':(')
    if op == 0:
        break
