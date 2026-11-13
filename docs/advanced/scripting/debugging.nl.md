# Testen en debuggen

QuizXpress heeft een scriptconsole, zoals de console van een webbrowser. De console toont wat uw script met `console.log()` schrijft, en elke fout in een script met de dia, de regel en de kolom waar die optrad.

## Naar de console schrijven

```javascript
console.log('Slide ' + (slide.slideNumber + 1) + ': ' + slide.question);
console.warn('No music file set');
console.error('Something went wrong');
```

`console.log()`, `console.info()`, `console.warn()` en `console.error()` accepteren een willekeurig aantal waarden, ook objecten en arrays. Waarschuwingen en fouten worden apart geteld, zodat ze opvallen.

!!! tip
    Gebruik `console.log()` in plaats van `alert()`. `alert()` toont een berichtvenster dat de hele quiz stillegt totdat iemand het sluit.

## In Quiz Studio

De console staat onder de scripteditor. Klik op 'Testen' om het script uit te voeren: de uitvoer verschijnt in de console, gevolgd door 'Testrun voltooid'. Als het script mislukt, toont de console de fout en markeert de editor de regel. Dubbelklik op een bericht om naar de bijbehorende regel in het script te gaan.

- 'Wissen' maakt de console leeg, 'Kopiëren' kopieert alle berichten, bijvoorbeeld om hulp te vragen aan een AI-assistent.
- 'Fouten' en 'Waarschuwingen' tonen hoeveel er zijn.
- Berichten die zich herhalen, bijvoorbeeld van een timer, worden samengevoegd tot één regel met een teller.

## Tijdens een show

Een scriptfout stopt de show nooit: QuizXpress meldt de fout en gaat door. De scriptconsole van QuizXpress Director toont wat de scripts deden. Deze wordt nooit op het geprojecteerde scherm getoond.

Zodra een script naar de console schrijft of mislukt, toont de Director een knop 'Script' tussen de commandoknoppen, met het aantal fouten erop. Klik op de knop om de scriptconsole te openen.

Hoe zichtbaar de console is, is een optie. Klik met de rechtermuisknop op de commandoknoppen van de Director en kies 'Scriptfouten':

| Optie | Wat het doet |
|---|---|
| 'Automatisch (console openen bij testen vanuit Quiz Studio)' | Wanneer u de quiz test vanuit Quiz Studio, opent de console bij de eerste fout. In een echte show krijgt u alleen de knop. Dit is de standaardinstelling. |
| 'Knop met het aantal fouten tonen' | Alleen de knop. |
| 'Console openen bij de eerste fout' | De console opent bij de eerste fout, ook in een echte show. |
| 'Niet tonen' | Geen knop en geen console. |

'Scriptconsole openen' in hetzelfde menu opent de console op elk moment.

!!! tip
    De console is ook een goede plek voor informatie voor de quizmaster. Het voorbeeld [Vragen van het web](examples.md#vragen-van-het-web) schrijft de vraag die het heeft gedownload, met het juiste antwoord gemarkeerd, naar de console.
