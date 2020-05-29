from tkinter import *
from tkinter import messagebox
import pygame

#interface globale du jeu
def interface():
    global can1, can2, event, start, image_fond, zoom_fond, icone_perso
    #booléens des évents du jeu
    global bool_piece1,bool_piece2,bool_piece3,bool_piece4
    global bool_bquitter, bool_clic2, bool_clic3, bool_clic4, bool_clic5, bool_fantome
    global bool_intervention, bool_invitation, bool_lettre, bv, coffre_actif, coffre_ouvert
    global bool_2,bool_5,bool_8,compt,compt1,compt2,bool_indice,tentative,k,n,Gagné,Perdu,bool_quitter,bool_voir,bool_bindice, bool_regles, bool_debut,bool_fin
    global Perdu1, Perdu2,bool_coffre,bool_cle,bool_tir,bool_clé,bool_coffre2
    #booléens de l'interface
    global texte_global, notif_in_use, fondmenu, quitter, texte_global2

    #2 canvas sont nécessaires
        #premier canvas -> affichage de scene
    can1=Canvas(InterfaceJeu,width=852,height=480,bg='blue')
    can1.place(x=0,y=0)
        #second canvas -> interface d'interaction
    can2=Canvas(InterfaceJeu,width=852,height=320,bg='black')
    can2.place(x=0,y=480)

    texte_global=can2.create_text(220,75,text="",fill="black", anchor="nw")
    texte_global2=can2.create_text(370,200,text="",fill="black", anchor="center")
    image_fond=can1.create_image(0,0, anchor="nw")
    zoom_fond=can1.create_image(0,0, anchor="nw")
    can1.itemconfig(image_fond, image=fond)

    icone_perso=can1.create_image(0,330, anchor="nw", tags="icone")

    #boutons
    start=Button(InterfaceJeu, text="Commencer", command=regles)
    start.place(x=376,y=515)

    quitter=Button(InterfaceJeu,text="Quitter",command=on_closing)
    quitter.place(x=391,y=560)

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
    bool_regles=False
    bool_debut=False
    bool_fin=False
    Perdu1=False
    Perdu2=False
    bool_coffre=False
    bool_cle=False
    bool_tir=False
    bool_clé=False
    bool_coffre2=False

    pygame.mixer.music.load("music/theme.mp3") # import du fichier
    pygame.mixer.music.play(loops=-1) # on joue le fichier
    pygame.mixer.music.set_volume(0.6) # réglage du volume (facultatif)"""

def regles(x="1"):
    global can1,fond2,image_fond, brief2, returnb, bool_regles, start
    reset_interface()
    bool_regles == True
    if x == "1":
        returnb=Button(InterfaceJeu,text='retour',command=interface)
        returnb.place(x=30,y=150)
        can1.itemconfig(image_fond,image=regles1)
        brief2=Button(InterfaceJeu, text="Suite du briefing", command=lambda: regles("2"))
        brief2.place(x=376,y=575)
    elif x == "2":
        can1.itemconfig(image_fond,image=regles2)
        returnb.place_forget()
        returnb=Button(InterfaceJeu,text='retour',command=lambda: regles("1"))
        returnb.place(x=30,y=150)
        brief2.place_forget()
        start=Button(InterfaceJeu, text="Allons enquêter", command=piece1)
        start.place(x=376,y=575)
    else:
        print("Mais par où êtes vous bien passé ?")

def reset_interface(): #fonction utilisée pour changer de scène
    global can1, can2, start, quitter, brief2, returnb, bool_regles
    start.place_forget()  #on enlève les boutons de l'interface de départ
    quitter.place_forget()

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
    print(clicX,clicY)

    #SPÉCIFIQUES#

