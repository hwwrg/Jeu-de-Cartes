"""
Cart
52 carte
    couleurs : trèfle, carreau, cœur, pique
    figures : rois, dames, valets, As, 2-10
mélange carte
tirer carte
afficher carte
"""

from random import shuffle, randint
from tkinter import *

# shuffle : mélanger
# randint(int1, int2) : renvoie un nombre entier tiré aléatoirement entre int1 inclus et int2 inclus.

##import random

class JeudDeCarte:
    """Mélanger les carte et en tirer une"""

    # Consructeur
    def __init__(self):
        """ Créer liste de 52 cartes"""
        # listes figure et couleur
        listNum = []
        for i in range(2,11):
            listNum.append(i)
        self.figure = ["Roi", "Dame", "Valet", "As"] + listNum

        self.couleur = ["Trèfle", "Carreau", "Cœur", "Pique"]

        #liste cartes
        self.cartes = []
        for c in self.couleur:
            for f in self.figure:
                self.tmp = (f,c)
                self.cartes.append(self.tmp)

    #Mélanger les cartes
    def Melange(self):
        shuffle(self.cartes)

    #Tirer une carte aléatoirement
    def Tire(self):
        self.num = randint(0, len(self.cartes)-1)
        self.f = self.cartes[self.num][0]
        self.c = self.cartes[self.num][1]

    #Afficher la carte et créer objets f et c
    def Affichage(self):
        self.c = str(self.f) + " de " + self.c


##test = JeudDeCarte()
##test.Melange()
##test.Tire()
##test.Affichage()

#Créer la fenêtre
root = Tk()
root.geometry("900x500")


def melange():
    jeu = JeudDeCarte()
    jeu.Melange()
    catre_Affi = Label(root, text = jeu.cartes[:3])
    catre_Affi.grid(row=1, column=0, rowspan = 3 )

def tire():
    jeu = JeudDeCarte()
    jeu.Tire()
    jeu.Affichage()
    cart_Tire_Affi_Label = Label(root, text = jeu.c)
    cart_Tire_Affi_Label.grid(row=5, column=0)

def main():

    #Intanciation de la class
    jeu = JeudDeCarte()

    #Créer interface
    carte_Label = Label(root, text="Les cartes mélangées sont : ")
    cart_Tire_Label = Label(root, text = "Votre carte est : ")
    mel_Boutton = Button(root, text="Mélanger", command=melange)
    tire_Boutton = Button(root, text="Tirer", command=tire)
    exit_Bouton = Button(root, text = "Quit", command=root.destroy)

    carte_Label.grid(row=0, column=0)
    cart_Tire_Label.grid(row=4, column=0)
    mel_Boutton.grid(row=6, column=0)
    tire_Boutton.grid(row=6, column=1)
    exit_Bouton.grid(row=6, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()