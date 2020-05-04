from tkinter import *
import pygame

#interface globale du jeu
def interface():
    global can1, can2, event, start, image_fond, zoom_fond
    #booléens des évents du jeu
    global bool_piece1,bool_piece2,bool_piece3,bool_piece4
    global bool_bquitter, bool_clic2, bool_clic3, bool_clic4, bool_clic5, bool_fantome
    global bool_intervention, bool_invitation, bool_lettre, bv, coffre_actif, coffre_ouvert
    #booléens de l'interface
    global texte_global, notif_in_use, fondmenu, quitter, reglesb

    #2 canvas sont nécessaires
        #premier canvas -> affichage de scene
    can1=Canvas(InterfaceJeu,width=852,height=480,bg='blue')
    can1.place(x=0,y=0)
        #second canvas -> interface d'interaction
    can2=Canvas(InterfaceJeu,width=852,height=320,bg='black')
    can2.place(x=0,y=480)

    texte_global=can2.create_text(220,75,text="",fill="black")
    image_fond=can1.create_image(0,0, anchor="nw")
    zoom_fond=can1.create_image(230,210, anchor="nw")
    can1.itemconfig(image_fond, image=fond)

    #boutons
    start=Button(InterfaceJeu, text="START", command=piece1)
    start.place(x=406,y=575)

    quitter=Button(InterfaceJeu,text="Quitter",command=InterfaceJeu.destroy)
    quitter.place(x=206,y=575)

    reglesb=Button(InterfaceJeu,text="regles",command=regles)
    reglesb.place(x=606,y=575)

    #booleens
    notif_in_use=False
    bv=False
    bool_piece1="False"
    bool_piece2="False"
    bool_piece3="False"
    bool_piece4="False"
    bool_bquitter=False
    bool_clic2=False
    bool_clic3=False
    bool_fantome=False
    bool_clic4=False
    bool_clic5=False
    bool_invitation=False
    bool_lettre=False
    bool_intervention=False
    coffre_actif=False
    coffre_ouvert=False
    '''
    pygame.mixer.music.load("nyan.mp3") # import du fichier
    pygame.mixer.music.play() # on joue le fichier
    pygame.mixer.music.set_volume(0.6) # réglage du volume (facultatif)'''

def regles():
    global can1,fond2,image_fond
    reset_interface()
    retour=Button(InterfaceJeu,text='retour',command=interface)
    retour.place(x=30,y=150)
    enonce=can1.create_text(300,250,text="les regles sont ...",fill="blue")#remplace le print
    can1.itemconfig(image_fond,image=fond_piece1)

def reset_interface(): #fonction utilisée pour changer de scène
    global can1, can2, start, quitter, reglesb
    start.place_forget()  #on enlève les boutons de l'interface de départ
    start.place_forget()
    quitter.place_forget()
    reglesb.place_forget()

#INTERACTIONS ---------------------------------------------------------------------------------- #INTERACTIONS
    #GLOBALES#
def notif(texte,color): #est appelée lorsqu'il faut afficher un texte à l'utilisateur
    global can1, can2, texte_global,notif_in_use
    can2.itemconfig(texte_global,text=texte,fill=color)
    notif_in_use = True

def boutonNotif(): #est appelée en même temps pour afficher le bouton de confirmation de lecture
    global can1, can2, bvalidation, notif_in_use, bv
    bv = True
    if notif_in_use == True:
        bvalidation=Button(InterfaceJeu, text="OK!", command=supprimeNotif)
        bvalidation.place(x=205,y=575)
    else:
        print('EXCEPTION')

def supprimeNotif(): #est appelée après l'usage du bouton pour enlever toute notif
    global bvalidation,notif, notif_in_use, bv
    if notif_in_use == True:
        notif(" ","black")
        if bv == True:
            bvalidation.place_forget()
    notif_in_use = False

def clic(event): #recupère les positions obtenues par objectChecker()
    global clicX,clicY
    clicX=event.x
    clicY=event.y

    #SPÉCIFIQUES#

