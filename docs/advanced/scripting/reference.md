# Reference

All objects, properties and functions that scripts can use.

## Handlers

QuizXpress calls these functions when they exist in a slide's script. The script editor's default template contains all of them, commented out.

| Handler | Called when… |
|---|---|
| `onLoadSlide(slide)` | The slide is loaded. `slide` is the current [slide object](#slide). |
| `onStartCountdown()` | The countdown starts. |
| `onEndCountdown(isPaused)` | The countdown ends. `isPaused` is `true` if the countdown was paused, `false` if it ended normally. |
| `onCommandNext()` | The 'next' command is given. Return `true` if the script handled the command and QuizXpress should ignore it; return `false` to let QuizXpress handle it as usual. |
| `onNextSlide(currentSlideNumber)` | QuizXpress is about to go to the next slide. Return the slide to go to: a number (the 0-based slide index), a string with the slide id (for example `"#slide1"`), or a slide object from `qx.slides`. |
| `onCorrectAnswer(player)` | A fastest-finger question is judged correct. `player` is the [player](#player) who buzzed. |
| `onIncorrectAnswer(player)` | A fastest-finger question is judged wrong. `player` is the [player](#player) who buzzed. |

## qx

The global `qx` object is the entry point to QuizXpress.

| Name | Description | Example |
|---|---|---|
| `qx.slide` | The current slide. | `let notes = qx.slide.notes;` |
| `qx.slides` | All slides in the quiz. | `let roundA = qx.slides.find(s => s.class === 'roundA');` |
| `qx.teams` | All active players. | `let votedA = qx.teams.filter(t => t.lastVote === 'A').length;` |
| `qx["name"]` | Get or set a global named variable, kept across slides and shown with `[jsvar.name]`. | `qx["roundname"] = "Geography";` |
| `qx.utils` | Script utilities. | `qx.utils.message("Hello");` |
| `qx.sink` | The QuizXpress [sink object](#qxsink). | `let player = qx.sink.playerFromDevice(10);` |

## slide

| Name | Description |
|---|---|
| `slide.slideType` | The type of slide, as a number (see [Slide types](#slide-types)). |
| `slide.slideNumber` | The slide index, starting at 0. |
| `slide.question` | The text of the question element. |
| `slide.answers` | Array with the text of all answers. |
| `slide.correctAnswer` | The correct answer. |
| `slide.notes` | The slide notes. |
| `slide.hasVideo` | `true` if the slide has a video. |
| `slide.hasAudio` | `true` if the slide has audio. |
| `slide.isPictureQuestion` | `true` if this is a picture question. |
| `slide.answerTime` | The countdown time in seconds. |
| `slide.pointsAtStart` | Points at the start of the question. |
| `slide.pointsAtEnd` | Points at the end of the question. |
| `slide.penaltyPointsAtStart` | Penalty points (wrong answer) at the start. |
| `slide.penaltyPointsAtEnd` | Penalty points at the end. |
| `slide.class` | The slide class. |
| `slide.id` | The slide id. |
| `slide["fieldName"]` | Read a [custom slide field](../custom-data-fields.md), for example `slide["DasLightScene"]`. |

### Slide types

`slide.slideType` is a number. Copy this into your script to work with names instead:

```javascript
const PluginSlideType = {
    Unknown: 0,
    Question: 1,
    TestQuestion: 2,
    Banner: 3,
    EndOfRound: 4,
    Demographic: 5,
    LastManStanding: 6,
    AudienceResponse: 7,
    Wager: 8,
    Minigame: 9,
    MajorityRules: 10,
    JeopardyRound: 11,   // Trivia Board round
    TriviaLadderRound: 12,
    BingoRound: 13,
    TriviaFeud: 14,
    SpeedRound: 15
};

if (slide.slideType === PluginSlideType.Question) {
    alert("It's a question!");
}
```

## qx.sink

| Name | Description |
|---|---|
| `qx.sink.keypads` | Access to the buzzer subsystem. |
| `qx.sink.playerFromDevice(device)` | The [player](#player) on a device number. |
| `qx.sink.winnerOfLastQuestion` | The [player](#player) who won the last question. |
| `qx.sink.quizFile` | The name of the running quiz. |
| `qx.sink.sound` | Access to the [sound subsystem](#sound). |
| `qx.sink.gotoSlide(slideNo)` | Jump to a specific slide. |
| `qx.sink.endQuiz()` | End the quiz player immediately. |

## player

The objects in `qx.teams`, and those returned by `playerFromDevice` and `winnerOfLastQuestion`.

| Name | Description |
|---|---|
| `player.name` | Get or set the player's name. |
| `player.group` | The player's group name. |
| `player.lastVote` | The last vote received. |
| `player.keypad` | The player's keypad number. |
| `player.score` | Get or set the current score. |
| `player.excluded` | Get or set whether the player is excluded. |
| `player.timeUsed` | Time used (decimal number). |
| `player.isMobilePlayer` | `true` if the player is connected through a mobile device. |
| `player.id` | Unique id (GUID) of the player. |

## sound

Available as `qx.sink.sound`.

| Name | Description | Example |
|---|---|---|
| `loadMusic(name, filename, loop)` | Load a sound file from disk under a name. | `qx.sink.sound.loadMusic("song1", "C:\\Music\\song1.mp3", false);` |
| `playMusic(name)` | Play a loaded sound. | `qx.sink.sound.playMusic("song1");` |
| `stopMusic(name)` | Stop playing. | `qx.sink.sound.stopMusic("song1");` |
| `unloadMusic(name)` | Unload the sound and free its resources. | `qx.sink.sound.unloadMusic("song1");` |
| `setVolume(volume)` | Set the playback volume (0–100). | |
| `startPlaylist(files[], volume)` | Start playing a list of songs. | |
| `endPlaylist()` | Stop the playlist. | |
| `playBuzzerSound(keypad)` | Play the buzzer sound for a keypad. | |

!!! tip
    In JavaScript strings, a backslash must be doubled: write Windows paths as `"C:\\Music\\song1.mp3"`.

## Global functions

| Name | Description | Example |
|---|---|---|
| `sendUDP(ip, port, message)` | Send a text message over UDP (no error handling). | `sendUDP("127.0.0.1", 53432, "start");` |
| `sendTCP(ip, port, message)` | Send a text message over TCP. | `sendTCP("127.0.0.1", 53432, "end");` |
| `sendOSC(ip, port, oscaddress, p1, [p2])` | Send data to an OSC handler. | `sendOSC("127.0.0.1", 4532, "/scene1", 20);` |
| `getEnv("name")` | The value of an environment variable. | `let port = getEnv("DASLIGHT_PORT");` |
| `fetch(url)` | Fetch text data from a web address. See the [stock ticker example](examples.md#get-data-from-a-web-service). | |
| `alert(message)` | Show a message box. For debugging only; it halts the show. | `alert("hello world");` |
| `setTimeout`, `setInterval`, `clearInterval` | Standard JavaScript timers. | See the [Clock example](examples.md#clock). |
