# Comprimere e decomprimere un quiz

Quando si creano quiz di grandi dimensioni con molti contenuti multimediali, come frammenti video e audio, il file del quiz può facilmente diventare grande e scomodo da gestire durante la fase di modifica, e può esaurire la memoria interna del PC. Per ovviare a questo problema, QuizXpress consente di mantenere i file multimediali esterni (collegati). Ciò va bene mentre si costruisce il quiz, ma quando il quiz deve essere spostato su un altro PC o consegnato a qualcun altro, tutti i file collegati devono accompagnarlo, e dimenticarne uno causa problemi durante lo spettacolo.

La funzione ‘Pack’ risolve il problema: salva una copia del quiz con tutti i suoni e i video al suo interno, come un unico file da portare su un altro computer. Può anche rendere quel file molto più piccolo, riducendo ogni suono e video alla parte effettivamente riprodotta e comprimendoli. Il quiz che si sta modificando non viene mai cambiato: la compressione scrive sempre un nuovo file.

## Comprimere un quiz

1. Salvare prima il quiz. Un quiz che non è mai stato salvato non può essere compresso.
2. Premere F1 per accedere al menu backstage e fare clic su ‘Pack’.
3. Controllare il nome del file in ‘Save as’. Per impostazione predefinita il quiz compresso viene salvato accanto al quiz, con ‘(packed)’ aggiunto al nome. Fare clic su ‘Browse...’ per scegliere un'altra posizione o un altro nome.
4. Scegliere le opzioni (vedere sotto) e fare clic su ‘Pack’.

![La finestra di dialogo Pack quiz](../../assets/images/studio-pack-dialog.webp){ loading=lazy }

L'elenco mostra ogni suono e video del quiz: la diapositiva in cui si trova, se è incorporato o collegato, la sua dimensione, la parte riprodotta (‘Plays’) e, in ‘Result’, ciò che la compressione farà con esso, ad esempio ‘Trim to 1:19–9:54’.

Durante la compressione, l'avanzamento viene mostrato in basso e ogni riga indica a che punto si trova. È possibile tenere d'occhio il risultato per ogni suono o video man mano che arriva. Fare clic su ‘Cancel’ per interrompere: in tal caso non viene salvato nulla.

![Compressione in corso](../../assets/images/studio-pack-progress.webp){ loading=lazy }

Al termine, una barra verde mostra quanto tempo è stato necessario e quanto era grande il quiz prima e dopo la compressione. Fare clic su ‘Show in folder’ per aprire la cartella con il quiz compresso.

![Il risultato della compressione](../../assets/images/studio-pack-done.webp){ loading=lazy }

## Ritagliare suoni e video

Spesso durante il quiz viene riprodotta solo una piccola parte di una canzone o di un videoclip, ad esempio 20 secondi di una canzone di 4 minuti. Con ‘Trim to the part that is played’ (separatamente per ‘Sounds’ e ‘Videos’), il quiz compresso conserva solo quella parte. Questo può far risparmiare molto spazio, soprattutto nei round musicali e nei bingo musicali.

- La parte conservata va da ‘Start’ a ‘End’ del suono o del video, e include la parte ‘Replay’ quando il suono o il video viene riprodotto di nuovo dopo la risposta.
- ‘Margin’ aggiunge alcuni secondi prima e dopo quella parte (1 secondo per impostazione predefinita), in modo da avere un po' di margine se in seguito si desidera modificare i tempi.
- I tempi di inizio, fine e riproduzione ripetuta nel quiz compresso vengono regolati automaticamente, quindi il quiz viene riprodotto esattamente come prima.
- Un suono o un video che viene riprodotto fino alla fine mantiene la sua fine. Un video in loop che viene riprodotto fino alla fine mantiene anche il suo inizio, perché ricomincia dall'inizio del file.
- I video di sfondo vengono ritagliati allo stesso modo degli altri video.
- Quando viene riprodotto (quasi) l'intero file, non c'è nulla da ritagliare e il file resta com'è.

!!! note
    Nel quiz compresso non è possibile spostare l'inizio di un suono o di un video ritagliato più indietro della parte conservata. Se si desidera comunque modificare molto i tempi, farlo nel quiz originale e comprimerlo di nuovo.

