# Advanced properties grid

Le volet des propriétés est l’endroit où vous pouvez rapidement définir toutes les propriétés détaillées du ou des éléments sélectionnés. Chaque élément (comme une question, une réponse, une diapositive, une vidéo ou une image) possède ses propres propriétés. Il n’est pas indispensable de l’utiliser, car les réglages les plus importants sont accessibles depuis le ruban, mais pour les utilisateurs avancés, cela peut être un moyen plus rapide d’arriver à ses fins. (certaines propriétés plus avancées ou plus obscures ne sont accessibles que depuis le volet des propriétés). Dans les chapitres suivants, vous trouverez une explication des propriétés les plus importantes. Vous pouvez afficher le volet des propriétés en allant dans le menu VIEW et en cochant ‘Properties’ (dans la section ‘Views’).

QuizXpress affiche ces propriétés dans le **panneau des propriétés**, que vous obtenez par défaut, et propose toujours la **grille de propriétés classique** utilisée par les versions précédentes. Les deux affichent exactement les mêmes propriétés et vous pouvez passer de l’une à l’autre quand vous le souhaitez ; les chapitres ci-dessous s’appliquent donc aux deux.

## Le panneau des propriétés

![](../../assets/images/properties-panel-overview.webp){ width="322" loading=lazy }

Au lieu d’une longue liste alphabétique, le panneau regroupe les propriétés de l’élément sélectionné en pages et en sections, et attribue à chaque propriété un contrôle adapté : un interrupteur pour un réglage oui/non, un curseur pour une transparence, un échantillon de couleur pour une couleur, etc. Tout ce que vous modifiez est appliqué immédiatement à la diapositive.

**Ce qui est sélectionné**

Le haut du panneau indique ce que vous modifiez : une icône, le type de l’élément et une seconde ligne avec son contenu (le texte d’une réponse, le nom de fichier d’une image). Lorsque vous sélectionnez plusieurs éléments à la fois — par exemple les quatre réponses d’une question — le titre indique ‘4 objects selected’ et le panneau affiche les propriétés qu’ils ont en commun. Les propriétés dont les valeurs diffèrent entre les éléments sélectionnés apparaissent vides ou avec ‘Mixed’ ; dès que vous en définissez une, tous les éléments sélectionnés reçoivent la nouvelle valeur.

**Pages**

Sous la zone de recherche se trouve une rangée de pages : *Gameplay*, *Scoring*, *Design*, *Text*, *Media* et *Advanced*. Seules les pages qui possèdent réellement des propriétés pour la sélection en cours sont affichées, et la page la plus pertinente pour l’élément sélectionné vient en premier — la page *Text* pour un élément de texte, *Gameplay* pour une diapositive de quiz. La page *Advanced* (l’onglet `{}`) rassemble les propriétés techniques : métadonnées, paramètres des appareils mobiles et scripts. Cliquez sur un onglet pour changer de page ; le panneau mémorise votre choix pour chaque type d’élément.

**Sections et options supplémentaires**

Chaque page est divisée en sections telles que ‘Timing’, ‘Answering’ ou ‘Border’. Cliquez sur le titre d’une section pour la replier, et utilisez *Expand all sections* / *Collapse all sections* dans le menu d’options pour toutes les replier ou les déplier d’un coup. Les sections qui contiennent aussi des propriétés rarement utilisées affichent un lien **More options** en bas ; cliquez dessus pour les révéler et sur **Fewer options** pour les masquer à nouveau. Le panneau mémorise les sections que vous avez repliées et celles qui affichent leurs options supplémentaires.

**Trouver une propriété**

![](../../assets/images/properties-panel-search.webp){ width="322" loading=lazy }

Si vous ne savez pas où se trouve une propriété, saisissez un mot dans la zone de recherche en haut (ou appuyez sur *Ctrl+F*). Le panneau affiche alors toutes les propriétés correspondantes de toutes les pages en même temps, avec la partie correspondante du nom en surbrillance. La recherche porte aussi sur les descriptions : un mot qui n’apparaît que dans l’explication d’une propriété permet donc de la retrouver. Cliquez sur le ✕ dans la zone de recherche pour revenir à l’affichage normal.

### Modifier les valeurs

![](../../assets/images/properties-panel-text-editors.webp){ width="322" loading=lazy }

La plupart des propriétés se comprennent d’elles-mêmes : saisir dans une zone, actionner un interrupteur, choisir dans une liste déroulante. Quelques-unes méritent d’être signalées.

Les **nombres** peuvent être saisis, modifiés pas à pas avec les petites flèches à droite de la zone ou — souvent plus rapidement — en *faisant glisser le nom de la propriété* vers la gauche ou la droite. Maintenez *Shift* enfoncée pendant le glissement pour des pas plus grands et *Alt* pour des pas plus fins. Les propriétés qui ont un minimum et un maximum raisonnables, comme une transparence, reçoivent un curseur accompagné d’une zone numérique ; les deux restent synchronisés.

Les **polices** se définissent avec une liste déroulante qui affiche un aperçu de chaque police installée, une zone de taille et des boutons pour le gras, l’italique et le souligné.

Les **propriétés groupées**, comme un dégradé ou une taille, affichent un résumé sur une seule ligne. Cliquez sur le nom de la propriété pour déplier en dessous les réglages individuels (pour un dégradé : From, To et Type).

### Couleurs

![](../../assets/images/properties-panel-color-picker.webp){ width="333" loading=lazy }

Une propriété de couleur affiche un échantillon avec sa valeur hexadécimale. Cliquez dessus et vous obtenez :

- **No color**, pour les propriétés qui peuvent rester vides (un arrière-plan transparent, par exemple).
- Une **palette** de teintes en haut et une rangée de **Standard colors** en dessous.
- **Recent colors** — les couleurs que vous avez utilisées précédemment, de sorte que reprendre une couleur sur plusieurs éléments ne demande qu’un clic. Elles sont mémorisées tant que QuizXpress Studio est en cours d’exécution.
- **Custom color**, qui déplie un carré saturation/luminosité, une barre de teinte, une barre d’opacité et une zone où vous pouvez saisir ou coller une valeur hexadécimale telle que `#1E4A6B`.

La petite pipette à droite du titre ‘Custom color’ prélève une couleur **n’importe où sur votre écran** — y compris en dehors de QuizXpress. Cliquez dessus et l’écran se fige ; une loupe suit votre souris et montre les pixels individuels avec la couleur sous le curseur. Cliquez pour prendre cette couleur, utilisez les touches fléchées pour vous déplacer d’un pixel à la fois (maintenez *Shift* pour dix), ou appuyez sur *Esc* pour annuler. Comme l’écran n’a pas de transparence, l’opacité de la couleur que vous aviez est conservée.