def presentation_clic(event): #Interactions clic liées à l'arrivée du joueur dans le manoir
    global bool_clic2, bool_clic4, notif ,bool_intervention
    if 293<event.x<335 and 316<event.y<436 :
        notif("Salut ! Je m'appelle Xavier , vers 19h j'etais à mon club de lecture\n On vient tout juste de commencer le dernier tome de Game Of Throne ! ","white")
        boutonNotif()

    if 399<event.x<446 and 304<event.y<442 :
        notif("Je suis Mark Armeau ,\nhier à 19h je suis aller boire un verre pour me changer les idées.","white")
        boutonNotif()

    if 535<event.x<572 and 316<event.y<436 and bool_clic2==False :
        notif("Enchantée , je suis Sophie . Hier , lors de cet effroyable incident ,\n j'etait invitée a un bal dansant...\n d'ailleurs euh... \n Non rien oubliez .","white")
        boutonNotif()
        bool_intervention=True

    if 734<event.x<784 and 322<event.y<433 and bool_clic4==False :
        notif("Bonjour ! Je m'appelle Martine , hier , j'ai passer la journée avec mes petits-fils ", "white")
        boutonNotif()

def quitter1():
    global bquitter1,can2,fantome,notif,bool_clic2,bool_clic3,fantome1,quitter1,bool_fantome
    global bool_clic4,perso6,can1,bool_clic5,bool_invitation,bool_lettre,bool_intervention

    bool_bquitter=True
    notif(" ","black")

    if bool_fantome==True:
        can2.delete("fantome")
        supprimeNotif()
        bquitter1.place_forget()

    if bool_invitation==True:
        can1.delete("invitation")
        can1.create_image(600,300,tags="robe",image=perso5)
        bool_invitation=False
        bquitter1.place_forget()

    if bool_clic3==True:
        fantome1("\t\tAllons voir!")
        bquitter1.place_forget()
        bool_clic3=False

    if bool_lettre==True:
        can1.delete("lettre")
        can1.create_image(320,270,tags="bleu",image=perso6)
        bquitter1.place_forget()
        bool_lettre=False

    if bool_clic5==True:
        fantome1("\t\t\t\t\t\tMartine toujours aussi maladroite cet énigme parle de trois endroits du manoire.\n\t\t\t\t\t\tMais d'abord allons voir ce coffre.")
        bquitter1.place_forget()
        bool_clic5=False

    if bool_intervention==True:
        fantome1("\t\t\t\t\t Sophie perd toujours tout. Elle les retrouve suvent dans le salon sur ta droite.\n\t\t\t\t\tSouvent dans des endroits improbable, il faut aller voir." )
        bquitter1.place_forget()
        bool_intervention=False

def fantome1(texte):
    global can1,bool_piece3,can2,fantome,quitter1,notif,bquitter1,bool_fantome
    can2.create_image(100,100,tags="fantome",image=fantome)
    notif(texte,"blue")
    bquitter1=Button(InterfaceJeu, text="suivant", command=quitter1)
    bquitter1.place(x=745,y=645)
    bool_fantome=True

def clic_coffre(event) :
    global can1,bool_piece4, trouver
    if  0< event.x<73   and  257<event.y<301:
        trouver()
    else:
        print("stop")

def clic2(event) :
    global can1,invitation,fantome1,perso5,bool_clic2,bool_bquitter,notif,bool_clic3,bool_invitation

    if  199<event.x<226 and 285<event.y<295:
        trouver()
        bool_clic2=True
        bool_invitation=True

    elif 580<event.x<642 and 205<event.y<378 and bool_clic2==True:
        notif("\t\t Merci de l'avoir retrouvé maintenant je peux vous faire confiance\n\t\t j'ai vu Martine cacher quelquechose dans un tiroir dans le couloir.","white")
        bool_clic3=True

def clic4(event):
    global bool_clic4,trouver,notif,bool_clic5,bool_lettre
    if 255<event.x<275 and 326<event.y<371:
        bool_clic4=True
        bool_lettre=True
        trouver()
    if 296<event.x<347 and 175<event.y<339 and bool_clic4==True:
        notif("j'avais peur de vous le dire mais j'ai trouvé un coffre fermé dans le piano\n il y avait ecris dessus:\n-mon premier est un recipient où l'on met des fleurs\n -mon second est une fille rousse emprisonnée par un carré marron\n -mon troisième permet d'éclairer et réchauffer la piéce\nJe vous le dis car j'ai fais tomber la feuille dans la cheminée. ","white")
        bool_clic5=True

def trouver():
        global bvoir1,notif
        notif("tu as trouvé quelque chose, veux-tu le voir?","white")
        bvoir1=Button(InterfaceJeu, text="voir", command=voir1)
        bvoir1.place(x=745,y=645)

