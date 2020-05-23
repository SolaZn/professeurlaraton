from tkinter import *
"""import pygame """

#interface globale du jeu
def interface():
    global can1, can2, event, start, image_fond, zoom_fond
    #booléens des évents du jeu
    global bool_piece1,bool_piece2,bool_piece3,bool_piece4
    global bool_bquitter, bool_clic2, bool_clic3, bool_clic4, bool_clic5, bool_fantome
    global bool_intervention, bool_invitation, bool_lettre, bv, coffre_actif, coffre_ouvert
    global bool_2,bool_5,bool_8,compt,compt1,compt2,bool_indice,tentative,k,n,Gagné,Perdu,bool_quitter,bool_voir,bool_bindice,bool_debut,bool_fin
    #booléens de l'interface
    global texte_global, notif_in_use, fondmenu, quitter, reglesb,texte_global2

    #2 canvas sont nécessaires
        #premier canvas -> affichage de scene
    can1=Canvas(InterfaceJeu,width=852,height=480,bg='blue')
    can1.place(x=0,y=0)
        #second canvas -> interface d'interaction
    can2=Canvas(InterfaceJeu,width=852,height=320,bg='black')
    can2.place(x=0,y=480)

    texte_global=can2.create_text(220,75,text="",fill="black", anchor="nw")
    image_fond=can1.create_image(0,0, anchor="nw")
    zoom_fond=can1.create_image(0,0, anchor="nw")
    can1.itemconfig(image_fond, image=fond)
    texte_global2=can2.create_text(370,210,text="",fill="black")

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
    bool_5=False
    bool_2=False
    bool_8=False
    compt=0
    compt1=0
    compt2=0
    k=0
    bool_indice=False
    tentative=0
    Gagné=False
    Perdu=False
    n=1
    bool_quitter=False
    bool_voir=False
    bool_bindice=False
    bool_debut=False
    bool_fin=False



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
def notif(texte,color,size="normal",posx_txt=220,posy_txt=75,notif_type="discussion",police="TkDefaultFont"): #est appelée lorsqu'il faut afficher un texte non spécial (une notification en gros) à l'utilisateur
    #color : spécifier une couleur en anglais sous forme de string; posx_txt/posy_txt : position en x et y du texte, notif_type : crée un tag pour rendre la suppression plus facile
    #police : donne la police spécifiée au texte, sinon police système
    global can1, can2, texte_global,notif_in_use
    font_size = 25
    if size == "normal":
        font_size = 12
    elif size == "small":
        font_size = 8
    elif size == "big":
        font_size = 18

    can2.itemconfig(texte_global,text=texte,fill=color,font=(police,font_size),tags=notif_type)
    can2.coords(texte_global,posy_txt,posy_txt)
    notif_in_use = True

def boutonNotif(): #est appelée en même temps pour afficher le bouton de confirmation de lecture
    global can1, can2, bvalidation, notif_in_use, bv
    bv = True
    if notif_in_use == True:
        bvalidation=Button(InterfaceJeu, text="OK!", command=supprimeNotif)
        bvalidation.place(x=205,y=620)
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
    global bool_clic2, bool_clic4, notif ,bool_intervention,bouton,n,boutonNotif,trouver,bool_8,bindice1,bool_indice,coffre_ouvert,bembarquer,embarquement,Gagné,Perdu,bool_bindice
    global bool_2,compt,compt1,k,bool_fin
    if 293<event.x<335 and 316<event.y<436 and coffre_ouvert==False :
        notif("Salut ! Je m'appelle Xavier , vers 19h j'etais à mon club de lecture\n On vient tout juste de commencer le dernier tome de Game Of Throne ! ","white")
        bouton()
    elif 293<event.x<335 and 316<event.y<436 and coffre_ouvert==True :
        notif("On l'embarque ?","white")
        Gagné=True
        Perdu=False
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=300,y=550)
            bool_fin=True




    if 399<event.x<446 and 304<event.y<442 and coffre_ouvert==False :
        notif("Je suis Mark Armeau ,\n hier à 19h ? Je suis aller boire un verre pour me changer les idées.","white")
        bouton()
    elif 399<event.x<446 and 304<event.y<442 and coffre_ouvert==True :
        notif("On l'embarque ?","white")
        Perdu=True
        Gagné=False
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=300,y=550)
            bool_fin=True


    if 535<event.x<572 and 316<event.y<436 and bool_clic2==False :
        notif("Enchantée , je suis Sophie . Hier , lors de cet effroyable incident ,\n j'etait invitée a un bal dansant mais j'ai perdu l'invitation...\n d'ailleurs... Non rien oubliez .","white")
        bool_intervention=True
        bouton()
        if n==2:
            notif2("Objectif->Retrouver l'invitation de Sophie pour l'innocenter")
            n+=1


    if 734<event.x<784 and 322<event.y<433 and bool_clic4==False :
        notif("Bonjour ! Je m'appelle Martine . \n Hier ? j'ai passer toute la journée avec mes petits-fils . ", "white")
        bouton()

    if 138<event.x<162 and 263<event.y<293  :
        bool_8=True
        trouver()
        compt+=1
        if bool_indice==True:
            bindice1.place_forget()
            bool_bindice=False
        if compt==1:
            k+=1

    if 592<event.x<617 and 331<event.y<364  :
        bool_2=True
        trouver()
        compt1+=1
        if bool_indice==True:
            bindice1.place_forget()
            bool_bindice=False
        if compt1==1:
            k+=1



