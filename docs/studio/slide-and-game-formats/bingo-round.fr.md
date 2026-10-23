# Bingo round

Ce type de diapositive lance une partie classique de Number Bingo, Emoji Bingo, Music Bingo ou Trivia Bingo. Ce type de jeu ne peut actuellement être joué que lorsque le public utilise l'application Smart Buzzer pour appareils mobiles.

![](../../assets/images/image99.webp){ width="518" loading=lazy }

En sélectionnant l'élément des boules de Bingo sur la diapositive, l'onglet contextuel Bingo apparaît dans le ruban, et vous pouvez configurer les différents aspects de votre nouveau jeu de bingo comme décrit dans la section [Propriétés Bingo](../user-interface-overview/advanced-properties-grid.md#proprietes-du-bingo).

QuizXpress prend en charge les jeux de Bingo suivants :

| ![](../../assets/images/image100.webp){ width="257" loading=lazy } | ![](../../assets/images/image101.webp){ width="259" loading=lazy } |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](../../assets/images/image102.webp){ width="257" loading=lazy }                                                                                       | ![](../../assets/images/image103.webp){ width="259" loading=lazy }                                                                                       |

## Créer un jeu de Bingo

Vous pouvez créer une nouvelle manche de bingo soit avec le Quiz Wizard, soit en insérant manuellement une diapositive de bingo depuis le sélecteur Quiz Slides de l'onglet INSERT du ruban.

![](../../assets/images/image104.webp){ width="604" loading=lazy }

Pour un jeu traditionnel de Number Bingo ou d'Emoji Bingo, il suffit de créer cette seule diapositive. Cliquez simplement sur les boules de Bingo, puis sélectionnez « Regular Bingo » ou « Emoji Bingo ».

![](../../assets/images/image105.webp){ width="190" loading=lazy }

Pour une manche de Trivia Bingo, en revanche, vous devrez aussi créer les questions dont la réponse (qui peut être un texte ou une image) apparaîtra dans les cases de la carte de bingo. Les questions doivent être insérées après la diapositive Bingo, et vous devez terminer la manche par une diapositive de *fin de manche*. Comme chaque carte comporte 24 cases à remplir, il faut au moins 24 questions. Créer davantage de questions rendra les cartes plus aléatoires. Par exemple, si vous n'avez que 24 questions, chaque carte aura « Coverall » à la dernière question, et tout le monde aura Bingo. Si vous créez plus de questions, comme pour le bingo classique, toutes les réponses ne figureront pas sur les cartes.

Les types de questions pris en charge dans une manche de Trivia Bingo sont les questions numériques, textuelles, à lettre et les questions ouvertes avec une seule image (ce qui donne une case de bingo en image).

Pour créer des cases de texte sur votre carte de bingo, utilisez le modèle de diapositive « open question » :

![](../../assets/images/image106.webp){ loading=lazy }

Et réglez le mode de saisie (Input mode) sur Number, Letter ou Text :

![](../../assets/images/image107.webp){ loading=lazy }

Cela donnera une case de bingo contenant la bonne réponse définie pour la question. Utiliser « Number » ou « Text » ne change pas grand-chose, mais avec le type « Letter », seule la première lettre apparaît sur la carte de bingo.

Pour créer une case de carte de bingo avec une *image*, choisissez la disposition suivante :

![](../../assets/images/image108.webp){ loading=lazy }

Sélectionnez l'élément image et cochez l'option « Hidden » dans la section « Adjust » du ruban.

![](../../assets/images/image109.webp){ width="298" loading=lazy }

L'image sera alors masquée lors de la présentation du quiz au public, et elle apparaîtra sur la carte de Bingo comme une case image (vous pouvez choisir d'afficher aussi l'image sur le grand écran pendant un quiz, mais la réponse sera alors très facile à trouver sur la carte de Bingo !).

![](../../assets/images/image110.webp){ loading=lazy }

Le Quiz Wizard aide également à créer rapidement une manche de Trivia Bingo ou de Music Bingo. Lancez simplement le Quiz Wizard (onglet HOME, bouton Quiz Wizard), appuyez sur « create a new round » puis sur « a Bingo round ». Vous pouvez alors choisir parmi les quatre types de Bingo et indiquer vos préférences.

