
from tkinter import Tk, Canvas, Button, Entry, Label
from PIL import Image, ImageTk
from pathlib import Path
from equationdegre1 import resoudre_equation_deg1
from seconddegree import resoudre_equation_deg2
from degre3 import resoudre_equation_deg3
from equ4 import resoudre_equation_deg4
from ineqdegre1 import inequationdegre1
from system2 import resoudre_systeme
from sytemineq import resoudre_systemineq
from essaie3inequation import resoudre_ineq2nd
from fonction2 import Etude_De_Fonction
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np



#image page
OUTPUT_PATH = Path(__file__).parent
IMAGE_PAGE1 = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE2 = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE3 = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE4 = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_Equation_1_degre = OUTPUT_PATH / "image.jpg"
IMAGE_PAG_Equation_2_degre = OUTPUT_PATH / "image.jpg"
IMAGE_PAG_Equation_3_degre = OUTPUT_PATH / "image.jpg"
IMAGE_PAG_Equation_4_degre = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_Systeme_Equation = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_Inequation_1_degre = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_Inequation_2_degre = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_Systeme_Inequation = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_fonction = OUTPUT_PATH / "image.jpg"
IMAGE_PAGE_solution = OUTPUT_PATH / "image.jpg"


window = Tk()
window.geometry("900x600")
window.resizable(False, False)
window.title("Mathapp")


canvas = Canvas(window, width=900, height=600)
canvas.pack(fill="both", expand=True)


bg_image = None
label_resultat_fonction = None
canvas_fig_fonction = None
canvas_fig_fonction2 = None

#  page 1 
def show_page1():
    global bg_image
    canvas.delete("all") 

    pil_image = Image.open(IMAGE_PAGE1).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Bienvenue dans Mathapp",
        fill="#000000",
        font=("Inter", 32, "bold")
    )

    canvas.create_text(
        450, 250,
        anchor="center",
        text="L’outil de résolution de vos problèmes mathématiques",
        fill="#000000",
        font=("Inter", 15, "bold")
    )

    suivant_button = Button(window, text="SUIVANT", font=("Inter", 20, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page2)
    canvas.create_window(450, 380, anchor="center", window=suivant_button)

#  page 2 
def show_page2():
    global bg_image, label_resultat_fonction, canvas_fig_fonction, canvas_fig_fonction2
    canvas.delete("all")
    
    # Nettoyer les widgets précédents (canvas matplotlib et labels)
    if 'label_resultat_fonction' in globals() and label_resultat_fonction:
        try:
            label_resultat_fonction.destroy()
            label_resultat_fonction = None
        except:
            pass
    if 'canvas_fig_fonction' in globals() and canvas_fig_fonction:
        try:
            canvas_fig_fonction.get_tk_widget().destroy()
            canvas_fig_fonction = None
        except:
            pass
    if 'canvas_fig_fonction2' in globals() and canvas_fig_fonction2:
        try:
            canvas_fig_fonction2.get_tk_widget().destroy()
            canvas_fig_fonction2 = None
        except:
            pass

    pil_image = Image.open(IMAGE_PAGE2).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="En quoi pouvons nous vous aidez ?",
        fill="#000000",
        font=("Inter", 24, "bold")
    )

    Equation_button = Button(window, text="Équation", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page3,width=15)
    canvas.create_window(450, 200, anchor="center", window=Equation_button)

    Inequation_button = Button(window, text="Inéquation", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page4,width=15)
    canvas.create_window(450, 300, anchor="center", window=Inequation_button)

    Etude_de_fonction_button = Button(window, text="Étude de fonction", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page_fonction,width=15)
    canvas.create_window(450, 400, anchor="center", window=Etude_de_fonction_button)

    quitter_button = Button(window, text="QUITTER", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=window.quit)
    canvas.create_window(0, 600, anchor="sw", window=quitter_button)

