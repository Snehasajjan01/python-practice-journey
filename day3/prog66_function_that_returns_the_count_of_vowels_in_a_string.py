#Write a python program to define a function that counts vowels in a string
def count_vowels(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'i' or s[i] == 'u':
            count += 1
    return count
s = input('Enter a String:')

count = count_vowels(s)
print('Count of vowels in {} are:{}'.format(s,count))

    