from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        maxel = arr[0]

        for i in range(len(arr)):
            if arr[i] > maxel:
                maxel = arr[i]
            else:
                arr[i] = maxel
        return arr[::-1]

if __name__ == "__main__":
    soln = Solution()
    test_cases = [
        [17,18,5,4,6,1],
        [1,2,3,4],
        [4,3,2,1]
    ]

    for test in test_cases:
        print(f"{test} -> {soln.replaceElements(test)}")
            