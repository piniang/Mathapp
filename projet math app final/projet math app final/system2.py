from sympy import symbols, Eq, solve
#from sympy.solvers.solveset import solveset_real

def resoudre_systeme(a1, b1, c1, a2, b2, c2):

 x, y = symbols('x y')
 print("Entrer les valeurs ")
 #a1 = float(input("a1 = "))
 #b1 = float(input("b1 = "))
 #c1 = float(input("c1 = "))
 #a2 = float(input("a2 = "))
 #b2 = float(input("b2 = "))
 #c2 = float(input("c2 = "))
 eq1 = Eq(a1*x + b1*y, c1)
 eq2 = Eq(a2*x + b2*y, c2)
 solution = solve((eq1, eq2), (x, y))
 return "\nResultat dans R:", solution
