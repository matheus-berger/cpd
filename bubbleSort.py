
def bubbleSort(data):
    n = len(data)
    temp = int()

    for j in range(n):
        for i in range(0, n-1):
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
    return data


listReverse = [5, 4, 3, 2, 1]
listSorted = [1, 2, 3, 4, 5]
listAleatory = [2, 7, 1, 9, 8]
listRepeated = [9, 8, 9, 2, 2]

print("\n::: BUBBLE SORT :::\n")

print(f"> Reverse ordered list: \nAfter {listReverse}")
bubbleSort(listReverse)
print(f"Before {listReverse}\n")

print(f"> Ordered list: \nAfter {listSorted}")
bubbleSort(listSorted)
print(f"Before {listSorted}\n")

print(f"> List with repeated data: \nAfter {listRepeated}")
bubbleSort(listRepeated)
print(f"Before {listRepeated}\n")

print(f"> List with random data: \nAfter {listAleatory}")
bubbleSort(listAleatory)
print(f"Before {listAleatory}\n")
