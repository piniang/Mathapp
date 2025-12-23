def resoudre_equation_deg1(a, b):
    print("Équation de la forme : ax + b = 0")

    # Entrée des coefficients
   # a = float()
    #b = float()

    # differents cas
    if a == 0 and b == 0:
        return("L'équation admet une infinité de solutions.")
    elif a == 0 and b != 0:
        return("L'équation n'a pas de solution.")
    else:
        x = -b / a
        return f"La solution unique (dans R) est : x = {x:.2f}"

# Appel de la fonction
#resoudre_equation_deg1()
