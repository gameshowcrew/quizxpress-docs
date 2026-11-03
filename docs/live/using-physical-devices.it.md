# Usare i dispositivi fisici

Un sistema QuizXpress completo con hardware può presentarsi come segue:

![](../assets/images/image349.webp){ width="514" loading=lazy }

In questa configurazione vengono utilizzati tutti gli elementi hardware supportati da QuizXpress: pulsantiere/buzzer, braccialetti Galaxy e tabelle punteggi. Come si può vedere, per ogni tipo di dispositivo viene utilizzato un ricevitore separato.

Prima di descrivere il software in dettaglio, vediamo innanzitutto i tipi di buzzer supportati e come usarli.

## Usare le pulsantiere, i buzzer e le colonnine buzzer QuizXpress { #usare-i-keypad-i-buzzer-e-le-colonnine-buzzer-quizxpress }

Entrambi i tipi di pulsantiere QuizXpress, la pulsantiera Basic e la pulsantiera Plus, hanno sei pulsanti e un pulsante Dito più Veloce. Quando viene presentata una domanda, premendo uno dei pulsanti si accende la spia rossa di trasmissione in alto a destra sulla pulsantiera, a indicare che sta inviando la propria scelta al ricevitore wireless collegato al computer su cui è in esecuzione QuizXpress Live. Finché la spia rossa della pulsantiera continua ad accendersi, la pulsantiera sta tentando di inviare la scelta al ricevitore. Quando la spia verde in alto a sinistra lampeggia, il segnale è stato elaborato correttamente. Se la trasmissione non è riuscita, il LED rosso lampeggia alcune volte.

Le pulsantiere QuizXpress sono abbinate a un singolo ricevitore e ogni ricevitore ha un numero di serie univoco (quindi, per ordinare un ricevitore di riserva, assicurarsi di indicare il numero di serie). QuizXpress include un comodo strumento per *abbinare* una pulsantiera al ricevitore collegato e assegnarle un numero. Lo strumento *QuizXpress Device Programmer* si trova nella voce QuizXpress del menu Start di Windows, oppure nel menu *Tools* di QuizXpress Studio.

