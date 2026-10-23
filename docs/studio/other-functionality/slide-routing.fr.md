# Routage des diapositives

Normalement, un quiz se déroule de façon linéaire, de la diapositive 1 jusqu'à la fin. Avec le routage des diapositives, vous pouvez définir différents « parcours » dans vos quiz. Les parcours peuvent être statiques (par exemple, la diapositive 10 toujours suivie de la diapositive 20) ou dynamiques, selon le résultat d'une diapositive de vote. Avec l'option dynamique, vous pouvez laisser vos joueurs décider de la suite grâce à leurs votes, par exemple en leur faisant choisir un clip vidéo ou une musique à diffuser, ou la manche de questions à jouer.

Un visualiseur intégré aide à visualiser l'enchaînement des diapositives.

Vous définissez un parcours en attribuant un Id à la diapositive vers laquelle vous voulez sauter, dans les propriétés de la diapositive. Il peut s'agir d'un nom arbitraire mais unique qui a du sens pour vous en tant qu'auteur du quiz :

![](../../assets/images/image281.webp){ loading=lazy }

Ensuite, faites référence à cet Id dans la propriété « Next slide » de la réponse ou de l'image sur une diapositive Audience Response/Majority Rules :

![](../../assets/images/image282.webp){ loading=lazy }

L'exemple ci-dessus montre une diapositive Audience Response avec 4 images. Lorsque l'option A (Paris) obtient le plus de votes, le système saute à la diapositive dont l'Id est « Paris ».

Bien sûr, il peut arriver qu'il y ait égalité lors du vote, lorsque deux réponses ou plus ont le même nombre de votes. Le comportement dans ce cas peut être défini dans les propriétés de la diapositive (lorsque le routage est actif sur cette diapositive) avec la propriété « Next slide tie mode ». Il existe trois options :

- Re-vote, la diapositive est rechargée et le vote est refait jusqu'à ce qu'une réponse obtienne la majorité

- Randomize, le système choisit au hasard le parcours de l'une des réponses les plus votées

- Prompt, une invite est présentée à l'animateur (sur l'écran principal) pour qu'il fasse un choix

Chaque diapositive possède également une propriété « Next slide » qui définit la prochaine diapositive que le système présentera. Lorsqu'elle est laissée vide, le déroulement par défaut est suivi (passage à la diapositive suivante).

Pour sauter vers une diapositive autre que la diapositive suivante par défaut, renseignez la propriété « Next slide » de la diapositive elle-même. Un exemple : vous êtes à la fin d'une manche et vous souhaitez revenir à une diapositive de sélection de manche. En appliquant cela à l'exemple précédent, la dernière diapositive de la manche Paris peut renvoyer à la diapositive de vote.

![](../../assets/images/image283.webp){ width="298" loading=lazy } ![](../../assets/images/image284.webp){ width="271" loading=lazy }
