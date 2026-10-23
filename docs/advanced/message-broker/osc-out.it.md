# OSC Out

Con OSC Out si decide quale messaggio OSC QuizXpress invia quando succede qualcosa nel quiz. Utilizzarlo per i dispositivi che reagiscono solo ai propri comandi, come una console luci ETC Eos o Ion: una risposta corretta può attivare il cue 20, il dito più veloce sul keypad 3 può attivare una macro, e ogni nuova diapositiva può attivare il cue con lo stesso numero.

Il [canale in uscita IP](ip-outbound.md) invia sempre gli stessi messaggi fissi, come `/correct` e `/buzz 3 A`. Va bene per il proprio software, ma una console luci ignora i messaggi che non conosce. OSC Out invia esattamente i messaggi che la console si aspetta, ed è possibile usare entrambi allo stesso tempo.

## Preparare una console ETC Eos o Ion

Una console della famiglia Eos (Eos, Gio, Ion, Element, ETCnomad) accetta solo messaggi OSC che iniziano con `/eos/`. Prima che QuizXpress possa controllarla:

1. Nelle impostazioni di rete della console, selezionare 'UDP Strings & OSC' per la porta di rete che collega la console al computer QuizXpress.
2. In Setup, sotto 'Show Control', attivare 'OSC RX' e 'String RX', e impostare il 'OSC RX Port'. ETC raccomanda la porta 8000.
3. Annotare l'indirizzo IP della console. Inviare alla console principale, non a una di backup o a un client.

I nomi di queste impostazioni differiscono leggermente tra le versioni del software Eos; il manuale ETC della propria versione riporta i dettagli.

## Attivare OSC Out

