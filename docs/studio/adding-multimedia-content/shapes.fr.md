# Formes

Vous pouvez ajouter des formes ou des images quelconques à votre diapositive. Les formes peuvent servir à diverses fins, par exemple :

- Vous pouvez insérer une grande flèche pour attirer l’attention sur un détail d’une image au sujet de laquelle vous interrogez votre public. En réglant l’option Visibility sur ‘Visible after answers’, la forme ne devient visible qu’une fois le compte à rebours de la question terminé.

- Vous pouvez masquer une partie d’une image sur une diapositive en la recouvrant d’une forme. En réglant l’option Visibility sur ‘Hide after answers’, la forme est masquée dès la fin du compte à rebours, ce qui révèle ce qui se trouve derrière.

Pour insérer une forme, utilisez la commande *Insert->Shape* du volet des tâches (cette commande apparaît après la sélection de l’arrière-plan de la diapositive). Vous êtes alors invité à sélectionner un fichier de forme. Par défaut, l’explorateur de fichiers filtre les fichiers *\*.emf* ou *\*.wmf*. Ces types de fichiers utilisent un format « vectoriel » (par opposition aux formats bitmap) qui reste net même après un redimensionnement. Les formes peuvent aussi utiliser n’importe quel format d’image pris en charge (png, jpg, bmp, etc.) comme source ; vous pouvez sélectionner ces autres formats dans l’explorateur de fichiers. Notez que les fichiers image se redimensionnent mal et que le résultat peut apparaître pixélisé lorsqu’ils sont agrandis.

L’élément de forme possède les propriétés suivantes :

| Property       | Description                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Picture        | L’image source de la forme. Vous pouvez utiliser le bouton … pour sélectionner une autre source                                                                                                 |
| Rotation Angle | L’angle de rotation éventuel de la forme                                                                                                                                                        |
| Transparency   | Transparence de la forme                                                                                                                                                                        |
| Visibility     | Condition de visibilité. Peut être réglée sur ‘Always visible’, ‘Visible after answers’ (masque la forme jusqu’à la fin de la question) ou ‘Hide after answers’ (affiche la forme jusqu’à la fin de la question). |

Pour supprimer une forme, sélectionnez-la et appuyez sur la touche Suppr. QuizXpress est livré avec quelques exemples de formes. Vous pouvez aussi créer vos propres formes, par exemple avec Microsoft PowerPoint, en enregistrant une forme PowerPoint comme image (cliquez avec le bouton droit sur la forme, sélectionnez ‘Save as picture’, puis choisissez *wmf* ou *emf* comme format de fichier).

## Formes de texte

Vous pouvez ajouter des éléments de texte à vos diapositives de quiz, et leur visibilité peut être contrôlée exactement comme celle des formes image. Un élément de texte peut par exemple servir à afficher la bonne réponse d’une question ouverte (une fois la question répondue et jugée), ou à donner des indices pendant la question. Dans la grille des propriétés, vous pouvez régler certaines propriétés plus avancées, comme la couleur du panneau d’arrière-plan du texte et le rayon des coins, afin de créer de beaux visuels (notez que ces propriétés ne sont pas disponibles dans le ruban). Les formes de texte possèdent les propriétés supplémentaires suivantes :

| Property                | Description                                                                           |
|-------------------------|---------------------------------------------------------------------------------------|
| Background transparency | Transparence du panneau d’arrière-plan. Par défaut, l’arrière-plan est totalement transparent. |
| Border color            | Couleur de la bordure autour du panneau                                               |
| Border width            | Épaisseur du trait autour du panneau                                                  |
| Corner radius           | Rayon des coins du panneau d’arrière-plan                                             |
| Gradient                | Remplissage en dégradé de l’arrière-plan                                              |
| Alignment               | Alignement du texte (gauche, centré, droite)                                          |
| Drop shadow             | Ombre portée du texte                                                                 |
| Shadow color            | Couleur de l’ombre portée                                                             |
| Text                    | Le texte lui-même                                                                     |
| Text color              | Couleur du texte                                                                      |
| Font                    | Police utilisée pour afficher le texte                                                |

Avec ces propriétés, vous pouvez créer des panneaux de texte comme celui-ci :