| ![](../assets/images/image350.webp){ width="287" loading=lazy } | ![](../assets/images/image351.webp){ width="288" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

Per iniziare a programmare una pulsantiera o un buzzer QuizXpress, collegare il ricevitore al computer e scegliere il tipo di ricevitore nell'elenco a discesa dei ricevitori. Inserire l'intervallo di pulsantiere da programmare e premere Connect. Dovrebbe comparire un segno di spunta verde a indicare che la connessione al ricevitore è riuscita.

Lo strumento di programmazione consente di programmare il numero (id) di una singola pulsantiera, oppure in modo semiautomatico di un intero set di pulsantiere (è comunque necessario premere i pulsanti «mano» e «B» su ciascuna pulsantiera). Per programmare una singola pulsantiera, impostare il numero richiesto nel campo «Keypad to set», fare clic su «Set» e, entro 4 secondi, premere entrambi i pulsanti «mano» e «B» sulla pulsantiera (vedere l'immagine a destra).

Le pulsantiere hanno un'associazione univoca con il ricevitore e devono prima essere abbinate a esso. Quando si imposta l'id di una pulsantiera, questa viene anche immediatamente abbinata al ricevitore collegato. Per abbinare la pulsantiera Master, premere il pulsante «Set» sullo strumento di programmazione e premere contemporaneamente i pulsanti Power e Up sulla pulsantiera Master.

Per programmare i buzzer QuizXpress, fare clic sul pulsante «Set Buzzer» dello strumento di programmazione. La spia gialla sul ricevitore si accende. A questo punto premere insieme il pulsante B e il pulsante grande. Tenere premuto il pulsante grande finché non lampeggia. Quando lampeggia, attendere che la spia gialla si spenga, quindi premere il buzzer. Il numero del buzzer apparirà ora nello strumento di programmazione.

Per programmare i buzzer QuizXpress Galaxy RGB, seguire gli stessi passaggi descritti sopra per i buzzer, ma invece di premere B e il pulsante grande, premere C e il pulsante grande finché il buzzer non lampeggia.

Anche le colonnine buzzer Sparkle e il tavolo buzzer Luminous possono essere programmati. Utilizzano lo stesso ricevitore dei buzzer QuizXpress.

Per programmare le colonnine buzzer Sparkle:

- Spegnere il buzzer.

- Premere il pulsante «Set Buzzer» nel QuizXpress Device Programmer.

- Premere ora il pulsante del buzzer sullo Sparkle e riaccendere lo Sparkle.

- Lo Sparkle lampeggerà, a indicare che è stato programmato con l'ID indicato nell'applicazione di programmazione.

Per programmare i tavoli da quiz Luminous:

- ![](../assets/images/image352.webp){ width="106" loading=lazy }Spegnere il Luminous.

- Premere il pulsante «Set Buzzer» nel QuizXpress Device Programmer.

- Premere ora il piccolo pulsante nero accanto al pulsante On/Off del Luminous e riaccendere il Luminous.

- Il Luminous lampeggerà, a indicare che è stato programmato con l'ID indicato nello strumento di programmazione.

## Usare le pulsantiere Fleetwood Reply Systems { #usare-i-keypad-fleetwood-reply-systems }

| ![](../assets/images/image353.webp){ width="193" loading=lazy } | Le pulsantiere Fleetwood Reply Mini hanno cinque pulsanti. Quando viene mostrata una domanda, premendo uno dei pulsanti si accende la spia di trasmissione nella parte superiore della pulsantiera, a indicare che sta inviando la propria scelta al ricevitore wireless collegato al computer su cui è in esecuzione Quiz Show. Quando la spia sulla pulsantiera diventa rossa, significa che la risposta non è stata ricevuta dal ricevitore wireless e il partecipante deve provare a inviare di nuovo la risposta. Quando la spia diventa verde, il segnale è stato elaborato correttamente. |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Usare i buzzer Sony

I buzzer Sony BuzzTM sono disponibili in due versioni: cablata e wireless. Hanno quattro pulsanti colorati, che rappresentano le risposte a scelta multipla A (blu), B (arancione), C (verde) e D (giallo), e un grande pulsante rosso. Il pulsante rosso può illuminarsi.

In Quiz Show, le risposte a scelta multipla hanno lo stesso colore dei quattro pulsanti colorati a scelta multipla del buzzer.

| ![](../assets/images/image354.webp){ width="65" loading=lazy } | Non appena una domanda viene mostrata in QuizXpress Live, i pulsanti rossi di tutti i buzzer (tranne quelli dei giocatori già eliminati dal gioco) si accendono, a indicare che i buzzer sono in attesa di un input. |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Quando una domanda è a scelta multipla (Dito più Veloce o votazione; vedere [Condurre lo show con QuizXpress Live](index.md)), un giocatore deve premere uno dei pulsanti a scelta multipla per rispondere. Quando una domanda è «aperta» (il che implica che è sempre Dito più Veloce), per rispondere occorre premere il pulsante rosso.

Quando una domanda è «Dito più Veloce» e un giocatore è il più veloce a premere, la spia rossa inizia a lampeggiare. Se la domanda era una «domanda aperta», il giocatore comunica la risposta al Quizmaster, che la giudica. Se la domanda era a scelta multipla, il giocatore ha già dato la risposta premendo uno dei quattro pulsanti a scelta multipla; in questo caso Quiz Show giudica automaticamente la risposta e aggiunge o sottrae punti.

Se la risposta era sbagliata, il conto alla rovescia continua. Il giocatore che ha risposto in modo errato non può più partecipare alla risposta alla domanda corrente, quindi il suo buzzer non si accenderà fino alla visualizzazione della domanda successiva.
