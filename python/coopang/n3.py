def is_palindrome(str):
        last = len(str) - 1
        for i in range(len(str)//2):
            if str[i] != str[last-i]:
                return False
        return True


print(is_palindrome("aba"))

print(is_palindrome("b"))
print(is_palindrome("aabaa"))
print(is_palindrome("aaaa"))
print(is_palindrome("abadgd"))
print(is_palindrome("abadfg"))

