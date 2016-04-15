# coding: utf-8
# oneeditor.py

def one_editor_apart(string1, string2):
    short = (len(string1)>=len(string2)) if len(string2) else len(string1)
    longer = (len(string2)>len(string1)) if len(string1) else len(string2)
    count = 0
    if(longer-short>1):
        return false
    else:
        string1 = list(string1)
        string2 = list(string2)
        string1.sort()
        string2.sort()
        for i in range(short):
            if(string1[i]==string2[i]):
                count+=1
        return short==count




print(one_editor_apart("cat", "at"))
print(one_editor_apart("ata", "at"))
        


