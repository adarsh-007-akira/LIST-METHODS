elems=int(input("Number Of Elements In List : \n"))
lst = []
for i in range(elems):
    lst.append((input(f"What is the {i+1} element :\n")))
def finder(list, string):
    newlst=list.copy()
    word=string
    find=False
    for i in list:
        if i==word:
            find=True
    print("Elment exists")
finder(lst,"Adarsh")