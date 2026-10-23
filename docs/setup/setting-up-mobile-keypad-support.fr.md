# Configurer la prise en charge des keypads mobiles

QuizXpress permet d'utiliser des téléphones mobiles et des tablettes comme appareils de saisie. Les joueurs peuvent se connecter avec un navigateur web standard, ou utiliser notre application Smart Buzzer pour Android et iOS. Vous devez posséder une licence prenant en charge les keypads mobiles pour pouvoir activer cette fonctionnalité.

Pour activer la prise en charge des keypads mobiles, cochez d'abord la case ‘Enable mobile keypad support’. Trois sections à configurer apparaissent alors :

## Mode serveur

Il existe deux façons d'utiliser le système avec des keypads mobiles :

1)  Avec l'un de nos serveurs cloud (Internet requis pour vous et vos joueurs, qui peuvent participer depuis le monde entier)

2)  Avec un routeur Wi-Fi local connecté à votre ordinateur portable (aucune connexion Internet requise, mais tous les joueurs doivent se trouver au même endroit pour se connecter à votre routeur)

![](../assets/images/image324.webp){ width="455" loading=lazy }

Plusieurs options sont disponibles :

- **Play in ‘Headless’ mode** – À utiliser lorsqu'aucun écran externe\projecteur n'est disponible et que vous souhaitez que les joueurs jouent uniquement sur leur mobile. Veuillez noter que, dans ce cas, les mini-jeux ainsi que les questions vidéo ne sont pas pris en charge. En mode headless, seul l'écran Director est affiché sur l'ordinateur, avec un lecteur de quiz intégré (reportez-vous à [QuizXpress Director](../live/quizxpress-director/index.md) pour plus d'informations sur Director).

- **Show pictures on mobile device** – Indique si les images sont également envoyées à l'application Smart Buzzer / à l'application navigateur buzzerpad (remarque : pendant le quiz, vous pouvez activer ou désactiver cette option dans les Mobile Settings de Director).

- **Enable waiting room** – lorsque cette option est activée, tous les joueurs mobiles sont immédiatement définis comme ‘disabled’ après leur inscription et ne peuvent pas participer au quiz, bien que leur appareil affiche les questions. L'hôte doit d'abord activer chaque joueur dans Director. Utilisez-la, par exemple, lorsque les joueurs doivent payer un droit d'entrée avant de pouvoir participer.

- **Enable team name moderation – lorsque cette option est activée, le serveur buzzerpad analyse les noms des joueurs à la recherche de mots grossiers dans une liste prédéfinie (actuellement uniquement en néerlandais, anglais et français) et les remplace par ‘#####’**

- **Allow profile pictures – permet aux joueurs de télécharger leur photo de profil dans le quiz afin qu'elle apparaisse dans les classements et d'autres éléments visuels.Data collection with custom fields**

Le système permet de collecter des données auprès des utilisateurs individuels sur un écran qui s'affiche après leur connexion au quiz. Les champs à collecter peuvent être configurés ici dans Quiz Setup, et les données saisies seront disponibles après le quiz dans le fichier de sortie d'Analyzer.

![](../assets/images/image325.webp){ width="449" loading=lazy }

Pour ajouter un champ, cliquez sur Add et saisissez les détails dans la fenêtre contextuelle des champs personnalisés :

![](../assets/images/image326.webp){ width="296" loading=lazy }

Lorsque l'utilisateur se connecte, un écran de saisie de données lui est présenté, comme dans l'exemple suivant :

![](../assets/images/image327.webp){ width="211" loading=lazy }

En mode *Remote server*, vous pouvez sélectionner le serveur utilisé pour héberger votre session de quiz en cliquant sur le bouton *Configure proxy / server*. Le serveur par défaut est [www.buzzerpad.com](http://www.buzzerpad.com). Ce serveur est situé dans le centre-sud des États-Unis. Si vous êtes en Europe, vous pouvez passer à [www.buzzerpad.eu](http://www.buzzerpad.eu) pour une latence plus faible.

## Section Mobile keypad

Vous configurez ici la plage de keypads pouvant se connecter à votre quiz. Par défaut, lorsque vous activez la prise en charge des keypads mobiles, le champ ‘Mobile device range’ est rempli avec les identifiants de 1 jusqu'au nombre maximal de joueurs autorisé par votre licence.

Si vous disposez déjà d'un kit de buzzers ou de keypads, vous pouvez l'étendre avec des joueurs jouant sur des keypads mobiles. Dans ce cas, lorsque vous activez la prise en charge des keypads mobiles, un champ ‘Mobile device range’ commençant à l'identifiant de keypad ou de buzzer le plus élevé défini dans l'onglet Buzzers apparaît. Le nombre maximal est dans ce cas celui autorisé par votre licence.

Exemple : dans l'onglet Buzzers, vous indiquez que vous jouez avec les keypads QuizXpress 1-20. Dans l'onglet Mobile, vous activez la prise en charge des keypads mobiles. Si vous avez une licence Ultimate 50 (qui autorise jusqu'à 50 joueurs), le champ ‘Mobile device range’ sera rempli avec 21-50.

### Jouer en groupes

Lorsque vous voulez que votre public s'affronte en groupes avec des appareils mobiles, vous devez prédéfinir une liste de groupes. Lorsqu'un joueur se connecte à votre quiz, il est invité sur son appareil à sélectionner le groupe pour lequel il joue.

En cliquant sur le bouton ‘Groups’, un formulaire apparaît où vous pouvez configurer les groupes et leur comportement :

![](../assets/images/image328.webp){ width="298" loading=lazy }

Dans la section inférieure, vous définissez le comportement pour les questions de type doigt le plus rapide et les questions de vote.

### Personnaliser l'image de marque de l'application mobile

Lorsque vous jouez avec l'application QuizXpress Smart Buzzer, vous pouvez configurer votre propre image de marque avec le Branding Designer, en modifiant les couleurs, le logo et l'image d'accueil de l'application :

![](../assets/images/image329.webp){ width="549" loading=lazy }

Jouer avec des groupes prédéfinis

**Section Mobile host remote**

Cette section présente le code QR utilisé pour connecter l'application de télécommande à votre ordinateur.

L'application permettant de contrôler le quiz en cours est disponible pour Android et iOS. Vous les trouverez ici :

| Mobile Director pour Android | <https://play.google.com/store/apps/details?id=com.gameshowcrew.quizxpressdirector> |
|-----------------------------|-------------------------------------------------------------------------------------|
| Mobile Director pour iOS     | <https://apps.apple.com/us/app/quizxpress-director/id1493187163>                    |

Dans l'application Mobile remote, vous pouvez enregistrer plusieurs ordinateurs à contrôler. Ces ordinateurs sont affichés par leur ‘Location name’, qui peut être défini dans la section Mobile remote. Le nom par défaut est le nom de l'ordinateur.

Pour connecter la télécommande Mobile presenter à l'ordinateur, ouvrez l'application Virtual remote et cliquez sur le bouton ‘plus’. Un lecteur de code QR s'ouvre sur votre appareil mobile. Scannez le code QR affiché dans la section Mobile remote, et le nom saisi dans le champ ‘Location name’ sera ajouté à la liste des ordinateurs de l'application Mobile remote.

!!! warning

    veuillez noter que l'application dispose d'un paramètre de serveur qui doit correspondre au serveur sélectionné dans Quiz Setup. De plus, si vous utilisez le Wi-Fi, vous devez régler le paramètre de l'application sur ‘Wi-Fi’.**

## Autres options – Waiting room

Si vous lancez un quiz avec QuizXpress Mobile et souhaitez mieux contrôler qui entre dans la partie, vous pouvez utiliser le paramètre ‘Waiting Room’. Lorsque ce paramètre est actif, les joueurs qui entrent dans la partie sont inactifs par défaut.

Pour laisser des joueurs entrer dans la partie, activez-les explicitement dans l'onglet Teams de QuizXpress Director. Un exemple est un quiz de bar où les joueurs doivent payer un petit droit pour participer : à la réception du paiement d'un joueur, l'hôte peut activer ce joueur.