#  page 3 
def show_page3():
    global bg_image
    canvas.delete("all")  

    pil_image = Image.open(IMAGE_PAGE3).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    Equation_1e_degre_button = Button(window, text="Équation 1e degré", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page1Equation_1_degre,width=20)
    canvas.create_window(450, 100, anchor="center", window=Equation_1e_degre_button)

    Equation_2e_degre_button = Button(window, text="Équation 2e degré", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page1Equation_2_degre,width=20)
    canvas.create_window(450, 200, anchor="center", window=Equation_2e_degre_button)

    Equation_3e_degre_button = Button(window, text="Équation 3e degré", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page1Equation_3_degre,width=20)
    canvas.create_window(450, 300, anchor="center", window=Equation_3e_degre_button)

    Equation_4e_degre_button = Button(window, text="Équation 4e degré", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page1Equation_4_degre,width=20)
    canvas.create_window(450, 400, anchor="center", window=Equation_4e_degre_button)

    SystemeEquation_button = Button(window, text="Système d'équations", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page_Systeme_Equation,width=20)
    canvas.create_window(450, 500, anchor="center", window=SystemeEquation_button)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page2)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

def show_page4():
    global bg_image
    canvas.delete("all")  

    pil_image = Image.open(IMAGE_PAGE4).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="En quoi pouvons nous vous aidez ?",
        fill="#000000",
        font=("Inter", 24, "bold")
    )

    Inequation_1e_degre_button = Button(window, text="Inéquation 1e degré", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page1Inequation_1_degre,width=20)
    canvas.create_window(450, 200, anchor="center", window=Inequation_1e_degre_button)

    Inequation_2e_degre_button = Button(window, text="Inéquation 2e degré", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page1Inequation_2_degre,width=20)
    canvas.create_window(450, 300, anchor="center", window=Inequation_2e_degre_button)

    Systeme_Inequation_button = Button(window, text="Système d'équations", font=("Inter", 15, "bold"),
                              bg="#D9D9D9", fg="#000000", command=show_page_Systeme_Inequation,width=20)
    canvas.create_window(450, 400, anchor="center", window=Systeme_Inequation_button)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page2)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)


def resolution_equation_deg1():
  global solution, page_precedent
  page_precedent = show_page1Equation_1_degre
  try:
      a = float(entry_a.get())
      b = float(entry_b.get())
      solution = resoudre_equation_deg1(a, b)  

      show_page_solution()
  except ValueError:
        solution = "Veuillez entrer des nombres valides."
        show_page_solution()

#page equ 1degre
def show_page1Equation_1_degre():
    global bg_image, entry_a, entry_b
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAGE_Equation_1_degre).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre équation",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    
    canvas.create_text(
    220.0,
    200.0,
    anchor="nw",
    text="a=____.\n\n\nb=____.\n\n  ",
    fill="#000000",
    font=("Inter", 20 )
    )


    entry_a = Entry(window, font=("Inter", 14), justify="center")
    entry_b = Entry(window, font=("Inter", 14), justify="center")

    canvas.create_window(280, 216, width=70, height=34, window=entry_a)
    canvas.create_window(280, 312, width=70, height=34, window=entry_b)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page3)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command= resolution_equation_deg1)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)

def resolution_equation_deg2():
  global solution, page_precedent
  a = float(entry_a.get())
  b = float(entry_b.get())
  c = float(entry_c.get())

  solution = resoudre_equation_deg2(a, b, c)
  page_precedent = show_page1Equation_2_degre
  show_page_solution()

#page equ 2degre
def show_page1Equation_2_degre():
    global bg_image, entry_a, entry_b, entry_c
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAG_Equation_2_degre).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre équation",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_text(
    220.0,
    200.0,
    anchor="nw",
    text="a=____.\n\n\nb=____.\n\n\nc=____.\n\n  ",
    fill="#000000",
    font=("Inter", 20 )
  )
    
    # Zone de saisie  centrée dans les espaces attribués aux valeurs
    entry_a = Entry(window, font=("Inter", 14), justify="center")
    entry_b = Entry(window, font=("Inter", 14), justify="center")
    entry_c = Entry(window, font=("Inter", 14), justify="center")

    
    canvas.create_window(280, 216, width=70, height=30, window=entry_a)
    canvas.create_window(280, 312, width=70, height=30, window=entry_b)
    canvas.create_window(280, 409, width=70, height=30, window=entry_c)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page3)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_equation_deg2)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)

def resolution_equation_deg3():
  global solution, page_precedent
  a = float(entry_a.get())
  b = float(entry_b.get())
  c = float(entry_c.get())
  d = float(entry_d.get())

  solution = resoudre_equation_deg3(a, b, c, d)
  page_precedent = show_page1Equation_3_degre
  show_page_solution()

