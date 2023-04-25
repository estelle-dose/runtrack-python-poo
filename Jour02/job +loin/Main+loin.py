def triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b :
        if a==b==c :
            return("triangle equilateral")
        elif a == b or b == c or c == a :
            if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2 :
                return("isocele rectangle")
            else :
                return("isocele")
        elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2 :
            return("rectangle")
        else :
            return("quelconque")
    else :
        return("pas de triangle")
    
print(triangle(4, 4, 4))
print(triangle(5, 4, 3))
print(triangle(2, 4, 4))
print(triangle(10, 21, 18))
