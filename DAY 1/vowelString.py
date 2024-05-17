
# Write a Python program to count the number of vowels in a string.

word = input("enter a word ")
vowel =['a','e','i','o','u']
count=0
for i in word:
     if i.lower() in vowel:
         count+=1
print(count)


