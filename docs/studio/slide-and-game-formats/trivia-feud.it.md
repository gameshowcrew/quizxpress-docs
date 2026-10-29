# Trivia Feud

Impostare il tipo di diapositiva su ‘Trivia Feud’ per creare un gioco basato su un sondaggio. Dopo aver impostato il tipo di diapositiva su Trivia Feud, si apre l’editor del sondaggio (Survey editor), in cui è possibile inserire la domanda del sondaggio e le risposte del sondaggio con le relative percentuali:

![](../../assets/images/image76.webp){ width="578" loading=lazy }

Oltre a inserire i dettagli e le risposte del sondaggio, è possibile impostare il gioco su tre diverse modalità: Manual, Interactive o Multiplayer. Maggiori informazioni sono riportate di seguito.

È possibile utilizzare la funzionalità di intelligenza artificiale di QuizXpress per generare i sondaggi. Dopo aver inserito una domanda del sondaggio, premere il pulsante ‘Complete with AI’ per compilare automaticamente le risposte del sondaggio e le relative percentuali. Per ulteriori informazioni, fare riferimento a [Mini games](../mini-games/index.md).

Dopo aver inserito i dettagli e premuto OK, l’anteprima in QuizXpress Studio appare come segue. Lo sfondo dello schermo può essere modificato (ad esempio per includere il nome della propria azienda o il proprio marchio).

![](../../assets/images/image77.webp){ width="615" loading=lazy }

Facendo clic sul sondaggio, nella barra multifunzione viene mostrata la scheda TRIVIA FEUD. Qui è possibile cambiare la modalità di gioco e aprire il Survey Editor facendo clic su ‘Edit Survey’.

![](../../assets/images/image78.webp){ width="592" loading=lazy }

Nella barra degli strumenti e nella finestra delle proprietà avanzate sono disponibili varie opzioni, che verranno spiegate più avanti nel contesto delle diverse modalità disponibili.

Dopo l’avvio dello show, QuizXpress Live mostra il tabellone Trivia Feud con la domanda del sondaggio e le risposte del sondaggio nascoste. Il tabellone qui sotto è un esempio di gioco Feud in modalità Manual.

![](../../assets/images/image79.webp){ width="591" loading=lazy }

Trivia Feud prevede tre modalità di gioco: **Manual**, **Interactive** (Dito più Veloce) e **Multiplayer**.

## Modalità Manual

In modalità manuale, il gioco è controllato interamente da una schermata di QuizXpress Director, il pannello di controllo del Quizmaster, che viene eseguito sullo schermo del portatile mentre lo show è proiettato su un grande schermo.

![](../../assets/images/image80.webp){ loading=lazy }

Le risposte al sondaggio date dai giocatori possono essere rivelate manualmente premendo i pulsanti corrispondenti in Director. I punti accumulati sono mostrati in alto e i punteggi sono mostrati per entrambe le squadre.

Lo si può anche usare per giocare esattamente il formato dello show televisivo, seguendo questi passaggi:

- Iniziare con un Faceoff tra le due squadre premendo il pulsante ‘Start Faceoff’:

- I giocatori usano il proprio buzzer (che può essere una pulsantiera, un buzzer o un telefono cellulare) per prenotarsi. Il giocatore più veloce a prenotarsi viene mostrato sullo schermo.

- Il giocatore che si è prenotato per primo dà una risposta al sondaggio.

- Il Quizmaster rivela la risposta (se è presente sul tabellone) premendo il pulsante corrispondente in QuizXpress Director. I punti della risposta vengono aggiunti ai punti della tabella punteggi superiore, che mostra i punti che può vincere il giocatore vincitore.

- Premere il pulsante ‘Switch team’.

- Anche l’altro giocatore dà ora una risposta al sondaggio, che il Quizmaster rivela sul tabellone se presente.

- A seconda di quale squadra ha dato la risposta di rango più alto, rendere questa squadra la ‘squadra che gioca’ (quindi mantenere la squadra attualmente selezionata oppure premere di nuovo ‘switch team’).

- I membri della squadra che gioca (o il singolo, nel caso di una sfida testa a testa tra due persone) cercano di citare quante più risposte possibile.

  - Se una risposta è presente, fare clic sulla risposta corrispondente per rivelarla sul tabellone e aggiungere i punti al totale dei punti da vincere, mostrato in alto sul tabellone.

> ![](../../assets/images/image81.webp){ width="317" loading=lazy }

- Se una risposta non è presente, fare clic sul pulsante ‘Incorrect’ per mostrare sullo schermo una croce che indica che la risposta era errata. L’impostazione ‘max wrong answers’ del tabellone, indicata in QuizXpress Studio per la diapositiva, determina dopo quante croci il turno passa alla squadra avversaria:

> ![](../../assets/images/image82.webp){ width="316" loading=lazy }

- Come nello show televisivo ufficiale, la squadra avversaria ha ora la possibilità di indovinare una delle risposte rimanenti. La risposta data è:

  - visibile sul tabellone: fare clic sulla risposta corrispondente in Director per rivelarla. Quindi fare clic sul pulsante ‘Playing team wins’ per assegnare i punti alla squadra:

> ![](../../assets/images/image83.webp){ width="358" loading=lazy }

- non presente sul tabellone: fare clic sul pulsante ‘Incorrect’ per mostrare la croce rossa. Quindi fare clic su ‘switch team’ per tornare alla squadra che giocava inizialmente e poi sul pulsante ‘Playing team wins’ per assegnare i punti alla squadra.

