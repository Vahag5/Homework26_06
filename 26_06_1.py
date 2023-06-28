def sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

def merge(ls1, ls2):
    ls3 = ls1+ls2
    sorted_list = sort(ls3)
    return sorted_list

lst1 = [4,5,6]
lst2 = [446, 15, 856]
print(merge(lst1, lst2))









