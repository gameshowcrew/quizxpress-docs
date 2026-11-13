# Binnenkomstanimaties

Sinds versie 8.6 kunnen de vraag en de antwoorden in Quiz Show een entree maken: in plaats van simpelweg te verschijnen, faden ze in, schuiven ze van de zijkant binnen, poppen ze op, vallen ze en stuiteren ze, enzovoort. U kiest een effect voor de vraag en een effect voor de antwoorden, en of de antwoorden na elkaar of allemaal tegelijk binnenkomen.

## Een binnenkomst instellen

Selecteer de dia in Quiz Studio en open het gedeelte ‘Animatie’ van de diaeigenschappen (in het [geavanceerde eigenschappenraster](../user-interface-overview/advanced-properties-grid.md) vindt u dezelfde instellingen onder ‘Weergave’):

| Instelling | Wat het doet |
|---|---|
| ‘Binnenkomst vraag’ | Hoe de vraag binnenkomt. Afbeeldingen die geen antwoorden zijn, komen samen met de vraag binnen. |
| ‘Binnenkomst antwoorden’ | Hoe de antwoorden binnenkomen. Bij een afbeeldingsvraag met meerdere afbeeldingen komen de antwoordafbeeldingen als antwoorden binnen. |
| ‘Volgorde antwoorden’ | ‘Eén voor één’: de antwoorden komen na elkaar binnen. ‘Allemaal tegelijk’: ze komen tegelijkertijd binnen. Wordt getoond wanneer een binnenkomst voor antwoorden is ingesteld. |
| ‘Animatiesnelheid’ | ‘Normaal’, ‘Langzaam’ of ‘Snel’. Geldt voor de vraag en de antwoorden. |
| ‘Aftellen tijdens animatie’ | Indien ingeschakeld begint het aftellen terwijl de vraag en de antwoorden nog binnenkomen. Indien uitgeschakeld (de standaardinstelling) begint het aftellen zodra alles op het scherm staat. |

‘Volgorde antwoorden’, ‘Animatiesnelheid’ en ‘Aftellen tijdens animatie’ verschijnen pas wanneer een binnenkomst is ingesteld voor de vraag of de antwoorden.

Wanneer zowel de vraag als de antwoorden een binnenkomst hebben, beginnen de antwoorden wanneer de vraag halverwege is, zodat de twee in elkaar overlopen.

## Effecten

| Effect | Wat u ziet |
|---|---|
| ‘Geen’ | Geen animatie: het item verschijnt simpelweg (de standaardinstelling). |
| ‘Infaden’ | Het item faadt in. |
| ‘Van links inschuiven’ / ‘rechts’ / ‘boven’ / ‘onder’ | Het item schuift van buiten het scherm binnen. |
| ‘Afwisselend links en rechts’ | De antwoorden komen om en om van links en van rechts binnen, te beginnen links. Bij gebruik voor de vraag schuift deze van links binnen. |
| ‘Inzoomen’ | Het item groeit vanaf de helft van zijn grootte terwijl het infaadt. |
| ‘Opploppen’ | Het item poppt op, schiet iets door en komt tot rust. |
| ‘Omdraaien’ | Het item klapt open als een kaart die wordt omgedraaid. |
| ‘Draaien’ | Het item draait op zijn plaats terwijl het groeit. |
| ‘Vallen en stuiteren’ | Het item valt van boven naar binnen en stuitert voordat het tot rust komt. |

Bij de snelheid ‘Normaal’ doet een item ongeveer 0,6 seconde over de binnenkomst, bij ‘Langzaam’ ongeveer 0,9 seconde en bij ‘Snel’ ongeveer 0,35 seconde. ‘Draaien’ en ‘Vallen en stuiteren’ duren iets langer, zodat ze leesbaar blijven.

## Antwoorden die later worden getoond

Als de antwoorden niet direct worden getoond, omdat ‘Antwoord tonen actie’ is ingesteld op ‘Verbergen en één voor één tonen’ of ‘Verbergen en tegelijk tonen na vertraging’, wordt de ‘Binnenkomst antwoorden’ gebruikt telkens wanneer antwoorden verschijnen.

## Welke dia’s het ondersteunen

Binnenkomstanimaties werken op vraagdia’s en de andere diatypen die een vraag en antwoorden tonen. Ze zijn niet beschikbaar voor Trivia Feud, Bingo-rondes, minigames, Trivia Bord-rondes en Trivia Ladder-rondes; voor die dia’s worden de instellingen onder ‘Animatie’ niet getoond.

!!! tip
    Binnenkomstanimaties combineren goed met [tekstonthullingsanimaties](text-reveal-animations.md): laat de vraag binnenschuiven en onthul vervolgens de tekst woord voor woord, of laat de antwoorden een voor een binnenvallen nadat de vraag is voorgelezen.
