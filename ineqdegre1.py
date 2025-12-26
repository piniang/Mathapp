def inequationdegre1 (a,b,operateur):
    #cas ou a=0
     if a==0:
          if operateur == ">" and b > 0:
               return (" x appartient a R") 
          elif operateur == "<" and b < 0:
               return ("x appartient a R ")
          else :
               return f"pas de solution dans R"
    # solution c'est la valeur de reference pour determiner l'intervalle solution s'il existe
     solution = -b/a 
     if a>0:
          if operateur == ">":
               return f"x > {solution}"
          elif operateur == ">=":
               return f"x >= {solution}"
          elif operateur == "<":
               return f"x < {solution}"
          elif operateur == "<=":
               return f"x <= {solution}"
          
     else : #a<0:
          if operateur == ">":
               return "x < {solution}"
          elif operateur == ">=":
               return f"x <= {solution}"
          elif operateur == "<":
               return f"x > {solution}"
          elif operateur == "<=":
               return f"x >= {solution}"



