# Forme

È possibile aggiungere alla diapositiva forme o immagini arbitrarie. Le forme possono essere utilizzate per vari scopi, ad esempio:

- Si può inserire una grande freccia per evidenziare un dettaglio di un'immagine sulla quale si interroga il pubblico. Impostando l'opzione Visibility su ‘Visible after answers’, la forma diventa visibile solo al termine del conto alla rovescia della domanda.

- Si può nascondere parte di un'immagine su una diapositiva sovrapponendovi una forma. Impostando l'opzione Visibility su ‘Hide after answers’, la forma viene nascosta al termine del conto alla rovescia, rivelando ciò che si trova dietro.

Per inserire una forma, utilizzare il comando *Insert->Shape* nel riquadro delle attività (questo comando diventa visibile dopo aver selezionato lo sfondo della diapositiva). Viene quindi richiesto di selezionare un file di forma. Per impostazione predefinita, la finestra di selezione file filtra i file *\*.emf* o *\*.wmf*. Questi tipi di file utilizzano un formato « vettoriale » (a differenza dei formati bitmap) che mantiene un aspetto nitido anche dopo il ridimensionamento. Le forme possono anche utilizzare come origine qualsiasi formato di immagine supportato (png, jpg, bmp, ecc.); è possibile selezionare questi altri formati nella finestra di selezione file. Si noti che i file immagine non si ridimensionano bene e il risultato può apparire pixelato se vengono ingranditi.

L'elemento forma ha le seguenti proprietà:

| Property       | Description                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Picture        | L'immagine di origine della forma. Il pulsante … consente di selezionare un'altra origine                                                                                                       |
| Rotation Angle | L'angolo di rotazione facoltativo della forma                                                                                                                                                   |
| Transparency   | Trasparenza della forma                                                                                                                                                                         |
| Visibility     | Condizione di visibilità. Può essere impostata su ‘Always visible’, ‘Visible after answers’ (nasconde la forma fino al termine della domanda) o ‘Hide after answers’ (mostra la forma fino al termine della domanda). |

Per eliminare una forma, selezionarla e premere il tasto Canc. QuizXpress include alcune forme di esempio predefinite. È anche possibile creare forme personalizzate, ad esempio con Microsoft PowerPoint, salvando una forma di PowerPoint come immagine (fare clic con il pulsante destro del mouse sulla forma, selezionare ‘Save as picture’ e scegliere *wmf* o *emf* come formato di file).

## Forme di testo

È possibile aggiungere elementi di testo alle diapositive del quiz e controllarne la visibilità proprio come per le forme immagine. Un esempio di utilizzo di un elemento di testo è mostrare la risposta corretta a una domanda aperta (dopo che alla domanda è stata data risposta ed è stata giudicata), oppure fornire suggerimenti durante la domanda. Tramite la griglia delle proprietà è possibile impostare alcune proprietà più avanzate, come il colore del pannello di sfondo del testo e il raggio degli angoli, per creare elementi visivi accattivanti (si noti che queste proprietà non sono disponibili nella barra multifunzione). Le forme di testo hanno le seguenti proprietà aggiuntive:

| Property                | Description                                                                           |
|-------------------------|---------------------------------------------------------------------------------------|
| Background transparency | Trasparenza del pannello di sfondo. Per impostazione predefinita lo sfondo è completamente trasparente. |
| Border color            | Colore del bordo attorno al pannello                                                  |
| Border width            | Spessore della linea attorno al pannello                                              |
| Corner radius           | Raggio degli angoli del pannello di sfondo                                            |
| Gradient                | Riempimento sfumato dello sfondo                                                      |
| Alignment               | Allineamento del testo (sinistra, centro, destra)                                     |
| Drop shadow             | Ombra esterna del testo                                                               |
| Shadow color            | Colore dell'ombra esterna                                                             |
| Text                    | Il testo stesso                                                                       |
| Text color              | Colore del testo                                                                      |
| Font                    | Carattere utilizzato per disegnare il testo                                           |

Con queste proprietà è possibile creare pannelli di testo come questo:

![](../../assets/images/image196.webp){ width="376" loading=lazy }

