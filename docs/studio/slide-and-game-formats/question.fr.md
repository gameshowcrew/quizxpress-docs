# Question

Ce type correspond à une question de quiz classique. Les variantes suivantes sont possibles :

- *Everyone Answers (également appelé vote) :* permet à chaque joueur de répondre à une question.

- *Lock-out (également appelé fastest finger)* : le joueur qui appuie le premier sur son buzzer a le droit de répondre à une question.

- *Question à choix multiples* : question avec plusieurs réponses parmi lesquelles les joueurs peuvent choisir. Les réponses données sont jugées automatiquement par le système (c’est-à-dire si ‘Judge question’ est réglé sur ‘Automatically’). Vous pouvez créer une question à choix multiples en allant dans l’onglet DESIGN et en changeant la mise en page pour une mise en page comportant plusieurs réponses.

- *Question ouverte (sans choix multiples)* : question à laquelle un joueur/une équipe répond oralement, puis qui est jugée par l’animateur de quiz (à l’aide de sa télécommande de présentateur, du clavier ou de QuizXpress Director). Vous pouvez créer une question ouverte en allant dans le menu DESIGN et en changeant la mise en page pour une mise en page sans réponses. Dans la section ‘input mode’, sélectionnez ‘default’ comme mode de saisie.

- Types de saisie étendus, qui concernent les questions avec des réponses numériques, en texte complet ou à première lettre. Ces questions peuvent être répondues avec l’application QuizXpress Smart Buzzer ou avec le site web buzzerpad. Vous pouvez créer une question ouverte avec une réponse numérique, une lettre ou un texte en sélectionnant ‘number’, ‘letter’ ou ‘text’ comme mode de saisie.

Dans la section des points, vous pouvez indiquer le nombre de points à gagner pour une bonne réponse, le nombre de points perdus pour une mauvaise réponse et le nombre de points perdus lorsqu’aucune réponse n’est donnée. Vous pouvez aussi faire diminuer les points au fur et à mesure que le chronomètre décompte pendant une question. Pour cela, saisissez le nombre de points ‘At start’ et ‘At end’. Vous pouvez faire de même pour les points de pénalité (*Wrong answer* et *No answer*).

![](../../assets/images/image30.webp){ width="222" loading=lazy }

Avec ces options, vous pouvez récompenser par davantage de points les joueurs qui répondent rapidement. En même temps, les mauvaises réponses peuvent être davantage pénalisées au début d’une question afin d’éviter que les gens ne devinent/ne parient immédiatement après le début du compte à rebours.

Pour une question à choix multiples, vous pouvez définir des points de bonus de rapidité pour les trois joueurs les plus rapides à répondre correctement. Cela donne une question de type ‘tout le monde peut répondre’, avec un élément ‘fastest finger’. Pour accéder au réglage des points de bonus, cliquez sur le bouton ‘Speed Bonus’ dans la section Points, après quoi le formulaire suivant s’ouvre :

![](../../assets/images/image31.webp){ width="201" loading=lazy }

Attribuez une valeur supérieure à zéro pour chaque entrée (si vous souhaitez récompenser uniquement le joueur le plus rapide, ne renseignez que les points du premier à répondre). Pendant le quiz, un indicateur animé de points de bonus apparaît à l’écran une fois la question terminée pour mettre en avant le ou les joueurs qui ont gagné les points de bonus.

Le jingle du joueur arrivé premier au bonus sera également joué (pour plus d’informations sur les jingles, veuillez consulter [Configuring sounds – the Sounds tab page](../../setup/configuring-sounds-the-sounds-tab-page.md))

![](../../assets/images/image32.webp){ width="275" loading=lazy }

## Questions à choix multiples

Lorsque vous créez une question à choix multiples, vous pouvez indiquer dans QuizXpress Studio laquelle des réponses est la bonne. Si vous le faites, QuizXpress peut juger l’exactitude des réponses données par les équipes pendant le quiz. Vous pouvez indiquer quelle réponse est la bonne en sélectionnant d’abord l’une des réponses avec la souris, puis en cochant ‘Correct Answer’ dans le panneau de propriétés. Vous pouvez aussi utiliser le menu contextuel en sélectionnant d’abord la réponse, puis en faisant un clic droit et en choisissant ‘Set correct answer’. De plus, vous pouvez définir les bonnes réponses des questions à choix multiples dans la représentation ‘Table Mode’ des questions (cliquez sur l’onglet VIEW puis sur ‘Table Mode’). Dans la dernière colonne de la grille, vous pouvez indiquer la bonne réponse pour les questions à choix multiples (à réponse unique).

