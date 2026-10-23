# Test e debug

QuizXpress dispone di una console di script, simile alla console di un browser web. Mostra ciò che lo script scrive con `console.log()` e ogni errore di uno script, con la diapositiva, la riga e la colonna in cui si è verificato.

## Scrivere nella console

```javascript
console.log('Slide ' + (slide.slideNumber + 1) + ': ' + slide.question);
console.warn('No music file set');
console.error('Something went wrong');
```

`console.log()`, `console.info()`, `console.warn()` e `console.error()` accettano un numero qualsiasi di valori, anche oggetti e array. Avvisi ed errori vengono conteggiati separatamente, in modo da risaltare.

!!! tip
    Usare `console.log()` al posto di `alert()`. `alert()` mostra una finestra di messaggio che blocca l'intero quiz finché qualcuno non la chiude.

## In Quiz Studio

La console si trova sotto l'editor di script. Fare clic su 'Test' per eseguire lo script: il suo output appare nella console, seguito da 'Test run finished'. Quando lo script fallisce, la console mostra l'errore e l'editor evidenzia la riga. Fare doppio clic su un messaggio per passare alla sua riga nello script.

- 'Clear' svuota la console, 'Copy' copia tutti i messaggi, ad esempio per chiedere aiuto a un assistente IA.
- 'Errors' e 'Warnings' indicano quanti ce ne sono.
- I messaggi che si ripetono, ad esempio quelli di un timer, vengono raggruppati in una sola riga con un contatore.

## Durante uno show

Un errore di script non interrompe mai lo show: QuizXpress lo segnala e prosegue. La console di script di QuizXpress Director mostra cosa hanno fatto gli script. Non viene mai mostrata sullo schermo proiettato.

Non appena uno script scrive nella console o fallisce, il Director mostra un pulsante 'Script' tra i pulsanti dei comandi, con il numero di errori. Fare clic sul pulsante per aprire la console di script.

La visibilità della console è un'opzione. Fare clic con il pulsante destro del mouse sui pulsanti dei comandi del Director e scegliere 'Script errors':

| Opzione | Cosa fa |
|---|---|
| 'Automatic (open the console when testing from Quiz Studio)' | Quando si testa il quiz da Quiz Studio, la console si apre al primo errore. In uno show reale compare solo il pulsante. È l'impostazione predefinita. |
| 'Show a button with the number of errors' | Solo il pulsante. |
| 'Open the console on the first error' | La console si apre al primo errore, anche in uno show reale. |
| 'Do not show' | Né pulsante né console. |

'Open script console' nello stesso menu apre la console in qualsiasi momento.

!!! tip
    La console è anche un buon posto per le informazioni destinate al conduttore del quiz. L'esempio [Domande dal web](examples.md#domande-dal-web) scrive nella console la domanda scaricata, con la risposta corretta contrassegnata.
