from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        k = total_len // 2
        if total_len % 2 == 0:
            return (self.optimal(nums1, nums2, k) + self.optimal(nums1, nums2, k -1)) / 2.0
        else:
            return self.optimal(nums1, nums2, k)

    def naive(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_list = []
        i, j = 0, 0

        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                sorted_list.append(nums2[j])
                j += 1
            elif j == len(nums2):
                sorted_list.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                sorted_list.append(nums1[i])
                i += 1
            else:
                sorted_list.append(nums2[j])
                j += 1

        k = len(sorted_list) // 2
        if len(sorted_list) % 2 == 0:
            return (sorted_list[k] + sorted_list[k - 1]) / 2.0
        else:
            return sorted_list[k]
        

    def optimal(self, nums1: List[int], nums2: List[int], target_k: int) -> float:
        k1 = len(nums1) // 2
        k2 = len(nums2) // 2
        total_len = len(nums1) + len(nums2)

        if len(nums1) == 0:
            return nums2[target_k]
        if len(nums2) == 0:
            return nums1[target_k]

        if nums1[k1] < nums2[k2]:
            # {A_left, B_left, A_right}, B_right
            if target_k <= total_len // 2:
                return self.optimal(nums1, nums2[:k2 + 1], target_k)
            # A_left, {B_left, A_right, B_right}
            else:
                return self.optimal(nums1[k1 + 1:], nums2, target_k)
        else:
            # {A_left, B_left, B_right}, A_right
            if target_k <= total_len // 2:
                return self.optimal(nums1[:k1 + 1], nums2, target_k)
            # B_left, {A_left, A_right, B_right}
            else:
                return self.optimal(nums1, nums2[k2 + 1:], target_k)



sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
# print(sol.findMedianSortedArrays([1, 2], [3, 4]))
# print(sol.findMedianSortedArrays([1, 2, 9, 10], [3, 4, 4, 5, 5, 6]))
