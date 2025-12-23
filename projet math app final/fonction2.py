import numpy as np
from sympy import symbols, limit, diff, solve, S, sympify, oo, Interval, Union
import sympy as sp
from sympy.calculus.util import continuous_domain
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x = sp.symbols('x')

def formater_intervalle(inter):
    """Formate un intervalle SymPy pour l'affichage"""
    if isinstance(inter, Interval):
        j = inter.start
        k = inter.end
        
        # Déterminer les crochets
        gauche = "]" if inter.left_open else "["
        droite = "[" if inter.right_open else "]"
        
        # Gérer les infinis
        if j == -sp.oo:
            j_str = "-∞"
        else:
            try:
                j_str = f"{float(j):.2f}"
            except:
                j_str = str(j)
        
        if k == sp.oo:
            k_str = "+∞"
        else:
            try:
                k_str = f"{float(k):.2f}"
            except:
                k_str = str(k)
        
        return f"{gauche}{j_str}; {k_str}{droite}"
    return str(inter)

def formater_domaine(domaine):
    """Formate le domaine de définition pour l'affichage"""
    if isinstance(domaine, Union):
        return " ∪ ".join([formater_intervalle(inter) for inter in domaine.args])
    elif isinstance(domaine, Interval):
        return formater_intervalle(domaine)
    else:
        return str(domaine)

def calculer_limites_bornes(func, domaine):
    """Calcule les limites aux bornes du domaine de définition"""
    limites = []
    limites_deja_calculees = set()  # Pour éviter les doublons
    
    def extraire_bornes(dom):
        """Extrait toutes les bornes du domaine"""
        bornes = []
        if isinstance(dom, Union):
            for inter in dom.args:
                if isinstance(inter, Interval):
                    if inter.start != -sp.oo:
                        bornes.append(('gauche', inter.start, inter.left_open))
                    if inter.end != sp.oo:
                        bornes.append(('droite', inter.end, inter.right_open))
        elif isinstance(dom, Interval):
            if dom.start != -sp.oo:
                bornes.append(('gauche', dom.start, dom.left_open))
            if dom.end != sp.oo:
                bornes.append(('droite', dom.end, dom.right_open))
        return bornes
    
    bornes = extraire_bornes(domaine)
    
    # Calculer les limites aux bornes finies
    for direction, borne, ouvert in bornes:
        cle = (direction, float(borne), ouvert)
        if cle not in limites_deja_calculees:
            limites_deja_calculees.add(cle)
            try:
                if direction == 'gauche':
                    if ouvert:
                        lim = sp.limit(func, x, borne, dir='+')
                    else:
                        lim = sp.limit(func, x, borne, dir='-')
                else:  # droite
                    if ouvert:
                        lim = sp.limit(func, x, borne, dir='-')
                    else:
                        lim = sp.limit(func, x, borne, dir='+')
                
                if lim == sp.oo:
                    lim_str = "+∞"
                elif lim == -sp.oo:
                    lim_str = "-∞"
                else:
                    try:
                        lim_str = f"{float(lim):.2f}"
                    except:
                        lim_str = str(lim)
                
                symbole = "⁻" if direction == 'gauche' else "⁺"
                limites.append(f"lim(x→{borne}{symbole}) = {lim_str}")
            except:
                symbole = "⁻" if direction == 'gauche' else "⁺"
                limites.append(f"lim(x→{borne}{symbole}) = Indéfinie")
    
    # Limites aux infinis si le domaine s'étend jusqu'à l'infini (une seule fois)
    a_infini_negatif = False
    a_infini_positif = False
    
    if isinstance(domaine, Union):
        for inter in domaine.args:
            if isinstance(inter, Interval):
                if inter.start == -sp.oo:
                    a_infini_negatif = True
                if inter.end == sp.oo:
                    a_infini_positif = True
    elif isinstance(domaine, Interval):
        if domaine.start == -sp.oo:
            a_infini_negatif = True
        if domaine.end == sp.oo:
            a_infini_positif = True
    
    if a_infini_negatif:
        try:
            lim_inf = sp.limit(func, x, -sp.oo)
            if lim_inf == sp.oo:
                limites.append("lim(x→-∞) = +∞")
            elif lim_inf == -sp.oo:
                limites.append("lim(x→-∞) = -∞")
            else:
                try:
                    limites.append(f"lim(x→-∞) = {float(lim_inf):.2f}")
                except:
                    limites.append(f"lim(x→-∞) = {lim_inf}")
        except:
            limites.append("lim(x→-∞) = Indéfinie")
    
    if a_infini_positif:
        try:
            lim_inf = sp.limit(func, x, sp.oo)
            if lim_inf == sp.oo:
                limites.append("lim(x→+∞) = +∞")
            elif lim_inf == -sp.oo:
                limites.append("lim(x→+∞) = -∞")
            else:
                try:
                    limites.append(f"lim(x→+∞) = {float(lim_inf):.2f}")
                except:
                    limites.append(f"lim(x→+∞) = {lim_inf}")
        except:
            limites.append("lim(x→+∞) = Indéfinie")
    
    return limites

