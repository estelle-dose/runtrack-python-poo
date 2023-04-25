def saity(type, saison):
    if type == "fruits" and saison == "hiver" :
        return("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete" :
        return("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver" :
        return("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete" :
        return("artichaut, aubergine, navet")
    else :
        return("nothing")
    
print(saity("fruits", "ete"))
print(saity("fruits", "hiver"))
print(saity("legume", "hiver"))
print(saity("legume", "ete"))
print(saity("legume", "automne"))