elems=int(input("Number Of Elements In List : \n"))
lst = []
for i in range(elems):
    lst.append(int(input(f"What is the {i+1} element :\n")))
def swap(lst):
    lst
    newlst=lst.copy()
    x=int(input("Position One :\n"))
    y=int(input("Postion Two :\n"))
    newlst[x]=lst[y]
    newlst[y]=lst[x]
    return newlst
newlst=swap(lst)
print(f"Before Swap\n{lst}\nAfter Swap\n{newlst}\n")