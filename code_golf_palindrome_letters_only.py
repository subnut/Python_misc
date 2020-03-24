## Source: https://stringlabs.io/codegolf/challenge/palindromicallyspeaking

''' Write a function called hannah that takes in a string and returns
    whether or not the letters (and only the letters) in that sentence are a palindrome (case insensitive).
    Your function should return a boolean.  '''

## Best submission: 70 bytes
## My answer: 68 bytes 

def hannah(s):
	l=[x for x in s if x.isalpha()]
	return l==l[::-1]