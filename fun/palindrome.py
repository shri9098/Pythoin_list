# def Ispalindrome(word):
#     x = ""
#     for i in word:
#         x = x + i
#         if w == x:
#             print("Yes")
#
#
# w = "malayalam"
# print(Ispalindrome(w))

# class Palindrome:
#     word = 'malayalam'
#
#     @staticmethod
#     def is_palindrome(word):
#         rev = word[::-1]
#         if rev == word:
#             print("yes")
#         else:
#             print("No")
#
#
# word = "malayalam"
# Palindrome.is_palindrome(word)


class Palindrome:
    @staticmethod
    def is_palindrome(word):
        # Please write your code here.
        rev = word[::-1]
        if rev == word:
            print("yes")
        else:
            print("No")


word = input()
print(Palindrome.is_palindrome(word))




