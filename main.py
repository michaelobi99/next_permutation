from permute import nextPermutation
from permute import List

def main():
    myList: List = [1,2,3,4,5,6,7,8,9,10]
    for lst in nextPermutation(myList):
        print(lst)

main()