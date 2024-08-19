
def select_sort(data):
    n = len(data)
    for i in range(n - 1):
        menor = data[i]
        menor_id = i
        for j in range(i + 1, n):
            if data[j] < menor:
                menor = data[j]
                menor_id = j
        data[i], data[menor_id] = data[menor_id], data[i]


array = [3, 2, 1, 4, 5]
select_sort(array)
print(array) 
