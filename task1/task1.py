import argparse

def cercle_aray(n, m):
    i = 1
    while True:
        print(i, end=' ')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Печать последовательности чисел в цикле с заданным шагом.")
    parser.add_argument('n', type=int, help='Количество элементов в последовательности.')
    parser.add_argument('m', type=int, help='Шаг для перехода к следующему элементу.')
    
    args = parser.parse_args()
    
    cercle_aray(args.n, args.m)
