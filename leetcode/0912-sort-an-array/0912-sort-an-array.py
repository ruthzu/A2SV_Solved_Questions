class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half, right_half):
            arr = []
            i, j = 0, 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr.append(left_half[i])
                    i += 1
                else:
                    arr.append(right_half[j])
                    j += 1

            arr.extend(left_half[i:])
            arr.extend(right_half[j:])
            return arr

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]

            mid = (left + right) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)

        return mergeSort(0, len(nums) - 1, nums)