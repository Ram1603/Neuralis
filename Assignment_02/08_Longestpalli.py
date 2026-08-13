def longestPalindrome(s):
    longest = ""

    
    for i in range(len(s)):
      
        for j in range(i, len(s)):
            # Extract the slice (substring)
            sub = s[i : j + 1]

            # Check if 'sub' reads the same forward and backward
            if sub == sub[::-1]:
                # If this palindrome is longer than our previous best, save it!
                if len(sub) > len(longest):
                    longest = sub

    return longest