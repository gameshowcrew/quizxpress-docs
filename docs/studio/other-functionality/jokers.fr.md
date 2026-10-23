# Jokers

Les joueurs peuvent utiliser des Jokers, des jetons qui permettent d'influencer l'issue d'un quiz ! Les joueurs peuvent choisir de jouer un Joker chaque fois qu'ils pensent que cela leur donnera un avantage. Les Jokers ne sont disponibles que lorsque l'on joue avec des téléphones mobiles.

![](../../assets/images/image287.webp){ loading=lazy }

Actuellement, trois types de Jokers sont disponibles :

- **Time Warp**, avance le temps afin que les autres joueurs aient moins de temps pour répondre

- **Free Ride**, obtient automatiquement la bonne réponse à la question sans y répondre

- **Point Boost**, les joueurs voient les points gagnés pour une question multipliés lorsqu'ils répondent correctement

Les Jokers sont définis dans Studio pour l'ensemble du quiz en cliquant sur File > Options :

![](../../assets/images/image288.webp){ width="234" loading=lazy }

Pour chaque type, vous pouvez configurer les éléments suivants :

**Point booster**

- Available : combien de fois le joker peut être utilisé par un joueur

- Multiplier : combien de fois les points gagnés sont multipliés

- Handle on screen : le lecteur de quiz indique qu'un joker a été joué

Free Ride

- Available : combien de fois le joker peut être utilisé par un joueur

- Handle on screen : le lecteur de quiz indique qu'un joker a été joué

**Time Warp**

- Available : combien de fois le joker peut être utilisé par un joueur

- What is the remaining time when the joker has been used : quel est le temps restant lorsque le joker a été utilisé

!!! note

    Time Warp est toujours affiché à l'écran, car il affecte tous les joueurs

Show team playing the joker : affiche le nom de l'équipe dans l'indicateur de joker affiché à l'écran dans le lecteur de quiz lorsqu'un joueur joue un joker.

Les jokers sont automatiquement activés sur toutes les diapositives de type Question. S'il y a des questions pour lesquelles vous ne souhaitez pas que les Jokers soient utilisés, vous pouvez les désactiver explicitement dans les propriétés de la diapositive :

![](../../assets/images/image289.webp){ width="333" loading=lazy }

![](../../assets/images/image290.webp){ width="180" loading=lazy }

Lorsque des jokers sont disponibles, les joueurs voient un menu sur leur Smart Buzzer (application ou web) grâce auquel ils peuvent jouer le joker de leur choix :

!!! note

    un seul joueur peut jouer un Time Warp par question, et Free Ride et Point Booster s'excluent mutuellement (vous pouvez utiliser l'un ou l'autre). D'autres types de Jokers seront disponibles dans les versions futures.
