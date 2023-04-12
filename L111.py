# The Authors are Bethany Berlage, Olivia Busk, and Rosemary Hoffman

def my_get_method(dict,key,default):
    if key in dict:
        return dict[key]
    else:
        return default

dict1={"a":1,"b":1,"o":2,"n":1,"s":2,"r":2,"u":2}
print(my_get_method(dict1,"b",0))
print(my_get_method(dict1,"c","yay"))
print(my_get_method(dict1,"y",True))
print(my_get_method(dict1,"w",4.6))
