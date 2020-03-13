from tkinter import *
import pygame

#interface globale du jeu
def interface():
    global can1, can2, event, start, image_fond
    global bool_piece1,bool_piece2,bool_piece3,bool_piece4
    global texte_global

    #2 canvas sont nécessaires
        #premier canvas -> affichage de scene
    can1=Canvas(InterfaceJeu,width=852,height=480,bg='blue')
    can1.place(x=0,y=0)
        #second canvas -> interface d'interaction
    can2=Canvas(InterfaceJeu,width=852,height=320,bg='black')
    can2.place(x=0,y=480)

    texte_global=can2.create_text(220,75,text="",fill="black")
    image_fond=can1.create_image(0,0, anchor="nw")

    #boutons
    start=Button(InterfaceJeu, text="START", command=piece1)
    start.place(x=406,y=575)

    #booleens
    notif_in_use=False
    bool_piece1="False"
    bool_piece2="False"
    bool_piece3="False"
    bool_piece4="False"
    '''
    pygame.mixer.music.load("nyan.mp3") # import du fichier
    pygame.mixer.music.play() # on joue le fichier
    pygame.mixer.music.set_volume(0.6) # réglage du volume (facultatif)'''


def reset_interface(): #fonction utilisée pour changer de scène
    global can1, can2, start
    start.place_forget()  #on enlève les boutons de l'interface

def notif(texte,color):
    global can1, can2, texte_global,notif_in_use
    can2.itemconfig(texte_global,text=texte,fill=color)

def boutonNotif():
    global can1, can2, bvalidation, notif_in_use
    print("Ici")
    notif_in_use = True
    bvalidation=Button(InterfaceJeu, text="OK!", command=supprimeNotif)
    bvalidation.place(x=350,y=580) #enlever bouton event texte


def supprimeNotif():
    global bvalidation,notif, notif_in_use
    if notif_in_use == True:
        notif(" ","black")
        bvalidation.place_forget()
        notif_in_use = False

def clic(event): #test position pour zones de clic avec if else
    global clicX,clicY
    clicX=event.x
    clicY=event.y

def objectChecker(nom_piece):
    #donner la position d'appui de l'utilisateur pour déterminer si il a cliqué sur l'image
    global can1, can2
    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",clic)

#hall du manoir
def piece1():
    '''#objectif : le joueur part d'ici, il doit aller vers les autres
    pieces du manoir dans le but de Résoudre des énigmes
       #fonctions à faire : faire fonction pour trouver objet (focus et bind...)'''
    global can1, can2, notif, image_fond
    global bhaut_piece1, bdroit_piece1, bgauche_piece1
    global bool_piece1

    bool_piece1="True"
    #boutons de l'interface dans la piece
    reset_interface()
    reset_piece2()
    reset_piece3()
    reset_piece4()

    bhaut_piece1=Button(InterfaceJeu, text="↑", command=piece2)
    bhaut_piece1.place(x=755,y=515)
    bdroit_piece1=Button(InterfaceJeu, text="→", command=piece3)
    bdroit_piece1.place(x=775,y=575)
    bgauche_piece1=Button(InterfaceJeu, text="←", command=piece4)
    bgauche_piece1.place(x=735,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece1)

    #interactions de la piece

        #on va opposer l'event à la matrice
    matrice_piece1()

    #discussions de la piece
    texte_piece1="Bonjour mec"
    notif(texte_piece1,"white")
    boutonNotif()

def matrice_piece1():
    #tableau des positions des persos
    global can1, can2, bool_piece1
    if bool_piece1 == "True":
        pass #replacer les clicX, clicY
    elif bool_piece1 == "Inactive":
        print("CASTANER")

def reset_piece1(): #fonction utilisée pour changer de scène, on enlève tout
    global can1, can2, bhaut_piece1, bdroit_piece1, bgauche_piece1
    global bool_piece1
    if bool_piece1=="True" or bool_piece1 == "Inactive":
        bhaut_piece1.place_forget()
        bdroit_piece1.place_forget()
        bgauche_piece1.place_forget()
        bool_piece1 = "Inactive"

#couloir haut du manoir
def piece2():
    global can1, can2, notif, image_fond, bbas_piece2
    global bool_piece2
    bool_piece2="True"

    #boutons de l'interface dans la piece
    reset_piece1()
    bbas_piece2=Button(InterfaceJeu, text="↓", command=piece1)
    bbas_piece2.place(x=755,y=575)

    matrice_piece1()

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece2)

    pygame.mixer.music.stop()

def reset_piece2():
    global can1, can2, image_fond, bbas_piece2,bool_piece2
    global bool_place2
    if bool_piece2=="True" or bool_piece2 == "Inactive":
        bbas_piece2.place_forget()
        bool_piece2 = "Inactive"

#salon sous la nuit du manoir
def piece3():
    global can1, can2, notif, image_fond, bgauche_piece3
    global bool_piece3
    bool_piece3="True"
    #boutons de l'interface dans la piece
    reset_piece1()

    bgauche_piece3=Button(InterfaceJeu, text="←", command=piece1)
    bgauche_piece3.place(x=735,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece3)

def reset_piece3():
    global can1, can2, image_fond, bgauche_piece3,bool_piece3
    global bool_place3
    if bool_piece3=="True" or bool_piece3 == "Inactive" :
        bgauche_piece3.place_forget()
        bool_piece3 = "Inactive"

#salle de musique du manoir
def piece4():
    global can1, can2, notif, image_fond
    global bdroit_piece4, bool_piece4
    bool_piece4=True

    #boutons de l'interface dans la piece
    reset_piece1()

    bdroit_piece4=Button(InterfaceJeu, text="→", command=piece1)
    bdroit_piece4.place(x=775,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece4)


def reset_piece4():
    global can1, can2, image_fond
    global bdroit_piece4,bool_piece4
    if bool_piece4 == "True" or bool_piece4 == "Inactive" :
        bdroit_piece4.place_forget()
        bool_piece4 = "Inactive"

#creation fenetre graphique
InterfaceJeu=Tk()
InterfaceJeu.geometry('852x700')
#importation des images
fond_piece1=PhotoImage(file="images/background-1.png")
fond_piece2=PhotoImage(file="images/background-2.png")
fond_piece3=PhotoImage(file="images/background-3.png")
fond_piece4=PhotoImage(file="images/background-4.png")
clicX=0
clicY=0

#initialisatoin des boutons

#lancement
pygame.mixer.init()
interface()
InterfaceJeu.mainloop()
