# Mode de récupération de QuizXpress Live

Pour éviter de perdre des données ou de devoir redémarrer le quiz en cas de panne du système, QuizXpress Live dispose d'un mécanisme de récupération intégré. Après chaque question terminée, le système enregistre tout son état interne sur le disque dans un fichier d'instantané, y compris les scores, les données d'attribution des buzzers, la question en cours, etc.

Le fichier d'instantané est supprimé lorsque l'application se termine *normalement*. Si le système s'arrête *anormalement* pour une raison quelconque, le fichier reste en place et est détecté au prochain démarrage de QuizXpress Live. Une question vous est alors posée :

![](../assets/images/image473.webp){ width="395" loading=lazy }

Si vous répondez ‘Yes’, le système recharge l'instantané et vous pouvez reprendre là où vous vous étiez arrêté. Si vous répondez ‘No’, le système démarre normalement. Quoi qu'il arrive, vous n'avez donc pas à importuner votre public en rejouant une partie de votre quiz.

!!! note

    ce mode de récupération n'est pas actif lorsque vous lancez votre quiz depuis QuizXpress Studio en mode test. Lorsque vous présentez votre quiz à un vrai public, il est donc conseillé de le lancer en double-cliquant sur le fichier .qx, en démarrant Quiz Show.exe et en sélectionnant un fichier manuellement, ou en lançant le quiz avec ‘Run Production’ depuis QuizXpress Studio.
