# Personnaliser l'apparence du site web buzzerpad

Il existe trois façons de créer une apparence personnalisée pour le site web buzzerpad de QuizXpress :

1)  Nous pouvons acheter un nom de domaine personnalisé pour vous et créer une version à votre marque derrière ce domaine. Contactez-nous à info@gameshowcrew.com pour les détails et les tarifs.

2)  Vous pouvez passer des paramètres dans l'URL pour personnaliser l'apparence et créer un lien vers celle-ci depuis votre propre site web (vous ne voulez pas que vos clients aient à utiliser le long lien) ou utiliser un site comme https://tinyurl.com/ pour masquer les paramètres de l'URL. Si vous affichez un QR code à l'écran (appuyez sur Q lorsque le quiz est en cours dans le quiz player) pour permettre aux joueurs d'accéder facilement au buzzer web, vous pouvez indiquer les paramètres de personnalisation du QR code dans QuizXpress Director. Dans l'onglet Mobile, appuyez sur Settings et, dans la boîte de dialogue de configuration qui s'affiche, saisissez les paramètres dans le champ URL Extension. Pour plus d'informations, reportez-vous à 5.7.8.3.

3)  Intégrer le site web buzzerpad dans un iFrame et transmettre les paramètres depuis la

> référence de l'iFrame. Cela vous permet également d'ajouter votre flux de diffusion (comme YouTube) sur la même
>
> page. Si vous avez besoin de plus d'informations à ce sujet, n'hésitez pas à nous contacter à info@gameshowcrew.com.

Personnalisation avec des paramètres d'URL

Vous pouvez passer plusieurs paramètres au site web buzzerpad pour en personnaliser l'apparence selon vos besoins. Les paramètres sont les suivants :

| **Nom**     | **Description**                                                                                           | **Exemple**                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| name        | Transmet le nom du joueur                                                                                 | name=John                                                   |
| fname       | Transmet le nom du joueur et rend le champ de saisie en lecture seule                                     | fname=Peter                                                 |
| themecolor  | La couleur principale du site                                                                             | themecolor=FE5602                                           |
| about       | Le texte « à propos » affiché sur la page de connexion (veillez à utiliser l'échappement HTML pour le caractère espace, etc.) | about=About%20QuizXpress                    |
| abouturl    | L'URL vers laquelle le texte « à propos » doit pointer                                                    | abouturl=https://www.quizxpress.com                         |
| gotext      | Le texte du bouton GO                                                                                     | gotext=ENTER (remarque : veillez à encoder correctement la chaîne) |
| compact     | Passez 1 pour rendre la disposition de l'écran de connexion plus compacte                                 | compact=1                                                   |
| logo        | URL de votre propre logo. Assurez-vous que le logo fait 120 pixels de haut, avec un fond transparent      | logo=https://www.quizxpress.com/logo.png                    |
| pin         | Transmet le code PIN afin que le joueur n'ait pas besoin de le saisir                                     | pin=12345                                                   |
| ticket      | Transmet le code du billet                                                                                | ticket=AG1234F                                              |
| uid         | Transmet une identité d'utilisateur fixe sous forme de GUID (le format hexadécimal est XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX) | uid=aed6373a-db53-499d-9428-a7ad22289272  |
| autoconnect | Lorsque vous transmettez *fname*, *pin* et *autoconnect*=1, le keypad se connecte automatiquement         | pin=12345&fname=Player1&autoconnect=1                       |

Par exemple :

[https://buzzerpad.eu/?compact=1&logo=https://quizxpress.com/files/quiztime.png&themecolor=E46C0A&about=About%20Quiz%20Time](https://buzzerpad.eu/?compact=1&logo=https://quizxpress.com/files/quiztime.png&themecolor=E46C0A&about=About%20Quiz%20Time%20)

Le rendu sera le suivant :

![](../../assets/images/image397.webp){ width="286" loading=lazy }

L'image du logo « quiz time » a été téléversée sur le site quizxpress.com afin de pouvoir être utilisée comme logo personnalisé. Votre logo doit être hébergé quelque part sur votre propre site web.
