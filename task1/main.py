from task1 import BinaryHeap
from time import time

with open("numbers.txt", "r") as file:
    number_array = [int(line.strip()) for line in file]

def insert_test(n):
    start = time()
    B = BinaryHeap()
    for i in range(n):
        B.insert(number_array[i])
    stop = time()
    return (stop - start, B)
def linear_test(n):
    start = time()
    B = BinaryHeap(number_array[:n])
    B.restore_order()
    stop = time()
    return (stop - start, B)
def delete_min_test(B):
    start = time()
    B.delete_min()
    stop = time()
    return stop - start

i = 10
while i <= 1000000:
    time_insert, heap_insert = insert_test(i)
    time_linear, heap_linear = linear_test(i)
    time_delete_min_insert = delete_min_test(heap_insert)
    time_delete_min_linear = delete_min_test(heap_linear)
    print(f"insert for {i} elts: {time_insert/1000} milliseconds", end=' ----- ')
    print(f"delete_min: {time_delete_min_insert/1000} milliseconds")
    print(f"linear for {i} elts: {time_linear/1000} milliseconds", end=' ----- ')
    print(f"delete_min: {time_delete_min_linear/1000} milliseconds")
    print()
    i*=10



