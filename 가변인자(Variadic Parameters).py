def sum_numbers(n1, n2):
    # n1, n2 : int
    result = n1 + n2
    return result

def sum_all(*args):
    # *args : list
    result = 0
    for i in args:
        result += i
    print('type of *args : ', type(args))
    return result

def sum_all_with_name(**kwargs):
    # **kwargs : dictionary
    result = 0
    names = []

    for k, v in kwargs.items():
        names.append(k)
        result+=v
    print('type of **kwargs : ', type(kwargs))
    return result, names

def sum_all_both(*args, **kwargs):
    # *args : list
    # **kwargs : dictionary
    result = 0
    names = []

    for i in args:
        result += i

    for k, v in kwargs.items():
        names.append(k)
        result += v

    return result, names

if __name__ == '__main__':
    numbers = [1,2,3,4]
    print(sum_numbers(numbers[0], numbers[1]))
    print(sum_all(numbers[0], numbers[1], numbers[2], numbers[3]))
    print(sum_all_with_name(one=numbers[0], two=numbers[1], three=numbers[2], four=numbers[3]))
    print(sum_all_both(numbers[0], numbers[1], three=numbers[2], four=numbers[3]))