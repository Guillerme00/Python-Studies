#importing
import threading


#Single thread, the program execute tasks sequentially,
# one at time, and for the next task init, the previous must to be completed
def new():
    for _ in range(6):
        print("Single Thread")

t1 = threading.Thread(target=new)

t1.start()
t1.join()
print('Sucess')