def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            current_value = list1[i]
            i += 1
        elif list1[i] > list2[j]:
            current_value = list2[j]
            j += 1
        else:
            current_value = list1[i]
            i += 1
            j += 1

        if not merged_list or merged_list[-1] != current_value:
            merged_list.append(current_value)

    while i < len(list1):
        if not merged_list or merged_list[-1] != list1[i]:
            merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        if not merged_list or merged_list[-1] != list2[j]:
            merged_list.append(list2[j])
        j += 1

    return merged_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)

print(merged)