## Plusieurs bonnes réponses

QuizXpress permet d’avoir plusieurs bonnes réponses. Les options suivantes sont disponibles :

### Single correct

C’est le mode par défaut, dans lequel une question à choix multiples n’a qu’une seule bonne réponse.

### Multiple correct (one response)

Dans ce mode, la question peut avoir plusieurs bonnes réponses, mais les joueurs ne peuvent en choisir qu’une seule. Pour chaque réponse, vous pouvez définir une exactitude différente le cas échéant. Vous pouvez l’utiliser pour créer des questions où les joueurs peuvent gagner plus de points s’ils sont ‘plus proches’ de la bonne réponse, comme l’illustre la question ci-dessous (2000 est la réponse exacte) :

![](../../assets/images/image33.webp){ width="449" loading=lazy }

L’‘exactitude’ (correctness) d’une réponse se définit en faisant un clic droit sur la réponse et en sélectionnant ‘Set Correctness’ dans le menu contextuel. La boîte de dialogue suivante vous aide à définir la valeur d’exactitude :

![](../../assets/images/image34.webp){ width="311" loading=lazy }

Vous pouvez aussi l’utiliser pour créer des questions de style ‘Family Feud’ comme celle ci-dessous. En donnant aux réponses l’exactitude correspondant aux pourcentages des réponses de Family Feud, choisir une réponse plus populaire rapportera plus de points au joueur. Si vous fixez les points de la question à 100, le nombre de points qu’un joueur peut gagner en donnant une certaine réponse est le pourcentage correspondant.

![](../../assets/images/image35.webp){ loading=lazy }

### Multiple correct (multiple responses)

Dans ce mode, la question peut également avoir plusieurs bonnes réponses, chacune avec une ‘exactitude’ différente, mais les joueurs peuvent désormais sélectionner plus d’une réponse. Ainsi, par exemple, lorsque les réponses A et C sont toutes deux définies comme correctes (chacune avec 50 % d’exactitude), les joueurs peuvent gagner 100 % des points en répondant à la question avec *à la fois* A et C. S’ils répondaient avec A et B à la place, ils ne gagneraient que 50 % des points.

Si les joueurs doivent répondre avec toutes les bonnes réponses pour gagner des points, sélectionnez la question et, dans le panneau de propriétés, réglez le ‘response mode’ sur ‘multiple responses, exact match’.

### Ordered

Dans ce mode, un joueur doit mettre les réponses dans le bon ordre. Vous pouvez créer des questions comme celle présentée ci-dessous (la bonne réponse serait C->A->D->B).

Si vous voulez que les joueurs donnent l’ordre exact pour gagner des points, sélectionnez la question et, dans le panneau de propriétés, réglez le ‘ordered answer mode’ sur ‘exact match’ (qui est la valeur par défaut). Si donner un ordre partiellement correct doit également rapporter des points, réglez le ‘ordered answer mode’ sur ‘partial match’. Dans ce cas, le pourcentage de réponses placées au bon endroit donnera le même pourcentage des points qui peuvent être gagnés pour la question. Par exemple, si l’ordre correct est ABCD et qu’un joueur répond ACBD, cela donnera 50 % des points qui peuvent être gagnés pour la question.

![](../../assets/images/image36.webp){ loading=lazy }

Pour modifier l’ordre, faites un clic droit sur l’une des réponses ordonnées et cliquez sur ‘Set Order’ :![](../../assets/images/image37.webp){ width="284" loading=lazy }

## Questions numériques, en texte complet et à première lettre

QuizXpress prend en charge trois types de saisie utilisables avec l’application Smart Buzzer ou le site web buzzerpad : numérique, texte complet et première lettre. Vous pouvez utiliser ces types de saisie en combinaison avec une question ouverte. Les options sont les suivantes :

![](../../assets/images/image38.webp){ width="286" loading=lazy }

Choisir *Default* pour une question ouverte donne une question classique de type fastest finger, qui peut se jouer avec des buzzers ou des keypads. Avec l’application Smart Buzzer ou le site web buzzerpad, un buzzer est affiché à l’écran. La personne qui appuie en premier verrouille les buzzers de tous les autres joueurs et répond oralement à l’animateur de quiz.

### Saisie de nombre

|     |
|-----|

