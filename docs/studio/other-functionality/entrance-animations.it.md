# Animazioni di entrata

Dalla versione 8.6, la domanda e le risposte possono fare il loro ingresso in QuizXpress Live: invece di comparire semplicemente, entrano in dissolvenza, scorrono dal bordo, saltano fuori, cadono e rimbalzano, e così via. Si sceglie un effetto per la domanda e uno per le risposte, e si decide se le risposte entrano una dopo l'altra o tutte insieme.

## Impostare un'entrata

Selezionare la diapositiva in QuizXpress Studio e aprire la sezione ‘Animazione’ delle proprietà della diapositiva (nella [griglia delle proprietà avanzate](../user-interface-overview/advanced-properties-grid.md) le stesse impostazioni si trovano sotto ‘Aspetto’):

| Impostazione | Cosa fa |
|---|---|
| ‘Entrata Domanda’ | Come entra la domanda. Le immagini che non sono risposte entrano insieme alla domanda. |
| ‘Entrata Risposte’ | Come entrano le risposte. In una domanda con più immagini, le immagini di risposta entrano come risposte. |
| ‘Ordine Risposte’ | ‘Una alla Volta’: le risposte entrano una dopo l'altra. ‘Tutte Insieme’: entrano contemporaneamente. Visibile quando è impostata un'entrata delle risposte. |
| ‘Velocità Animazione’ | ‘Normale’, ‘Lenta’ o ‘Veloce’. Vale per la domanda e per le risposte. |
| ‘Countdown durante Animazione’ | Se attivato, il conto alla rovescia parte mentre la domanda e le risposte stanno ancora entrando. Se disattivato (impostazione predefinita), parte non appena tutto è sullo schermo. |

‘Ordine Risposte’, ‘Velocità Animazione’ e ‘Countdown durante Animazione’ compaiono solo dopo aver impostato un'entrata per la domanda o per le risposte.

Quando sia la domanda sia le risposte hanno un'entrata, le risposte iniziano quando la domanda è a metà del suo ingresso, così le due animazioni si susseguono in modo fluido.

## Effetti

| Effetto | Cosa si vede |
|---|---|
| ‘Nessuna’ | Nessuna animazione: l'elemento compare e basta (impostazione predefinita). |
| ‘Dissolvenza in Entrata’ | L'elemento compare in dissolvenza. |
| ‘Scorri da Sinistra’ / ‘da Destra’ / ‘dall'Alto’ / ‘dal Basso’ | L'elemento scorre dentro da fuori dello schermo. |
| ‘Alterna Sinistra e Destra’ | Le risposte arrivano a turno da sinistra e da destra, iniziando da sinistra. La domanda scorre da sinistra. |
| ‘Zoom Avanti’ | L'elemento cresce da metà della sua dimensione mentre compare in dissolvenza. |
| ‘Pop’ | L'elemento salta fuori, supera leggermente la sua dimensione e poi si assesta. |
| ‘Capovolgi’ | L'elemento si gira come una carta. |
| ‘Ruota’ | L'elemento ruota fino alla sua posizione mentre cresce. |
| ‘Cadi e Rimbalza’ | L'elemento cade dall'alto e rimbalza prima di fermarsi. |

Con la velocità ‘Normale’ un elemento impiega circa 0,6 secondi a entrare, con ‘Lenta’ circa 0,9 secondi e con ‘Veloce’ circa 0,35 secondi. ‘Ruota’ e ‘Cadi e Rimbalza’ durano un po' di più, per restare leggibili.

## Risposte mostrate in seguito

Se le risposte non vengono mostrate subito, perché ‘Mostra Azioni Risposta’ è impostato su ‘Nascondi e Mostra una alla Volta’ o ‘Nascondi e Mostra Insieme’, l'‘Entrata Risposte’ viene usata ogni volta che compaiono delle risposte.

## Diapositive supportate

Le animazioni di entrata funzionano sulle diapositive di domanda e sugli altri tipi di diapositiva che mostrano una domanda e delle risposte. Non sono disponibili per Trivia Feud, round di Bingo, Moduli Gioco, round Tabellone Trivia e Trivia Ladder; per queste diapositive le impostazioni ‘Animazione’ non vengono mostrate.

!!! tip
    Le animazioni di entrata si combinano bene con le [animazioni di comparsa del testo](text-reveal-animations.md): far scorrere dentro la domanda e poi rivelare il testo parola per parola, oppure far cadere le risposte una alla volta dopo aver letto la domanda.
