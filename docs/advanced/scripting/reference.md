# Reference

All handlers, objects, properties and functions that scripts can use. In the script editor, the template lists all handlers and the suggestions (type a dot or press Ctrl+Space) show the rest.

## Handlers

QuizXpress calls these functions when they exist in a slide's script. A handler that isn't defined changes nothing.

### The slide

| Handler | Called when… |
|---|---|
| `onLoadSlide(slide)` | The slide is shown. `slide` is the current [slide](#slide), the same as `qx.slide`. Can be `async` to `await` a [`fetch()`](#global-functions): QuizXpress Live waits for it before it shows the slide. |
| `onUnloadSlide(slide)` | The slide is about to be left, for any reason: next, previous or a jump from the Director. Clean up here, for example stop the music you started. |

### The countdown

| Handler | Called when… |
|---|---|
| `onStartCountdown()` | The countdown starts, or resumes after a pause. |
| `onCountdownTick(secondsLeft)` | Every second of the countdown. `secondsLeft` is the number on the clock. |
| `onEndCountdown(isPaused)` | The countdown stops. `isPaused` is `true` if the countdown was paused, `false` if it ended. |
| `onTimeout()` | The time to answer ran out. See [the end of a question](working-with-quizxpress.md#responding-to-the-show). |

### The answers

| Handler | Called when… |
|---|---|
| `onVote(player, answer, isCorrect)` | A team answered with the keypad (multiple choice, voting). `answer` is the answer as on the keypad, like `'A'`. `isCorrect` is `false` when the answer is wrong or the slide has no correct answer. Also called when a team changes its answer. |
| `onFastestFinger(player)` | A team pressed first on a fastest finger question. |
| `onCorrectAnswer(player)` | The answer of the fastest team was judged correct. |
| `onIncorrectAnswer(player)` | The answer of the fastest team was judged wrong. |
| `onScoreChanged(player, oldScore, newScore)` | The score of a team changed. |

`player` is a [player](#player).

### What is next

| Handler | Called when… |
|---|---|
| `onCommandNext()` | The 'next' command is given (button, key or remote control). Return `true` if the script handled the command and QuizXpress should ignore it; return `false` to let QuizXpress handle it as usual. |
| `onNextSlide(currentSlideNumber)` | QuizXpress is about to go to the next slide, and the slide has no 'Next slide' set. Return the slide to go to: a number (the slide number, starting at 0), a string with the slide id (for example `'#final'`), or a slide from `qx.slides`. Return nothing to go to the next slide. |

## qx

The global `qx` object is the entry point to QuizXpress.

| Name | Description | Example |
|---|---|---|
| `qx.slide` | The current [slide](#slide). | `let notes = qx.slide.notes;` |
| `qx.slides` | All slides in the quiz. | `let final = qx.slides.find(s => s.id === 'final');` |
| `qx.teams` | All teams, as [players](#player). | `let votedA = qx.teams.filter(t => t.lastVote === 'A').length;` |
| `qx.leaderBoard` | All teams sorted by score, the leader first. | `let leader = qx.leaderBoard[0];` |
| `qx.roundLeaderBoard` | The scores of the current round (since the last End of Round slide). Each entry has `team` (a [player](#player)) and `roundScore`. | `let best = qx.roundLeaderBoard[0].team.name;` |
| `qx.groups` | The names of the demographic groups. | |
| `qx["name"]` | Get or set a global named value, kept across slides and shown on a slide with `[jsvar.name]`. | `qx["roundname"] = "Geography";` |
| `qx.utils.message(text)` | Write a line to the log file of QuizXpress Live. | |
| `qx.sink` | QuizXpress Live itself, see [qx.sink](#qxsink). | `let player = qx.sink.playerFromDevice(10);` |

## slide

The current slide (`qx.slide`, or the `slide` argument of a handler), and the slides in `qx.slides`.

| Name | Description |
|---|---|
| `slide.slideType` | The type of slide, see [SlideType](#slidetype). |
| `slide.slideNumber` | The slide number, starting at 0. |
| `slide.question` | The text of the question. |
| `slide.answers` | Array with the texts of all answers. |
| `slide.correctAnswer` | The correct answer. |
| `slide.notes` | The slide notes. |
| `slide.category` | The category (topic) of the slide. |
| `slide.hasVideo` | `true` if the slide has a video. |
| `slide.hasAudio` | `true` if the slide has audio. |
| `slide.isPictureQuestion` | `true` if this is a picture question. |
| `slide.answerTime` | The countdown time in seconds. |
| `slide.pointsAtStart` | Points at the start of the question. |
| `slide.pointsAtEnd` | Points at the end of the question. |
| `slide.penaltyPointsAtStart` | Penalty points (wrong answer) at the start. |
| `slide.penaltyPointsAtEnd` | Penalty points at the end. |
| `slide.id` | The slide id ('Metadata' section of the slide properties). |
| `slide.class` | The slide class ('Metadata' section of the slide properties). |
| `slide["fieldName"]` | Read a [custom slide field](../custom-data-fields.md), for example `slide["DasLightScene"]`. |
| `slide.setQuestion(text)` | Replace the question text, for this show only. |
| `slide.setAnswers(answers)` | Replace the answers in order (A, B, C…), for this show only. At most as many answers as the slide has. |
| `slide.setCorrectAnswer(letters)` | Set the correct answer: `'B'`, or `'AC'` when more answers are correct. For this show only. |

See [Changing the question](working-with-quizxpress.md#changing-the-question).

### SlideType

The global `SlideType` gives the slide types by name:

```javascript
if (slide.slideType === SlideType.Question) {
    console.log("It's a question!");
}
```

`SlideType.Question`, `TestQuestion`, `Banner` (billboard), `EndOfRound`, `Demographic`, `LastManStanding`, `AudienceResponse`, `Wager`, `Minigame`, `MajorityRules`, `JeopardyRound` (Trivia Board round), `TriviaLadderRound`, `BingoRound`, `TriviaFeud`, `SpeedRound`, `PairingQuestion`.

## player

The objects in `qx.teams` and `qx.leaderBoard`, the `player` argument of handlers, and those returned by `playerFromDevice` and `winnerOfLastQuestion`.

| Name | Description |
|---|---|
| `player.name` | Get or set the player's name. |
| `player.group` | The player's demographic group. |
| `player.lastVote` | The last answer received, like `'A'`. |
| `player.keypad` | The player's keypad number. |
| `player.score` | Get or set the current score. See [Changing scores](working-with-quizxpress.md#changing-scores). |
| `player.excluded` | Get or set whether the player is excluded. |
| `player.timeUsed` | Time used (decimal number). |
| `player.isMobilePlayer` | `true` if the player is connected through a mobile device. |
| `player.id` | Unique id (GUID) of the player. |

## qx.sink

| Name | Description |
|---|---|
| `qx.sink.gotoSlide(slideNumber)` | Jump to a slide (number starting at 0). |
| `qx.sink.endQuiz()` | End the quiz. |
| `qx.sink.restartQuiz()` | Restart the quiz. |
| `qx.sink.playerFromDevice(device)` | The [player](#player) on a device number. |
| `qx.sink.winnerOfLastQuestion` | The [player](#player) who won the last question. |
| `qx.sink.players` | All players. |
| `qx.sink.quizFile` | The file name of the running quiz. |
| `qx.sink.keypads` | Access to the buzzer subsystem. |
| `qx.sink.sound` | Access to the [sound subsystem](#sound). |

## sound

Available as `qx.sink.sound`.

| Name | Description | Example |
|---|---|---|
| `loadMusic(name, filename, loop)` | Load a sound file from disk under a name. | `qx.sink.sound.loadMusic("song1", "C:\\Music\\song1.mp3", false);` |
| `playMusic(name)` | Play a loaded sound, or continue after `pauseMusic()`. | `qx.sink.sound.playMusic("song1");` |
| `pauseMusic(name)` | Pause playing. | `qx.sink.sound.pauseMusic("song1");` |
| `stopMusic(name)` | Stop playing. | `qx.sink.sound.stopMusic("song1");` |
| `unloadMusic(name)` | Unload the sound and free its resources. | `qx.sink.sound.unloadMusic("song1");` |
| `setMusicVolume(name, volume)` | Set the volume of one sound (0–100). | `qx.sink.sound.setMusicVolume("song1", 50);` |
| `setVolume(volume)` | Set the playback volume (0–100). | |
| `startPlaylist(files[], volume)` | Start playing a list of songs. | |
| `endPlaylist()` | Stop the playlist. | |
| `playBuzzerSound(keypad)` | Play the buzzer sound for a keypad. | |

!!! tip
    In JavaScript strings, a backslash must be doubled: write Windows paths as `"C:\\Music\\song1.mp3"`.

Always stop the music you started in `onUnloadSlide()`: the quizmaster can leave the slide at any moment. With 'Test' in Studio, the sound functions do nothing.

## Global functions

| Name | Description | Example |
|---|---|---|
| `console.log(…)`, `console.info(…)`, `console.warn(…)`, `console.error(…)` | Write to the [script console](debugging.md). | `console.log("Votes:", votes);` |
| `fetch(url)` | Download a web page or the response of a web service. Gives an object with `status` (like 200), `statusText` and `text`. Waits at most 10 seconds; when it fails, it throws an error you can catch. See [Questions from the web](examples.md#questions-from-the-web). | `let response = await fetch(url);` |
| `setTimeout(function, ms)` | Run a function once, after a number of milliseconds. | `setTimeout(() => console.log('later'), 2000);` |
| `setInterval(function, ms)` | Run a function repeatedly. Returns an id for `clearInterval()`. Stops automatically when the slide is left. | See the [Clock example](examples.md#clock). |
| `clearInterval(id)` | Stop a `setInterval()`. | |
| `sendUDP(ip, port, message)` | Send a text message over UDP (no error handling). | `sendUDP("127.0.0.1", 53432, "start");` |
| `sendTCP(ip, port, message)` | Send a text message over TCP. | `sendTCP("127.0.0.1", 53432, "end");` |
| `sendOSC(ip, port, oscaddress, p1, [p2])` | Send data to an OSC handler. | `sendOSC("127.0.0.1", 4532, "/scene1", 20);` |
| `getEnv("name")` | The value of an environment variable. | `let port = getEnv("DASLIGHT_PORT");` |
| `sleep(ms)` | Wait a number of milliseconds. The show waits too, so keep it short. | |
| `alert(message)` | Show a message box. For debugging only; it halts the show. Use `console.log()` instead. | `alert("hello world");` |
