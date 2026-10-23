# Configurer les équipes – l'onglet Teams

L'onglet Teams existe en deux ‘versions’ : l'une lorsque des buzzers Sony sont sélectionnés dans l'onglet ‘Buzzers’, l'autre lorsque des buzzers Fleetwood Reply ou QuizXpress (appareils numérotés) sont sélectionnés.

## Onglet Teams – Buzzers Sony

L'onglet Teams utilisé lorsque des buzzers Sony sont sélectionnés se trouve ci-dessous. Fonctionnalités :

- Ajout et suppression d'équipes

- Indication de la participation ou non d'une équipe au quiz.

- Attribution d'avatars aux équipes. En bas de la page des paramètres des équipes, vous pouvez indiquer dans quel dossier se trouvent les avatars utilisés.

En haut de la page, vous voyez combien de jeux de buzzers sont nécessaires compte tenu du nombre d'équipes participantes dans la liste.

Une autre fonctionnalité est la possibilité d'utiliser des équipes anonymes. Dans ce cas, la liste des équipes/avatars est ignorée, et le processus d'inscription ressemble à celui des buzzers Fleetwood Reply. Cela s'utilise généralement lorsqu'un grand nombre de buzzers Sony sont employés, car la procédure d'inscription normale des buzzers Sony — qui associe un à un chaque buzzer à une équipe — prendrait trop de temps.

![](../assets/images/image330.webp){ width="605" loading=lazy }

## Onglet Teams – Keypads QuizXpress

Dans l'onglet Teams, vous pouvez définir les noms des équipes/joueurs et définir des groupes. Cet onglet n'est pas disponible lorsque seul Mobile est utilisé ; lorsque Mobile est utilisé en combinaison avec des keypads ou des buzzers, la page est toujours affichée.

Pour tous les types de buzzers sauf les buzzers Sony, le nombre d'équipes est déduit de la chaîne ‘Keypads’ saisie dans l'onglet ‘Buzzers’. Par exemple, lorsque la chaîne 1-50 est utilisée, l'onglet ‘Teams’ affiche une liste de keypads de 1 à 50 et les noms d'équipe par défaut *Team 1 … Team 50*. Les noms d'équipe peuvent être modifiés dans la deuxième colonne de la liste.

Comme expliqué ci-dessus, si vous souhaitez modifier le nombre d'équipes, modifiez la chaîne ‘Keypads’ dans l'onglet ‘Buzzers’.

!!! note

    il est possible d'utiliser des avatars avec des buzzers Reply/QuizXpress. Pour cela, créez des images (.jpg ou .gif) dans le dossier d'avatars par défaut (c:\program files\game show crew\QuizXpress\Data\IQ\Avatars) portant le nom des équipes. Par exemple, pour Team A, créez une image nommée ‘Team A.jpg’.

Comme on peut le voir sur l'image ci-dessous, diverses autres commandes sont disponibles :

- Generate Names : permet de générer rapidement des noms d'équipe selon un certain modèle, suivi d'un index. Par exemple, vous pouvez générer rapidement des noms comme team 1…team 50, player 1…player 50, participant 1…participant 50

- Import : importer la liste des noms d'équipe depuis Excel ou un fichier texte. Pour Excel, placez les noms dans la première colonne de la première feuille ; pour un fichier texte, mettez chaque nom sur une nouvelle ligne.

- Save to PDF : pour obtenir un aperçu des équipes attribuées à chaque keypad, exportez la liste en PDF en appuyant sur le bouton ‘Save to PDF’

- Groups : il est possible de répartir les équipes en groupes. Vous en saurez plus dans la section suivante.

> ![](../assets/images/image331.webp){ width="605" loading=lazy }

### Regrouper les keypads

Il est possible de répartir les équipes en groupes dans Quiz Setup (il est également possible de le faire pendant le déroulement d'un quiz. Pour plus d'informations à ce sujet, reportez-vous à la section [Demographic](../live/starting-a-quiz/the-quiz-screen-voting-everybody-answers.md#demographic) sur les diapositives de quiz démographiques.

Lorsque vous cliquez sur le bouton ‘Groups’, une liste s'affiche où vous pouvez saisir les noms des groupes et l'ensemble de keypads correspondant. Voir l'image ci-dessous :

![](../assets/images/image332.webp){ width="605" loading=lazy }

En appuyant sur le bouton ‘Add’, une fenêtre apparaît où vous pouvez saisir à la fois le nom du groupe et les keypads correspondants (en saisissant une chaîne de keypads). Vous pouvez également supprimer des groupes.

Lors de la saisie de la plage de keypads d'un groupe (par exemple, ‘1, 2, 3, 10-20’), une vérification confirme que la plage se situe dans la plage de keypads définie dans l'onglet ‘Buzzers’. Si ce n'est pas le cas, un message d'erreur s'affiche.

Les autres paramètres que vous pouvez modifier ici concernent le comportement des groupes pour les questions de type doigt le plus rapide et les questions de vote.

Les options pour les questions de type doigt le plus rapide sont :

| **Lockout**    | Avec cette option activée, seul le premier joueur d'un groupe à répondre peut répondre à la question. Si la réponse fournie est fausse, tout le groupe est verrouillé. |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **No lockout** | Si la première personne du groupe répond faux, une autre personne du groupe peut encore tenter sa chance.                                                                    |

Les options pour les questions de vote sont :

| **Accept only the first response** | Seule la première réponse reçue du groupe compte et ajoute des points au score du groupe |
|------------------------------------|--------------------------------------------------------------------------------------------|
| **Sum points**                     | Toutes les réponses sont acceptées, et les points sont additionnés                                      |
| **Average points**                 | Toutes les réponses sont acceptées, et la moyenne des points est calculée                                    |

#### Afficher les réponses des groupes en temps réel pendant le quiz

Lorsque vous activez le paramètre ‘Show real time group responses’, les réponses de chaque groupe sont affichées à l'écran en temps réel pendant le jeu télévisé.

![](../assets/images/image333.webp){ width="442" loading=lazy }

Pendant le compte à rebours, vous voyez pour chaque groupe le nombre de joueurs du groupe, ainsi que le nombre de ceux qui ont déjà répondu. Par exemple, dans l'image ci-dessus, le groupe HR compte 15 joueurs, dont 3 ont déjà répondu.

À la fin du compte à rebours, le nombre de bonnes réponses, le nombre de mauvaises réponses et le pourcentage de bonnes réponses sont affichés par groupe.

![](../assets/images/image334.webp){ width="463" loading=lazy }

### Attribuer des appareils Galaxy et des tableaux des scores aux participants

Lorsque votre licence QuizXpress inclut la prise en charge des appareils Galaxy ou des tableaux des scores, vous voyez les options suivantes dans l'onglet Buzzers de QuizXpress Setup :

![](../assets/images/image335.webp){ width="234" loading=lazy }

Lorsque vous activez la prise en charge de Galaxy ou des tableaux des scores, des colonnes supplémentaires apparaissent dans la liste de l'onglet Teams.

![](../assets/images/image336.webp){ width="504" loading=lazy }

Chaque appareil Galaxy ou tableau des scores possède un identifiant. Dans cette liste, vous pouvez indiquer quel identifiant d'appareil Galaxy et/ou de tableau des scores est utilisé pour chaque joueur.
