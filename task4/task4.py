import sys

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return f"Минимальное количество ходов: {moves}"

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    numbers = [int(line.strip()) for line in lines]
    return numbers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python3 task4.py <имя файла>")
    else:
        filename = sys.argv[1]
        try:
            nums = read_data(filename)
            print(min_moves(nums))
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
