import math

# 1. Addition basique
def addition(a, b):
    return a + b


# 2. Soustraction basique
def soustraction(a, b):
    return a - b


# 3. Multiplication basique
def multiplication(a, b):
    return a * b


# 4. Division basique
def division(a, b):
    return a/b


# 5. Quotient de la division euclidienne (ou division entière)
def quotient(a, b):
    return a // b


# 6. Reste de la division euclidienne
def reste(a, b):
    return a % b


# 7. Retourne le nombre sans tenir compte de son signe
def valeur_absolue(a):
    return abs(a)

# 8. Retourne la valeur au carré
def carre(a):
    return a * a


# 9. Retourne la racine carré de la valeur
def racine_carre(a):
    return math.sqrt(a)


# 10. Retourne la somme des éléments de la liste
def somme_liste(l):
    return sum(l)


# 11. Retourne a puissance b
def puissance(a, b):
    return a ** b


# 12. Retourne l'inverse du nombre
def inverse(a):
    if a == 0:
        raise ValueError("Cannot divide by zero")
    return 1 / a


# 13. Retourne une version triée de la liste
def tri(l): 
    return sorted(l)

# 14. Retourne la factorielle de la valeur
def factoriel(a):
    fact = 1
    for k in range(1, a+1):
        fact = fact*k
    return fact

# 15. Retourne la plus grande valeur de la liste
def maximum(l):
    max_val = l[0]
    for val in l:
        if val > max_val:
            max_val = val
    return max_val

# 16. Retourne le logarithme (en base de 10) de la valeur
def logarithme(a):
    return math.log10(a)