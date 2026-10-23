# La scheda Mobile

La scheda Mobile mostra tutti i dispositivi mobili attualmente connessi.

![](../../assets/images/image455.webp){ loading=lazy }

Da qui è possibile:

- Select Jingle: forzare la **selezione del jingle** per tutti i giocatori che usano l’app Smart Buzzer

- **Send Message:** inviare un messaggio al giocatore o ai giocatori selezionati

- **Blacklist Player: bloccare definitivamente il giocatore selezionato in modo che non possa più rientrare nel quiz**

- **Latency Test: verificare la qualità della connessione di tutti i dispositivi**

- **Pair with Host Remote: mostrare il codice QR da scansionare con l’app Director (telecomando mobile del conduttore del quiz) per aggiungere questo computer all’elenco dei computer controllabili.**

- Settings: aprire la finestra di dialogo delle impostazioni mobili

- Chat: aprire una sessione di chat per chattare con tutti i giocatori

- Sulla destra è visibile il PIN corrente (quando si opera in modalità server)

## Test di latenza

Il test di latenza viene usato soprattutto in modalità Wi-Fi locale, per verificare che tutti i giocatori abbiano una connessione solida al router. Invia un ping a tutti i dispositivi e misura il tempo necessario per ricevere una risposta. Il tempo viene tracciato dietro ciascun dispositivo mobile in un grafico come questo:

![](../../assets/images/image456.webp){ loading=lazy }

Quando un dispositivo è molto lento o disconnesso, il grafico diventa rosso e il conduttore del quiz può invitare il giocatore ad avvicinarsi al punto di accesso. Nota: non lasciare il test di latenza in esecuzione durante il quiz, perché il test utilizza banda Wi-Fi e capacità del server.

## Chat istantanea

È possibile avviare una sessione di chat con i giocatori facendo clic sul pulsante Chat.

![](../../assets/images/image457.webp){ width="171" loading=lazy }  
Dopo aver avviato la chat, i giocatori vedono un pulsante della chat sul proprio telefono.

![](../../assets/images/image458.webp){ width="163" loading=lazy } ![](../../assets/images/image459.webp){ width="166" loading=lazy }

Premendo il pulsante della chat, i giocatori possono inviare messaggi al conduttore del quiz, che sono visibili in una scheda denominata ‘Chat’. Il conduttore del quiz vede tutti i messaggi per utente e può rispondere a ciascun giocatore singolarmente.

![](../../assets/images/image460.webp){ width="416" loading=lazy }

!!! note

    attualmente questa funzione è disponibile solo per i giocatori che usano il buzzer web buzzerpad. Non è ancora disponibile nell’app Smart Buzzer.*

## Impostazioni

Alcune impostazioni avanzate si trovano sotto il pulsante *Settings*:

![](../../assets/images/image461.webp){ width="332" loading=lazy }

Le caselle di controllo in alto controllano messaggi di conferma facoltativi inviati ai dispositivi connessi. Questi messaggi aiutano gli utenti a capire cosa sta succedendo. La prima opzione restituisce al dispositivo ogni risposta ricevuta, con un messaggio del tipo ‘We received answer D’. La seconda opzione invia un avviso solo quando non è stata ricevuta alcuna risposta oppure la risposta non è stata elaborata in tempo (ad esempio a causa della latenza del flusso video). La terza opzione invia al dispositivo, dopo ogni domanda, un messaggio con i punti vinti/persi, e l’ultima opzione consente di controllare se il dispositivo mostra che il giocatore ha risposto correttamente o in modo errato.

Con l’impostazione ‘Game PIN indicator’ è possibile configurare un indicatore del PIN da mostrare in quattro posizioni diverse della schermata del quiz durante il quiz. Questa impostazione non si applica in modalità Wi-Fi, poiché in tale modalità non viene usato alcun PIN. L’indicatore del PIN appare così:

![](../../assets/images/image462.webp){ width="310" loading=lazy }

Sono presenti anche alcune impostazioni per controllare il keypad mobile, ad esempio se debba riprodurre suoni e, per il sito web buzzerpad, un’opzione per impostarlo sul comportamento da keypad semplice, ovvero con la visualizzazione di un keypad a soli 7 pulsanti (modalità legacy). Qui è anche possibile indicare se mostrare le immagini anche sui telefoni cellulari.

La sezione QR code display consente di indicare se mostrare un codice QR che rimanda al buzzer web, come indicato in QuizXpress Setup, oppure un link all’app Smart Buzzer negli store di app iOS e Android. Se si mostra l’URL del buzzer web, è possibile specificare parametri aggiuntivi nel campo URL Extension, utili per personalizzare l’aspetto del keypad web. Per maggiori informazioni, consultare [Personalizzare il sito web buzzerpad](../using-mobile-keypads/branding-the-buzzerpad-website.md).

Il cursore Server delay può essere usato per ritardare tutte le azioni inviate ai dispositivi mobili, per ottenere una migliore sincronizzazione con il flusso di trasmissione. Mantenere questo valore a 0 quando non si trasmette in streaming. Ad esempio, se la latenza del flusso YouTube è di circa 3 secondi, è possibile impostare il ritardo a 3 secondi. In questo modo, quando il conto alla rovescia parte nel flusso YouTube dei giocatori, parte anche sul loro dispositivo. Senza il ritardo, il conto alla rovescia sul dispositivo partirebbe 3 secondi prima del timer su YouTube, il che può creare confusione.

Quando l’opzione ‘Extend answer time’ è selezionata, il sistema continua ad accettare i voti anche dopo la scadenza del conto alla rovescia, per il tempo impostato nel cursore ‘Server delay’. Ciò può servire a compensare la latenza dello streaming. Ad esempio, se il flusso ha un ritardo di 5 secondi, i giocatori all’altro capo del flusso vedono ancora scorrere l’orologio per 5 secondi dopo che si è già fermato in studio. Quindi, con questa opzione attiva, il sistema accetta ancora i voti in questi ultimi 5 secondi, evitando che i giocatori perdano una domanda.

**Change mobile device range on the fly**

Si immagini di aver avviato un quiz online in cui si attendono fino a 20 giocatori (intervallo di dispositivi “1-20”) e che, 10 minuti dopo l’inizio dell’introduzione, altri 15 giocatori vogliano unirsi. In precedenza sarebbe stato necessario riavviare il quiz e far registrare di nuovo tutti con il nuovo PIN, ecc. Per evitarlo, ora è possibile aggiornare l’intervallo dei dispositivi mobili mentre il quiz è in corso.

A tal fine, aprire Director nel lettore del quiz, andare alla scheda Mobile e fare clic sul pulsante Settings. Quindi fare clic sul pulsante Change device range e immettere il nuovo intervallo:

![](../../assets/images/image463.webp){ loading=lazy }

Il sistema verificherà la validità dell’intervallo e chiederà conferma. Dopo l’approvazione, il server verrà aggiornato. Si noti che, riducendo l’intervallo — ad esempio passando da “1-50” a “1-20” — i giocatori connessi che rientrano al di fuori del nuovo intervallo verranno disconnessi.
