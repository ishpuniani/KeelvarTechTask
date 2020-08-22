class Solution:

    @classmethod
    def check_array_sort(cls, arr):
        '''
        Uses the two pointer approach to check
        Time Complexity = O(n^2)
        Space Complexity = O(1)

        :param arr: Array to be checked
        :return: True if array does NOT contain sum of some pairs. Else false
        '''
        arr.sort()
        for num in arr:
            res = cls.find_sum_using_pointers(arr, num)
            if res:
                return False
        return True

    @classmethod
    def check_array_set(cls, arr):
        '''
        Uses the set approach to check
        Time Complexity = O(n^2)
        Space Complexity = O(n)

        :param arr: Array to be checked
        :return: True if array does NOT contain sum of some pairs. Else false
        '''
        for num in arr:
            res = cls.find_sum_using_set(arr, num)
            if res:
                return False
        return True

    @classmethod
    def find_sum_using_set(cls, arr, target):
        '''
        Function to find sum using set implementation
        1. Create a new set
        2. Iterate over the array
        3. Check if target - element exists in the array
        4. Add element to array
        :param arr: Array to check
        :param target: The sum to find
        :return: True if sum is found, false if not.
        '''
        num_set = set()
        for n in arr:
            n2 = target - n
            if n2 in num_set:
                return True
            num_set.add(n)
        return False

    @classmethod
    def find_sum_using_pointers(cls, arr, target):
        '''
        Function to find sum in array using the two-pointer approach
        :param arr: Array to be checked
        :param target: sum to find
        :return: True if sum is found, false if not.
        '''
        start = 0
        end = len(arr) - 1
        while start < end:
            temp_sum = arr[start] + arr[end]
            if temp_sum == target:
                return True
            elif temp_sum < target:
                start += 1
            else:
                end -= 1
        return False
