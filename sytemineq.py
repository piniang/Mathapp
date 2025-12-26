import matplotlib.pyplot as plt
import numpy as np
def resoudre_systemineq(a1, b1, c1, a2, b2, c2, relation_etudie1, relation_etudie2):
# Choix des X pour tracer les droites
    X_val = np.linspace(-30, 30, 400)

# Fonction pour calculer Y 
    def cherche_y(a, b, c, X):
        if b == 0:  # droite verticale
            return None
        return (c - a * X) / b

# Calcul des Y
    Y1 = cherche_y(a1, b1, c1, X_val)
    Y2 = cherche_y(a2, b2, c2, X_val)

# Création de la grille pour la zone solution
    Xgri, Ygri = np.meshgrid(np.linspace(-30, 30, 400), np.linspace(-30, 30, 400))
    in1 = a1*Xgri + b1*Ygri
    if relation_etudie1 == ">=":
        ineq1 = in1 >= c1
    elif relation_etudie1 == "<=":
        ineq1 = in1 <= c1
    elif relation_etudie1 == ">":
        ineq1 = in1 > c1
    elif relation_etudie1 == "<":
        ineq1 = in1 < c1
    else:
        return("Relation 1 invalide ! Utilisez >=, <=, > ou <")
    in2 = a2*Xgri + b2*Ygri
    if relation_etudie2 == ">=":
        ineq2 = in2 >= c2
    elif relation_etudie2 == "<=":
        ineq2 = in2 <= c2
    elif relation_etudie2 == ">":
        ineq2 = in2 > c2
    elif relation_etudie2 == "<":
        ineq2 = in2 < c2
    else:
        return("Relation 2 invalide ! Utilisez >=, <=, > ou <")
    solution_zone = ineq1 & ineq2

# Tracé
    solution = plt.figure(figsize=(8, 8))

# Zone solution
    plt.imshow(solution_zone, extent=(-30, 30, -30, 30), origin='lower',
        cmap='Greens', alpha=0.3)
#plt.text(-28, 28, "ZONE DE SOLUTION", color='blue', fontsize=12)


# Droites
    if b1 != 0:
        plt.plot(X_val, Y1, 'r', label= f"Droite 1 : {a1} x + {b1} y = {c1}")
    else:
        plt.axvline(c1/a1, color='r', label="Droite 1 (verticale)")

    if b2 != 0:
        plt.plot(X_val, Y2, 'b', label=f"Droite 2 : {a2} x + {b2} y = {c2}")
    else:
        plt.axvline(c2/a2, color='b', label="Droite 2 (verticale)")

    # Mise en forme
    plt.xlim(-30, 30)
    plt.ylim(-30, 30)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Zone de solution du système d'inéquations en vert")
    plt.grid(True)
    plt.legend()
    #plt.show()
    return solution