![](../../assets/images/image196.webp){ width="376" loading=lazy }

### Symboles de texte

Grâce aux formes de texte, vous pouvez créer des écrans personnalisés contenant des données connues uniquement pendant le déroulement du jeu. Pour cela, les champs de texte (formes) de QuizXpress peuvent contenir des « symboles » prédéfinis. Lorsque le jeu est lancé devant un public, ces symboles sont remplacés par leurs valeurs correspondantes.

Vous pouvez utiliser, entre autres, les noms des joueurs, les scores, les réponses, les temps de réponse, le code PIN, l’index de la diapositive, les notes de la diapositive, le nombre de réponses correctes et incorrectes, et bien d’autres choses encore.

Voici quelques exemples d’écrans à la conception personnalisée. La partie gauche montre l’aspect de la diapositive dans QuizXpress Studio. La partie droite montre l’aspect qu’elle pourrait avoir pendant une partie.

| ![](../../assets/images/image197.webp){ loading=lazy } | ![](../../assets/images/image198.webp){ loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ![](../../assets/images/image199.webp){ loading=lazy }  | ![](../../assets/images/image200.webp){ loading=lazy } |
|                                                                                 |                                                                                 |

Lors de la modification d’éléments de texte dans l’éditeur de texte (double-cliquez sur un texte ou une forme de texte pour l’ouvrir), un bouton ‘Insert Symbol’ permet d’insérer un symbole de texte. Vous pouvez aussi saisir les symboles manuellement. La boîte de dialogue Insert Symbol énumère tous les symboles avec une explication pour chacun.

![](../../assets/images/image201.webp){ width="544" loading=lazy }

Quelques exemples de symboles utilisables :

| **\[date\]**        | Date actuelle                                       | **\[slide.answer\]**     | Bonne réponse de la question actuelle |
|---------------------|-----------------------------------------------------|--------------------------|------------------------------------|
| **\[time\]**        | Heure actuelle                                      | **\[playerX.name\]**     | Nom du joueur de rang X            |
| **\[pin\]**         | Code PIN mobile actuel                              | **\[playerX.score\]**    | Score du joueur de rang X          |
| **\[url\]**         | URL du serveur de jeu                               | **\[playerX.lastvote\]** | Dernier vote                       |
| **\[correct\]**     | Nb de joueurs ayant répondu correctement après la question | **\[playerX.time\]**     | Temps de réponse en millisecondes  |
| **\[incorrect\]**   | Nb de joueurs ayant répondu faux après la question  | **\[playerX.timesec\]**  | Temps de réponse en secondes       |
| **\[novote\]**      | Nb de joueurs n’ayant pas répondu après la question | **\[buzzerX.name\]**     | Nom du joueur avec le buzzer X     |
| **\[slide.index\]** | Numéro de la diapositive de la question actuelle    | **\[buzzerX.score\]**    | Score du joueur avec le buzzer X   |
| **\[slide.notes\]** | Notes de la question actuelle                       |                          |                                    |

Vous pouvez utiliser ces symboles dans n’importe quel élément de texte. Par exemple, vous pouvez insérer une forme de texte et saisir quelque chose comme : « Veuillez ouvrir votre application Smart Buzzer et vous connecter avec le code de jeu : \[pin\] »

Les symboles de texte sont un excellent moyen de rendre vos diapositives de quiz plus dynamiques et, par exemple, de concevoir vos propres tableaux des scores personnalisés.

## Formes temporisées

Vous pouvez aussi afficher et masquer des formes et des éléments de texte au fil du temps en réglant les propriétés des formes temporisées dans l’onglet de ruban contextuel SHAPE TOOLS. Cela vous permet, par exemple, de créer un « indice » qui apparaît après un certain temps au cours du compte à rebours, comme le montre l’exemple suivant :

![](../../assets/images/image202.webp){ loading=lazy }

Dans cet exemple, l’élément de texte avec panneau apparaît lorsque 40 % du temps du compte à rebours se sont écoulés.

Lorsque vous laissez le pourcentage ‘Hide at:’ à 0 %, l’indice reste affiché jusqu’à la fin du compte à rebours.

Vous pouvez également, par exemple, retirer au fil du temps des éléments qui masquent des parties d’une photo.
