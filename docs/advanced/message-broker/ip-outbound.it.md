# Canale IP in uscita

Con il canale in uscita, QuizXpress invia un messaggio ogni volta che nel quiz accade qualcosa, come un cambio di diapositiva, la pressione di un buzzer o una variazione di punteggio. La propria applicazione ascolta questi messaggi e risponde, ad esempio pilotando una tabella punteggi esterna o uno spettacolo di luci.

Attivarlo nella scheda 'IP Outbound' delle [impostazioni di Message Broker](index.md#aprire-le-impostazioni-di-message-broker):

![La scheda IP Outbound](../../assets/images/mb-ip-outbound-tab.webp){ width="420" loading=lazy }

## Impostazioni

**On/Off**
:   Attiva o disattiva il canale in uscita.

**Test**
:   Apre un modulo di prova in cui è possibile attivare gli eventi a mano:

    ![Modulo di prova del canale in uscita](../../assets/images/mb-outbound-test-form.webp){ width="560" loading=lazy }

**Send a heartbeat message every second**
:   Invia un messaggio heartbeat ogni secondo, in modo che il lato ricevente possa capire che il lettore del quiz è ancora in esecuzione. Usarlo per rilevare una connessione caduta inaspettatamente; una sessione normale inizia sempre con `/start` e termina con `/close`.

**Send input from keypads/buzzers**
:   Inoltra ogni pressione di pulsantiera e buzzer. È facoltativo perché può produrre molti messaggi.

**Send score changes**
:   Invia un messaggio ogni volta che cambia il punteggio di un giocatore, ad esempio per pilotare tabelle punteggi esterne.

**Send countdown tick**
:   Invia il tempo rimanente ogni secondo mentre il conto alla rovescia è in corso.

**Number slides from 1 (also MIDI triggers)**
:   I numeri delle diapositive in `/slidechanged`, `/slideinfo` e nel trigger MIDI 'Slide Changed' iniziano da 1, come in Studio e nei comandi in ingresso `goto` e `getslide`. Quando è disattivata, iniziano da 0, come nelle versioni precedenti; lasciarla disattivata se l'applicazione o la configurazione MIDI conta già a partire da 0.

**Send slide details (/slideinfo)**
:   Invia la domanda, le risposte e la risposta corretta di ogni nuova diapositiva. Vedere [Dettagli della diapositiva e classifica](#dettagli-della-diapositiva-e-classifica).

**Send the leaderboard (/leaderboard)**
:   Invia tutte le squadre in ordine di classifica dopo le variazioni di punteggio. Vedere [Dettagli della diapositiva e classifica](#dettagli-della-diapositiva-e-classifica).

**Send text answers as /textvote**
:   Le risposte testuali dalle pulsantiere (numeri, lettere, testo libero) vengono inviate come `/textvote` invece di `/buzz`, in modo che l'applicazione possa distinguerle dalla pressione dei pulsanti. Quando è disattivata, entrambe vengono inviate come `/buzz`, come nelle versioni precedenti. Richiede 'Send input from keypads/buzzers'.

**Protocol**
:   - **UDP/ASCII:** testo ASCII semplice, parametri separati da spazi.
    - **UDP/UTF8:** lo stesso, codificato in UTF-8. Sceglierlo quando i nomi delle squadre o le risposte contengono caratteri accentati.
    - **UDP/OSC:** messaggi in formato [Open Sound Control (OSC)](https://en.wikipedia.org/wiki/Open_Sound_Control), che [Max](https://cycling74.com/), QLab, TouchOSC e strumenti simili possono elaborare direttamente. I numeri vengono inviati come interi a 32 bit e il testo come stringhe UTF-8.

**Server address**
:   L'indirizzo IP del computer che riceve i messaggi. Usare `127.0.0.1` se è lo stesso computer.

**Server port**
:   Il numero di porta su cui è in ascolto l'applicazione ricevente.

!!! tip
    Il [registro messaggi](index.md#registro-messaggi) mostra ogni messaggio in uscita, così è possibile verificare che cosa dovrebbe ricevere l'applicazione.

!!! note
    Una consolle luci come una ETC Eos o Ion reagisce solo ai propri comandi, non a questi messaggi fissi. Usare [OSC Out](osc-out.md) per inviarle esattamente i messaggi che si aspetta.

## Messaggi

Il lato ricevente apre un socket UDP. I messaggi sono stringhe di testo semplice nel formato `/message {parameter1} {parameter2} …`. Ogni sessione inizia con `/start` e termina con `/close`.

| Messaggio | Significato |
|---|---|
| `/start` | Inizio della sessione. |
| `/close` | Fine della sessione: QuizXpress Live si sta chiudendo. |
| `/heartbeat {counter}` | Inviato ogni secondo con un contatore crescente, ad esempio `/heartbeat 2345`. |
| `/countdowntick {remainingtimeMs}` | Inviato ogni secondo mentre il conto alla rovescia è in corso, con il tempo rimanente in millisecondi, ad esempio `/countdowntick 23100`. |
| `/slidechanged {old#} {new#} {questiontype} {slide class} {slide id}` | Viene mostrata una nuova diapositiva. La classe e l'id sono facoltativi e si impostano nei metadati della diapositiva in Studio, così è possibile reagire a una classe o a un id invece che a un numero di diapositiva che cambia quando le diapositive vengono riordinate. Esempio: `/slidechanged 6 7 question MySpecialSlideType banner1`. Con 'Number slides from 1', `0` come vecchio numero significa che non c'era una diapositiva precedente. |
| `/command {command}` | Un comando dalla pulsantiera Master: `power`, `scores`, `chart`, `leaderboard`, `groupchart`, `up`, `down`, `pause`, `questionmark`, `next`, `wrong` o `right`. Esempio: `/command up`. |
| `/buzz {device} {key}` | La pressione di un tasto su un dispositivo, ad esempio `/buzz 10 A`, o `/buzz 8 RED` per il pulsante Dito più Veloce. Anche le risposte testuali vengono inviate come `/buzz`, a meno che 'Send text answers as /textvote' sia attivo. |
| `/textvote {device} {text}` | Una risposta testuale da un dispositivo, ad esempio `/textvote 8 Paris`. Solo con 'Send text answers as /textvote'. |
| `/fastestfinger {device}` | Il dispositivo che è stato il primo in una domanda Dito più Veloce. |
| `/screenchanged {screentype}` | Il lettore del quiz ha cambiato schermata: `welcomescreen`, `signonscreen`, `countdownscreen`, `quizscreen` o `finalscorescreen`. Esempio: `/screenchanged countdownscreen`. |
| `/timeout` | La domanda è scaduta senza una risposta corretta. |
| `/startcountdown` | Il conto alla rovescia della domanda è partito. |
| `/pausecountdown` | Il conto alla rovescia è in pausa; il sistema è inattivo. |
| `/endcountdown` | Il conto alla rovescia si è fermato; la domanda è terminata. |
| `/correct` | Una risposta alla domanda corrente è stata giudicata corretta. |
| `/incorrect` | Una risposta alla domanda corrente è stata giudicata errata. |
| `/answerrevealed` | La risposta corretta viene mostrata sulla diapositiva, ad esempio quando il tempo è scaduto in una domanda a votazione. Su una diapositiva Trivia Feud viene inviato per ogni risposta che viene girata sul tabellone. |
| `/restart` | Il quiz è stato riavviato dalla schermata dei punteggi finali. |
| `/scorechanged {device} {teamname} {old score} {new score}` | Il punteggio di una squadra è cambiato. Esempio: `/scorechanged 10 'John Trivialta' 5 10` significa che la squadra 'John Trivialta' sul dispositivo 10 è passata da 5 a 10 punti. In OSC il nome della squadra è una stringa senza le virgolette. |
| `/claimbingo` | Un giocatore ha dichiarato Bingo. |
| `/falsebingo` | Un Bingo dichiarato si è rivelato falso. |
| `/bingo` | Un Bingo dichiarato è valido. |
| `/slideinfo {json}` | I dettagli della nuova diapositiva, inviati subito dopo `/slidechanged`. Solo con 'Send slide details'. |
| `/leaderboard {json}` | Tutte le squadre in ordine di classifica. Solo con 'Send the leaderboard'. |

Esempio dei messaggi durante un quiz:

![Esempio di messaggi in uscita](../../assets/images/mb-outbound-example-messages.webp){ loading=lazy }

## Dettagli della diapositiva e classifica

`/slideinfo` e `/leaderboard` trasportano [JSON](https://www.json.org/) su una sola riga, che la maggior parte degli strumenti può leggere direttamente (Node-RED, Max con `dict.deserialize`, Bitfocus Companion, Python). In OSC il JSON è un argomento di tipo stringa. Con UDP/ASCII, i caratteri accentati sono scritti come codici `\u`, che qualsiasi lettore JSON riconverte nel carattere corretto.

`/slideinfo` viene inviato subito dopo `/slidechanged`, ad esempio:

```
/slideinfo {"number":44,"previous":45,"type":"question","question":"Which aircraft type has recently been added?","answers":["A340","A380","B787"],"correctAnswer":"C","category":"Default Category","answerTime":30,"points":10,"class":"","id":""}
```

| Campo | Significato |
|---|---|
| `number`, `previous` | Il numero della nuova diapositiva e di quella precedente, contati secondo l'impostazione 'Number slides from 1'. |
| `type` | Il tipo di diapositiva, lo stesso di `/slidechanged`. |
| `question`, `answers` | Il testo della domanda e le risposte, nell'ordine della diapositiva. |
| `correctAnswer` | La risposta corretta, ad esempio `C` per la terza risposta. |
| `category`, `answerTime`, `points` | La categoria, il tempo di risposta in secondi e i punti per una risposta corretta. |
| `class`, `id` | La classe e l'id della diapositiva dai metadati della diapositiva in Studio. |

!!! warning
    `/slideinfo` contiene la risposta corretta non appena la diapositiva compare. Non mostrarlo su uno schermo che i giocatori possono vedere prima che la risposta venga rivelata.

`/leaderboard` viene inviato dopo le variazioni di punteggio. Quando molti punteggi cambiano contemporaneamente, ad esempio alla fine di una domanda, si riceve una sola classifica dopo l'ultima modifica invece di una per squadra:

```
/leaderboard [{"rank":1,"device":2,"name":"Brainiacs","group":"","score":30},{"rank":2,"device":1,"name":"Zoë's Team","group":"","score":10},{"rank":2,"device":3,"name":"Quizzers","group":"","score":10}]
```

Le squadre con lo stesso punteggio condividono una posizione, e la posizione successiva viene saltata (1, 2, 2, 4). `group` è il gruppo demografico della squadra, se presente.

## Esempio: un semplice listener UDP

Questa applicazione console C# (.NET Framework 4.8) è in ascolto sulla porta 12345 e stampa ogni messaggio ricevuto. Impostare il 'Server port' in Message Broker sullo stesso numero.

```csharp
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class UDPServer
{
    static void Main(string[] args)
    {
        int port = 12345; // La porta su cui restare in ascolto
        UdpClient udpListener = new UdpClient(port);
        Console.WriteLine($"UDP server is listening on port {port}");

        try
        {
            while (true)
            {
                IPEndPoint senderEndPoint = new IPEndPoint(IPAddress.Any, port);
                byte[] receivedBytes = udpListener.Receive(ref senderEndPoint);
                string receivedText = Encoding.UTF8.GetString(receivedBytes);
                Console.WriteLine($"Received: {receivedText}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
        }
        finally
        {
            udpListener.Close();
        }
    }
}
```
