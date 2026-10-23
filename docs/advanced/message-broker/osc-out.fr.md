# OSC Out

Avec OSC Out, vous décidez quel message OSC QuizXpress envoie lorsqu'un événement se produit dans le quiz. Utilisez-le pour les appareils qui ne réagissent qu'à leurs propres commandes, comme une console d'éclairage ETC Eos ou Ion : une bonne réponse peut déclencher le cue 20, le doigt le plus rapide sur le keypad 3 peut déclencher une macro, et chaque nouvelle diapositive peut déclencher le cue portant le même numéro.

Le [canal sortant IP](ip-outbound.md) envoie toujours les mêmes messages fixes, tels que `/correct` et `/buzz 3 A`. C'est suffisant pour votre propre logiciel, mais une console d'éclairage ignore les messages qu'elle ne connaît pas. OSC Out envoie exactement les messages attendus par la console, et vous pouvez utiliser les deux en même temps.

## Préparer une console ETC Eos ou Ion

Une console de la famille Eos (Eos, Gio, Ion, Element, ETCnomad) n'accepte que les messages OSC qui commencent par `/eos/`. Avant que QuizXpress puisse la piloter :

1. Dans les paramètres réseau de la console, cochez 'UDP Strings & OSC' pour le port réseau qui relie la console à l'ordinateur QuizXpress.
2. Dans Setup, sous 'Show Control', activez 'OSC RX' et 'String RX', puis définissez le 'OSC RX Port'. ETC recommande le port 8000.
3. Notez l'adresse IP de la console. Envoyez les messages à la console principale, pas à une console de secours ni à un client.

Les noms de ces paramètres diffèrent légèrement selon les versions du logiciel Eos ; le manuel ETC de votre version donne tous les détails.

## Activer OSC Out