#page equ 3degre
def show_page1Equation_3_degre():
    global bg_image, entry_a, entry_b, entry_c, entry_d
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAG_Equation_3_degre).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre équation",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_text(
    220.0,
    150.0,
    anchor="nw",
    text="a=____.\n\n\nb=____.\n\n\nc=____.\n\n\nd=____.\n\n  ",
    fill="#000000",
    font=("Inter", 18 )
 )
    # Zone de saisie  centrée dans les espaces attribués aux valeurs
    entry_a = Entry(window, font=("Inter", 14), justify="center")
    entry_b = Entry(window, font=("Inter", 14), justify="center")
    entry_c = Entry(window, font=("Inter", 14), justify="center")
    entry_d = Entry(window, font=("Inter", 14), justify="center")

    canvas.create_window(276, 162, width=70, height=30, window=entry_a)
    canvas.create_window(276, 242, width=70, height=30, window=entry_b)
    canvas.create_window(276, 324, width=70, height=30, window=entry_c)
    canvas.create_window(276, 405, width=70, height=30, window=entry_d)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page3)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_equation_deg3)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)

def resolution_equation_deg4():
  global solution, page_precedent
  a = float(entry_a.get())
  b = float(entry_b.get())
  c = float(entry_c.get())
  d = float(entry_d.get())
  e = float(entry_e.get())

  solution = resoudre_equation_deg4(a, b, c, d, e)
  page_precedent = show_page1Equation_4_degre
  show_page_solution()
#page equ 4degre
def show_page1Equation_4_degre():
    global bg_image, entry_a, entry_b, entry_c, entry_d, entry_e
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAG_Equation_4_degre).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre équation",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_text(
    220.0,
    150.0,
    anchor="nw",
    text="a=____.\n\n\nb=____.\n\n\nc=____.\n\n\nd=____.\n\n\ne=____.\n\n  ",
    fill="#000000",
    font=("Inter", 15 )
  )
    # Zone de saisie  centrée dans les espaces attribués aux valeurs
    entry_a = Entry(window, font=("Inter", 14), justify="center")
    entry_b = Entry(window, font=("Inter", 14), justify="center")
    entry_c = Entry(window, font=("Inter", 14), justify="center")
    entry_d = Entry(window, font=("Inter", 14), justify="center")
    entry_e = Entry(window, font=("Inter", 14), justify="center")

    canvas.create_window(273, 160, width=70, height=30, window=entry_a)
    canvas.create_window(273, 231, width=70, height=30, window=entry_b)
    canvas.create_window(273, 296, width=70, height=30, window=entry_c)
    canvas.create_window(273, 365, width=70, height=30,  window=entry_d)
    canvas.create_window(273, 436, width=70, height=30, window=entry_e)


    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page3)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)
    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_equation_deg4)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)

def resolution_systeme():
  global solution, page_precedent
  a1 = float(entry_a1.get())
  b1 = float(entry_b1.get())
  c1 = float(entry_c1.get())
  a2 = float(entry_a2.get())
  b2 = float(entry_b2.get())
  c2 = float(entry_c2.get())

  solution =  resoudre_systeme(a1, b1, c1, a2, b2, c2)
  page_precedent = show_page_Systeme_Equation
  show_page_solution() 
#page systeme equ
def show_page_Systeme_Equation():
    global bg_image, entry_a1, entry_a2, entry_b1, entry_b2, entry_c1, entry_c2
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAGE_Systeme_Equation).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre système d'équations",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_text(
    220.0,
    150.0,
    anchor="nw",
    text="Equation 1:\n\na1=____.\n\nb1=____.\n\nc1=____.\n\nEquation 2:\n\na2=____.\n\nb2=____.\n\nc2=____.\n\n  ",
    fill="#000000",
    font=("Inter", 15 )
    )

    # Zone de saisie  centrée dans les espaces attribués aux valeurs
    entry_a1 = Entry(window, font=("Inter", 14), justify="center")
    entry_b1 = Entry(window, font=("Inter", 14), justify="center")
    entry_c1 = Entry(window, font=("Inter", 14), justify="center")

    entry_a2 = Entry(window, font=("Inter", 14), justify="center")
    entry_b2 = Entry(window, font=("Inter", 14), justify="center")
    entry_c2 = Entry(window, font=("Inter", 14), justify="center")

    canvas.create_window(283, 204, width=70, height=30, window=entry_a1)
    canvas.create_window(283, 251, width=70, height=30, window=entry_b1)
    canvas.create_window(283, 296, width=70, height=30, window=entry_c1)

    canvas.create_window(283, 389, width=70, height=30,  window=entry_a2)
    canvas.create_window(283, 436, width=70, height=30, window=entry_b2)
    canvas.create_window(283, 482, width=70, height=30, window=entry_c2)


    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page3)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_systeme)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)
    
    #page ineq 1degre


