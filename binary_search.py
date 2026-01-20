numb_list = []

for i in range(0,101):
    numb_list.append(i)

def find_number(numb_list, numb):
    low = 0
    high = len(numb_list) - 1
    mid = low + (high-low)//2
    
    while low <= high:
        if numb < high/2:
            print("Low")
        
        elif numb > high/2:
            print("High")


find_number(numb_list, 5)