![](../../assets/images/image39.webp){ width="126" loading=lazy }Pour le type de saisie *Number*, l’application Smart Buzzer ou le site web buzzerpad présente aux joueurs un écran où ils peuvent saisir une valeur numérique.

Pour les questions numériques, vous pouvez aussi spécifier une plage comme ‘80-90’. Cela signifie que toutes les réponses comprises (bornes incluses) entre 80 et 90 sont jugées correctes. Vous pouvez aussi transformer la question en question d’approximation (par exemple ‘combien y a-t-il de billes dans le bocal’) où seul le joueur dont la réponse est la plus proche de la bonne réponse obtient des points. Dans ce cas, cochez ‘Nearest wins’. S’il y a plusieurs gagnants, les joueurs qui ont donné la réponse le plus rapidement remportent les points.

Dans les questions numériques de type nearest-wins, un nombre quelconque de joueurs peut gagner des points. Vous configurez le nombre de gagnants dans la grille de propriétés en modifiant le champ ‘Nearest Wins’.

![](../../assets/images/image40.webp){ width="413" loading=lazy }

Dans ce cas, les 3 joueurs les plus proches de la bonne réponse gagnent des points.

### Saisie de texte complet

Le type *Full-Text* permet aux joueurs de saisir du texte libre (sans distinction de casse ; les majuscules n’ont pas d’importance).

Pour les questions en texte complet, vous pouvez indiquer si vous voulez une correspondance exacte avec les réponses données, ou utiliser une correspondance approximative (fuzzy matching) et définir une tolérance pour admettre de petites fautes d’orthographe. Si vous voulez autoriser plusieurs réponses, vous pouvez saisir plusieurs textes dans le champ ‘correct answer’, séparés par un point-virgule (par exemple ‘Belgium;Belgique;Belgie’). Utilisez l’option Test pour vérifier que la tolérance des réponses texte en ‘fuzzy match’ fonctionne correctement.

#### Questions en texte complet à réponses multiples

Les questions texte peuvent aussi avoir plusieurs réponses. Par exemple, vous pouvez jouer une chanson et demander l’artiste et le titre. Chaque bonne réponse rapportera 50 % des points. Supposons que vous jouiez une chanson de Madonna intitulée Holiday et que vous vouliez que les joueurs répondent à la fois l’artiste et le titre :

1)  Créez une question texte standard avec la bonne réponse : Madonna ![](../../assets/images/image41.webp){ width="602" loading=lazy }

2)  Allez dans les propriétés avancées de la diapositive et cherchez ‘Full-text answers’.

3)  Cliquez sur les trois points \[…\] pour ouvrir l’éditeur Full-text answer et ajoutez le titre de la chanson ‘Holiday’. Si nécessaire, vous pouvez aussi définir la correspondance approximative par réponse ou saisir des variantes de réponse pour chaque bonne réponse, séparées par un point-virgule :

Lorsque la question est présentée, le joueur voit l’écran suivant :

![](../../assets/images/image42.webp){ width="335" loading=lazy }

Par défaut, le joueur voit autant de champs de saisie qu’il y a de bonnes réponses définies, mais vous pouvez aussi limiter le nombre de champs avec le paramètre ‘Full-text response limit’ :

![](../../assets/images/image43.webp){ width="377" loading=lazy }

Ainsi, par exemple, vous pourriez demander ‘Citez 4 pays qui bordent l’Allemagne’, régler la Full-text response limit sur 4 et saisir les 9 pays limitrophes comme bonnes réponses.

### Saisie de lettre

Pour le type *Letter*, une grille de A à Z est présentée aux joueurs pour qu’ils choisissent une lettre.

Les questions avec le type de réponse lettre affichent sur le téléphone une grille avec toutes les lettres de l’alphabet. Les joueurs choisissent la première lettre de ce qu’ils pensent être la réponse. À la fin de la question, le buzzer indique si la réponse était correcte ou incorrecte, ainsi que la bonne réponse complète.

Pour les questions à première lettre, vous pouvez aussi afficher la grille de lettres mélangée sur le buzzer mobile (une fois ou toutes les 2 secondes) pour ajouter une difficulté supplémentaire aux joueurs. Ce paramètre est disponible dans le panneau des propriétés avancées de la diapositive :

![](../../assets/images/image44.webp){ width="231" loading=lazy }

Lorsque cette option est réglée sur *Shuffle* ou *Moving*, la grille du buzzer a une disposition aléatoire :

![](../../assets/images/image45.webp){ width="187" loading=lazy }

## Questions d’association