### Dégradés

![](../../assets/images/properties-panel-gradient-presets.webp){ width="313" loading=lazy }

Une propriété de dégradé affiche un aperçu du dégradé. À côté se trouve un bouton en forme de palette qui ouvre un ensemble de **gradient presets** prêts à l’emploi — un clic donne à l’arrière-plan d’une diapositive ou à une zone de texte un aspect abouti. Pour conserver un dégradé que vous avez créé vous-même, faites un clic droit sur la propriété de dégradé et choisissez *Add to my gradients* ; il apparaît ensuite sous **My gradients** dans le sélecteur (jusqu’à cinq). Faites un clic droit sur l’un de vos propres dégradés dans le sélecteur pour le supprimer. Vos dégradés sont conservés d’une session à l’autre.

### Réinitialiser, copier et coller

Faites un clic droit sur n’importe quelle propriété pour obtenir :

- **Reset to default** — remet la propriété à la valeur qu’elle a dans une nouvelle diapositive.
- **Copy value** et **Paste value** — pratiques pour transférer une couleur, une police ou un dégradé d’un élément à un autre. *Ctrl+C* et *Ctrl+V* font la même chose pour la propriété dans laquelle vous travaillez ; vous pouvez ainsi copier une couleur ici et la coller directement dans un autre programme sous la forme `#1E4A6B`, ou l’inverse.

### Descriptions

![](../../assets/images/properties-panel-descriptions.webp){ width="333" loading=lazy }

Le survol du nom d’une propriété affiche une info-bulle expliquant son rôle. Si vous préférez avoir cette explication en permanence sous les yeux, activez *Show descriptions* dans le menu d’options : une barre apparaît alors en bas du panneau avec le nom et l’explication de la propriété sur laquelle se trouve votre souris.

### Options

![](../../assets/images/properties-panel-options-menu.webp){ width="333" loading=lazy }

Le bouton **…** dans le coin supérieur droit du panneau contient les réglages du panneau lui-même : développer et réduire toutes les sections, afficher les descriptions, le thème sombre et le passage à la grille de propriétés classique.

### Thème sombre

![](../../assets/images/properties-panel-dark-theme.webp){ width="333" loading=lazy }

*Dark theme* dans le menu d’options donne au panneau une palette de couleurs sombres, plus reposante pour les yeux lorsque vous concevez des diapositives claires ou que vous travaillez dans une pièce peu éclairée. Le choix est mémorisé au prochain démarrage de QuizXpress Studio et n’affecte que le panneau des propriétés.

## La grille de propriétés classique

![](../../assets/images/image18.webp){ width="644" loading=lazy }

La grille utilisée par les versions précédentes de QuizXpress est toujours là. Elle répertorie toutes les propriétés de l’élément sélectionné en groupes alphabétiques et constitue le moyen le plus rapide de tout voir d’un seul coup. Choisissez *Classic property grid* dans le menu **…** du panneau des propriétés pour y passer, et le bouton *Switch to the new properties panel* à droite de la barre d’outils propre à la grille pour revenir en arrière. QuizXpress mémorise celle des deux que vous préférez.

## Propriétés des diapositives de quiz

Ces propriétés s’affichent en cliquant sur l’arrière-plan d’une question. Les propriétés sont réparties en différents groupes :

- *Appearance*, définit le rendu de la question.

- *Behavior*, définit le comportement de la question pendant le jeu.

- *General*, propriétés générales.

- *Metadata, métadonnées de cette diapositive (Id et Class)*

