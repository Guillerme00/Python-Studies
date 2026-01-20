numb_list = []

for i in range(0,100000):
    numb_list.append(i)

def find_number(numb_list, numb, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if numb_list[mid] == numb:
            print("Ok")
            return mid

        elif numb_list[mid] > numb:
            high = mid -1
        
        elif numb_list[mid] < numb:
            low = mid + 1


print(find_number(numb_list, 32585, 0, (len(numb_list)-1)))