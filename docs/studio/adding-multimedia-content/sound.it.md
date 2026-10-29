# Suono

Gli spezzoni sonori possono essere usati per domande come « Chi ha scritto questa canzone? », « Quale uccello sta cantando qui? » o « Che rumore è questo? ». Per rendere le cose più interessanti, è possibile variare la velocità del suono nel tempo impostando le proprietà ‘Speed from’ (percentuale di velocità di riproduzione all'inizio del suono) e ‘Speed to’ (velocità di riproduzione alla fine dello spezzone sonoro). Allo stesso modo è possibile variare l'intonazione del suono.

## Inserire un file audio

Per aggiungere uno spezzone sonoro a una diapositiva del quiz, selezionare la scheda della barra multifunzione INSERT e fare clic sul pulsante ‘Audio’, quindi selezionare un file mp3 o wav e scegliere se collegare o incorporare il file:

![](../../assets/images/image206.webp){ width="321" loading=lazy }

Il collegamento produce file del quiz più piccoli e più facili da gestire, ma occorre assicurarsi che tutti i file esterni restino accessibili, nel percorso originale oppure nella cartella in cui è memorizzato il file del quiz (in alternativa, è possibile mantenere esterni i file e [comprimere il quiz con il packing](../other-functionality/packing-and-unpacking-a-quiz.md) prima di distribuirlo; il packing può anche tagliare i suoni alla parte riprodotta e comprimerli).

Una volta inserito il file, diventa visibile la scheda contestuale AUDIO della barra multifunzione, dove configurare le varie opzioni.

![La scheda AUDIO della barra multifunzione](../../assets/images/image207.webp){ width="720" loading=lazy }

## Ritagliare un suono

Di solito si desidera riprodurre solo una parte di una canzone o di una registrazione: il ritornello, l'introduzione o solo i pochi secondi che rivelano la risposta. L'editor di ritaglio mostra il suono come forma d'onda, in modo da vedere dove inizia la musica, dove diventa forte e dove sfuma, e da scegliere la parte da riprodurre ascoltandola.

L'editor di ritaglio non modifica il file audio stesso. Imposta soltanto l'ora di inizio e di fine del suono, quindi è sempre possibile tornare al brano completo.

### Aprire la finestra di ritaglio

Selezionare l'icona del suono sulla diapositiva, quindi utilizzare uno di questi metodi:

- Fare clic sul pulsante ‘Trim’ nel gruppo ‘Timing’ della scheda AUDIO della barra multifunzione, accanto ai tempi di inizio e di fine. La piccola freccia nell'angolo in basso a destra del gruppo ‘Timing’ apre lo stesso editor.

    ![Il pulsante Trim nella scheda AUDIO della barra multifunzione](../../assets/images/sound-ribbon-trim-button.webp){ width="420" loading=lazy }

- Fare clic con il pulsante destro del mouse sull'icona del suono sulla diapositiva e scegliere ‘Trim sound...’.

    ![Trim sound nel menu contestuale del suono](../../assets/images/sound-context-menu-trim.webp){ width="240" loading=lazy }

!!! note
    Non è possibile ritagliare i brani Spotify, i file MIDI o un file audio collegato che non può essere trovato. In questi casi il pulsante ‘Trim’ è disattivato.

### Scegliere la parte da riprodurre

![L'editor di ritaglio](../../assets/images/sound-trim-editor.webp){ loading=lazy }

La parte che verrà riprodotta è evidenziata in blu. Per modificarla:

- **Trascinare sulla forma d'onda** per selezionare una nuova parte, oppure trascinare i marcatori all'inizio e alla fine della selezione.
- **Digitare i tempi** nelle caselle ‘Start’ e ‘End’. È possibile inserire secondi (`75`), minuti e secondi (`1:15`) oppure ore, minuti e secondi (`0:01:15`), con decimali se lo si desidera (`1:15.5`). ‘Length’ indica per quanto tempo viene riprodotta la parte selezionata.
- **Impostare l'inizio o la fine durante l'ascolto**: fare clic su ‘Set start (I)’ o ‘Set end (O)’, oppure premere I oppure O sulla tastiera, nell'esatto momento in cui si sente il punto giusto. Quando non è in corso alcuna riproduzione, questi pulsanti utilizzano la posizione del cursore.
- **‘Whole track’** seleziona di nuovo l'intero suono.

Fare clic in un punto qualsiasi della forma d'onda per posizionare il cursore (la linea arancione).

Per ascoltare:

- ‘Play selection’ (o la barra spaziatrice) riproduce la parte selezionata. Premere di nuovo la barra spaziatrice per interrompere.
- ‘Play from cursor’ riproduce dal cursore fino alla fine del suono.
- Mentre il suono è in riproduzione, fare clic sulla forma d'onda per passare a quel punto.

Il display accanto ai pulsanti mostra la posizione corrente e la durata totale del suono.

Per un lavoro preciso, ingrandire con la rotellina del mouse e utilizzare Maiusc + rotellina del mouse o la barra di scorrimento sotto la forma d'onda per spostarsi a sinistra e a destra. ‘Zoom to fit’ mostra di nuovo l'intero suono.

Fare clic su ‘OK’ per applicare i nuovi tempi di inizio e di fine, oppure su ‘Cancel’ per lasciare il suono com'era. È possibile annullare un ritaglio in un solo passaggio con Annulla. Se il [volume del suono è stato normalizzato](#normalizzare-il-volume), QuizXpress misura di nuovo la nuova parte in modo che mantenga lo stesso livello sonoro.

### Impostare la parte di replay

Nello stesso editor è possibile scegliere la parte che viene riprodotta di nuovo dopo la rivelazione della risposta (vedere [Replay](#replay) più avanti). Spesso si tratta di una parte diversa della canzone rispetto a quella riprodotta durante la domanda, ad esempio il ritornello.

![L'editor di ritaglio con la parte di replay](../../assets/images/sound-trim-editor-replay.webp){ loading=lazy }

1. Selezionare ‘Replay after the answer is revealed’. L'editor passa a ‘Replay’ e la selezione diventa verde.
2. Selezionare la parte di replay nello stesso modo descritto sopra.
3. Facoltativamente, inserire un ‘Delay (s)’: il numero di secondi da attendere dopo la rivelazione della risposta prima che inizi il replay.

Utilizzare i pulsanti ‘Playback’ e ‘Replay’ in alto a sinistra per passare da una parte all'altra. La parte che non si sta modificando viene mostrata come una barra lungo il bordo inferiore della forma d'onda (blu per la riproduzione, verde per il replay), in modo da vedere il rapporto tra le due.

!!! note
    Il replay non è disponibile quando l'opzione ‘Keep playing’ del suono è attiva, perché in tal caso il suono non si interrompe mai.

## Replay

Spesso si desidera riprodurre di nuovo (parte del) brano dopo la fine della domanda, in sincronia con la rivelazione della risposta corretta sulla diapositiva. Questo si ottiene abilitando la funzione di replay audio:

![](../../assets/images/image208.webp){ width="576" loading=lazy }

È possibile impostare un ritardo iniziale, l'ora di inizio e l'ora di fine del brano. Il modo più semplice per scegliere la parte di replay è usare la forma d'onda nell'editor di ritaglio; vedere [Impostare la parte di replay](#impostare-la-parte-di-replay).

## Normalizzare il volume

Canzoni e clip sonori provenienti da fonti diverse raramente hanno lo stesso volume: una vecchia registrazione o un brano classico può essere molto più silenzioso di una canzone pop moderna, così i giocatori fanno fatica a sentire una domanda e vengono assordati dalla successiva. La normalizzazione del volume risolve il problema. QuizXpress misura il volume reale di ogni suono e lo regola in modo che tutti i suoni vengano riprodotti con lo stesso volume, sia in Quiz Studio sia durante lo show.

La normalizzazione non modifica i file audio. Imposta il ‘Loudness gain’ del suono (vedere [sotto](#la-proprieta-loudness-gain)), quindi è sempre possibile modificarlo o annullarlo. Viene misurata solo la parte del suono che viene riprodotta: quella compresa tra l'ora di inizio e quella di fine.

È possibile normalizzare tutti i suoni del quiz in una volta sola, oppure un singolo suono.

### Tutti i suoni del quiz

Fare clic su ‘Normalize volume’ nel gruppo ‘Tools’ della scheda HOME della barra multifunzione.

![Normalize volume nella scheda HOME della barra multifunzione](../../assets/images/normalize-home-tools.webp){ width="220" loading=lazy }

Si apre la finestra ‘Normalize sound volume’, che inizia subito a misurare tutti i suoni del quiz. Le canzoni lunghe richiedono alcuni secondi ciascuna.

![La finestra Normalize sound volume](../../assets/images/normalize-dialog.webp){ loading=lazy }

Per ogni suono vengono mostrati:

- **Slide** e **Sound**: dove si trova il suono e di che cosa si tratta (il nome del file, oppure il testo della domanda per un suono incorporato).
- **Source**: se il suono è incorporato nel quiz o collegato, e il relativo tipo di file.
- **Loudness**: il volume del suono, in LUFS (Loudness Units relative to Full Scale, la misura usata da servizi di streaming ed emittenti). Più vicino a 0 significa più forte: −8 LUFS è una canzone pop forte, −22 LUFS una registrazione silenziosa.
- **Peak**: il momento più forte del suono, in dBFS. 0 dBFS è il massimo che un file audio può memorizzare.
- **Change**: di quanto QuizXpress alzerà (+) o abbasserà (−) il suono, in dB.
- **Status**: tutto ciò che vale la pena sapere sul suono (vedere la tabella seguente).

Scegliere il ‘Target loudness’:

| Target | Use it when |
|---|---|
| Standard (−16 LUFS) | È l'impostazione predefinita. Circa lo stesso volume della musica sui servizi di streaming. |
| Quieter (−18 LUFS) | Si desidera un po' più di margine, ad esempio quando i suoni vengono riprodotti sopra una musica di sottofondo. |
| Broadcast (−23 LUFS) | Si desidera il livello usato da televisione e radio europee (EBU R128). Decisamente più silenzioso; alzare il volume dell'impianto audio di conseguenza. |

La modifica del target aggiorna subito la colonna ‘Change’; i suoni non vengono misurati di nuovo. Quiz Studio ricorda il target scelto e lo utilizza anche per normalizzare i singoli suoni.

Se prima di aprire la finestra sono state selezionate alcune diapositive, l'elenco ‘Sounds’ consente di scegliere tra ‘All sounds in the quiz’ e ‘Sounds on the selected slides’.

Tutti i suoni che cambieranno sono selezionati. Deselezionare un suono per lasciarlo com'è. La riga in basso mostra quanti suoni verranno regolati. Fare clic su ‘Apply’ per impostare i nuovi loudness gain. È possibile annullare l'intera normalizzazione in un solo passaggio con Annulla.

| Status | Meaning |
|---|---|
| Limited to avoid clipping | Il suono è silenzioso ma ha già picchi elevati. QuizXpress lo alza solo fin dove possibile senza distorsione (i picchi restano sotto −1 dBFS), quindi può rimanere un po' più silenzioso degli altri. |
| Already at target | Il suono è già al volume target e non viene modificato. |
| Silent | Nella parte riprodotta non c'è alcun suono (controllare l'ora di inizio e di fine). |
| Skipped: MIDI has no audio to measure | I file MIDI non possono essere misurati e mantengono il proprio volume. |
| Skipped: Spotify track | I brani Spotify non possono essere misurati e mantengono il proprio volume. |
| Sound file is missing | Un file audio collegato non può essere trovato. [Correggere il collegamento](../other-functionality/fixing-broken-links.md) e riprovare. |

### Un singolo suono

Per normalizzare un solo suono, ad esempio dopo averlo sostituito, selezionare l'icona del suono sulla diapositiva e fare clic su ‘Normalize’ nel gruppo ‘Effects’ della scheda AUDIO della barra multifunzione, oppure fare clic con il pulsante destro del mouse sull'icona del suono e scegliere ‘Normalize volume’. La descrizione comandi del pulsante mostra il volume target che verrà utilizzato: quello scelto per ultimo nella finestra ‘Normalize sound volume’.

![Il pulsante Normalize nella scheda AUDIO della barra multifunzione](../../assets/images/normalize-sound-button.webp){ width="720" loading=lazy }

QuizXpress misura il suono e imposta subito il relativo loudness gain, senza aprire alcuna finestra. Una barra sotto la barra multifunzione mostra il risultato, con un collegamento ‘Undo’ per annullarlo:

![Il risultato della normalizzazione di un singolo suono](../../assets/images/normalize-sound-result.webp){ width="720" loading=lazy }

### La proprietà ‘Loudness gain’

Il risultato della normalizzazione viene memorizzato nella proprietà ‘Loudness gain’ del suono, nella sezione ‘Audio’ del pannello delle proprietà. 0 dB lascia il suono invariato; l'intervallo va da −30 a +20 dB. È anche possibile regolarla con precisione manualmente.

![Loudness gain nel pannello delle proprietà](../../assets/images/normalize-loudness-gain.webp){ width="250" loading=lazy }

Il loudness gain si aggiunge al ‘Volume’ del suono. A differenza del volume, che può solo rendere un suono più silenzioso, il loudness gain può anche rendere più forte un suono silenzioso.

!!! tip
    Normalizzare dopo aver ritagliato un suono, perché è la parte riprodotta a determinarne il volume. Se un suono è già stato normalizzato e se ne modifica l'ora di inizio o di fine nell'[editor di ritaglio](#ritagliare-un-suono), QuizXpress misura la nuova parte e regola automaticamente il loudness gain.

## Importazione di playlist Spotify ™

È possibile importare le proprie playlist Spotify (facoltativamente con la copertina dell'album e un'anteprima di 30 secondi dei brani) e creare senza fatica un quiz Trivia Music o un gioco Disco Bingo. QuizXpress non interagisce direttamente con Spotify, ma supporta un formato di file CSV prodotto dal sito [Exportify](https://watsonbox.github.io/exportify/). Per usare questa funzione, esportare la playlist in CSV tramite il sito e importare il file in QuizXpress. Viene visualizzato un modulo in cui effettuare alcune scelte:

![](../../assets/images/image209.webp){ width="224" loading=lazy }

Se con queste opzioni si crea un gioco Bingo, si ottiene un insieme di caselle con copertine di album e testo Artista/Titolo, come:

![](../../assets/images/image210.webp){ loading=lazy }

Le diapositive create e le impostazioni di gioco possono essere ritoccate dopo l'importazione.

## Applicare effetti sonori

Quando si riproducono i suoni sono possibili vari effetti:

- **Aumentare la velocità del suono** – si ottiene assegnando lo stesso valore alle proprietà ‘speed percentage’ e ‘target speed percentage’ del suono nel Property Editor. Questo valore deve essere superiore a 100 per accelerare il suono. Per visualizzare le proprietà di un suono, fare clic con il pulsante sinistro del mouse sull'icona del suono nell'area di progettazione.

- **Rallentare la velocità del suono** – si ottiene assegnando a entrambe le proprietà sopra menzionate un valore inferiore a 100. Anche in questo caso, assegnare lo stesso valore a entrambe; il motivo è spiegato più avanti.

- **Da velocità lenta a velocità normale** – per ottenerlo, inserire un valore inferiore a 100 per la proprietà ‘speed percentage’ del suono. In questo modo il suono inizia a essere riprodotto rallentato. Lasciare invariata la proprietà ‘target speed percentage’; il suo valore predefinito è 100, cioè velocità normale. Di conseguenza, QuizXpress riprodurrà il suono prima lentamente, ma con il passare del tempo raggiungerà la velocità target di 100 (velocità normale).

- **Da velocità elevata a velocità normale** – per ottenerlo, selezionare un valore superiore a 100 per la proprietà ‘speed percentage’. Lasciare invariata la proprietà ‘target speed percentage’.

- **Reverse** – riproduce lo spezzone sonoro al contrario, sfidando i giocatori a riconoscere la canzone (selezionare la casella Reverse audio nella barra multifunzione del suono)

È possibile ascoltare questi effetti sonori mentre si crea la domanda che contiene il suono. Per ascoltare il suono e i suoi effetti, fare clic sul pulsante ‘Play’ nella barra multifunzione, oppure selezionare ‘Play’ dal menu contestuale del suono.

Se non si desidera che il suono parta subito all'inizio della domanda, utilizzare la proprietà ‘Intro Pause’ del suono per ritardare la riproduzione (questo dà ai partecipanti la possibilità di leggere prima la domanda, oppure al Quizmaster la possibilità di leggerla prima ad alta voce).

!!! note

    gli altri suoni, come i suoni del buzzer, la musica di sottofondo e la musica del conto alla rovescia, possono essere configurati in Quiz Setup.*
