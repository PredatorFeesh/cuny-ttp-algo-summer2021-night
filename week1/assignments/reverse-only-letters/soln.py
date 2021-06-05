class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s)-1
        
        # If left and right are letters, we swap.
        # If left is not letter, move one  right
        # If right is not letter, move left
        newstr = list(s)
        
        while i <= j:
            print(newstr[i], newstr[j])
            if newstr[i].isalpha() and newstr[j].isalpha():
                newstr[i], newstr[j] = newstr[j], newstr[i]
                i += 1
                j -= 1
            elif not newstr[i].isalpha():
                i += 1
            elif not newstr[j].isalpha():
                j -= 1
        
        return ''.join(newstr)
                

if __name__ == "__main__":
    soln = Solution();

    test_cases = [
        'af-as-fsa-f-asf',
        'abcdefg',
        's+asd-_asd+;asd',
    ]

    for test in test_cases:
        print(f"{test} -> {soln.reverseOnlyLetters(test)}")

