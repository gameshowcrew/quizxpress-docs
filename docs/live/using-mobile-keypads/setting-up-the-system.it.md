# Configurazione del sistema

Come visto in precedenza, il sistema offre diverse possibilità per gestire diversi scenari. Per ulteriori informazioni sulla configurazione di QuizXpress per l'uso con i dispositivi mobili, fare riferimento anche a [Configurazione del supporto per le pulsantiere mobili](../../setup/setting-up-mobile-keypad-support.md).

**Modalità Server**

Quando si utilizza il sistema in modalità server, è necessaria una **connessione internet affidabile** con una velocità adeguata. Il traffico dati di QuizXpress non è molto elevato rispetto, ad esempio, a un flusso video, ma una connessione inaffidabile o forti cali di velocità avranno un impatto importante sul sistema e sull'esperienza complessiva. Naturalmente, quando si trasmette il quiz in streaming su internet, potrebbero esserci requisiti aggiuntivi per il flusso video. È sempre consigliabile collegare il computer al router tramite cavo per ottenere una connessione più costante e affidabile. Il pubblico può partecipare al quiz in due modi: tramite il sito web buzzerpad (.com o .eu) o tramite l'app Smart Buzzer. Per i dettagli, si vedano i capitoli successivi. In [Configurazione del supporto per le pulsantiere mobili](../../setup/setting-up-mobile-keypad-support.md) è possibile leggere tutto sulla configurazione del sistema per la modalità server in Quiz Setup.

**Modalità Wi-Fi**

In una configurazione Wi-Fi autonoma, bisogna collegare il laptop al router tramite un cavo di rete. Il router funge da punto di accesso Wi-Fi locale per i dispositivi mobili dei giocatori, per il dispositivo che esegue l'app di controllo remoto Director e per il laptop. Di seguito un'immagine di tale configurazione:

![](../../assets/images/image355.webp){ width="604" loading=lazy }

Il laptop ottiene un indirizzo IP dal router locale e non necessita di alcuna connessione a Internet. Un router standard di buona qualità supporta fino a circa 50 giocatori. Sono disponibili sul mercato anche router che gestiscono più connessioni. I cellulari/tablet devono connettersi allo stesso router e, avviando l'app Smart Buzzer, quando il dispositivo trova il quiz in corso, viene abilitato il pulsante ‘Accedi con WiFi locale’.

Si noti che alcuni pacchetti antivirus includono firewall integrati molto restrittivi, che richiedono una configurazione speciale per consentire il traffico di rete di QuizXpress. Per aggiungere un'eccezione per QuizXpress, consentire tutto il traffico per il programma *qxserver.exe*, che si trova nella cartella di installazione di QuizXpress. Questo non è necessario con il firewall standard di Windows.