def quitter1():
    global bquitter1,can2,fantome,notif,bool_clic2,bool_clic3,fantome1,quitter1,bool_fantome,k
    global bool_clic4,perso6,can1,bool_clic5,bool_invitation,bool_lettre,bool_intervention,bool_8,bool_2,bool_5,n2,n5,n8,indice,bindice1,bool_indice,fincharade,tentative,bool_quitter
    global bool_bindice
    bool_bquitter=True
    notif(" ","black")
    bquitter1.place_forget()
    bool_quitter=False

    if bool_fantome==True:
        can2.delete("fantome")


    if bool_invitation==True:
        can1.delete("invitation")
        can1.create_image(600,300,tags="robe",image=perso5)
        bool_invitation=False


    if bool_clic3==True:
        fantome1("\t\tAllons voir !")

        bool_clic3=False

    if bool_lettre==True:
        can1.delete("lettre")
        can1.create_image(320,270,tags="bleu",image=perso6)

        bool_lettre=False


    if bool_indice==True and k<3 and bool_bindice==False:
        bindice1=Button(InterfaceJeu, text="indice", command=indice)
        bindice1.place(x=20,y=670)
        bool_bindice=True
    elif bool_indice==True and k==3 and tentative==0:

        fincharade()


        bindice1.place_forget()
        bool_indice=False
        tentative=1

    if bool_clic5==True:
        fantome1("\t Martine toujours aussi maladroite cet énigme parle de trois endroits du manoir et d'une soustraction .\n\t Allons chercher ce qu'il y a dans ces endroits je te conseille de prendre une feuille\n\t Si tu ne trouve pas les endroits utilise le bouton indice, il va apparaitre comme par magie .")
        bool_indice=True
        bool_clic5=False

    if bool_intervention==True:
        fantome1(" \t Sophie perd toujours tout. Elle retrouve parfois ses affaires dans le salon sur ta droite.\n\tSouvent dans des endroits improbables sous des meubles, il faut aller voir." )

        bool_intervention=False
    if bool_8==True:
        can1.delete("n8")
        bool_8=False
    if bool_2==True:
        can1.delete("n2")
        bool_2=False
    if bool_5==True:
        can1.delete("n5")
        bool_5=False
    if k==3 and tentative==0:

        fincharade()
        if bool_indice==True:

            bindice1.place_forget()
            bool_indice=False
        tentative=1


def fantome1(texte):
    global can1,bool_piece3,can2,fantome,quitter1,notif,bquitter1,bool_fantome,bouton
    can2.create_image(100,100,tags="fantome",image=fantome)
    notif(texte,"blue")
    bool_fantome=True
    bouton()

def bouton():
    global bquitter1,quitter1,bool_quitter
    if bool_quitter==False:

        bquitter1=Button(InterfaceJeu, text="suivant", command=quitter1)
        bquitter1.place(x=745,y=645)
        bool_quitter=True


def notif2(texte):
    global texte_global2,can2
    can2.itemconfig(texte_global2,text=texte,fill="red")