def voir1():
    global bvoir1,bool_clic2,can1,fantome1,invitation,bool_clic4,lettre,bool_invitation,bool_lettre, coffre_ouvert, coffre_actif
    global zoom_fond, bool_piece4
    bvoir1.place_forget()
    notif(" ","black")
    if coffre_ouvert == False and bool_piece4 == "True":
        notif("Vous avez trouvé un coffre","white")
        can1.itemconfig(zoom_fond,image=coffre_ferme)
        if coffre_ouvert == True:
            notif("Le coffre est déjà ouvert","white")
        elif coffre_actif == False:
            coffre("init")
        elif coffre_actif == True:
            coffre("refresh")

    if bool_invitation==True:
        can1.create_image(300,400,tags="invitation",image=invitation)
        fantome1 ("\t\tbravo tu as trouvé l'invitation allons parler à sophie \n\t\t pour plus d'informations. ")
    if bool_lettre==True:
        can1.create_image(300,400,tags="lettre",image=lettre)
        fantome1("\t\t Elle aurais reçu une lettre de menace. Mais pourquoi?\n\t\t Allons parler à Martine pour plus d'informations. ")

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#hall du manoir
def piece1():
    '''#objectif : le joueur part d'ici, il doit aller vers les autres
    pieces du manoir dans le but de Résoudre des énigmes
       #fonctions à faire : faire fonction pour trouver objet (focus et bind...)'''
    global can1, can2, notif, image_fond
    global bhaut_piece1, bdroit_piece1, bgauche_piece1
    global bool_piece1,perso1,perso2,perso3,perso4, bool_clic2,bool_clic4,presentation_clic

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

    can1.create_image(314,380,tags="perso",image=perso1)
    can1.create_image(420,380,tags="perso",image=perso2)
    can1.create_image(550,380,tags="perso1",image=perso3)
    can1.create_image(760,380,tags="perso2",image=perso4)

    if bool_clic2==False:
        can1.create_image(550,380,tags="perso1",image=perso3)

    elif bool_clic2==True:
        can1.delete("perso1")

    if bool_clic4==False:
        can1.create_image(760,380,tags="perso2",image=perso4)

    elif bool_clic4==True:
        can1.delete("perso2")

    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",presentation_clic)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece1)

def matrice_piece1():
    #tableau des positions des persos
    global can1, can2, bool_piece1
    if bool_piece1 == "True":
        pass #replacer les clicX, clicY
    elif bool_piece1 == "Inactive":
        print("CASTANER")

def reset_piece1(): #fonction utilisée pour changer de scène, on enlève tout
    global bhaut_piece1, bdroit_piece1, bgauche_piece1, supprimeNotif
    global bool_piece1,perso1,perso2,perso3,perso4
    if bool_piece1=="True" or bool_piece1 == "Inactive":
        bhaut_piece1.place_forget()
        bdroit_piece1.place_forget()
        bgauche_piece1.place_forget()
        can1.delete("perso")
        can1.delete("perso1")
        can1.delete("perso2")

        supprimeNotif()
        bool_piece1 = "Inactive"

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#couloir haut du manoir
def piece2():
    global can1, can2, notif, image_fond, bbas_piece2
    global bool_piece2,bool_clic4
    bool_piece2="True"

    #boutons de l'interface dans la piece
    reset_piece1()
    bbas_piece2=Button(InterfaceJeu, text="↓", command=piece1)
    bbas_piece2.place(x=755,y=575)

    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",clic4)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece2)

    pygame.mixer.music.stop()

def reset_piece2():
    global can1, can2, image_fond, bbas_piece2, supprimeNotif
    global bool_piece2
    if bool_piece2=="True" or bool_piece2 == "Inactive":
        bbas_piece2.place_forget()
        supprimeNotif()
        bool_piece2 = "Inactive"

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#salon sous la nuit du manoir
def piece3():
    global can1, can2, notif, image_fond, bgauche_piece3
    global bool_piece3
    bool_piece3="True"
    #boutons de l'interface dans la piece
    reset_piece1()

    bgauche_piece3=Button(InterfaceJeu, text="←", command=piece1)
    bgauche_piece3.place(x=735,y=575)

    if bool_clic2==True:
        can1.create_image(600,300,tags="robe",image=perso5)

        #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece3)
    can1.focus_set()
    can1.bind("<ButtonPress-1>",clic2)


