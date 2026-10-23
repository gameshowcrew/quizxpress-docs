# Condividere, aggiornare e risolvere i problemi di uno skin personalizzato

## Condividere uno skin con un altro computer

Uno skin personalizzato completo è composto da due elementi, entrambi nella cartella dati `%appdata%\QuizXpress`:

- `skin.config`
- la cartella `Skins\<your skin>` con le relative immagini

Copiare entrambi nella cartella dati dell'altro computer e selezionare lì lo skin in Quiz Setup. Se si è usato il `dir="Skins\<your skin>"` relativo come descritto in [Creare uno skin personalizzato](creating-a-custom-skin.md#passaggio-4-aggiungere-la-definizione-dello-skin), non occorre modificare nulla. Anche i tipi di carattere usati dallo skin devono essere installati sull'altro computer.

## Dopo un aggiornamento di QuizXpress

Un aggiornamento sostituisce il `skin.config` installato, ma non tocca mai la propria copia né la cartella del proprio skin, quindi lo skin continua a funzionare. Tuttavia, poiché uno skin 'User.' legge solo la propria copia, gli skin integrati da cui eredita restano come erano al momento della copia. Le nuove impostazioni e i miglioramenti che un aggiornamento aggiunge agli skin integrati non vengono recepiti dal proprio skin.

Per aggiornare il proprio skin dopo un aggiornamento:

1. Copiare l'elemento `<skin>…</skin>` dal proprio `skin.config` in un luogo sicuro, ad esempio un file di testo accanto ad esso.
2. Copiare il nuovo `skin.config` dalla cartella di installazione nella cartella dati, sostituendo la propria copia.
3. Incollare di nuovo l'elemento `<skin>` subito sopra `</skins>` (e aggiungere di nuovo `hidden="true"` agli skin integrati, se lo si era fatto).

La cartella dello skin con le immagini non richiede modifiche.

## Risoluzione dei problemi

| Sintomo | Causa e soluzione |
|---|---|
| Il mio skin non compare in Quiz Setup. | Verificare di aver modificato la copia in `%appdata%\QuizXpress` (non il file installato), che sia salvata, che lo skin non abbia `hidden="true"` e di aver riavviato Quiz Setup. |
| QuizXpress Live mostra un errore relativo al file dello skin e non si avvia. | Il messaggio indica che cosa non va. Cause comuni: un errore XML (virgolette o `/>` mancanti, una `&` che dovrebbe essere scritta come `&amp;`), un 'parent' che non corrisponde al 'name' di uno skin esistente, o un valore non valido (per gli attributi con un insieme fisso di valori, il messaggio elenca i valori consentiti). Correggere il file e riavviare. |
| Il mio skin è selezionato, ma il quiz ha l'aspetto di uno skin integrato. | Gli skin personalizzati non sono disponibili nell'edizione Home. In caso contrario, verificare di non aver modificato il 'name' dello skin dopo averlo selezionato in Quiz Setup; se è così, selezionarlo di nuovo. |
| Un'impostazione non ha effetto. | Controllare l'ortografia dei nomi di elementi e attributi rispetto allo skin radice (distinguono tra maiuscole e minuscole) e verificare che l'elemento si trovi all'interno del proprio elemento `<skin>`. Riavviare il quiz dopo il salvataggio. |
| La mia immagine non viene mostrata. | Il file non è stato trovato o non è leggibile. Controllare il nome del file (compresa l'estensione) e il 'dir' dello skin. L'errore viene scritto nel file di log di QuizXpress come "Skin image … not found, please check skin.config". |
