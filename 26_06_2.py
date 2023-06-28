def sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
def deepcopy(ls):
    qanak = len(ls)
    ls2 = []
    for i in range(qanak): 
        if type(ls[i]) == list:
            ls2.append(ls[i].copy())     
            for j in range(len(ls[i])):
                if type(ls[i][j]) == list:
                    ls2[i][j] = ls[i][j].copy()
        else:
            ls2.append(ls[i])
    
    return ls2
def is_sorted(list1) :
    list2 = deepcopy(list1)
    sorted_list = sort(list1)
    if sorted_list == list2 :
        return True 
    else: 
        return False


ls1 = [1,2,3,4,5]   # True
print(is_sorted(ls1))
 
ls2 = [1,2,3,8,5]   # False
print(is_sorted(ls2))






