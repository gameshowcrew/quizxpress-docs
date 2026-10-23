# Présentation

QuizXpress Mobile permet aux joueurs d'utiliser leur téléphone mobile comme périphérique de saisie. Les joueurs peuvent rejoindre un quiz en se rendant sur notre site web buzzerpad (connexion internet requise) et en saisissant le code PIN affiché à l'écran pour se connecter.

QuizXpress Mobile offre également un moyen de jouer avec des téléphones mobiles sans connexion internet. Dans cette solution, les joueurs téléchargent l'application QuizXpress Smart Buzzer, disponible pour iOS et Android. Un routeur Wi-Fi est branché à l'ordinateur, et tous les joueurs s'y connectent avec leur téléphone. Après le démarrage d'un quiz, les joueurs peuvent se connecter dans l'application Smart Buzzer en appuyant sur le bouton *JOIN Wi-Fi Game*. L'application Smart Buzzer permet également de jouer via internet en saisissant un code PIN.

Grâce à cet ajout, QuizXpress prend désormais en charge :

| **Scénario** |                                                                | **Internet requis** | **Routeur Wi-Fi requis** | **Appareil mobile requis** | **Installation d'une application mobile requise** |
|--------------|----------------------------------------------------------------|-----------------------|---------------------------|----------------------------|-----------------------------------------|
| 1            | Keypads sans fil à radiofréquence (RF)                         | Non                   | Non                       | Non                        | Non                                     |
| 2            | Appareils mobiles sur buzzerpad.com via un navigateur web      | Oui                   | Non                       | Oui                        | Non                                     |
| 3            | Appareil mobile avec l'application Smart Buzzer sur Wi-Fi local | Non                   | Oui                       | Oui                        | Oui                                     |
| 4            | Appareil mobile avec l'application Smart Buzzer sur buzzerpad.com via un PIN | Oui     | Non                       | Oui                        | Oui                                     |

Tous les scénarios présentent des avantages et des inconvénients différents, et le meilleur choix dépend de vos besoins spécifiques.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 39%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Scénario</strong></th>
<th><strong>Avantages</strong></th>
<th><strong>Inconvénients</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1 Keypads RF sans fil</strong></td>
<td><p>Aucune dépendance externe vis-à-vis d'internet, du Wi-Fi ou d'appareils mobiles.</p>
<p>Simple à utiliser pour les joueurs.</p></td>
<td>Pas de capacités de saisie étendues (uniquement ABCDEF et fastest finger). Logistique de distribution des keypads aux joueurs et de récupération ensuite.</td>
</tr>
<tr class="even">
<td><strong>2 Navigateur sur buzzerpad.com</strong></td>
<td>Pas besoin de demander aux joueurs d'installer une application. Pour de grands groupes de joueurs (jusqu'à 2000).</td>
<td>Une connexion internet est requise</td>
</tr>
<tr class="odd">
<td><strong>3 Application sur Wi-Fi local</strong></td>
<td><p>Communication rapide à faible latence.</p>
<p>Prise en charge du mode headless (sans écran central).</p>
<p>Prise en charge de types de saisie étendus.</p></td>
<td>Avec une infrastructure de base (routeur Wi-Fi standard), seuls de petits groupes d'environ 50 joueurs sont pris en charge. Remarque : si aucune connexion internet ou de données mobiles n'est disponible, assurez-vous que les joueurs ont téléchargé l'application à l'avance</td>
</tr>
<tr class="even">
<td><strong>4 Application avec internet complet</strong></td>
<td><p>Prise en charge de grands groupes</p>
<p>Capacités de saisie étendues</p>
<p>Aucune configuration Wi-Fi locale nécessaire</p></td>
<td>Une connexion internet est requise</td>
</tr>
</tbody>
</table>

Le keypad mobile (à la fois buzzerpad et l'application Smart Buzzer) offre d'excellentes fonctionnalités :

- Les questions sont entièrement présentées sur l'appareil mobile, y compris les images et les effets.

- Différents types de questions spécifiques à l'utilisation d'un téléphone mobile :

  - Des questions numériques, par exemple pour demander le résultat d'une formule ou une année historique.

  - Des questions à texte libre (réponse unique ou multiple)

  - Des questions sur la première lettre (A-Z)

- Points bonus personnalisables pour les 3 équipes les plus rapides à répondre correctement.

- Expérience améliorée pour les questions d'ordre et les questions à plusieurs bonnes réponses. Les utilisateurs peuvent d'abord ordonner les réponses sur leur appareil, puis envoyer le résultat à QuizXpress en une seule fois.

- Fonction de télécommande grâce à l'application Mobile QuizXpress Director disponible pour iOS et Android. Pour plus d'informations, reportez-vous à 5.2.4.4.

En plus des fonctionnalités ci-dessus, l'application Smart Buzzer offre quelques fonctionnalités supplémentaires :

- Branding designer pour personnaliser l'application mobile avec des logos et des couleurs.

- Prise en charge du « mode headless » pour présenter un quiz sans écran central.

- Jingles d'équipe sélectionnables par l'utilisateur. Si vous avez configuré l'utilisation de jingles en définissant le dossier Jingles dans les paramètres (voir [Configurer les sons – l'onglet Sounds](../../setup/configuring-sounds-the-sounds-tab-page.md) ), une liste de tous les fragments sonores disponibles est présentée aux joueurs. Chaque joueur peut choisir un jingle qui sera utilisé pendant la partie dans les situations suivantes :

<!-- -->

- Points bonus - le son du joueur qui a été le premier à donner la bonne réponse est joué lorsque l'écran des points bonus est affiché.

- Fastest finger – le son du joueur qui a appuyé en premier est joué, tandis que le nom du joueur apparaît à l'écran dans le quiz player.

- Aperçus des scores intermédiaires – le son du joueur classé premier est joué lors de l'affichage du classement.

Voici quelques exemples de scénarios pris en charge :

- Un DJ qui présente un quiz dans un pub local sans couverture 4G. Les clients téléchargent l'application une seule fois et se connectent à un routeur Wi-Fi local pour jouer. Le pub n'a pas de téléviseur, le présentateur utilise donc le mode headless. Le DJ a personnalisé l'application aux couleurs de sa propre entreprise grâce au QuizXpress Branding Designer.

- Une grande société événementielle qui présente un quiz pour un grand groupe. La société ne souhaite pas que le public installe une application ; elle utilise donc buzzerpad.com et un code PIN pour faire participer les gens. Le quiz est présenté sur un immense écran affichant des vidéos, du son et des images.

- Une société événementielle qui diffuse un quiz sur internet à des milliers de joueurs, en utilisant un code PIN en mode serveur. La société a vendu des billets aux joueurs au préalable ; les billets sont validés lorsqu'un joueur se connecte à la partie et saisit son code dans la fenêtre contextuelle qui apparaît.
