def twoSum(nums: list[int], target: int):
    """
        Given a list of numbers called nums and a target value k
        return true or false whether there are two numbers
        in nums that can be added together and equal k
        Example:
        nums = [1,2,3]
        k = 5
        output -> True

        The function returns true because 
        nums[1] + nums[2] = 5

        2nd Example:
        nums = [1,2,3]
        k = 10
        output -> False
        The function will return false because
        there is no combination of any two numbers
        which will add up to target value 10
    """
    #your code goes here beneath this line

#dont edit beneath this line
def main():
    #[0,1,2,3,4,5,6,7,8,9]
    nums = [i for i in range(10)]

    result = twoSum(nums, 9)
    assert result == True
    result = twoSum(nums, 17)
    assert result == True
    result = twoSum(nums, -3)
    assert result == False
    result = twoSum(nums, 1000)
    assert result == False
    result = twoSum(nums, 6)
    assert result == True


if __name__ == '__main__':
    main()
