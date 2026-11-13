# AI-assistenten

Quiz Studio kan worden bediend door een AI-assistent zoals [Claude](https://claude.ai). U vertelt de assistent welke quiz u wilt (“maak een kroegquizronde over de jaren 90 met 10 meerkeuzevragen en een afbeeldingenronde”), en de assistent opent, bouwt, bewerkt en bewaart de quiz in uw Quiz Studio-venster terwijl u meekijkt. Alles wat de assistent doet, gebeurt in de Quiz Studio die u open hebt staan, zodat u het resultaat kunt bekijken, zelf kunt aanpassen en kunt doorgaan.

Dit verschilt van de [AI Quiz Generator](../../studio/quizxpress-and-ai.md), een onderdeel van Studio dat vragen voor u genereert. Met een AI-assistent werkt u in een gesprek, en de assistent kan bijna alles wat u zelf in Studio kunt: elk type dia maken, teksten, antwoorden, punten, stijlen en achtergronden wijzigen, minigames toevoegen, de quiz op fouten controleren en opslaan.

## Hoe het werkt

De verbinding gebruikt een standaard met de naam MCP (Model Context Protocol), waarmee AI-assistenten andere programma’s kunnen gebruiken. Quiz Studio heeft een kleine MCP-server ingebouwd:

- Deze staat **uit** totdat u hem inschakelt in de Opties, zie [Een AI-assistent verbinden](connecting-an-ai-assistant.md).
- Deze accepteert alleen verbindingen van **programma’s op uw eigen computer**. Niemand op het netwerk of internet kan hem gebruiken.
- U hebt een AI-assistent nodig die MCP ondersteunt, bijvoorbeeld Claude Code. De assistent is een apart product met een eigen abonnement: het maakt geen deel uit van QuizXpress en gebruikt uw QuizXpress AI-tegoed niet.

Zolang een assistent verbonden is, meldt een balk onder het lint dat.

## Goed om te weten

!!! warning "Wijzigingen kunnen niet ongedaan worden gemaakt"
    De wijzigingen van de assistent kunt u niet ongedaan maken met Ongedaan maken, en Quiz Studio wist na elke wijziging de geschiedenis voor ongedaan maken. Sla uw quiz onder een andere naam op voordat u een assistent grote wijzigingen laat doorvoeren, zodat u altijd terug kunt.

- De assistent opent, maakt of sluit geen quiz zolang de quiz in Studio niet-opgeslagen wijzigingen bevat. Hij moet u eerst vragen: sla de quiz op, of laat hem de wijzigingen weggooien.
- Zolang er een dialoogvenster open is in Studio (bijvoorbeeld de Opties), moet de assistent wachten. Sluit het dialoogvenster en hij kan verder.
- Elke keer dat de assistent een dia toevoegt, toont Studio die dia en scrolt de miniaturen ernaartoe.
- Dit geldt alleen voor Quiz Studio. Quiz Live, Director en Setup kunnen niet door een assistent worden bediend.

## In dit gedeelte

- [Een AI-assistent verbinden](connecting-an-ai-assistant.md): schakel het in en verbind uw assistent.
- [Claude Desktop gebruiken](claude-desktop.md): stel de Claude-app voor Windows in, ook in Parallels op een Mac.
- [Wat een assistent kan doen](what-an-assistant-can-do.md): de mogelijkheden, met voorbeelden van wat u kunt vragen.
