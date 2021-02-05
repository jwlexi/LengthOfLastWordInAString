#given a string s, return the length of the last word
# s = "The daily byte" return 4 (because byte is four characters long)

def LengthOfLastWord(s):
    x = s.strip()
    if " " not in x:
        return len(x);
    for i in range (len(x)):
        if x[i] == " ":
            j = x[i + 1:]
    return len(j)
    
#o(n)

print(LengthOfLastWord("the daily byte"))
print(LengthOfLastWord("aardvark"))