def presentation_clic(event): #Interactions clic liées à l'arrivée du joueur dans le manoir
    global bool_clic2, bool_clic4, notif ,bool_intervention,bouton,n,boutonNotif,trouver,bool_8,bindice1,bool_indice,coffre_ouvert,bembarquer,embarquement,Gagné,Perdu,bool_bindice
    global bool_2,compt,compt1,k, icone_perso, bool_fin,Perdu1,Perdu2

    if 293<event.x<335 and 316<event.y<436 and coffre_ouvert==False :
        notif("Salut ! Je m'appelle Xavier Molingé. Vers 19 heures, j'étais à mon club de lecture\n On vient tout juste de commencer le dernier tome de Game Of Thrones ! ","white")
        bouton()
        can1.itemconfig(icone_perso,image=icone_perso1)
         #affiche le perso
    elif 293<event.x<335 and 316<event.y<436 and coffre_ouvert==True :
        notif("Alors inspecteur, \non embarque Xavier Molingé ? \nIl dit être allé à son club de lecture !","white")
        Gagné=True
        Perdu=False
        Perdu2=False
        Perdu1=False
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=300,y=550)
            bool_fin=True

    if 399<event.x<446 and 304<event.y<442 and coffre_ouvert==False :
        notif("Je suis Mark Armeau,\nhier à 19h je suis allé boire un verre pour me changer les idées.","white")
        bouton()
        can1.itemconfig(icone_perso, image=icone_perso2)
    elif 399<event.x<446 and 304<event.y<442 and coffre_ouvert==True :
        notif("Alors inspecteur, \non embarque Mark Armeau ? \nIl dit être parti boire un verre.","white")
        Perdu=True
        Gagné=False
        Perdu2=False
        Perdu1=False
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=350,y=550)
            bool_fin=True

    if 535<event.x<572 and 316<event.y<436 and bool_clic2==False and coffre_ouvert==False:
        can1.itemconfig(icone_perso, image=icone_perso3)
        notif("Enchantée, je suis Sophie Daprès-Silva. Hier, lors de cet effroyable incident,\nj'étais invitée à un bal dansant mais j'ai perdu l'invitation...\nD'ailleurs... \nNon rien oubliez...","white")
        bool_intervention=True
        bouton()
        if n==2:
            notif2("Objectif -> Retrouver l'invitation de Sophie pour l'innocenter")
            n+=1
    elif 535<event.x<572 and 316<event.y<436 and bool_clic2==False and coffre_ouvert==True:
            notif("Alors inspecteur \n on embarque Sophie?\nelle dit etre allée à un bal","white")
            Perdu=False
            Gagné=False
            Perdu2=True
            Perdu1=False
            if bool_fin==False:
                bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
                bembarquer.place(x=350,y=550)
                bool_fin=True

    if 734<event.x<784 and 322<event.y<433 and bool_clic4==False and coffre_ouvert==False:
        notif("Bonjour ! Je m'appelle Martine Alaplaghe. Hier, j'ai passé toute la journée avec mes petits fils ", "white")
        can1.itemconfig(icone_perso, image=icone_perso4)
        bouton()
    elif 734<event.x<784 and 322<event.y<433 and bool_clic4==False and coffre_ouvert==True:
        notif("Alors inspecteur\non embarque Martine ?\n elle dit qu'elle était avec ses petits-enfants","white")
        Perdu=False
        Gagné=False
        Perdu2=False
        Perdu1=True
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=350,y=550)
            bool_fin=True

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
    global bquitter1,can2,fantome,notif,bool_clic2,bool_clic3,fantome1,quitter1,bool_fantome,k, icone_perso
    global bool_clic4,perso6,can1,bool_clic5,bool_invitation,bool_lettre,bool_intervention,bool_8,bool_2,bool_5,n2,n5,n8,indice,bindice1,bool_indice,fincharade,tentative,bool_quitter
    global bool_bindice,bool_coffre,bool_tir,bool_clé
    bool_bquitter=True
    notif(" ","black")
    bquitter1.place_forget()
    bool_quitter=False
    can1.itemconfig(icone_perso,image=transparent)

    if bool_fantome==True:
        can2.delete("fantome")

    if bool_invitation==True:
        can1.delete("invitation")
        can1.create_image(600,300,tags="robe",image=perso5)
        bool_invitation=False

    if bool_clic3==True:
        fantome1("Allons voir!")
        bool_clic3=False

    if bool_lettre==True:
        can1.delete("lettre")
        can1.create_image(320,270,tags="bleu",image=perso6)

        bool_lettre=False
    if bool_tir==True:
        fantome1("Une clé ? Martine adore les cheminées. \nPeut-etre que la clé est proche d'une cheminée.")
        bool_tir=False
    if bool_clé==True:
        can1.delete("cle")
        bool_clé=False

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
        fantome1("Martine, toujours aussi maladroite... \nCette énigme parle de trois endroits du manoir et d'une soustraction.\nAllons chercher ce qu'il y a dans ces endroits. Je te conseille de prendre une feuille !\nSi tu ne trouves pas les réponses demande-moi un peu d'aide, je t'accompagnerai.")
        bool_indice=True
        bool_clic5=False

    if bool_intervention==True:
        fantome1("Sophie perd toujours tout. Ce qu'elle perd, elle le retrouve souvent dans le salon \nsur ta droite. Souvent d'ailleurs, dans des endroits improbables... \nSous des meubles... Il faut aller voir." )
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
    if bool_coffre==True:
        fantome1("Tu as ouvert le coffre bien joué ! \nRegarde bien le coffre, mais qui est donc le coupable ? \nJe pense que tu as tous les indices en main pour trouver le coupable.\nEmbarque celui qui m'a tué !")
        bool_coffre=False


