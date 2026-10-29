# Morra Cinese

Nel minigioco Rock Paper Scissors, il pubblico gioca contro un avversario virtuale.
I giocatori scelgono sasso, carta o forbici sul proprio buzzer, keypad o telefono. La mano del
computer si muove su e giù tre volte prima di rivelare la sua scelta.

![Schermata di voto di Rock Paper Scissors con lo stile di mano bianco](../../assets/images/rock-paper-scissors-voting.webp){ loading=lazy }

## Giocare un round

1. Avviare il gioco. Compare lo studio e parte la musica di sottofondo.
2. Usare 'Next' per aprire la votazione.
3. I giocatori premono **A per sasso**, **B per carta** o **C per forbici**. In ogni round conta solo la
   prima scelta valida; i voti successivi vengono ignorati.
4. Usare 'Next' per chiudere la votazione e avviare l'animazione della mano. La musica si interrompe e
   gli effetti sonori accompagnano i tre movimenti e la rivelazione.
5. Dopo la rivelazione, usare 'Next' per mostrare i risultati del round ed eliminare i giocatori sconfitti.
   Le loro tessere scompaiono con un'animazione e un effetto sonoro. Le tessere rimanenti
   si spostano in una nuova disposizione.
6. Usare 'Next' per aprire il round successivo, oppure per terminare il gioco quando la modalità di gioco
   selezionata è giunta al termine.

Valgono le regole consuete: il sasso batte le forbici, le forbici battono la carta e la carta batte il sasso.
I giocatori che scelgono lo stesso gesto del computer restano in gioco, ma non ottengono
i punti per una risposta corretta. I giocatori che perdono, o che non inviano una scelta valida
prima della chiusura della votazione, vengono eliminati.

!!! tip
    Ad esempio, se il computer rivela sasso, i giocatori che hanno scelto carta vincono il round,
    quelli che hanno scelto sasso pareggiano e quelli che hanno scelto forbici vengono eliminati.

![Risultati del round con lo stile di mano neon e i giocatori rimasti](../../assets/images/rock-paper-scissors-results.webp){ loading=lazy }

## Modalità di gioco e punteggio

![Impostazioni di Rock Paper Scissors con anteprime delle mani e colori di voto](../../assets/images/rock-paper-scissors-settings.webp){ width="600" loading=lazy }

Aprire le impostazioni del gioco per scegliere una modalità di gioco:

- **'Rounds'**: si gioca un numero stabilito di round. 'Number of rounds' deve essere almeno **1**.
- **'Last man standing'**: si continua finché non rimane esattamente un giocatore, oppure tutti
  sono stati eliminati. In questa modalità 'Number of rounds' è disattivato.

'Points for survivors' imposta il bonus assegnato ai giocatori che sopravvivono al gioco.
'Points for every right answer' imposta i punti assegnati per aver battuto il computer in
un round. Una risposta in pareggio mantiene il giocatore in gioco senza assegnare questi punti del round.

### La sorpresa del dito

'Chance for the finger to appear' imposta la percentuale di probabilità che il computer riveli
un dito medio al posto di sasso, carta o forbici. Si tratta di una finta eliminazione scherzosa:
il pubblico sembra fuori gioco, ma le sue tessere ritornano e il gioco continua.

Impostare la probabilità su **0** per disattivare questa sorpresa.

## Aspetto

### Stile della mano

Scegliere uno stile di mano utilizzando le anteprime nelle impostazioni:

- **White**: un classico guanto bianco da cartone animato.
- **Neon**: una mano viola luminosa con tocchi di azzurro e rosa.
- **Comic**: una mano rossa decisa in stile fumetto.
- **Robot**: una mano robotica spigolosa.

Lo stile selezionato viene usato per l'animazione principale, le immagini di scelta
sasso/carta/forbici e le icone di scelta dei giocatori. Anche i pannelli di scelta e le tessere dei giocatori
si adattano allo stile della mano.

### Sfondo

Lo sfondo predefinito è uno studio da gameshow al neon animato. Usare il selettore 'Background image'
per scegliere una propria immagine fissa. Rimuovere l'immagine personalizzata per tornare allo
studio predefinito.

### Colori di voto dei giocatori

Scegliere i colori per sasso, carta e forbici in 'Player voting colors'. I
colori predefiniti sono grigio, verde chiaro e rosso.

Attivare 'Show player voting colors while voting' per mostrare la scelta di ogni giocatore mentre
la votazione è ancora aperta. Quando questa opzione è disattivata, le tessere indicano che il giocatore ha votato
e la sua scelta viene mostrata dopo che il computer ha rivelato la sua mano.

## Tessere dei giocatori e gruppi numerosi

L'area dei giocatori si adatta automaticamente al numero di giocatori rimasti:

- I gruppi piccoli mostrano i numeri e i nomi dei giocatori. I nomi più lunghi usano fino a due righe.
- I gruppi più grandi usano tessere compatte con i numeri dei giocatori.
- Per i gruppi molto numerosi, le tessere mostrano lo stato del giocatore senza numero se il numero sarebbe
  troppo piccolo da leggere.

La visualizzazione dei numeri dipende dallo spazio disponibile e dalle dimensioni della finestra di gioco,
quindi non esiste un numero fisso di giocatori oltre il quale compaiono i numeri. Man mano che i giocatori vengono eliminati,
la disposizione viene ricalcolata e i numeri ricompaiono quando c'è spazio sufficiente. I nomi e
le icone di scelta ritornano quando il gruppo si riduce.

I giocatori eliminati vengono rimossi automaticamente dopo l'animazione di eliminazione. Non esiste
una modalità di visualizzazione dei giocatori separata né un'impostazione 'Hide expelled players' da selezionare.

## Audio

Il gioco include musica di sottofondo ed effetti per i movimenti della mano, la rivelazione
e la scomparsa dei giocatori eliminati. La musica di sottofondo parte all'apertura del
gioco e suona durante la votazione. Si interrompe quando inizia l'animazione della mano.

In 'Sound', usare 'Music during voting' per scegliere una propria musica. Il pulsante di riproduzione
consente di ascoltare in anteprima la selezione; il pulsante di cancellazione ripristina la musica predefinita del gioco.

!!! note
    La musica e gli effetti sonori standard sono inclusi nel gioco. Non è necessario installare
    file audio separati.

## Messaggi personalizzati

Attivare 'Use custom texts' per sostituire i messaggi predefiniti:

- **'Voting text'**: il titolo mostrato mentre i giocatori scelgono.
- **'Winner'**: il messaggio mostrato quando rimane un solo giocatore.
- **'All out'**: il messaggio mostrato quando tutti sono stati eliminati.

Usare il pulsante di reimpostazione per ripristinare i messaggi predefiniti.