### Simboli di testo

Con le forme di testo è possibile creare schermate personalizzate che contengono dati noti solo durante lo svolgimento dello show. A tale scopo, i campi di testo (forme) di QuizXpress possono contenere « simboli » predefiniti. Quando lo show viene eseguito davanti al pubblico, questi simboli vengono sostituiti dai valori corrispondenti.

È possibile utilizzare, tra l'altro, nomi dei giocatori, punteggi, risposte, tempi di risposta, codice PIN, indice della diapositiva, note della diapositiva, numero di risposte corrette e errate e molto altro.

Di seguito sono riportati alcuni esempi di schermate con un design personalizzato. La parte sinistra mostra l'aspetto della diapositiva in QuizXpress Studio. La parte destra mostra l'aspetto che la diapositiva potrebbe avere durante una partita.

| ![](../../assets/images/image197.webp){ loading=lazy } | ![](../../assets/images/image198.webp){ loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ![](../../assets/images/image199.webp){ loading=lazy }  | ![](../../assets/images/image200.webp){ loading=lazy } |
|                                                                                 |                                                                                 |

Quando si modificano elementi di testo nell'editor di testo (fare doppio clic su un testo o su una forma di testo per aprirlo), un pulsante ‘Insert Symbol’ consente di inserire un simbolo di testo. È anche possibile digitare i simboli manualmente. La finestra di dialogo Insert Symbol elenca tutti i simboli con una spiegazione per ciascuno.

![](../../assets/images/image201.webp){ width="544" loading=lazy }

Alcuni esempi di simboli utilizzabili:

| **\[date\]**        | Data corrente                                       | **\[slide.answer\]**     | Risposta corretta della domanda corrente |
|---------------------|-----------------------------------------------------|--------------------------|------------------------------------|
| **\[time\]**        | Ora corrente                                        | **\[playerX.name\]**     | Nome del giocatore con posizione X |
| **\[pin\]**         | PIN mobile corrente                                 | **\[playerX.score\]**    | Punteggio del giocatore con posizione X |
| **\[url\]**         | URL del server di gioco                             | **\[playerX.lastvote\]** | Ultimo voto                        |
| **\[correct\]**     | N. di giocatori che hanno risposto correttamente dopo la domanda | **\[playerX.time\]**     | Tempo di risposta in millisecondi  |
| **\[incorrect\]**   | N. di giocatori che hanno risposto in modo errato dopo la domanda | **\[playerX.timesec\]**  | Tempo di risposta in secondi       |
| **\[novote\]**      | N. di giocatori che non hanno risposto dopo la domanda | **\[buzzerX.name\]**     | Nome del giocatore con il buzzer X |
| **\[slide.index\]** | Numero della diapositiva della domanda corrente     | **\[buzzerX.score\]**    | Punteggio del giocatore con il buzzer X |
| **\[slide.notes\]** | Note della domanda corrente                         |                          |                                    |

È possibile utilizzare i simboli in qualsiasi elemento di testo. Ad esempio, si può inserire una forma di testo e digitare qualcosa come: « Aprite l'app Smart Buzzer e collegatevi con il codice di gioco: \[pin\] »

I simboli di testo sono un ottimo modo per rendere più dinamiche le diapositive del quiz e, ad esempio, per progettare tabelle punteggi personalizzate.

## Forme temporizzate

È anche possibile mostrare e nascondere forme ed elementi di testo nel tempo impostando le proprietà delle forme temporizzate nella scheda contestuale della barra multifunzione SHAPE TOOLS. Questo consente, ad esempio, di creare un « suggerimento » che compare dopo un certo tempo durante il conto alla rovescia, come mostrato nell'esempio seguente:

![](../../assets/images/image202.webp){ loading=lazy }

In questo esempio, l'elemento di testo con pannello compare dopo che è trascorso il 40% del tempo del conto alla rovescia.

Se si lascia la percentuale ‘Hide at:’ allo 0%, il suggerimento rimane visibile fino alla fine del conto alla rovescia.

In alternativa è possibile, ad esempio, rimuovere nel tempo gli elementi che coprono parti di una foto.
