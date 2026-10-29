# MIDI e DMX

QuizXpress può controllare dispositivi esterni tramite MIDI. Un esempio tipico è un controller luci DMX: quando nel quiz accade qualcosa, come una risposta corretta o la fine del conto alla rovescia, QuizXpress invia messaggi MIDI che portano le luci su una scena corrispondente.

## Attivare il supporto MIDI

Aprire le [impostazioni di Message Broker](index.md#aprire-le-impostazioni-di-message-broker), attivare il supporto MIDI e fare clic su 'Configure':

![Impostazioni di Message Broker](../../assets/images/mb-settings.webp){ width="300" loading=lazy }

Si apre la schermata di configurazione MIDI:

![Schermata di configurazione MIDI](../../assets/images/mb-midi-configuration.webp){ loading=lazy }

- **In alto:** selezionare il dispositivo MIDI di ingresso e di uscita. Il dispositivo di ingresso serve solo per la funzione 'Learn' (vedere sotto). Il dispositivo di uscita riceve i messaggi MIDI che QuizXpress invia quando nel quiz accadono eventi.
- **Al centro, a sinistra:** i trigger, ossia gli eventi che avvengono all'interno di QuizXpress.
- **Al centro, a destra:** i messaggi MIDI inviati per il trigger selezionato.

## Aggiungere un trigger

Fare clic sul pulsante 'Add' di sinistra e scegliere il tipo di trigger:

![Aggiunta di un trigger](../../assets/images/mb-midi-add-trigger.webp){ width="300" loading=lazy }

Alcuni trigger hanno un parametro facoltativo che restringe il momento in cui scattano. In questo esempio, il trigger scatta solo quando il buzzer 2 vince una domanda Dito più Veloce:

![Un trigger Dito più Veloce filtrato sul buzzer 2](../../assets/images/mb-midi-trigger-fastest-finger.webp){ width="300" loading=lazy }

### Trigger disponibili

| Trigger | Scatta quando… |
|---|---|
| Timeout | La domanda corrente scade, ad esempio perché nessuno ha risposto in tempo. |
| Correct Answer | Il Quizmaster giudica corretta una risposta. |
| Incorrect Answer | Il Quizmaster giudica errata una risposta. |
| Answer Revealed | La risposta corretta viene mostrata sulla diapositiva. Su una diapositiva Trivia Feud, ogni risposta che viene girata sul tabellone. |
| Start Countdown | Il conto alla rovescia parte. |
| End Countdown | Il conto alla rovescia termina. |
| Pause Countdown | Il Quizmaster mette in pausa il conto alla rovescia. |
| Countdown Tick | Il conto alla rovescia avanza. È possibile filtrare in base al numero di secondi rimasti. |
| Restart | Il quiz riparte e torna alla schermata di benvenuto. |
| Dito più Veloce | Un giocatore è il primo a rispondere a una domanda Dito più Veloce. È possibile filtrare in base al numero del dispositivo (pulsantiera o buzzer). |
| Screen Changed | La schermata cambia, ad esempio schermata di benvenuto → schermata di accesso dei buzzer → schermata del quiz → schermata dei punteggi. È possibile filtrare in base al tipo di schermata. |
| Slide Changed | Il quiz passa a un'altra diapositiva. È possibile filtrare in base al numero della diapositiva di partenza/arrivo o alla classe della diapositiva. I numeri delle diapositive iniziano da 0 (la prima diapositiva è 0), a meno che 'Number slides from 1' sia selezionato nella scheda [IP Outbound](ip-outbound.md#impostazioni). |
| Remote Command | Arriva un comando dalla pulsantiera Master. |
| Receive Keypad | Arriva un segnale da una pulsantiera o da un buzzer. È possibile filtrare in base al numero della pulsantiera e al tasto (A = 1, B = 2 e così via; Dito più Veloce = 0). |
| Claim Bingo | Un giocatore dichiara Bingo. |
| False Bingo | Un Bingo dichiarato non supera la convalida. |
| Bingo | Un Bingo dichiarato è valido e il giocatore vince. |

!!! tip
    Filtrare 'Slide Changed' in base a una **classe di diapositiva** è più robusto che filtrare in base ai numeri delle diapositive. Si assegna una classe a una diapositiva in QuizXpress Studio; se in seguito si riordinano le diapositive, i trigger basati sulla classe continuano a funzionare, mentre quelli basati sui numeri dovrebbero essere aggiornati.

## Definire i messaggi MIDI

Per ogni trigger, definire la sequenza di messaggi MIDI da inviare al dispositivo di uscita (l'elenco a destra). Ci sono due modi per farlo.

**Impararli dal proprio controller (consigliato).** Fare clic su 'Learn' (diventa verde), quindi impostare il controller luci sulla scena desiderata. I messaggi MIDI compaiono nell'elenco man mano. Fare di nuovo clic su 'Learn' al termine.

**Inserirli manualmente.** Fare clic sul pulsante 'Add' di destra:

![Aggiunta manuale di un messaggio MIDI](../../assets/images/mb-midi-add-message.webp){ width="300" loading=lazy }

Fare doppio clic su un messaggio o su un trigger nell'elenco per modificarlo.

Fare clic su 'Test' per inviare i messaggi selezionati al dispositivo di uscita e verificare che il controller risponda correttamente.

Quando tutto è configurato, chiudere la schermata di configurazione MIDI e poi chiudere le impostazioni di Message Broker con 'OK'. Da quel momento, QuizXpress invia i messaggi MIDI al dispositivo di uscita selezionato.

## Provare senza hardware MIDI

Due strumenti gratuiti consentono di provare senza alcun dispositivo MIDI fisico:

1. **[loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html)** crea un dispositivo MIDI virtuale, in modo che i programmi possano comunicare in MIDI tra loro senza hardware.

    ![loopMIDI](../../assets/images/mb-loopmidi.webp){ width="500" loading=lazy }

2. **[Virtual MIDI Sliders](http://www.granucon.com/SoftwarePages/Vms.aspx)** mostra come QuizXpress pilota un controller MIDI generico. Anche la funzione 'Learn' funziona con questo dispositivo virtuale.

    ![Virtual MIDI Sliders](../../assets/images/mb-virtual-midi-sliders.webp){ loading=lazy }
