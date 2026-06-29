def is_palindrome(s):
    left = 0
    right = len(s) -1
    while left < right:
        #skip invalid character from left
        if not s[left].isalnum():
            left+=1
            continue
        #skip invalid character from right
        if not s[right].isalnum():
            right-=1
            continue
        # if both word not match then return false 
        if s[left].lower() != s[right].lower():
            return False
        left +=1
        right -=1

        
    return True

s = "A man, a plan, a cana++++l: Panama"

print(is_palindrome(s))