def Etude_De_Fonction(fonction, point, pt_deriv):
    try:
        func = sp.sympify(fonction)
        i = float(point)
        a = float(pt_deriv)

        # Calcul de la limite en un point donné
        try:
            lim_calc = sp.limit(func, x, i)
            if lim_calc == sp.oo:
                limite_str = "+∞"
            elif lim_calc == -sp.oo:
                limite_str = "-∞"
            else:
                try:
                    limite_str = f"{float(lim_calc):.2f}"
                except:
                    limite_str = str(lim_calc)
        except:
            limite_str = "Indéfinie"
        
        limite_point = f"Limite en {point} : {limite_str}"

        # Domaine de définition avec formatage correct
        domaine = continuous_domain(func, x, S.Reals)
        domaine_str = formater_domaine(domaine)
        
        # Calculer les limites aux bornes du domaine
        limites_bornes = calculer_limites_bornes(func, domaine)
        limites_bornes_str = "\n".join(limites_bornes) if limites_bornes else "Aucune limite aux bornes"

        # Calcul de la dérivée
        deriv = sp.diff(func, x)
        deriv_str = sp.pretty(deriv, use_unicode=True)

        # Continuité en un point donné
        try:
            gauche = limit(func, x, a, dir='-')
            droite = limit(func, x, a, dir='+')
            valeur = func.subs(x, a)

            # Conversion en float pour comparaison
            try:
                g_val = float(gauche.evalf()) if gauche not in [sp.oo, -sp.oo] else gauche
                d_val = float(droite.evalf()) if droite not in [sp.oo, -sp.oo] else droite
                v_val = float(valeur.evalf()) if valeur not in [sp.oo, -sp.oo] else valeur
                
                if g_val == d_val == v_val:
                    continuite = (
                        f"f(x) est continue en x = {a}\n"
                        f"f({a}) = {v_val:.1f}\n"
                        f"lim(x→{a}⁻) = {g_val:.1f} et lim(x→{a}⁺) = {d_val:.1f}"
                    )
                else:
                    continuite = (
                        f"f(x) n'est pas continue en x = {a}\n"
                        f"lim(x→{a}⁻) = {g_val:.1f}\n"
                        f"lim(x→{a}⁺) = {d_val:.1f}\n"
                        f"f({a}) = {v_val:.1f}"
                    )
            except:
                continuite = f"Évaluation de la continuité complexe en x = {a}"
                
        except Exception as e:
            continuite = f"Impossible d'évaluer la continuité en x = {a}. Erreur : {str(e)}"

        # Calcul des valeurs remarquables (points critiques et leurs valeurs)
        valeurs_remarquables = []
        point_critique_reels = []
        try:
            point_critique = sp.solve(deriv, x)
            point_critique_reels = [p.evalf() for p in point_critique if p.is_real]
            point_critique_reels = sorted(point_critique_reels)
            
            if point_critique_reels:
                valeurs_remarquables.append("Points critiques (f'(x) = 0):")
                for pt in point_critique_reels:
                    try:
                        val_pt = func.subs(x, pt)
                        if val_pt == sp.oo:
                            val_str = "+∞"
                        elif val_pt == -sp.oo:
                            val_str = "-∞"
                        else:
                            try:
                                val_str = f"{float(val_pt):.2f}"
                            except:
                                val_str = str(val_pt)
                        valeurs_remarquables.append(f"  x = {float(pt):.2f} → f({float(pt):.2f}) = {val_str}")
                    except:
                        valeurs_remarquables.append(f"  x = {float(pt):.2f} → f({float(pt):.2f}) = Indéfinie")
            else:
                valeurs_remarquables.append("Aucun point critique réel")
            
            # Calcul de la dérivée seconde pour déterminer la nature des points critiques
            try:
                deriv2 = sp.diff(deriv, x)
                if point_critique_reels:
                    valeurs_remarquables.append("\nNature des points critiques:")
                    for pt in point_critique_reels:
                        try:
                            val_deriv2 = deriv2.subs(x, pt)
                            if val_deriv2.is_real:
                                val_deriv2_float = float(val_deriv2.evalf())
                                if val_deriv2_float > 0:
                                    nature = "minimum local"
                                elif val_deriv2_float < 0:
                                    nature = "maximum local"
                                else:
                                    nature = "point d'inflexion"
                                valeurs_remarquables.append(f"  x = {float(pt):.2f} : {nature} (f''({float(pt):.2f}) = {val_deriv2_float:.2f})")
                            else:
                                valeurs_remarquables.append(f"  x = {float(pt):.2f} : nature indéterminée")
                        except:
                            valeurs_remarquables.append(f"  x = {float(pt):.2f} : nature indéterminée")
            except:
                pass
            
            # Ajouter -∞ et +∞ aux extrémités
            points_etendus = [-sp.oo] + point_critique_reels + [sp.oo]
            
            intervalles = []
            behaviours = []
            values = []

            for i in range(len(points_etendus) - 1):
                left = points_etendus[i]
                right = points_etendus[i + 1]
                
                # Point milieu sûr
                if left == -sp.oo and right != sp.oo:
                    midpoint = right - 1
                elif right == sp.oo and left != -sp.oo:
                    midpoint = left + 1
                elif left == -sp.oo and right == sp.oo:
                    midpoint = 0
                else:
                    midpoint = (left + right) / 2

                try:
                    val_mid = deriv.subs(x, midpoint)
                    if val_mid.is_real:
                        sign = sp.sign(val_mid)
                    else:
                        sign = 0
                except:
                    sign = 0

                behaviour = '↗' if sign > 0 else '↘' if sign < 0 else '→'

                intervalles.append((left, right))
                behaviours.append(behaviour)

                # Valeur de f(x) à droite (sauf pour +∞)
                if right == sp.oo:
                    value = None
                else:
                    try:
                        value = func.subs(x, right)
                    except:
                        value = None
                values.append(value)

            # Création du tableau de variation
            fig, ax = plt.subplots(figsize=(12, 5))
            fig.patch.set_facecolor('white')

            # Préparation des données du tableau
            intervalle_str = []
            for left, right in intervalles:
                left_str = "-∞" if left == -sp.oo else f"{float(left):.1f}"
                right_str = "+∞" if right == sp.oo else f"{float(right):.1f}"
                intervalle_str.append(f"]{left_str}; {right_str}[")

            signs_row = []
            for i in range(len(intervalles)):
                left, right = intervalles[i]
                if left == -sp.oo and right != sp.oo:
                    midpoint = right - 1
                elif right == sp.oo and left != -sp.oo:
                    midpoint = left + 1
                elif left == -sp.oo and right == sp.oo:
                    midpoint = 0
                else:
                    midpoint = (left + right) / 2
                
                try:
                    val_mid = deriv.subs(x, midpoint)
                    s = sp.sign(val_mid.evalf()) if val_mid.is_real else 0
                    signs_row.append("+" if s > 0 else "-" if s < 0 else "0")
                except:
                    signs_row.append ("?")

            values_row = []
            for val in values:
                if val is None:
                    values_row.append("")
                else:
                    try:
                        values_row.append(f"{float(val):.1f}")
                    except:
                        values_row.append(str(val))

            # Création du tableau
            table_data = [
                ["Intervalle"] + intervalle_str,
                ["Signe f'(x)"] + signs_row,
                ["Variation"] + behaviours,
                ["f(x)"] + values_row
            ]

            ax.axis('tight')
            ax.axis('off')

            table = ax.table(cellText=table_data, cellLoc='center', loc='center', 
                           colWidths=[0.15] * (len(intervalles) + 1))
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1.2, 2)

            for (i, j), cell in table.get_celld().items():
                if i == 0 or j == -1:
                    cell.set_text_props(weight='bold')
                cell.set_edgecolor('black')
                cell.set_linewidth(1)

            plt.tight_layout()

        except Exception as e:
            # Si erreur dans le tableau, créer une figure vide
            fig, ax = plt.subplots(figsize=(12, 5))
            ax.text(0.5, 0.5, f"Erreur dans le tableau de variation: {str(e)}", 
                   ha='center', va='center', transform=ax.transAxes)
            ax.axis('off')
            valeurs_remarquables = [f"Erreur dans le calcul des valeurs remarquables: {str(e)}"]

        # Résultat final avec toutes les informations
        valeurs_remarquables_str = "\n".join(valeurs_remarquables) if valeurs_remarquables else "Aucune valeur remarquable"
        
        solution = (
            f"f(x) = {fonction}\n\n"
            f"Domaine de définition : {domaine_str}\n\n"
            f"Limites aux bornes du domaine :\n{limites_bornes_str}\n\n"
            f"{limite_point}\n\n"
            f"Dérivée : f'(x) = {deriv_str}\n\n"
            f"Valeurs remarquables :\n{valeurs_remarquables_str}\n\n"
            f"Continuité : {continuite}"
        )  
        # Tracé de la courbe de la fonction

        fig2, ax2 = plt.subplots(figsize=(7, 5))

        # Créer un espace de valeurs pour x
        xs = np.linspace(-10, 10, 400)

        # Convertir la fonction sympy en fonction numpy
        f_lamb = sp.lambdify(x, func, "numpy")

        try:
            ys = f_lamb(xs)
        except:
            ys = [None] * len(xs)

        ax2.plot(xs, ys, "b--", label="courbe de la fonction")
        ax2.set_title("Courbe de f(x)")
        ax2.set_xlabel("Abscisses")
        ax2.set_ylabel("Ordonnées")
        ax2.legend()
        ax2.grid(True)
        
        return fig, fig2, solution

    except Exception as e:
        # En cas d'erreur générale
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.text(0.5, 0.5, f"Erreur: {str(e)}", 
               ha='center', va='center', transform=ax.transAxes)
        ax.axis('off')
        
        solution = f"Erreur dans l'étude de fonction: {str(e)}"
        return fig, solution