def objectif() :
    global notif2,bool_intervention,bool_clic3,n
    if n==1:

        notif2("Objectif -> Parler aux suspects")
        n+=1


def clic_coffre(event) :
    global can1,bool_piece4,trouver,coffre_ouvert
    if  0< event.x<73   and  257<event.y<301: #Si on est dans la zone et que le coffre n'a pas été ouvert
        if coffre_ouvert == False:
            trouver()
        elif coffre_ouvert == True:
            notif("Le coffre a déjà été ouvert","green")
    else:
        print("stop")

def clic2(event) :
    global can1,invitation,fantome1,perso5,bool_clic2,bool_bquitter,notif,bool_clic3,bool_invitation,notif2,n,bouton,bool_5,compt2,k,bindice1,bool_indice,bool_bindice

    if  199<event.x<226 and 285<event.y<295 and n==3:
        trouver()
        bool_clic2=True
        bool_invitation=True
    elif  199<event.x<226 and 285<event.y<295 and n>3:
        notif("l'invitation est déjà trouvé","green")

    elif 580<event.x<642 and 205<event.y<378 and bool_clic2==True :
        notif("\t\t Merci de l'avoir retrouvé maintenant je peux vous faire confiance\n\t\t j'ai vu Martine cacher quelque chose dans un tiroir dans le couloir au 1er étage .","white")
        bool_clic3=True
        bouton()
        if n==3:
            notif2("Objectif -> Trouver ce que Martine à cachée dans le tiroir   ")
            n+=1
    if  73<event.x<131 and 218<event.y<309:
        bool_5=True
        trouver()
        compt2+=1
        if bool_indice==True:
            bindice1.place_forget()
            bool_bindice=False
        if compt2==1:
            k+=1


def clic4(event):
    global bool_clic4,trouver,notif,bool_clic5,bool_lettre,n,notif2,bouton
    if 255<event.x<275 and 326<event.y<371:
        bool_clic4=True
        bool_lettre=True
        trouver()
    if 296<event.x<347 and 175<event.y<339 and bool_clic4==True:
        notif("j'avais peur de vous le dire mais j'ai trouvé un coffre fermé dans le piano\n il y avait écrit dessus:\n-mon premier est un récipient où l'on met des fleurs\n -mon second est une fille rousse emprisonnée par un carré marron\n -mon troisième permet d'éclairer et réchauffer la pièce\n -mon quatrième est la soustraction de mon deuxieme par mon troisieme\n-> Mon tout forme le code Je vous le dis car j'ai fait tomber la feuille dans la cheminée. ","white")
        bool_clic5=True

        bouton()
        if n==4:
            notif2("\tObjectif -> Trouver les endroits du manoir dont parle la charade puis ouvrir le coffre")
            n+=1

def trouver():
        global bvoir1,notif,bool_invitation,n,bool_voir

        notif("Tu as trouvé quelque chose, veux-tu le voir ?","white")
        if bool_voir==False:
            bvoir1=Button(InterfaceJeu, text="voir", command=voir1)
            bvoir1.place(x=745,y=645)
            bool_voir=True

def voir1():
    global bvoir1,bool_clic2,can1,fantome1,invitation,bool_clic4,lettre,bool_invitation,bool_lettre, coffre_ouvert, coffre_actif,bouton
    global zoom_fond, bool_piece4,n,n2,n8,n5,bool_5,bool_2,bool_8,bool_voir
    bvoir1.place_forget()
    notif(" ","black")
    bool_voir=False

    if coffre_ouvert == False and bool_piece4 == "True":
        notif("Vous avez trouvé un coffre","white")
        can1.itemconfig(zoom_fond,image=coffre_ferme)
        if coffre_ouvert == True:
            notif("Le coffre est déjà ouvert","white")
        elif coffre_actif == False:
            coffre("init")
        elif coffre_actif == True:
            coffre("refresh")

    if bool_invitation==True and n==3:
        can1.create_image(300,400,tags="invitation",image=invitation)
        fantome1 ("\t\t Bravo tu as trouvé l'invitation allons parler à Sophie \n\t\t pour plus d'informations. ")

    if bool_lettre==True:
        can1.create_image(300,400,tags="lettre",image=lettre)
        fantome1("\t\t Elle aurais reçu une lettre de menace . Mais pourquoi ?\n\t\t Allons parler à Martine pour plus d'informations . ")
    if bool_2==True:
        can1.create_image(300,400,tags="n2",image=n2)
        bouton()
    if bool_8==True:
        can1.create_image(300,400,tags="n8",image=n8)
        bouton()
    if bool_5==True:
        can1.create_image(300,400,tags="n5",image=n5)
        bouton()
