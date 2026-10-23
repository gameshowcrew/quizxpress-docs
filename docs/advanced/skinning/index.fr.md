# Skinning

L'apparence du lecteur de quiz QuizXpress, QuizXpress Live, peut être entièrement modifiée selon vos préférences ou votre charte graphique en créant un 'skin' personnalisé. QuizXpress est livré avec cinq skins intégrés (QuizXpress Classic, QuizXpress 2022, Dark Theme, TV Show et Techno), que vous pouvez sélectionner dans Quiz Setup, sous l'onglet 'Screens', dans la section 'Appearance'. Voir [Personnaliser l'apparence](../../setup/customizing-the-look-the-screens-tab-page.md).

Créer votre propre skin se résume à quatre choses :

1. copier le fichier standard `skin.config` dans votre dossier de données QuizXpress ;
2. ajouter votre propre définition de skin qui hérite d'un des skins intégrés ;
3. ne remplacer que les paramètres que vous souhaitez modifier ;
4. placer vos propres visuels (images PNG) dans un dossier propre à votre skin.

Cette page explique le fonctionnement des skins. [Créer un skin personnalisé](creating-a-custom-skin.md) vous guide pas à pas, et [Partager, mettre à jour et dépanner](maintaining-a-custom-skin.md) traite de ce qui vient ensuite.

Les paramètres individuels (couleurs, polices, images, tailles) ne sont pas décrits dans ce manuel : chacun est documenté dans un commentaire placé directement au-dessus de son élément dans `skin.config` lui-même.

!!! warning "Not in the Home edition"
    Les skins personnalisés ne sont pas disponibles dans l'édition Home de QuizXpress. Dans l'édition Home, le lecteur de quiz utilise toujours les skins intégrés, même lorsqu'un skin 'User.' est sélectionné.

## Le fichier skin.config

Une grande partie de l'apparence du lecteur de quiz est définie dans un fichier texte XML nommé `skin.config`. Chaque skin que vous pouvez choisir dans Quiz Setup est un élément `<skin>` de ce fichier. Chaque skin contient des éléments pour les différentes parties du show, tels que `<welcomescreen>`, `<quizscreen>`, `<scorescreen>`, `<infopanel>` ou `<pinindicator>`, et leurs attributs contiennent les couleurs, les polices, les images et les dimensions.

![La structure de premier niveau de skin.config, skins repliés](../../assets/images/skinning-skin-config-structure.webp){ loading=lazy }

Chaque élément est documenté dans le commentaire (affiché en vert dans Notepad++) situé directement au-dessus. Le commentaire en haut du fichier explique comment saisir les valeurs : couleurs (noms, RVB, ARVB ou hexadécimal comme `#7A6699`), polices (`"Arial Bold"` ou `"Arial Bold, 22"`), rectangles, booléens et positions 3D.

![Chaque élément est documenté directement au-dessus, ici l'écran d'accueil](../../assets/images/skinning-skin-config-documentation.webp){ loading=lazy }

Pour modifier le fichier, nous recommandons [Notepad++](https://notepad-plus-plus.org/), un éditeur gratuit avec coloration syntaxique XML. N'importe quel éditeur de texte brut convient, mais n'utilisez jamais un traitement de texte.

## Le fichier installé et votre propre copie

QuizXpress connaît deux emplacements pour `skin.config` :

| Emplacement | Description |
|---|---|
| `C:\Program Files (x86)\Game Show Crew\QuizXpress\skin.config` | Les skins intégrés. **Ne modifiez pas ce fichier** : chaque mise à jour de QuizXpress le remplace. |
| `%appdata%\QuizXpress\skin.config` (par exemple `C:\Users\<you>\AppData\Roaming\QuizXpress`) | Votre propre copie. Quiz Setup répertorie chaque skin de ce fichier avec le préfixe 'User.', de sorte qu'ils n'entrent jamais en conflit avec les skins intégrés. |

!!! note
    Lorsque vous sélectionnez un skin 'User.', le lecteur de quiz lit **uniquement votre copie** de `skin.config`, y compris les skins intégrés dont votre skin hérite. C'est pourquoi vous copiez le fichier entier plutôt que d'écrire un fichier contenant seulement votre propre skin. Voir [Après une mise à jour de QuizXpress](maintaining-a-custom-skin.md#apres-une-mise-a-jour-de-quizxpress) pour savoir ce que cela implique lors d'une mise à jour.

## Héritage : ne modifier que ce qui est différent

Un skin peut désigner un skin 'parent'. Lorsque le lecteur de quiz charge un skin, il charge d'abord le parent complet (puis le parent du parent, et ainsi de suite), puis applique par-dessus les éléments du skin lui-même. Cela fonctionne attribut par attribut : un attribut que vous indiquez remplace la valeur héritée, un attribut que vous omettez conserve la valeur héritée. La valeur `default` conserve elle aussi la valeur héritée.

Les skins intégrés fonctionnent déjà ainsi. Techno hérite de Dark Theme, qui hérite de QuizXpress Classic :

```text
QuizXpress (QuizXpress Classic)   - the root skin, defines every setting
├── QuizXpress 2022
├── TVShow (TV Show)
└── DarkMode (Dark Theme)
    └── Techno
```

Choisissez donc comme parent de votre skin le skin intégré le plus proche de ce que vous voulez, et ne placez dans votre propre skin que les éléments et attributs que vous souhaitez modifier. Il reste ainsi léger et facile à maintenir.

## Où le lecteur de quiz cherche les images

Les images et autres ressources sont référencées dans `skin.config` par leur nom de fichier, par exemple `background-image="strip.png"`. Chaque skin possède un attribut 'dir' qui désigne son dossier de ressources. Le lecteur de quiz recherche une image dans l'ordre suivant et utilise le premier fichier trouvé :

1. Si l'attribut contient un chemin complet (`C:\...\logo.png`) : exactement ce fichier.
2. Le dossier de ressources de votre propre skin.
3. Le dossier de ressources de son parent, puis du grand-parent, et ainsi de suite.
4. Le dossier par défaut général `Data\IQ\default` dans le dossier d'installation.

Un 'dir' peut être un chemin complet ou relatif. Un 'dir' relatif est d'abord recherché sous `Data\IQ` dans le dossier d'installation (c'est là que les skins intégrés conservent leurs images, par exemple `Data\IQ\QuizXpress 2022`), puis sous votre dossier de données `%appdata%\QuizXpress`.

Résultat pratique : **une image que vous placez dans le dossier de votre skin sous le même nom de fichier qu'une image du skin parent la remplace automatiquement**, et chaque image que vous ne remplacez pas provient toujours du parent.
