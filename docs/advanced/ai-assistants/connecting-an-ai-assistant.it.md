# Collegare un assistente IA

## Attivarlo

1. In Quiz Studio, andare in HOME → Options e aprire la scheda 'AI Completion'.
2. Sotto 'AI assistants (MCP)', selezionare 'Allow AI assistants to control Quiz Studio' e fare clic su OK.

La pagina mostra l'indirizzo a cui un assistente deve connettersi: `http://127.0.0.1:8766/mcp`. L'impostazione viene memorizzata, quindi resta attiva al successivo avvio di Studio. Deselezionare la casella per disattivarla di nuovo.

## Collegare l'assistente

Aggiungere Quiz Studio come server MCP nel proprio assistente IA, usando l'indirizzo indicato sopra e il trasporto HTTP. La procedura dipende dall'assistente. Per Claude Code, eseguire questo comando una sola volta in un prompt dei comandi:

```
claude mcp add --transport http quizstudio http://127.0.0.1:8766/mcp
```

Gli altri assistenti che supportano server MCP tramite HTTP hanno un'impostazione analoga in cui si inseriscono un nome e l'indirizzo. Per Claude Desktop, vedi [Usare Claude Desktop](claude-desktop.md).

Quiz Studio deve essere in esecuzione mentre l'assistente lavora. Avviare la conversazione come di consueto, ad esempio: "Apri il mio quiz 'Friday night.qx' in Quiz Studio e mostrami una panoramica delle diapositive."

## Cosa si vede in Studio

Non appena l'assistente si connette, sotto la barra multifunzione compare una barra: 'An AI assistant is connected to Quiz Studio. Changes it makes cannot be undone with Undo.' Fare clic su 'Turn off' nella barra per scollegare l'assistente e disattivare di nuovo l'impostazione. Fare clic sulla croce per nascondere la barra.

## Usarlo per una sola sessione

Se non si desidera attivare l'impostazione in modo permanente, avviare Quiz Studio con l'opzione `-mcp`. L'assistente può connettersi durante quella sessione e l'impostazione resta disattivata. Quiz Studio inoltre salta la schermata di benvenuto, quindi può essere avviato da uno script o da un assistente. È possibile aggiungere il quiz da aprire:

```
"Quiz Studio.exe" -mcp "C:\Quizzes\Friday night.qx"
```

Per usare un'altra porta, ad esempio quando si eseguono due copie di Studio, aggiungere la porta: `-mcp:8800`. L'indirizzo diventa quindi `http://127.0.0.1:8800/mcp`.

## Risoluzione dei problemi

**La barra indica 'AI assistants cannot connect: port 8766 is already in use'.** Un altro programma, o un'altra copia di Quiz Studio, sta usando la porta. Chiudere l'altra copia oppure avviare Studio con `-mcp:` seguito da un altro numero di porta.

**L'assistente dice che Quiz Studio non risponde oppure mostra una finestra di dialogo.** Quiz Studio non può ricevere comandi mentre è aperta una finestra di dialogo. Chiudere la finestra (ad esempio Options o una domanda 'Save changes?') e chiedere all'assistente di riprovare.

**L'assistente non riesce a connettersi affatto.** Verificare che l'opzione sia selezionata, che Quiz Studio sia in esecuzione e che l'indirizzo nell'assistente sia esattamente quello mostrato nelle Options. Non è necessario modificare nulla nel firewall di Windows: la connessione resta sul proprio computer.
