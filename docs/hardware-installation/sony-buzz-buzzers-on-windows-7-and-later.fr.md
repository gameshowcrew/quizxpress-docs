# Buzzers Sony Buzz sous Windows 7 et versions ultérieures

La dernière révision des buzzers Sony Buzz™ nécessite une procédure particulière pour fonctionner avec QuizXpress sous Windows Vista ou Windows 7. Cette annexe décrit les étapes permettant d'installer correctement le récepteur USB Sony Buzz™ sur ces systèmes d'exploitation.

Vous pouvez reconnaître cette nouvelle révision grâce au texte “Manufactured by Logitech…” sur le récepteur USB. Les buzzers n'ont pas de bouton d'alimentation sur le côté droit, et la LED bleue présente sur les révisions précédentes est absente. Ce modèle de buzzer s'allume en appuyant une fois sur le grand bouton rouge.

Branchez le récepteur sur un port USB de votre ordinateur. Au bout d'un moment, un message indique l'échec de l'installation du périphérique :

Accédez au menu Démarrer et sélectionnez Ordinateur->Propriétés :

![](../assets/images/image485.webp){ width="330" loading=lazy }

Dans la fenêtre qui s'affiche, sélectionnez *Gestionnaire de périphériques* :

![](../assets/images/image486.webp){ width="360" loading=lazy }

Dans la fenêtre du Gestionnaire de périphériques, développez le nœud Contrôleurs de bus USB :

![](../assets/images/image487.webp){ width="364" loading=lazy }

Sélectionnez le nœud qui indique une erreur, cliquez dessus avec le bouton droit et sélectionnez Mettre à jour le pilote dans le menu :

![](../assets/images/image488.webp){ width="365" loading=lazy }

Dans l'assistant, sélectionnez “Rechercher un pilote sur mon ordinateur” :

![](../assets/images/image489.webp){ width="362" loading=lazy }

Sur l'écran suivant, sélectionnez ‘Choisir parmi une liste de pilotes disponibles sur mon ordinateur’ puis Suivant :

![](../assets/images/image490.webp){ width="397" loading=lazy }

Sur l'écran suivant, sélectionnez “Périphérique d'entrée USB” et appuyez sur Suivant :

Le récepteur Buzz™ est maintenant installé et prêt à l'emploi.

![](../assets/images/image491.webp){ width="317" loading=lazy }

Fermez la fenêtre ; dans le Gestionnaire de périphériques, le récepteur de buzzers sans fil apparaîtra désormais sous le nom “Périphérique d'entrée USB”.

![](../assets/images/image492.webp){ width="317" loading=lazy }

Pour localiser le périphérique de buzzer *après* son installation, par exemple pour le désinstaller, vous devrez ouvrir les propriétés de chacune des entrées *Périphérique d'entrée USB* (clic droit ; Propriétés)

![](../assets/images/image493.webp){ width="291" loading=lazy }

Ensuite, dans la fenêtre *Propriétés de Périphérique d'entrée USB*, sélectionnez l'onglet ‘Détails’ et choisissez *Description du périphérique signalée par le bus* dans la liste déroulante ‘Propriété’. Si le champ ‘Valeur’ affiche le texte *Logitech Trebek(tm) controllerV1*, vous avez trouvé le périphérique de buzzer Sony.

![](../assets/images/image494.webp){ width="289" loading=lazy }