def reset_piece3():
    global bgauche_piece3, supprimeNotif
    global bool_piece3
    if bool_piece3=="True" or bool_piece3 == "Inactive" :
        bgauche_piece3.place_forget()
        supprimeNotif()
        bool_piece3 = "Inactive"
    if bool_clic2==True:
        can1.delete("robe")

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#salle de musique du manoir
def piece4():
    global can1, can2, notif, image_fond, zoom_fond
    global bdroit_piece4, bool_piece4,clic2,clic3,bool_clic2,perso5
    global coffre_ouvert

    bool_piece4="True"

    #boutons de l'interface dans la piece
    reset_piece1()

    bdroit_piece4=Button(InterfaceJeu, text="→", command=piece1)
    bdroit_piece4.place(x=775,y=575)

    if bool_clic2==True:
        can1.create_image(600,300,tags="robe",image=perso5)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece4)
    can1.focus_set()
    can1.bind("<ButtonPress-1>",clic_coffre) #les évenements cliqués seront opposés à la matrice clic_coffre()

    if coffre_actif == True and coffre_ouvert == False:
        notif("Le coffre est déjà sur la table","white")
        can1.itemconfig(zoom_fond,image=coffre_ferme)
        coffre("init")
    if coffre_ouvert == True:
        notif("Le coffre a déjà été ouvert","green") #TROUVER UN MOYEN DE MODIFIER LA TAILLE DES NOTIFS C TROP PETIT (ITEM CONFIG ?, IL Y A UN TUPLE A FAIRE, voir si on peut laisser la police système et changer la taille à sa guise)

#EVENTS LIÉS AU COFFRE
def coffre(mode): #le coffre est l'énigme de la piece, init initialisation du coffre, refresh actualisation du coffre, delete suppression
    global coffre_actif, code_coffre, position_coffre, case_code, haut_code, bas_code, valid_code
    global chiffre0,chiffre1,chiffre2,chiffre3
    global coffre_actif

    if mode == "init":
        code_coffre = [0,0,0,0]
        position_coffre=0
        coffre_actif = True

        #boutons crées ici pour éviter qu'ils ne soient doubles, le mode init étant l'initialisation, il s'applique uniquement au premier appel.
        haut_code=Button(InterfaceJeu, text="↑", command=lambda: inc_coffre(position_coffre,"inc"))
        haut_code.place(x=435,y=515)
        bas_code=Button(InterfaceJeu, text="↓", command=lambda: inc_coffre(position_coffre,"dec"))
        bas_code.place(x=435,y=545)
        case_code=Button(InterfaceJeu, text="→", command=lambda: inc_coffre(position_coffre,"change"))
        case_code.place(x=345,y=565)
        valid_code=Button(InterfaceJeu, text='✅', command=lambda: checkCoffre())
        valid_code.place(x=460,y=530)

        can2.delete('coffre') #on delete les éventuels textes restants de la dernière initialisation

        can2.create_text(350,40,text="Tapez le code.",font=("Tahoma",18),fill="white",tags='coffre')
        can2.create_text(350,65,text=code_coffre[0],font=("Tahoma",16),fill="white",tags=('coffre','chiffre0')) #test avec 2 tags dont un pour appliquer couleut txt spécifiquement
        can2.create_text(370,75,text=code_coffre[1],font=("Tahoma",16),fill="white",tags='coffre')
        can2.create_text(390,65,text=code_coffre[2],font=("Tahoma",16),fill="white",tags='coffre')
        can2.create_text(410,75,text=code_coffre[3],font=("Tahoma",16),fill="white",tags='coffre')

    elif mode == "delete":
        print(code_coffre[0])
        can2.delete('alert')
        can2.delete('coffre')

        haut_code.place_forget()
        bas_code.place_forget()
        case_code.place_forget()
        valid_code.place_forget()

    elif mode == "refresh": #si le coffre est encore actif quand on repasse après
        if coffre_actif == True:
            can2.delete('coffre') #on sort des interactions du coffre (textes...)

            can2.create_text(350,40,text="Tapez le code.",font=("Tahoma",18),fill="white",tags='coffre')
            can2.create_text(350,65,text=code_coffre[0],font=("Tahoma",16),fill="white",tags=('coffre','chiffre0')) #test avec 2 tags dont un pour appliquer couleut txt spécifiquement
            can2.create_text(370,75,text=code_coffre[1],font=("Tahoma",16),fill="white",tags='coffre')
            can2.create_text(390,65,text=code_coffre[2],font=("Tahoma",16),fill="white",tags='coffre')
            can2.create_text(410,75,text=code_coffre[3],font=("Tahoma",16),fill="white",tags='coffre')