- *Points,* section d’attribution des points.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Propriété</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Answer time</td>
<td>La durée du compte à rebours en secondes. Indiquez la valeur 0 pour une question sans limite de temps. Vous pouvez alors terminer la question en appuyant sur la barre d’espace. Le compte à rebours peut être mis en pause en appuyant sur ‘P’ dans QuizXpress Live.</td>
</tr>
<tr class="even">
<td>Auto judge</td>
<td>Ce réglage est valable pour une question de type « doigt le plus rapide » (Voting = no) et à choix multiple. Dans ce cas, le réglage ‘Auto judge’ indique si une question sera jugée automatiquement par QuizXpress Live lorsqu’un bouton de choix multiple est pressé sur un buzzer/keypad (pour les buzzers sans choix multiple, auto-judge est toujours automatiquement réglé sur ‘No’).</td>
</tr>
<tr class="odd">
<td>Auto advance when media ends</td>
<td>Passe automatiquement à la diapositive suivante lorsqu’une vidéo ou un son sur un billboard se termine. Cela aide à créer des quiz qui se déroulent seuls. Cette propriété est disponible lorsqu’il y a un élément multimédia sur la diapositive et que le Type de la diapositive est billboard.</td>
</tr>
<tr class="even">
<td>Background image</td>
<td>L’image d’arrière-plan de la diapositive de quiz.</td>
</tr>
<tr class="odd">
<td>Background stretch mode</td>
<td>Indique comment l’image d’arrière-plan est étirée sur la diapositive. Il peut s’agir de ‘Fill’ pour simplement remplir toute la diapositive avec l’image (le rapport d’aspect n’est pas conservé) ou de ‘Zoom’ pour conserver le bon rapport d’aspect en perdant éventuellement certaines parties de l’image</td>
</tr>
<tr class="odd">
<td>Background video</td>
<td><p>Une vidéo qui est lue derrière la diapositive pendant le quiz. Une image ou une vidéo dans un espace réservé est lue par-dessus. Une fois définie, ces réglages apparaissent en dessous : <em>Video storage type</em> (embedded or linked), <em>Linked file</em> (pour une vidéo liée), <em>Loop</em> (activé par défaut), <em>Silent</em> (activé par défaut) et, sous ‘More options’, <em>Sync with quiz</em> (met la vidéo en pause lorsqu’une équipe buzze, que le compte à rebours est en pause ou que la question se termine).</p>
<p>Sur une catégorie, la vidéo d’arrière-plan est appliquée à chaque diapositive formatée avec cette catégorie. Voir <a href="../../backgrounds/">Background video</a>.</p></td>
</tr>
<tr class="even">
<td>Bonus points</td>
<td>Les points bonus pour le 1<sup>er</sup>, le 2<sup>e</sup> et le 3<sup>e</sup> joueur le plus rapide à répondre correctement.</td>
</tr>
<tr class="odd">
<td>Class</td>
<td>Un texte librement défini par l’utilisateur pour classer le type de diapositive. Ces données seront exportées dans le fichier de scores de l’Analyzer et envoyées à MessageBroker afin de pouvoir être utilisées pour déclencher un comportement particulier</td>
</tr>
<tr class="even">
<td>Category</td>
<td>La catégorie de cette diapositive de quiz. En sélectionnant une catégorie, vous définissez la mise en forme graphique. Remarque : vous pouvez définir vos propres catégories ! Pour une explication des catégories, reportez-vous à la section 3.3</td>
</tr>
<tr class="odd">
<td>Continue after correct answer</td>
<td>Lorsqu’une bonne réponse est donnée à une question de type « doigt le plus rapide » (de type ‘default’, la réponse est donnée oralement et jugée correcte), le compte à rebours continue et les autres joueurs peuvent appuyer (souvent utilisé pour des jeux lors d’un événement se déroulant en dehors d’un quiz).</td>
</tr>
<tr class="even">
<td>Correct answer</td>
<td>La bonne réponse pour cette diapositive. Applicable uniquement lorsque le mode de saisie (voir ci-dessous) est ‘numeric’, ‘letter’ ou ‘text’.</td>
</tr>
<tr class="odd">
<td>Custom HTML Screen</td>
<td>Une page HTML personnalisée à afficher sur les appareils mobiles lorsque cette diapositive est chargée <em>(usage avancé)</em></td>
</tr>
<tr class="even">
<td>Delay before answer</td>
<td>Temps en secondes qui s’écoule avant l’affichage des réponses. Cela permet à l’animateur de quiz de lire la question à voix haute avant que les réponses ne s’affichent.</td>
</tr>
<tr class="odd">
<td>Delay between answers<sup>*</sup></td>
<td>Si ‘Delay before answer’ et ‘hide and show one by one’ ont tous deux été définis, cette propriété apparaît. Elle définit le délai qui s’écoule entre chaque réponse qui apparaît.</td>
</tr>
<tr class="even">
<td>Demographic group<sup>*</sup></td>
<td>Cette propriété peut être définie lorsque le <strong>Type</strong> de la diapositive est ‘Demographic’. Elle définit un groupe démographique. Lorsque le quiz est lancé, les personnes qui appuient sur leur buzzer pendant l’affichage d’une diapositive de quiz démographique appartiendront au groupe indiqué par cette propriété. Reportez-vous également à la section 5.4.5.5 pour plus d’informations sur les groupes démographiques.</td>
</tr>
<tr class="odd">
<td>End of round action<sup>*</sup></td>
<td>Cette propriété peut être définie lorsque le <strong>Type</strong> de la diapositive est ‘End of round’. Ses valeurs possibles sont ‘Disable one loser’, auquel cas le participant ayant le moins de points est éliminé, et ‘Quizmaster selects losers’, auquel cas l’animateur de quiz peut sélectionner un par un les participants qui seront éliminés.</td>
</tr>
<tr class="even">
<td>Evaluation mode</td>
<td>Indique si l’évaluation d’une réponse numérique est ‘exact match’ (la réponse donnée doit correspondre exactement à la bonne réponse de la question) ou ‘nearest wins’ (le joueur le plus proche de la réponse remporte les points indiqués).</td>
</tr>
<tr class="odd">
<td>Gradient</td>
<td>Le dégradé de remplissage de l’arrière-plan de la diapositive. Cette propriété ne s’applique que si vous n’avez pas d’image en arrière-plan. Une couleur de dégradé ‘from’ et une couleur de dégradé ‘to’ peuvent être sélectionnées, ainsi qu’un type de dégradé.</td>
</tr>
<tr class="even">
<td>Id</td>
<td>Un ID unique pour identifier cette diapositive (par exemple pour le routage statique des diapositives avec la propriété <em>Next slide</em>)</td>
</tr>
<tr class="odd">
<td>Input type</td>
<td>Pour une question ouverte, vous pouvez choisir entre ‘default’ (question de type « doigt le plus rapide ») ou une réponse ‘number’, ‘letter’ ou ‘text’. Les trois derniers modes ne s’appliquent que lors de l’utilisation de téléphones mobiles (car les keypads et les buzzers ne proposent pas de saisie numérique ou textuelle).</td>
</tr>
<tr class="even">
<td>Language</td>
<td>La langue d’affichage actuelle (d’édition) de la diapositive pour les quiz bilingues.</td>
</tr>
<tr class="odd">
<td>Lock-out on wrong answer</td>
<td>Définit le mode de blocage pour une question de type « doigt le plus rapide ». Soit le joueur est bloqué après une mauvaise réponse, soit il peut réessayer.</td>
</tr>
<tr class="even">
<td>Multiple correct answers</td>
<td>Indique si cette question a plus d’une bonne réponse et si les bonnes réponses multiples suivent un ordre précis</td>
</tr>
<tr class="odd">
<td>Mute countdown sound</td>
<td>Coupe le son du compte à rebours pour cette question</td>
</tr>
<tr class="even">
<td>Next slide</td>
<td>L’ID de la diapositive à afficher après celle-ci (routage statique des diapositives)</td>
</tr>
<tr class="odd">
<td>Notes</td>
<td>Un texte (indices) destiné à l’animateur de quiz, qui sera inclus dans l’export PDF</td>
</tr>
<tr class="even">
<td>Ordered answer mode</td>
<td>Pour les réponses ordonnées, vous pouvez indiquer si vous voulez que les réponses correspondent exactement à l’ordre (Exact match) ou si une réponse partiellement correcte rapporte aussi des points (un pourcentage des points, selon le nombre de réponses placées au bon endroit).</td>
</tr>
<tr class="odd">
<td>Penalty points end</td>
<td>Nombre de points retirés lorsqu’un participant répond incorrectement à la fin du compte à rebours (interpolation entre début – fin)</td>
</tr>
<tr class="even">
<td>Penalty points start</td>
<td>Nombre de points retirés lorsqu’un participant répond incorrectement au début du compte à rebours</td>
</tr>
<tr class="odd">
<td>Points at end</td>
<td>Nombre de points ajoutés lorsqu’un participant répond correctement à la fin du compte à rebours. Doit être inférieur ou égal à ‘points at start time’. Les points sont interpolés entre le début et la fin du compteur. Ainsi, lorsque les points à la fin sont inférieurs aux points au début, le nombre de points à gagner diminue pendant que le compte à rebours s’écoule. Lorsque les deux valeurs sont égales, les points pouvant être gagnés restent les mêmes tout au long du compte à rebours.</td>
</tr>
<tr class="even">
<td>Points at start</td>
<td>Nombre de points ajoutés lorsqu’un participant répond correctement au début du compte à rebours.</td>
</tr>
<tr class="odd">
<td>Points to lose on no answer</td>
<td>Les points retirés lorsqu’aucune réponse n’est donnée (applicable uniquement aux questions de vote)</td>
</tr>
<tr class="even">
<td>Steal Points</td>
<td>Lorsque l’option steal points est active pour une question de type « doigt le plus rapide » (buzzer), un joueur qui donne une réponse incorrecte ne perd pas de points. À la place, les points de pénalité configurés pour la diapositive sont attribués à tous les autres joueurs et la question se termine immédiatement.</td>
</tr>
<tr class="odd">
<td>Response limit</td>
<td>Le nombre maximum d’équipes dont le système acceptera les réponses. Par exemple, si vous jouez avec 100 équipes, vous pouvez régler cette valeur sur 25 afin que seules les 25 premières équipes puissent répondre à la question.</td>
</tr>
<tr class="even">
<td>Response mode</td>
<td>Indique si cette question n’accepte qu’une seule réponse par joueur ou plusieurs (utilisé en combinaison avec ‘Multiple correct answers’). Si cette option est réglée sur ‘multiple responses, exact match’, la réponse multiple doit correspondre exactement aux bonnes réponses pour gagner des points.</td>
</tr>
<tr class="odd">
<td>Revise answer</td>
<td>Ici, vous pouvez remplacer l’option globale permettant aux joueurs de réviser leur réponse (définie globalement dans Quiz Setup pour toutes les diapositives).</td>
</tr>
<tr class="even">
<td>Safety net<sup>*</sup></td>
<td>Utilisé pour les questions d’échelle de trivia (trivia ladder). Dans une manche d’échelle de trivia, lorsqu’un joueur répond incorrectement, il redescend jusqu’au filet de sécurité le plus proche de l’échelle de trivia.</td>
</tr>
<tr class="odd">
<td>Script</td>
<td>Comportement personnalisé de la diapositive codé en JavaScript <em>(usage avancé)</em></td>
</tr>
<tr class="even">
<td>Show answers action<sup>*</sup></td>
<td>Lorsque ‘Delay before answer’ a été défini, cette propriété apparaît. En la réglant sur ‘hide and show at once’, les réponses sont affichées d’un coup une fois le délai écoulé. En la réglant sur ‘hide and show one by one’, les réponses sont affichées une par une une fois le délai écoulé.</td>
</tr>
<tr class="odd">
<td>Show correct answer</td>
<td>Mode d’affichage de la bonne réponse sur cette diapositive. Soit suivre le réglage global indiqué dans Quiz Setup, soit ne jamais afficher la bonne réponse, soit toujours afficher la bonne réponse.</td>
</tr>
<tr class="even">
<td>Shuffle mode</td>
<td>Détermine ce qui se passe lorsque le quiz est mélangé</td>
</tr>
<tr class="odd">
<td>Start timer</td>
<td>Indique si le minuteur du compte à rebours doit démarrer automatiquement lorsque la question apparaît ou par une action manuelle.</td>
</tr>
<tr class="even">
<td>Steal points</td>
<td>Applicable aux questions de type « doigt le plus rapide ». Lorsque cette option est activée, tous les autres joueurs volent les points du joueur qui a buzzé lorsque la réponse fournie est fausse.</td>
</tr>
<tr class="odd">
<td>Style</td>
<td>Le style de rendu de la question. Vous trouverez plus d’informations sur les styles dans le chapitre « Styles ».</td>
</tr>
<tr class="even">
<td>Text evaluation</td>
<td>Indique si l’évaluation d’une réponse textuelle est ‘exact match’ (la réponse donnée doit correspondre exactement à la bonne réponse) ou ‘fuzzy match’ (un algorithme autorise un certain pourcentage de différence entre la réponse donnée et la bonne réponse, de sorte que les joueurs peuvent faire de petites fautes d’orthographe).</td>
</tr>
<tr class="odd">
<td>Tolerance</td>
<td>Variation autorisée entre la bonne réponse et les réponses données. S’applique aux questions dont l’input type est ‘text’ avec ‘text evaluation’ réglé sur ‘fuzzy match’.</td>
</tr>
<tr class="even">
<td>Topic<sup>*</sup></td>
<td>Le thème de la question. Il sert à générer automatiquement un Trivia Board précédent.</td>
</tr>
<tr class="odd">
<td>Transition</td>
<td>L’animation de transition spécifique lors du passage à la diapositive suivante (par défaut, une transition aléatoire est sélectionnée par le système)</td>
</tr>
<tr class="even">
<td>Type</td>
<td><p>Champ en lecture seule indiquant le type de la diapositive :</p>
<ul>
<li><p><em>Question</em> : la diapositive est une question de quiz normale.</p></li>
<li><p><em>Billboard</em> : la diapositive est réservée à l’affichage.</p></li>
<li><p><em>End of round</em> : la diapositive marque la fin d’une manche du quiz. Les scores intermédiaires sont affichés et l’animateur de quiz a la possibilité d’éliminer des équipes. Voir aussi la propriété : ‘End of Round’.</p></li>
<li><p><em>Test question</em> : diapositive utilisée pour faire la démonstration du système aux participants. Aucun point n’est ajouté ni retiré.</p></li>
<li><p><em>Demographic</em> : cette diapositive sert à répartir tous les participants en groupes concurrents. Voir aussi la propriété ‘Demographic group’.</p></li>
<li><p><em>Last Man Standing</em> : la diapositive est une question de quiz. Les participants qui répondent incorrectement à la question sont éliminés du quiz.</p></li>
<li><p><em>Audience Response</em> : diapositive servant simplement à recueillir une réponse du public sans modifier les scores du quiz. Les données de réponse peuvent être affichées dans un graphique.</p></li>
<li><p><em>Wager</em> : permet au public de miser un pourcentage de ses scores sur la question suivante.</p></li>
<li><p><em>Majority Rules</em> : une diapositive dont la bonne réponse dépend de ce que le public choisit le plus</p></li>
<li><p><em>Minigame</em> : une diapositive qui lance le minijeu sélectionné</p></li>
<li><p><em>Trivia Board</em> : une diapositive qui démarre une manche où les questions sont organisées par Topic/Points et présentées sous forme de grille</p></li>
<li><p><em>Trivia Ladder :</em> démarre une manche Trivia Ladder où les joueurs montent d’un échelon à chaque bonne réponse</p></li>
<li><p><em>Speed Round :</em> démarre une manche où un joueur doit répondre à un maximum de questions en un temps déterminé.</p></li>
<li><p><em>Trivia Bingo :</em> démarre une manche de Bingo, construite soit à partir des diapositives de quiz suivantes, soit comme un jeu de Bingo numérique traditionnel.</p></li>
<li><p><em>Trivia Feud :</em> une diapositive où les joueurs répondent à une question de type sondage.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Voting</td>
<td>Indique si tous les participants peuvent répondre ou si seul le premier participant à buzzer peut répondre.</td>
</tr>
</tbody>
</table>
<p><sup>* la visibilité de la propriété dépend d’autres propriétés</sup></p></td>
</tr>
</tbody>
</table>

