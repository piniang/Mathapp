def resoudre_equation_deg4(a, b, c, d, e):

 from sympy import symbols, Eq, solve
 x = symbols('x',real=True)
 print("Entrer les valeurs ")
 #a = float(input("a = "))
 #b = float(input("b = "))
 #c = float(input("c = "))
 #d = float(input("d = "))
 #e = float(input("e = "))
 eq = Eq(a*x**4 + b*x**3 + c*x**2 + d*x + e, 0)

 solution = solve((eq), (x))
 return "Résultat dans R : x = " + ", ".join(f"{float(s):.2f}" for s in solution)
