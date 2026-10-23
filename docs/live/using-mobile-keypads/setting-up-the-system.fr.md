# Configurer le système

Comme indiqué précédemment, le système offre plusieurs possibilités adaptées à différents scénarios. Pour plus d'informations sur la configuration de QuizXpress pour une utilisation avec des téléphones mobiles, reportez-vous également à [Configurer la prise en charge des keypads mobiles](../../setup/setting-up-mobile-keypad-support.md).

**Mode serveur**

Lorsque vous utilisez le système en mode serveur, vous avez besoin d'une **connexion internet fiable** avec un débit correct. Le trafic de données de QuizXpress n'est pas très élevé comparé, par exemple, à un flux vidéo, mais une connexion peu fiable ou de fortes chutes de débit auront un impact majeur sur le système et sur l'expérience globale. Bien sûr, si vous diffusez en même temps votre quiz sur internet, le flux vidéo peut nécessiter des exigences supplémentaires. Il est toujours conseillé de connecter votre ordinateur à votre routeur par câble pour obtenir une connexion plus constante et plus fiable. Votre public peut participer à votre quiz de deux manières : via le site web buzzerpad.com ou via l'application Smart Buzzer. Voir les chapitres suivants pour plus de détails. Dans [Configurer la prise en charge des keypads mobiles](../../setup/setting-up-mobile-keypad-support.md), vous trouverez toutes les informations sur la configuration du système en mode serveur dans Quiz Setup.

**Mode Wi-Fi autonome**

Dans une configuration Wi-Fi autonome, vous connectez votre ordinateur portable à votre routeur à l'aide d'un câble réseau. Le routeur sert de point d'accès Wi-Fi local pour les appareils mobiles de vos joueurs, votre appareil exécutant l'application de télécommande et votre ordinateur portable. Voir ci-dessous une image d'une telle configuration :

![](../../assets/images/image355.webp){ width="604" loading=lazy }

L'ordinateur portable obtient une adresse IP du routeur local et n'a besoin d'aucune connexion internet. Un routeur standard correct prend en charge jusqu'à environ 50 joueurs ; il existe également des routeurs capables de gérer davantage de connexions. Les téléphones/tablettes doivent se connecter au même routeur et, lors du lancement de l'application Smart Buzzer, le bouton JOIN WI-FI GAME est activé dès que l'appareil trouve le quiz en cours.

Notez que certains logiciels antivirus incluent des pare-feu intégrés très stricts, qui nécessitent une configuration spéciale pour autoriser le trafic réseau de QuizXpress. Pour ajouter une exception pour QuizXpress, autorisez tout le trafic du programme *qxserver.exe*, situé dans le dossier d'installation de QuizXpress. Cela n'est pas nécessaire avec le pare-feu Windows standard.
