# La schermata del quiz: voting (tutti rispondono)

Dopo il video del conto alla rovescia (che può essere disattivato e/o sostituito con un video personalizzato in Quiz Setup), compare la schermata del quiz. Come si vede dalla schermata di esempio qui sotto, ci sono alcune aree che richiedono particolare attenzione, tutte parte di quello che chiamiamo «Information Panel»:

1.  Il timer del conto alla rovescia. Il timer conta alla rovescia dal tempo indicato al momento della creazione del quiz in QuizXpress Live fino a zero. Sotto il timer è indicata la posizione della domanda nel quiz, nel formato \<numero della domanda/numero totale di domande>.

2.  Le squadre (partecipanti) che hanno premuto il proprio keypad. Questo indicatore ha tre fasi: prima mostra una griglia di quadrati che indica da quale keypad è stata ricevuta una risposta, offrendo un quadro generale. Quando restano pochi keypad, mostra i singoli numeri dei keypad. Quando ne restano ancora meno, mostra i nomi dei giocatori come impostati in Quiz Setup, aiutando il conduttore del quiz a identificare gli ultimi giocatori che devono ancora rispondere.

3.  Il numero totale di giocatori che hanno già fornito una risposta.

4.  Il numero di punti ottenibili rispondendo correttamente alla domanda. Si noti che i punti possono diminuire nel tempo a seconda delle impostazioni della diapositiva definite in Studio.

![](../../assets/images/image407.webp){ loading=lazy }

Quando ogni squadra ha fatto la propria scelta, il sistema valuta tutte le risposte e aggiunge o sottrae punti ai punteggi. Inoltre, nella parte superiore della schermata del quiz viene mostrato un grafico:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Numero di squadre che hanno risposto correttamente</p></li>
<li><p>Numero di squadre che hanno risposto in modo errato</p></li>
<li><p>Numero di squadre che non hanno risposto affatto</p></li>
</ul></th>
<th><img src="../../../assets/images/image408.webp" alt="" width="368" loading="lazy"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Quando si utilizzano i Sony Buzzer, QuizXpress Live gestisce una diapositiva di quiz di tipo voting in modo leggermente diverso. Invece di un contatore nella parte superiore dello schermo che conta le squadre che hanno risposto finora, compare un pannello con il nome e l'avatar di ogni squadra man mano che risponde. Dopo che tutti hanno premuto il proprio buzzer (o il conto alla rovescia ha raggiunto lo zero), QuizXpress Live mostra tutte le risposte scelte, le valuta e visualizza i punteggi totali di tutte le squadre. Di seguito è mostrata una rappresentazione visiva di questa sequenza.