def fantome1(texte):
    global can1,bool_piece3,can2,fantome,quitter1,notif,bquitter1,bool_fantome,bouton, icone_perso
    notif(texte,"blue")
    bool_fantome=True
    can1.itemconfig(icone_perso,image=fantome)
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
    global can1,bool_piece4,trouver,coffre_ouvert,bool_clé,bool_cle,bool_coffre2,n,notif
    if  0< event.x<73   and  257<event.y<301 and bool_cle == True: #Si on est dans la zone et que le coffre n'a pas été ouvert
        if coffre_ouvert == False:
            trouver()
            bool_coffre2=True
        elif coffre_ouvert == True:
            notif("Le coffre a déjà été ouvert","green")

    if 692<event.x<727 and 112<event.y<130 and n<=4:
        bool_clé=True
        bool_cle=True
        trouver()
    if 692<event.x<727 and 112<event.y<130 and n>4:
        notif("La clé a déja été trouvée","green")


def clic2(event) :
    global can1,invitation,fantome1,perso5,bool_clic2,bool_bquitter,notif,bool_clic3,bool_invitation,notif2,n,bouton,bool_5,compt2,k,bindice1,bool_indice,bool_bindice, icone_perso, coffre_ouvert
    global Gagné,Perdu,Perdu1,Perdu2,bool_fin,bembarquer,embarquement

    if  199<event.x<226 and 285<event.y<295 and n<=3:
        trouver()
        bool_clic2=True
        bool_invitation=True
    elif  199<event.x<226 and 285<event.y<295 and n>3:
        notif("L'invitation a déjà été trouvée","green")

    if 580<event.x<642 and 205<event.y<378 and bool_clic2==True and coffre_ouvert==False :
        notif("Merci de l'avoir retrouvée ! Maintenant je peux vous faire confiance...\nJ'ai vu Martine cacher quelque chose dans un tiroir dans le couloir \ndu haut en revenant des toilettes.","white", posx_txt=0)
        can1.itemconfig(icone_perso, image=icone_perso3)
        bool_clic3=True
        bouton()
        if n==3:
            notif2("Objectif -> Trouver ce que Martine a caché dans le tiroir d'en haut")
            n+=1
    if 580<event.x<642 and 205<event.y<378 and bool_clic2==True and coffre_ouvert==True :
        notif("Alors inspecteur, \non embarque Sophie ?\nElle dit être allée à un bal.","white")
        Perdu=False
        Gagné=False
        Perdu2=True
        Perdu1=False
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=350,y=550)
            bool_fin=True

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
    global bool_clic4,trouver,notif,bool_clic5,bool_lettre,n,notif2,bouton, icone_perso
    global Gagné,Perdu,Perdu1,Perdu2,bool_fin,bembarquer,embarquement,coffre_ouvert,bool_cle,bool_tir,n

    if 255<event.x<275 and 326<event.y<371 and bool_cle==True and n<=4:
        bool_clic4=True
        bool_lettre=True
        trouver()
    elif 255<event.x<275 and 326<event.y<371 and bool_cle==False and n<=4:
        notif("Le tiroir est fermé, il faut trouver la clé","white")
        bool_tir=True
        bouton()
    elif 255<event.x<275 and 326<event.y<371 and bool_cle==True and n>4:
        notif("La lettre a déja été trouvé","green")

    if 296<event.x<347 and 175<event.y<339 and bool_clic4==True and coffre_ouvert==False:
        can1.itemconfig(icone_perso, image=icone_perso4)
        notif("J'avais peur de vous le dire mais j'ai trouvé un coffre fermé dans le mécanisme du piano\n Dessus, ces mots:\n - Mon premier est un recipient où l'on met des fleurs\n - Mon deuxième est une fille rousse emprisonnée dans un cadre marron\n - Mon troisième permet à la fois d'éclairer et réchauffer la piéce\n - Mon quatrième est la soustraction de mon deuxieme par mon troisieme\n -> Mon tout forme un code. J'aurais bien voulu vous le donner \nmais quelqu'un a pris le papier contenant le code dans mon bureau et l'a mis dans la cheminée.","white",posy_txt=35, posx_txt=75)
        bool_clic5=True

        bouton()
        if n==4:
            notif2("Objectif -> Trouver les endroits du manoir dont parle la charade puis ouvrir le coffre")
            n+=1

    if 296<event.x<347 and 175<event.y<339 and bool_clic4==True and coffre_ouvert==True:
        notif("Alors inspecteur,\non embarque Martine ?\n Elle dit qu'elle était avec ses petits-enfants au moment du meurtre","white")
        Perdu=False
        Gagné=False
        Perdu2=False
        Perdu1=True
        if bool_fin==False:
            bembarquer=Button(InterfaceJeu, text="embarquer", command=embarquement)
            bembarquer.place(x=350,y=550)
            bool_fin=True