def indice():
    global can2,bindince1,premier,deuxieme,troisieme,bdeuxieme,btroisieme,bpremier,bool_indice,notif,bouton,bool_bindice

    bindice1.place_forget()
    bool_bindice=False

    can2.create_text(350,40,text="il vous manque  un indice sur quelle partie de la charade ?",font=("TkDefaultFont",18),fill="white",tags='indice')
    bpremier=Button(InterfaceJeu, text="mon premier", command=premier)
    bpremier.place(x=20,y=550)
    bdeuxieme=Button(InterfaceJeu, text="mon second", command=deuxieme)
    bdeuxieme.place(x=300,y=550)
    btroisieme=Button(InterfaceJeu, text="mon troisième", command=troisieme)
    btroisieme.place(x=600,y=550)

def resetindice() :
    global can2,premier,deuxieme,troisieme,bpremier,btroisieme,bdeuxieme
    can2.delete("indice")
    bpremier.place_forget()
    bdeuxieme.place_forget()
    btroisieme.place_forget()
def premier ():
    global notif,bouton,resetindice
    resetindice()
    notif("l'objet ce trouve proche des escaliers de droite dans le hall ","white")
    bouton()
def deuxieme ():
    global notif,bouton,resetindice
    resetindice()
    notif("l'objet est un tableau ","white")
    bouton()
def troisieme ():
    global notif,bouton,resetindice
    resetindice()
    notif("l'objet ce trouve proche de l'endroit où vous avez trouvé l'invitation de Sophie ","white")
    bouton()

def fincharade():
    global bool_indice,fantome1,bindice1

    fantome1("\t Bravo tu as trouvé les 3 endroits\n\t Maintenant il faut mettre dans l'ordre de la Charade les chiffres que tu as trouvé \n\t Afin de former le mot de passe !  ")
    if bool_indice==True:

        bindice1.place_forget()
        bool_indice=False
def embarquement():
    global Gagné,Perdu,notif,Gagné,image_fond,can1,gagné,bembarquement,reset_piece1,Perdu,perdu,retour,bretourmenu
    notif("   ","white")
    bembarquer.place_forget()
    reset_piece1()
    bretourmenu=Button(InterfaceJeu, text="retour menu", command=retour)
    bretourmenu.place(x=745,y=645)
    if Gagné==True:
        can1.itemconfig(image_fond,image=gagné)
        notif("En effet, il n'etait pas a son club de lecture car il deteste Game Of Throne\n Il a tué Jack car il voulait récupérer son Manoir et l'avoir pour lui tout seul.","white")
    if Perdu==True:
         can1.itemconfig(image_fond,image=perdu)
         notif("il était bien au bar ce soir la d'ailleurs l'odeur le prouvait ","white")
def retour():
   global interface,bretourmenu,notif
   notif(" ","white")
   bretourmenu.place_forget()
   interface()

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#hall du manoir
def piece1():
    '''#objectif : le joueur part d'ici, il doit aller vers les autres
    pieces du manoir dans le but de Résoudre des énigmes
       #fonctions à faire : faire fonction pour trouver objet (focus et bind...)'''
    global can1, can2, notif, image_fond
    global bhaut_piece1, bdroit_piece1, bgauche_piece1
    global bool_piece1,perso1,perso2,perso3,perso4, bool_clic2,bool_clic4,presentation_clic,objectif,bool_debut,fantome1,bouton

    if bool_debut==False:
        fantome1("\t Hey ! Oups désolé de t'avoir fait peur. \n\t Oui oui, c'est moi... Jack, la victime... \n\t Je compte bien t'apporter toute l'aide nécessaire afin de trouver le coupable !")
        bool_debut=True

    objectif()

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
    global bool_piece2,bool_clic4,perso6,bool_clic4
    bool_piece2="True"

    #boutons de l'interface dans la piece
    reset_piece1()
    bbas_piece2=Button(InterfaceJeu, text="↓", command=piece1)
    bbas_piece2.place(x=755,y=575)

    if bool_clic4==True:

        can1.create_image(320,270,tags="bleu",image=perso6)

    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",clic4)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece2)

    pygame.mixer.music.stop()

