# Area di progettazione

L’area di progettazione contiene una rappresentazione visiva di quella che chiamiamo una “diapositiva del quiz”. Mostra la diapositiva del quiz esattamente come verrà visualizzata durante lo show. Una diapositiva del quiz è composta da più elementi: una domanda, risposte a scelta multipla, immagini, forme e testo, un video o un elemento audio, ecc. Gli elementi possono essere selezionati singolarmente o come gruppo e poi modificati. Anche la diapositiva del quiz nel suo insieme può essere selezionata per modificarne le proprietà. Per selezionare una diapositiva del quiz, fare clic sullo sfondo della diapositiva. Vedere [Quiz slide properties](advanced-properties-grid.md#proprieta-delle-diapositive-del-quiz) per una panoramica di tutte le proprietà di una diapositiva.

Gli elementi della diapositiva possono essere selezionati e ridimensionati facendo clic con il tasto sinistro su una delle maniglie di ridimensionamento e trascinandola fino alla dimensione desiderata. Quando sono selezionati più elementi, usando il tasto Ctrl oppure trascinando un riquadro di selezione con il mouse, la modifica delle proprietà mostrate nel riquadro delle proprietà (o tramite i controlli della barra multifunzione) cambia le proprietà di tutti gli elementi selezionati contemporaneamente. Ciò è utile, ad esempio, per impostare in un colpo solo il carattere di tutte le risposte di una domanda: selezionare prima tutte le risposte, quindi modificare la proprietà ‘font’ nel riquadro delle proprietà. Durante lo spostamento, gli oggetti si agganciano alle [guide intelligenti](#guide-intelligenti) e a una griglia invisibile; tenere premuto il tasto *Ctrl* durante il trascinamento per disattivare questo aggancio.

## Guide intelligenti

Mentre si spostano o si ridimensionano gli elementi di una diapositiva, Quiz Studio mostra le guide intelligenti: linee rosse che indicano quando gli elementi sono allineati, e l’elemento si aggancia in posizione non appena si avvicina. In questo modo è facile creare diapositive ordinate e coerenti senza misurare nulla.

![Guide intelligenti durante lo spostamento di una risposta](../../assets/images/smart-guides-spacing.webp){ loading=lazy }

- **Allineamento dei bordi**: compare una linea rossa tratteggiata quando un bordo dell’elemento è allineato con il bordo di un altro elemento o con il bordo della diapositiva. Piccole croci rosse contrassegnano gli elementi allineati.
- **Allineamento dei centri**: compare una linea rossa tratto-punto quando il centro dell’elemento è allineato con il centro di un altro elemento o con il centro della diapositiva.
- **Spaziatura uguale**: quando l’elemento si trova alla stessa distanza dall’elemento sopra (o prima) e da quello sotto (o dopo), oppure alla stessa distanza che separa altri elementi della stessa riga o colonna, in ogni spazio uguale compaiono frecce con la distanza in pixel. Nell’immagine qui sopra, tutte e quattro le risposte distano 20 pixel l’una dall’altra.
- **Dimensione uguale**: durante il ridimensionamento di un elemento, questo si aggancia alla larghezza o all’altezza di un altro elemento della diapositiva, e su ogni elemento con quella dimensione compare un indicatore di dimensione.

![Guide intelligenti durante il ridimensionamento di una risposta](../../assets/images/smart-guides-size.webp){ loading=lazy }

Durante il trascinamento, una copia semitrasparente dell’elemento mostra dove verrà posizionato, e una piccola etichetta mostra la sua posizione (X e Y) oppure, durante il ridimensionamento, la sua dimensione, in pixel della diapositiva. Le guide intelligenti funzionano anche quando si spostano insieme più elementi selezionati.

- Tenere premuto il tasto *Ctrl* durante il trascinamento per posizionare un elemento liberamente, senza guide intelligenti né griglia.
- Premere *Esc* durante il trascinamento per annullare lo spostamento e lasciare l’elemento dov’era.

Per disattivare (o riattivare) le guide intelligenti, fare clic con il tasto destro sullo sfondo della diapositiva e fare clic su ‘Smart guides’. Quiz Studio ricorda questa impostazione. Gli elementi si agganciano quindi solo alla griglia invisibile.

![Guide intelligenti nel menu contestuale della diapositiva](../../assets/images/smart-guides-menu.webp){ width="200" loading=lazy }

!!! tip
    Per allineare più elementi in un colpo solo, selezionarli e usare gli [strumenti di allineamento](../other-functionality/home-alignment-size-order.md) della barra multifunzione HOME.

## Inserire una diapositiva

Per inserire una nuova diapositiva, andare al menu INSERT e scegliere uno dei layout predefiniti nella sezione ‘Quiz Slides’. I riquadri blu scuro rappresentano i segnaposto per l’inserimento di un’immagine o di un video.

![](../../assets/images/image13.webp){ loading=lazy }

Scegliendo i layout nella riga inferiore è possibile inserire rispettivamente un Modulo Gioco, un Tabellone Trivia, un Trivia Ladder, un gioco Trivia Feud o un round di Bingo.

È anche possibile cambiare il layout di una diapositiva esistente dal menu DESIGN facendo clic sulla freccia dell’elenco a discesa nella sezione ‘Change Layout’. Compare lo stesso elenco a discesa mostrato sopra, che consente di scegliere un nuovo layout. Gli elementi del layout attuale che si adattano al nuovo layout verranno copiati. Ad esempio, passando da un layout con una domanda, un’immagine e tre risposte a un layout con una domanda, un’immagine e quattro risposte, l’immagine, la domanda e le tre risposte verranno tutte copiate nel nuovo layout.
