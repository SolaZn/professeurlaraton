from tkinter import *

#interface globale du jeu
def interface():
    global can1, can2, event, start, image_fond

    #2 canvas sont nécessaires
        #premier canvas -> affichage de scene
    can1=Canvas(InterfaceJeu,width=852,height=480,bg='blue')
    can1.place(x=0,y=0)
        #second canvas -> interface d'interaction
    can2=Canvas(InterfaceJeu,width=852,height=320,bg='black')
    can2.place(x=0,y=480)

    image_fond=can1.create_image(0,0, anchor="nw")

    #boutons
    start=Button(InterfaceJeu, text="START", command=piece1)
    start.place(x=406,y=575)

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
    #boutons de l'interface dans la piece
    reset_interface()

    bhaut_piece1=Button(InterfaceJeu, text="↑", command=piece2)
    bhaut_piece1.place(x=755,y=515)
    bdroit_piece1=Button(InterfaceJeu, text="→", command=piece3)
    bdroit_piece1.place(x=775,y=575)
    bgauche_piece1=Button(InterfaceJeu, text="←", command=piece4)
    bgauche_piece1.place(x=735,y=575)
    
    can1.create_image(314,380,image=perso1)
    can1.create_image(420,380,image=perso2)
    can1.create_image(550,380,image=perso3)
    can1.create_image(760,380,image=perso4)
  

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece1)

    #interactions de la piece
    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",clic)

def reset_piece1(): #fonction utilisée pour changer de scène, on enlève tout
    global can1, can2, bhaut_piece1, bdroit_piece1, bgauche_piece1
    bhaut_piece1.place_forget()
    bdroit_piece1.place_forget()
    bgauche_piece1.place_forget()


#couloir haut du manoir
def piece2():
    global can1, can2, notif, image_fond, bbas_piece2

    #boutons de l'interface dans la piece
    reset_interface()
    reset_piece1()

    bbas_piece2=Button(InterfaceJeu, text="↓", command=piece1)
    bbas_piece2.place(x=755,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece2)

def reset_piece2():
    global can1, can2, image_fond, bbas_piece2
    bbas_piece2.place_forget()

#salon sous la nuit du manoir
def piece3():
    global can1, can2, notif, image_fond

    #boutons de l'interface dans la piece
    reset_interface()
    reset_piece1()

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece3)

#salle de musique du manoir
def piece4():
    global can1, can2, notif, image_fond

    #boutons de l'interface dans la piece
    reset_interface()
    reset_piece1()

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece4)

#creation fenetre graphique
InterfaceJeu=Tk()
InterfaceJeu.geometry('852x700')
#importation des images
fond_piece1=PhotoImage(file="images/background-1.png")
fond_piece2=PhotoImage(file="images/background-2.png")
fond_piece3=PhotoImage(file="images/background-3.png")
fond_piece4=PhotoImage(file="images/background-4.png")
perso1=PhotoImage(file="lunette.png")
perso2=PhotoImage(file="persovert.png")
perso3=PhotoImage(file="robeperso.png")
perso4=PhotoImage(file="filleperso.png")

#lancement
interface()
InterfaceJeu.mainloop()
