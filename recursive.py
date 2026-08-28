def max(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = max(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max


def max1(lst):
    result = lst[0]
    for x in lst[1:]:
        if x > result:
            result = x
    return result


numbers1 = [3, 1, 4, 1, 5, 9, 2, 6]
numbers2 = [3]
#print(max(numbers))   # 9
print(max(numbers1))  # 9
#print(max(numbers2))  # 3


