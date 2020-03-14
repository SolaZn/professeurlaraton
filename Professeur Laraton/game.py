from tkinter import *


#interface globale du jeu
def interface():
    global can1, can2, event, start, image_fond, fondmenu,quitter,regles
    global bool_piece1,bool_piece2,bool_piece3,bool_piece4

    #2 canvas sont nécessaires
        #premier canvas -> affichage de scene
    can1=Canvas(InterfaceJeu,width=1920,height=600)
    can1.place(x=0,y=0)
    image_fondmenu=can1.create_image(0,0, image=fond, anchor="nw")

        #second canvas -> interface d'interaction
    can2=Canvas(InterfaceJeu,width=852,height=320,bg='black')
    can2.place(x=0,y=480)

    image_fond=can1.create_image(0,0, anchor="nw")

    #boutons
    start=Button(InterfaceJeu, text="START", command=piece1)
    start.place(x=406,y=575)
    quitter=Button(InterfaceJeu,text="Quitter",command=InterfaceJeu.destroy)
    quitter.place(x=206,y=575)
    regles=Button(InterfaceJeu,text="regles",command=regles)
    regles.place(x=606,y=575)

    #booleens piece
    bool_piece1=False
    bool_piece2=False
    bool_piece3=False
    bool_piece4=False

def reset():
    global can1,bou1,bou2,bou3,fond2
    start.place_forget()
    quitter.place_forget()
    regles.place_forget()
    retour=Button(InterfaceJeu,text='retour',comand=interface)
    bou4.place(x=30,y=150)


def regles():
    global can1,fond2,image_fond
    reset()
    enonce=can1.create_text(300,250,text="les regles sont ...",fill="blue")#remplace le print

    can1.itemconfig(image_fond,image=fond_piece1)




def reset_interface(): #fonction utilisée pour changer de scène
    global can1, can2, start
    start.place_forget()  #on enlève les boutons de l'interface

def clic(event): #test position pour zones de clic avec if else
    print(event.x,event.y)

#hall du manoir
def piece1():
    '''#objectif : le joueur part d'ici, il doit aller vers les autres
    pieces du manoir dans le but de Résoudre des énigmes
       #fonctions à faire : reset_interface() -> fait
       faire fonction pour trouver objet (focus et bind...)
       enlever les boutons en venant des autres pieces'''
    global can1, can2, notif, image_fond
    global bhaut_piece1, bdroit_piece1, bgauche_piece1
    global bool_piece1

    bool_piece1=True
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
    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",clic)

def reset_piece1(): #fonction utilisée pour changer de scène, on enlève tout
    global can1, can2, bhaut_piece1, bdroit_piece1, bgauche_piece1
    if bool_piece1==True :
        bhaut_piece1.place_forget()
        bdroit_piece1.place_forget()
        bgauche_piece1.place_forget()


#couloir haut du manoir
def piece2():
    global can1, can2, notif, image_fond, bbas_piece2
    global bool_piece2
    bool_piece2=True

    #boutons de l'interface dans la piece
    reset_piece1()
    bbas_piece2=Button(InterfaceJeu, text="↓", command=piece1)
    bbas_piece2.place(x=755,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece2)

def reset_piece2():
    global can1, can2, image_fond, bbas_piece2,bool_piece2
    if bool_piece2==True :
        bbas_piece2.place_forget()

#salon sous la nuit du manoir
def piece3():
    global can1, can2, notif, image_fond, bgauche_piece3
    global bool_piece3
    bool_piece3=True
    #boutons de l'interface dans la piece


    reset_piece1()

    bgauche_piece3=Button(InterfaceJeu, text="←", command=piece1)
    bgauche_piece3.place(x=735,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece3)

def reset_piece3():
    global can1, can2, image_fond, bgauche_piece3,bool_piece3
    if bool_piece3==True :
        bgauche_piece3.place_forget()

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
    if bool_piece4==True :
        bdroit_piece4.place_forget()

#creation fenetre graphique
InterfaceJeu=Tk()
InterfaceJeu.geometry('852x700')
#importation des images
fond_piece1=PhotoImage(file="images/background-1.png")
fond_piece2=PhotoImage(file="images/background-2.png")
fond_piece3=PhotoImage(file="images/background-3.png")
fond_piece4=PhotoImage(file="images/background-4.png")
fond=PhotoImage(file="images/bgmenu.png")
#initialisatoin des boutons

#lancement
interface()
InterfaceJeu.mainloop()
