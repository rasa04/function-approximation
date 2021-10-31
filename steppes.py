x_all = [5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7, 7.2, 7.4]
y_all = [-3.535, -2.695, -1.676, -0.515, 0.746, 2.056, 3.36, 4.599, 5.714, 6.65]
# for i in range(0, 10):
#     x_all.append(float(input("Введите x ")))
#     y_all.append(float(input("Введите y ")))
print("-----------")
x = float(input("Введите х после чего подсчитается значение функции в этой точке"))
h = round(x_all[1] - x_all[0], 3)
k = 4

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
    if round(x_all[location] + k * h, 3) == x_all[location + k]:
        x_we_need = x_all[location:location + 5]
        y_we_need = y_all[location:location + 5]
        t = round((x - x_we_need[0]) / h, 3)
        q = round((x - x_we_need[-1]) / h, 3)
        print(x_we_need, y_we_need, x_all, y_all, x, h, t, q, k, sep='\n')
except IndexError:
    """
        Если x надо определить через q
    """
    x_we_need = x_all[k+1:-1]
    x_we_need.append(x_all[-1])
    y_we_need = y_all[k+1:-1]
    y_we_need.append(y_all[-1])
    t = round((x - x_we_need[0]) / h, 3)
    q = round((x - x_we_need[-1]) / h, 3)
    print(x_we_need, y_we_need, x_all, y_all, x, h, t, q, k, sep='\n')


"""
    находим конечные разности
"""
kes = [[]]
for i in range(k):
    try:
        kes[0].append(round(y_we_need[i + 1] - y_we_need[i], 3))
    except:
        continue


for j in range(1, k):
    kes.append([])
    for i in range(k - j):
        try:
            kes[j].append(round(kes[j-1][i+1]-kes[j-1][i], 3))
        except:
            continue

for i in kes:
    print(i)
"""
    находим значение функции на данной точке
"""


