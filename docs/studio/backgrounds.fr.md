# Arrière-plans

Chaque style de QuizXpress possède un arrière-plan. Vous pouvez modifier l’arrière-plan d’une diapositive (également après avoir sélectionné un style) en cliquant avec le bouton droit sur la diapositive et en choisissant ‘Select background picture…’.

Vous pouvez aussi choisir une image d’arrière-plan dans la galerie d’arrière-plans de la section Background Image du ruban Design. Vous pouvez également ajouter vos propres arrière-plans à la galerie.

Comme pour les styles, vous pouvez mieux organiser votre espace de travail en filtrant les arrière-plans que vous n’utilisez pas. Vous accédez au filtre via le bouton de lancement de boîte de dialogue (« dialog launcher ») de la section Background Image du ruban Design.

![](../assets/images/image279.webp){ width="466" loading=lazy }

## Vidéo en arrière-plan

Au lieu d’une image fixe, une diapositive peut aussi avoir une vidéo qui défile derrière elle : des nuages en mouvement, un compte à rebours, une animation en boucle à vos couleurs. La question, les réponses et tout le reste de la diapositive restent au-dessus de la vidéo.

Pour en ajouter une, cliquez avec le bouton droit sur l’arrière-plan de la diapositive et choisissez ‘Background video…’, puis sélectionnez un fichier vidéo. Vous pouvez aussi la définir dans le volet des propriétés : sélectionnez la diapositive, puis cliquez sur la propriété ‘Background video’ dans la section Background de la page Design. Si vous sélectionnez plusieurs diapositives et définissez la propriété, elles reçoivent toutes la même vidéo d’arrière-plan ; la vidéo n’est stockée qu’une seule fois dans le fichier du quiz.

![Menu contextuel de l’arrière-plan de la diapositive avec les options de vidéo d’arrière-plan](../assets/images/background-video-context-menu.webp){ loading=lazy }

Dans l’éditeur, la diapositive affiche la première image de la vidéo, avec une petite icône de vidéo dans le coin supérieur gauche afin que vous puissiez voir quelles diapositives ont une vidéo d’arrière-plan. Pour la voir en mouvement, cliquez avec le bouton droit sur l’arrière-plan et choisissez ‘Play background video’ (et ‘Stop background video’ pour l’arrêter). L’aperçu (F5) la lit également.

Une vidéo d’arrière-plan n’occupe pas d’espace réservé image/vidéo ; vous pouvez donc toujours placer une image ou une [vidéo dans un espace réservé](adding-multimedia-content/video.md#combiner-une-video-en-arriere-plan-et-une-video-dans-un-espace-reserve) sur la même diapositive ; elle est lue au-dessus de la vidéo d’arrière-plan.

Dès qu’une diapositive a une vidéo d’arrière-plan, les paramètres suivants apparaissent sous la propriété ‘Background video’ :

![Paramètres de la vidéo d’arrière-plan dans le volet des propriétés](../assets/images/properties-panel-background-video.webp){ width="322" loading=lazy }

| Property           | Description                                                                                                                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Video storage type | Embedded (la vidéo est stockée dans le fichier du quiz) ou linked (le quiz renvoie au fichier vidéo sur le disque). Voir [Vidéo](adding-multimedia-content/video.md#inserer-une-video) pour savoir quand utiliser l’un ou l’autre. |
| Linked file        | Le nom du fichier vidéo, pour une vidéo liée                                                                                                                                                                |
| Loop               | Relance la vidéo lorsqu’elle se termine. Activé par défaut.                                                                                                                                                 |
| Silent             | Lit la vidéo sans son. Activé par défaut, afin que la vidéo d’arrière-plan ne gêne pas les sons de vos questions.                                                                                           |
| Sync with quiz     | Met la vidéo en pause lorsqu’une équipe buzze, que le compte à rebours est en pause ou que la question se termine, et la reprend lorsque la question continue. Désactivé par défaut : la vidéo continue simplement de défiler. (Sous ‘More options’.) |

Pour supprimer la vidéo d’arrière-plan, cliquez avec le bouton droit sur l’arrière-plan de la diapositive et choisissez ‘Remove background video’.

!!! tip
    Donnez une vidéo d’arrière-plan à une [catégorie](using-categories.md), et chaque diapositive que vous formatez avec cette catégorie la reçoit aussi.

Pendant le quiz, la vidéo d’arrière-plan démarre dès que la diapositive apparaît. Gardez des vidéos d’arrière-plan courtes et légères : une boucle de quelques secondes en HD suffit généralement.
