# Script

A partire dalla versione 8.5, QuizXpress include un motore JavaScript integrato. Con gli script è possibile creare comportamenti ed elementi di gioco personalizzati che altrimenti non sarebbero possibili. Oltre a tutto ciò che offre il linguaggio JavaScript, uno script può leggere informazioni sulla diapositiva corrente, sui giocatori, sui punteggi e sui buzzer, rispondere agli eventi del quiz, modificare la domanda e i punteggi durante lo show, ottenere dati da internet e comunicare con altre apparecchiature.

Questa sezione spiega come funzionano gli script in QuizXpress. Non insegna JavaScript: sul web c'è molto materiale, e gli assistenti IA aiutano bene a scrivere script. Si presuppone una conoscenza di base della programmazione. Per i dettagli su ciò che il motore supporta esattamente, vedere [Jint](https://github.com/sebastienros/jint), il motore JavaScript utilizzato da QuizXpress.

!!! warning "Usare con cautela"
    Gli script sono destinati agli utenti esperti e non sono necessari per il normale utilizzo di QuizXpress. Uno script può corrompere i punteggi o confondere lo svolgimento del quiz. Un errore in uno script non interrompe mai lo show, ma la parte di script successiva all'errore non viene eseguita. Eseguire test approfonditi prima di usare uno script in uno show dal vivo.

    Non offriamo supporto (gratuito) per la scrittura di script.

## Come viene eseguito uno script

Uno script appartiene a una diapositiva. Quando QuizXpress Live mostra la diapositiva, esegue lo script: prima il codice esterno alle funzioni, poi il gestore `onLoadSlide()`. Finché la diapositiva è visibile, QuizXpress chiama gli altri gestori quando accade qualcosa: parte il conto alla rovescia, una squadra vota, il tempo scade… Quando si lascia la diapositiva, viene eseguito `onUnloadSlide()` e lo script si ferma. Le sue variabili scompaiono e i suoi timer `setInterval()` si fermano.

Per conservare informazioni da una diapositiva alla successiva, o per mostrare un valore sulla diapositiva, usare l'oggetto `qx`: vedere [Lavorare con QuizXpress](working-with-quizxpress.md).

## L'editor di script

Ogni diapositiva ha una proprietà 'Script'. In QuizXpress Studio, fare clic sui tre puntini della proprietà 'Script' per aprire l'editor di script. Quando una diapositiva non ha ancora uno script, l'editor mostra un modello che spiega le basi ed elenca tutti i gestori, commentati (mostrati in verde). Rimuovere il `//` davanti a un gestore per usarlo.

![L'editor di script con il modello predefinito](../../assets/images/js-script-editor-template.webp){ loading=lazy }

I **gestori** sono funzioni con un nome specifico che QuizXpress chiama automaticamente quando accade qualcosa, se esistono nello script. Ad esempio, `onLoadSlide(slide)` viene eseguito quando la diapositiva viene mostrata, e `onVote(player, answer, isCorrect)` viene eseguito ogni volta che una squadra risponde. Il [Riferimento](reference.md#gestori) li elenca tutti.

È possibile inserire codice anche al di fuori dei gestori. Viene eseguito non appena lo script viene caricato, il che è utile per le impostazioni all'inizio dello script e per caricare la musica.

L'editor assiste durante la digitazione:

- **Suggerimenti**: digitare un punto dopo `qx`, `slide` o un giocatore, oppure premere Ctrl+Spazio, e un elenco mostra cosa si può usare, con una breve spiegazione. Tra le parentesi di una funzione, un suggerimento a comparsa mostra i suoi argomenti.
- **Controllo della sintassi**: un errore di battitura, come una parentesi mancante, viene sottolineato con una linea rossa ondulata, e l'errore è mostrato accanto al pulsante 'Test'. Fare clic sull'errore per passare alla sua riga.
- **Console**: sotto l'editor, la console mostra l'output di `console.log()` e gli errori di un'esecuzione di test. Vedere [Test e debug](debugging.md).
- **'Example scripts on GitHub'**, in alto a destra, apre la nostra raccolta di quiz di esempio pronti all'uso con i relativi script.

I pulsanti:

- **'Save'** memorizza lo script nella diapositiva, e quindi nel quiz.
- **'Test'** esegue lo script come fa QuizXpress Live quando mostra la diapositiva: il codice esterno alle funzioni e poi `onLoadSlide()`. Viene eseguito in una sandbox con questa diapositiva e dieci squadre di esempio, e non tocca il quiz. Gli altri gestori non vengono chiamati, perché nella sandbox non accade nulla.

![Test di uno script: l'output appare nella console](../../assets/images/js-test-console.webp){ loading=lazy }

## Passi successivi

- [Lavorare con QuizXpress](working-with-quizxpress.md): l'oggetto `qx`, la condivisione di dati tra diapositive, la visualizzazione dei valori dello script su una diapositiva, e la modifica della domanda e dei punteggi.
- [Test e debug](debugging.md): la console in Studio e nel Director.
- [Riferimento](reference.md): tutti i gestori, oggetti, proprietà e funzioni disponibili per gli script.
- [Esempi](examples.md): script pronti all'uso e quiz di esempio.
