# Utiliser les catégories

Les catégories permettent de donner le même aspect à des groupes de questions. Par exemple, dans un même quiz, vous pouvez avoir des questions sur la science, la musique, le cinéma, etc. Pour que toutes les questions sur la science aient le même aspect, vous pouvez créer une catégorie nommée ‘Science’. Pour cette catégorie, vous pouvez ensuite définir des propriétés telles que l’image d’arrière-plan, la police et les couleurs. Lorsque vous créez une nouvelle question sur la science, vous pouvez appliquer la catégorie ‘Science’, et toute la question sera mise en forme selon le modèle ‘Science’. Toutes les catégories sont stockées dans votre fichier de quiz actuel. Si vous utilisez fréquemment les mêmes catégories, nous vous conseillons de créer un fichier de quiz vide qui servira de point de départ à tous vos quiz. Les catégories jouent aussi un rôle important lors de l’import de questions directement depuis Excel : comme les informations de mise en forme avancée ne peuvent pas être stockées dans Excel, chaque question d’Excel peut à la place faire référence à une catégorie existante dont la mise en forme sera appliquée à la diapositive nouvellement créée. Pour créer une nouvelle catégorie, passez d’abord à la vue ‘Category’ :

![](../assets/images/image26.webp){ width="407" loading=lazy }

Activez ensuite l’onglet de ruban INSERT, cliquez sur l’un des modèles et saisissez un nom pour votre catégorie :

![](../assets/images/image27.webp){ width="220" loading=lazy }

Vous pouvez maintenant définir les propriétés de la catégorie, comme l’arrière-plan à utiliser. Pour appliquer une catégorie, revenez à la vue normale des diapositives du quiz, sélectionnez une ou plusieurs diapositives dans le panneau des miniatures à gauche, activez l’onglet DESIGN et choisissez la catégorie dans la galerie Categories :

![](../assets/images/image28.webp){ width="350" loading=lazy }

Les diapositives sélectionnées seront alors mises en forme comme la diapositive de la catégorie.

## Vidéo d’arrière-plan pour une catégorie

Une catégorie peut aussi avoir une [vidéo d’arrière-plan](backgrounds.md#video-en-arriere-plan), par exemple une animation en boucle aux couleurs de la manche ‘Science’. Sélectionnez la diapositive de la catégorie dans la vue Category et définissez-la comme pour une diapositive normale : faites un clic droit sur son arrière-plan et choisissez ‘Background video…’, ou définissez la propriété ‘Background video’ dans le volet des propriétés, avec ses réglages (loop, silent, sync with quiz).

Lorsque vous appliquez la catégorie, chaque diapositive sélectionnée reçoit la vidéo d’arrière-plan avec les mêmes réglages. La vidéo n’est stockée qu’une seule fois dans le fichier de quiz, quel que soit le nombre de diapositives qui l’utilisent. Une image ou une vidéo placée dans les emplacements réservés de ces diapositives reste en place et est lue par-dessus la vidéo d’arrière-plan. Appliquer à nouveau la catégorie, ou une autre catégorie avec une vidéo d’arrière-plan, remplace la vidéo d’arrière-plan de la diapositive. Vous pouvez ensuite encore modifier les réglages de la vidéo d’arrière-plan diapositive par diapositive.

Les questions importées depuis Excel qui font référence à la catégorie reçoivent aussi sa vidéo d’arrière-plan, sauf si la colonne BACKGROUND-VIDEO de la question désigne une vidéo propre (voir [Import and export of questions](import-and-export-of-questions.md)).