def trouver():
        global bvoir1,notif,bool_invitation,n,bool_voir

        notif("Tu as trouvé quelque chose, veux-tu le voir ?","white")
        if bool_voir==False:
            bvoir1=Button(InterfaceJeu, text="voir", command=voir1)
            bvoir1.place(x=745,y=645)
            bool_voir=True

def voir1():
    global bvoir1,bool_clic2,can1,fantome1,invitation,bool_clic4,lettre,bool_invitation,bool_lettre, coffre_ouvert, coffre_actif,bouton
    global zoom_fond, bool_piece4,n,n2,n8,n5,bool_5,bool_2,bool_8,bool_voir,bool_clé,clé,bool_coffre2
    bvoir1.place_forget()
    notif(" ","black")
    bool_voir=False

    if coffre_ouvert == False and bool_piece4 == "True" and bool_coffre2==True:
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
        fantome1 ("Bravo tu as trouvé l'invitation ! Allons parler à Sophie \npour plus d'informations. ")

    if bool_lettre==True:
        can1.create_image(300,400,tags="lettre",image=lettre)
        fantome1("Elle aurait reçu une lettre de menace... Mais pourquoi ?\nAllons parler à Martine pour plus d'informations. ")
    if bool_2==True:
        can1.create_image(300,400,tags="n2",image=n2)
        bouton()
    if bool_8==True:
        can1.create_image(300,400,tags="n8",image=n8)
        bouton()
    if bool_5==True:
        can1.create_image(300,400,tags="n5",image=n5)
        bouton()
    if bool_clé==True:
        can1.create_image(300,420,tags="cle",image=clé)
        fantome1("Bravo tu as trouvé la clé.\nAllons voir ce qu'il y a dans ce tiroir !")

