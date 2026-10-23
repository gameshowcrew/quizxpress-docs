# Message Broker

Message Broker è un plugin avanzato di QuizXpress che scambia dati con applicazioni e dispositivi esterni, come i controller luci MIDI e DMX. Usarlo per creare effetti che rispondono a ciò che accade nel quiz, configurare sale quiz, controllare l'illuminazione, creare formati di gioco personalizzati o costruire moduli esterni propri in ambienti come [Cycling ‘74 Max](https://cycling74.com/).

Questa sezione descrive QuizXpress 8.5 e versioni successive.

!!! note
    Message Broker è un componente aggiuntivo con licenza per QuizXpress e richiede un acquisto una tantum.

## Canali dati

- **TCP/UDP:** comunicazione in ingresso e in uscita tramite messaggi di testo semplice (ASCII o UTF-8). Vedere [Canale IP in ingresso](ip-inbound.md) e [Canale IP in uscita](ip-outbound.md).
- **Telnet:** inviare comandi e ricevere dati direttamente da una console Telnet. Vedere [Canale IP in ingresso](ip-inbound.md).
- **OSC:** il canale in uscita può inviare anche messaggi [Open Sound Control](ip-outbound.md#impostazioni), per strumenti come Max, QLab e TouchOSC. Per inviare esattamente i messaggi attesi da una consolle luci o da un altro dispositivo, come un ETC Eos o Ion, usare [OSC Out](osc-out.md).
- **MIDI:** gli eventi di QuizXpress attivano messaggi MIDI configurabili, spesso usati per controllare mixer luci DMX. Vedere [MIDI e DMX](midi-and-dmx.md).

Questo schema mostra come è collegato tutto:

![Come Message Broker collega QuizXpress a dispositivi esterni](../../assets/images/mb-overview-diagram.webp){ loading=lazy }

## Aprire le impostazioni di Message Broker

Message Broker si configura da QuizXpress Director mentre un quiz è in esecuzione. Avviare un quiz, premere il tasto 'D' per aprire [QuizXpress Director](../../live/quizxpress-director/index.md) e passare alla scheda 'Extensions':

![La scheda Extensions in QuizXpress Director](../../assets/images/mb-director-extensions.webp){ loading=lazy }

!!! warning
    Chiudere le impostazioni di Message Broker con 'OK', non con 'Cancel'. 'Cancel' annulla tutte le modifiche.

## Registro messaggi

Il registro messaggi mostra tutto ciò che Message Broker fa mentre il quiz è in corso: i comandi in arrivo con il loro risultato, i messaggi in uscita tramite UDP, OSC e MIDI, e ciò che fanno i server (ascolto, connessioni, accessi e mittenti rifiutati). Usarlo per configurare e provare una connessione, o per capire perché un'applicazione esterna non risponde come previsto.

Aprirlo con 'Message log...' in fondo alle impostazioni di Message Broker. Per aprirlo automaticamente ogni volta che si avvia un quiz, selezionare 'Open the message log at start' nella scheda 'IP Inbound'.

![Il registro messaggi](../../assets/images/mb-message-log.webp){ loading=lazy }

- L'icona all'inizio di ogni riga indica di che cosa si tratta: una freccia blu verso il basso per un comando in ingresso, una freccia verde verso l'alto per un messaggio in uscita, e un segno di informazione, avviso o errore per tutto il resto.
- I comandi in ingresso mostrano il risultato sulla destra: 'OK' con la risposta, oppure 'ERR' con il motivo per cui il comando non è riuscito.
- Digitare nella casella del filtro per mostrare solo le righe che contengono quel testo, ad esempio un comando, un messaggio o un indirizzo IP.
- 'Incoming' e 'Outgoing' mostrano o nascondono comandi e messaggi. 'Timer ticks' mostra i tick del conto alla rovescia e gli heartbeat, che vengono inviati ogni secondo e sono nascosti per impostazione predefinita.
- 'Pause' impedisce la comparsa di nuove righe in modo da poter leggere l'elenco; conta le nuove righe, che compaiono quando si fa di nuovo clic su 'Pause'.
- Fare clic su una riga per vedere il testo completo e la risposta sotto l'elenco. 'Copy' copia le righe visibili, ad esempio per inviarle all'assistenza. 'Clear' svuota il registro.

Il registro conserva le ultime 5000 righe. Le password non vi compaiono mai: vengono mostrate come `****`.

!!! note
    Il registro messaggi si apre sullo schermo di QuizXpress Director. Quando si apre all'inizio di un quiz, prima che venga mostrato Director, si apre su uno schermo senza il quiz, così è possibile tenerlo aperto durante uno show dal vivo. Con un solo schermo, si apre sopra il quiz.
