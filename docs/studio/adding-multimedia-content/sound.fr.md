# Son

Les extraits sonores peuvent servir pour des questions comme « Qui a écrit cette chanson ? », « Quel oiseau chante ici ? » ou « Quel est ce bruit ? ». Pour pimenter les choses, vous pouvez faire varier la vitesse du son au fil du temps en réglant les propriétés ‘Speed from’ (pourcentage de vitesse de lecture au début du son) et ‘Speed to’ (vitesse de lecture à la fin de l’extrait sonore). De même, vous pouvez faire varier la hauteur du son.

## Insérer un fichier audio

Pour ajouter un extrait sonore à une diapositive de quiz, sélectionnez l’onglet de ruban INSERT et cliquez sur le bouton ‘Audio’, puis sélectionnez un fichier mp3 ou wav et indiquez si vous souhaitez lier ou intégrer le fichier :

![](../../assets/images/image206.webp){ width="321" loading=lazy }

Lier les fichiers donne des fichiers de quiz plus petits et plus faciles à gérer, mais vous devrez veiller à ce que tous les fichiers externes restent accessibles, soit à leur emplacement d’origine, soit dans le dossier où le fichier du quiz est stocké (vous pouvez aussi garder les fichiers externes et [regrouper votre quiz](../other-functionality/packing-and-unpacking-a-quiz.md) avant de le distribuer ; le regroupement peut aussi découper les sons pour ne garder que la partie lue et les compresser).

Une fois le fichier inséré, l’onglet de ruban contextuel AUDIO devient visible pour configurer les différentes options.

![L’onglet de ruban AUDIO](../../assets/images/image207.webp){ width="720" loading=lazy }

## Découper un son

Le plus souvent, vous ne voulez lire qu’une partie d’une chanson ou d’un enregistrement : le refrain, l’introduction, ou simplement les quelques secondes qui donnent la réponse. L’éditeur de découpe affiche le son sous forme de forme d’onde, ce qui vous permet de voir où la musique commence, où elle devient forte et où elle s’estompe, et de choisir la partie à lire en l’écoutant.

L’éditeur de découpe ne modifie pas le fichier audio lui-même. Il définit seulement l’heure de début et de fin du son, vous pouvez donc toujours revenir à la piste complète.

### Ouvrir la fenêtre de découpe

Sélectionnez l’icône du son sur la diapositive, puis utilisez l’une de ces méthodes :

- Cliquez sur le bouton ‘Trim’ du groupe ‘Timing’ de l’onglet de ruban AUDIO, à côté des heures de début et de fin. La petite flèche dans le coin inférieur droit du groupe ‘Timing’ ouvre le même éditeur.

    ![Le bouton Trim de l’onglet de ruban AUDIO](../../assets/images/sound-ribbon-trim-button.webp){ width="420" loading=lazy }

- Cliquez avec le bouton droit sur l’icône du son sur la diapositive et choisissez ‘Trim sound...’.

    ![Trim sound dans le menu contextuel du son](../../assets/images/sound-context-menu-trim.webp){ width="240" loading=lazy }

!!! note
    Vous ne pouvez pas découper les pistes Spotify, les fichiers MIDI ni un fichier audio lié introuvable. Le bouton ‘Trim’ est grisé dans ces cas.

### Choisir la partie à lire

![L’éditeur de découpe](../../assets/images/sound-trim-editor.webp){ loading=lazy }

La partie qui sera lue est surlignée en bleu. Pour la modifier :

- **Faites glisser le curseur sur la forme d’onde** pour sélectionner une nouvelle partie, ou faites glisser les marqueurs au début et à la fin de la sélection.
- **Saisissez les heures** dans les champs ‘Start’ et ‘End’. Vous pouvez saisir des secondes (`75`), des minutes et secondes (`1:15`) ou des heures, minutes et secondes (`0:01:15`), avec des décimales si vous le souhaitez (`1:15.5`). ‘Length’ indique la durée de lecture de la partie sélectionnée.
- **Définissez le début ou la fin en écoutant** : cliquez sur ‘Set start (I)’ ou ‘Set end (O)’, ou appuyez sur I ou O au clavier, au moment précis où vous entendez le bon endroit. Lorsqu’aucun son n’est en cours de lecture, ces boutons utilisent la position du curseur.
- **‘Whole track’** sélectionne à nouveau le son complet.