## Comprimere suoni e video

Con ‘Format’ si sceglie come vengono memorizzati i suoni e i video nel quiz compresso:

| Suoni | Che cosa fa |
|---|---|
| ‘Keep the format’ | I suoni restano come sono. Il ritaglio li taglia senza convertirli, quindi non c'è perdita di qualità. |
| ‘MP3, high quality (about 190 kbps)’ | Converte i suoni in MP3. In questo modo i file WAV diventano molto più piccoli. |
| ‘MP3, compact (about 130 kbps)’ | Converte i suoni in un MP3 più piccolo, comunque adatto alla riproduzione in sala. |

| Video | Che cosa fa |
|---|---|
| ‘Keep the video (cut at keyframes)’ | I video restano come sono, senza perdita di qualità. Un video ritagliato inizia quindi dal fotogramma chiave più vicino prima del taglio, al massimo qualche secondo prima; i tempi vengono regolati di conseguenza. |
| ‘H.264, high quality’ | Converte i video in MP4 (H.264), che viene riprodotto ovunque ed è di solito molto più piccolo. |
| ‘H.264, compact’ | Converte i video in un MP4 più piccolo, con una certa perdita di dettaglio. |

Accanto al formato video è possibile limitare la dimensione dell'immagine a ‘Up to 1080p’ o ‘Up to 720p’. I video con un'immagine più grande vengono ridotti, il che fa risparmiare molto spazio per i video 4K.

QuizXpress converte un file solo quando ne vale la pena: un MP3 o un video già compatto viene lasciato com'è (‘Already compact’) e un risultato che non sarebbe più piccolo dell'originale non viene utilizzato (‘Would not get smaller’). Ciò mantiene anche veloce la compressione.

Le scelte effettuate vengono ricordate per la volta successiva in cui si comprime un quiz.

## Installare ffmpeg

Il ritaglio e la compressione vengono eseguiti con ffmpeg, uno strumento gratuito che non fa parte di QuizXpress. Sotto le opzioni, la finestra di dialogo mostra quale versione di ffmpeg utilizza. Quando ffmpeg non è installato, una barra nella parte superiore della finestra di dialogo offre tre modi per ottenerlo:

![La finestra di dialogo Pack senza ffmpeg](../../assets/images/studio-pack-no-ffmpeg.webp){ loading=lazy }

- ‘Install with winget’ installa ffmpeg con il gestore di pacchetti di Windows. Si apre una finestra della console; seguirla e accettare i termini di winget quando li richiede. Quando la finestra si chiude, QuizXpress trova ffmpeg da solo e il ritaglio e la compressione diventano disponibili.
- ‘Download’ apre la pagina di download di ffmpeg nel browser. Estrarre il download in una cartella a scelta.
- ‘Locate ffmpeg.exe...’ consente di indicare un file ffmpeg.exe già in proprio possesso, ad esempio nella cartella ‘bin’ del download. Il file ffprobe.exe fornito insieme deve trovarsi nella stessa cartella.

Anche senza ffmpeg è possibile comprimere un quiz: i file multimediali collegati vengono quindi incorporati così come sono.

## File mancanti

Quando un file audio o video collegato non viene trovato, la sua riga viene mostrata in rosso (‘File not found, stays linked’) e un avviso in basso indica quanti file mancano. È comunque possibile comprimere il quiz, ma quei file restano collegati e mancheranno su un altro computer. Per includerli, individuare prima i file mancanti nel quiz e comprimere di nuovo.

## Decomprimere un quiz

È anche possibile decomprimere un file di quiz compresso in precedenza. Ciò estrae tutti i contenuti multimediali (audio/video) in una cartella locale e collega gli elementi multimediali del quiz ai file locali. Questo accelera i tempi di caricamento del quiz e riduce l'utilizzo di memoria nel lettore di quiz. Il suo utilizzo principale è evitare problemi con file di quiz enormi (~1,5 GB o più). Per decomprimere un quiz, premere F1 per accedere al menu backstage e fare clic su ‘Unpack’.