def indice():
    global can2,bindince1,premier,deuxieme,troisieme,bdeuxieme,btroisieme,bpremier,bool_indice,notif,bouton,bool_bindice,bretour1,retour1

    bindice1.place_forget()
    bool_bindice=False

    can2.create_text(350,40,text="Il vous manque un indice sur quelle partie de la charade?",font=("TkDefaultFont",18),fill="white",tags='indice')
    bpremier=Button(InterfaceJeu, text="Mon premier", command=premier)
    bpremier.place(x=20,y=550)
    bdeuxieme=Button(InterfaceJeu, text="Mon deuxieme", command=deuxieme)
    bdeuxieme.place(x=300,y=550)
    btroisieme=Button(InterfaceJeu, text="Mon troisieme", command=troisieme)
    btroisieme.place(x=600,y=550)
    bretour1=Button(InterfaceJeu, text="retour", command=retour1)
    bretour1.place(x=745,y=645)

def resetindice() :
    global can2,premier,deuxieme,troisieme,bpremier,btroisieme,bdeuxieme,bretour1
    can2.delete("indice")
    bpremier.place_forget()
    bdeuxieme.place_forget()
    btroisieme.place_forget()
    bretour1.place_forget()
def premier ():
    global notif,bouton,resetindice
    resetindice()
    notif("L'objet se trouve proche des escaliers de droite dans le hall.","white")
    bouton()
def deuxieme ():
    global notif,bouton,resetindice
    resetindice()
    notif("L'objet est un tableau... Logique non ?","white")
    bouton()
def troisieme ():
    global notif,bouton,resetindice
    resetindice()
    notif("L'objet ne se trouve pas si loin que ça de l'endroit où vous avez trouvé l'invitation de Sophie ","white")
    bouton()

def fincharade():
    global bool_indice,fantome1,bindice1

    fantome1("Bravo! Tu as trouvé les 3 endroits.\nMaintenant, il faut mettre dans l'ordre de la charade les chiffres que tu as trouvé \nafin de former le code du coffre dans le piano !")
    if bool_indice==True:
        bindice1.place_forget()
        bool_indice=False
def retour1():
    global resetindice,bool_bindice,bindice,indice,quitter1
    resetindice()
    quitter1()

def embarquement():
    fin()

def retour():
   global interface,bretourmenu,notif
   notif(" ","white")
   bretourmenu.place_forget()
   can1.delete("credits")
   interface()

def souris (event):
    global bool_clic2,bool_clic4,n
    if 293<event.x<335 and 316<event.y<436 or 399<event.x<446 and 304<event.y<442 or 535<event.x<572 and 316<event.y<436 and bool_clic2==False or 734<event.x<784 and 322<event.y<433 and bool_clic4==False or 138<event.x<162 and 263<event.y<293 and n>=5 or n>=5 and 592<event.x<617 and 331<event.y<364  :
        InterfaceJeu.config(cursor="hand1")
        InterfaceJeu.update_idletasks
    else :
        InterfaceJeu.config(cursor="arrow")
        InterfaceJeu.update_idletasks
def souris2(event):
    global n,bool_clic2
    if 199<event.x<226 and 285<event.y<295 and n>=3 or 580<event.x<642 and 205<event.y<378 and bool_clic2==True or 73<event.x<131 and 218<event.y<309 and n>=5 :
        InterfaceJeu.config(cursor="hand1")
        InterfaceJeu.update_idletasks
    else :
        InterfaceJeu.config(cursor="arrow")
        InterfaceJeu.update_idletasks
