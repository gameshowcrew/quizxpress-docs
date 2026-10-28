# Trabajar con QuizXpress

## El objeto qx

QuizXpress expone sus elementos internos a los scripts mediante un objeto global llamado `qx`. Por ejemplo, `qx.slide` devuelve la diapositiva actual, y la diapositiva a su vez tiene propiedades como `notes`. Este script escribe las notas de la diapositiva en la consola cuando hace clic en 'Test' en Studio:

```javascript
console.log(qx.slide.notes);
```

El editor le ayuda a encontrar propiedades: escriba `qx.` o `slide.` y aparece una lista con todas las propiedades disponibles, con una breve explicación de cada una.

![Autocompletado en el editor de scripts](../../assets/images/js-autocomplete.webp){ loading=lazy }

Las partes más utilizadas de `qx`:

| | |
|---|---|
| `qx.slide` | La diapositiva actual: pregunta, respuestas, respuesta correcta, puntos, id, clase… |
| `qx.slides` | Todas las diapositivas del quiz. |
| `qx.teams` | Todos los equipos, con su nombre, mando, puntuación y último voto. |
| `qx.leaderBoard` | Los equipos ordenados por puntuación, con el líder primero. |
| `qx.roundLeaderBoard` | Las puntuaciones de la ronda actual. |
| `qx.sink` | El propio QuizXpress Live: ir a una diapositiva, finalizar el quiz, reproducir música… |
| `qx["name"]` | Un valor que se conserva entre diapositivas, vea más abajo. |

La [Referencia](reference.md) enumera cada objeto, propiedad y función con su significado.

## Responder al desarrollo del show

Los manejadores son la forma en que un script participa en el show. Algunos ejemplos:

```javascript
// cada segundo de la cuenta atrás
function onCountdownTick(secondsLeft) {
    if (secondsLeft === 10)
        qx['message'] = 'Ten seconds left!';
}

// un equipo respondió con su mando
function onVote(player, answer, isCorrect) {
    console.log(player.name + ' answered ' + answer);
}

// se abandona la diapositiva: limpiar
function onUnloadSlide(slide) {
    qx.sink.sound.stopMusic('tension');
}
```

!!! note "El final de una pregunta"
    Según los ajustes de la pregunta, QuizXpress Live llama a `onEndCountdown()` cuando se agotó el tiempo o todos respondieron, o solo a `onTimeout()`. Un script que tiene que hacer algo una sola vez al final de una pregunta gestiona ambos y recuerda que ya lo hizo:

    ```javascript
    let done = false;

    function onTimeout() { endOfQuestion(); }
    function onEndCountdown(isPaused) { if (!isPaused) endOfQuestion(); }

    function endOfQuestion() {
        if (done)
            return;
        done = true;
        // ...
    }
    ```

## Compartir datos entre diapositivas

Las variables de un script desaparecen cuando se abandona su diapositiva, por lo que las variables ordinarias de JavaScript no sobreviven hasta la siguiente diapositiva. Para conservar datos entre diapositivas, utilice el almacenamiento global del objeto `qx`.

En la primera diapositiva de una ronda podría escribir:

```javascript
qx["roundname"] = "Movies";
```

y en cualquier diapositiva posterior:

```javascript
let roundName = qx["roundname"];   // "Movies"
```

Los valores permanecen hasta que se cierra QuizXpress Live, también cuando se reinicia el quiz. Para empezar de nuevo con un quiz reiniciado, borre los valores en el script de la primera diapositiva.

Para conservar una lista o un objeto, almacénelo como texto con `JSON.stringify()` y conviértalo de nuevo con `JSON.parse()`:

```javascript
let played = JSON.parse(qx['played'] || '[]');   // una lista vacía la primera vez
played.push(qx.slide.slideNumber);
qx['played'] = JSON.stringify(played);
```

## Mostrar valores del script en una diapositiva

Puede mostrar estos valores con nombre en una diapositiva con el símbolo de texto `[jsvar.<name>]`. Añada una forma de texto a la diapositiva e introduzca el símbolo, por ejemplo `[jsvar.roundname]`:

![Una forma de texto con el símbolo de texto jsvar](../../assets/images/js-jsvar-text-symbol.webp){ width="560" loading=lazy }

Defina la variable en el script:

![Definir la variable en el script](../../assets/images/js-jsvar-set-variable.webp){ width="560" loading=lazy }

Cuando el quiz se ejecuta, la diapositiva muestra el valor:

![El valor aparece en la diapositiva](../../assets/images/js-jsvar-result.webp){ loading=lazy }

Esto también funciona en tiempo real: cada vez que el script cambia el valor, la diapositiva muestra de inmediato el nuevo valor, también cuando cambia dentro de un temporizador. El [ejemplo del reloj](examples.md#reloj) lo utiliza para mostrar la hora actual.

## Cambiar la pregunta

Un script puede cambiar la pregunta, las respuestas y la respuesta correcta de la diapositiva actual, por ejemplo con una pregunta que haya descargado:

```javascript
function onLoadSlide(slide) {
    slide.setQuestion('What is the capital of Australia?');
    slide.setAnswers(['Sydney', 'Canberra', 'Melbourne', 'Perth']);
    slide.setCorrectAnswer('B');
}
```

- `setAnswers()` sustituye las respuestas en orden (A, B, C…). La diapositiva ya debe tener ese número de respuestas; no puede añadir respuestas.
- `setCorrectAnswer()` toma la letra de la respuesta correcta, o varias letras (`'AC'`) cuando hay más respuestas correctas.
- Hágalo en `onLoadSlide()`, antes de que se muestre la diapositiva.

Estos cambios son solo para el show: el archivo del quiz permanece como está. Con 'Test' en Studio la diapositiva tampoco cambia. Consulte el ejemplo [Preguntas de la web](examples.md#preguntas-de-la-web).

## Cambiar las puntuaciones

La puntuación de un jugador se puede leer y cambiar:

```javascript
team.score += 50;   // 50 puntos de bonificación
```

La bonificación se suma a la puntuación del equipo. En Analyzer, los resultados de una pregunta muestran solo los puntos de esa pregunta. En una pregunta de prueba la puntuación no cambia. Consulte el ejemplo [Bono de racha](examples.md#quizzes-de-ejemplo).

## Elegir la siguiente diapositiva

`onNextSlide(currentSlideNumber)` decide qué diapositiva viene a continuación, cuando la diapositiva no tiene definido 'Next slide'. Devuelva un número de diapositiva (empezando en 0), un id de diapositiva como `'#final'`, o una diapositiva de `qx.slides`. No devuelva nada para pasar sin más a la siguiente diapositiva.

```javascript
function onNextSlide(currentSlideNumber) {
    let leader = qx.leaderBoard[0];
    if (leader && leader.score >= 100)
        return '#final';
}
```

Asigne a las diapositivas un id o una clase en la sección 'Metadata' de las propiedades de la diapositiva, para que su script pueda encontrarlas. El ejemplo [Orden aleatorio de preguntas](examples.md#quizzes-de-ejemplo) elige la siguiente pregunta al azar.
