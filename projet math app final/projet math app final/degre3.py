from sympy import symbols, solve
def resoudre_equation_deg3(a, b, c, d):
 x = symbols('x',real=True)

 # Saisie des coefficients
 print("Soit une équation de la forme : ax^3 + bx^2 + cx +d = 0")
 #a = float(input("a = "))
 #b = float(input("b = "))
 #c = float(input("c = "))
 #d = float(input("d = ")) 

 degree = 3

 # Construire le polynôme
 equation = a*x**3 + b*x**2 + c*x + d

 # Résolution
 solutions = solve(equation, x)
 return("Résultat :", solutions)

