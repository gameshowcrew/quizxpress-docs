# Test con le pulsantiere virtuali

La pulsantiera virtuale (Virtual Keypad) è utile per testare il quiz senza alcuna dipendenza esterna. Si tratta di una pulsantiera software eseguita sullo stesso computer del quiz. È possibile avviare una nuova pulsantiera virtuale (VK) dal menu a discesa External Tools di Studio oppure dal menu Start di Windows, nella sezione QuizXpress. Una volta avviata un'istanza della pulsantiera virtuale, questa inizia a cercare di connettersi a QuizXpress Live. Finché la connessione non riesce, i pulsanti della pulsantiera sono disattivati (grigi).

| ![](../assets/images/image398.webp){ width="107" loading=lazy } | ![](../assets/images/image399.webp){ width="105" loading=lazy } | ![](../assets/images/image400.webp){ width="290" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Connessione in corso                                                            | Connesso                                                                        | Menu contestuale della pulsantiera virtuale                                           |

Una volta connessi, è possibile modificare al volo il numero della pulsantiera con il selettore numerico. Per accedere al menu contestuale, fare clic con il pulsante destro del mouse sullo schermo della pulsantiera. Il menu contestuale offre i comandi seguenti:

| Menu          | Descrizione                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| Properties    | Apre la finestra di dialogo Properties, in cui è possibile vedere l'indirizzo IP del server e la porta utilizzati |
| Clone         | Clona una nuova istanza. L'ID della pulsantiera verrà incrementato                                            |
| Always on Top | Mantiene la pulsantiera davanti a tutte le altre applicazioni                                               |
| Randomizer    | Abilita/disabilita una modalità in cui la pulsantiera invia input casuali per facilitare i test             |
| Exit          | Chiude la pulsantiera virtuale                                                                              |
