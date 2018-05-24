def word_count(str):
    if(not str.startswith("\"") and not str.endswith("\"")):
        return True

    str=str.replace("\"","")
    words = str.split()
    excludedletters="\t\n-,:.1234567890"
    return(sum(w not in excludedletters for w in words))

str=input("Enter string: ")
print(word_count(str))