def souris3(event):
    global bool_clic4, n
    if 255<event.x<275 and 326<event.y<371 and n>=4 or 296<event.x<347 and 175<event.y<339 and bool_clic4==True:
        InterfaceJeu.config(cursor="hand1")
        InterfaceJeu.update_idletasks
    else :
        InterfaceJeu.config(cursor="arrow")
        InterfaceJeu.update_idletasks
def souris4(event):
    global n
    if  0< event.x<73   and  257<event.y<301 and n>=5 or 692<event.x<727 and 112<event.y<130 and n>=4:
        InterfaceJeu.config(cursor="hand1")
        InterfaceJeu.update_idletasks
    else :
        InterfaceJeu.config(cursor="arrow")
        InterfaceJeu.update_idletasks
def reset_bouton():
    global bool_fin,bembarquer
    if bool_fin==True:
        bembarquer.place_forget()
        bool_fin=False

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#hall du manoir
def piece1():
    '''#objectif : le joueur part d'ici, il doit aller vers les autres
    pieces du manoir dans le but de Résoudre des énigmes'''
    global can1, can2, notif, image_fond
    global bhaut_piece1, bdroit_piece1, bgauche_piece1, returnb
    global bool_piece1,perso1,perso2,perso3,perso4, bool_clic2,bool_clic4,presentation_clic,objectif, bool_debut,fantome1,bouton,souris,reset_bouton

    objectif()
    bool_piece1="True"
    #boutons de l'interface dans la piece
    reset_interface()
    returnb.place(x=6000,y=6000)
    reset_piece2()
    reset_piece3()
    reset_piece4()
    reset_bouton()

    if bool_debut==False:
        fantome1("Hey ! Oups désolé de t'avoir fait peur. \nOui oui, c'est moi... Jack, la victime... \nJe compte bien t'apporter toute l'aide nécessaire afin de trouver le coupable !")
        bool_debut=True

        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/puzzles.mp3")
        pygame.mixer.music.play(loops=-1)

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
    can1.bind("<Motion>",souris)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece1)

def reset_piece1(): #fonction utilisée pour changer de scène, on enlève tout
    global bhaut_piece1, bdroit_piece1, bgauche_piece1, supprimeNotif, bembarquer
    global bool_piece1,perso1,perso2,perso3,perso4, icone_perso, coffre_ouvert, bool_fin
    if bool_piece1=="True" :
        bhaut_piece1.place_forget()
        bdroit_piece1.place_forget()
        bgauche_piece1.place_forget()
        can1.delete("perso")
        can1.delete("perso1")
        can1.delete("perso2")
        can1.itemconfig(icone_perso, image=transparent)
        supprimeNotif()
        bool_piece1 = "Inactive"

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#couloir haut du manoir
def piece2():
    global can1, can2, notif, image_fond, bbas_piece2
    global bool_piece2,bool_clic4,perso6,bool_clic4,souris3,reset_bouton
    bool_piece2="True"

    #boutons de l'interface dans la piece
    reset_piece1()
    reset_bouton()
    bbas_piece2=Button(InterfaceJeu, text="↓", command=piece1)
    bbas_piece2.place(x=755,y=575)

    if bool_clic4==True:

        can1.create_image(320,270,tags="bleu",image=perso6)

    can1.focus_set() #test clic zones
    can1.bind("<ButtonPress-1>",clic4)
    can1.bind("<Motion>",souris3)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece2)