## Propriétés de la question

Ces propriétés s’affichent en cliquant sur la zone de question d’une diapositive

| Propriété | Description |
|---|---|
| Alignment | L’alignement du texte de la question |
| Drop shadow | Indique si une ombre est appliquée sous le texte de la question |
| Gradient | Le dégradé de remplissage de l’arrière-plan de la question. |
| Shadow color | Indique la couleur de l’ombre |
| Text | Le texte de la question |
| Text Color | La couleur du texte de la question |
| Text font | La police utilisée pour le texte de la question |
| Text reveal animation | Comment le texte est révélé. Show (par défaut : s’affiche directement), Show letter by letter ou Show word by word |
| Text reveal delay (sec) | Le délai après lequel le texte s’affiche |
| Text reveal speed | Vitesse de révélation du texte |
| Transparency | Transparence de l’arrière-plan de la question |

## Propriétés des réponses

Ces propriétés s’affichent en cliquant sur une zone de réponse d’une diapositive

| Propriété | Description | |
|---|---|---|
| Alignment | | L’alignement du texte de la réponse |
| Correct answer | | Indique si la réponse sélectionnée est la bonne réponse. Réglez sur ‘true’ si la réponse sélectionnée est la bonne réponse. |
| Correctness | | Applicable aux questions avec plusieurs bonnes réponses, cette valeur définit l’exactitude (en pourcentage du total des points de la question) de la réponse. |
| Drop shadow | | Indique si une ombre est appliquée sous le texte de la question |
| Gradient | | Le dégradé de remplissage de l’arrière-plan de la question. L’applicabilité de cette propriété dépend du style utilisé. |
| Shadow color | | La couleur de l’ombre portée |
| Text | | Le texte de la réponse |
| Text reveal animation | | Comment le texte est révélé. Show (par défaut : s’affiche directement), Show letter by letter ou Show word by word |
| Text reveal delay (sec) | | Le délai après lequel le texte s’affiche |
| Text reveal speed | | Vitesse de révélation du texte |
| Text color | | La couleur du texte de la réponse |
| Text font | | La police du texte de la réponse |
| Transparency | | Transparence de l’arrière-plan du panneau de réponse |

