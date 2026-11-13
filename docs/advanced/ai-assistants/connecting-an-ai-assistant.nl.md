# Een AI-assistent verbinden

## Inschakelen

1. Ga in Quiz Studio naar START → Opties en open het tabblad 'AI-voltooiing'.
2. Vink onder 'AI-assistenten (MCP)' de optie 'AI-assistenten toestaan Quiz Studio te bedienen' aan en klik op OK.

De pagina toont het adres waarmee een assistent verbinding moet maken: `http://127.0.0.1:8766/mcp`. De instelling wordt onthouden en blijft dus aan wanneer u Studio de volgende keer start. Haal het vinkje weg om de instelling weer uit te schakelen.

## Uw assistent verbinden

Voeg Quiz Studio toe als MCP-server in uw AI-assistent, met het bovenstaande adres en het HTTP-transport. Hoe u dat doet, hangt af van de assistent. Voor Claude Code voert u dit commando eenmalig uit in een opdrachtprompt:

```
claude mcp add --transport http quizstudio http://127.0.0.1:8766/mcp
```

Andere assistenten die MCP-servers via HTTP ondersteunen, hebben een vergelijkbare instelling waar u een naam en het adres invoert. Voor Claude Desktop, zie [Claude Desktop gebruiken](claude-desktop.md).

Quiz Studio moet draaien terwijl de assistent werkt. Start het gesprek zoals u gewend bent, bijvoorbeeld: “Open mijn quiz ‘Vrijdagavond.qx’ in Quiz Studio en geef me een overzicht van de dia’s.”

## Wat u ziet in Studio

Zodra de assistent verbinding maakt, verschijnt er een balk onder het lint: ‘Een AI-assistent is verbonden met Quiz Studio. Wijzigingen die deze aanbrengt, kunt u niet ongedaan maken.’ Klik op 'Uitschakelen' op de balk om de assistent los te koppelen en de instelling weer uit te schakelen. Klik op het kruisje om de balk te verbergen.

## Slechts voor één sessie gebruiken

Als u de instelling niet permanent wilt inschakelen, start u Quiz Studio met de optie `-mcp`. De assistent kan dan tijdens die sessie verbinding maken en de instelling blijft uit. Quiz Studio slaat ook het welkomstscherm over, zodat u het vanuit een script kunt starten of door een assistent kunt laten starten. U kunt de quiz die moet worden geopend toevoegen:

```
"Quiz Studio.exe" -mcp "C:\Quizzes\Friday night.qx"
```

Om een andere poort te gebruiken, bijvoorbeeld als u twee exemplaren van Studio draait, voegt u de poort toe: `-mcp:8800`. Het adres wordt dan `http://127.0.0.1:8800/mcp`.

## Probleemoplossing

**De balk meldt 'AI-assistenten kunnen geen verbinding maken: poort 8766 is al in gebruik'.** Een ander programma, of een ander exemplaar van Quiz Studio, gebruikt de poort. Sluit het andere exemplaar of start Studio met `-mcp:` en een ander poortnummer.

**De assistent meldt dat Quiz Studio niet reageert of een dialoogvenster toont.** Quiz Studio kan geen opdrachten aannemen zolang er een dialoogvenster open is. Sluit het dialoogvenster (bijvoorbeeld de Opties of de vraag 'Wijzigingen opslaan?') en vraag de assistent het opnieuw te proberen.

**De assistent kan helemaal geen verbinding maken.** Controleer of de optie is aangevinkt, of Quiz Studio draait en of het adres in de assistent precies overeenkomt met het adres in de Opties. U hoeft niets te wijzigen in de Windows-firewall: de verbinding blijft op uw eigen computer.
