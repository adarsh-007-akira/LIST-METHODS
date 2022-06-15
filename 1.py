elems=int(input("Number Of Elements In List : \n"))
lst = []
for i in range(elems):
    lst.append(int(input(f"What is the {i+1} element :\n")))
last=len(lst)-1
first=0
newlst=lst.copy()
newlst[first]=lst[last]
newlst[last]=lst[first]
print(f"Before Interchange\n{lst}\nAfter Interchange\n{newlst}")