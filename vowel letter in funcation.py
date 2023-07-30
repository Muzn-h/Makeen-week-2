#vowel letter in funcations

str = "Hello "

print(str)

v= "aieou"
def vowel(s):
    count = 0
    for i in s:
        if (i in v):
            count += 1
    return count
print(vowel(str))

