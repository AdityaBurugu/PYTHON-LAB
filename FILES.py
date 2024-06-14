#Write a program to print each line of a file in reverse order
file_data=[]
with open("demo.txt","r") as f:
    file_data.extend(f.read().split("\n"))
f.close()
for line in file_data:
    print(line[::-1].rstrip()) #rstrip removes whitespaces before and after a text

#Write a program to compute the number of characters, words and lines in a file.
file_data=[]
char_count=0
word_count = 0
with open("demo.txt","r") as f:
    file_data.extend(f.read().split("\n"))
f.close()
for line in file_data:
    words=line.split()
    word_count+=len(words)
    for chars in words:
        char_count+=len(chars)
print(f"Lines:{len(file_data)},Words:{word_count},Characters:{char_count}")

#Write a program to count frequency of characters in a given file.
file_data=[]
freq_counter={}
string = ""
with open("demo.txt","r") as f:
    file_data.extend(f.read().split("\n"))
f.close()
for line in file_data:
    words = line.split()
    for word in words:
        string += word
for char in string:
    if char not in freq_counter:
        freq_counter[char] = string.count(char)
print(freq_counter)
