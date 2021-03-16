lista = [3,5,6, 4,2]
newlist = []
i = 0
n = len(lista)

while i <= n - 1:
    if lista[i] < 5:
        newlist.append(lista[i])
    i = i + 1

print(newlist)
"""
if i < n -1: #Waypoint1
    if lista[i] < 5:
        newlist.append(lista[i])
    i = i + 1
    #GOTO Waypoint1
else:
    print(newlist)
"""
