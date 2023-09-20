#2.Write a program to check String is Palindrome or not.

Palindrome_word = input("enter word: ")
ans_p = Palindrome_word[::-1]
if Palindrome_word == ans_p:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
 
