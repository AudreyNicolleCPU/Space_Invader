# Space_Invader 

*-- Français --*

Ce dossier contient le projet du space invader revisité. Les règles du jeu sont affichées dans la commande options - à propos, de la fenêtre du jeu lorsque vous démarrez le programme. Ce projet est composé d'un fichier principal, le ficher **class_fenetre.py**. En effet, le programme principal qui permet de créer un objet de la classe **Fenetre**, qui, elle, permet de lancer le jeu en appuyant sur le bouton jouer. Ainsi, pour mettre en route le programme, il faut exécuter ce fichier.

Les différentes entités de ce jeu soit les méchants (normaux ou méchant bonus), les projectiles (boule de feu, rocher, projectile secret ou les bonus), les îlots et le joueur sont chacun associés à une classe 'mère' avec potentiellement des classes 'fille'. Ces classes 'mère' sont, chacune, associées à un fichier qui porte leur nom. Les objets de ces classes sont utilisés et liés entre eux dans la classe **Fenêtre**, par exemple les collisions qui sont l'interaction de deux entités différentes sont gérées dans la classe **Fenetre**. Les interactions qui sont propres aux entités elles-mêmes sont gérées par leur classe, par exemple le fait de bouger le joueur est géré par la classe **Player**.

Méthodes récusives : 
    - dans le fichier class_fenetre : - gestion_tir_M_bonus
                                      - bad_daddy_is_comming
                                      - gestion_fin_de_vie_EHPHAD
                                      - on_prepare_un_bonus
                                      - action_bonus
                                      - gestion_collisions
                                      - move_papa
                                      - move_groupe
                                      - update_score

Implémentation de listes : 
     - dans la classe **Fenetre** : - méthode __init__ : self.enemy, 
                                             self.lst_ilot,self.lst_bonus
     - dans la classe **Player** :  - méthode __init__ : self.nb_vie,
                                     self.projectile, self.thermos_bu
     - dans la classe **Ilot** :  - méthode __init__ : self.lst_carre
     - dans la classe **Mechant** :  - méthode __init__ : self.projectile
               
                                      
Toutes les images utilisées sont libre de droit ou bien leur utilisation a été validé par la personne concernée.

Auteurs : Emma BEGARD et Audrey NICOLLE 


*-- English --*

This folder contains the space invader revisited project. The rules of the game are displayed in the command options - à propos, of the game window when you start the program. This project is composed of a main file, the file **class_fenetre.py**. The main program that allows you to create an object of the class **Fenetre**, which allows you to launch the game by pressing the play button. Thus, to start the program, it is necessary to execute this file.

The different entities of this game, i.e. the bad guys (normal or bonus bad guys), the projectiles (fireball, rock, secret projectile or bonuses), the islands and the player are each associated with a 'mother' class with potentially 'daughter' classes. These 'mother' classes are each associated with a file bearing their name. The objects of these classes are used and linked together in the **Fenetre** class, e.g. collisions which are the interaction of two different entities are handled in the **Fenetre** class.Interactions which are specific to the entities themselves are handled by their class, e.g. moving the player is handled by the **Player** class.


Recusive methods : 
    - in the class_fenetre file : - gestion_tir_M_bonus
                                  - bad_daddy_is_comming
                                  - gestion_fin_de_vie_EHPHAD
                                  - on_prepare_un_bonus
                                  - action_bonus
                                  - gestion_collisions
                                  - move_papa
                                  - move_groupe
                                  - update_score

Implementation of lists : 
     - in the **Fenetre** class : - method __init__ : self.enemy, 
                                             self.lst_ilot,self.lst_bonus
     - in **Player** class: - method __init__: self.nb_life,
                                     self.projectile, self.thermos_bu
     - in class **Ilots** : - method __init__ : self.lst_carre
     - in class **Mechant** :  - method __init__ : self.projectile

All the images used are free of rights or their use has been validated by the person concerned.

Authors : Emma BEGARD and Audrey NICOLLE 
