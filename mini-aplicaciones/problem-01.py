#!/usr/bin/python3
"""
Practice 01: Palindrome

Statement:
  Create a system that detects if a word is a palindrome or not

Analysis:
  * To solve this problem, the user has to enter a word on the screen and
    the system verifies if it is a palindrome or not.
  * A palindrome word is read the same as right and left.
"""


def palindrome(word):
  word = word.replace(' ', '')
  word = word.lower()
  
  word_reverse = word[::-1]

  if word == word_reverse: 
    return True
  else:
    return False

  

def main():
  word = input("Enter a word: ")
  __palindrome = palindrome(word)

  if __palindrome:
    print("It's palindrome")
  else:
    print("It isn't palindrome")

if __name__ == '__main__':
  main()