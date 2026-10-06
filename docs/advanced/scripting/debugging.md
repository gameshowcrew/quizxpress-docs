# Testing and debugging

QuizXpress has a script console, like the console of a web browser. It shows what your script writes with `console.log()`, and every error in a script with the slide, the line and the column where it happened.

## Writing to the console

```javascript
console.log('Slide ' + (slide.slideNumber + 1) + ': ' + slide.question);
console.warn('No music file set');
console.error('Something went wrong');
```

`console.log()`, `console.info()`, `console.warn()` and `console.error()` take any number of values, also objects and arrays. Warnings and errors are counted separately, so they stand out.

!!! tip
    Use `console.log()` instead of `alert()`. `alert()` shows a message box that halts the whole quiz until someone closes it.

## In Quiz Studio

The console sits below the script editor. Click 'Test' to run the script: its output appears in the console, followed by 'Test run finished'. When the script fails, the console shows the error and the editor marks the line. Double-click a message to go to its line in the script.

- 'Clear' empties the console, 'Copy' copies all messages, for example to ask an AI assistant for help.
- 'Errors' and 'Warnings' show how many there are.
- Messages that repeat, for example from a timer, are collapsed into one line with a count.

## During a show

A script error never stops the show: QuizXpress reports it and goes on. The script console of QuizXpress Director shows what the scripts did. It is never shown on the projected screen.

As soon as a script writes to the console or fails, the Director shows a 'Script' button among the command buttons, with the number of errors on it. Click the button to open the script console.

How visible the console is, is an option. Right-click the command buttons of the Director and choose 'Script errors':

| Option | What it does |
|---|---|
| 'Automatic (open the console when testing from Quiz Studio)' | When you test the quiz from Quiz Studio, the console opens on the first error. In a real show, you only get the button. This is the default. |
| 'Show a button with the number of errors' | Only the button. |
| 'Open the console on the first error' | The console opens on the first error, also in a real show. |
| 'Do not show' | No button and no console. |

'Open script console' in the same menu opens the console at any moment.

!!! tip
    The console is also a good place for information for the quizmaster. The [Questions from the web](examples.md#questions-from-the-web) example writes the question it downloaded, with the correct answer marked, to the console.