def reset_piece2():
    global can1, can2, image_fond, bbas_piece2, supprimeNotif,perso6,bool_clic4
    global bool_piece2
    if bool_piece2=="True" or bool_piece2 == "Inactive":
        bbas_piece2.place_forget()


        supprimeNotif()
        bool_piece2 = "Inactive"
    if bool_clic4==True:
        can1.delete("bleu")
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



    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece4)
    can1.focus_set()
    can1.bind("<ButtonPress-1>",clic_coffre) #les évenements cliqués seront opposés à la matrice clic_coffre()

    if coffre_actif == True and coffre_ouvert == False:
        notif("Le coffre est déjà sur la table","white",notif_type="alert")
        '''fantome1("Trouvons le code !")''' #bloque l'affichage de l'alerte
        can1.itemconfig(zoom_fond,image=coffre_ferme)
        coffre("init")
    if coffre_ouvert == True:
        notif("Le coffre a déjà été ouvert","green",size="big",notif_type="alert")
        '''fantome1("Tu devrais jeter un oeil ailleurs")  #fantome notifie utilisateur de la fin de l'énigme''' #à vérifier mais ça bloque l'affichage des alertes notifs

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

        can2.create_text(350,40,text="Tapez le code.",font=("TkDefaultFont",18),fill="white",tags='coffre')
        can2.create_text(350,65,text=code_coffre[0],font=("TkDefaultFont",16),fill="white",tags=('coffre','chiffre0')) #test avec 2 tags dont un pour appliquer couleut txt spécifiquement
        can2.create_text(370,75,text=code_coffre[1],font=("TkDefaultFont",16),fill="white",tags='coffre')
        can2.create_text(390,65,text=code_coffre[2],font=("TkDefaultFont",16),fill="white",tags='coffre')
        can2.create_text(410,75,text=code_coffre[3],font=("TkDefaultFont",16),fill="white",tags='coffre')

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

            can2.create_text(350,40,text="Tapez le code.",font=("TkDefaultFont",18),fill="white",tags='coffre')
            can2.create_text(350,65,text=code_coffre[0],font=("TkDefaultFont",16),fill="white",tags=('coffre','chiffre0')) #test avec 2 tags dont un pour appliquer couleut txt spécifiquement
            can2.create_text(370,75,text=code_coffre[1],font=("TkDefaultFont",16),fill="white",tags='coffre')
            can2.create_text(390,65,text=code_coffre[2],font=("TkDefaultFont",16),fill="white",tags='coffre')
            can2.create_text(410,75,text=code_coffre[3],font=("TkDefaultFont",16),fill="white",tags='coffre')

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
    global code_coffre, coffre_ouvert, zoom_fond, can1 ,n,notif2

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
        notif("Vous avez trouvé le code !","green",size="big")
        coffre_ouvert = True
        coffre_actif = False

        can1.itemconfig(zoom_fond,image=coffre_ouvert_img)
        coffre("delete")
        if n==5:
            notif2("Objectif -> Embarquer le coupable")

    else:
        notif("Cela n'a pas l'air de fonctionner","red")

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
coffre_ferme=PhotoImage(file="images/background-4,2.png")
coffre_ouvert_img=PhotoImage(file="images/background-4,1.png")
transparent=PhotoImage(file="images/transparent.png")
n2=PhotoImage(file="images/2.png")
n8=PhotoImage(file="images/8.png")
n5=PhotoImage(file="images/5.png")
gagné=PhotoImage(file="images/fond fin gagne.png")
perdu=PhotoImage(file="images/fond fin perdu.png")
#lancement
"""pygame.mixer.init()"""
interface()
'''InterfaceJeu.wm_state(newstate="zoomed")''' #mets le jeu en plein écran
InterfaceJeu.title('233rd Roland Street; Affair for the Night Team') #change le titre du jeu
InterfaceJeu.mainloop()
