# Créer un skin personnalisé

Dans les étapes ci-dessous, nous créons un skin nommé 'QuizXpress 2023', basé sur le skin intégré 'QuizXpress 2022'. Remplacez ces noms par les vôtres. Si vous ne l'avez pas encore lu, [Skinning](index.md) explique le fonctionnement des skins.

## Étape 1 : ouvrir le dossier de données de QuizXpress

Dans QuizXpress Studio, accédez à l'onglet 'HOME', ouvrez le menu 'Advanced' et choisissez 'Browse Datafolder'. Une fenêtre de l'Explorateur Windows s'ouvre sur le dossier de données. Vous pouvez également saisir `%appdata%\QuizXpress` dans la barre d'adresse de l'Explorateur Windows.

![Onglet HOME, menu Advanced, Browse Datafolder](../../assets/images/skinning-browse-datafolder.webp){ width="400" loading=lazy }

## Étape 2 : copier skin.config dans le dossier de données

Copiez `skin.config` du dossier d'installation (`C:\Program Files (x86)\Game Show Crew\QuizXpress`) vers le dossier de données. Copiez-le, ne le déplacez pas.

Ouvrez Quiz Setup, accédez à l'onglet 'Screens' et ouvrez la liste 'Selected skin' dans la section 'Appearance'. Chaque skin intégré apparaît désormais une seconde fois avec le préfixe 'User.' : ces entrées proviennent de votre copie.

![Les skins de votre copie apparaissent avec le préfixe User.](../../assets/images/skinning-user-skins-in-quiz-setup.webp){ loading=lazy }

!!! tip
    Pour garder la liste ordonnée, ajoutez `hidden="true"` aux éléments `<skin>` des skins intégrés dans **votre copie**. Les skins masqués n'apparaissent plus dans Quiz Setup, mais continuent de fonctionner comme parent de votre propre skin.

## Étape 3 : créer un dossier pour vos visuels

Dans le dossier de données, créez un dossier `Skins`, et dans celui-ci un dossier portant le nom de votre skin : `%appdata%\QuizXpress\Skins\QuizXpress 2023`. Laissez-le vide pour le moment.

## Étape 4 : ajouter la définition de votre skin

Ouvrez le `skin.config` copié (celui du dossier de données) dans votre éditeur. À la fin du fichier, juste au-dessus de la balise fermante `</skins>`, ajoutez :

```xml
<skin name="QuizXpress 2023"
      displayname="QuizXpress 2023"
      dir="Skins\QuizXpress 2023"
      parent="QuizXpress 2022">

</skin>
```

Les attributs de l'élément `<skin>` :

| Attribut | Signification |
|---|---|
| `name` | Nom interne. Doit être unique dans le fichier ; c'est le nom que les autres skins utilisent comme 'parent'. |
| `displayname` | Le nom affiché dans Quiz Setup (avec le préfixe 'User.'). Facultatif ; s'il est omis, le 'name' est affiché. |
| `dir` | Le dossier de ressources du skin. Utilisez le chemin relatif `Skins\<your skin>` : il est recherché dans votre dossier de données et fonctionne tel quel sur un autre ordinateur ou un autre compte utilisateur. Un chemin complet fonctionne aussi. |
| `parent` | Le 'name' (et non le nom affiché) du skin dont hériter, par exemple `QuizXpress 2022`, `DarkMode`, `TVShow` ou `Techno`. Facultatif, mais fortement recommandé. |
| `hidden` | `true` masque le skin dans Quiz Setup. Facultatif. |

Enregistrez le fichier.

## Étape 5 : sélectionner le skin dans Quiz Setup

Rouvrez Quiz Setup (il lit la liste des skins au démarrage), sélectionnez 'User.QuizXpress 2023' dans la liste 'Selected skin' et enregistrez les paramètres. Désormais, le lecteur de quiz utilise votre skin. Comme le skin est encore vide, il est identique à son parent.

![Sélection de votre propre skin dans Quiz Setup](../../assets/images/skinning-select-custom-skin.webp){ width="400" loading=lazy }

## Étape 6 : remplacer des paramètres

Apportez maintenant les modifications qui définissent votre skin. Repérez l'élément que vous souhaitez modifier dans le skin parent, ou dans 'QuizXpress' (le skin racine, qui contient tous les paramètres avec leur documentation), copiez-le dans votre propre skin et ne conservez que les attributs que vous modifiez.

Par exemple, nous voulons un arrière-plan violet pour l'indicateur de PIN (le panneau qui affiche le PIN de la partie pendant le quiz). Dans le skin racine, nous trouvons :

```xml
<pinindicator
    background-color="#01539F"
    text-font-family="default"
    pin-font-family="default"
/>
```

Nous voulons uniquement changer la couleur d'arrière-plan ; nous n'ajoutons donc que cet attribut à notre skin :

```xml
<skin name="QuizXpress 2023" displayname="QuizXpress 2023"
      dir="Skins\QuizXpress 2023" parent="QuizXpress 2022">

    <pinindicator background-color="Purple" />

</skin>
```

Les polices conservent les valeurs héritées du parent. Lancez un quiz : l'indicateur de PIN est maintenant violet :

![L'indicateur de PIN avec la nouvelle couleur d'arrière-plan](../../assets/images/skinning-pin-indicator-purple.webp){ width="220" loading=lazy }

Procédez de la même manière pour tout le reste : ajoutez l'élément une seule fois à votre skin et placez-y tous les attributs que vous modifiez pour cet élément.

!!! note
    Le lecteur de quiz lit `skin.config` au démarrage. Après avoir enregistré une modification, arrêtez le quiz et relancez-le pour voir le résultat.

## Étape 7 : remplacer des images

Les images intégrées d'un skin se trouvent dans son dossier sous `Data\IQ` dans le dossier d'installation. Les images de QuizXpress 2022, le parent de notre exemple, se trouvent dans `Data\IQ\QuizXpress 2022` :

![Les ressources d'images du skin QuizXpress 2022](../../assets/images/skinning-skin-assets-folder.webp){ loading=lazy }

Il existe deux façons d'utiliser vos propres visuels.

**Remplacer une image par son nom.** C'est la méthode la plus simple et elle ne nécessite aucune modification de `skin.config` :

- Repérez l'image que vous souhaitez modifier dans le dossier du parent. Si elle n'y est pas, cherchez dans le dossier du grand-parent, par exemple `Data\IQ\QuizXpress`.
- Copiez-la dans le dossier de votre skin, `%appdata%\QuizXpress\Skins\QuizXpress 2023`, en conservant le nom du fichier.
- Modifiez la copie dans votre éditeur d'images préféré. Conservez les mêmes dimensions en pixels et enregistrez-la au format PNG (avec transparence là où l'original en a).

Comme le dossier de votre skin est parcouru avant celui du parent, votre image est utilisée automatiquement.

**Référencer une image explicitement.** Si vous préférez vos propres noms de fichiers, définissez l'attribut dans votre skin. Par exemple, pour l'arrière-plan du panneau d'informations :

```xml
<infopanel background-image="infopanel_bg.png" />
```

Le lecteur de quiz recherche maintenant `infopanel_bg.png` dans le dossier de votre skin. Vous pouvez aussi saisir un chemin complet. Pour revenir à l'image intégrée, utilisez la valeur `default`.

Lancez un quiz et vérifiez que vos images s'affichent. Si une image est introuvable, le lecteur de quiz affiche l'image intégrée, ou aucune : voir [Dépannage](maintaining-a-custom-skin.md#depannage).
