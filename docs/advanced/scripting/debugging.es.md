# Pruebas y depuración

QuizXpress dispone de una consola de scripts, como la consola de un navegador web. Muestra lo que su script escribe con `console.log()` y cada error de un script, con la diapositiva, la línea y la columna donde ocurrió.

## Escribir en la consola

```javascript
console.log('Slide ' + (slide.slideNumber + 1) + ': ' + slide.question);
console.warn('No music file set');
console.error('Something went wrong');
```

`console.log()`, `console.info()`, `console.warn()` y `console.error()` aceptan cualquier número de valores, también objetos y matrices. Las advertencias y los errores se cuentan por separado, para que destaquen.

!!! tip
    Utilice `console.log()` en lugar de `alert()`. `alert()` muestra un cuadro de mensaje que detiene todo el quiz hasta que alguien lo cierra.

## En Quiz Studio

La consola se encuentra debajo del editor de scripts. Haga clic en 'Test' para ejecutar el script: su salida aparece en la consola, seguida de 'Test run finished'. Cuando el script falla, la consola muestra el error y el editor marca la línea. Haga doble clic en un mensaje para ir a su línea en el script.

- 'Clear' vacía la consola, 'Copy' copia todos los mensajes, por ejemplo para pedir ayuda a un asistente de IA.
- 'Errors' y 'Warnings' muestran cuántos hay.
- Los mensajes que se repiten, por ejemplo los de un temporizador, se agrupan en una sola línea con un contador.

## Durante un show

Un error de script nunca detiene el show: QuizXpress lo notifica y continúa. La consola de scripts de QuizXpress Director muestra lo que han hecho los scripts. Nunca se muestra en la pantalla proyectada.

En cuanto un script escribe en la consola o falla, el Director muestra un botón 'Script' entre los botones de comando, con el número de errores. Haga clic en el botón para abrir la consola de scripts.

La visibilidad de la consola es una opción. Haga clic con el botón derecho en los botones de comando del Director y elija 'Script errors':

| Opción | Qué hace |
|---|---|
| 'Automatic (open the console when testing from Quiz Studio)' | Cuando prueba el quiz desde Quiz Studio, la consola se abre en el primer error. En un show real, solo aparece el botón. Es el valor predeterminado. |
| 'Show a button with the number of errors' | Solo el botón. |
| 'Open the console on the first error' | La consola se abre en el primer error, también en un show real. |
| 'Do not show' | Ni botón ni consola. |

'Open script console' en el mismo menú abre la consola en cualquier momento.

!!! tip
    La consola también es un buen lugar para información destinada al presentador del quiz. El ejemplo [Preguntas de la web](examples.md#preguntas-de-la-web) escribe en la consola la pregunta que descargó, con la respuesta correcta marcada.
