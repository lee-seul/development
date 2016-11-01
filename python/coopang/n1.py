def solution(inputs):
    arr1 = []
    arr2 = []
    arr3 = []
    for i in range(len(inputs)):
        if i % 3 == 0:
            arr1.append(inputs[i])
        elif i % 3 == 1:
            arr2.append(inputs[i])
        elif i % 3 == 2:
            arr3.append(inputs[i])
        
    result = []
    for i in range(len(inputs)):
        if i % 3 == 0:
            result.append(["arr1", arr1.pop(0)])
        elif i % 3 == 1:
            result.append(["arr2", arr2.pop(0)])
        elif i % 3 == 2:
            result.append(["arr3", arr3.pop(0)])
        
    return print(result)

solution(["a", "b", "c", "d", "e", "f", "g", "h"])


