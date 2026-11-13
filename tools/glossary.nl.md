# Dutch translation glossary (docs.quizxpress.com / `*.nl.md`)

Term dictionary for the Dutch manual. Every `*.nl.md` page follows it, so one concept always has one
Dutch word. Add a row here before using a new term in more than one page.

## Rules

1. **Register.** Formal: *u / uw* (as the Dutch product UI is formal). Never *je / jij / jouw*.
2. **Product and app names are never translated**: QuizXpress, Quiz Studio, Quiz Setup, Quiz Show,
   Quiz Show Solo, Quiz Center, QuizXpress Director, Analyzer, Smart Buzzer, Message Broker,
   Game Show Crew, Quiz Wizard, buzzerpad, Syncfusion, YouTube, Windows, Excel, PowerPoint, etc.
   Third-party names and trademarks stay as they are (Family Feud, Jeopardy, Bingo, Trivia Feud, …).
3. **UI labels follow the Dutch product.** A button, tab, ribbon group or dialog title that exists in
   the Dutch QuizXpress UI is written exactly as the Dutch UI shows it, in single curly quotes
   ‘Vraag Type’, even when it looks odd. The English → Dutch pairs come from the product's
   `*.nl.resx` files (search them by the English label). If no Dutch label exists, translate it
   and keep the quotes.
4. **Keep structure identical** to the English page: same headings in the same order, same images
   (same alt-text position), same tables, admonitions (`!!! note` etc.), lists and code blocks.
   Translate text, image alt text and the `# Heading`. Do not touch file names, link targets, image
   paths, HTML/`attr_list` attributes (`{ width="253" loading=lazy }`) or code.
5. **Code, scripts, file names, commands, JSON/XML keys, key names (Enter, Esc, F5), URLs, ports,
   product names in code spans** stay untouched. Comments inside code samples may stay English.
6. **Numbers and formats:** keep digits; decimal comma in prose only when the English page writes a
   decimal number in prose (‘0.5 seconds’ → ‘0,5 seconde’). Do not change values in code or settings.
7. **Typography:** use the same curly quotes ‘ ’ as the English source for UI labels and “ ” for quoted
   speech. Use the Dutch rule for compounds: write one word (*quizmaster*, *scorebord*, *toetsenbord*);
   use a hyphen only where Dutch needs it (*Excel-bestand*, *e-mail*, *tv-scherm*, *USB-poort*).
8. **Sentences:** natural Dutch, not word-for-word. Short sentences, active voice, same helpful tone as
   the English manual.

## Core vocabulary

| English | Dutch | Note |
|---|---|---|
| slide | dia (pl. dia’s) | as in the Dutch UI |
| question | vraag (pl. vragen) | |
| question type | vraagtype | UI label: ‘Vraag Type’ |
| answer | antwoord (pl. antwoorden) | |
| correct / incorrect answer | juist / onjuist antwoord | |
| wager (question) | weddenschap | |
| round | ronde | |
| end of round | einde ronde | quote exactly as the UI shows it |
| quiz | quiz (pl. quizzen) | |
| quizmaster / host | quizmaster | |
| player | speler | |
| team | team (pl. teams) | |
| score / scoreboard | score / scorebord | |
| points | punten | |
| countdown / timer | aftellen / klok | UI: ‘Aftellen’, ‘Klok’ |
| time to answer | antwoordtijd | |
| buzzer | buzzer | keep the loan word |
| keypad | keypad | keep the loan word; *toetsenpaneel* only as a generic description |
| fastest finger (first) | snelste drukker / snelste vinger | follow the UI per context |
| lockout | uitsluiting | |
| multiple choice | meerkeuze | |
| open question | open vraag | |
| mini game | minigame (pl. minigames) | UI: ‘Minigames’ where it exists |
| game format | spelvorm | |
| property grid | eigenschappenraster | UI: follow the Dutch label if present |
| properties | eigenschappen | |
| ribbon | lint | the Office-style ribbon |
| toolbar | werkbalk | |
| dialog (window) | dialoogvenster / venster | |
| settings / preferences | instellingen / voorkeuren | |
| setup | configuratie | the tab ‘Setup’ in nav is ‘Setup’ → *Configuratie* |
| live | live | |
| picture / image | afbeelding | |
| background | achtergrond | |
| video / sound / music / audio | video / geluid / muziek / audio | |
| text | tekst | |
| shape | vorm | |
| style | stijl | |
| skin | skin | keep the loan word (as in the product) |
| template | sjabloon | |
| transition | transitie | |
| animation | animatie | |
| layout | indeling | |
| font | lettertype | |
| preview | voorbeeld | |
| export / import | exporteren / importeren | |
| save / open | opslaan / openen | |
| trim | bijsnijden (video) / inkorten (audio) | |
| pack (a quiz) | inpakken | UI: ‘Inpakken’ |
| plugin | plug-in | |
| script | script | |
| hint | hint | |
| leaderboard | ranglijst | |
| hardware | hardware | |
| troubleshooting | probleemoplossing | |
| license / licensing | licentie / licenties | |
| update | update | |
| version | versie | |
| shortcut | sneltoets | |
| keyboard | toetsenbord | |
| screen | scherm | |
| projector | beamer | |
| audience | publiek | |
| participant | deelnemer | |
| registration | registratie | |
| card (Bingo) | kaart | UI: ‘Bingo kaart’ |
| claim (Bingo) | claim / bingomelding | UI: ‘Bingo-meldingen’ |
| Trivia Board | Trivia Bord | UI label |
| Trivia Feud | Trivia Feud | product/format name, not translated |
| billboard | billboard | slide type, keep |
| hotspot | hotspot | |
| Message Broker | Message Broker | not translated |
| inbound / outbound | inkomend / uitgaand | |
| AI assistant | AI-assistent | |
| mobile device | mobiel apparaat | |
| web keypad | webkeypad | |

## Quiz Studio ribbon tabs (as in the Dutch product, capitals)

| English | Dutch |
|---|---|
| HOME | START |
| INSERT | INVOEGEN |
| QUESTION | VRAAG |
| DESIGN | ONTWERPEN |
| VIEW | BEELD |
| PICTURE / SHAPE / SPEECH tools | AFBEELDING / VORM / SPRAAK |
| Chart tools | Grafiek |

## Decisions added while translating

| English | Dutch |
|---|---|
| thumbnail(s) / thumbnails panel | miniatuur / miniaturen, miniaturenpaneel |
| backstage menu | Backstage-menu |
| design area | ontwerpgebied |
| smart guides | slimme hulplijnen |
| Graphical Mode / Table Mode | grafische modus / tabelmodus |
| Quiz Slides (ribbon group) | ‘Quiz Vragen’ (as in the UI) |
| quiz slide | quizdia |
| Word Game | woordspel |
| Last Man Standing | not translated |
| notes (prose) / Notes (View checkbox) | notities / ‘Opmerkingen’ |
| survey | enquête |
| reveal / Reveal mode | onthullen / onthullingsmodus |
| tile / topic tiles | tegel / onderwerptegels |
| ladder step / safety net | trede / vangnet |
| Faceoff | Faceoff (not translated) |
| dialog launcher | dialoogvensterstarter |
| Run Production | ‘Start Productie’ |
