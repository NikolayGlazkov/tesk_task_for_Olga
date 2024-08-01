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

print(min_moves(read_data("data.txt")))