# Module Wheel of Fortune

Wheel of Fortune permet de faire tourner une roue pour tirer un prix ou des points pour une équipe, ou simplement tirer une équipe précise.

![La Wheel of Fortune avec des prix et des points](../../assets/images/wheel-of-fortune-game.webp){ loading=lazy }

Vous trouverez ci-dessous les écrans de configuration avec leurs paramètres par défaut :

| ![L'onglet ‘Game’](../../assets/images/wheel-of-fortune-settings-game.webp){ width="240" loading=lazy } | ![L'onglet ‘Appearance’](../../assets/images/wheel-of-fortune-settings-appearance.webp){ width="240" loading=lazy } | ![L'onglet ‘Other’](../../assets/images/wheel-of-fortune-settings-other.webp){ width="240" loading=lazy } |
|---|---|---|

- Participants : choisissez qui joue avec la roue.

    - ‘Select participating players before game’ : vous sélectionnez les joueurs sur l'écran du Director, juste avant le lancement de la roue.
    - ‘Play the game with the top’ : le nombre indiqué de joueurs les mieux classés jouent avec la roue.
    - ‘The player with this ranking can stop the wheel for a prize’ : un seul joueur d'un certain rang peut arrêter la roue avec son keypad. Décochez ‘Show player’ pour masquer le panneau qui indique qui est ce joueur.
    - ‘Play with the winner of the last question’ : l'équipe qui a donné la première la bonne réponse à la question précédente joue avec la roue. Si personne n'a répondu correctement à cette question, la roue est ignorée.
    - ‘None (wheel only)’ : seule la roue est affichée, sans équipes. Utilisez cette option pour tirer un prix pour quelqu'un dans la salle. Les points de la roue sont affichés, mais ne sont pas attribués à une équipe.

- Draw a prize : les prix (qui peuvent aussi être des points positifs ou négatifs) sont affichés sur la roue. En appuyant sur le bouton ‘Setup prizes’, les prix peuvent être configurés, voir [Configuration des prix](#configuration-des-prix).

- Draw a team/player : les participants sélectionnés sont répartis sur la roue. Sous ‘Show in wheel’, vous choisissez si la roue affiche les noms des équipes ou les numéros de keypad. Le nombre de segments de la roue peut être choisi en sélectionnant une valeur pour ‘Number of segments’. Si la case située devant ‘Show prize’ est cochée, les prix qui peuvent être gagnés (ou perdus) sont affichés à côté de la roue. Pendant que la roue tourne, les prix s'illuminent les uns après les autres. Lorsque la roue s'arrête sur un joueur/une équipe, le prix mis en évidence est gagné (ou perdu, dans le cas de points négatifs). Les prix (ou les points) peuvent être définis en appuyant sur le bouton ‘Setup prizes’. Ce mode ne fonctionne pas en combinaison avec l'option ‘stop the wheel’ de la section ‘participants’, car des prix sont nécessaires sur la roue pour le jeu ‘stop the wheel’, ni avec ‘None (wheel only)’.

- Draw bonus points : les points positifs, négatifs et Kapow! sont répartis sur la roue dans le nombre de segments indiqué. Pour les points positifs et négatifs, chaque segment augmente ou diminue respectivement en valeur (par exemple : des points positifs de 1 avec 5 segments donnent les valeurs 1, 2, 3, 4 et 5 ; des points négatifs de -2 avec 4 segments donnent les valeurs -2, -4, -6, -8). Les points Kapow! sont des points négatifs fixes sur le nombre de segments indiqué. Les segments Kapow! sont ceux sur lesquels les joueurs ne veulent pas tomber ! Le nombre total de segments pour la section ‘Draw bonus points’ ne peut pas dépasser 40.

- Onglet Appearance : définissez le texte du titre du jeu, la police du titre (également utilisée pour le panneau à côté de la roue et pour le résultat) et la police du texte sur la roue. Choisissez une image d'arrière-plan ainsi que l'image affichée au centre de la roue. Sans image centrale, la roue affiche une étoile dorée au centre. Sous ‘Sound’, vous pouvez choisir une musique (un fichier MP3) qui joue tant que la roue est à l'écran.

- Onglet Other : réglez la vitesse de rotation de la roue ainsi que la durée de rotation.

## Configuration des prix

![La fenêtre ‘Setup prizes’](../../assets/images/wheel-of-fortune-setup-prizes.webp){ loading=lazy }

Chaque ligne est un prix :

- Prize type : ‘Prize’ pour quelque chose à gagner, ou ‘Points’ pour gagner des points (ou en perdre, avec un nombre négatif).
- Points : le nombre de points pour un prix ‘Points’. La roue affiche ce nombre.
- Prize name : le texte sur la roue et dans le message destiné au gagnant.
- Repeat : le nombre de segments que le prix occupe sur la roue. Un prix qui apparaît plusieurs fois est réparti sur la roue.
- Image : une image facultative, affichée sur la roue à la place du nom.

La fenêtre commence avec huit lignes. Appuyez sur ‘Add prize’ pour obtenir plus de lignes, jusqu'à 40 prix. Les lignes vides au-delà des huit premières sont supprimées lorsque vous appuyez sur ‘OK’. La roue peut contenir 40 segments au total, ou 24 lorsque les prix ont une image.

La même fenêtre permet de configurer les prix affichés à côté de la roue lorsque vous tirez une équipe/un joueur. La colonne ‘Repeat’ n'y est pas utilisée.

!!! note
    Les anciennes versions de QuizXpress ne prennent en charge que huit prix. Jouez un quiz comportant davantage de prix sur un ordinateur doté de la dernière version.

## Jouer

Pour faire tourner la roue, appuyez sur le bouton ‘Spin’ dans le panneau de gauche.

![](../../assets/images/image143.webp){ width="142" loading=lazy }

Pendant que la roue tourne, les lumières autour de la jante défilent. Lorsque la roue s'arrête, le segment situé sous le pointeur clignote et conserve un contour doré, et le résultat est affiché en bas de l'écran.

![Le résultat après un tour](../../assets/images/wheel-of-fortune-result.webp){ loading=lazy }

Lorsque le paramètre ‘Stop the wheel’ est activé, le joueur qui peut arrêter la roue avec son keypad est indiqué dans le panneau ‘Teams’ du jeu. Le buzzer sous le nom tremble lorsque le joueur appuie sur son keypad. La roue peut aussi être arrêtée en appuyant sur le bouton ‘Stop the Wheel!’ (mais cela n'est généralement pas nécessaire, puisque le joueur doit arrêter la roue).

![Le joueur qui peut arrêter la roue](../../assets/images/wheel-of-fortune-stop-the-wheel.webp){ loading=lazy }

![](../../assets/images/image144.webp){ width="143" loading=lazy }
