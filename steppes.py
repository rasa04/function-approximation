"""

        Универсальная программа для подсчитывания интерполяционных полиномов ньютона

"""
from math import sin, log, exp

ques = input('Использовать функцию синуса (sin) или ввести новую (new) ? - ')
if ques == 'sin':
    x_all = [5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7, 7.2, 7.4]  # типо находит значения только между этими числами
    y_all = [-3.535, -2.695, -1.676, -0.515, 0.746, 2.056, 3.36, 4.599, 5.714, 6.65]
elif ques == 'ln':
    x_all = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # типо находит значения только между этими числами
    y_all = [0.693147, 1.09861, 1.38629, 1.60944, 1.79176, 1.94591, 2.07944, 2.19722, 2.30259, 2.3979]
elif ques == 'new':
    ques = input('назовите функцию - ')
    x_all = []
    y_all = []
    for i in range(0, 10):
        x_all.append(float(input("Введите x ")))  # типо находит значения только между этими числами
        y_all.append(float(input("Введите y ")))
print("-----------")
x = float(input("Введите х после чего подсчитается значение функции в этой точке: "))
h = round(x_all[1] - x_all[0], 4)

""" 

    Определьяем k
    
"""
k = 0
if x_all[1] - x_all[0] < 1:
    while not (x_all[1] - x_all[0]) ** (k + 1) < 0.0005:
        k += 1
elif x_all[1] - x_all[0] == 1:
    k = 3

else:
    while not (x_all[1] - x_all[0]) ** (k + 1) < 0.0005:
        k -= 1
    k = abs(k)
"""

 Считываем конечные разности
 
"""
global location  # перед каким x-n стоит наша точка x
for i in range(0, 9):
    if x_all[i] < x < x_all[i + 1]:
        location = i

try:
    """
        Если x можно определить через t
    """
    if round(x_all[location] + k * h, 4) == x_all[location + k]:
        x_we_need = x_all[location:location + 5]
        y_we_need = y_all[location:location + 5]
        t = round((x - x_we_need[0]) / h, 4)
        q = round((x - x_we_need[-1]) / h, 4)
        print(x_we_need, y_we_need, x_all, y_all, x, h, t, q, k, sep='\n')
        mean = 't'
except IndexError:
    """
        Если x надо определить через q
    """
    x_we_need = x_all[k + 1:-1]
    x_we_need.append(x_all[-1])
    y_we_need = y_all[k + 1:-1]
    y_we_need.append(y_all[-1])
    t = round((x - x_we_need[0]) / h, 4)
    q = round((x - x_we_need[-1]) / h, 4)
    mean = 'q'
    print(x_we_need, y_we_need, x_all, y_all, x, h, t, q, k, sep='\n')

"""

    находим конечные разности
    
"""
kes = [[]]
for i in range(k):
    try:
        kes[0].append(round(y_we_need[i + 1] - y_we_need[i], 4))
    except:
        continue

for j in range(1, k):
    kes.append([])
    for i in range(k - j):
        try:
            kes[j].append(round(kes[j - 1][i + 1] - kes[j - 1][i], 4))
        except:
            continue

for i in kes:
    print(i)
"""

    находим значение функции на данной точке
    
"""


def factorial(f):  # Факториал
    fac = 1
    for j in range(f):
        fac *= j + 1
        return fac


if mean == 't':  # Для 1го интерпольяционного полинома ньютона
    equal = y_we_need[0]
    for i in range(k):
        tes = 1
        for j in range(i + 1):
            tes *= t - j
        equal += tes * kes[i][0] / factorial(i + 1)

elif mean == 'q':  # Для 2го интерпольяционного полинома ньютона
    equal = y_we_need[-1]
    for i in range(k):
        qes = 1
        for j in range(i + 1):
            qes *= q + j
        equal += qes * kes[i][-1] / factorial(i + 1)

"""
        Подсчитываем погрешность
"""
if ques == 'sin':
    error = abs(x * sin(x) - equal)
    true_value = x * sin(x)
elif ques == 'ln':
    e = exp(1)
    error = abs(log(x, e) - equal)
    true_value = log(x, e)
else:
    error = 'undefined'
    true_value = 'undefined'

print(f' {ques}({x}) = ', true_value, '\n', f'f({x}) = ', equal, '\n', 'Погрешность: ', error)
