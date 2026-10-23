# L’onglet Media Player

Cet onglet de Director affiche le lecteur multimédia de QuizXpress. Avec le lecteur multimédia, vous pouvez :

- Lancer une vidéo plein écran sur l’écran principal

- Afficher une image plein écran sur l’écran principal

- Lire un fichier MP3

- Présenter une image promotionnelle sur l’application Smart Buzzer

- Relire/reprendre la vidéo de la diapositive en cours

- Relire/reprendre le son de la diapositive en cours

- Régler le volume du lecteur de quiz

- Gérer une liste de fichiers multimédias

- Lire des fichiers en un clic depuis la [console de sons](#la-console-de-sons)

Lorsque vous ajoutez des fichiers à la liste, ils sont en réalité copiés dans le dossier local de données de l’application QuizXpress (chemin dans l’Explorateur : %AppData%\QuizXpress\Media). Cela évite les problèmes si les fichiers d’origine sont déplacés, supprimés, etc. Ainsi, si vous supprimez un fichier de la liste, il est supprimé du stockage de QuizXpress, mais le fichier d’origine reste intact.

![](../../assets/images/image454.webp){ width="605" loading=lazy }

## Rechercher dans la liste

Si vous avez beaucoup de fichiers multimédias, utilisez le champ de recherche au-dessus de la liste pour en trouver un rapidement. Saisissez une partie du nom d’un fichier et la liste n’affiche que les fichiers qui le contiennent, par exemple 'chris' trouve à la fois 'Chris Rea - Driving home for christmas' et 'Band Aid 30 - Do They Know It's Christmas'. Les majuscules et minuscules n’ont pas d’importance. Appuyez sur Esc ou videz le champ pour afficher de nouveau tous les fichiers.

![Liste multimédia filtrée avec le champ de recherche](../../assets/images/media-player-search.webp){ width="605" loading=lazy }

Pendant que vous tapez dans le champ de recherche, des touches comme Espace, 'C' et 'S' vont dans le champ et ne déclenchent pas les raccourcis de Director. La recherche ne fait que filtrer la liste ; la console de sons conserve tous ses pads.

## La console de sons

À côté de la liste, l’onglet Media Player comporte une console de sons (sound board) : une grille de pads colorés et lumineux, comme les launchpads utilisés par les DJ. Un clic sur un pad lance son son, sa vidéo ou son image, de sorte que jingles, applaudissements et musiques d’entrée sont toujours à portée de main.

![Console de sons avec un pad en lecture et un pad en pause](../../assets/images/media-player-sound-board.webp){ loading=lazy }

- Le pad en cours de lecture s’illumine et affiche le temps restant ainsi qu’une barre de progression. Un pad en pause affiche un symbole de pause.
- Cliquez de nouveau sur un pad en lecture pour l’arrêter.
- Les pads inactifs affichent la durée de leur fichier.

Cliquer sur un pad sélectionne aussi son fichier dans la liste, de sorte que les boutons lecture, pause, arrêt et retour de la barre d’outils agissent sur ce fichier.

### Afficher la liste, la console de sons ou les deux

Utilisez les boutons 'List' et 'Sound board' à droite de la barre d’outils pour afficher la liste, la console de sons ou les deux côte à côte. Au moins l’un des deux est toujours affiché. Lorsque les deux sont affichés, faites glisser la séparation entre eux pour donner plus de place à l’un ou à l’autre. Director mémorise votre choix.

### Placer des fichiers sur les pads

La première fois que vous ouvrez la console de sons, elle est remplie automatiquement avec vos fichiers multimédias. Pour l’organiser vous-même :

- Faites glisser un fichier de la liste vers un pad.
- Faites glisser des fichiers directement depuis l’Explorateur Windows vers un pad. Ils sont ajoutés à la liste multimédia (copiés dans le dossier multimédia, comme avec 'Add') et placés sur ce pad. Lorsque vous déposez plusieurs fichiers, les autres vont sur les pads vides suivants.
- Faites glisser un pad sur un autre pad pour les échanger.

Une fois que vous avez modifié la console vous-même, les nouveaux fichiers multimédias n’y sont plus ajoutés automatiquement. Utilisez 'Fill empty pads with media files' (voir ci-dessous) pour les ajouter.

![Console de sons à côté de la liste, avec le menu du pad](../../assets/images/media-player-sound-board-menu.webp){ loading=lazy }

### Options des pads et de la console

Faites un clic droit sur un pad pour :

- 'Play' ou 'Stop' le lancer ou l’arrêter.
- 'File' : choisir le fichier multimédia lu par le pad. Outre vos fichiers multimédias, un pad peut aussi contrôler le son ou la vidéo de la diapositive en cours ('Slide Sound' et 'Slide Video').
- 'Label' : donner un nom court au pad, par exemple 'Applause' plutôt qu’un long nom de fichier. Laissez vide pour afficher de nouveau le nom du fichier.
- 'Color' : choisir une couleur, ou 'Automatic' pour colorer les pads par colonne.
- 'Clear pad' : retirer le fichier du pad. Le fichier reste dans la liste multimédia.

Le même menu, également disponible par un clic droit sur la console autour des pads, propose des options pour toute la console :

- 'Grid size' : de 3 × 4 jusqu’à 8 × 8 pads. Les pads gardent leur place lorsque vous changez la taille.
- 'Clicking a playing pad' : choisir si un clic sur un pad en lecture l’arrête (par défaut), le relance, ou le met en pause et le reprend.
- 'Fill empty pads with media files' : place sur les pads vides les fichiers multimédias qui ne sont pas encore sur la console.
- 'Clear all pads' : vide la console. Vos fichiers multimédias sont conservés.

!!! note
    La console de sons est stockée sur cet ordinateur, à côté du dossier multimédia (%AppData%\QuizXpress\SoundBoard.xml), elle sera donc toujours là lors de votre prochain show. Lorsque vous supprimez un fichier de la liste multimédia, il est aussi retiré de ses pads.