Lorsque vous avez fini de créer vos questions, vous pouvez prévisualiser une carte (aléatoire) en faisant un clic droit sur la diapositive de bingo et en sélectionnant Preview (ou en appuyant sur F5).

Voici un exemple d'aperçu d'une carte de Trivia Bingo :

![](../../assets/images/image111.webp){ loading=lazy }

Pendant l'exécution de votre quiz, dès que votre diapositive Bingo est présentée, le système crée un ensemble de cartes aléatoires et les distribue automatiquement à vos joueurs.

Pour le Trivia Bingo, une option (dans l'onglet BINGO du ruban) permet de mélanger les diapositives de la manche de Bingo afin qu'elles apparaissent dans un ordre différent à chaque fois que vous jouez le quiz :

![](../../assets/images/image112.webp){ width="158" loading=lazy }

Il est possible de personnaliser l'image affichée au centre des cartes de Bingo dans l'application mobile et d'utiliser votre propre image. Pour cela, sélectionnez l'élément Bingo sur la diapositive Bingo, ouvrez le volet des propriétés avancées (onglet VIEW, cochez « Properties »), cliquez sur la propriété « Center image » puis sur le bouton à trois points pour sélectionner un fichier image :

![](../../assets/images/image113.webp){ loading=lazy }

Utilisez votre propre image centrale pour promouvoir votre marque auprès des joueurs !

### Motifs de Bingo pris en charge

![](../../assets/images/image114.webp){ width="146" loading=lazy }

Vous pouvez définir jusqu'à cinq motifs successifs menant au Bingo. Vous pouvez sélectionner trois motifs en cliquant sur les boutons « Pattern » dans les sections First pattern, Second pattern et Third pattern de l'onglet BINGO du ruban. Si vous voulez définir un quatrième et un cinquième motif, vous pouvez le faire dans le volet Properties.

Vous pouvez choisir parmi 13 motifs prédéfinis. Il est également possible de définir des motifs personnalisés.

À l'ouverture des motifs, une animation est affichée pour les motifs concernés (par exemple, le motif de ligne horizontale est valide pour chaque ligne horizontale).

Pendant une partie de Bingo, une animation montrant le motif en cours qui donne le Bingo s'affiche à la fois dans le lecteur de quiz et sur le téléphone mobile.

La version 7.1 apporte la possibilité de créer vos propres motifs de bingo. Pour cela, choisissez le motif personnalisé dans le ruban (dernière entrée du sélecteur de motifs), après quoi l'éditeur de motifs s'affiche :

| ![](../../assets/images/image115.webp){ width="203" loading=lazy } | ![](../../assets/images/image116.webp){ width="205" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Variante de motif 1                                                             | Variante de motif 2                                                             |

Vous créez le motif en cliquant sur les cases. Un motif peut avoir plusieurs variantes qui donnent toutes un bingo valide (de façon analogue à un Bingo en ligne horizontale, par exemple, où chaque ligne horizontale donne un Bingo). Dans le lecteur de quiz comme dans l'application mobile, les variantes sont présentées aux joueurs dans une animation.

### Cases vides par ligne

Pour activer les cases vides, ouvrez la vue des propriétés dans Studio (VIEW->Properties dans le ruban), sélectionnez la diapositive Bingo et repérez la propriété nommée Blanks per row :

![](../../assets/images/image117.webp){ width="605" loading=lazy }

Cette valeur indique le nombre de cases vides par ligne sur votre carte. Elle peut être comprise entre 0 et 4. Avec une valeur de 2, la carte de Bingo sur l'appareil mobile ressemblera à ceci :

![](../../assets/images/image118.webp){ width="128" loading=lazy }

Les cases vides servent de jokers lors de l'évaluation d'une déclaration de Bingo. Ainsi, dans l'exemple de carte de gauche, en marquant simplement 30, 50 et 67, le joueur pourrait déclarer un Bingo pour une ligne horizontale. Quand on joue avec des cases vides, il faut réfléchir aux motifs à jouer. Par exemple, jouer pour une ligne verticale n'est peut-être pas une bonne idée, car certaines colonnes pourraient ne comporter qu'une seule case à marquer. De même, des motifs plus complexes, comme un losange, pourraient ne jamais être réalisables avec certaines cartes.

### Options avancées

*Auto advance after claim* – lorsque cette option est activée, le jeu passe automatiquement à la suite après une déclaration de Bingo. Lorsqu'elle n'est pas activée, le jeu attend que l'animateur passe à la suite.

*Virtual caller* – lorsqu'elle est activée, les numéros tirés sont annoncés à voix haute par l'ordinateur (avec le synthétiseur vocal Windows par défaut).

**Utiliser une voix personnalisée pour l'annonceur de Bingo**

Lorsque l'option Virtual Caller est activée, le synthétiseur vocal Windows est utilisé par défaut pour annoncer les numéros. Vous pouvez cependant créer vos propres fichiers vocaux, par exemple avec l'aide d'une célébrité locale. Pour cela, créez dans le dossier de données de l'application QuizXpress (dans l'Explorateur Windows, saisissez *%appdata%\quizxpress* dans la barre de navigation) un sous-dossier nommé « bingo ». Dans ce dossier, créez les fichiers mp3 de chaque numéro à annoncer (par ex. 1.mp3, 2.mp3, 3.mp3, etc.) et, éventuellement, un fichier nommé « welcome.mp3 » qui sera lu au début du jeu de Bingo. Le système lira ces fichiers à chaque tirage d'une nouvelle boule.

### Mode False Bingo

![](../../assets/images/image119.webp){ width="604" loading=lazy }

Vous pouvez indiquer ce qui doit se passer lorsqu'une fausse déclaration de Bingo est faite. Les options sont :

- Continue playing – le joueur qui a fait une fausse déclaration peut déclarer un autre bingo pour le même motif.

- Exclude for patterns – le joueur qui a fait une fausse déclaration ne peut plus déclarer de bingo pour le même motif. Il doit attendre que quelqu'un d'autre ait un bingo valide et que le système passe au motif suivant.

- Exclude for round – le joueur qui a fait une fausse déclaration ne peut plus déclarer de bingo pendant le reste de la manche (ce qui peut être toute la partie s'il n'y a qu'une seule manche de Bingo).

Dans le volet des propriétés, deux paramètres supplémentaires sont disponibles pour les fausses déclarations de Bingo :

False Bingo limit – définit une limite au nombre de fausses déclarations de Bingo par joueur. Une fois la limite atteinte, le joueur est exclu du jeu.

False Bingo handling – détermine la façon dont les fausses déclarations de Bingo sont traitées : On-Screen ou Silent. En mode silencieux, seules les déclarations de Bingo qui aboutiront à un Bingo valide sont affichées dans le lecteur de quiz.

### Traitement des déclarations

Il existe deux options pour traiter une déclaration de Bingo :

![](../../assets/images/image120.webp){ width="605" loading=lazy }

Fastest : seul le premier joueur à déclarer un Bingo est pris en compte ; les autres personnes qui appuient aussi sur Bingo sont bloquées. Lorsque le Bingo est valide, le motif suivant est joué. Tous les joueurs jouent alors pour le nouveau motif.

Multiple : toutes les déclarations faites dans les quelques secondes suivant la déclaration du premier joueur sont traitées. S'il y a eu une déclaration de Bingo valide, le motif passe au motif suivant une fois toutes les déclarations traitées.

### Contraintes lors de l'enregistrement d'un quiz

Il existe quelques contraintes lors de la création d'une manche de Bingo. Par exemple, il est important qu'il n'y ait pas de cases en double sur la carte. Le système intègre un vérificateur de règles qui contrôle le quiz avant l'enregistrement :

![](../../assets/images/image121.webp){ width="475" loading=lazy }

Il le fait automatiquement pour les questions textuelles. Pour les cases en image, vous devrez le faire vous-même ; veillez à ne pas inclure deux questions avec la même image.

## Jouer une partie de Bingo

Le lecteur de quiz se charge d'enregistrer les cartes de Bingo de tous les joueurs et d'écouter les déclarations de Bingo envoyées par les joueurs. Vous trouverez ci-dessous des exemples des différents jeux de Bingo.

### Types de jeux de Bingo

![](../../assets/images/image122.webp){ width="424" loading=lazy }**Number Bingo**

L'écran affiche les 9 dernières boules jouées avec leur couleur (qui indique la section de la carte de Bingo) ainsi que la dernière boule tirée. Il indique combien de boules restent à tirer ainsi que le motif en cours menant à un Bingo.

![](../../assets/images/image123.webp){ width="423" loading=lazy }**Emoji Bingo**

L'Emoji Bingo est fondamentalement identique au Number Bingo, sauf qu'au lieu de 75 numéros, ce sont les 75 emojis les plus couramment utilisés.

![](../../assets/images/image124.webp){ width="422" loading=lazy }**Trivia Bingo**

Dans le Trivia Bingo, les questions sont affichées sur le grand écran avec le motif en cours et le compte à rebours. La réponse, qui est un texte ou une image, doit être trouvée sur la carte (s'il y a plus de questions que de cases sur la carte, il se peut que la réponse ne soit \*pas\* sur une carte).

**Music Bingo**

Le Music Bingo (ou même Video Bingo) est fondamentalement identique au Trivia Bingo. Des questions avec des extraits musicaux sont affichées à l'écran, et les réponses (textes ou images) se trouvent sur la carte de Bingo.

Le Quiz Wizard offre une prise en charge spécifique du Music Bingo. Il vous permet de sélectionner un dossier contenant des fichiers mp3, à partir duquel la manche de Bingo est construite automatiquement.

![](../../assets/images/image125.webp){ width="585" loading=lazy }

### Déclarer un Bingo

Lorsqu'un joueur a marqué suffisamment de cases pour compléter un motif, il fait une déclaration en appuyant sur le bouton Bingo de l'application mobile. Le nom du joueur s'affiche alors à l'écran avec un compte à rebours de 3 secondes pendant que le système valide la déclaration. Aucune vérification manuelle n'est nécessaire.

![](../../assets/images/image126.webp){ loading=lazy }

Après la validation, un pouce levé ou un pouce baissé s'affiche sur le grand écran ainsi que sur le mobile.

![](../../assets/images/image127.webp){ loading=lazy } ![](../../assets/images/image128.webp){ width="103" loading=lazy }

En cas de Bingo valide, le joueur gagne des points (si configuré) et le système passe au motif suivant.

Lorsqu'il n'y a plus de motif à jouer, la manche se termine et le quiz reprend à la diapositive de fin de manche (lorsqu'il n'y a qu'une seule manche et pas de diapositive de fin de manche, le quiz affiche l'écran des scores final).

Le traitement de plusieurs déclarations ressemble à ceci :

![](../../assets/images/image129.webp){ loading=lazy }

Lorsqu'un joueur se déconnecte de votre quiz ou perd la connexion à la session, la carte de Bingo et les cases marquées ne sont pas perdues. Lorsqu'il rejoint à nouveau la partie, la carte est présentée telle qu'elle était au moment de la déconnexion. De plus, si le lecteur de quiz plante, vous pouvez redémarrer le quiz, restaurer l'instantané enregistré et poursuivre la manche de Bingo.

### Vue en direct des cartes

Dans QuizXpress Director, dans l'onglet « Teams », une option permet de consulter la carte de Bingo actuelle du joueur sélectionné. La carte indique aussi quelles cases ont déjà été jouées, marquées en vert.

Pour afficher la carte d'un joueur, sélectionnez le joueur et appuyez sur le bouton « Show bingo card ». Ainsi, en cas de litige, vous pouvez toujours vérifier.

![](../../assets/images/image130.webp){ loading=lazy }

### Modifier les motifs de Bingo pendant une session de Bingo

Dans QuizXpress Director, il est désormais possible de modifier les motifs d'une manche de Bingo, ainsi que certains autres paramètres de Bingo, pendant un quiz (avant le début de la manche). Pour cela, double-cliquez sur la diapositive Bingo dans l'onglet Questions afin d'ouvrir les paramètres d'une manche de Bingo.

![](../../assets/images/image131.webp){ width="605" loading=lazy }
