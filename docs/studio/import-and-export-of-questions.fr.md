# Import et export de questions

Dans QuizXpress Studio, vous pouvez importer depuis différentes sources et exporter vers celles-ci. Pour cela, cliquez sur l'onglet de ruban FILE, puis sur Import ou Export pour afficher les options.

## Import au format Excel

QuizXpress Studio permet d'importer des questions depuis Microsoft Excel. Vous trouverez peut-être plus pratique de saisir vos questions dans Excel (bien que QuizXpress Studio dispose également d'une vue tabulaire pour saisir rapidement des questions), ou vous disposez peut-être d'une base de données de questions exportable vers Excel.

QuizXpress Studio prend en charge le format de fichier natif Office 2007 .xlsx ainsi que le format CSV (fichier texte séparé par des virgules). Le format .xlsx est à privilégier, car il pose moins de problèmes de localisation, de caractères spéciaux, etc.

Pour définir vos questions dans Excel, ouvrez le modèle préinstallé *quiztemplate.xlsx* (vous trouverez ce fichier dans le dossier d'installation de QuizXpress). Vous pouvez également ouvrir le modèle depuis le menu backstage, dans la section ‘Import’. Ci-dessous, le modèle rempli avec quelques questions musicales, chacune avec une vidéo d'arrière-plan et certaines avec une vidéo :

![Le modèle Excel avec des exemples de questions musicales](../assets/images/excel-template.webp){ loading=lazy }

La première ligne est obligatoire et doit respecter les noms d'en-tête ci-dessous :

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Colonne</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Q</td>
<td>Colonne contenant le texte de la question. Si vous souhaitez importer une langue principale et une langue secondaire, séparez le texte des deux langues par || .</td>
</tr>
<tr class="even">
<td>A1-A6</td>
<td><p>Colonnes contenant les réponses des questions à choix multiple. La bonne réponse doit se trouver dans la colonne A1 ; le système mélange les réponses pour vous. Vous pouvez laisser toutes les colonnes A* vides pour une question ouverte, ou ne remplir que A1 et A2 pour une question à choix multiple à deux réponses, etc.</p>
<p>Vous pouvez également indiquer explicitement la bonne réponse des questions à choix multiple en la plaçant entre crochets (‘[‘ et ‘]’). Dans ce cas, le système ne mélange pas les réponses. Si vous souhaitez importer une langue principale et une langue secondaire, séparez le texte des deux langues par ||.</p></td>
</tr>
<tr class="odd">
<td>CAT</td>
<td>Un nom de catégorie facultatif. Les questions importées seront automatiquement mises en forme selon cette catégorie. Si vous souhaitez utiliser votre propre catégorie, vous devez la créer dans le quiz avant l'import.</td>
</tr>
<tr class="even">
<td>P1-P6</td>
<td>Nom de fichier facultatif d'un fichier image. Il peut s'agir du chemin absolu (complet) du fichier, ou d'un simple nom de fichier si le fichier image se trouve dans le même dossier que le fichier XLSX importé. Les formats de fichier pris en charge sont <em>jpg, png, bmp, wmf, emf</em> et <em>gif.</em> Vous pouvez également indiquer explicitement l'image de la bonne réponse des questions à choix multiple en plaçant le nom du fichier image entre crochets (‘[‘ et ‘]’).</td>
</tr>
<tr class="odd">
<td>NOTES</td>
<td>Les notes facultatives de l'animateur de quiz à ajouter à la question</td>
</tr>
<tr class="even">
<td>SOUND</td>
<td>Un chemin facultatif vers un fichier son à ajouter à la question</td>
</tr>
<tr class="odd">
<td>VIDEO</td>
<td>Un chemin facultatif vers un fichier vidéo (WMV, AVI, etc.) à ajouter à la question (ne peut pas être utilisé avec P1-P4). Laissez tous les autres champs vides pour obtenir une diapositive vidéo en plein écran.</td>
</tr>
<tr class="even">
<td>BACKGROUND</td>
<td>Un chemin facultatif vers une image d'arrière-plan pour la diapositive (png, jpg, bmp, etc.)</td>
</tr>
<tr class="odd">
<td>BACKGROUND-VIDEO</td>
<td>Un chemin facultatif vers une vidéo qui se joue derrière la diapositive (voir <a href="../backgrounds/">Vidéo d'arrière-plan</a>). Elle n'utilise pas d'emplacement réservé, elle peut donc être combinée avec des images (P1-P6) ou une VIDEO. Lorsque la question a une catégorie avec une vidéo d'arrière-plan, la vidéo de cette colonne la remplace pour cette question.</td>
</tr>
</tbody>
</table>

Les classeurs créés avec un ancien modèle, sans la colonne BACKGROUND-VIDEO, peuvent toujours être importés.

En plus de cet ensemble fixe de colonnes, il existe un certain nombre de colonnes personnalisables que vous pouvez choisir dans la liste déroulante du modèle Excel :

| Colonne              | Description                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| A7                   | Définit la réponse 7. À utiliser pour l'import Trivia Feud                                                                                  |
| A8                   | Définit la réponse 8. À utiliser pour l'import Trivia Feud                                                                                  |
| POINTS-START         | Points à gagner au début du compte à rebours                                                                                                |
| POINTS-END           | Points à gagner à la fin du compte à rebours                                                                                                |
| PENALTY-POINTS-START | Points de pénalité au début du compte à rebours                                                                                             |
| PENALTY-POINTS-END   | Points de pénalité à la fin du compte à rebours                                                                                             |
| NO-ANSWER-POINTS     | Points de pénalité en l'absence de réponse                                                                                                  |
| BONUS-POINTS-1       | Points bonus pour le joueur le plus rapide avec une bonne réponse                                                                           |
| BONUS-POINTS-2       | Points bonus pour le deuxième joueur le plus rapide avec une bonne réponse                                                                  |
| BONUS-POINTS-3       | Points bonus pour le troisième joueur le plus rapide avec une bonne réponse                                                                 |
| ANSWER-TIME          | Temps de réponse en secondes                                                                                                                |
| STYLE                | Nom du style de diapositive (voir les info-bulles du sélecteur de styles de Studio pour les noms corrects ; par exemple : Millionaire, Neon Tubes, etc.) |
| TRANSITION           | Le nom de la transition de diapositive. Valeurs valides : Default, None, MoveRight, MoveLeft, MoveToFront, PageTurnLeft, ScaleToZero, LiftAndMoveRight, Fade |
| SHUFFLEMODE          |                                                                                                                                             |
| EVALUATION-MODE      |                                                                                                                                             |
| NEAREST-WINS-WINNERS |                                                                                                                                             |
| TEXT-EVALUATION      |                                                                                                                                             |
| TOLERANCE            |                                                                                                                                             |
| END-OF-ROUND-ACTION  |                                                                                                                                             |

Enregistrez le fichier dans Excel, puis sélectionnez ‘FILE->Import->Import from Excel’ dans QuizXpress Studio. Un explorateur de fichiers s'affiche, dans lequel vous pouvez sélectionner le fichier Excel à importer.

En fonction des colonnes que vous remplissez, QuizXpress sélectionne automatiquement une mise en page de diapositive adaptée. Par exemple, pour obtenir une question à choix multiple à 3 réponses avec une vidéo, remplissez les colonnes Q, A1, A2, A3 et VIDEO. Pour obtenir une question ouverte avec un extrait sonore, une image et une image d'arrière-plan, remplissez les colonnes Q, P1, SOUND et BACKGROUND.

Par défaut, toutes les diapositives sont créées comme des questions de quiz. Vous pouvez toutefois préciser le type de diapositive à créer en faisant précéder le texte de la colonne Q de l'un des identifiants suivants :

| Préfixe | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {Q}    | Crée une question normale. Vous pouvez utiliser les qualificatifs supplémentaires suivants pour préciser la création de la question : **EA** – Everyone Answers, **FF** – Fastest Finger, **NUM** – crée une question numérique, **LET** – crée une question à lettre, **TXT** – crée une question à texte libre, **CA** – Countdown Automatically, **CM** – Countdown Manual. Par exemple, **{Q, EA, CM}** crée une question à laquelle tout le monde peut répondre (vote), avec démarrage manuel du compte à rebours. |
| {T}    | Crée une question de test                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| {W}    | Crée une diapositive de mise (vous devez également indiquer deux pourcentages ou plus dans les réponses, comme ‘20%’)                                                                                                                                                                                                                                                                                                                                                         |
| {B}    | Crée une diapositive d'affichage (statique)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| {A}    | Crée une diapositive de réponse du public                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| {D}    | Crée une diapositive démographique                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| {L}    | Crée une diapositive last-man-standing                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| {E}    | Crée une diapositive de fin de manche                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| {M}    | Crée une diapositive Majority Rules                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {J}    | Crée une diapositive Trivia Board                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| {TL}   | Crée une diapositive Trivia Ladder                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| {TF}   | Crée une diapositive Trivia Feud (utilisez A1..A8 pour les entrées du sondage)                                                                                                                                                                                                                                                                                                                                                                                               |
| {SR}   | Crée une diapositive Speed Round (doit se terminer par une diapositive de fin de manche)                                                                                                                                                                                                                                                                                                                                                                                     |

Ainsi, par exemple, le texte « {A}Aimez-vous cette soirée quiz ? » importe une diapositive Audience Response avec le texte « Aimez-vous cette soirée quiz ? »

Le son et la vidéo insérés dans votre diapositive à l'aide des colonnes SOUND, VIDEO et BACKGROUND-VIDEO sont normalement intégrés, ce qui signifie que tout le contenu du fichier son/vidéo est stocké dans le fichier du quiz. Cela peut produire des fichiers de quiz volumineux. Pour l'éviter, vous pouvez faire précéder les valeurs de ces colonnes de ‘{L}’ afin d'indiquer que vous souhaitez lier les fichiers multimédias. Par exemple : « {L} C:\Users\Public\Videos\Sample Videos\Wildlife.wmv ». Notez que les fichiers liés doivent rester présents sur votre système lors de l'exécution du quiz. Lorsque plusieurs questions utilisent le même fichier vidéo d'arrière-plan, celui-ci n'est stocké qu'une seule fois dans le quiz.

Vous pouvez ajouter des paramètres à une vidéo dans la colonne VIDEO ou BACKGROUND-VIDEO en les plaçant entre accolades après le nom du fichier, séparés par des points-virgules. Par exemple : « intro.mp4{loop=false;sync-with-quiz=true} ». Les paramètres que vous omettez conservent leur valeur par défaut.

| Paramètre      | Description                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
| start-at       | Où la vidéo démarre, par exemple 00:00:05                                                                                 |
| stop-at        | Où la vidéo s'arrête, par exemple 00:00:20                                                                                |
| loop           | true ou false : relancer la vidéo lorsqu'elle se termine. Par défaut : true pour une vidéo d'arrière-plan, false pour une vidéo dans un emplacement réservé |
| silent         | true ou false : lecture sans son. Par défaut : true pour une vidéo d'arrière-plan, false pour une vidéo dans un emplacement réservé |
| volume         | Volume de 0 à 100 (100 par défaut)                                                                                        |
| speed          | Vitesse de lecture en pourcentage, de 25 à 250 (100 par défaut)                                                           |
| effect         | Un effet vidéo, tel que Blur ou Mosaic                                                                                    |
| intro-pause    | VIDEO uniquement : secondes d'attente avant le démarrage de la vidéo (1 par défaut)                                       |
| sync-with-quiz | BACKGROUND-VIDEO uniquement : true pour mettre la vidéo d'arrière-plan en pause en même temps que le quiz (false par défaut) |

Vous pouvez créer des manches dans votre quiz en ajoutant plusieurs feuilles de calcul au classeur Excel. Pour chaque feuille de calcul, une diapositive de quiz de type ‘billboard’ est insérée dans le quiz, contenant le nom de la feuille de calcul pour annoncer la manche suivante. Par exemple, supposons que vous ayez deux feuilles de calcul, ‘Round 1’ et ‘Round 2’, contenant chacune dix questions. Lors de l'import du fichier Excel dans QuizXpress Studio, vous obtenez un quiz contenant : un billboard avec le texte ‘Round 1’, suivi de dix questions, suivi d'un billboard avec le texte ‘Round 2’, de nouveau suivi de dix questions.

## Export vers Excel

‘FILE->Export->Export to Excel’ enregistre les questions de votre quiz dans le même format, sous forme de fichier CSV qui s'ouvre dans Excel et peut être importé à nouveau. Les images, sons et vidéos sont enregistrés à côté du fichier CSV. Les sons et les vidéos conservent le nom de leur fichier d'origine, et un fichier partagé par plusieurs questions, comme la vidéo d'arrière-plan d'une catégorie, n'est enregistré qu'une seule fois. Pour les vidéos, seuls les paramètres qui diffèrent de la valeur par défaut sont écrits.

## Import depuis PowerPoint

QuizXpress Studio permet également d'importer des questions depuis PowerPoint. Dans ce cas, les diapositives PowerPoint sont importées sous forme d'images et placées sur des diapositives Billboard. Si vous souhaitez transformer des diapositives en questions, un post-traitement est nécessaire : définissez d'abord le type de diapositive sur ‘Question’, puis, s'il s'agit de réponses à choix multiple, modifiez la mise en page de la diapositive pour inclure le même nombre de réponses, définissez le style de la diapositive sur ‘Just Text’ et supprimez les textes des questions et des réponses dans QuizXpress Studio.

## Import depuis Spotify™

Cette fonction vous permet de transformer vos playlists préférées en quiz musical QuizXpress ou en bingo musical presque sans effort. Spotify expose environ 30 secondes du morceau (prédéfinies) et une image de la pochette de l'album. Il y a deux étapes simples : vous exportez d'abord votre playlist vers un fichier séparé par des virgules (csv) avec Exportify, un site web public accessible à l'adresse : <https://exportify.app/> . Ensuite, vous importez ce fichier csv dans QuizXpress Studio à l'aide de la fonction d'import Excel. Le système reconnaît le format et vous présente le formulaire d'options suivant :

![](../assets/images/image255.webp){ width="270" loading=lazy }

Vous y indiquez ce que vous souhaitez créer, ainsi que plusieurs options. Dans cet exemple, nous créons un bingo musical de 75 diapositives : la moitié des cases du bingo seront composées de pochettes d'album, et le reste sera du texte avec Artiste/Titre. Après l'import, les extraits musicaux de 30 secondes se trouveront sur les diapositives, et un exemple de carte de bingo ressemblera à ceci :

![](../assets/images/image256.webp){ loading=lazy }

De la même manière, vous pouvez créer un quiz musical avec des questions.

![](../assets/images/image257.webp){ loading=lazy }

!!! note

    veillez à ne violer aucun droit d'auteur lorsque vous utilisez cette fonction.*

## Import depuis QuizXpress

Si vous souhaitez ajouter les questions d'un quiz QuizXpress existant à un quiz que vous êtes en train de créer, cliquez sur le bouton *Import from QuizXpress* et sélectionnez un fichier QuizXpress. Vous pouvez aussi ouvrir deux instances de QuizXpress Studio et copier-coller des diapositives de l'une à l'autre.

## Export vers PDF

QuizXpress Studio vous permet d'exporter vos questions au format PDF. Ce fichier PDF peut être imprimé ou envoyé à vos clients pour leur donner un aperçu du quiz. Votre animateur de quiz peut également souhaiter en recevoir une version imprimée avant le jeu télévisé. L'export PDF est disponible via ‘FILE->Export->Export to PDF’. *(Remarque : cette option n'est pas disponible dans l'édition Home).* L'export PDF propose les options suivantes :

![](../assets/images/image258.webp){ width="370" loading=lazy }

| Champ                     | Description                                                          |
|---------------------------|----------------------------------------------------------------------|
| Target PDF File           | Le fichier PDF de sortie. Utilisez le bouton \[…\] pour naviguer jusqu'à un dossier/fichier |
| Logo on first page        | Le logo qui sera affiché sur la première page du PDF                 |
| Include slides            | Activer pour inclure des images des diapositives                     |
| Include questions as text | Inclure un aperçu textuel des questions et des réponses              |
| Show correct answers      | Inclure les bonnes réponses dans le résultat.                        |
| Include question numbers  | Inclure les numéros de question dans l'export PDF                    |
| Page options              | Permet de combiner plusieurs diapositives sur une page               |

!!! note

    pour pouvoir lire des documents PDF sur votre ordinateur, vous avez besoin du lecteur Adobe PDF, disponible en téléchargement à l'adresse <http://get.adobe.com/reader/>*

## Export vers HTML

Vous pouvez exporter un quiz au format HTML pour l'exécuter sur un site web. Notez que cette fonctionnalité est très basique : entre autres, les effets audio, vidéo et image ne sont pas pris en charge, et bien qu'un score soit affiché, il n'y a pas d'annonce du score final.
