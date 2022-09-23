from typing import List

class Permutation:
    def __init__(self, l: List):
        self.__index: int = 0
        self.__counter: int = self.permutation_count(len(l))
        self.__lst: List = [[]] * self.__counter
        self.permute(l, 0, len(l)-1)
        self.__index = -1

    def permute(self, lst: List, beg: int, end: int):
        if beg == end:
            self.__lst[self.__index] = [x for x in lst]
            self.__index += 1
            return
        else:
            for i in range(beg, end + 1):
                lst[beg], lst[i] = lst[i], lst[beg]
                self.permute(lst, beg + 1, end)
                lst[beg], lst[i] = lst[i], lst[beg]

    @staticmethod
    def permutation_count(size: int):
        result = 1
        for i in range(size, 0, -1):
            result *= i
        return result

    def __next__(self):
        self.__index += 1
        if self.__index == self.__counter:
            raise StopIteration
        else:
            return self.__lst[self.__index]

class nextPermutation:
    def __init__(self, l: List):
        self.__innerList = l

    def __iter__(self):
        return Permutation(self.__innerList)

def main():
    lst = [1, 2, 3]
    for elem in nextPermutation(lst):
        print(elem)

if __name__ == "__main__":
    main()
