# Skinning

L'aspetto del quiz player di QuizXpress, QuizXpress Live, può essere modificato completamente in base alle proprie preferenze o alla propria immagine coordinata creando uno 'skin' personalizzato. QuizXpress include cinque skin integrati (QuizXpress Classic, QuizXpress 2022, Dark Theme, TV Show e Techno), selezionabili in Quiz Setup nella scheda 'Screens', nella sezione 'Appearance'. Vedere [Personalizzare l'aspetto](../../setup/customizing-the-look-the-screens-tab-page.md).

Creare il proprio skin si riduce a quattro operazioni:

1. copiare il file standard `skin.config` nella cartella dati di QuizXpress;
2. aggiungere la propria definizione di skin che eredita da uno degli skin integrati;
3. sovrascrivere solo le impostazioni che si desidera modificare;
4. inserire la propria grafica (immagini PNG) in una cartella appartenente al proprio skin.

Questa pagina spiega come funzionano gli skin. [Creare uno skin personalizzato](creating-a-custom-skin.md) guida passo dopo passo, e [Condividere, aggiornare e risolvere i problemi](maintaining-a-custom-skin.md) tratta ciò che viene dopo.

Le singole impostazioni (colori, tipi di carattere, immagini, dimensioni) non sono descritte in questo manuale: ciascuna è documentata in un commento posto direttamente sopra il rispettivo elemento nello stesso `skin.config`.

!!! warning "Not in the Home edition"
    Gli skin personalizzati non sono disponibili nell'edizione Home di QuizXpress. Nell'edizione Home il quiz player usa sempre gli skin integrati, anche quando è selezionato uno skin 'User.'.

## Il file skin.config

Gran parte dell'aspetto del quiz player è definita in un file di testo XML denominato `skin.config`. Ogni skin selezionabile in Quiz Setup è un elemento `<skin>` di quel file. Ogni skin contiene elementi per le varie parti dello show, come `<welcomescreen>`, `<quizscreen>`, `<scorescreen>`, `<infopanel>` o `<pinindicator>`, e i loro attributi contengono colori, tipi di carattere, immagini e dimensioni.

![La struttura di primo livello di skin.config, con gli skin compressi](../../assets/images/skinning-skin-config-structure.webp){ loading=lazy }

Ogni elemento è documentato nel commento (mostrato in verde in Notepad++) posto direttamente sopra di esso. Il commento all'inizio del file spiega come inserire i valori: colori (nomi, RGB, ARGB o esadecimale come `#7A6699`), tipi di carattere (`"Arial Bold"` o `"Arial Bold, 22"`), rettangoli, valori booleani e posizioni 3D.

![Ogni elemento è documentato direttamente sopra, qui la schermata di benvenuto](../../assets/images/skinning-skin-config-documentation.webp){ loading=lazy }

Per modificare il file si consiglia [Notepad++](https://notepad-plus-plus.org/), un editor gratuito con evidenziazione della sintassi XML. Va bene qualsiasi editor di testo semplice, ma non usare mai un programma di videoscrittura.

## Il file installato e la propria copia

QuizXpress conosce due posizioni per `skin.config`:

| Posizione | Che cos'è |
|---|---|
| `C:\Program Files (x86)\Game Show Crew\QuizXpress\skin.config` | Gli skin integrati. **Non modificare questo file**: ogni aggiornamento di QuizXpress lo sostituisce. |
| `%appdata%\QuizXpress\skin.config` (ad esempio `C:\Users\<you>\AppData\Roaming\QuizXpress`) | La propria copia. Quiz Setup elenca ogni skin di questo file con il prefisso 'User.', in modo che non siano mai in conflitto con gli skin integrati. |

!!! note
    Quando si seleziona uno skin 'User.', il quiz player legge **solo la propria copia** di `skin.config`, compresi gli skin integrati da cui il proprio skin eredita. Per questo si copia l'intero file anziché scrivere un file contenente solo il proprio skin. Vedere [Dopo un aggiornamento di QuizXpress](maintaining-a-custom-skin.md#dopo-un-aggiornamento-di-quizxpress) per le implicazioni in caso di aggiornamento.

## Ereditarietà: modificare solo ciò che è diverso

Uno skin può indicare uno skin 'parent' (genitore). Quando il quiz player carica uno skin, carica prima il genitore completo (e il genitore del genitore, e così via), quindi applica sopra gli elementi dello skin stesso. Questo avviene per singolo attributo: un attributo incluso sostituisce il valore ereditato, un attributo omesso mantiene il valore ereditato. Anche il valore `default` mantiene il valore ereditato.

Gli skin integrati funzionano già in questo modo. Techno eredita da Dark Theme, che eredita da QuizXpress Classic:

```text
QuizXpress (QuizXpress Classic)   - the root skin, defines every setting
├── QuizXpress 2022
├── TVShow (TV Show)
└── DarkMode (Dark Theme)
    └── Techno
```

Scegliere quindi come genitore del proprio skin lo skin integrato più vicino a ciò che si desidera, e inserire nel proprio skin solo gli elementi e gli attributi che si vogliono modificare. In questo modo resta piccolo e facile da mantenere.

## Dove il quiz player cerca le immagini

Le immagini e le altre risorse sono referenziate in `skin.config` tramite il nome del file, ad esempio `background-image="strip.png"`. Ogni skin ha un attributo 'dir' che indica la sua cartella delle risorse. Il quiz player cerca un'immagine in questo ordine e usa il primo file trovato:

1. Se l'attributo contiene un percorso completo (`C:\...\logo.png`): esattamente quel file.
2. La cartella delle risorse del proprio skin.
3. La cartella delle risorse del suo genitore, poi del nonno, e così via.
4. La cartella predefinita generale `Data\IQ\default` nella cartella di installazione.

Un 'dir' può essere un percorso completo o relativo. Un 'dir' relativo viene cercato prima sotto `Data\IQ` nella cartella di installazione (qui gli skin integrati conservano le proprie immagini, ad esempio `Data\IQ\QuizXpress 2022`), poi sotto la propria cartella dati `%appdata%\QuizXpress`.

Il risultato pratico: **un'immagine inserita nella cartella del proprio skin con lo stesso nome di file di un'immagine dello skin genitore la sostituisce automaticamente**, e ogni immagine non sostituita proviene comunque dal genitore.
