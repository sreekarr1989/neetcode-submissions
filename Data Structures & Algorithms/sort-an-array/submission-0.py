class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            # Base case
            if len(arr) <= 1:
                return arr

            # Split the array into two halves
            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # Merge the sorted halves
            return merge(left, right)

        def merge(left, right):
            result = []

            i = 0
            j = 0

            # Compare elements from both arrays
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Add remaining elements
            result.extend(left[i:])
            result.extend(right[j:])

            return result

        return merge_sort(nums)
