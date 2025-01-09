import math
import random

class BinaryHeap() :
    def __init__(self, arr=None):
        #1-index based array
        #created without array
        try:
            self.heap_arr = [None] + arr
        #created with array
        except Exception:
            self.heap_arr = [None]

    def insert(self, elt):
        self.heap_arr.append(elt)
        self.bubble_up(len(self.heap_arr) - 1)

    def bubble_up(self, index):
        # elt is root
        if index <= 1:
            return
        parent_index = index // 2
        # parent is bigger and elt is not root
        while index > 1 and self.heap_arr[index] < self.heap_arr[parent_index]:
            self.heap_arr[index], self.heap_arr[parent_index] = self.heap_arr[parent_index], self.heap_arr[index]
            index = parent_index
            parent_index = index // 2

    def restore_order(self):
        """apply heapify_down to all elements in the array form the end to the beginnign"""
        n = len(self.heap_arr) - 1
        for i in range(n//2, 0, -1):
            self.heapify_down(i, n)

    def heapify_down(self, index, heap_size):
        left_child = 2 * index
        right_child = 2 * index + 1
        smallest = index
        
        # Compare with left child
        if left_child <= heap_size and self.heap_arr[left_child] < self.heap_arr[smallest]:
            smallest = left_child

        # Compare with right child
        if right_child <= heap_size and self.heap_arr[right_child] < self.heap_arr[smallest]:
            smallest = right_child

        # If a smaller child exists, swap and continue heapifying
        if smallest != index:
            self.heap_arr[index], self.heap_arr[smallest] = self.heap_arr[smallest], self.heap_arr[index]
            self.heapify_down(smallest, heap_size)

    def in_order(self, elt_index=1):
        n = len(self.heap_arr)
        left = 2*elt_index
        right = 2*elt_index+1
        #is leaf
        if left >= n:
            return str(self.heap_arr[elt_index])

        #only left child
        if right >= n:
            return f"{self.in_order(left)} {self.heap_arr[elt_index]}"

        #both childs
        return f"{self.in_order(left)} {self.heap_arr[elt_index]} {self.in_order(right)}"

    def pre_order(self, elt_index=1):
        n = len(self.heap_arr)
        left = 2*elt_index
        right = 2*elt_index+1
        #is leaf
        if left >= n:
            return str(self.heap_arr[elt_index])

        #only left child
        if right >= n:
            return f"{self.heap_arr[elt_index]} {self.pre_order(left)}"

        #both childs
        return f"{self.heap_arr[elt_index]} {self.pre_order(left)} {self.pre_order(right)}"

    def post_order(self, elt_index=1):
        n = len(self.heap_arr)
        left = 2*elt_index
        right = 2*elt_index+1
        #is leaf
        if left >= n:
            return str(self.heap_arr[elt_index])

        #only left child
        if right >= n:
            return f"{self.post_order(left)} {self.heap_arr[elt_index]}"

        #both childs
        return f"{self.post_order(left)} {self.post_order(right)} {self.heap_arr[elt_index]}"

    def level_order(self):
        return ''.join(f"{elt} " for elt in self.heap_arr[1:])

    def delete_min(self):
        #replace root with last elt
        self.heap_arr[1] = self.heap_arr.pop(-1)
        self.heapify_down(1, len(self.heap_arr) - 1)

    def __str__(self):
        if not self.heap_arr or len(self.heap_arr) <= 1:
            return "<empty heap>"
        levels = []
        n = len(self.heap_arr) - 1  # Adjust for the first element being None

        # Calculate the height of the heap
        height = math.floor(math.log2(n)) + 1

        # Build each level of the heap
        for level in range(height):
            start_index = 2**level
            end_index = min(2**(level + 1), n + 1)
            levels.append(self.heap_arr[start_index:end_index])

        # Find the max width for centering
        max_width = len(" ".join(map(str, levels[-1])))

        # Construct the string with centered levels
        result = []
        for i, level in enumerate(levels):
            level_str = " ".join(map(str, level))
            padding = (max_width - len(level_str)) // 2
            result.append(" " * padding + level_str)

        return "\n".join(result)

if __name__ == "__main__":
    insertion = [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]
    A = BinaryHeap()
    for elt in insertion:
        A.insert(elt)
    
    B = BinaryHeap(insertion)
    B.restore_order()

    print("Tree A:")
    print(A)
    print()
    print(f"in order: {A.in_order()}")
    print(f"pre order: {A.pre_order()}")
    print(f"post order: {A.post_order()}")
    print(f"level order: {A.level_order()}")

    print("\nTree B:")
    print(B, "\n")
    print(f"in order: {B.in_order()}")
    print(f"pre order: {B.pre_order()}")
    print(f"post order: {B.post_order()}")
    print(f"level order: {B.level_order()}")

    print("\nTree A after delete min 2 time:")
    A.delete_min()
    A.delete_min()
    print(A)

    print("\nTree B after delete min 2 time:")
    A.delete_min()
    B.delete_min()
    print(B)
