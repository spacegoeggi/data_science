import matplotlib.pyplot as plt


def merge_sort(to_sort):
    if len(to_sort) > 1:
        # part the list
        mid = len(to_sort) // 2
        left = to_sort[:mid]
        right = to_sort[mid:]

        # recursive call of merge_sort
        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        i = 0

        # as long as both lists have elements
        while l<len(left) and r<len(right):
            if left[l] <= right[r]:
                to_sort[i] = left[l] 
                l += 1
            else:
                to_sort[i]= right[r]
                r += 1
            i += 1
        # if only the left list has elements
        while l < len(left):
            to_sort[i] = left[l]
            l += 1
            i += 1
        # if only the right list has elements
        while r < len(right):
            to_sort[i] = right[r]
            r += 1
            i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show() # plot of original list
merge_sort(my_list)
plt.plot(x, my_list)
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