def inc_coffre(nb_coffre, incdec): #1er arg position liste code; 2eme arg increm ou decrem ou change pour décaler input
    global code_coffre, position_coffre, case_code
    global chiffre0, chiffre1, chiffre2, chiffre3
    #la fonction gère le système de "déplacement" et de "compteur" du code
    if incdec == 'inc':
        if code_coffre[nb_coffre] < 9:
            can2.delete('coffre')
            code_coffre[nb_coffre]+=1
            print(code_coffre[nb_coffre])
            coffre("refresh")
        else:
            code_coffre[nb_coffre] = 9
            coffre("b")
    elif incdec == 'dec':
        if code_coffre[nb_coffre] > 0:
            can2.delete('coffre')
            code_coffre[nb_coffre] = code_coffre[nb_coffre] - 1
            coffre("refresh")
        else:
            code_coffre[nb_coffre] = 0
            coffre("refresh")
    elif incdec == 'change':
        print("oh")
        if position_coffre < 3:
            position_coffre = position_coffre + 1
            # je redéfinis à chaque fois la position du bouton pour le déplacer sous le chiffre correspondant
            # voir pour descendre le bouton
            if position_coffre == 0:
                x = 345
                y = 565
                case_code.place_configure(x=x, y=y)
                supprimeNotif()
            elif position_coffre == 1:
                x = 365
                y = 565
                case_code.place_configure(x=x, y=y)
                can2.itemconfig('chiffre0',fill='red') #trouver moyen pour couleur
                supprimeNotif()
            elif position_coffre == 2:
                x = 385
                y = 565
                case_code.place_configure(x=x, y=y)
                supprimeNotif()
            elif position_coffre == 3:
                x = 405
                y = 565
                case_code.place_configure(x=x, y=y)
                supprimeNotif()
            else:
                print('salut')

            can2.delete('coffre')
            coffre("refresh")
        else:
            can2.delete("coffre")
            position_coffre = -1
            inc_coffre(position_coffre,"change")
            coffre('refresh')
    else:
        can2.create_text(370,90,text='Un chiffre entre 0 et 9', fill="white",tags='alert')
    print("ehoh")

def checkCoffre(): #fonction appelée pour vérifier le bon résultat du code tapé, n'a besoin que des données du code
    global code_coffre, coffre_ouvert, zoom_fond, can1

    passedcode = 0 #j'ai choisi l'incrémentation pour pouvoir valider en couleur dans le désordre
    if code_coffre[0] == 2:
        passedcode += 1
        #changer couleur chiffre réussi, la couleur est encore à appliquer, ne marche pas
    if code_coffre[1] == 8:
        passedcode +=1
    if code_coffre[2] == 5:
        passedcode +=1
    if code_coffre[3] == 3:
        passedcode +=1

    if passedcode == 4:
        notif("Vous avez trouvé le code !","green")
        coffre_ouvert = True
        coffre_actif = False

        can1.itemconfig(zoom_fond,image=coffre_ouvert_img)
        coffre("delete")
    else:
        notif("Cela n'a pas l'air de marcher","red")

def reset_piece4():
    global bdroit_piece4
    global bool_piece4, coffre_actif, zoom_fond, can1
    if bool_piece4 == "True" or bool_piece4 == "Inactive" :
        bdroit_piece4.place_forget()
        if coffre_actif == True:
            coffre("delete")
            can1.itemconfig(zoom_fond,image=transparent) #image transparente qui remplace le zoom
        supprimeNotif()
        bool_piece4 = "Inactive"

#----- PARTIE EXECUTION DU CODE -----
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

perso1=PhotoImage(file="images/perso/lunette.png")
perso2=PhotoImage(file="images/perso/persovert.png")
perso3=PhotoImage(file="images/perso/robeperso.png")
perso4=PhotoImage(file="images/perso/filleperso.png")
perso5=PhotoImage(file="images/robecluedo2.png")
perso6=PhotoImage(file="images/filleperso2.png")

fond=PhotoImage(file="images/bgmenu.png")
fantome=PhotoImage(file="images/fantome.png")
invitation=PhotoImage(file="images/feuille invitation .png")
lettre=PhotoImage(file="images/feuille lettre.png")
coffre_ferme=PhotoImage(file="images/background-4,1.png")
coffre_ouvert_img=PhotoImage(file="images/background-4,2.png")
transparent=PhotoImage(file="images/transparent.png")

#lancement
pygame.mixer.init()
interface()
InterfaceJeu.mainloop()