| ![](../../assets/images/image409.webp){ width="160" loading=lazy } | ![](../../assets/images/image410.webp){ width="166" loading=lazy } |                                                                                 | ![](../../assets/images/image411.webp){ width="155" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ![](../../assets/images/image412.webp){ loading=lazy } |                                                                                 | ![](../../assets/images/image413.webp){ loading=lazy } | ![](../../assets/images/image414.webp){ loading=lazy } |

Il voting è una delle possibili modalità di una diapositiva di quiz. Le altre varianti sono descritte di seguito.

## Fastest Finger/ Lock-out

Nella sezione precedente abbiamo trattato la schermata di una domanda «voting», alla quale tutti possono rispondere. Con una domanda fastest-finger, può rispondere solo la prima persona che preme il proprio buzzer. Se risponde in modo errato, vengono sottratti punti dal suo punteggio e il conto alla rovescia continua. Gli altri giocatori hanno quindi la possibilità di premere il proprio buzzer (il giocatore che ha risposto in modo errato non può più rispondere alla domanda corrente).

Nella pagina successiva è mostrata una tipica schermata fastest finger. La differenza più importante rispetto a una schermata voting è che in questa schermata, in basso, c'è una grande barra con il nome della squadra (o della persona) che ha premuto per prima il proprio buzzer. Questa barra mostra anche la risposta data, l'avatar della squadra e i punti guadagnati/persi. In questo caso la squadra 17 ha dato la risposta giusta, guadagnando così 10 punti. Il grande segno di spunta verde indica che la domanda ha ricevuto una risposta corretta. In questo esempio, la risposta corretta era stata impostata su Answer-‘D’ in QuizXpress Studio e l'opzione ‘autojudge’ (judge question automatically nella barra multifunzione del menu) della diapositiva del quiz era impostata su true. In questo caso QuizXpress valuta automaticamente la risposta quando viene premuto un pulsante a scelta multipla su un buzzer. Quando un buzzer non ha un pulsante a scelta multipla (ad esempio i Sparkle poles), l'opzione ‘auto judge’ non si applica automaticamente. In tal caso la squadra\il giocatore deve rispondere a voce, dopodiché il conduttore del quiz deve valutare la risposta utilizzando il proprio telecomando, la tastiera del computer o QuizXpress Director. Per ulteriori informazioni sui comandi del conduttore del quiz, vedere [Controllo del quiz](../controlling-the-quiz.md).

Il fatto che ‘Team 17’ abbia premuto per prima può essere verificato controllando l'«Information Panel» nella parte superiore dello schermo. Questo pannello mostra, in riquadri separati, l'ora in cui ogni squadra ha premuto il buzzer. Ogni riquadro contiene il nome di una squadra che ha premuto il proprio buzzer, insieme all'orario in cui lo ha premuto, ordinati da sinistra a destra, a partire dalla squadra più veloce.

| ![](../../assets/images/image415.webp){ loading=lazy } | ![](../../assets/images/image416.webp){ loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

Si noti che l'Information Panel in alto mostra il numero di punti ottenibili (che possono diminuire nel tempo, come spiegato in precedenza). Inoltre, non c'è alcun indicatore del numero di squadre che hanno risposto, poiché non è applicabile a una domanda fastest-finger.

!!! note

    Quando si utilizzano i buzzer QuizXpress (che hanno sia i pulsanti a scelta multipla ABCD sia un grande pulsante buzzer) per domande a scelta multipla, tenere presenti queste due opzioni:*

- *Quando ‘auto judge’ è ‘true’ nella finestra delle proprietà (equivalente nella barra multifunzione del menu: ‘Judge question’ è impostato su ‘Automatically’), i partecipanti devono usare i pulsanti ABCD del buzzer. QuizXpress valuta automaticamente la risposta data.*

- *Quando ‘auto judge’ è ‘false’ nella finestra delle proprietà (equivalente nella barra multifunzione del menu: ‘Judge question’ è impostato su ‘Manual’), i partecipanti devono usare il grande pulsante buzzer per prenotarsi. Il giocatore che ha premuto più velocemente dà quindi la risposta a voce e il conduttore del quiz la valuta.*

## Billboard

Una diapositiva di quiz Billboard è una diapositiva di quiz con cui non è possibile alcuna interazione dei giocatori — è semplicemente una visualizzazione statica. È possibile progettare una diapositiva Billboard proprio come una domanda normale, utilizzando testo, colori, immagini, suoni e video.

Utili applicazioni di una diapositiva Billboard includono:

- Indicazione del round

- Mostrare la domanda (come anteprima) prima di una diapositiva di quiz voting.

- Mostrare informazioni di marketing sotto forma di immagini, suoni o video

## End of Round

In QuizXpress è possibile indicare che una diapositiva di quiz segna la «fine di un round». Per farlo, impostare il tipo di una diapositiva di quiz su ‘End of Round’ in QuizXpress Studio.

Quando durante un quiz viene mostrata una diapositiva End of Round, non ha luogo alcuna interazione con i partecipanti. Ad esempio, può essere usata per mostrare il testo «Fine del round 3». Come in precedenza, la diapositiva può essere progettata a piacere, utilizzando video, suoni e immagini.

Quando si imposta una diapositiva su ‘End of Round’, è possibile impostare un'altra opzione, chiamata ‘end of round action’. Può essere impostata su una delle seguenti opzioni:

- Disable one player: elimina automaticamente il giocatore con meno punti. Se più giocatori sono a pari merito in fondo alla classifica intermedia, il conduttore del quiz seleziona quale giocatore verrà eliminato, utilizzando i tasti freccia della tastiera o il telecomando del conduttore del quiz. Il giocatore/la squadra selezionato/a viene evidenziato/a con una luce rossa lampeggiante. Premendo la barra spaziatrice della tastiera, o il pulsante inferiore del telecomando del conduttore, il giocatore selezionato viene eliminato. Decidere quale giocatore eliminare quando più squadre hanno lo stesso punteggio esula dall'ambito di QuizXpress Live — ad esempio, un conduttore del quiz potrebbe porre una domanda di stima ed eliminare il giocatore la cui risposta è più lontana da quella corretta.

> ![](../../assets/images/image417.webp){ loading=lazy }

- Manually dismiss players: il conduttore del quiz può selezionare un numero qualsiasi di giocatori da eliminare. Lo fa uno alla volta, sempre utilizzando la tastiera o il telecomando del conduttore per selezionarli. Un esempio di diapositiva di quiz ‘End of Round, quizmaster selects losers’ è mostrato sopra. Il pulsante «play» in basso nello schermo indica che il conduttore del quiz ha finito di eliminare i giocatori; premerlo (selezionarlo con la tastiera e premere spazio) fa proseguire il quiz. Il pulsante con la freccia rotante annulla il processo di eliminazione se il conduttore del quiz elimina qualcuno per errore, dopodiché può ricominciare a eliminare i giocatori.

- Automatically dismiss players: con questa opzione, il sistema disattiva automaticamente un certo numero di giocatori (come configurato per la diapositiva in Studio), senza alcun riscontro visivo per il pubblico.

Show scoreboard/Show round scores: il sistema mostra la classifica dell'intero quiz oppure del round corrente.

Reset scores: azzera tutti i punteggi alla fine del round.

Un round è definito come l'insieme delle diapositive comprese tra:

- La prima diapositiva del quiz e la prima diapositiva End of Round (round 1)

- Due diapositive *End of Round*

- La diapositiva che segue l'ultima diapositiva *End of Round* e l'ultima diapositiva del quiz

Di seguito è riportato un esempio di quiz con tre round.

![](../../assets/images/image418.webp){ width="595" loading=lazy }

Una diapositiva ‘End of Round’ può essere usata anche per i round ‘Last Man Standing’. Quando si utilizzano domande ‘Last Man Standing’, i giocatori che rispondono in modo errato vengono eliminati dal quiz e non possono più partecipare. Quando viene mostrata una diapositiva ‘End of Round’, tutti i giocatori che sono fuori dal gioco a causa di domande ‘Last Man Standing’ possono rientrare.

!!! note

    I giocatori\le squadre possono anche essere attivati\disattivati da QuizXpress Director. In QuizXpress Director è inoltre possibile aggiungere nuovi giocatori durante un quiz o modificare i punti di una squadra. Per ulteriori informazioni su QuizXpress Director, vedere [QuizXpress Director](../quizxpress-director/index.md).*

## Test Question

Una diapositiva di quiz ‘Test Question’ si comporta come una normale diapositiva di quiz, tranne che non vengono aggiunti/sottratti punti quando la domanda ha ricevuto risposta. Può essere usata per dimostrare come funziona il sistema ed è spesso utilizzata come prima domanda di un quiz per far familiarizzare i giocatori con il sistema.

## Demographic

Il tipo di diapositiva di quiz ‘Demographic’ consente di dividere tutti i giocatori in gruppi diversi che competono tra loro (esempi di questo tipo di quiz includono «battaglia dei sessi», «marketing contro finanza», ecc.).

Per utilizzare questa funzionalità, impostare il tipo di una diapositiva di quiz su ‘Demographic’ in QuizXpress Studio. Nella griglia delle proprietà compare quindi un campo di immissione chiamato ‘Demographic group’, in cui è possibile inserire il nome di un gruppo demografico (ad es. ‘Males’). Per il layout della diapositiva di quiz, è necessario selezionare un layout che contenga una domanda e nessuna risposta. Inserire un testo della domanda che indichi ai giocatori che un certo gruppo di persone deve premere il proprio buzzer per diventare membro di un gruppo specifico (ad es. «Premete il buzzer se siete uomini»).

!!! note

    In alternativa, è possibile dividere il pubblico in gruppi prima dell'inizio del quiz in QuizXpress Setup. Qui si può definire quali keypad appartengono a quale gruppo. Per ulteriori informazioni, fare riferimento a [Grouping keypads](../../setup/setting-up-teams-the-teams-tab-page.md#raggruppare-i-keypad)*

## Last Man Standing

Una diapositiva di quiz di tipo ‘Last Man Standing’ elimina dal round del quiz ogni giocatore che risponde in modo errato a una domanda. Se dopo l'eliminazione rimane un solo giocatore, questi vince il round e il quiz passa alla prima diapositiva End of Round incontrata, oppure alla fine del quiz. Se invece tutti i giocatori rimasti rispondono in modo errato a una domanda, nessuno di essi viene eliminato.

## Domande di risposta del pubblico

Questo è un tipo di domanda che può essere utilizzato per raccogliere dati/statistiche arbitrari dal pubblico. Le risposte date a una domanda di risposta del pubblico vengono registrate ma non hanno alcun impatto sui punteggi. Dopo una domanda di risposta del pubblico, è possibile mostrare un grafico con il tasto «C» per visualizzare la distribuzione delle risposte date.

![](../../assets/images/image419.webp){ width="604" loading=lazy }

## Domanda Wager

Le domande Wager possono essere usate per far scommettere il pubblico sull'esito della domanda successiva. Consentono di creare domande «in stile Jeopardy» in cui le persone puntano punti in base a quanto ritengono di sapere su un argomento.

Quando si imposta una diapositiva di quiz sul tipo ‘Wager’, in QuizXpress Studio appare come segue:

![](../../assets/images/image420.webp){ loading=lazy }

Il testo della domanda viene modificato per impostazione predefinita in «Please place your bet for the next question…», ma il testo può essere cambiato in seguito a piacere. Le risposte a questo tipo di domanda servono a impostare la percentuale del punteggio che il giocatore può vincere o perdere nella domanda successiva. Ad esempio, se il giocatore risponde ‘C’ a questa domanda, significa che punta il 66% del proprio punteggio sulla domanda successiva. Se risponde correttamente alla domanda successiva, il suo punteggio aumenta del 66%. Naturalmente, se si utilizza un layout di diapositiva con cinque risposte, le percentuali sono distribuite su cinque opzioni (0%, 25%, 50%, 75% e 100%). È anche possibile impostare la percentuale manualmente facendo clic su una qualsiasi delle risposte e modificando la proprietà ‘Wager %’.

Le puntate (wager) possono essere usate anche con un numero di punti anziché una percentuale.
