# Video

QuizXpress supporta anche l'uso di spezzoni video. Gli spezzoni video possono essere usati nelle domande, ma anche, ad esempio, per comunicare un messaggio di marketing al pubblico. Esiste uno speciale formato di diapositiva « video a schermo intero » che riproduce il video selezionato a schermo intero durante lo show.

QuizXpress supporta vari formati di file, ma per riprodurre correttamente i file video è necessario che nel sistema sia installato il CODEC video corretto (un componente di Windows utilizzato per riprodurre in streaming un determinato formato video). Il programma di installazione di QuizXpress aggiunge al sistema il pacchetto di codec LAV. L'ultima versione di tale pacchetto di codec è disponibile qui: <https://github.com/Nevcairiel/LAVFilters/releases>

## Inserire un video

Per aggiungere un video a una domanda, creare prima una nuova domanda con un modello che abbia un segnaposto immagine/video.

| ![](../../assets/images/image211.webp){ width="163" loading=lazy } | ![](../../assets/images/image212.webp){ width="161" loading=lazy } | ![](../../assets/images/image213.webp){ loading=lazy } | Quest'ultimo modello mostra il video a schermo intero. È possibile usarlo anche per mostrare materiale promozionale sulla propria azienda tra una domanda e l'altra! |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

Fare quindi clic con il pulsante destro del mouse sul segnaposto dell'immagine e scegliere ‘Select Video’ dal menu contestuale. Si apre una finestra di dialogo in cui è possibile selezionare uno spezzone video *(\*.avi, \*.wmv, \*.mov, \*.mp4, \*.mpg, \*.mpeg, \*.flv, \*.3gp, \*.webm*).

Proprio come l'audio, un video può essere collegato o incorporato. Incorporare uno spezzone video in un quiz significa che lo spezzone viene inserito nel file del quiz. Collegare uno spezzone video significa che dal file del quiz viene creato un riferimento a un video presente nel file system. In generale, si consiglia di *collegare* i video mentre si sta ancora modificando il quiz. Al termine delle modifiche, è possibile usare la [funzione ‘Pack’](../other-functionality/packing-and-unpacking-a-quiz.md) per riunire tutti i file collegati esternamente in un unico grande file del quiz (max 2 GB). Il packing può anche tagliare i video alla parte riprodotta e comprimerli, mantenendo piccolo il file compresso. Con questo file combinato è facile spostare il quiz su un altro computer senza preoccuparsi delle risorse esterne.

!!! note

    quando si collegano i video, assicurarsi di non rimuoverli dal file system. Quando si copia il quiz su un altro computer, i video devono essere copiati nella stessa cartella del file del quiz in modo che QuizXpress possa trovarli.*

Il contenuto video incorporato non può superare i 30 MB. In generale, cercare di mantenere i video il più piccoli possibile: se la domanda dura solo trenta secondi, è inutile inserire un video di quattro minuti. In tal caso, utilizzare uno strumento di montaggio video per tagliare il video.

## Modificare le proprietà del video

Quando si seleziona un video, diventa visibile la scheda contestuale della barra multifunzione per il video:

![La scheda Video della barra multifunzione](../../assets/images/video-ribbon.webp){ loading=lazy }

Da qui è possibile visualizzare l'anteprima del video, impostare i marcatori di inizio e fine, impostare il volume e cambiare la velocità di riproduzione (si noti che la modifica della velocità di riproduzione potrebbe non funzionare con tutti i tipi di video e dipende dai CODEC utilizzati). È inoltre possibile configurare un effetto che cambia nel tempo. Ad esempio, è possibile usare l'effetto Mosaic per mostrare il video completamente pixelato all'inizio e rivelarne gradualmente i dettagli mentre si pone al pubblico una domanda sul video, con punti decrescenti. È anche possibile riprodurre il video in modalità silenziosa e ripetere lo spezzone in loop fino al termine della domanda. Con ‘Select Picture’ è possibile riportare l'elemento della diapositiva a un'immagine statica.

Con Replay è possibile abilitare la riproduzione ripetuta di una parte del video al termine della domanda (quando viene rivelata la risposta corretta).

## Video in sfondo

Un video può anche essere riprodotto dietro l'intera diapositiva, come sfondo. Un video di sfondo di questo tipo non viene inserito in un segnaposto: fare clic con il pulsante destro del mouse sullo sfondo della diapositiva e scegliere ‘Background video…’, oppure impostare la proprietà ‘Background video’ della diapositiva. Per impostazione predefinita, un video di sfondo viene riprodotto in loop e senza audio. Vedere [Video di sfondo](../backgrounds.md#video-di-sfondo) per tutte le sue impostazioni.

Nella schermata seguente, un video di sfondo è combinato con una forma sovrapposta per creare un effetto TV vecchio stile (una forma con uno schermo trasparente è posizionata sopra il video di sfondo).

![](../../assets/images/image215.webp){ loading=lazy }

!!! note
    Le versioni precedenti avevano una casella ‘Background’ per un video in un segnaposto. Quella casella non c'è più: un video di sfondo ha ora un proprio posto dietro la diapositiva. I video di sfondo nei quiz creati con una versione precedente vengono convertiti automaticamente all'apertura del quiz.

## Combinare un video di sfondo con un video in un segnaposto

Poiché il video di sfondo non usa un segnaposto, una diapositiva può avere entrambi: un video di sfondo in riproduzione dietro la diapositiva e un video (o un'immagine) nel suo segnaposto, che viene riprodotto sopra di esso. Ad esempio, si può usare un'animazione di studio in loop come video di sfondo e lo spezzone di film della domanda nel segnaposto.

![Una diapositiva con un video di sfondo e un video nel suo segnaposto](../../assets/images/background-and-placeholder-video.webp){ loading=lazy }

I due video mantengono ciascuno le proprie impostazioni. Il video nel segnaposto parte dopo la sua pausa introduttiva (‘Intro Pause’) e si mette sempre in pausa e riprende insieme al quiz. Il video di sfondo parte non appena compare la diapositiva e, a meno che non si attivi ‘Sync with quiz’, continua a essere riprodotto. Lasciare il video di sfondo silenzioso (impostazione predefinita) in modo che il suo audio non si mescoli con quello del video nel segnaposto.
