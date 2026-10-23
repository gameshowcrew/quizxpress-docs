# Analizzare i risultati del quiz con QuizXpress Analyzer

QuizXpress include uno strumento di analisi grafico denominato Analyzer. Analyzer aiuta a comprendere e visualizzare i dati raccolti durante il quiz. È possibile aprire più set di dati, per confrontare i dati raccolti nel tempo. Sono disponibili tre viste:

- Question view

- Team view

- Demographic Groups (se durante un quiz erano presenti gruppi demografici)

La vista incentrata sulle domande si presenta così:

![](../assets/images/image471.webp){ width="604" loading=lazy }

1)  L'elenco di tutte le domande del set di dati

2)  La domanda stessa con le possibili risposte (se il file del quiz .qx è disponibile nel sistema, viene visualizzata un'immagine della diapositiva; se non è più disponibile, si vedrà solo una rappresentazione testuale)

3)  Le risposte e i punteggi (per la domanda selezionata) per squadra/giocatore. Quando sono disponibili gruppi demografici, in basso a destra viene mostrata una scheda ‘Demographic Groups’. In questa scheda, per ciascun gruppo, viene mostrato in una tabella il numero di voti per risposta per la domanda selezionata.

4)  Un grafico a torta che mostra la distribuzione delle risposte per la domanda selezionata. Quando sono disponibili gruppi demografici, nella scheda Demographic Groups la distribuzione delle risposte di un gruppo può essere visualizzata selezionando quel gruppo dall'elenco posto sopra il grafico della distribuzione delle risposte.

La vista per squadra ha il seguente layout:

![](../assets/images/image472.webp){ width="547" loading=lazy }

1)  L'elenco dei nomi delle squadre/dei giocatori. Si noti che qui è possibile selezionare più squadre.

2)  Un grafico che mostra l'andamento del punteggio nel tempo

3)  Le domande e le risposte della o delle squadre selezionate

La vista dei gruppi demografici ha lo stesso layout. Nella tabella, per ogni domanda, vengono visualizzate tutte le risposte. Per ogni gruppo selezionato viene visualizzato il numero di voti per ciascuna risposta. Viene inoltre mostrato l'andamento del punteggio nel tempo per il o i gruppi selezionati.

Tutti i dati mostrati in Analyzer vengono memorizzati durante un quiz da QuizXpress Live sotto forma di documenti XML nella cartella dati dell'applicazione QuizXpress (in Windows 7 il percorso di questa cartella è ‘C:\Users\\username>\AppData\Roaming\QuizXpress\Scores’). Si noti che è possibile aprire questa cartella da QuizXpress Studio tramite il menu Tools->Advanced.
