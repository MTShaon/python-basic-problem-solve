# Write a Python program to hash a word.
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]

word = input("enter the word : ")

word =word.upper()

coded = word[0]
for a in word[1:len(word)]:
    i=65-ord(a)
    coded = coded+str(soundex[i])

print("\n the coded word is : ",coded)
