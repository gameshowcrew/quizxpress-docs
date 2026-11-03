# Word Game

Un elemento Word Game è un elemento grafico per creare domande basate su parole e frasi. Quando si inserisce un Word Game, compare la seguente finestra:

![](../../assets/images/image221.webp){ width="320" loading=lazy }.

Qui si inserisce il testo da visualizzare e si selezionano il tipo di gioco e le eventuali opzioni correlate.

Esistono quattro giochi diversi:

| *Word Reveal* (mostrato qui nel formato a griglia fissa di 52 lettere). Le lettere compaiono nel tempo, partendo da una griglia vuota | ![](../../assets/images/image222.webp){ width="279" loading=lazy } |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| *Word Scramble* (anagramma). La parola o la frase si riordina nel tempo                                                        | ![](../../assets/images/image223.webp){ width="388" loading=lazy } |
| *Letter Grid. Le parole sono nascoste in una griglia di lettere casuale. Al termine della domanda, le parole vengono evidenziate.* | ![](../../assets/images/image224.webp){ width="122" loading=lazy }  |
| *Word Wheel. La parola è presentata come una ruota (facoltativamente rotante). Una lettera viene rimossa a caso e posizionata al centro.* | ![](../../assets/images/image225.webp){ width="126" loading=lazy } |

Sia Word Reveal sia Word Scramble possono essere presentati visivamente come una normale griglia su più righe (griglia di lettere dinamica) oppure su un tabellone fisso di 52 caselle (come nel gioco televisivo La Ruota della Fortuna©). Si noti che per questi due elementi spetta all'utente suddividere la frase su più righe premendo Invio per andare a capo.

Con Word Reveal è possibile scegliere di controllare manualmente la rivelazione da QuizXpress Director. Durante l'esecuzione di un quiz, quando viene mostrata la diapositiva compare la scheda ‘Reveal Word Game’ in QuizXpress Director. Qui è possibile rivelare manualmente una lettera citata da un giocatore premendo il pulsante corrispondente, oppure rivelare una vocale, una consonante, una parola o l'intera frase (all).

Se la lettera fa parte della frase, viene rivelata nel lettore del quiz. Dopo aver premuto una lettera, Director mostra anche se è presente nella frase (lettera verde) o no (lettera rossa).

![](../../assets/images/image226.webp){ loading=lazy }

Se un giocatore tenta di indovinare la parola, è possibile giudicarla premendo il pulsante corretto o errato, dopodiché sullo schermo del lettore del quiz compare per il pubblico un grande segno di spunta verde o una croce rossa.

Il lettore del quiz mostra la griglia di lettere con le lettere rivelate. Può anche mostrare una panoramica delle lettere non ancora scelte (abilitando l'opzione ‘Show alphabet strip’ nelle proprietà avanzate di QuizXpress Studio).

![](../../assets/images/image227.webp){ loading=lazy }

La modalità manuale supporta anche l'acquisto di vocali e la vincita o perdita di punti indovinando le consonanti. Le impostazioni del punteggio per vocali e consonanti possono essere configurate in QuizXpress Studio dopo aver selezionato l'elemento Word Game sulla diapositiva.

![](../../assets/images/image228.webp){ width="359" loading=lazy }

Il giocatore che parteciperà al gioco può essere selezionato durante il quiz in QuizXpress Director, nella scheda Reveal Word game.

![](../../assets/images/image229.webp){ width="505" loading=lazy }

I punti vinti o persi vengono mostrati nel lettore del quiz.

| ![](../../assets/images/image230.webp){ loading=lazy } | ![](../../assets/images/image231.webp){ loading=lazy } | ![](../../assets/images/image232.webp){ loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Acquisto di una vocale**                                                      | **Consonante corretta**                                                         | **Consonante errata**                                                           |

Per i giochi automatici Word Reveal e Word Scramble è possibile configurare la tempistica di rivelazione/riordino. Per impostazione predefinita ogni passaggio richiede lo stesso tempo, il che significa che, nel gioco di rivelazione, le lettere compaiono a intervalli fissi. Questo può andare bene per una singola parola, ma per una frase più lunga si potrebbe preferire uno schema diverso, ad esempio mostrando più lettere all'inizio e poi rallentando. È possibile scegliere l'opzione preferita nella sezione ‘Reveal timing’.

Una volta inserito l'elemento Word Game nella diapositiva, è possibile configurarlo ulteriormente: fare clic sull'elemento Word Game, quindi modificarne le impostazioni nella barra multifunzione Word Game nella parte superiore di Studio, oppure nella griglia delle proprietà avanzate visualizzata a destra in QuizXpress Studio.

![](../../assets/images/image233.webp){ loading=lazy }

Questo elemento può essere usato per diversi tipi di domande. Ad esempio, una domanda Dito più Veloce in cui il giocatore che prenota la risposta con il buzzer indovina la frase corretta in base alle lettere rivelate finora, oppure indica una lettera da rivelare e poi tenta di indovinare la frase. Oppure si può usare una domanda a risposta testuale libera con QuizXpress mobile, in cui tutti i giocatori possono digitare la risposta corretta. Combinandola con punti decrescenti, i giocatori più veloci ottengono più punti. In alternativa, si può dare a ogni giocatore il suo turno e fargli vincere punti usando la modalità di rivelazione manuale in combinazione con i punti. Colore, carattere, dimensione delle lettere, spaziatura e così via possono essere tutti modificati nella barra multifunzione o nella griglia delle proprietà avanzate.

L'elemento Word Game segue la proprietà ‘Show correct answer’ della diapositiva. Se impostata su ‘Do not show’, il Word Game non rivela la risposta corretta al termine della domanda. Se impostata su ‘Global’ (impostazione predefinita), il Word Game segue l'impostazione ‘Show correct answer on quiz slides’ di Quiz Setup.
