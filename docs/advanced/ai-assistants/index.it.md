# Assistenti IA

Quiz Studio può essere controllato da un assistente IA come [Claude](https://claude.ai). Si dice all'assistente quale quiz si desidera ("crea un round di quiz da pub sugli anni '90 con 10 domande a risposta multipla e un round di immagini"), ed esso apre, costruisce, modifica e salva il quiz nella finestra di Quiz Studio mentre si osserva. Tutto ciò che fa avviene nel Quiz Studio aperto, quindi è possibile esaminare il risultato, modificarlo personalmente e proseguire.

Questo è diverso dall'[AI Quiz Generator](../../studio/quizxpress-and-ai.md), una parte di Studio che genera domande per l'utente. Con un assistente IA si lavora in una conversazione, e l'assistente può fare quasi tutto ciò che si può fare in Studio: creare ogni tipo di diapositiva, modificare testi, risposte, punti, stili e sfondi, aggiungere minigiochi, controllare gli errori del quiz e salvarlo.

## Come funziona

La connessione usa uno standard chiamato MCP (Model Context Protocol), che consente agli assistenti IA di usare altri programmi. Quiz Studio include un piccolo server MCP:

- È **disattivato** finché non lo si attiva nelle Options, vedere [Collegare un assistente IA](connecting-an-ai-assistant.md).
- Accetta solo connessioni da **programmi sul proprio computer**. Nessuno in rete o su Internet può usarlo.
- Serve un assistente IA che supporti MCP, ad esempio Claude Code. L'assistente è un prodotto separato con un proprio abbonamento: non fa parte di QuizXpress e non utilizza i crediti IA di QuizXpress.

Finché un assistente è connesso, una barra sotto la barra multifunzione lo segnala.

## Da sapere

!!! warning "Le modifiche non possono essere annullate"
    Le modifiche dell'assistente non possono essere annullate con Undo, e Quiz Studio cancella la cronologia di annullamento dopo ciascuna di esse. Salvare il quiz con un altro nome prima di lasciare che un assistente apporti modifiche estese, in modo da poter sempre tornare indietro.

- L'assistente non apre, non crea e non chiude un quiz finché il quiz in Studio ha modifiche non salvate. Deve prima chiedere: salvare il quiz, oppure dirgli di scartare le modifiche.
- Finché in Studio è aperta una finestra di dialogo (ad esempio Options), l'assistente deve attendere. Chiudere la finestra e potrà continuare.
- Ogni volta che l'assistente aggiunge una diapositiva, Studio la mostra e scorre le miniature fino ad essa.
- Questo vale solo per Quiz Studio. Quiz Live, Director e Setup non possono essere controllati da un assistente.

## In questa sezione

- [Collegare un assistente IA](connecting-an-ai-assistant.md): attivarlo e collegare l'assistente.
- [Usare Claude Desktop](claude-desktop.md): configura l'app Claude per Windows, anche in Parallels su un Mac.
- [Cosa può fare un assistente](what-an-assistant-can-do.md): le possibilità, con esempi di richieste.
