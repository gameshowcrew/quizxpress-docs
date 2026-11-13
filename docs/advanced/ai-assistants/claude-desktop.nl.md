# Claude Desktop gebruiken

[Claude Desktop](https://claude.ai/download) is de Claude-app voor Windows en Mac. De app kan Quiz Studio net zo bedienen als Claude Code, maar maakt op een andere manier verbinding: via een klein brugprogramma met de naam `mcp-remote`. Deze pagina legt uit hoe u dit instelt, ook als u QuizXpress in Parallels op een Mac gebruikt.

Schakel eerst de instelling voor AI-assistenten in Quiz Studio in, zoals beschreven in [Een AI-assistent verbinden](connecting-an-ai-assistant.md).

## Wat u nodig hebt

- **Claude Desktop voor Windows**, geïnstalleerd op dezelfde computer als Quiz Studio. Er is ook een versie voor Windows on ARM.
- **Node.js** (de LTS-versie van [nodejs.org](https://nodejs.org)). Het brugprogramma draait hierop. Om te controleren of het is geïnstalleerd, opent u een opdrachtprompt en typt u `node --version`: er moet een versienummer verschijnen.

!!! note
    Voeg Quiz Studio niet toe onder 'Instellingen' → 'Connectors' in Claude. Die connectors maken verbinding vanaf de servers van Anthropic op internet, en Quiz Studio accepteert alleen verbindingen vanaf uw eigen computer.

## Quiz Studio toevoegen aan Claude Desktop

1. Ga in Claude Desktop naar 'Instellingen' → 'Developer' en klik op 'Edit Config'. Hiermee opent u het configuratiebestand `claude_desktop_config.json`.
2. Sluit Claude Desktop volledig af. Het venster sluiten is niet genoeg: open Taakbeheer, selecteer Claude en klik op 'Taak beëindigen'. Als Claude nog actief is terwijl u het bestand bewerkt, kan het uw wijzigingen overschrijven.
3. Open het bestand in Kladblok en voeg dit blok toe direct na de eerste `{`:

   ```json
     "mcpServers": {
       "quizstudio": {
         "command": "cmd",
         "args": ["/c", "npx", "-y", "mcp-remote", "http://127.0.0.1:8766/mcp"]
       }
     },
   ```

   Laat de rest van het bestand ongewijzigd en sla het op.
4. Start Quiz Studio en start daarna Claude Desktop opnieuw.
5. Controleer onder 'Instellingen' → 'Developer' of `quizstudio` als actief wordt weergegeven. De eerste keer kan dit ongeveer een minuut duren, doordat het brugprogramma wordt gedownload.

Start nu een gesprek zoals u gewend bent, bijvoorbeeld: “Geef me een overzicht van de dia’s van de quiz die open staat in Quiz Studio.”

!!! tip
    Gebruik precies de bovenstaande vorm, met `cmd` en `/c`. Claude Desktop op Windows vindt `npx` niet altijd als het rechtstreeks wordt gestart.

## QuizXpress in Parallels op een Mac

Quiz Studio accepteert alleen verbindingen vanaf de computer waarop het draait. Als QuizXpress in Windows in Parallels draait, geldt de Mac als een andere computer, waardoor Claude op de Mac Quiz Studio niet kan bereiken.

Installeer Claude Desktop **in Windows**, in dezelfde virtuele machine als QuizXpress, en stel het in zoals hierboven beschreven. Uw Claude-account en gesprekken zijn dezelfde als op de Mac.

## Het tabblad Code van Claude Desktop gebruiken

Claude Desktop heeft ook een tabblad 'Code', waarmee Claude Code draait. Dit gebruikt `claude_desktop_config.json` niet. In plaats daarvan leest het het bestand `.mcp.json` in de map waarin u werkt en maakt het rechtstreeks verbinding, zonder het brugprogramma:

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

Claude Code vraagt u de server goed te keuren voordat deze wordt gebruikt. Start na een wijziging van het bestand een nieuwe sessie in het tabblad Code: een sessie die al open is, ziet de server niet.

## Probleemoplossing

**`quizstudio` verschijnt niet onder 'Instellingen' → 'Developer', of uw wijzigingen in het bestand zijn weg.** Claude Desktop was nog actief terwijl u het bestand bewerkte. Sluit het af via Taakbeheer, voer de wijziging opnieuw door en start Claude.

**`quizstudio` blijft op starten staan of toont een fout.** Controleer of Node.js is geïnstalleerd (`node --version`), of Quiz Studio draait en of de optie voor AI-assistenten is aangevinkt in de opties van Quiz Studio. Sluit daarna Claude Desktop af via Taakbeheer en start het opnieuw.

**Claude op de Mac kan geen verbinding maken met Quiz Studio in Parallels.** Dat is te verwachten: draai Claude Desktop in Windows, zie [QuizXpress in Parallels op een Mac](#quizxpress-in-parallels-op-een-mac).
