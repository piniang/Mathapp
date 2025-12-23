from sympy import symbols, sympify, S, limit
from sympy.calculus.util import continuous_domain

x = symbols('x')

# Demander la fonction
fonction_str = input("Entrez votre fonction en x : ")
fonction = sympify(fonction_str)

# Domaine de definition
domaine = continuous_domain(fonction, x, S.Reals)
print(f"\n Domaine de definition de f(x) = {fonction} : {domaine}")

#  continuité en un point donné
a = float(input("\nEntrez un point pour tester la continuité : "))

try:
    gauche = limit(fonction, x, a, dir='-')
    droite = limit(fonction, x, a, dir='+')
    valeur = fonction.subs(x, a)

    if gauche == droite == valeur:
        print(f" f(x) est continue en x = {a}")
    else:
        print(f" f(x) n’est pas continue en x = {a}")
        
except Exception as e:
    print(f" Impossible d’évaluer la continuité en x = {a}. Erreur : {e}")
