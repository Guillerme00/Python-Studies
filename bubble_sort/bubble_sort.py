
# Bubble sort works based on a simple idea:
# if the next item is smaller than the current one, we swap them.
# If it is not smaller, we do not swap and continue comparing
# the next pair of elements.

def bubble(number_list):

    for i in range(len(number_list)):
        for j in range(len(number_list) - 1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    return number_list


# Bubble sort is not a good algorithm for big lists,
# because it becomes very slow

# Bubble sort has a time complexity of O(n²),
# which is inefficient compared to better sorting algorithms.