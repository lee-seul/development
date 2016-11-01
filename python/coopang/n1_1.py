
arr1 = []
arr2 = []
arr3 = []
def enqueue(order, value):
    if order % 3 == 0:
        arr1.append(value)
    elif order % 3 == 1:
        arr2.append(value)
    elif order % 3 == 2:
        arr3.append(value)
    
def dequeue(order):
    if order % 3 == 0:
        return "[" + "arr1"+"," + arr1.pop(0) + "]"
    elif order % 3 == 1:
        return "[" + "arr2"+"," + arr2.pop(0) + "]"
    elif order % 3 == 2:
        return "[" + "arr3"+"," + arr3.pop(0) + "]"
         
def solution(inputs) :
    for i in range(len(inputs)):
        enqueue(i%3, inputs[i])
        
    result = []
    for i in range(len(inputs)):
        result.append(dequeue(i%3))
        
    return print(result)

solution(["a", "b", "c"])
