# coding: utf-8

from threading import Thread

def work(start, end, result):
    total = 0
    for i in range(start, end):
        total += 1
    result.append(total)
    return


if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=work, args=(START, END, result))
    th1.start()
    th1.join()

print(f"Result: {sum(result)}")

