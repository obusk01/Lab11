# The Authors are Bethany Berlage, Olivia Busk, and Rosemary Hoffman


dict={}
names=["Busk","Olivia","Berlage","Bethany","Hoffman","Rosemary","Paradisio", "Vinnie","Nixon", "Emily","Anspach","Grace","Bong", "Saerin","Eafon", "Breanna","O'Roark", "Katherine","Stephenson", "Sarah","Dockery", "Krista","Faye Gallaway", "Gabrielle"]
last_names=names[::2]
def histogram(x):
    d=dict{}
    for char in word:
        if char[0] not in d:
            d[char[0]]=[char]
        else:
            d[char[0]].append(char)
    return d

print(histogram(last_names))




# for x in last_names:
#     dict.append(x,x[0])
# print(dict)


# inverse=dict()
# for key in names:
#     val=names[key]
#     if val not in inverse:
#         inverse[val]=[key]
#     else:
#         inverse[val]=[key]
# print(inverse)