- Infine, è possibile rivelare manualmente le risposte rimanenti ai giocatori e al pubblico.

La descrizione qui sopra mostra come giocare nello stesso modo del formato televisivo originale. Poiché l’impostazione manuale offre il pieno controllo, è possibile anche ideare modi alternativi di giocare.

Se si dispone di un altro modo per stabilire quale squadra inizierà la partita, è possibile selezionare manualmente una squadra premendo il messaggio ‘team playing’:

![](../../assets/images/image84.webp){ width="596" loading=lazy }

Verrà mostrata una finestra di selezione in cui è possibile scegliere la squadra che inizia.

![](../../assets/images/image85.webp){ width="170" loading=lazy }

Se giocano più di 2 giocatori/squadre, è possibile scegliere quali squadre si sfidano facendo clic sui pulsanti ‘select left team’ e ‘select right team’.

![](../../assets/images/image86.webp){ width="271" loading=lazy }

![](../../assets/images/image87.webp){ width="317" loading=lazy }

Il pannello di controllo in QuizXpress Director contiene anche un ‘points multiplier’. Scegliendo un valore di 2 o 3, i giocatori ricevono rispettivamente 2 o 3 volte più punti. Lo si potrebbe applicare, ad esempio, a un round finale in cui una squadra deve superare un certo numero di punti per vincere.

## Modalità Interactive (Dito più Veloce)

In questa modalità tutti i giocatori partecipano e possono prenotarsi per dare la propria risposta.

Il giocatore più veloce a prenotarsi viene mostrato sul grande schermo con il punteggio attuale e ha la possibilità di rispondere al sondaggio.

![](../../assets/images/image88.webp){ width="255" loading=lazy }

I giocatori hanno un tempo limitato per fornire una risposta. Questo è indicato da un conto alla rovescia in alto. Il tempo può essere configurato nella proprietà Answer Time (disponibile nella griglia delle proprietà). Se un giocatore non risponde entro il tempo previsto, compaiono tre croci e al giocatore vengono sottratti dei punti di penalità.

![](../../assets/images/image89.webp){ loading=lazy }

Se la risposta data è presente sul tabellone, il Quizmaster la rivela facendo clic sul pulsante corrispondente in QuizXpress Director. I punti vengono mostrati in alto e poi aggiunti al totale del giocatore.

![](../../assets/images/image90.webp){ width="223" loading=lazy } ![](../../assets/images/image91.webp){ width="227" loading=lazy }

Se la risposta data non è presente, fare clic sulla croce in Director, che viene quindi mostrata sul grande schermo. In questo caso verranno sottratti i punti indicati per ‘wrong answer’ nella scheda QUESTION.

![](../../assets/images/image92.webp){ width="568" loading=lazy }

Quando si crea la diapositiva Trivia Feud in modalità Dito più Veloce, è possibile indicare quante risposte può dare un giocatore dopo essersi prenotato (max correct answers), quante risposte errate possono essere date prima che il turno del giocatore termini (max incorrect answers) e se un giocatore viene escluso dal tabellone corrente o può prenotarsi di nuovo (Exclude o Continue).

![](../../assets/images/image93.webp){ width="605" loading=lazy }

Le impostazioni qui sopra possono essere modificate anche nel pannello delle proprietà avanzate, che si può mostrare facendo clic sulla scheda VIEW e spuntando ‘Properties’. In questo pannello sono visibili tutte le impostazioni che si applicano al Trivia Feud una volta selezionato.

L’opzione auto reveal indica se le risposte rimanenti che non sono state citate verranno mostrate automaticamente quando tutti i giocatori sono fuori gioco, oppure se il Quizmaster le rivelerà manualmente una per una facendo clic sulle risposte in QuizXpress Director.

## Modalità Multiplayer

Quando il tabellone è in modalità multiplayer, tutto il pubblico può partecipare.

![](../../assets/images/image94.webp){ width="321" loading=lazy }

Un conto alla rovescia è mostrato in alto sul tabellone Trivia Feud. In QuizXpress Studio, nella scheda QUESTION, il ‘Answer time’ può essere configurato nello stesso modo di una normale domanda.

I giocatori inviano le proprie risposte tramite il telefono cellulare mentre il conto alla rovescia è in corso, inserendo e inviando più testi.

![](../../assets/images/image95.webp){ width="385" loading=lazy }

Nella finestra delle proprietà di Studio (se non è visibile, mostrarla facendo clic sulla scheda VIEW e poi spuntando Properties) sono visibili le seguenti opzioni che si applicano alla modalità multiplayer:

**Response limit**: specifica il numero massimo di risposte che un giocatore può inviare.

**Tolerance**: specifica la tolleranza utilizzata da QuizXpress per giudicare le risposte date. Una tolleranza più alta ammette più errori di ortografia.

**Auto reveal**: indica se, al termine del conto alla rovescia, le risposte verranno mostrate automaticamente oppure se il Quizmaster le rivelerà manualmente una per una facendo clic sulle risposte in QuizXpress Director.

In questa modalità è possibile specificare più risposte corrette, separate da un punto e virgola:

![](../../assets/images/image96.webp){ width="430" loading=lazy }

L’input dei giocatori viene confrontato con ciascuna voce utilizzando la tolleranza impostata.
