# Vidéo

QuizXpress prend également en charge l’utilisation d’extraits vidéo. Les extraits vidéo peuvent servir dans les questions, mais aussi, par exemple, pour communiquer un message marketing à votre public. Il existe un format de diapositive spécial « vidéo plein écran » qui lit la vidéo sélectionnée en plein écran pendant le jeu.

QuizXpress prend en charge de nombreux formats de fichier, mais pour lire correctement les fichiers vidéo, le CODEC vidéo approprié (un composant Windows utilisé pour diffuser un format vidéo donné) doit être installé sur votre système. Le programme d’installation de QuizXpress ajoute le pack de codecs LAV à votre système. La dernière version de ce pack de codecs se trouve ici : <https://github.com/Nevcairiel/LAVFilters/releases>

## Insérer une vidéo

Pour ajouter une vidéo à une question, créez d’abord une nouvelle question avec un modèle comportant un espace réservé image/vidéo.

| ![](../../assets/images/image211.webp){ width="163" loading=lazy } | ![](../../assets/images/image212.webp){ width="161" loading=lazy } | ![](../../assets/images/image213.webp){ loading=lazy } | Ce dernier modèle affiche la vidéo en plein écran. Vous pouvez aussi l’utiliser pour montrer du matériel promotionnel sur votre entreprise entre les questions ! |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

Cliquez ensuite avec le bouton droit sur l’espace réservé de l’image et cliquez sur ‘Select Video’ dans le menu contextuel. Une boîte de dialogue de fichier s’ouvre, dans laquelle vous pouvez sélectionner un extrait vidéo *(\*.avi, \*.wmv, \*.mov, \*.mp4, \*.mpg, \*.mpeg, \*.flv, \*.3gp, \*.webm*).

Comme pour l’audio, une vidéo peut être liée ou intégrée. Intégrer un extrait vidéo dans un quiz signifie que l’extrait est incorporé au fichier du quiz. Lier un extrait vidéo signifie qu’une référence est créée depuis le fichier du quiz vers une vidéo du système de fichiers. En général, il est recommandé de *lier* les vidéos tant que vous êtes en train de modifier le quiz. Une fois la modification terminée, vous pouvez utiliser la [fonction ‘Pack’](../other-functionality/packing-and-unpacking-a-quiz.md) pour regrouper tous les fichiers liés externes dans un seul gros fichier de quiz (2 Go maximum). Le regroupement peut aussi découper les vidéos pour ne garder que la partie lue et les compresser, ce qui garde le fichier regroupé de petite taille. Avec ce fichier combiné, il est facile de déplacer votre quiz vers un autre ordinateur sans vous soucier des ressources externes.

!!! note

    lorsque vous liez des vidéos, veillez à ne pas les supprimer de votre système de fichiers. Lorsque vous copiez le quiz sur un autre ordinateur, les vidéos doivent être copiées dans le même dossier que le fichier du quiz afin que QuizXpress puisse les retrouver.*

Le contenu vidéo intégré ne peut pas dépasser 30 Mo. En général, essayez de garder vos vidéos aussi petites que possible : si votre question ne dure que trente secondes, il est inutile d’insérer une vidéo de quatre minutes. Dans ce cas, utilisez un outil de montage vidéo pour couper la vidéo.

## Modifier les propriétés de la vidéo

Lorsque vous sélectionnez une vidéo, l’onglet de ruban contextuel de la vidéo apparaît :

![L’onglet de ruban Video](../../assets/images/video-ribbon.webp){ loading=lazy }

Vous pouvez y prévisualiser la vidéo, définir les marqueurs de début et de fin, régler le volume et modifier la vitesse de lecture (notez que la modification de la vitesse de lecture peut ne pas fonctionner avec tous les types de vidéo et dépend des CODEC utilisés). Vous pouvez également configurer un effet qui évolue dans le temps. Par exemple, vous pouvez utiliser l’effet Mosaic pour afficher la vidéo entièrement pixélisée au début et en révéler progressivement les détails pendant que vous posez une question à votre public sur la vidéo, avec des points décroissants. Vous pouvez aussi lire la vidéo en mode silencieux et la répéter en boucle jusqu’à la fin de la question. Avec ‘Select Picture’, vous pouvez rétablir l’élément de la diapositive en image fixe.

Avec Replay, vous pouvez activer la relecture d’une partie de la vidéo une fois la question terminée (lorsque la bonne réponse est révélée).

## Vidéo en arrière-plan

Une vidéo peut aussi être lue derrière toute la diapositive, comme arrière-plan. Une telle vidéo d’arrière-plan n’est pas placée dans un espace réservé : cliquez avec le bouton droit sur l’arrière-plan de la diapositive et choisissez ‘Background video…’, ou définissez la propriété ‘Background video’ de la diapositive. Une vidéo d’arrière-plan est lue en boucle et sans son par défaut. Voir [Vidéo d’arrière-plan](../backgrounds.md#video-en-arriere-plan) pour tous ses paramètres.

Dans la capture d’écran ci-dessous, une vidéo d’arrière-plan est combinée à une forme superposée pour créer un effet de vieille télévision (une forme avec un écran transparent est placée au-dessus de la vidéo d’arrière-plan).

![](../../assets/images/image215.webp){ loading=lazy }

!!! note
    Les versions précédentes proposaient une case ‘Background’ pour une vidéo dans un espace réservé. Cette case a disparu : une vidéo d’arrière-plan a désormais sa propre place derrière la diapositive. Les vidéos d’arrière-plan des quiz créés avec une version antérieure sont converties automatiquement à l’ouverture du quiz.

## Combiner une vidéo en arrière-plan et une vidéo dans un espace réservé

Comme la vidéo d’arrière-plan n’utilise pas d’espace réservé, une diapositive peut avoir les deux : une vidéo d’arrière-plan lue derrière la diapositive et une vidéo (ou une image) dans son espace réservé, lue par-dessus. Par exemple, utilisez une animation de studio en boucle comme vidéo d’arrière-plan et l’extrait de film de la question dans l’espace réservé.

![Une diapositive avec une vidéo d’arrière-plan et une vidéo dans son espace réservé](../../assets/images/background-and-placeholder-video.webp){ loading=lazy }

Les deux vidéos conservent chacune leurs propres paramètres. La vidéo de l’espace réservé démarre après sa pause d’introduction (‘Intro Pause’) et se met toujours en pause et reprend en même temps que le quiz. La vidéo d’arrière-plan démarre dès que la diapositive apparaît et, sauf si vous activez ‘Sync with quiz’, continue de défiler. Laissez la vidéo d’arrière-plan silencieuse (valeur par défaut) afin que son son ne se mélange pas à celui de la vidéo de l’espace réservé.
