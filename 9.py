
elems=int(input("Number Of Elements In List : \n"))
lst = []
for i in range(elems):
    lst.append((int(input(f"What is the {i+1} element :\n"))))

def repeatNum(lst, elem):
    newlst=lst
    element=elem
    count=0
    for i in newlst:
        if element==i:
            count+=1
    print(count)

repeatNum(lst, 7)