Aprire le [impostazioni del Message Broker](index.md#aprire-le-impostazioni-di-message-broker) e passare alla scheda 'OSC Out':

![La scheda OSC Out](../../assets/images/mb-osc-out-tab.webp){ width="420" loading=lazy }

**Mode**
:   Attiva o disattiva OSC Out.

**Send to**
:   L'indirizzo IP e la porta di ricezione OSC della console; per una console ETC, il 'OSC RX Port' delle sue impostazioni Show Control.

**Rules**
:   Ogni regola indica a QuizXpress quali messaggi inviare per un evento. 'Add...' crea una regola e 'Edit...' (o un doppio clic) ne modifica una. Deselezionare una regola per disattivarla senza eliminarla. Le frecce cambiano l'ordine, e 'Test' invia subito la regola selezionata alla console, in modo da verificare che reagisca.

## Modificare una regola

![Modifica di una regola OSC](../../assets/images/mb-osc-rule.webp){ width="420" loading=lazy }

**Event**
:   Ciò che accade nel quiz, ad esempio 'Correct answer' o 'Slide changes'. Vedere [Eventi e filtri](#eventi-e-filtri).

**Filters**
:   Alcuni eventi possono essere ristretti, ad esempio 'Fastest finger' a un solo keypad, o 'Slide changes' alle diapositive di una certa classe. Un filtro non selezionato accetta tutto.

**OSC messages**
:   I messaggi da inviare, uno per riga, nell'ordine in cui vengono scritti. 'Examples' inserisce righe già pronte per ETC Eos e QLab.

**Enabled**
:   Attiva o disattiva la regola.

**Test**
:   Invia subito i messaggi alla console. I segnaposto ricevono un valore di esempio, ad esempio la diapositiva 1.

Mentre si digita, l'editor controlla ogni riga e mostra cosa non va, ad esempio le virgolette mancanti.

### Scrivere i messaggi

Scrivere un messaggio come lo scrive ETC nei suoi manuali: l'indirizzo, poi `=` e gli argomenti, separati da virgole.

| Si scrive | QuizXpress invia |
|---|---|
| `/eos/cue/1/20/fire` | Solo l'indirizzo, senza argomenti: attiva il cue 20 della lista cue 1. |
| `/eos/sub/1=1.0` | Un numero decimale (`1.0`): il submaster 1 al massimo. |
| `/eos/macro/fire=5` | Un numero intero (`5`): attiva la macro 5. |
| `/eos/newcmd="Chan 1 At Full#"` | Testo tra virgolette doppie: digita il comando nella riga di comando della console. |
| `# finale lights` | Niente: una riga che inizia con `#` è una nota. |

Il testo tra virgolette doppie viene sempre inviato come testo, anche quando è un numero (`"7"`). Senza virgolette, un numero con il punto decimale viene inviato come numero decimale, un numero senza punto come numero intero, e qualsiasi altra cosa come testo.

### Segnaposto

I segnaposto tra parentesi graffe vengono sostituiti con valori del quiz al momento dell'invio del messaggio. `/eos/cue/1/{slide}/fire` attiva il cue 5 quando appare la diapositiva 5, quindi una sola regola copre l'intero quiz.

| Segnaposto | Valore | Disponibile per |
|---|---|---|
| `{slide}` | Il numero della diapositiva corrente, contato da 1 come in Studio. | Tutti gli eventi |
| `{previous}` | Il numero della diapositiva precedente, `0` per la prima diapositiva. | Tutti gli eventi |
| `{class}`, `{id}` | La classe e l'id della diapositiva corrente, impostati nei metadati della diapositiva in Studio. | Tutti gli eventi |
| `{type}` | Il tipo di diapositiva, ad esempio `question`. | Tutti gli eventi |
| `{device}` | Il numero del keypad o del buzzer. | Fastest finger, Keypad press |
| `{key}` | Il tasto premuto, ad esempio `A`. | Keypad press |
| `{keynumber}` | Il tasto come numero: A = 1, B = 2 e così via, il pulsante del dito più veloce = 0. | Keypad press |
| `{seconds}`, `{ms}` | Il tempo rimanente in secondi e in millisecondi. | Countdown tick |
| `{screen}` | Lo schermo, ad esempio `quizscreen` o `finalscorescreen`. | Screen changes |
| `{command}` | Il pulsante del telecomando, ad esempio `ok` o `f1`. | Remote control button |

Un segnaposto che non appartiene all'evento viene inviato così come è scritto; l'editor lo segnala.

!!! note
    OSC Out conta sempre le diapositive da 1, come Studio, anche quando 'Number slides from 1' nella scheda 'IP Outbound' è disattivato.

### Eventi e filtri

| Event | Si attiva quando… | Filters |
|---|---|---|
| Slide changes | Viene mostrata una nuova diapositiva. | 'From slide', 'To slide', 'Slide class' |
| Screen changes | Il quiz player cambia schermo, ad esempio passando al quiz o ai punteggi finali. | 'Screen' |
| Countdown starts | Il conto alla rovescia parte o riprende dopo una pausa. | – |
| Countdown paused | Il conto alla rovescia viene messo in pausa. | – |
| Countdown tick | Ogni secondo mentre il conto alla rovescia è in corso. | 'Seconds left' |
| Countdown ends | Il conto alla rovescia si ferma. | – |
| Timeout | Il tempo della domanda è scaduto. | – |
| Correct answer | Una risposta viene giudicata corretta. | – |
| Incorrect answer | Una risposta viene giudicata sbagliata. | – |
| Answer revealed | La risposta corretta viene mostrata sulla diapositiva, anche nelle domande a voto in cui nessuno giudica una risposta. Su una diapositiva Trivia Feud, ogni risposta che viene girata sul tabellone. | – |
| Fastest finger | Un giocatore è il primo in una domanda di dito più veloce. | 'Keypad' |
| Keypad press | Viene premuto un tasto su un keypad o un buzzer. | 'Keypad', 'Key' (A = 1, B = 2, dito più veloce = 0) |
| Remote control button | Viene premuto un pulsante sul telecomando del conduttore del quiz. | 'Button' |
| Quiz restarts | Il quiz riparte. | – |
| Bingo claimed, False bingo, Bingo | Viene dichiarato un Bingo, risulta falso o è valido. | – |

- 'Countdown tick' senza filtro invia i suoi messaggi ogni secondo. Con 'Seconds left' li invia una sola volta, quando il conto alla rovescia supera quel momento, ad esempio 5 secondi prima della fine.
- Subito dopo un dito più veloce, il conto alla rovescia termina. Quel 'Countdown ends' viene saltato, in modo che le luci possano restare sul vincitore.
- I numeri di diapositiva nei filtri 'From slide' e 'To slide' contano da 1. Il filtro su una classe di diapositive continua a funzionare quando si riordinano le diapositive.

## Esempi per ETC Eos

| Cosa deve succedere | Evento e filtro | Messaggio OSC |
|---|---|---|
| Ogni diapositiva attiva il cue con il proprio numero nella lista cue 1 | Slide changes | `/eos/cue/1/{slide}/fire` |
| Una risposta corretta attiva il cue 20 | Correct answer | `/eos/cue/1/20/fire` |
| La rivelazione di ogni domanda ha un proprio look, nella lista cue 2 | Answer revealed | `/eos/cue/2/{slide}/fire` |
| Si accende la luce del vincitore | Fastest finger | `/eos/newcmd="Chan %1 At Full#",{device}` |
| Un look speciale per il finale | Slide changes, 'Slide class' finale | `/eos/macro/99/fire` |
| Premere Go 5 secondi prima della fine | Countdown tick, 'Seconds left' 5 | `/eos/key/go_0` |
| Abbassare il submaster 1 quando il conto alla rovescia va in pausa | Countdown paused | `/eos/sub/1=0.3` |

In `/eos/newcmd`, Eos sostituisce `%1` con il primo argomento, qui il numero del keypad, quindi il comando diventa ad esempio `Chan 3 At Full`. Il `#` finale funziona come il tasto Invio.

!!! tip
    Gli altri dispositivi funzionano allo stesso modo. QLab, ad esempio, avvia il cue 5 con `/cue/5/start`; usare `/cue/{slide}/start` per seguire le diapositive.

## Verificare cosa viene inviato

Il [registro dei messaggi](index.md#registro-messaggi) mostra ogni messaggio OSC inviato, con l'evento che lo ha generato. Una riga che non è stato possibile inviare, ad esempio perché un segnaposto ha reso non valido l'indirizzo, appare come errore.

![Messaggi OSC nel registro dei messaggi](../../assets/images/mb-osc-message-log.webp){ loading=lazy }

!!! note
    OSC Out invia via UDP a una sola console. La console non risponde, quindi il registro dei messaggi mostra ciò che QuizXpress ha inviato, non ciò che la console ne ha fatto.