def reset_piece2():
    global can1, can2, image_fond, bbas_piece2, supprimeNotif,perso6,bool_clic4
    global bool_piece2, icone_perso, bool_fin, coffre_ouvert, bembarquer
    if bool_piece2=="True" :
        bbas_piece2.place_forget()
        supprimeNotif()
        bool_piece2 = "Inactif"
    if bool_clic4==True:
        can1.delete("bleu")
    can1.itemconfig(icone_perso, image=transparent)

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#salon sous la nuit du manoir
def piece3():
    global can1, can2, notif, image_fond, bgauche_piece3
    global bool_piece3,souris2,reset_bouton
    bool_piece3="True"
    #boutons de l'interface dans la piece
    reset_piece1()
    reset_bouton()
    bgauche_piece3=Button(InterfaceJeu, text="←", command=piece1)
    bgauche_piece3.place(x=735,y=575)

    if bool_clic2==True:
        can1.create_image(600,300,tags="robe",image=perso5)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece3)
    can1.focus_set()
    can1.bind("<ButtonPress-1>",clic2)
    can1.bind("<Motion>",souris2)


def reset_piece3():
    global bgauche_piece3, supprimeNotif
    global bool_piece3, icone_perso, bool_fin, coffre_ouvert, bembarquer
    if bool_piece3=="True"  :
        bgauche_piece3.place_forget()
        supprimeNotif()
        bool_piece3 = "Inactive"
    if bool_clic2==True:
        can1.delete("robe")
    can1.itemconfig(icone_perso, image=transparent)

#PIECE ------------------------------------------------------------------------------------------------------------------------- #PIECE
#salle de musique du manoir
def piece4():
    global can1, can2, notif, image_fond, zoom_fond
    global bdroit_piece4, bool_piece4,clic2,clic3,bool_clic2,perso5
    global coffre_ouvert,souris4,reset_bouton

    bool_piece4="True"

    #boutons de l'interface dans la piece
    reset_piece1()
    reset_bouton()

    bdroit_piece4=Button(InterfaceJeu, text="→", command=piece1)
    bdroit_piece4.place(x=775,y=575)

    #fond de la piece
    can1.itemconfig(image_fond,image=fond_piece4)
    can1.focus_set()
    can1.bind("<ButtonPress-1>",clic_coffre)#les évenements cliqués seront opposés à la matrice clic_coffre()
    can1.bind("<Motion>",souris4)

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

def checkCoffre(): #fonction appelée pour vérifier le bon résultat du code tapé, n'a besoin que des données du code
    global code_coffre, coffre_ouvert, zoom_fond, can1 ,n,notif2,bouton,bool_coffre

    passedcode = 0 #j'ai choisi l'incrémentation pour pouvoir valider en couleur dans le désordre
    if code_coffre[0] == 2:
        passedcode += 1
        #changer couleur chiffre mouais, la couleur pourraît être appliquée, ne marche pas
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
        bouton()
        bool_coffre=True
        if n==5:
            notif2("Objectif -> Embarquer le coupable entre les 4 suspects")

    else:
        notif("Cela n'a pas l'air de fonctionner","red")

def reset_piece4():
    global bdroit_piece4, bool_fin, bembarquer, coffre_ouvert
    global bool_piece4, coffre_actif, zoom_fond, can1, icone_perso
    if bool_piece4 == "True"  :
        bdroit_piece4.place_forget()
        if coffre_actif == True:
            coffre("delete")
            can1.itemconfig(zoom_fond,image=transparent) #image transparente qui remplace le zoom
        supprimeNotif()
        bool_piece4 = "Inactive"
    can1.itemconfig(icone_perso, image=transparent)

