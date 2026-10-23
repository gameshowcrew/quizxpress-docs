# Creare uno skin personalizzato

Nei passaggi seguenti creiamo uno skin denominato 'QuizXpress 2023', basato sullo skin integrato 'QuizXpress 2022'. Sostituire i nomi con i propri. Se non lo si è ancora letto, [Skinning](index.md) spiega come funzionano gli skin.

## Passaggio 1: aprire la cartella dati di QuizXpress

In QuizXpress Studio, passare alla scheda 'HOME', aprire il menu 'Advanced' e scegliere 'Browse Datafolder'. Si apre una finestra di Esplora risorse di Windows sulla cartella dati. In alternativa, è possibile digitare `%appdata%\QuizXpress` nella barra degli indirizzi di Esplora risorse.

![Scheda HOME, menu Advanced, Browse Datafolder](../../assets/images/skinning-browse-datafolder.webp){ width="400" loading=lazy }

## Passaggio 2: copiare skin.config nella cartella dati

Copiare `skin.config` dalla cartella di installazione (`C:\Program Files (x86)\Game Show Crew\QuizXpress`) nella cartella dati. Copiarlo, non spostarlo.

Aprire Quiz Setup, passare alla scheda 'Screens' e aprire l'elenco 'Selected skin' nella sezione 'Appearance'. Ogni skin integrato compare ora una seconda volta con il prefisso 'User.': queste voci provengono dalla propria copia.

![Gli skin della propria copia compaiono con il prefisso User.](../../assets/images/skinning-user-skins-in-quiz-setup.webp){ loading=lazy }

!!! tip
    Per mantenere l'elenco ordinato, aggiungere `hidden="true"` agli elementi `<skin>` degli skin integrati nella **propria copia**. Gli skin nascosti non compaiono più in Quiz Setup, ma continuano a funzionare come genitore del proprio skin.

## Passaggio 3: creare una cartella per la grafica

Nella cartella dati, creare una cartella `Skins` e al suo interno una cartella con il nome del proprio skin: `%appdata%\QuizXpress\Skins\QuizXpress 2023`. Per ora lasciarla vuota.

## Passaggio 4: aggiungere la definizione dello skin

Aprire nel proprio editor il `skin.config` copiato (quello nella cartella dati). In fondo al file, subito sopra il tag di chiusura `</skins>`, aggiungere:

```xml
<skin name="QuizXpress 2023"
      displayname="QuizXpress 2023"
      dir="Skins\QuizXpress 2023"
      parent="QuizXpress 2022">

</skin>
```

Gli attributi dell'elemento `<skin>`:

| Attributo | Significato |
|---|---|
| `name` | Nome interno. Deve essere univoco nel file; è il nome che gli altri skin usano come 'parent'. |
| `displayname` | Il nome mostrato in Quiz Setup (con il prefisso 'User.'). Facoltativo; se omesso, viene mostrato il 'name'. |
| `dir` | La cartella delle risorse dello skin. Usare il percorso relativo `Skins\<your skin>`: viene cercato nella cartella dati e funziona senza modifiche su un altro computer o account utente. Funziona anche un percorso completo. |
| `parent` | Il 'name' (non il nome visualizzato) dello skin da cui ereditare, ad esempio `QuizXpress 2022`, `DarkMode`, `TVShow` o `Techno`. Facoltativo, ma vivamente consigliato. |
| `hidden` | `true` nasconde lo skin in Quiz Setup. Facoltativo. |

Salvare il file.

## Passaggio 5: selezionare lo skin in Quiz Setup

Riaprire Quiz Setup (legge l'elenco degli skin all'avvio), selezionare 'User.QuizXpress 2023' nell'elenco 'Selected skin' e salvare le impostazioni. D'ora in poi il quiz player usa il proprio skin. Poiché lo skin è ancora vuoto, ha esattamente lo stesso aspetto del suo genitore.

![Selezione del proprio skin in Quiz Setup](../../assets/images/skinning-select-custom-skin.webp){ width="400" loading=lazy }

## Passaggio 6: sovrascrivere le impostazioni

Apportare ora le modifiche che definiscono il proprio skin. Individuare l'elemento da modificare nello skin genitore, oppure in 'QuizXpress' (lo skin radice, che contiene ogni impostazione con la relativa documentazione), copiarlo nel proprio skin e conservare solo gli attributi che si modificano.

Ad esempio, vogliamo uno sfondo viola per l'indicatore del PIN (il pannello che mostra il PIN della partita durante il quiz). Nello skin radice troviamo:

```xml
<pinindicator
    background-color="#01539F"
    text-font-family="default"
    pin-font-family="default"
/>
```

Vogliamo cambiare solo il colore di sfondo, quindi aggiungiamo al nostro skin soltanto quell'attributo:

```xml
<skin name="QuizXpress 2023" displayname="QuizXpress 2023"
      dir="Skins\QuizXpress 2023" parent="QuizXpress 2022">

    <pinindicator background-color="Purple" />

</skin>
```

I tipi di carattere mantengono i valori ereditati dal genitore. Avviare un quiz: l'indicatore del PIN è ora viola:

![L'indicatore del PIN con il nuovo colore di sfondo](../../assets/images/skinning-pin-indicator-purple.webp){ width="220" loading=lazy }

Seguire lo stesso schema per qualsiasi altra modifica: aggiungere l'elemento una sola volta al proprio skin e inserirvi tutti gli attributi che si modificano per quell'elemento.

!!! note
    Il quiz player legge `skin.config` all'avvio. Dopo aver salvato una modifica, interrompere il quiz e riavviarlo per vedere il risultato.

## Passaggio 7: sostituire le immagini

Le immagini integrate di uno skin si trovano nella sua cartella sotto `Data\IQ` nella cartella di installazione. Le immagini di QuizXpress 2022, il genitore del nostro esempio, si trovano in `Data\IQ\QuizXpress 2022`:

![Le risorse grafiche dello skin QuizXpress 2022](../../assets/images/skinning-skin-assets-folder.webp){ loading=lazy }

Ci sono due modi per usare la propria grafica.

**Sostituire un'immagine in base al nome.** È il metodo più semplice e non richiede alcuna modifica a `skin.config`:

- Individuare l'immagine da modificare nella cartella del genitore. Se non c'è, cercare nella cartella del nonno, ad esempio `Data\IQ\QuizXpress`.
- Copiarla nella cartella del proprio skin, `%appdata%\QuizXpress\Skins\QuizXpress 2023`, mantenendo il nome del file.
- Modificare la copia con il proprio editor di immagini preferito. Mantenere le stesse dimensioni in pixel e salvarla in formato PNG (con trasparenza dove l'originale la prevede).

Poiché la cartella del proprio skin viene esaminata prima di quella del genitore, la propria immagine viene usata automaticamente.

**Fare riferimento a un'immagine in modo esplicito.** Se si preferiscono nomi di file propri, impostare l'attributo nel proprio skin. Ad esempio, per lo sfondo del pannello informativo:

```xml
<infopanel background-image="infopanel_bg.png" />
```

Il quiz player cerca ora `infopanel_bg.png` nella cartella del proprio skin. È anche possibile inserire un percorso completo. Per tornare all'immagine integrata, usare il valore `default`.

Avviare un quiz e verificare che le proprie immagini vengano mostrate. Se un'immagine non viene trovata, il quiz player mostra l'immagine integrata, oppure nessuna: vedere [Risoluzione dei problemi](maintaining-a-custom-skin.md#risoluzione-dei-problemi).
