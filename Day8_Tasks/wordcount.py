"""5. Word Counter Program A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results."""

f=open("Article.txt","r")
print(f.read(),'\n')

f=open("Article.txt","r")
count=f.read()
word=count.split()
total_words=len(word)
print("Words count is",total_words)
f.close()

line=0
f=open("Article.txt","r")
for li in f:
    line+=1
print("Line count is",line)
f.close()

f=open("Article.txt","r")
char=f.read()
total_char=len(char)
print("Character count is",total_char)
f.close()