def fin():
    global Gagné,Perdu,notif,Gagné,image_fond,can1,gagné,bembarquement,reset_piece1,Perdu,perdu,retour,bretourmenu, Perdu1,Perdu2, bcredits, bquitter
    notif("   ","white")
    bembarquer.place_forget()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("music/theme.mp3")
    pygame.mixer.music.play(loops=-1)

    reset_piece1()
    reset_piece2()
    reset_piece3()
    reset_piece4()

    notif2(" ",)
    bretourmenu=Button(InterfaceJeu, text="Recommencer", command=retour)
    bretourmenu.place(x=725,y=505)
    bcredits=Button(InterfaceJeu, text="Crédits", command=affcredits)
    bcredits.place(x=725,y=555)
    bquitter=Button(InterfaceJeu,text="Quitter",command=on_closing)
    bquitter.place(x=725,y=605)
    if Gagné==True:
        can1.itemconfig(image_fond,image=gagné)
        notif("En effet, il n'était pas à son club de lecture... \nApparemment, il déteste Game Of Thrones (pauvre de lui...)\nIl a tué Jack, le propriétaire, juste après le dîner \ncar il voulait récupérer son manoir et l'avoir pour lui tout seul.","white")
    if Perdu2==True:
        can1.itemconfig(image_fond,image=perdu)
        notif("Mais tu n'as pas trouvé l'invitation ?! Elle était innocente.\nElle part en prison tandis que le vrai tueur \ncours toujours !","white")
    if Perdu1==True:
        can1.itemconfig(image_fond,image=perdu)
        notif("Mais tu n'as pas trouvé la lettre ?! Que vont penser ses petits-enfants ?\nLeur grand-mère est en prison et le vrai tueur \ncours toujours !","white")
    if Perdu==True:
        can1.itemconfig(image_fond,image=perdu)
        notif("Il était bien au bar ce soir là, d'ailleurs l'odeur le prouvait. \nApparemment, il aime bien la boisson. \nIl part en prison tandis que le vrai tueur \ncours toujours !","white")

def affcredits():
    global bcredits, image_fond, bquitter
    bcredits.place_forget()
    bquitter.place(x=725,y=555)
    notif("   ","white")
    can1.itemconfig(image_fond,image=img_credits)

def on_closing():
    global bool_fin
    if bool_fin == False:
        if messagebox.askokcancel("Quitter le jeu", "Voulez-vous quitter le jeu ? Votre progression ne sera pas sauvegardée."):
            pygame.mixer.music.stop()
            pygame.quit()
            InterfaceJeu.destroy()
    elif bool_fin == True:
        if messagebox.askokcancel("Quitter le manoir", "Merci sincèrement d'avoir joué ! Voulez-vous quitter le manoir ? Il saura toujours vous accueillir."):
            pygame.mixer.music.stop()
            pygame.quit()
            InterfaceJeu.destroy()

#----- PARTIE EXECUTION DU CODE -----
#creation fenetre graphique
InterfaceJeu=Tk()
InterfaceJeu.geometry('852x700')
InterfaceJeu.protocol("WM_DELETE_WINDOW", on_closing)

#importation des images
fond_piece1=PhotoImage(file="images/background-1.png")
fond_piece2=PhotoImage(file="images/background-2.png")
fond_piece3=PhotoImage(file="images/background-3.png")
fond_piece4=PhotoImage(file="images/background-4.png")
regles1=PhotoImage(file="images/regles/regles1.png")
regles2=PhotoImage(file="images/regles/regles2.png")
clicX=0
clicY=0

perso1=PhotoImage(file="images/perso/lunette.png")
icone_perso1=PhotoImage(file="images/perso/icones/lunettecluedo1.png")
perso2=PhotoImage(file="images/perso/persovert.png")
icone_perso2=PhotoImage(file="images/perso/icones/vertcluedo1.png")
perso3=PhotoImage(file="images/perso/robeperso.png")
icone_perso3=PhotoImage(file="images/perso/icones/robecluedo1.png")
perso4=PhotoImage(file="images/perso/filleperso.png")
icone_perso4=PhotoImage(file="images/perso/icones/fillecluedo1.png")
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
clé=PhotoImage(file="images/key.png")
img_credits=PhotoImage(file="images/fond_credits.png")

#lancement
pygame.init()
interface()
'''InterfaceJeu.wm_state(newstate="zoomed")''' #mets le jeu en plein écran
InterfaceJeu.title('Detective Larathon and The Phantom Menace') #change le titre du jeu
InterfaceJeu.mainloop()