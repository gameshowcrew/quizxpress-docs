# Tiro alla Fune

Rope Rumble è un veloce gioco di tiro alla fune a squadre. I giocatori sono divisi in due squadre, Red e Blue, e competono premendo i propri buzzer per dare potenza al tiratore di fune della propria squadra. Ogni pressione del buzzer aggiunge forza al lato della squadra, creando una sfida emozionante mentre la fune e la bandiera centrale si spostano nell'arena.

Il gioco valuta l'attività delle squadre a intervalli rapidi, quindi il vantaggio può cambiare da un momento all'altro. La squadra che tira più forte tira la fune dalla propria parte, e più grande è il suo vantaggio, più la fune si sposta. La prima squadra a tirare la bandiera oltre la linea di vittoria vince il round.

![](../../assets/images/image168.webp){ loading=lazy }

Per aumentare la suspense, Rope Rumble può essere giocato con un limite di tempo. Se il tempo scade prima che una delle due squadre raggiunga la linea di vittoria, la vittoria va alla squadra dalla cui parte si trova la bandiera. Se la bandiera è esattamente al centro, vince la squadra che ha tirato più forte nell'intero round; se anche questo è un pareggio, il round finisce in parità e nessuno riceve punti. È possibile giocare più round, e i giocatori della squadra vincente ricevono il numero di punti configurato.

Con comandi intuitivi, grafica animata, monitoraggio dei punteggi in tempo reale e un avvincente formato da tiro alla fune, Rope Rumble trasforma l'attività dei buzzer in una competizione energica e coinvolgente per un pubblico di qualsiasi dimensione.

## Gioco equo con squadre diseguali

Le squadre non hanno sempre la stessa dimensione: un numero dispari di giocatori, oppure due gruppi di dimensioni diverse. Se ogni pressione del buzzer contasse semplicemente, la squadra più grande vincerebbe quasi sempre, anche se i suoi giocatori non premono più velocemente. Per questo Rope Rumble confronta per impostazione predefinita le squadre **per giocatore**: le pressioni del buzzer di ogni squadra vengono divise per il suo numero di giocatori. Una squadra di 4 che preme più forte di una squadra di 6 vince il tiro alla fune. Il modo in cui le squadre vengono confrontate si imposta con 'Team balance' (vedi sotto).

Altri accorgimenti mantengono il gioco equo:

- Ogni giocatore conta al massimo 15 pressioni al secondo, quindi un auto-clicker o un tasto bloccato non può far vincere una squadra.
- Il tabellone mostra il numero di giocatori di ogni squadra accanto alle sue pressioni del buzzer, così il pubblico capisce perché la squadra più piccola può essere in vantaggio con meno pressioni.
- I giocatori che arrivano dopo la formazione delle squadre (per esempio un ritardatario sulla pulsantiera mobile) vengono aggiunti alla squadra più piccola, oppure alla squadra del proprio gruppo quando le squadre sono divise per gruppo. Il telefono indica loro per quale squadra giocano.
- Un round inizia solo se entrambe le squadre hanno almeno un giocatore. Altrimenti lo schermo mostra "Entrambe le squadre devono avere almeno un giocatore".

## Impostazioni di Rope Rumble

![Impostazioni di Rope Rumble](../../assets/images/rope-rumble-settings.webp){ width="311" loading=lazy }

Le impostazioni di Rope Rumble determinano la durata del gioco, la rapidità con cui le pressioni dei buzzer spostano la fune e il modo in cui vengono formate le squadre. Per aprire le impostazioni, selezionare Rope Rumble e scegliere Configure.

**Number of games to play**

Specifica quanti round vengono giocati prima della fine di Rope Rumble. Al termine di un round, il Director può avviare il round successivo fino al raggiungimento del numero configurato.

**Points for winning team**

Imposta il numero di punti assegnati a ciascun giocatore della squadra vincente al termine di un round.

**Buzz sample speed**

Controlla la frequenza con cui il gioco valuta le pressioni dei buzzer e aggiorna la posizione della fune.

- Fast: le pressioni dei buzzer vengono valutate più frequentemente, con un movimento della fune più rapido e reattivo.

- Slow: le pressioni dei buzzer vengono valutate meno frequentemente, con un movimento più graduale.

Il valore predefinito è 250 millisecondi. L'intervallo disponibile va da 100 a 400 millisecondi.

**Pull strength**

Controlla di quanto si sposta la fune quando una squadra tira più forte dell'altra durante un intervallo di campionamento. È la distanza per una squadra che fa tutto il lavoro; un vantaggio minore sposta meno la fune.

- Low: crea un tiro alla fune più lento e graduale.

- High: il vantaggio di ciascuna squadra sposta la fune più lontano, producendo un gioco più rapido e decisivo.

**Win distance**

Determina quanto la bandiera deve allontanarsi dal centro perché una squadra vinca il round.

- Una distanza minore rende più facile vincere e accorcia il round.

- Una distanza maggiore crea una sfida più lunga e offre alle squadre più opportunità di recuperare.

**Maximum time per round**

Imposta la durata massima di ogni round in secondi. Se il timer arriva a zero prima che una delle due squadre raggiunga la distanza di vittoria, vince la squadra dalla cui parte si trova la bandiera. Una bandiera esattamente al centro va alla squadra che ha tirato più forte nell'intero round, e una parità completa è un pareggio.

Impostare questo valore su 0 per disattivare il limite di tempo.

**Team balance**

Determina il modo in cui viene confrontata la forza delle due squadre.

- Per team member (fair for uneven teams): il valore predefinito. Le pressioni del buzzer di ogni squadra vengono divise per il numero di giocatori della squadra. Ogni giocatore deve partecipare: un giocatore che non preme conta come un giocatore che non tira. La scelta migliore per la maggior parte degli eventi.

- Per active player: le pressioni del buzzer di ogni squadra vengono divise per il numero dei suoi giocatori che hanno premuto almeno una volta durante il round. I giocatori che non si presentano mai non indeboliscono la propria squadra. Usare questa opzione quando si prevedono giocatori registrati che non parteciperanno, come posti vuoti o telefoni mai collegati.

- Off (the bigger team pulls harder): ogni pressione del buzzer conta allo stesso modo, e la squadra con più pressioni in un intervallo sposta la fune di un passo intero. È il modo in cui Rope Rumble funzionava in precedenza; una squadra più grande ha un netto vantaggio.

**Team colors**

Imposta i colori delle squadre Red e Blue. Fare clic sul pulsante di una squadra per scegliere un altro colore. I colori vengono usati per i simboli delle squadre, la barra della forza e il testo del vincitore.

**Split teams by player group**

Determina il modo in cui i giocatori vengono assegnati alle squadre Red e Blue.

- Se attivata, i giocatori vengono divisi in base al Group configurato. Questa opzione è pensata per gli eventi in cui i giocatori sono già stati organizzati in due gruppi. I gruppi possono avere dimensioni diverse; 'Team balance' mantiene il gioco equo.

- Se disattivata, i giocatori vengono assegnati alternativamente in ordine di pulsantiera, quindi le due squadre non differiscono mai di più di un giocatore.

**Background**

Consente di sostituire la grafica di Rope Rumble inclusa con un'immagine di sfondo personalizzata. Fare clic su Browse... per selezionare un file immagine (per esempio PNG, JPG o BMP). L'immagine selezionata viene mostrata nell'area di anteprima e salvata con la configurazione del quiz. Fare clic su Clear per rimuovere l'immagine personalizzata e tornare alla grafica predefinita inclusa.
