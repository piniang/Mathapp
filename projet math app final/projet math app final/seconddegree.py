import math
def resoudre_equation_deg2(a, b, c):
 #a = float() 
 #b = float()
 #c = float()
 delta = b**2 - 4*a*c 
 if delta < 0 : 
     return("pas de solution reelles") 
 elif delta == 0 : 
     x = (-b) / (2*a)
     return("la valeur de la solution :", x)
 else :
     x1 = (-b-math.sqrt(delta))/2*a 
     x2 = (-b+math.sqrt(delta))/2*a 
     return("les solution sont :", format(x1,".2f"), "et", format(x2,".2f"))