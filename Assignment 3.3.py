
# coding: utf-8

# In[4]:


sentence = input("enter the sentence")
words=sentence.split(" ")

def longestWord(words):
    longestLen=0
    longestWord=""
    for x in words:
        if longestLen<len(x):
            longestLen=len(x)
            longestWord=x
    print("the longest word is %s" %(longestWord))

longestWord(words)