Cliquez n’importe où dans la forme d’onde pour placer le curseur (la ligne orange).

Pour écouter :

- ‘Play selection’ (ou la barre d’espace) lit la partie sélectionnée. Appuyez à nouveau sur la barre d’espace pour arrêter.
- ‘Play from cursor’ lit depuis le curseur jusqu’à la fin du son.
- Pendant la lecture du son, cliquez sur la forme d’onde pour passer à cet endroit.

L’affichage à côté des boutons indique la position actuelle et la durée totale du son.

Pour un travail précis, effectuez un zoom avant avec la molette de la souris et utilisez Maj + molette de la souris ou la barre de défilement sous la forme d’onde pour vous déplacer vers la gauche et vers la droite. ‘Zoom to fit’ affiche à nouveau le son entier.

Cliquez sur ‘OK’ pour appliquer les nouvelles heures de début et de fin, ou sur ‘Cancel’ pour laisser le son tel qu’il était. Vous pouvez annuler un découpage en une seule étape avec Annuler. Si vous avez [normalisé le volume du son](#normaliser-le-volume), QuizXpress mesure à nouveau la nouvelle partie afin qu’elle reste aussi forte.

### Définir la partie de relecture

Dans le même éditeur, vous pouvez choisir la partie qui est lue à nouveau après la révélation de la réponse (voir [Relecture](#relecture) ci-dessous). Il s’agit souvent d’une autre partie de la chanson que celle lue pendant la question, par exemple le refrain.

![L’éditeur de découpe affichant la partie de relecture](../../assets/images/sound-trim-editor-replay.webp){ loading=lazy }

1. Cochez ‘Replay after the answer is revealed’. L’éditeur passe en mode ‘Replay’ et la sélection devient verte.
2. Sélectionnez la partie de relecture de la même manière que décrit ci-dessus.
3. Si vous le souhaitez, saisissez un ‘Delay (s)’ : le nombre de secondes à attendre après la révélation de la réponse avant le début de la relecture.

Utilisez les boutons ‘Playback’ et ‘Replay’ en haut à gauche pour passer d’une partie à l’autre. La partie que vous ne modifiez pas est affichée sous forme de barre le long du bas de la forme d’onde (bleue pour la lecture, verte pour la relecture), ce qui vous permet de voir comment les deux se situent l’une par rapport à l’autre.

!!! note
    La relecture n’est pas disponible lorsque l’option ‘Keep playing’ du son est activée, car le son ne s’arrête alors jamais.

## Relecture

Vous voudrez souvent rejouer (une partie de) la musique une fois la question terminée, en synchronisation avec la révélation de la bonne réponse sur la diapositive. Pour cela, activez la fonction de relecture audio :

![](../../assets/images/image208.webp){ width="576" loading=lazy }

Vous pouvez définir un délai initial, l’heure de début de la chanson et l’heure de fin. Le moyen le plus simple de choisir la partie de relecture est d’utiliser la forme d’onde dans l’éditeur de découpe ; voir [Définir la partie de relecture](#definir-la-partie-de-relecture).

## Normaliser le volume

Les chansons et extraits sonores de sources différentes sont rarement aussi forts les uns que les autres : un vieil enregistrement ou un morceau classique peut être beaucoup plus faible qu’une chanson pop moderne, de sorte que les joueurs tendent l’oreille pour une question et sont assourdis à la suivante. La normalisation du volume règle ce problème. QuizXpress mesure le volume réel de chaque son et l’ajuste pour que tous les sons soient lus avec la même force, dans Quiz Studio et pendant le show.

La normalisation ne modifie pas les fichiers audio. Elle définit le ‘Loudness gain’ du son (voir [ci-dessous](#la-propriete-loudness-gain)), que vous pouvez donc toujours modifier ou annuler. Seule la partie du son qui est lue est mesurée : la partie comprise entre son heure de début et son heure de fin.

Vous pouvez normaliser tous les sons du quiz en une fois, ou un seul son.

### Tous les sons du quiz

Cliquez sur ‘Normalize volume’ dans le groupe ‘Tools’ de l’onglet de ruban HOME.

![Normalize volume dans l’onglet de ruban HOME](../../assets/images/normalize-home-tools.webp){ width="220" loading=lazy }

La fenêtre ‘Normalize sound volume’ s’ouvre et commence immédiatement à mesurer tous les sons du quiz. Les longues chansons prennent quelques secondes chacune.

![La fenêtre Normalize sound volume](../../assets/images/normalize-dialog.webp){ loading=lazy }

Pour chaque son, vous voyez :

- **Slide** et **Sound** : où se trouve le son et de quoi il s’agit (le nom du fichier, ou le texte de la question pour un son intégré).
- **Source** : si le son est intégré au quiz ou lié, et son type de fichier.
- **Loudness** : le volume du son, en LUFS (Loudness Units relative to Full Scale, la mesure utilisée par les services de streaming et les diffuseurs). Plus la valeur est proche de 0, plus le son est fort : −8 LUFS correspond à une chanson pop forte, −22 LUFS à un enregistrement faible.
- **Peak** : le moment le plus fort du son, en dBFS. 0 dBFS est le niveau maximal qu’un fichier audio peut stocker.
- **Change** : de combien QuizXpress va augmenter (+) ou diminuer (−) le son, en dB.
- **Status** : tout ce qu’il est utile de savoir sur le son (voir le tableau ci-dessous).

Choisissez le ‘Target loudness’ :

| Target | Use it when |
|---|---|
| Standard (−16 LUFS) | Valeur par défaut. À peu près aussi fort que la musique sur les services de streaming. |
| Quieter (−18 LUFS) | Vous voulez un peu plus de marge, par exemple lorsque les sons sont lus par-dessus une musique de fond. |
| Broadcast (−23 LUFS) | Vous voulez le niveau utilisé par la télévision et la radio européennes (EBU R128). Nettement plus faible ; augmentez le volume du système de sonorisation en conséquence. |

La modification de la cible met immédiatement à jour la colonne ‘Change’ ; les sons ne sont pas mesurés à nouveau. Quiz Studio mémorise la cible que vous avez choisie et l’utilise aussi pour normaliser les sons individuels.

Si vous avez sélectionné des diapositives avant d’ouvrir la fenêtre, la liste ‘Sounds’ vous permet de choisir entre ‘All sounds in the quiz’ et ‘Sounds on the selected slides’.

Tous les sons qui vont changer sont cochés. Décochez un son pour le laisser tel quel. La ligne en bas indique combien de sons seront ajustés. Cliquez sur ‘Apply’ pour définir les nouveaux loudness gains. Vous pouvez annuler toute la normalisation en une seule étape avec Annuler.

| Status | Meaning |
|---|---|
| Limited to avoid clipping | Le son est faible mais présente déjà des pics élevés. QuizXpress ne l’augmente que dans la mesure où il ne sera pas déformé (les pics restent sous −1 dBFS) ; il peut donc rester un peu plus faible que les autres. |
| Already at target | Le son est déjà au volume cible et n’est pas modifié. |
| Silent | Il n’y a pas de son dans la partie lue (vérifiez ses heures de début et de fin). |
| Skipped: MIDI has no audio to measure | Les fichiers MIDI ne peuvent pas être mesurés et conservent leur volume. |
| Skipped: Spotify track | Les pistes Spotify ne peuvent pas être mesurées et conservent leur volume. |
| Sound file is missing | Un fichier audio lié est introuvable. [Réparez le lien](../other-functionality/fixing-broken-links.md) et réessayez. |

### Un seul son

Pour normaliser un seul son, par exemple après l’avoir remplacé, sélectionnez l’icône du son sur la diapositive et cliquez sur ‘Normalize’ dans le groupe ‘Effects’ de l’onglet de ruban AUDIO, ou cliquez avec le bouton droit sur l’icône du son et choisissez ‘Normalize volume’. L’info-bulle du bouton indique le volume cible qui sera utilisé : celui choisi en dernier dans la fenêtre ‘Normalize sound volume’.

![Le bouton Normalize dans l’onglet de ruban AUDIO](../../assets/images/normalize-sound-button.webp){ width="720" loading=lazy }

QuizXpress mesure le son et définit immédiatement son loudness gain, sans ouvrir de fenêtre. Une barre sous le ruban affiche le résultat, avec un lien ‘Undo’ pour l’annuler :

![Le résultat de la normalisation d’un seul son](../../assets/images/normalize-sound-result.webp){ width="720" loading=lazy }

### La propriété ‘Loudness gain’

Le résultat de la normalisation est enregistré dans la propriété ‘Loudness gain’ du son, dans la section ‘Audio’ du volet des propriétés. 0 dB laisse le son inchangé ; la plage va de −30 à +20 dB. Vous pouvez aussi l’ajuster finement à la main.

![Loudness gain dans le volet des propriétés](../../assets/images/normalize-loudness-gain.webp){ width="250" loading=lazy }

Le loudness gain s’ajoute au ‘Volume’ du son. Contrairement au volume, qui ne peut que rendre un son plus faible, le loudness gain peut aussi rendre un son faible plus fort.

!!! tip
    Normalisez après avoir découpé un son, car c’est la partie lue qui détermine son volume. Si un son a déjà été normalisé et que vous modifiez son heure de début ou de fin dans l’[éditeur de découpe](#decouper-un-son), QuizXpress mesure la nouvelle partie et ajuste automatiquement le loudness gain.

## Import de playlists Spotify ™

Vous pouvez importer vos playlists Spotify (éventuellement avec les pochettes d’album et un extrait de 30 secondes des chansons) et créer sans effort un quiz Trivia Music ou un jeu Disco Bingo. QuizXpress n’interagit pas directement avec Spotify, mais prend en charge un format de fichier CSV produit par le site [Exportify](https://watsonbox.github.io/exportify/). Pour utiliser cette fonction, exportez votre playlist en CSV avec ce site et importez le fichier dans QuizXpress. Un formulaire s’affiche pour vous permettre de faire quelques choix :

![](../../assets/images/image209.webp){ width="224" loading=lazy }

Si nous créons un jeu Bingo avec ces options, nous obtenons un mélange de cases avec pochettes d’album et texte Artiste/Titre, comme :

![](../../assets/images/image210.webp){ loading=lazy }

Les diapositives et les paramètres de jeu créés peuvent être ajustés après l’import.

## Appliquer des effets sonores

Différents effets sont possibles lors de la lecture des sons :

- **Accélérer le son** – pour cela, donnez la même valeur aux propriétés ‘speed percentage’ et ‘target speed percentage’ du son dans le Property Editor. Cette valeur doit être supérieure à 100 pour accélérer le son. Pour afficher les propriétés d’un son, cliquez avec le bouton gauche sur l’icône du son dans la zone de conception.

- **Ralentir le son** – pour cela, donnez aux deux propriétés mentionnées ci-dessus une valeur inférieure à 100. Là encore, donnez la même valeur aux deux ; vous verrez pourquoi ci-dessous.

- **De la vitesse lente à la vitesse normale** – pour cela, saisissez une valeur inférieure à 100 pour la propriété ‘speed percentage’ du son. Le son commence ainsi à être lu au ralenti. Laissez la propriété ‘target speed percentage’ inchangée ; sa valeur par défaut est 100, c’est-à-dire la vitesse normale. Résultat : QuizXpress lira d’abord le son lentement, puis, au fil du temps, atteindra la vitesse cible de 100 (vitesse normale).

- **De la vitesse rapide à la vitesse normale** – pour cela, choisissez une valeur supérieure à 100 pour la propriété ‘speed percentage’. Laissez la propriété ‘target speed percentage’ inchangée.

- **Reverse** – lit l’extrait sonore à l’envers, ce qui met les joueurs au défi de reconnaître la chanson (cochez la case Reverse audio dans le ruban du son)

Vous pouvez écouter ces effets sonores pendant que vous créez la question qui contient le son. Pour écouter le son et ses effets, cliquez sur le bouton ‘Play’ du ruban, ou sélectionnez ‘Play’ dans le menu contextuel du son.

Si vous ne souhaitez pas que le son démarre immédiatement au début de la question, utilisez la propriété ‘Intro Pause’ du son pour retarder la lecture (cela donne aux participants la possibilité de lire d’abord la question, ou à l’animateur de quiz de la lire d’abord à voix haute).

!!! note

    les autres sons, tels que les sons de buzzer, la musique de fond et la musique du compte à rebours, peuvent être configurés dans Quiz Setup.*
