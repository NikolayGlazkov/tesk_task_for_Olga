import argparse

def cercle_aray(n, m):
    i = 1
    
    answer = []
    while True:
        # print(i, end=' ')
        answer.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    # print()
    return f'Полученный путь: {"".join(map(str,answer))}'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Печать последовательности чисел в цикле с заданным шагом.")
    parser.add_argument('n', type=int, help='Количество элементов в последовательности.')
    parser.add_argument('m', type=int, help='Шаг для перехода к следующему элементу.')
    
    args = parser.parse_args()
    
    print(cercle_aray(args.n, args.m))