def resolution_ineqdegre1():
    global solution, page_precedent
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operateur = relation.get()  
        solution = inequationdegre1 (a,b,operateur)
        
        page_precedent = show_page1Inequation_1_degre
        show_page_solution()
    except ValueError:
        solution = "Erreur : veuillez entrer des nombres valides."
        show_page_solution()


def show_page1Inequation_1_degre():
    global bg_image, entry_a, entry_b, relation
    
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAGE_Inequation_1_degre).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre inéquation",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_text(
    220.0,
    200.0,
    anchor="nw",
    text="a=____.\n\n\nb=____.\n\n  ",
    fill="#000000",
    font=("Inter", 20 )
    )
    entry_a = Entry(window, font=("Inter", 14), justify="center")
    entry_b = Entry(window, font=("Inter", 14), justify="center")
    relation = Entry(window, font=("Inter", 14), justify="center")

    canvas.create_window(280, 216, width=70, height=34, window=entry_a)
    canvas.create_window(280, 312, width=70, height=34, window=entry_b)
    canvas.create_window(280, 490, width=70, height=30, window=relation)

    canvas.create_text(
    220.0,
    430.0,
    anchor="nw",
    text="Choisir la relation (>=, <=, >, <) :",
    fill="#000000",
    font=("Inter", 20 )
)
    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page4)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_ineqdegre1)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)

def resolution_ineq2nd():
    global solution, page_precedent
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        relation_etudie = relation.get()  
        solution = resoudre_ineq2nd(a, b, c, relation_etudie)
        
        page_precedent = show_page1Inequation_2_degre
        show_page_solution()

    except ValueError:
        solution = "Erreur : veuillez entrer des nombres valides."
        show_page_solution()


#page ineq 2degre
def show_page1Inequation_2_degre():
    global bg_image, entry_a, entry_b, entry_c, relation
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAGE_Inequation_2_degre).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre inéquation",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_text(
    220.0,
    200.0,
    anchor="nw",
    text="a=____.\n\n\nb=____.\n\n\nc=____.\n\n  ",
    fill="#000000",
    font=("Inter", 20 )
)
    canvas.create_text(
    220.0,
    430.0,
    anchor="nw",
    text="Choisir la relation (>=, <=, >, <) :",
    fill="#000000",
    font=("Inter", 20 )
)
     # Zone de saisie  centrée dans les espaces attribués aux valeurs
    entry_a = Entry(window, font=("Inter", 14), justify="center")
    entry_b = Entry(window, font=("Inter", 14), justify="center")
    entry_c = Entry(window, font=("Inter", 14), justify="center")
    relation = Entry(window, font=("Inter", 14), justify="center")
   
    
    
    canvas.create_window(280, 216, width=70, height=30, window=entry_a)
    canvas.create_window(280, 312, width=70, height=30, window=entry_b)
    canvas.create_window(280, 409, width=70, height=30, window=entry_c)
    canvas.create_window(280, 490, width=70, height=30, window=relation)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page4)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_ineq2nd)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)


canvas_solution_fonction = None

def resolution_systemineq():
    global solution, page_precedent, canvas_solution_fonction

    if canvas_solution_fonction is not None:
        canvas_solution_fonction.get_tk_widget().destroy()
        canvas_solution_fonction = None

    a1 = float(entry_a1.get())
    b1 = float(entry_b1.get())
    c1 = float(entry_c1.get())
    a2 = float(entry_a2.get())
    b2 = float(entry_b2.get())
    c2 = float(entry_c2.get())
    relation_etudie1 = relation1.get()
    relation_etudie2 = relation2.get()

    solution = resoudre_systemineq(a1, b1, c1, a2, b2, c2, relation_etudie1, relation_etudie2)

    canvas_solution_fonction = FigureCanvasTkAgg(solution, master=window)
    canvas_solution_fonction.draw()
    canvas_solution_fonction.get_tk_widget().place(x=50, y=130, width=800, height=500)

    page_precedent = show_page_Systeme_Inequation
    show_page_solution()


