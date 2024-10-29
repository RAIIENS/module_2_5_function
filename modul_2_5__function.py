# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
def get_matrix(n, m, value):
    # Создаем список
    matrix = []
    # Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
    # В первом цикле добавляйте пустой список в список matrix.
    for i in range(n):
        # [] добавляем пустой список
        row = []
        # Напишите второй(внутренний) цикл for для кол - ва столбцов матрицы, m повторов.
        # Во втором цикле пополняйте ранее добавленный пустой cписок значениями value.
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix


result_1 = get_matrix(2, 2, 3)
print(result_1)
result_2 = get_matrix(3, 4, 5)
print(result_2)
result_3 = get_matrix(3, 2, 8)
print(result_3)
result_4 = get_matrix(4, 3, 9)
print(result_4)
