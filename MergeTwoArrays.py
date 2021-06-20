def merge_lists(lst1, lst2):

    arr1 = lst1 + lst2
    print(arr1)
    arr1.sort()
    print(arr1)

c = [1,3,4,5]
d = [1,3,1,3]
merge_lists(c, d)