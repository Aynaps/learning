def createList():
    """
        So in this lesson ill be checking your
        knowledge on lists and iteration

        I would like you to create a list of numbers 
        ranging from 0-9

        then iterate over that list and double the 
        number at num[i]

        return that list from this function
        Example:
        list1 = [1,2,3]
        ..your code runs...
        list1= [2,4,6]
        and then return that value
    """
    #your code goes here beneath this line

#dont edit beneath this line
def main():
    expected = [i*2 for i in range(10)]
    list1 = createList()
    for idx, _ in enumerate(list1):
        if list1[idx] != expected[idx]:
            print(f"FAIL: expected {expected[idx]} \n Actual: {list1[idx]}")
        else:
            print("PASS")

if __name__ == '__main__':
    main()
