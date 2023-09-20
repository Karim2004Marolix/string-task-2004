#8.Write a python program to Remove Repeated Character from String.
def remove_duplicate(s):
    string=set(s)
    string="".join(string)
    dup=""
    for i in s:
        if(i in dup):
            pass
        else:
            dup=dup+i
    print("After removing: ",dup)
    
s="stdsrdthw"
print(s)
print(remove_duplicate(s))