# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:43:01 2022
@author: emma.begard & audery.nicolle

Ce fichier contient la classe player qui permet de gérer les actions du joueur.
"""
#Import -----------------------------------------------------------------------

import projectile as pj
from PIL import Image, ImageTk

#Classe -----------------------------------------------------------------------

class Player :
    
    def __init__(self,window, canvas):
        """ 
        Cette classe permet de gérer les actions propres du joueur soit :
                - de le faire bouger latéralement.
                - de gérer sa vie et leur affichage.
                - tirer sur les ennemis
                
        
        Parameters : 
            window : la fenetre du jeu (tk)
            canvas : la zone de jeu où s'affiche le méchant
            self.__x : position sur l'axe des abscices (int)
            self.__y : position sur l'axe des ordonnées (int)
            self.vel : vélocité du joueur (int)
            self.image : image du joueur (objet canvas)
            self.yeti : contiendra l'image du joueur quand la partie demarrera 
                        (int ou objetc canvas)
            self.projectiles : contient tous les projectiles tirer par le joueur
                                (lst)
            self.nb_vie : contiendra les vies du joueur (list d'objet canvas)
            self.im_coeur : image d'une vie (objet tk)
            self.thermos_bu : contient un objet canvas, bonus, ou non (lst)
            self.resistance : permet de savoir si le joueur est resistant au
                                boule de feu (int).
        """
        self.x = 400
        self.y = 600
        self.vel = 10
        self.canvas = canvas
        self.window = window
        self.image = Image.open("Image/yeti.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((70,70))) 
        self.yeti = 0 
        self.projectile = []
        self.nb_vie = []
        self.im_coeur = Image.open("Image/coeur.png")
        self.redi_image1 = ImageTk.PhotoImage(self.im_coeur.resize((50,50)))
        self.thermos_bu = []
        self.resistance = 0
        
   
    def move_right(self, evt):
        """ 
        Cette méthode permet de déplacer le joeur à droite.
        
        Parameters : 
            evt : variable utilisé dans la fonction key_event => window.bind (str)
            
        Returns : none
        """
        if self.x < 950 :
            self.x += self.vel
            self.canvas.move(self.yeti, self.vel, 0)
            
            if self.thermos_bu != []:
                self.canvas.move(self.thermos_bu[0],self.vel,0)
            
        
    def move_left(self, evt):
        """ 
        Cette méthode permet de déplacer le joeur à gauche.
        
        Parameters : 
            evt : variable utilisé dans la fonction key_event => window.bind (str)
            
        Returns : none
        """
        if self.x  > 50 :
            self.x += -self.vel
            self.canvas.move(self.yeti, -self.vel, 0)
            
            if self.thermos_bu != []:
                self.canvas.move(self.thermos_bu[0],-self.vel,0)
        
    def crea_projectile (self, evt):
        """ 
        Cette méthode permet de créer un projectile que lorsque le projectile 
        précédent n'existe plus.
        
        Parameters : 
            evt : variable utilisé dans la fonction key_event => window.bind (str)
            
        Returns : none
        """
        # comme on ne peut avoir que 1 projectile à l'écran 
        if len(self.projectile) <= 0:
            self.projectile.append( pj.Projectile(self.x, self.y, self.canvas,\
                                                   "Image/rocher.png", -1,0) )
            self.projectile[-1].run(self.projectile)
           

    def key_event(self):
        """
        Cette méthode permet de gérer les actions de clavier : déplacement à 
        droite et gauche, tir.
        
        Parameters : none
        
        Returns : none 
        """
        #self.window.bind('evenement', fonction à appliquer si l'évènement arrive)
        self.window.bind('<Right>', self.move_right)
        self.window.bind('<Left>', self.move_left)
        self.window.bind('<space>', self.crea_projectile)
        self.canvas.focus_set()
    
    def crea_vie (self) :
        """ 
        Cette méthode permet de créer la barre de trois coeur de vie du joueur.
        
        Parameters : None
        
        Returns : none
        """
        #Initialisation
        i = 0
        x = 750

        while i < 3 : 
             
            vie = self.canvas.create_image( x,680, image = self.redi_image1 )
            self.nb_vie.append((vie,x))
            i += 1
            x += 70

    def gestion_vie (self, type_D_B) :
        """
        Cette méthode permet de gérer la vie du joueur. On peut soit ajouter 
        une vie soit en retirer une.
        
        Parameters : 
            type_D_B : permet de savoir s'il faut enlever ou ajouter une vie (int)
            
        Returns : None

        """

        #Condition pour enlever de la vie, (on vérfie qu'on peut tjs en enlever)
        if type_D_B == -1 and self.nb_vie != [] :
            self.canvas.delete(self.nb_vie[0][0])
            del self.nb_vie[0] 
        
        #Condition pour ajouter de la vie, (on vérfie qu'on a moins de 3 vies)
        elif type_D_B == 1 and len(self.nb_vie) < 3 :
           
            #la position selon x dépend de celle de l'ojet avant celui que 
            #l'on va ajouter dans self.nb_vie
            vie = self.canvas.create_image( self.nb_vie[0][1] - 70,680,\
                                                 image = self.redi_image1 )
            self.nb_vie.append((vie,self.nb_vie[-1][1] + 70))
    
    def tout(self):
        """
        Cette méthode permet de créer l'image du joueur et d'appeler la fonction
        qui permet de connaître les actions au clavier.
        
        Parameters : none.
        
        Returns : none.
        """
        
        self.yeti = self.canvas.create_image(self.x,self.y, \
                                             image = self.redi_image )
        self.key_event()


