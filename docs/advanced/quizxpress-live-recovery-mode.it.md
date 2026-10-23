# Modalità di ripristino di QuizXpress Live

Per evitare la perdita di dati o di dover riavviare il quiz in caso di guasto del sistema, QuizXpress Live dispone di un meccanismo di ripristino integrato. Dopo ogni domanda completata, il sistema salva su disco l'intero stato interno in un file di snapshot, inclusi punteggi, dati di assegnazione dei buzzer, domanda corrente e così via.

Il file di snapshot viene rimosso se l'applicazione termina *normalmente*. Se il sistema termina *in modo anomalo* per qualsiasi motivo, il file rimane e viene rilevato al successivo avvio di QuizXpress Live. Verrà quindi posta una domanda:

![](../assets/images/image473.webp){ width="395" loading=lazy }

Rispondendo ‘Yes’, il sistema ricarica lo snapshot ed è possibile riprendere da dove ci si era interrotti. Rispondendo ‘No’, il sistema si avvia normalmente. Qualunque cosa accada, quindi, non occorre disturbare il pubblico rigiocando una parte del quiz.

!!! note

    questa modalità di ripristino non è attiva quando si avvia il quiz da QuizXpress Studio in modalità test. Quando si presenta il quiz a un pubblico reale, si consiglia quindi di avviarlo facendo doppio clic sul file .qx, avviando Quiz Show.exe e selezionando manualmente un file, oppure avviando il quiz con ‘Run Production’ da QuizXpress Studio.
