import sys
import math


def read_circle_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Первая строка: строка вида "12", где 1 - x, 2 - y
        first_line = lines[0].strip()
        
        x_value = float(first_line[0])  # Первое число
        y_value = float(first_line[1])  # Второе число
        # Вторая строка: радиус
        r_value = float(lines[1].strip())
        return x_value, y_value, r_value

        
def read_points_data(filename):
    with open(filename, 'r') as file:
        print("testing")
        lines = file.readlines()
        # print(type(lines))
        annswer = [divmod(int(i.strip()), 10) for i in lines]
        return annswer
            # return int1, int2
        

def point_position_relative_to_circle(cx, cy, r, px, py):
    # Вычисляем расстояние от точки до центра окружности
    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    
    # Сравниваем расстояние с радиусом окружности
    if math.isclose(distance, r):
        return 0  # Точка лежит на окружности
    elif distance < r:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

# # # Пример использования
# cx = 1.0
# cy = 1.0
# r = 5.0


cx, cy, r = read_circle_data("file1.txt") # передача аргументов в переменные из функции

# print(point_position_relative_to_circle(cx, cy, r, px, py)) # формула решения
for i in read_points_data("file2.txt"):
            int1, int2 = i 
            print(point_position_relative_to_circle(cx, cy, r, int1, int2))
