from random import randint as ri
import time

arr = []

for i in range(100):
    arr.append(ri(0, 100))

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr 

sorted_arr = []
times = []

for i in range(10000):
    arr_temp = arr.copy()
    start = time.perf_counter()
    sorted_arr = bubble_sort(arr_temp)
    end = time.perf_counter()
    times.append((end - start) * 1000)

average_time = round(sum(times)/len(times), 5)
print('Среднее время выполнения сортировки пузырьком: ', average_time, ' ms.')
print('Результат: ', sorted_arr)

sorted_arr = []
times = []

for i in range(10000):
    arr_temp = arr.copy()
    start = time.perf_counter()
    sorted_arr = selection_sort(arr_temp)
    end = time.perf_counter()
    times.append((end - start) * 1000)
    
average_time = round(sum(times)/len(times), 5)
print('Среднее время выполнения сортировки выбором: ', average_time, ' ms.')
print('Результат: ', sorted_arr)