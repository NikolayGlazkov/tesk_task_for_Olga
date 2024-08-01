def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return f"Минимальное количество ходов: {moves}"

def read_data(filename):
    with open(filename, 'r') as file:
        # Читаем все строки из файла
        lines = file.readlines()
    
    # Преобразуем каждую строку в целое число и создаем список чисел
    numbers = [int(line.strip()) for line in lines]
    
    return numbers
# nums = [1,10, 2, 9,]
# print(f"Минимальное количество ходов: {min_moves(nums)}")  # Вывод: 2

print(min_moves(read_data("data.txt")))