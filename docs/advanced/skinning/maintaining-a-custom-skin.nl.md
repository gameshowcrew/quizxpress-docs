# Een eigen skin delen, bijwerken en problemen oplossen

## Een skin delen met een andere computer

Een complete eigen skin bestaat uit twee dingen, beide in de gegevensmap `%appdata%\QuizXpress`:

- `skin.config`
- de map `Skins\<your skin>` met de bijbehorende afbeeldingen

Kopieer beide naar de gegevensmap op de andere computer en selecteer daar de skin in Quiz Setup. Als u het relatieve `dir="Skins\<your skin>"` hebt gebruikt zoals beschreven in [Een eigen skin maken](creating-a-custom-skin.md#stap-4-voeg-uw-skindefinitie-toe), hoeft er niets te worden aangepast. Lettertypen die de skin gebruikt, moeten ook op de andere computer zijn geïnstalleerd.

## Na een QuizXpress-update

Een update vervangt de geïnstalleerde `skin.config`, maar raakt uw kopie of uw skinmap nooit aan, dus uw skin blijft werken. Omdat een 'User.'-skin echter alleen uw kopie leest, blijven de ingebouwde skins waarvan hij erft zoals ze waren toen u de kopie maakte. Nieuwe instellingen en verbeteringen die een update aan de ingebouwde skins toevoegt, worden niet door uw skin overgenomen.

Zo brengt u uw skin na een update weer op peil:

1. Kopieer uw element `<skin>…</skin>` uit uw `skin.config` naar een veilige plek, bijvoorbeeld een tekstbestand ernaast.
2. Kopieer de nieuwe `skin.config` uit de installatiemap naar de gegevensmap en vervang uw kopie.
3. Plak uw element `<skin>` terug, vlak boven `</skins>` (en voeg `hidden="true"` opnieuw toe aan de ingebouwde skins als u dat gebruikte).

Uw skinmap met afbeeldingen hoeft niet te veranderen.

## Probleemoplossing

| Symptoom | Oorzaak en oplossing |
|---|---|
| Mijn skin verschijnt niet in Quiz Setup. | Controleer of u de kopie in `%appdata%\QuizXpress` hebt bewerkt (niet het geïnstalleerde bestand), of het is opgeslagen, of uw skin niet `hidden="true"` heeft en of u Quiz Setup opnieuw hebt gestart. |
| QuizXpress Live toont een fout over het skinbestand en start niet. | De melding vertelt wat er niet klopt. Veelvoorkomende oorzaken: een XML-fout (een ontbrekend aanhalingsteken of `/>`, een `&` die als `&amp;` moet worden geschreven), een 'parent' die niet overeenkomt met de 'name' van een bestaande skin, of een ongeldige waarde (bij attributen met een vaste set waarden noemt de melding de toegestane waarden). Verbeter het bestand en start opnieuw. |
| Mijn skin is geselecteerd, maar de quiz ziet eruit als een ingebouwde skin. | Eigen skins zijn niet beschikbaar in de Home-editie. Controleer anders of u de 'name' van uw skin niet hebt gewijzigd nadat u die in Quiz Setup selecteerde; als dat zo is, selecteert u hem opnieuw. |
| Een instelling heeft geen effect. | Controleer de spelling van de element- en attribuutnamen aan de hand van de rootskin (ze zijn hoofdlettergevoelig) en controleer of het element binnen uw `<skin>`-element staat. Start de quiz opnieuw na het opslaan. |
| Mijn afbeelding wordt niet getoond. | Het bestand is niet gevonden of kon niet worden gelezen. Controleer de bestandsnaam (inclusief de extensie) en de 'dir' van uw skin. De fout wordt in het QuizXpress-logbestand geschreven als "Skin image … not found, please check skin.config". |