## Propriétés des images

Ces propriétés s’affichent en cliquant sur une zone d’image d’une diapositive

| Propriété | Description |
|---|---|
| Border | Indique si une bordure est tracée autour de l’image |
| Border color | La couleur de la bordure, lorsqu’elle est activée |
| Border thickness | Épaisseur en pixels de la bordure (lorsqu’elle est activée) |
| Corner radius | Rayon des coins de la ligne de bordure pour créer une bordure arrondie |
| Correct answer | Indique si l’image contient la bonne réponse. Cela ne peut être défini pour des images que si la diapositive ne contient que des images et est une diapositive à choix multiple. |
| Drop shadow | Indique si une ombre est appliquée sous l’image |
| Effect | Applique un effet à l’image. Voir [Recadrage](../adding-multimedia-content/pictures.md#recadrage) pour une explication plus détaillée des effets. |
| Hidden | Masque l’image pendant le quiz |
| Hidden on mobile | Indique si une image affichée sur une diapositive de quiz doit être masquée sur le téléphone mobile. Un scénario d’utilisation est celui où vous voulez afficher une image différente sur le téléphone mobile et sur le grand écran destiné au public. Par exemple, vous pouvez souhaiter que l’image mobile ait un rapport d’aspect différent. Dans ce cas, vous ne voulez pas que l’image affichée sur le grand écran apparaisse aussi sur le téléphone mobile. |
| Image | Une miniature de l’image. Cliquez sur le bouton de parcours (…) de cette propriété pour rechercher une image. |
| Inflate | Détermine si l’image doit remplir toute la zone en zoomant |
| Label | Une description textuelle de l’image (utilisée lorsque l’image ne peut pas être affichée) |
| Mobile device image | Une autre version de l’image à utiliser sur les appareils mobiles |
| Stretch | Étire l’image dans les deux directions pour remplir la zone (peut déformer l’image) |

## Propriétés des sons

Ces propriétés s’affichent en cliquant sur un élément sonore d’une diapositive

| Propriété | Description |
|---|---|
| Duration | La durée du son. Au départ, la durée complète est affichée. |
| Intro pause | Le temps d’attente avant le démarrage du son. Cela donne à l’animateur de quiz la possibilité de lire d’abord la question. |
| Keep playing | Par défaut, la musique que vous placez sur une diapositive s’arrête à la fin du compte à rebours. Avec cet indicateur, vous pouvez laisser la musique jouer jusqu’au passage à la diapositive suivante. |
| Pitch | La hauteur du son au début du compte à rebours |
| Remove vocals | Effet pour supprimer les voix (les résultats peuvent varier) |
| Repeat | Indique si le son doit se répéter. |
| Replay | Rejoue le son après que la bonne réponse a été révélée dans la question. |
| Replay delay | Affiché lorsque replay est activé. Indique le nombre de secondes après lesquelles la répétition commence |
| Replay start | Définit le moment où le fragment sonore commencera à être lu |
| Replay end | Définit le moment où le fragment sonore s’arrêtera |
| Reverse audio | Lit le fragment sonore à l’envers |
| Sound Storage Type | Indique si les données sonores sont stockées dans le fichier du quiz (embedded) ou sur le disque local (linked) |
| Speed percentage | La vitesse du son au début de la lecture. |
| Start at | La position dans le fichier son à partir de laquelle le son démarrera. |
| Stop at | Le moment où arrêter le son |
| Target Pitch | La hauteur du son à la fin du compte à rebours (la hauteur est interpolée du début à la fin) |
| Target speed percentage | La vitesse du son à la fin de la lecture. Remarque : en jouant avec ‘speed percentage’ et ‘target speed percentage’, il est possible de lire des sons ‘de lent à normal’ ou ‘de rapide à normal’. Régler les deux pourcentages sur 100 % lit simplement le fragment sonore du début à la fin à vitesse normale. |
| Volume | Le volume auquel jouer la musique |
| Volume fade | Fondu en entrée/sortie au démarrage/à l’arrêt de la musique |

## Propriétés des minijeux

| Propriété | Description |
|---|---|
| Minigame title | Par défaut, le buzzer mobile affiche à l’écran le nom du minijeu. Vous pouvez le remplacer et fournir votre propre texte. Ainsi, au lieu de voir « Horse race », vous pouvez afficher quelque chose de plus excitant. |

## Propriétés des vidéos

Ces propriétés s’affichent en cliquant sur une vidéo d’une diapositive

| Propriété | Description |
|---|---|
| Aspect Ratio | (lecture seule) rapport d’aspect |
| Codec | (lecture seule) décodeur vidéo utilisé |
| Duration | (lecture seule) durée de la vidéo |
| Effect | Effet facultatif sur la vidéo |
| End | Moment où terminer la vidéo |
| Intro Pause | Délai entre l’affichage de la diapositive et le démarrage de la vidéo |
| Linked File | Nom de fichier du fichier vidéo externe s’il est lié |
| Loop | Répète la vidéo après son arrêt |
| Replay | Rejoue la vidéo après que la bonne réponse a été révélée dans la question. |
| Replay delay | Le nombre de secondes après lesquelles la répétition commence |
| Replay start | Définit le moment de lecture où la vidéo commencera |
| Replay end | Définit le moment de lecture où la vidéo se terminera |
| Silent | Supprime le son de la vidéo |
| Start | Moment où démarrer la vidéo |
| Video Height | (lecture seule) hauteur de la vidéo |
| Video storage type | Indique si le fragment vidéo est intégré (embedded) ou lié (linked). Intégrer un fragment vidéo dans un quiz signifie que le fragment vidéo est incorporé au fichier du quiz. Lier un fragment vidéo signifie qu’une référence est créée depuis le fichier du quiz vers une vidéo du système de fichiers. En général, il est recommandé de lier les vidéos. *Remarque : lorsque vous liez des vidéos, veillez à ne pas supprimer les fichiers vidéo de votre système de fichiers. Lorsque vous déplacez le quiz vers un autre ordinateur, les vidéos doivent être copiées dans le même dossier que le fichier du quiz.* |
| (lecture seule) largeur de la vidéo | (lecture seule) largeur de la vidéo |

## Propriétés des formes

Ces propriétés s’affichent en cliquant sur une forme image ou une forme texte d’une diapositive.

| Propriété | Description |
|---|---|
| Alignment | L’alignement du texte de la forme texte |
| Background transparency | Applicable aux formes texte. Définit la transparence de la couleur utilisée pour l’arrière-plan (la propriété Gradient). |
| Border color | La couleur de bordure d’une forme texte |
| Border width | La largeur de la bordure d’une forme texte |
| Corner radius | Le rayon de la bordure d’une forme texte. Permet d’obtenir des coins arrondis. |
| Drop shadow | Indique s’il faut utiliser une ombre portée pour une forme texte |
| Gradient | Le dégradé de remplissage de l’arrière-plan d’une forme texte. Une couleur de dégradé ‘from’ et une couleur de dégradé ‘to’ peuvent être sélectionnées, ainsi qu’un type de dégradé. |
| Picture | Applicable aux formes image. Une miniature de l’image. Cliquez sur le bouton de parcours (…) pour rechercher une image. |
| Rotation Angle | L’angle de rotation de l’image ou du texte |
| Shadow color | Couleur de l’ombre portée d’une forme texte |
| Stretch | Applicable aux formes image. Étire l’image pour couvrir toute la zone du cadre de sélection qui l’entoure |
| Text | Le texte de la forme texte |
| Text color | La couleur du texte d’une forme texte |
| Text font | La police utilisée pour la forme texte |
| Transparency | Définit la transparence de l’image ou du texte |
| Visibility | Indique si une forme (image ou texte) est toujours visible, devient visible lorsqu’une réponse est révélée, est masquée lorsqu’une réponse est révélée, ou est minutée (apparaît à un moment précis pendant le compte à rebours). |

## Propriétés de la synthèse vocale

Ces propriétés s’affichent en cliquant sur un élément de synthèse vocale d’une diapositive.

| Propriété | Description |
|---|---|
| PreRoll | Indique le nombre de secondes d’attente avant le début de la lecture vocale |
| Rate | La vitesse à laquelle le texte de l’élément vocal est lu |
| Text | Le texte à lire |
| Voice | La voix à utiliser (choisissez-en une parmi les voix installées dans Windows) |
| Volume | Le volume du texte parlé |

## Propriétés des graphiques

Ces propriétés s’affichent en cliquant sur un graphique d’une diapositive

| Propriété | Description |
|---|---|
| Alignment | Alignement du titre du graphique |
| Area background | Définit la couleur d’arrière-plan de la zone de données du graphique |
| Axis color | La couleur utilisée pour l’axe |
| Axis label autosize | Définit automatiquement la taille des étiquettes sur l’axe. Si cette option n’est pas activée, vous pouvez choisir explicitement une police et une taille pour les étiquettes |
| Axis label color | La couleur utilisée pour les étiquettes de l’axe |
| Chart background | Définit la couleur d’arrière-plan de la zone située en dehors des données du graphique |
| Chart type | Le type de graphique. Choisissez entre Bar, Column, Doughnut ou Pie. |
| Corner radius | Rayon des coins de l’élément graphique |
| Dropshadow offset | Affiche une ombre portée pour la zone de données du graphique |
| Grid color | La couleur utilisée pour la grille dans la zone de données du graphique |
| Label color | Couleur des étiquettes affichées pour chaque élément du graphique |
| Label display mode | Pour les étiquettes, affiche les valeurs absolues, les pourcentages ou les deux |
| Label font | Police des étiquettes |
| Label style | Indique où positionner les étiquettes |
| Mode | Indique le type de données affichées dans le graphique : response (pourcentage de chaque réponse donnée) ou right/wrong (pourcentage de joueurs qui ont eu juste/faux) |
| Show 3D | Affiche une représentation 3D du graphique |
| Show legend | Affiche une légende pour les données du graphique (pourcentage de réponses pour chaque réponse) |
| Title | Titre du graphique |
| Title color | Couleur du titre du graphique |
| Title font | Police du titre du graphique |
| Visibility | Indique si le graphique est toujours visible (avec mises à jour en direct pendant le compte à rebours) ou seulement après la clôture de la question |

## Propriétés des jeux de mots

Ces propriétés s’affichent en cliquant sur un jeu de mots d’une diapositive

| Propriété | Description |
|---|---|
| Alignment | Alignement du texte |
| Background fill | Le dégradé de remplissage de l’arrière-plan du jeu de mots. Une couleur de dégradé ‘from’ et une couleur de dégradé ‘to’ peuvent être sélectionnées, ainsi qu’un type de dégradé. |
| Center index | Pour un jeu de roue de lettres (word wheel), indique la lettre qui apparaît au centre |
| Drop shadow | Indique s’il faut utiliser une ombre portée pour les lettres du jeu de mots |
| End reveal at | Pourcentage du temps du compte à rebours auquel la révélation se termine |
| Font | La police utilisée pour le texte |
| Interval | Pour les jeux de mots de type unscramble et reveal, contrôle le temps entre les étapes du jeu : linéaire, ralenti ou très ralenti. |
| Layout | Pour les jeux de mots reveal ou unscramble : grille de lettres dynamique ou grille de lettres fixe de 52 cellules. |
| Letter background fill | Le dégradé de remplissage de l’arrière-plan des cases de lettres du jeu de mots. Une couleur de dégradé ‘from’ et une couleur de dégradé ‘to’ peuvent être sélectionnées, ainsi qu’un type de dégradé. |
| Letter corner radius | Rayon des coins du jeu de mots |
| Letter spacing | Espace entre les lettres du jeu de mots |
| Manual control | Indique si les lettres sont révélées automatiquement ou si elles sont révélées manuellement par l’animateur de quiz depuis QuizXpress Director |
| Padding | Marge intérieure autour des lettres de la grille |
| Reverse | Pour un jeu de roue de lettres (word wheel), inverse le sens des lettres |
| Shadow color | Couleur de l’ombre portée des lettres |
| Spin | Fait tourner les lettres de la roue de lettres pour un défi supplémentaire |
| Start angle | Pour un jeu de roue de lettres (word wheel), l’angle de départ où apparaît la première lettre du mot |
| Start reveal at | Pourcentage du temps du compte à rebours auquel la révélation commence |
| Text | Le texte du jeu de mots |
| Text color | La couleur du texte |
| Text transparency | La transparence du texte |

## Propriétés du Trivia Board

Ces propriétés s’affichent lorsqu’un trivia board est sélectionné. Les propriétés marquées *Custom* ne s’affichent que lorsque 'Board position' est Custom ; voir [Concevoir votre propre plateau](../slide-and-game-formats/trivia-board-round.md#concevoir-votre-propre-tableau).

| Propriété | Description |
|---|---|
| Auto select | Sélectionne automatiquement une case au hasard avec une animation lorsque le plateau est sélectionné |
| Animation duration (sec) | Durée en secondes de l’animation de sélection aléatoire |
| Animation interval (sec) | Intervalle entre les changements de sélection pendant l’animation de sélection aléatoire |
| Background color (Topic Tiles) | Définit la couleur d’arrière-plan des cases de thème |
| Background color (Question Tiles) | Définit la couleur d’arrière-plan des cases de question |
| Board position | Automatic remplit l’écran (le plateau classique). Custom place le plateau là où il se trouve sur la diapositive, afin que vous puissiez le déplacer et le redimensionner pour l’adapter à votre arrière-plan |
| Circular tiles (Topic tiles) | Rend les cases circulaires (rectangulaires par défaut) |
| Column spacing | L’espace entre les colonnes de cases |
| Effect color | La couleur de l’ombre ou du contour du texte |
| Font (Topic Tiles) | Définit la police des cases de thème |
| Font (Question Tiles) | Définit la police des cases de question |
| Highlight color | La couleur de la sélection aléatoire |
| Image position (Topic Tiles) | *Custom.* Où se place l’image du thème : sur toute la case, ou à gauche, à droite ou au-dessus du nom du thème |
| Image scaling | *Custom.* Comment l’image d’une case est ajustée dans la case : Stretch, Fit, Fill ou Keep corners |
| Max. questions to play | Le nombre maximum de questions à jouer, ou 0 pour toutes les questions |
| Played tiles | Aspect d’une case une fois toutes ses questions jouées : Dimmed, Hidden ou No text |
| Randomize questions | Si plusieurs questions sont liées à une case, l’une d’elles sera sélectionnée au hasard. Toutefois, si l’option ‘Randomize questions’ n’est pas activée, les questions derrière la case seront présentées dans l’ordre où elles apparaissent dans le quiz. |
| Row spacing | L’espace entre les lignes de cases |
| Same text size for all tiles | Une taille de texte pour tous les noms de thèmes et une pour toutes les valeurs de points, jamais supérieure à la taille de police ; les noms de thèmes longs passent à la ligne sur deux lignes. Lorsque l’option est désactivée, chaque texte remplit sa propre case |
| Selection highlight | Comment la sélection aléatoire met une case en évidence : Fill, Tint, Outline ou Glow |
| Show topic name (Topic Tiles) | *Custom.* Affiche le nom du thème sur la case ; désactivez-le lorsque les images de thème contiennent déjà le nom |
| Text color (Question Tiles) | Définit la couleur du texte des cases de question |
| Text color (Topic Tiles) | Définit la couleur du texte des cases de thème |
| Text effect | Une ombre ou un contour autour du texte des cases |
| Tile image | *Custom.* Une image pour les cases de thème ou les cases de question, à la place de la couleur d’arrière-plan |
| Topic images (Topic Tiles) | *Custom.* Une image distincte pour chaque thème du plateau |
| Topic row height | La hauteur de la ligne de thèmes par rapport à une ligne de cases de question |
| Topics only | Affiche uniquement les thèmes sur le plateau |
| Vary tiles (Question Tiles) | *Custom.* Applique à l’image de la case un effet miroir différent sur chaque case |

## Propriétés du Trivia Ladder

Ces propriétés s’affichent lorsqu’une diapositive Trivia Ladder est sélectionnée.

| Propriété | Description |
|---|---|
| Background color | Définit la couleur d’arrière-plan de la trivia ladder |
| Background image | Définit l’image d’arrière-plan de l’échelle |
| Background stretch mode | Mode d’étirement de l’image d’arrière-plan |
| Border color | Définit la couleur de la bordure de la trivia ladder |
| Display mode | Où afficher l’échelle à l’écran : glisser depuis la droite de l’écran, glisser au centre de l’écran, afficher en plein écran, ou l’afficher en permanence (sur le côté droit de l’écran). |
| Keypads color | Définit la couleur des keypads |
| Safety net color | Définit la couleur des échelons de filet de sécurité |
| Separator color | Définit la couleur des séparateurs |
| Show border | Affiche la bordure de la trivia ladder |
| Step color | Définit la couleur des échelons |
| Wrong answer action | Indique quoi faire lorsqu’un joueur répond incorrectement : descendre d’un échelon, rester sur le même échelon, recommencer au début de l’échelle, ou retomber sur le filet de sécurité le plus proche. |

## Propriétés du Bingo

Lors de la configuration de votre jeu de Bingo, les propriétés suivantes sont disponibles :

| Propriété | Description |
|---|---|
| Auto advance after claim | Lorsqu’une réclamation est traitée à l’écran et que cette option est activée, le jeu continue automatiquement après la réclamation. Sinon, le jeu attend que l’animateur appuie sur Next. |
| Blanks per row | Le nombre de cases vides par ligne sur la carte de bingo. Cela peut servir à accélérer le jeu |
| Center Image | L’image centrale (bonus) qui apparaît sur la carte de Bingo mobile |
| Claims mode | Indique si seul le premier joueur à réclamer le bingo est traité ou tous les joueurs |
| Countdown time (sec) | Le temps du compte à rebours lors du traitement d’une réclamation de bingo à l’écran. |
| Enable Virtual Caller | Active le synthétiseur vocal de Windows pour annoncer les boules/couleurs dans un jeu de Bingo classique |
| False Bingo handling | Comment les faux bingos sont traités (devant le public, ou discrètement) |
| False Bingo limit | Combien de fois un joueur peut réclamer un bingo avant d’être exclu |
| False Bingo mode | Ce qui se passe lorsqu’un joueur réclame un faux Bingo |
| First Pattern…Fifth Pattern | Les motifs à jouer (jusqu’à 5 motifs peuvent être joués dans une même manche) |
| Game Type | Trivia Bingo, Number (traditional) Bingo ou Emoji Bingo. |
| Pattern penalty points | Les points à perdre pour un faux bingo (par motif) |
| Pattern Points | Les points à gagner pour un bingo valide (par motif) |
| Randomize questions | Lors d’un Trivia Bingo, cet indicateur signifie que les questions sont jouées dans un ordre aléatoire |
| Say Colors | Annonce les couleurs des colonnes avec les numéros (par exemple ‘Blue 4’) |

## Propriétés du Trivia Feud

Lors de la configuration d’une diapositive Trivia Feud, les propriétés suivantes sont disponibles :

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Propriété</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto scale text</td>
<td>Met à l’échelle le texte des réponses pour qu’il tienne dans les cases (ce qui donne des tailles de police différentes selon les réponses)</td>
</tr>
<tr class="even">
<td>Drop shadow</td>
<td>Ajoute une ombre portée aux textes des réponses</td>
</tr>
<tr class="odd">
<td>Leading zeros</td>
<td>Affiche les zéros non significatifs pour les scores du sondage</td>
</tr>
<tr class="even">
<td>Question font</td>
<td>Police de la question du sondage</td>
</tr>
<tr class="odd">
<td>Question text color</td>
<td>Couleur de la question du sondage</td>
</tr>
<tr class="even">
<td>Show light grid</td>
<td>Affiche la grille lumineuse en arrière-plan</td>
</tr>
<tr class="odd">
<td>Survey</td>
<td>Modifie les réponses du sondage</td>
</tr>
<tr class="even">
<td>Survey question</td>
<td>Modifie les questions du sondage</td>
</tr>
<tr class="odd">
<td>Survey text alignment</td>
<td>Alignement du texte du sondage</td>
</tr>
<tr class="even">
<td>Survey text color</td>
<td>Couleur des réponses du sondage</td>
</tr>
<tr class="odd">
<td>Game mode</td>
<td>Manual, Fastest Finger, Multiplayer</td>
</tr>
<tr class="even">
<td>Hide survey question</td>
<td>Masque la question du sondage (l’animateur de quiz préfère la lire à voix haute)</td>
</tr>
<tr class="odd">
<td>Max correct answers</td>
<td>Le nombre maximum de bonnes réponses qu’un joueur peut donner (fastest finger uniquement).</td>
</tr>
<tr class="even">
<td>Max incorrect answers</td>
<td><p>Le nombre maximum de mauvaises réponses qu’un joueur peut donner avant que le compte à rebours ne reprenne (mode fastest finger)</p>
<p>Le nombre maximum de mauvaises réponses avant que le tour ne passe à l’autre équipe (mode manual)</p></td>
</tr>
<tr class="odd">
<td>Penalty points</td>
<td>Le nombre de points de pénalité lorsqu’une réponse donnée est incorrecte (mode fastest finger)</td>
</tr>
<tr class="even">
<td>Points multiplier</td>
<td>Applique un multiplicateur de 2 ou 3 aux réponses du sondage afin qu’un joueur puisse gagner 2 ou 3 fois plus de points</td>
</tr>
<tr class="odd">
<td>Reveal order</td>
<td>L’ordre dans lequel les panneaux restants sont révélés (‘first to last’ ou ‘last to first’)</td>
</tr>
<tr class="even">
<td>Reveal delay (ms)</td>
<td>Le délai en millisecondes entre la révélation de chaque réponse du sondage. Permet à l’animateur de lire les réponses une par une pendant qu’elles s’affichent.</td>
</tr>
<tr class="odd">
<td>Wrong answer mode</td>
<td>Lorsqu’un joueur a donné le nombre de mauvaises réponses défini dans ‘max incorrect answers’, ce mode indique si le joueur est exclu pour cette question ou s’il peut buzzer à nouveau (continuer) (mode fastest finger)</td>
</tr>
</tbody>
</table>
