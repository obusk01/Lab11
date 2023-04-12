# The Authors are Bethany Berlage, Olivia Busk, and Rosemary Hoffman

redvelvet={"flour":3,"baking soda":2,"cocoa":2,"salt":1.5,"butter":1.5,"sugar":2,"vegetable oil":1,"vanilla extract":1,"white vinegar":1,"buttermilk":1}
lemon={"flour":1.5,"baking powder":2,"salt":1.5,"butter":1.5,"sugar":1,"eggs":2,"vanilla extract":1,"milk":1.5}
def similar_ingredients(h):
    a=redvelvet
    b=lemon
    if h in a:
        if h in b:
            print("Both recipes have", h)
        else:
            print(h, "is only in red velvet")
    else:
        print(h, "is only in lemon")

similar_ingredients("salt")
similar_ingredients("baking soda")
similar_ingredients("baking powder")