def show_page_Systeme_Inequation():
    global canvas_solution_fonction
    if canvas_solution_fonction is not None:
        canvas_solution_fonction.get_tk_widget().destroy()
        canvas_solution_fonction = None

    global bg_image, entry_a1, entry_a2, entry_b1, entry_b2, entry_c1, entry_c2, relation1, relation2
    canvas.delete("all")

    pil_image = Image.open(IMAGE_PAGE_Systeme_Inequation).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir les coefficients de votre système d'inéquations",
        fill="#000000",
        font=("Inter", 16, "bold")
    )

    canvas.create_text(
        350.0,
        200.0,
        anchor="nw",
        text="Choisir la relation (>=, <=, >, <) :",
        fill="#BC2C2C",
        font=("Inter", 20)
    )

    canvas.create_text(
        350.0,
        390.0,
        anchor="nw",
        text="Choisir la relation (>=, <=, >, <) :",
        fill="#BC2C2C",
        font=("Inter", 20)
    )

    entry_a1 = Entry(window, font=("Inter", 14), justify="center")
    entry_b1 = Entry(window, font=("Inter", 14), justify="center")
    entry_c1 = Entry(window, font=("Inter", 14), justify="center")
    relation1 = Entry(window, font=("Inter", 14), justify="center")

    entry_a2 = Entry(window, font=("Inter", 14), justify="center")
    entry_b2 = Entry(window, font=("Inter", 14), justify="center")
    entry_c2 = Entry(window, font=("Inter", 14), justify="center")
    relation2 = Entry(window, font=("Inter", 14), justify="center")

    canvas.create_window(283, 204, width=70, height=30, window=entry_a1)
    canvas.create_window(283, 251, width=70, height=30, window=entry_b1)
    canvas.create_window(283, 296, width=70, height=30, window=entry_c1)
    canvas.create_window(550, 251, width=70, height=30, window=relation1)

    canvas.create_window(283, 389, width=70, height=30, window=entry_a2)
    canvas.create_window(283, 436, width=70, height=30, window=entry_b2)
    canvas.create_window(283, 482, width=70, height=30, window=entry_c2)
    canvas.create_window(550, 436, width=70, height=30, window=relation2)

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page4)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_systemineq)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)


def resolution_Fonction():
    global solution, label_resultat_fonction, canvas_fig_fonction, canvas_fig_fonction2
    canvas.delete("all")
    
    # Nettoyer les widgets précédents (canvas matplotlib et labels)
    if 'label_resultat_fonction' in globals() and label_resultat_fonction:
        try:
            label_resultat_fonction.destroy()
        except:
            pass
    if 'canvas_fig_fonction' in globals() and canvas_fig_fonction:
        try:
            canvas_fig_fonction.get_tk_widget().destroy()
        except:
            pass
    if 'canvas_fig_fonction2' in globals() and canvas_fig_fonction2:
        try:
            canvas_fig_fonction2.get_tk_widget().destroy()
        except:
            pass

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page2)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    quitter_button = Button(window, text="Quitter", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=window.quit)
    canvas.create_window(900, 600, anchor="se", window=quitter_button)

    canvas.create_text(
        450, 100,
        anchor="center",
        text="SOLUTION DE L'ÉTUDE DE FONCTION",
        fill="#000000",
        font=("Inter", 16, "bold")
    )

    try:
        saisie = entry_fonction.get()
        
        if not saisie.strip():
            solution = "Veuillez entrer une fonction."
            return
        
        # Séparation simple
        parties = saisie.split(',')
        fonction = parties[0].strip()
        point = parties[1].strip() if len(parties) > 1 else "1"
        pt_deriv = parties[2].strip() if len(parties) > 2 else "1"

        # Appel de la fonction
        fig, fig2, solution = Etude_De_Fonction(fonction, point, pt_deriv)
        
        # Affichage du graphique (tableau de variation)
        canvas_fig_fonction2 = FigureCanvasTkAgg(fig2, master=window)
        canvas_fig_fonction2.draw()
        canvas_fig_fonction2.get_tk_widget().place(x=500, y=350, width=400, height=200)

        # Affichage du graphique (tableau de variation)
        canvas_fig_fonction = FigureCanvasTkAgg(fig, master=window)
        canvas_fig_fonction.draw()
        canvas_fig_fonction.get_tk_widget().place(x=50, y=350, width=400, height=200)
        
        # Affichage du texte de résultat avec un Label
        label_resultat_fonction = Label(
            window, 
            text=solution, 
            font=("Arial", 9), 
            justify="left", 
            bg="white",
            wraplength=800,
            anchor="nw"
        )
        label_resultat_fonction._is_resultat_fonction = True  # Marquer pour nettoyage
        label_resultat_fonction.place(x=50, y=150, width=800, height=180)
        
    except Exception as e:
        # En cas d'erreur, afficher un message d'erreur
        error_msg = f"Erreur lors de l'étude de fonction : {str(e)}"
        label_resultat_fonction = Label(
            window, 
            text=error_msg, 
            font=("Arial", 10), 
            justify="left", 
            bg="white",
            fg="red",
            wraplength=800
        )
        label_resultat_fonction._is_resultat_fonction = True
        label_resultat_fonction.place(x=50, y=150, width=800, height=180)
