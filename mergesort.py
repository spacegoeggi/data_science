def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))


plt.bar(x, my_list)
plt.xticks(ticks=range(len(my_list)))
plt.title("list before sorting")
plt.xlabel("position in list")
plt.ylabel("value")
plt.show() # plot of original list
merge_sort(my_list)
plt.bar(x, my_list)
plt.xticks(ticks=range(len(my_list)))
plt.title("list after sorting")
plt.xlabel("position in list")
plt.ylabel("value")
plt.show() # plot of sorted list


# changed ASSIGNMENT to assignment
# gelöscht: and not len(to_sort) < 1
# and len(to_sort) != 0
# changed mergeSort to merge_sort
# changed list_to_be_sorted_by_merch to to_sort    
# def assignment(new_list, i, old_list, j): 
#    new_list[i] = old_list[j]        rausgeschmissen
# x = range(len(my_list)) rausgeschmissen
# while l<len(left) and r<len(right): changed spacing

