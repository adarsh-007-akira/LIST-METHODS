elems=int(input("Number Of Elements In List : \n"))
lst = []
for i in range(elems):
    lst.append((input(f"What is the {i+1} element :\n")))
def deleteOccur(lst, ocuurance_allowed):
    lst
    count=0
    word=input("Operation to be performed on : \n")
    n=ocuurance_allowed
    newlst=[]
    for i in lst:
        if i==word:
            count+=1
            if count!=n:
                newlst.append(i)
        else:
            newlst.append(i)
    return newlst
newlst=deleteOccur(lst, 1)
print(f"Before Operation :\n{lst}\nAfter Operation\n{newlst}\n")