#page etude de fonction
def show_page_fonction():
    global bg_image, entry_fonction, label_resultat_fonction, canvas_fig_fonction, canvas_fig_fonction2
    canvas.delete("all")
    
    # Nettoyer les widgets précédents (canvas matplotlib et labels)
    if 'label_resultat_fonction' in globals() and label_resultat_fonction:
        try:
            label_resultat_fonction.destroy()
            label_resultat_fonction = None
        except:
            pass
    if 'canvas_fig_fonction' in globals() and canvas_fig_fonction:
        try:
            canvas_fig_fonction.get_tk_widget().destroy()
            canvas_fig_fonction = None
        except:
            pass
    if 'canvas_fig_fonction2' in globals() and canvas_fig_fonction2:
        try:
            canvas_fig_fonction2.get_tk_widget().destroy()
            canvas_fig_fonction2 = None
        except:
            pass

    pil_image = Image.open(IMAGE_PAGE_fonction).resize((900, 600))
    bg_image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.create_text(
        450, 100,
        anchor="center",
        text="Veuillez saisir la fonction à étudier",
        fill="#000000",
        font=("Inter", 16, "bold")
    )
    canvas.create_rectangle(
     250, 265, 650, 335,
     fill="#CAC6C5",
     outline=""
    )
    
    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=show_page2)
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    resoudre_button = Button(window, text="Résoudre", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=resolution_Fonction)
    canvas.create_window(900, 600, anchor="se", window=resoudre_button)

    # Zone de saisie  centrée dans le rectangle
    entry_fonction = Entry(
        window,
        font=("Inter", 14),
        justify="center"
    )
    canvas.create_window(450, 300, width= 380, height= 50, window=entry_fonction)



    

#page solution
def show_page_solution():
    global bg_image, solution
    canvas.delete("all")

    #pil_image = Image.open(IMAGE_PAGE_solution).resize((900, 600))
    #bg_image = ImageTk.PhotoImage(pil_image)
    #canvas.create_image(0, 0, image=bg_image, anchor="nw")
     # Fond gris clair
    canvas.create_rectangle(0, 0, 900, 600, fill="#DED9D9", outline="")
    canvas.create_text(
        450, 100,
        anchor="center",
        text="SOLUTION",
        fill="#000000",
        font=("Inter", 32, "bold")
    )

    canvas.create_text(
        450, 300,
        anchor="center",
        text=str(solution),  # ici on affiche le texte de la solution
        fill="#000000",
        font=("Inter", 20, "bold")
    )
    

    retour_button = Button(window, text="Retour", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=lambda: page_precedent())
    canvas.create_window(0, 600, anchor="sw", window=retour_button)

    quitter_button = Button(window, text="Quitter", font=("Inter", 15, "bold"),
                            bg="#D9D9D9", fg="#000000", command=window.quit)
    canvas.create_window(900, 600, anchor="se", window=quitter_button)

show_page1()
window.mainloop()
