# Canal IP entrant

Avec le canal entrant, des applications externes envoient des commandes texte à QuizXpress, par exemple pour passer à la diapositive suivante, juger une réponse ou modifier un score. Les commandes peuvent arriver via UDP, TCP ou Telnet.

Configurez-le dans l'onglet 'IP Inbound' des [paramètres de Message Broker](index.md#ouvrir-les-parametres-de-message-broker) :

![L'onglet IP Inbound](../../assets/images/mb-ip-inbound-tab.webp){ width="420" loading=lazy }

## Paramètres

**On/Off**
:   Active ou désactive les messages entrants.

**Protocol**
:   Points de terminaison pour UDP, TCP et Telnet. Vous pouvez activer les trois en même temps, mais chacun nécessite son propre numéro de port. Le port Telnet par défaut est 23.

**Settings**
:   - 'Local IP address' affiche l'adresse IP de cet ordinateur, dont l'expéditeur a besoin.
    - 'Open the message log at start' ouvre le [journal des messages](index.md#journal-des-messages) à chaque démarrage d'un quiz, pour que vous puissiez suivre chaque commande entrante.
    - 'TCP replies with OK/ERR status' fait répondre chaque commande TCP avec son résultat. Voir [Réponses](#reponses).

## Sécurité

Par défaut, n'importe qui sur le réseau peut envoyer des commandes à QuizXpress. Dans un lieu doté d'un réseau Wi-Fi public, utilisez les paramètres 'Security' pour garder le contrôle du show. Laissez un champ vide pour le laisser ouvert.

**Listen on**
:   La carte réseau qui reçoit les commandes :

    - 'All network adapters' : tous les réseaux auxquels cet ordinateur est connecté (par défaut).
    - 'This computer only (127.0.0.1)' : seules les applications de cet ordinateur peuvent envoyer des commandes.
    - Une adresse IP de cet ordinateur : uniquement le réseau de cette carte.

    Si vous choisissez une adresse et que l'ordinateur en reçoit ensuite une autre, par exemple sur un autre réseau, la liste affiche l'adresse enregistrée sous la forme '(not available)' et le [journal des messages](index.md#journal-des-messages) affiche une erreur indiquant que le canal entrant n'a pas pu démarrer.

**Password**
:   Lorsque vous définissez un mot de passe, les commandes ne sont acceptées qu'après que l'expéditeur a prouvé qu'il connaît le mot de passe :

    - **TCP :** envoyez `login <password>` une fois après la connexion. Après trois mots de passe erronés, QuizXpress ferme la connexion.
    - **Telnet :** Telnet demande le mot de passe dès que vous vous connectez.
    - **N'importe quelle commande, y compris via UDP :** ajoutez `-pw:<password>` à la commande, par exemple `next -pw:quiz123`. UDP n'a pas de connexion sur laquelle s'identifier, donc via UDP chaque commande en a besoin.

    Les commandes sans le bon mot de passe sont ignorées et affichées comme un avertissement dans le journal des messages.

**Allowed senders**
:   Les adresses IP autorisées à envoyer des commandes, séparées par des virgules. Une plage s'écrit avec une longueur de préfixe : `192.168.1.0/24` autorise de `192.168.1.0` à `192.168.1.255`. Exemple : `192.168.1.20, 192.168.1.30, 10.0.0.0/8`. QuizXpress ignore tout ce qui vient d'autres adresses et l'affiche comme 'Rejected' dans le journal des messages. Si une entrée n'est pas une adresse ou une plage valide, l'indication devient rouge et 'OK' reste désactivé tant que vous n'avez pas corrigé.

!!! note
    Cet ordinateur est toujours autorisé, quoi que vous saisissiez dans 'Allowed senders'.

!!! warning
    Le mot de passe protège le show contre les personnes qui ne le connaissent pas, mais il est envoyé en texte brut sur le réseau, tout comme les commandes. Le mot de passe est stocké en texte brut dans les paramètres de Message Broker.

## Commandes

Ces commandes fonctionnent via Telnet, TCP et UDP. Telnet et TCP envoient une réponse ; UDP jamais.

| Commande | Fonction |
|---|---|
| `next` | Avancer, par exemple vers la diapositive suivante. |
| `showleaderboard` | Afficher le tableau des scores général. |
| `showresponsechart` | Afficher le graphique des réponses après une question à choix multiples. |
| `judgecorrect` | Juger correcte une question ouverte ou manuelle. |
| `judgeincorrect` | Juger incorrecte une question ouverte ou manuelle. |
| `pausetimer` | Mettre le compte à rebours en pause. Si le minuteur est déjà en pause, rien ne se passe. |
| `resumetimer` | Reprendre le compte à rebours. Si le minuteur tourne déjà, rien ne se passe. |
| `endquiz` | Terminer le quiz et aller à l'écran des scores finaux. |
| `restart` | Redémarrer le quiz. |
| `goto` | Aller à une diapositive par son numéro ou par son identifiant, par exemple `goto 10` ou `goto #banner1`. Les numéros de diapositive commencent à 1, comme dans Studio. L'identifiant est une valeur texte unique que vous pouvez définir sur une diapositive. Mettez d'abord le compte à rebours en pause : tant que le compte à rebours tourne, le saut est ignoré. |
| `enableallplayers` | Activer tous les joueurs enregistrés. |
| `selectplayer` | Activer le joueur du numéro d'appareil indiqué et exclure tous les autres. |
| `selectplayers` | Activer une plage de joueurs, comme `1-5` ou `1,2,10`, et exclure tous les autres. |
| `addplayer` | Ajouter un joueur avec un numéro d'appareil et un nom, par exemple `addplayer 1 "John Trivialta"`. |
| `resetplayers` | Supprimer tous les joueurs. |
| `addscore` | Ajouter des points au score d'un joueur, par numéro d'appareil ou nom d'équipe, par exemple `addscore 3 5` ou `addscore "The Quizzers" -2`. |
| `setscore` | Définir le score d'un joueur, par numéro d'appareil ou nom d'équipe, par exemple `setscore 3 0`. |
| `setteamname` | Définir le nom d'équipe pour un appareil, par exemple `setteamname 1 "John Trivialta"`. |
| `setvolume` | Définir le volume du lecteur de quiz (0–100). |
| `buzz` | Envoyer un vote pour un joueur, par exemple `buzz 1 FF` ou `buzz 1 A`. Ajoutez `-f` pour forcer le vote même lorsque la diapositive bloque les buzzers. |
| `buzzwithtext` | Envoyer un vote texte, pour les questions numériques, de lettre ou à texte libre, par exemple `buzzwithtext 3 "Paris"`. Ajoutez `-f` pour le forcer. |
| `playjoker` | Jouer un joker pour un joueur : `playjoker <device> <joker>`, où le joker est `FreeRide`, `PointBooster` ou `TimeWarp`. |
| `sendkey` | Appuyer sur une touche dans le lecteur de quiz, comme si elle était saisie au clavier, par exemple `sendkey Space` ou `sendkey Up`. |
| `getcurrentscreen` | Renvoyer l'écran actuel : `WelcomeScreen`, `SignOnScreen`, `CountdownScreen`, `QuizScreen` ou `FinalScoreScreen`. |
| `getplayers` | Renvoyer tous les joueurs avec leurs attributs (score, nom, appareil, etc.). Ajoutez `-f json` ou `-f osc` pour choisir le format. |
| `getquiz` | Renvoyer un export complet du quiz en XML, sans images, son ni vidéo. Cela peut représenter beaucoup de données. |
| `getslide` | Renvoyer les détails d'une diapositive en XML, sans images, son ni vidéo, par exemple `getslide 10`. Sans numéro, renvoie la diapositive en cours. |
| `login` | Se connecter sur une connexion TCP lorsqu'un [mot de passe](#securite) est défini : `login <password>`. |

Mettez le texte contenant des espaces entre guillemets doubles : `setteamname 1 "The Quizzers"`. Les guillemets simples fonctionnent aussi : `setteamname 1 'The Quizzers'`. Les noms d'équipe peuvent contenir des apostrophes et des deux-points, comme `"Bart's Team"` ou `12:30`. La commande elle-même n'est pas sensible à la casse ; les noms d'équipe et les réponses conservent leurs majuscules.

Exemple de sortie de `getplayers` :

![Exemple de sortie de getplayers](../../assets/images/mb-getplayers-example.webp){ loading=lazy }

Exemple de sortie de `getslide 10` :

![Exemple de sortie de getslide](../../assets/images/mb-getslide-example.webp){ loading=lazy }

## Réponses

Telnet répond toujours avec `OK:` ou `FAILED:`, suivi de la réponse.

Via TCP, QuizXpress n'envoie que le texte de réponse d'une commande réussie, et rien lorsqu'elle échoue ou n'a pas de réponse. Il est alors difficile pour une application de savoir quand une réponse est complète. Cochez 'TCP replies with OK/ERR status' pour obtenir une réponse à chaque commande, dans ce format :

- une première ligne `OK`, ou `ERR` suivi de la raison de l'échec de la commande ;
- pour `OK`, les lignes de la réponse ;
- une dernière ligne contenant uniquement un point (`.`).

Une ligne de réponse qui commence par un point reçoit un point supplémentaire devant, afin que votre application puisse lire des lignes jusqu'à recevoir un `.` seul. Par exemple, `setscore 3 0` suivi de `setscore 9 5` (l'appareil 9 n'existe pas) donne :

```
OK
0
.
ERR team 9 not found
.
```

## Essayer des commandes avec Telnet

Telnet est le moyen le plus simple d'essayer des commandes à la main ou de déboguer. Windows n'inclut pas le client Telnet par défaut ; pour l'installer :

1. Ouvrez 'Control Panel'.
2. Ouvrez 'Programs'.
3. Sélectionnez 'Turn Windows features on or off'.
4. Cochez 'Telnet Client'.
5. Cliquez sur 'OK'. Windows recherche les fichiers nécessaires et installe le client.

Ouvrez ensuite une invite de commandes et tapez `telnet localhost` (en supposant que QuizXpress utilise le port par défaut 23). Une fenêtre Telnet s'ouvre avec l'invite `qx>`. Tapez `help` pour voir toutes les commandes, ou `help <command>` pour obtenir de l'aide sur une commande :

![Session Telnet avec la commande help](../../assets/images/mb-telnet-help.webp){ loading=lazy }

!!! tip
    Ouvrez le [journal des messages](index.md#journal-des-messages) à côté de votre fenêtre Telnet : il affiche chaque commande reçue par QuizXpress et son résultat.
