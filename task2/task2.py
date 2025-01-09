class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = [None for i in range(size)]
    def hash_code(self, num):
        return num % 10

class ChainingHashTable(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.arr = [[] for i in range(size)]

    def insert(self, num):
        index = self.hash_code(num)
        self.arr[index].append(num)

    def get_index(self, num):
        index = self.hash_code(num)
        index_arr = self.arr[index].index(num)
        return (index, index_arr)


    def __str__(self):
        return "".join(f"{elt}\n" for elt in self.arr).strip("\n")

class LinearProbingHashTable(HashTable):
    def insert(self, num):
        index = self.hash_code(num)
        while self.arr[index] is not None:
            index = (index + 1) % self.size
        self.arr[index] = num
    
    def get_index(self, num):
        index = self.hash_code(num)
        while self.arr[index] != num:
            index = (index + 1) % self.size
        return index

    def __str__(self):
        return "".join(f"{elt}\n" for elt in self.arr).strip("\n")
    
class QuadraticProbingHashTable(HashTable):
    def insert(self, num):
        index = self.hash_code(num)
        pos = index
        counter = 1
        while self.arr[index] is not None:
            index = (pos + counter ** 2) % self.size
            counter += 1
        self.arr[index] = num
    
    def get_index(self, num):
        index = self.hash_code(num)
        pos = index
        counter = 1
        while self.arr[index] != num:
            index = (pos + counter ** 2) % self.size
            counter += 1
        return index

    def __str__(self):
        return "".join(f"{elt}\n" for elt in self.arr).strip("\n")
    

if __name__ == "__main__":
    numbers_arr = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
    for size in range(10, 21, 10):
        print(f"{'-'*50}\nSize of hash table: {size}\n")
        print(f"insert order: {numbers_arr}\n")
        C = ChainingHashTable(size)
        for num in numbers_arr:
            C.insert(num)
        print(f"Chaining Hash Table:\n{C}")
        print(f"index of {numbers_arr[1]}: {C.get_index(numbers_arr[1])}\n")

        L = LinearProbingHashTable(size)
        for num in numbers_arr:
            L.insert(num)
        print(f"Linear Probing Hash Table:\n{L}")
        print(f"index of {numbers_arr[1]}: {L.get_index(numbers_arr[1])}\n")

        Q = QuadraticProbingHashTable(size)
        for num in numbers_arr:
            Q.insert(num)
        print(f"Quadratic Probing Hash Table:\n{Q}")
        print(f"index of {numbers_arr[1]}: {Q.get_index(numbers_arr[1])}\n")


    #notes:
    #hash function output dictates the hash table length
    #-> if the hash func can output 10 but the size of hash table is 5 it doesnt work
