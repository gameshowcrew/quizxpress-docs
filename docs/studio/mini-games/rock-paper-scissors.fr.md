# Rock Paper Scissors

Dans le mini-jeu Rock Paper Scissors, le public joue contre un adversaire virtuel.
Les joueurs choisissent pierre, feuille ou ciseaux sur leur buzzer, leur keypad ou leur téléphone. La main de
l'ordinateur monte et descend trois fois avant de révéler son choix.

![Écran de vote de Rock Paper Scissors avec le style de main blanc](../../assets/images/rock-paper-scissors-voting.webp){ loading=lazy }

## Jouer une manche

1. Lancez le jeu. Le studio apparaît et la musique de fond démarre.
2. Utilisez 'Next' pour ouvrir le vote.
3. Les joueurs appuient sur **A pour pierre**, **B pour feuille** ou **C pour ciseaux**. Seul leur premier
   choix valide compte à chaque manche ; les votes suivants sont ignorés.
4. Utilisez 'Next' pour fermer le vote et lancer l'animation de la main. La musique s'arrête, et des
   effets sonores accompagnent les trois mouvements et la révélation.
5. Après la révélation, utilisez 'Next' pour afficher les résultats de la manche et éliminer les joueurs perdants.
   Leurs tuiles disparaissent avec une animation et un effet sonore. Les tuiles restantes se
   replacent dans une nouvelle disposition.
6. Utilisez 'Next' pour ouvrir la manche suivante, ou terminer le jeu lorsque le mode de jeu
   sélectionné est arrivé à son terme.

Les règles habituelles s'appliquent : la pierre bat les ciseaux, les ciseaux battent la feuille et la feuille bat la pierre.
Les joueurs qui choisissent le même geste que l'ordinateur restent dans le jeu, mais ne gagnent pas
les points d'une bonne réponse. Les joueurs qui perdent, ou qui ne soumettent pas de choix valide
avant la fermeture du vote, sont éliminés.

!!! tip
    Par exemple, si l'ordinateur révèle pierre, les joueurs qui ont choisi feuille gagnent la manche,
    ceux qui ont choisi pierre font égalité, et ceux qui ont choisi ciseaux sont éliminés.

![Résultats de la manche avec le style de main néon et les joueurs restants](../../assets/images/rock-paper-scissors-results.webp){ loading=lazy }

## Mode de jeu et score

![Paramètres de Rock Paper Scissors avec aperçus des mains et couleurs de vote](../../assets/images/rock-paper-scissors-settings.webp){ width="600" loading=lazy }

Ouvrez les paramètres du jeu pour choisir un mode de jeu :

- **'Rounds'** : jouez un nombre défini de manches. 'Number of rounds' doit être d'au moins **1**.
- **'Last man standing'** : continuez jusqu'à ce qu'il ne reste qu'un seul joueur, ou que tout le monde
  soit éliminé. 'Number of rounds' est désactivé dans ce mode.

'Points for survivors' définit le bonus attribué aux joueurs qui survivent au jeu.
'Points for every right answer' définit les points attribués pour avoir battu l'ordinateur lors
d'une manche. Une réponse à égalité maintient le joueur dans le jeu sans lui attribuer ces points de manche.

### La surprise du doigt

'Chance for the finger to appear' définit le pourcentage de chances que l'ordinateur révèle
un doigt d'honneur à la place de pierre, feuille ou ciseaux. Il s'agit d'une fausse élimination pour rire :
le public semble éliminé, mais ses tuiles reviennent et le jeu continue.

Réglez la chance sur **0** pour désactiver cette surprise.

## Apparence

### Style de main

Choisissez un style de main à l'aide des aperçus dans les paramètres :

- **White** : un gant de dessin animé blanc classique.
- **Neon** : une main violette lumineuse avec des accents cyan et rose.
- **Comic** : une main rouge audacieuse dans le style bande dessinée.
- **Robot** : une main robotique anguleuse.

Le style sélectionné est utilisé pour l'animation principale, les images de choix
pierre/feuille/ciseaux et les icônes de choix des joueurs. Les panneaux de choix et les tuiles des joueurs
s'harmonisent également avec le style de main.

### Arrière-plan

L'arrière-plan par défaut est un studio de jeu télévisé néon animé. Utilisez le sélecteur 'Background image'
pour choisir votre propre image fixe. Effacez l'image personnalisée pour revenir au studio par défaut.

### Couleurs de vote des joueurs

Choisissez les couleurs de la pierre, de la feuille et des ciseaux sous 'Player voting colors'. Par
défaut, ce sont le gris, le vert clair et le rouge.

Activez 'Show player voting colors while voting' pour afficher le choix de chaque joueur tant que
le vote est encore ouvert. Lorsque cette option est désactivée, les tuiles indiquent que le joueur a voté,
et son choix est affiché une fois que l'ordinateur a révélé sa main.

## Tuiles des joueurs et grands groupes

La zone des joueurs s'adapte automatiquement au nombre de joueurs restants :

- Les petits groupes affichent les numéros et les noms des joueurs. Les noms plus longs utilisent jusqu'à deux lignes.
- Les groupes plus importants utilisent des tuiles compactes avec les numéros des joueurs.
- Pour les très grands groupes, les tuiles indiquent l'état du joueur sans numéro si le numéro serait
  trop petit pour être lisible.

L'affichage des numéros dépend de l'espace disponible et de la taille de la fenêtre de jeu,
il n'y a donc pas de nombre fixe de joueurs à partir duquel les numéros apparaissent. Au fur et à mesure que les joueurs sont éliminés,
la disposition est recalculée et les numéros réapparaissent lorsqu'il y a assez de place. Les noms et
les icônes de choix reviennent à mesure que le groupe diminue.

Les joueurs éliminés sont automatiquement retirés après l'animation d'élimination. Il n'existe
ni mode d'affichage des joueurs distinct, ni paramètre 'Hide expelled players' à sélectionner.

## Son

Le jeu comprend une musique de fond et des effets pour les mouvements de la main, la révélation
et la disparition des joueurs éliminés. La musique de fond démarre à l'ouverture du
jeu et joue pendant le vote. Elle s'arrête lorsque l'animation de la main commence.

Sous 'Sound', utilisez 'Music during voting' pour choisir votre propre musique. Le bouton de lecture
permet d'écouter votre sélection ; le bouton d'effacement rétablit la musique par défaut du jeu.

!!! note
    La musique et les effets sonores standard sont inclus avec le jeu. Aucun fichier son
    supplémentaire n'a besoin d'être installé.

## Messages personnalisés

Activez 'Use custom texts' pour remplacer les messages par défaut :

- **'Voting text'** : le titre affiché pendant que les joueurs choisissent.
- **'Winner'** : le message affiché lorsqu'il ne reste qu'un joueur.
- **'All out'** : le message affiché lorsque tout le monde a été éliminé.

Utilisez le bouton de réinitialisation pour rétablir les messages par défaut.
