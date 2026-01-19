import multiprocessing

results = []

def calc_square(numbers):
    global results
    for i in numbers:
        numb = i*i
        print(f"square: {numb}")
        results.append(numb)
        print(f"Final: {results}")


if __name__ == "__main__":
    arr =[2,4,8,16]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()
    p1.join()

    print(f"Final: {results}")