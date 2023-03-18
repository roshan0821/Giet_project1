def process_numbers(numbers_str):
    numbers=[int(num) for num in numbers_str.split(',')]
    idx_5=numbers.index(5)
    idx_8=numbers.index(8)
    case1_sum=sum(numbers[:idx_5]+numbers[:idx_8])
    case2_str=''.join(map(str, numbers[idx_5:idx_8+1:]))
    