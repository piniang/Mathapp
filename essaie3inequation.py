from sympy import symbols, solveset, S
from fonction2 import formater_domaine

def resoudre_ineq2nd(a, b, c, relation_etudie):
   x = symbols('x')
   ineq = a*x**2 + b*x + c

    # Déterminer la relation
   if relation_etudie == ">=":
      rel = ">="
   elif relation_etudie == "<=":
      rel = "<="
   elif relation_etudie == ">":
      rel = ">"
   elif relation_etudie == "<":
      rel = "<"
   else:
      return "Relation invalide ! Utilisez >=, <=, > ou <"

   if rel == ">=":
      solution = solveset(ineq >= 0, x, domain=S.Reals)
   elif rel == "<=":
      solution = solveset(ineq <= 0, x, domain=S.Reals)
   elif rel == ">":
      solution = solveset(ineq > 0, x, domain=S.Reals)
   elif rel == "<":
      solution = solveset(ineq < 0, x, domain=S.Reals)

    # Gestion des cas particuliers
   if solution == S.Reals:
      solution = "R"
   elif solution == S.EmptySet:
      solution = "∅"
   else:
      solution = formater_domaine(solution)

   return f"Résultat dans R : {solution}"
