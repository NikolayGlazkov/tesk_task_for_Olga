import math


def read_circle_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        first_line = lines[0].strip()
        
        x_value = float(first_line[0])  # Первое число
        y_value = float(first_line[1])  # Второе число
        r_value = float(lines[1].strip())  # Радиус
        return x_value, y_value, r_value

        
def read_points_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        points = [divmod(int(i.strip()), 10) for i in lines]
        return points


def point_position_relative_to_circle(cx, cy, r, px, py):
    distance = math.sqrt(pow((px - cx), 2) + pow((py - cy), 2))
    
    if math.isclose(distance, r):
        return 0  # Точка лежит на окружности
    elif distance < r:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности


def main(circle_file, points_file):
    cx, cy, r = read_circle_data(circle_file)  # Передача аргументов в переменные из функции

    for point in read_points_data(points_file):
        int1, int2 = point 
        print(point_position_relative_to_circle(cx, cy, r, int1, int2))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 task2.py <circle_file> <points_file>")
    else:
        circle_file = sys.argv[1]
        points_file = sys.argv[2]
        main(circle_file, points_file)
