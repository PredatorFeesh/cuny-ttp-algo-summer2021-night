class Solution:
    def reverse(self, x: int) -> int:
        return int( str( abs(x) )[::-1] )



if __name__ == "__main__":
    soln = Solution()

    test_cases = [
        123,
        -123,
        120,
        1200,
        -320
    ]

    for test in test_cases:
        print(f"{test} -> {soln.reverse(test)}")