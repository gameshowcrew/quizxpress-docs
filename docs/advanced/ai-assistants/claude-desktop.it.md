# Usare Claude Desktop

[Claude Desktop](https://claude.ai/download) è l'app di Claude per Windows e Mac. Può controllare Quiz Studio come Claude Code, ma si collega in un altro modo: attraverso un piccolo programma ponte chiamato `mcp-remote`. Questa pagina spiega come configurarlo, anche quando usi QuizXpress in Parallels su un Mac.

Prima di cominciare, attiva l'opzione per gli assistenti IA in Quiz Studio, come descritto in [Collegare un assistente IA](connecting-an-ai-assistant.md#attivarlo).

## Cosa ti serve

- **Claude Desktop per Windows**, installato sullo stesso computer di Quiz Studio. Esiste anche una versione per Windows su ARM.
- **Node.js** (la versione LTS da [nodejs.org](https://nodejs.org)): il programma ponte funziona con questo. Per controllare che sia installato, apri un prompt dei comandi e scrivi `node --version`: deve comparire un numero di versione.

!!! note
    Non aggiungere Quiz Studio in 'Impostazioni' → 'Connettori' di Claude. Quei connettori si collegano dai server di Anthropic su internet, mentre Quiz Studio accetta solo collegamenti dal tuo computer.

## Aggiungere Quiz Studio a Claude Desktop

1. In Claude Desktop, vai in 'Impostazioni' → 'Sviluppatore' e fai clic su 'Modifica configurazione'. Si apre il file di configurazione `claude_desktop_config.json`.
2. Chiudi Claude Desktop del tutto. Non basta chiudere la finestra: apri 'Gestione attività', seleziona Claude e fai clic su 'Termina attività'. Se Claude resta in esecuzione mentre modifichi il file, può sovrascrivere le tue modifiche.
3. Apri il file con Blocco note e aggiungi questo blocco subito dopo la prima `{`:

   ```json
     "mcpServers": {
       "quizstudio": {
         "command": "cmd",
         "args": ["/c", "npx", "-y", "mcp-remote", "http://127.0.0.1:8766/mcp"]
       }
     },
   ```

   Lascia il resto del file com'è e salvalo.
4. Avvia Quiz Studio, poi riavvia Claude Desktop.
5. In 'Impostazioni' → 'Sviluppatore', controlla che `quizstudio` risulti in esecuzione. La prima volta può volerci circa un minuto, mentre viene scaricato il programma ponte.

Ora avvia una conversazione come al solito, per esempio: "Mostrami una panoramica delle diapositive del quiz aperto in Quiz Studio."

!!! tip
    Usa esattamente la forma qui sopra, con `cmd` e `/c`. Su Windows, Claude Desktop non sempre trova `npx` se lo avvia direttamente.

## QuizXpress in Parallels su un Mac

Quiz Studio accetta solo collegamenti dal computer su cui è in esecuzione. Quando QuizXpress gira in Windows dentro Parallels, il Mac conta come un altro computer, quindi Claude sul Mac non può raggiungere Quiz Studio.

Installa Claude Desktop **dentro Windows**, nella stessa macchina virtuale di QuizXpress, e configuralo come descritto sopra. Il tuo account Claude e le tue conversazioni sono gli stessi del Mac.

## Usare la scheda Code di Claude Desktop

Claude Desktop ha anche una scheda 'Code', che esegue Claude Code. Non usa `claude_desktop_config.json`: legge invece il file `.mcp.json` nella cartella in cui lavori e si collega direttamente, senza il programma ponte:

```json
{
  "mcpServers": {
    "quizstudio": {
      "type": "http",
      "url": "http://127.0.0.1:8766/mcp"
    }
  }
}
```

Claude Code ti chiede di approvare il server prima di usarlo. Dopo aver modificato il file, apri una nuova sessione nella scheda Code: una sessione già aperta non vede il server.

## Risoluzione dei problemi

**`quizstudio` non compare in 'Impostazioni' → 'Sviluppatore', oppure le modifiche al file sono sparite.** Claude Desktop era ancora in esecuzione mentre modificavi il file. Chiudilo da 'Gestione attività', ripeti la modifica e avvia Claude.

**`quizstudio` resta in avvio, oppure mostra un errore.** Controlla che Node.js sia installato (`node --version`), che Quiz Studio sia in esecuzione e che nelle opzioni di Quiz Studio sia selezionata l'opzione per gli assistenti IA. Poi chiudi Claude Desktop da 'Gestione attività' e riavvialo.

**Claude sul Mac non riesce a collegarsi a Quiz Studio in Parallels.** È normale: usa Claude Desktop dentro Windows, vedi [QuizXpress in Parallels su un Mac](#quizxpress-in-parallels-su-un-mac).
