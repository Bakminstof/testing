# Сортировка выбором
def selection_sort(my_list):
    for i_min in range(len(my_list)):
        for current_element in range(i_min, len(my_list)):
            if my_list[current_element] < my_list[i_min]:
                my_list[current_element], my_list[i_min] = my_list[i_min], my_list[current_element]