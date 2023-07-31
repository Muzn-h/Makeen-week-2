#count words compared to the input n
def long_word (word_list , n):
    words=[]
    for word in word_list:
        if len(word)>n:
            words.append(word)
    return words
word_list = input("enter list of words with the spaces").split()
n= int(input ("enter a numberof n:"))
R= long_word (word_list ,n )
print("word long than ", n, "are" ,R)