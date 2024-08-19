
def insertionSort(data):
    n = len(data)
    
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        
        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1
        
        data[i + 1] = tmp

array = [5, 3, 4, 1, 2]
insertionSort(array)
print(array)