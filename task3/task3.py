class Puzzle:
    def __init__(self, word_list, puzzle_list, size_of_words) :
        self.w = word_list
        self.p = puzzle_list
        self.word_size = size_of_words

    def run(self):
        ordered_word_list = self.order_word_list(self.w)
        puzzle_words = self.list_of_words(self.p)
        #print(puzzle_words)
        ordered_puzzle_words = self.order_word_list(puzzle_words, True)
        #print(ordered_puzzle_words)
        ordered_puzzle_words = self.compare_ordered_words(ordered_word_list, ordered_puzzle_words)
        #print(ordered_puzzle_words)
        puzzle_words = self.reorder_words(self.w, ordered_puzzle_words, self.p)
        #print(puzzle_words)
        
        return puzzle_words

    def reorder_words(self, word_list, puzzle_words, puzzle):
        puzzle_words_verified = []
        for entry in puzzle_words:
            word=""
            y_start, x_start = entry[2]
            y_end, x_end = entry[3]
            if entry[1] == "H":
                word = "".join(puzzle[y_start][x_start:x_end+1])
            elif entry[1] == "V":
                word = "".join(puzzle[i][x_start] for i in range(y_start, y_end+1))
            elif entry[1] == "DR":
                #loop that goes one down and one right in the puzzle
                j, i = y_start, x_start
                while j < y_end+1 and i < x_end+1:
                    word += puzzle[j][i]
                    j+=1
                    i+=1
            elif entry[1] == "DL":
                #loop that goes one down and one left in the puzzle
                j, i = y_start, x_start
                while j < y_end+1 and i > x_end-1:
                    word += puzzle[j][i]
                    j+=1
                    i-=1
            #word found in the puzzle or its reverse is in the word_list
            if word in word_list: 
                puzzle_words_verified.append((word, entry[2], entry[3]))
            elif self.reversed_string(word) in word_list:
                puzzle_words_verified.append((self.reversed_string(word), entry[2], entry[3]))
        return puzzle_words_verified

    def reversed_string(self, string):
        return "".join(string[::-1])


    def compare_ordered_words(self, word_list, puzzle):
        puzzle = [entry for entry in puzzle if entry[0] in word_list]
        return puzzle
    
    def list_of_words(self, puzzle):
        """finds all possible words in a puzzle and puts them in a list
        along with orientation and position of first and last char in the puzzle"""
        puzzle_words_list = []
        # len n works both horizontaly and vertically in the array
        n = len(puzzle)
        
        for y in range(0, n):
            for x in range(0, n):
                #after horizontally
                if x + self.word_size - 1 < n:
                    word = "".join(puzzle[y][x:x+self.word_size])
                    #appending word, direction, coordinates of first and last char
                    puzzle_words_list.append([word, "H", (y, x), (y, x+self.word_size-1)])
                #down vertically
                if y + self.word_size - 1 < n: 
                    word = "".join(puzzle[i][x] for i in range(y, y + self.word_size))
                    puzzle_words_list.append([word, "V", (y, x), (y + self.word_size-1, x)])
                #right diagonally
                if y + self.word_size - 1 < n and x + self.word_size - 1 < n: 
                    word = ""
                    #loop that goes one down and one right in the puzzle
                    j, i = y, x
                    while j < y+self.word_size and i < x+self.word_size:
                        word += puzzle[j][i]
                        j+=1
                        i+=1
                    puzzle_words_list.append([word, "DR", (y, x), (y + self.word_size-1, x + self.word_size-1)])
                #left diagonally
                if y + self.word_size - 1 < n and x - self.word_size + 1 >= 0: 
                    word = ""
                    #loop that goes one down and one left in the puzzle
                    j, i = y, x
                    while j < y+self.word_size and i > x-self.word_size:
                        word += puzzle[j][i]
                        j+=1
                        i-=1
                    puzzle_words_list.append([word, "DL", (y, x), (y + self.word_size-1, x - self.word_size+1)])
        return puzzle_words_list
                    


    def order_word_list(self, word_list, puzzle_words=False):
        #don't change the actual word_list
        word_list_copy = word_list.copy()
        if puzzle_words:
            for i in range(len(word_list_copy)):
                word_list_copy[i][0] = "".join(sorted(word_list_copy[i][0]))
            return word_list_copy
            
        for i in range(len(word_list_copy)):
            word_list_copy[i] = "".join(sorted(word_list_copy[i]))
        return word_list_copy


if __name__ == '__main__' :
    puzzle = [
    ['t', 'h', 'i', 's', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
    ['w', 'o', 'r', 'd', 'p', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    ['r', 'a', 'n', 'd', 'p', 'm', 'l', 'e', 't', 't', 'e', 'r', 's', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd', 'l', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    ['f', 'i', 'v', 'e', 'e', 'o', 'r', 'd', 's', 't', 'o', 'f', 'i', 'n', 'd', 'x', 'y', 'z', 'a', 'b'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
    ['o', 'p', 'q', 'r', 's', 't', 'g', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    ['r', 'a', 'n', 'd', 'o', 'r', 'l', 'e', 't', 't', 'e', 'r', 's', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd', 'a', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    ['f', 'i', 'v', 'p', 'w', 'o', 'r', 'd', 's', 't', 'o', 'f', 'i', 'n', 'd', 'l', 'y', 'z', 'a', 'b'],
    ['a', 'b', 'e', 'd', 'e', 'f', 'p', 'e', 'a', 'c', 'h', 'l', 'm', 'n', 'o', 'p', 'e', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'm', 'n'],
    ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'o', 'h'],
    ['r', 'a', 'n', 'd', 'o', 'm', 'l', 'e', 't', 't', 'e', 'r', 's', 'x', 'y', 'z', 'a', 'b', 'c', 'n'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'o', 'g', 'n', 'a', 'm', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    ['f', 'i', 'v', 'e', 'w', 'o', 'r', 'd', 's', 't', 'o', 'f', 'i', 'n', 'd', 'x', 'y', 'z', 'a', 'b'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
    ['o', 'm', 'n', 'a', 'g', 'o', 'm', 'a', 'n', 'o', 'g', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ]

    # List of words to find
    word_list = ["apple", "grape", "peach", "lemon", "mango"]
    print("Puzzle:")
    for row in puzzle:
        print(" ".join(row))

    print(f"Words to find: {word_list}")

    P = Puzzle(word_list, puzzle, 5)
    print(f"\nWords found(word, (y,x) first char, (y,x) last char:\n{P.run()}")