Ouvrez les [paramètres du Message Broker](index.md#ouvrir-les-parametres-de-message-broker) et allez dans l'onglet 'OSC Out' :

![L'onglet OSC Out](../../assets/images/mb-osc-out-tab.webp){ width="420" loading=lazy }

**Mode**
:   Active ou désactive OSC Out.

**Send to**
:   L'adresse IP et le port de réception OSC de la console ; pour une console ETC, le 'OSC RX Port' de ses paramètres Show Control.

**Rules**
:   Chaque règle indique à QuizXpress quels messages envoyer pour un événement. 'Add...' crée une règle et 'Edit...' (ou un double-clic) en modifie une. Décochez une règle pour la désactiver sans la supprimer. Les flèches changent l'ordre, et 'Test' envoie immédiatement la règle sélectionnée à la console, ce qui vous permet de vérifier qu'elle réagit.

## Modifier une règle

![Modification d'une règle OSC](../../assets/images/mb-osc-rule.webp){ width="420" loading=lazy }

**Event**
:   Ce qui se passe dans le quiz, par exemple 'Correct answer' ou 'Slide changes'. Voir [Événements et filtres](#evenements-et-filtres).

**Filters**
:   Certains événements peuvent être restreints, par exemple 'Fastest finger' à un seul keypad, ou 'Slide changes' aux diapositives d'une certaine classe. Un filtre qui n'est pas coché accepte tout.

**OSC messages**
:   Les messages à envoyer, un par ligne, dans l'ordre où vous les écrivez. 'Examples' insère des lignes toutes faites pour ETC Eos et QLab.

**Enabled**
:   Active ou désactive la règle.

**Test**
:   Envoie immédiatement les messages à la console. Les variables reçoivent une valeur d'exemple, par exemple la diapositive 1.

Pendant que vous tapez, l'éditeur vérifie chaque ligne et indique ce qui ne va pas, par exemple un guillemet manquant.

### Écrire les messages

Écrivez un message comme ETC le fait dans ses manuels : l'adresse, puis `=` et les arguments, séparés par des virgules.

| Vous écrivez | QuizXpress envoie |
|---|---|
| `/eos/cue/1/20/fire` | Adresse seule, sans argument : déclenche le cue 20 de la liste de cues 1. |
| `/eos/sub/1=1.0` | Un nombre décimal (`1.0`) : le submaster 1 à fond. |
| `/eos/macro/fire=5` | Un nombre entier (`5`) : déclenche la macro 5. |
| `/eos/newcmd="Chan 1 At Full#"` | Du texte entre guillemets doubles : saisit la commande dans la ligne de commande de la console. |
| `# finale lights` | Rien : une ligne qui commence par `#` est une note. |

Un texte entre guillemets doubles est toujours envoyé comme texte, même lorsqu'il s'agit d'un nombre (`"7"`). Sans guillemets, un nombre avec un point décimal est envoyé comme nombre décimal, un nombre sans point comme nombre entier, et tout le reste comme texte.

### Variables

Les variables entre accolades sont remplacées par des valeurs du quiz au moment de l'envoi du message. `/eos/cue/1/{slide}/fire` déclenche le cue 5 quand la diapositive 5 apparaît, de sorte qu'une seule règle couvre tout le quiz.

| Variable | Valeur | Disponible pour |
|---|---|---|
| `{slide}` | Le numéro de la diapositive actuelle, à partir de 1 comme dans Studio. | Tous les événements |
| `{previous}` | Le numéro de la diapositive précédente, `0` pour la première diapositive. | Tous les événements |
| `{class}`, `{id}` | La classe et l'id de la diapositive actuelle, définis dans les métadonnées de la diapositive dans Studio. | Tous les événements |
| `{type}` | Le type de diapositive, par exemple `question`. | Tous les événements |
| `{device}` | Le numéro du keypad ou du buzzer. | Fastest finger, Keypad press |
| `{key}` | La touche pressée, par exemple `A`. | Keypad press |
| `{keynumber}` | La touche sous forme de nombre : A = 1, B = 2 et ainsi de suite, le bouton de doigt le plus rapide = 0. | Keypad press |
| `{seconds}`, `{ms}` | Le temps restant en secondes et en millisecondes. | Countdown tick |
| `{screen}` | L'écran, par exemple `quizscreen` ou `finalscorescreen`. | Screen changes |
| `{command}` | Le bouton de la télécommande, par exemple `ok` ou `f1`. | Remote control button |

Une variable qui n'appartient pas à l'événement est envoyée telle qu'elle est écrite ; l'éditeur vous en avertit.

!!! note
    OSC Out compte toujours les diapositives à partir de 1, comme Studio, même lorsque 'Number slides from 1' dans l'onglet 'IP Outbound' est désactivé.

### Événements et filtres

| Event | Se déclenche quand… | Filters |
|---|---|---|
| Slide changes | Une nouvelle diapositive est affichée. | 'From slide', 'To slide', 'Slide class' |
| Screen changes | Le lecteur de quiz change d'écran, par exemple vers le quiz ou les scores finaux. | 'Screen' |
| Countdown starts | Le compte à rebours démarre ou reprend après une pause. | – |
| Countdown paused | Le compte à rebours est mis en pause. | – |
| Countdown tick | Chaque seconde pendant que le compte à rebours tourne. | 'Seconds left' |
| Countdown ends | Le compte à rebours s'arrête. | – |
| Timeout | Le temps de la question est écoulé. | – |
| Correct answer | Une réponse est jugée correcte. | – |
| Incorrect answer | Une réponse est jugée fausse. | – |
| Answer revealed | La bonne réponse est affichée sur la diapositive, y compris pour les questions de vote où personne ne juge une réponse. Sur une diapositive Trivia Feud, chaque réponse retournée sur le tableau. | – |
| Fastest finger | Un joueur est le premier lors d'une question de doigt le plus rapide. | 'Keypad' |
| Keypad press | Une touche est pressée sur un keypad ou un buzzer. | 'Keypad', 'Key' (A = 1, B = 2, doigt le plus rapide = 0) |
| Remote control button | Un bouton est pressé sur la télécommande de l'animateur de quiz. | 'Button' |
| Quiz restarts | Le quiz redémarre. | – |
| Bingo claimed, False bingo, Bingo | Un Bingo est annoncé, s'avère faux ou est valide. | – |

- 'Countdown tick' sans filtre envoie ses messages chaque seconde. Avec 'Seconds left', il les envoie une seule fois, quand le compte à rebours passe ce moment, par exemple 5 secondes avant la fin.
- Juste après un doigt le plus rapide, le compte à rebours se termine. Ce 'Countdown ends' est ignoré, afin que les lumières puissent rester sur le gagnant.
- Les numéros de diapositive dans les filtres 'From slide' et 'To slide' comptent à partir de 1. Le filtrage sur une classe de diapositive continue de fonctionner lorsque vous réorganisez les diapositives.

## Exemples pour ETC Eos

| Ce qui doit se passer | Événement et filtre | Message OSC |
|---|---|---|
| Chaque diapositive déclenche le cue portant son numéro dans la liste de cues 1 | Slide changes | `/eos/cue/1/{slide}/fire` |
| Une bonne réponse déclenche le cue 20 | Correct answer | `/eos/cue/1/20/fire` |
| La révélation de chaque question a son propre style, dans la liste de cues 2 | Answer revealed | `/eos/cue/2/{slide}/fire` |
| La lumière du gagnant s'allume | Fastest finger | `/eos/newcmd="Chan %1 At Full#",{device}` |
| Un style spécial pour la finale | Slide changes, 'Slide class' finale | `/eos/macro/99/fire` |
| Appuyer sur Go 5 secondes avant la fin | Countdown tick, 'Seconds left' 5 | `/eos/key/go_0` |
| Baisser le submaster 1 quand le compte à rebours est mis en pause | Countdown paused | `/eos/sub/1=0.3` |

Dans `/eos/newcmd`, Eos remplace `%1` par le premier argument, ici le numéro du keypad, de sorte que la commande devient par exemple `Chan 3 At Full`. Le `#` à la fin fait office de touche Entrée.

!!! tip
    Les autres appareils fonctionnent de la même façon. QLab, par exemple, démarre le cue 5 avec `/cue/5/start` ; utilisez `/cue/{slide}/start` pour suivre les diapositives.

## Vérifier ce qui est envoyé

Le [journal des messages](index.md#journal-des-messages) affiche chaque message OSC envoyé, avec l'événement qui l'a déclenché. Une ligne qui n'a pas pu être envoyée, par exemple parce qu'une variable a rendu l'adresse invalide, apparaît comme une erreur.

![Messages OSC dans le journal des messages](../../assets/images/mb-osc-message-log.webp){ loading=lazy }

!!! note
    OSC Out envoie en UDP vers une seule console. La console ne répond pas : le journal des messages montre donc ce que QuizXpress a envoyé, pas ce que la console en a fait.
