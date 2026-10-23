# Canal IP sortant

Avec le canal sortant, QuizXpress envoie un message chaque fois que quelque chose se produit dans le quiz, comme un changement de diapositive, un appui sur un buzzer ou un changement de score. Votre propre application écoute ces messages et réagit, par exemple en pilotant un tableau des scores externe ou un jeu de lumière.

Activez-le dans l'onglet 'IP Outbound' des [paramètres de Message Broker](index.md#ouvrir-les-parametres-de-message-broker) :

![L'onglet IP Outbound](../../assets/images/mb-ip-outbound-tab.webp){ width="420" loading=lazy }

## Paramètres

**On/Off**
:   Active ou désactive le canal sortant.

**Test**
:   Ouvre un formulaire de test où vous pouvez déclencher des événements à la main :

    ![Formulaire de test du canal sortant](../../assets/images/mb-outbound-test-form.webp){ width="560" loading=lazy }

**Send a heartbeat message every second**
:   Envoie un message heartbeat chaque seconde, afin que le côté récepteur puisse constater que le lecteur de quiz tourne toujours. Utilisez-le pour détecter une connexion perdue de façon inattendue ; une session normale commence toujours par `/start` et se termine par `/close`.

**Send input from keypads/buzzers**
:   Relaie chaque appui sur un clavier et un buzzer. C'est facultatif car cela peut produire beaucoup de messages.

**Send score changes**
:   Envoie un message chaque fois que le score d'un joueur change, par exemple pour piloter des tableaux des scores externes.

**Send countdown tick**
:   Envoie le temps restant chaque seconde pendant que le compte à rebours tourne.

**Number slides from 1 (also MIDI triggers)**
:   Les numéros de diapositive dans `/slidechanged`, `/slideinfo` et le déclencheur MIDI 'Slide Changed' commencent à 1, comme dans Studio et dans les commandes entrantes `goto` et `getslide`. Lorsque l'option est désactivée, ils commencent à 0, comme dans les versions précédentes ; laissez-la désactivée si votre application ou votre configuration MIDI compte déjà à partir de 0.

**Send slide details (/slideinfo)**
:   Envoie la question, les réponses et la bonne réponse de chaque nouvelle diapositive. Voir [Détails de la diapositive et classement](#details-de-la-diapositive-et-classement).

**Send the leaderboard (/leaderboard)**
:   Envoie toutes les équipes dans l'ordre du classement après un changement de score. Voir [Détails de la diapositive et classement](#details-de-la-diapositive-et-classement).

**Send text answers as /textvote**
:   Les réponses textuelles des claviers (nombres, lettres, texte libre) sont envoyées sous la forme `/textvote` au lieu de `/buzz`, afin que votre application puisse les distinguer des appuis sur des boutons. Lorsque l'option est désactivée, les deux sont envoyés sous la forme `/buzz`, comme dans les versions précédentes. Nécessite 'Send input from keypads/buzzers'.

**Protocol**
:   - **UDP/ASCII :** texte ASCII brut, paramètres séparés par des espaces.
    - **UDP/UTF8 :** identique, encodé en UTF-8. Choisissez-le lorsque les noms d'équipe ou les réponses contiennent des caractères accentués.
    - **UDP/OSC :** messages au format [Open Sound Control (OSC)](https://en.wikipedia.org/wiki/Open_Sound_Control), que [Max](https://cycling74.com/), QLab, TouchOSC et des outils similaires peuvent traiter directement. Les nombres sont envoyés sous forme d'entiers 32 bits et le texte sous forme de chaînes UTF-8.

**Server address**
:   L'adresse IP de l'ordinateur qui reçoit les messages. Utilisez `127.0.0.1` s'il s'agit du même ordinateur.

**Server port**
:   Le numéro de port sur lequel l'application réceptrice écoute.

!!! tip
    Le [journal des messages](index.md#journal-des-messages) affiche chaque message sortant, ce qui vous permet de vérifier ce que votre application devrait recevoir.

!!! note
    Une console d'éclairage telle qu'un ETC Eos ou Ion ne réagit qu'à ses propres commandes, pas à ces messages fixes. Utilisez [OSC Out](osc-out.md) pour lui envoyer exactement les messages qu'elle attend.

## Messages

Le côté récepteur ouvre un socket UDP. Les messages sont des chaînes de texte brut au format `/message {parameter1} {parameter2} …`. Chaque session commence par `/start` et se termine par `/close`.

| Message | Signification |
|---|---|
| `/start` | Début de la session. |
| `/close` | Fin de la session : QuizXpress Live se ferme. |
| `/heartbeat {counter}` | Envoyé chaque seconde avec un compteur croissant, par exemple `/heartbeat 2345`. |
| `/countdowntick {remainingtimeMs}` | Envoyé chaque seconde pendant que le compte à rebours tourne, avec le temps restant en millisecondes, par exemple `/countdowntick 23100`. |
| `/slidechanged {old#} {new#} {questiontype} {slide class} {slide id}` | Une nouvelle diapositive est affichée. La classe et l'identifiant sont facultatifs et se définissent dans les métadonnées de la diapositive dans Studio, ce qui vous permet de réagir à une classe ou un identifiant plutôt qu'à un numéro de diapositive qui change lorsque les diapositives sont réorganisées. Exemple : `/slidechanged 6 7 question MySpecialSlideType banner1`. Avec 'Number slides from 1', `0` comme ancien numéro signifie qu'il n'y avait pas de diapositive précédente. |
| `/command {command}` | Une commande de la télécommande de l'animateur de quiz : `power`, `scores`, `chart`, `leaderboard`, `groupchart`, `up`, `down`, `pause`, `questionmark`, `next`, `wrong` ou `right`. Exemple : `/command up`. |
| `/buzz {device} {key}` | Un appui de touche sur un appareil, par exemple `/buzz 10 A`, ou `/buzz 8 RED` pour le bouton fastest finger. Les réponses textuelles sont aussi envoyées sous la forme `/buzz`, sauf si 'Send text answers as /textvote' est activé. |
| `/textvote {device} {text}` | Une réponse textuelle d'un appareil, par exemple `/textvote 8 Paris`. Uniquement avec 'Send text answers as /textvote'. |
| `/fastestfinger {device}` | L'appareil qui a été le premier à une question de type fastest finger. |
| `/screenchanged {screentype}` | Le lecteur de quiz a changé d'écran : `welcomescreen`, `signonscreen`, `countdownscreen`, `quizscreen` ou `finalscorescreen`. Exemple : `/screenchanged countdownscreen`. |
| `/timeout` | La question a expiré sans bonne réponse. |
| `/startcountdown` | Le compte à rebours de la question a démarré. |
| `/pausecountdown` | Le compte à rebours est en pause ; le système est inactif. |
| `/endcountdown` | Le compte à rebours s'est arrêté ; la question est terminée. |
| `/correct` | Une réponse à la question en cours a été jugée correcte. |
| `/incorrect` | Une réponse à la question en cours a été jugée fausse. |
| `/answerrevealed` | La bonne réponse est affichée sur la diapositive, par exemple lorsque le temps est écoulé sur une question de vote. Sur une diapositive Trivia Feud, il est envoyé pour chaque réponse retournée sur le tableau. |
| `/restart` | Le quiz a été redémarré depuis l'écran des scores finaux. |
| `/scorechanged {device} {teamname} {old score} {new score}` | Le score d'une équipe a changé. Exemple : `/scorechanged 10 'John Trivialta' 5 10` signifie que l'équipe 'John Trivialta' sur l'appareil 10 est passée de 5 à 10 points. En OSC, le nom de l'équipe est une chaîne sans guillemets. |
| `/claimbingo` | Un joueur a réclamé un Bingo. |
| `/falsebingo` | Un Bingo réclamé s'est révélé faux. |
| `/bingo` | Un Bingo réclamé est valide. |
| `/slideinfo {json}` | Les détails de la nouvelle diapositive, envoyés juste après `/slidechanged`. Uniquement avec 'Send slide details'. |
| `/leaderboard {json}` | Toutes les équipes dans l'ordre du classement. Uniquement avec 'Send the leaderboard'. |

Exemple de messages pendant un quiz :

![Exemple de messages sortants](../../assets/images/mb-outbound-example-messages.webp){ loading=lazy }

## Détails de la diapositive et classement

`/slideinfo` et `/leaderboard` transportent du [JSON](https://www.json.org/) sur une seule ligne, que la plupart des outils peuvent lire directement (Node-RED, Max avec `dict.deserialize`, Bitfocus Companion, Python). En OSC, le JSON est un argument de type chaîne. Avec UDP/ASCII, les caractères accentués sont écrits sous forme de codes `\u`, que tout lecteur JSON retransforme dans le bon caractère.

`/slideinfo` est envoyé juste après `/slidechanged`, par exemple :

```
/slideinfo {"number":44,"previous":45,"type":"question","question":"Which aircraft type has recently been added?","answers":["A340","A380","B787"],"correctAnswer":"C","category":"Default Category","answerTime":30,"points":10,"class":"","id":""}
```

| Champ | Signification |
|---|---|
| `number`, `previous` | Le numéro de la nouvelle diapositive et de la précédente, comptés selon le réglage 'Number slides from 1'. |
| `type` | Le type de diapositive, identique à celui de `/slidechanged`. |
| `question`, `answers` | Le texte de la question et les réponses, dans l'ordre de la diapositive. |
| `correctAnswer` | La bonne réponse, par exemple `C` pour la troisième réponse. |
| `category`, `answerTime`, `points` | La catégorie, le temps de réponse en secondes et les points pour une bonne réponse. |
| `class`, `id` | La classe et l'identifiant de la diapositive issus des métadonnées de la diapositive dans Studio. |

!!! warning
    `/slideinfo` contient la bonne réponse dès que la diapositive apparaît. Ne l'affichez pas sur un écran que les joueurs peuvent voir avant que la réponse soit révélée.

`/leaderboard` est envoyé après un changement de score. Lorsque de nombreux scores changent en même temps, par exemple à la fin d'une question, vous recevez un seul classement après le dernier changement au lieu d'un par équipe :

```
/leaderboard [{"rank":1,"device":2,"name":"Brainiacs","group":"","score":30},{"rank":2,"device":1,"name":"Zoë's Team","group":"","score":10},{"rank":2,"device":3,"name":"Quizzers","group":"","score":10}]
```

Les équipes ayant le même score partagent un rang, et le rang suivant est sauté (1, 2, 2, 4). `group` est le groupe démographique de l'équipe, le cas échéant.

## Exemple : un simple écouteur UDP

Cette application console C# (.NET Framework 4.8) écoute sur le port 12345 et affiche chaque message reçu. Réglez le 'Server port' dans Message Broker sur le même numéro.

```csharp
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class UDPServer
{
    static void Main(string[] args)
    {
        int port = 12345; // Le port sur lequel écouter
        UdpClient udpListener = new UdpClient(port);
        Console.WriteLine($"UDP server is listening on port {port}");

        try
        {
            while (true)
            {
                IPEndPoint senderEndPoint = new IPEndPoint(IPAddress.Any, port);
                byte[] receivedBytes = udpListener.Receive(ref senderEndPoint);
                string receivedText = Encoding.UTF8.GetString(receivedBytes);
                Console.WriteLine($"Received: {receivedText}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
        }
        finally
        {
            udpListener.Close();
        }
    }
}
```
