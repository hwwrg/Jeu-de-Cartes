from random import shuffle, randint, choice
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
    def Tire(self, cartes_shuffle):
        self.num = randint(0, len(self.cartes)-1)
        # random.choice()
        self.f = cartes_shuffle[self.num][0]
        self.c = cartes_shuffle[self.num][1]

    #Afficher la carte et créer objets f et c
    def Affichage(self):
        self.carte_tir = str(self.f) + " de " + self.c


##test = JeudDeCarte()
##test.Melange()
##test.Tire()
##test.Affichage()


class Joker(JeudDeCarte):
    """hériter Classe JeuDeCarte et ajouter 2 joker"""

    def __init__(self):
        JeudDeCarte.__init__(self)
        self.cartes = self.cartes + ['Joker Un', 'Joker Deux']

#Créer la fenêtre
root = Tk()
root.geometry("900x500")


def melange():
    global cartes_shuffle

    #Intanciation de la class
##    jeu = JeudDeCarte()
    jeu = Joker()
    jeu.Melange()
    cartes_shuffle = jeu.cartes

    carte_Affi.delete("1.0", END)
    carte_Affi.insert(END, cartes_shuffle)

def tire():

    #Intanciation de la class
##    jeu = JeudDeCarte()
    jeu = Joker()
    print(cartes_shuffle)
    jeu.Tire(cartes_shuffle)
    jeu.Affichage()


# Bug avec Entry : 2 valeurs affichées emsemble dans toutes les 2 cases
##    cart_Tire_No_Entry.delete(0, END)
##    cart_Tire_Affi_Entry.delete(0, END)
##    cart_Tire_No_Entry.insert(END, "No.{}".format(jeu.num+1))
##    cart_Tire_Affi_Entry.insert(END, jeu.carte_tir)


    cart_Tire_No_Label = Label(root, text="No.{}".format(jeu.num+1))
    cart_Tire_Affi_Label = Label(root, text=jeu.carte_tir)
    cart_Tire_No_Label.grid(row=5, column=0)
    cart_Tire_Affi_Label.grid(row=5, column=1, columnspan=2)


def main():
    global carte_Affi
    global cart_Tire_No_Entry
    global cart_Tire_Affi_Entry

    #Intanciation de la class
##    jeu = JeudDeCarte()
    jeu = Joker()

    #Créer interface
    carte_Label = Label(root, text="Les cartes mélangées sont : ")
    cart_Tire_Label = Label(root, text = "Votre carte est : ")
    mel_Boutton = Button(root, text="Mélanger", command=melange)
    tire_Boutton = Button(root, text="Tirer", command=tire)
    exit_Bouton = Button(root, text = "Quit", command=root.destroy)


    carte_Affi = Text(root, width=100, height=10)
    carte_Affi.grid(row=1, column=0, rowspan=3, columnspan=3)
    carte_Affi.insert(END, jeu.cartes)

    cart_Tire_No_Label = Label(root, text=" ")
    cart_Tire_Affi_Label = Label(root, text=" ")
    cart_Tire_No_Label.grid(row=5, column=0)
    cart_Tire_Affi_Label.grid(row=5, column=1, columnspan=2)

    # Bug avec Entry : 2 valeurs affichées emsemble dans toutes les 2 cases
##    cart_Tire_No_Entry = Entry(root, text = "  ")
##    cart_Tire_Affi_Entry = Entry(root, text = "  ") #, width=70)
##    cart_Tire_No_Entry.grid(row=5, column=0)
##    cart_Tire_Affi_Entry.grid(row=5, column=1, columnspan=2)

    carte_Label.grid(row=0, column=0)
    cart_Tire_Label.grid(row=4, column=0)
    mel_Boutton.grid(row=6, column=0)
    tire_Boutton.grid(row=6, column=1)
    exit_Bouton.grid(row=6, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()