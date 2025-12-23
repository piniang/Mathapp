from sympy import symbols, solve_univariate_inequality, oo, Interval, Union

def resoudre_ineq2nd(a, b, c, relation_etudie):
   x = symbols('x')

   #return("Soit une inéquation de la forme : ax^2 + bx + c ")
 
   # Demande à l'utilisateur le type d'inéquation
   #relation = input("Choisir la relation (>=, <=, >, <) : ")

   # Construire l'inéquation
   ineq = a*x**2 + b*x + c
   if relation_etudie == ">=":
      inequation = ineq >= 0
   elif relation_etudie == "<=":
      inequation = ineq <= 0 
   elif relation_etudie == ">":
      inequation = ineq > 0
   elif relation_etudie == "<":
      inequation = ineq < 0
   else:
      return("Relation invalide ! Utilisez >=, <=, > ou <")
 
   # Résolution
   solution = solve_univariate_inequality(inequation, x)
   if(solution==False):
      solution = "R"

   # Personnalisation des bornes    
      # Personnalisation des bornes    
   def intervalle(inter):
         j = inter.start
         k = inter.end
         gauche = '[' if not inter.left_open else '('
         droite = ']' if not inter.right_open else ')'
        
         # Pour les infinies
         if j == -oo:
            j = "−∞"
         if k == oo:
            k = "+∞"

         return f"{gauche}{j}, {k}{droite}"

      # Affichage de la solution
   if isinstance(solution, Union):
      solution_str = " U ".join([intervalle(inter) for inter in solution.args])
   elif isinstance(solution, Interval):
      solution_str = intervalle(solution)
   else:
      solution_str = str(solution)

   return f"Résultat dans R : {solution_str}"