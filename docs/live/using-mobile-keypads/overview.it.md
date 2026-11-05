# Panoramica

QuizXpress Mobile consente ai giocatori di utilizzare i dispositivi mobili come strumento di input. I giocatori possono partecipare a un quiz navigando sul nostro sito web buzzerpad (è necessaria la connessione a Internet) e inserendo il codice PIN visualizzato sullo schermo per connettersi.

QuizXpress Mobile offre anche un modo per giocare con i dispositivi mobili senza che sia disponibile una connessione a Internet. Con questa soluzione, i giocatori scaricano l'app QuizXpress Smart Buzzer, disponibile per iOS e Android. Al computer viene collegato un router Wi-Fi a cui tutti i giocatori si collegano con il proprio dispositivo. Dopo aver avviato un quiz, i giocatori possono connettersi attraverso l'app Smart Buzzer premendo il pulsante ‘Accedi con WiFi locale’. L'app Smart Buzzer supporta anche il gioco via Internet, inserendo un codice PIN.

Con questa aggiunta, QuizXpress ora supporta:

| **Scenario** | | **Connessione Internet** | **Router Wi-Fi** | **Dispositivi Mobili** | **App Smart Buzzer** |
|--------------|----------------------------------------------------------------|-----------------------|---------------------------|----------------------------|-----------------------------------------|
| 1 | Pulsantiere/Buzzer Hardware wireless RF | No | No | No | No |
| 2            | Dispositivi mobili su buzzerpad.com tramite browser web       | Sì                    | No                        | Sì                         | No                                      |
| 3 | Dispositivi Mobili con l'app Smart Buzzer su Wi-Fi locale | No | Sì | Sì | Sì |
| 4 | Dispositivi Mobili con l'app Smart Buzzer su buzzerpad.com tramite PIN | Sì | No | Sì | Sì |

Tutti gli scenari hanno differenti pro e contro e la soluzione preferibile dipende dalle specifiche esigenze.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 39%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Scenario</strong></th>
<th><strong>Vantaggi</strong></th>
<th><strong>Svantaggi</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1 Hardware RF wireless</strong></td>
<td><p>Nessuna dipendenza esterna da internet, Wi-Fi o dispositivi mobili.</p>
<p>Semplice da usare per i giocatori.</p></td>
<td>Nessuna capacità di input estesa (solo ABCDEF e Dito più Veloce). Logistica per fornire le pulsantiere ai giocatori e ritirarli al termine.</td>
</tr>
<tr class="even">
<td><strong>2 Browser su buzzerpad.com</strong></td>
<td>Non occorre chiedere ai giocatori di installare un'app. Per grandi gruppi di giocatori (fino a 2000).</td>
<td>È necessaria una connessione internet</td>
</tr>
<tr class="odd">
<td><strong>3 App Smart Buzzer su Wi-Fi locale</strong></td>
<td><p>Comunicazione veloce a bassa latenza.</p>
<p>Supporto della modalità headless (senza schermo centrale).</p>
<p>Supporto di tipi di input estesi.</p></td>
<td>Con un'infrastruttura di base (router Wi-Fi standard) sono supportati solo piccoli gruppi di circa 50 giocatori. Nota: se non è disponibile alcuna connessione internet o dati mobili, assicurarsi che i giocatori abbiano già scaricato l'app in anticipo</td>
</tr>
<tr class="even">
<td><strong>4 App Smart Buzzer con internet disponibile</strong></td>
<td><p>Supporto di grandi gruppi</p>
<p>Capacità di input estese</p>
<p>Nessuna configurazione Wi-Fi locale necessaria</p></td>
<td>È necessaria una connessione internet</td>
</tr>
</tbody>
</table>

La pulsantiera mobile (sia buzzerpad sia l’app Smart Buzzer) è dotata di alcune notevoli caratteristiche:

- Le domande sono presentate in modo completo sul dispositivo mobile, comprese le immagini e gli effetti.

- Vari tipi di domande specifici per l'uso di un telefono cellulare:

  - Domande Numeriche, per esempio per chiedere il risultato di una formula o un anno storico.

  - Domande Testuali (risposta singola o multipla)

  - Domande Lettera Iniziale (A-Z)

- Punti bonus personalizzabili per le prime 3 squadre più veloci a rispondere correttamente.

- Esperienza migliorata per le domande ordinate e le domande con più risposte corrette. I giocatori possono ordinare prima le risposte sul proprio dispositivo e poi inviare il risultato a QuizXpress in una sola volta.

- Funzionalità di controllo remoto tramite l'app Mobile QuizXpress Director disponibile per iOS e Android. Per ulteriori informazioni, consultare [QuizXpress Director App](using-the-mobile-apps.md#app-telecomando-mobile-director).

Oltre alle caratteristiche sopra descritte, l'app Smart Buzzer offre alcune funzioni aggiuntive:

- ‘Personalizza’ per personalizzare l'app mobile con immagine di benvenuto, immagine di sfondo e logo.

- Supporto della ‘Modalità Headless’ per presentare un quiz senza la necessità di uno schermo di proiezione.

- Jingle di squadra selezionabili dall'utente. Se è stato configurato l'uso dei jingle impostando la cartella Jingles nelle impostazioni (fare riferimento a [Configurare i suoni – la scheda Audio](../../setup/configuring-sounds-the-sounds-tab-page.md) ), ai giocatori verrà mostrato un elenco di tutti i frammenti sonori disponibili. Ogni giocatore può scegliere un jingle che verrà utilizzato durante la partita nelle situazioni seguenti:

<!-- -->

- Punti bonus – il suono del giocatore che per primo fornisce la risposta corretta viene riprodotto quando viene mostrata la schermata dei punti bonus.

- Dito più Veloce – viene riprodotto il file audio del giocatore che ha premuto per primo, insieme al suo nome che appare sullo schermo del quiz.

- Punteggi intermedi – il suono del giocatore al primo posto in classifica viene riprodotto quando si mostra la classifica.

Alcuni esempi di scenari supportati sono:

- Un DJ che presenta un quiz in un pub locale senza copertura dati. I visitatori scaricano l'app Smart Buzzer e si collegano a un router Wi-Fi locale per giocare. Il pub non ha un televisore o un monitor, quindi il Quizmaster utilizza la Modalità Headless. Il DJ ha personalizzato l'app utilizzando la Personalizzazione App di QuizXpress.

- Un’agenzia di eventi che presenta un quiz per un grande gruppo. L'azienda non vuole che il pubblico installi un'app, quindi utilizza il server buzzerpad e un codice PIN per far partecipare le persone. Il quiz viene presentato su un grande schermo che mostra video, suoni e immagini.

- Un’agenzia di eventi che trasmette un quiz in streaming su internet a migliaia di giocatori utilizzando un codice PIN in modalità server. La società ha venduto i biglietti ai giocatori anticipatamente. I biglietti vengono convalidati quando il giocatore si connette alla partita e inserisce il proprio codice nel popup che appare.
