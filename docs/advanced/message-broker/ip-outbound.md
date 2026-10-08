# IP outbound channel

With the outbound channel, QuizXpress sends a message whenever something happens in the quiz, such as a slide change, a buzzer press or a score change. Your own application listens for these messages and responds, for example by driving an external scoreboard or a light show.

Turn it on in the 'IP Outbound' tab of the [Message Broker settings](index.md#opening-the-message-broker-settings):

![The IP Outbound tab](../../assets/images/mb-ip-outbound-tab.webp){ width="320" loading=lazy }

## Settings

**On/Off**
:   Turns the outbound channel on or off.

**Test**
:   Opens a test form where you can trigger events by hand:

    ![Outbound channel test form](../../assets/images/mb-outbound-test-form.webp){ width="560" loading=lazy }

**Send a heartbeat message every second**
:   Sends a heartbeat message every second, so the receiving side can tell that the quiz player is still running. Use it to detect a connection that dropped unexpectedly; a normal session always starts with `/start` and ends with `/close`.

**Send input from keypads/buzzers**
:   Relays every keypad and buzzer press. This is optional because it can produce a lot of messages.

**Send score changes**
:   Sends a message whenever a player's score changes, for example to drive external scoreboards.

**Send countdown tick**
:   Sends the remaining time every second while the countdown runs.

**Number slides from 1 (also MIDI triggers)**
:   Slide numbers in `/slidechanged`, `/slideinfo` and the MIDI 'Slide Changed' trigger start at 1, as in Studio and in the inbound `goto` and `getslide` commands. When it's off, they start at 0, as in earlier versions; keep it off if your application or MIDI configuration already counts from 0.

**Send slide details (/slideinfo)**
:   Sends the question, the answers and the correct answer of every new slide. See [Slide details and leaderboard](#slide-details-and-leaderboard).

**Send the leaderboard (/leaderboard)**
:   Sends all teams in ranking order after scores change. See [Slide details and leaderboard](#slide-details-and-leaderboard).

**Send text answers as /textvote**
:   Text answers from keypads (numbers, letters, full text) are sent as `/textvote` instead of `/buzz`, so your application can tell them apart from button presses. When it's off, both are sent as `/buzz`, as in earlier versions. Needs 'Send input from keypads/buzzers'.

**Protocol**
:   - **UDP/ASCII:** plain ASCII text, parameters separated by spaces.
    - **UDP/UTF8:** the same, encoded as UTF-8. Choose this when team names or answers contain accented characters.
    - **UDP/OSC:** messages in [Open Sound Control (OSC)](https://en.wikipedia.org/wiki/Open_Sound_Control) format, which [Max](https://cycling74.com/), QLab, TouchOSC and similar tools can process directly. Numbers are sent as 32-bit integers and text as UTF-8 strings.

**Server address**
:   The IP address of the computer that receives the messages. Use `127.0.0.1` if it's the same computer.

**Server port**
:   The port number the receiving application listens on.

!!! tip
    The [message log](index.md#message-log) shows every message that goes out, so you can check what your application should receive.

## Messages

The receiving side opens a UDP socket. Messages are plain strings in the format `/message {parameter1} {parameter2} …`. Every session starts with `/start` and ends with `/close`.

| Message | Meaning |
|---|---|
| `/start` | Start of the session. |
| `/close` | End of the session: QuizXpress Live is closing. |
| `/heartbeat {counter}` | Sent every second with an increasing counter, for example `/heartbeat 2345`. |
| `/countdowntick {remainingtimeMs}` | Sent every second while the countdown runs, with the remaining time in milliseconds, for example `/countdowntick 23100`. |
| `/slidechanged {old#} {new#} {questiontype} {slide class} {slide id}` | A new slide is shown. The class and id are optional and set in the slide's metadata in Studio, so you can react to a class or id instead of a slide number that changes when slides are reordered. Example: `/slidechanged 6 7 question MySpecialSlideType banner1`. With 'Number slides from 1', `0` as the old number means there was no previous slide. |
| `/command {command}` | A command from the quizmaster remote control: `power`, `scores`, `chart`, `leaderboard`, `groupchart`, `up`, `down`, `pause`, `questionmark`, `next`, `wrong` or `right`. Example: `/command up`. |
| `/buzz {device} {key}` | A key press on a device, for example `/buzz 10 A`, or `/buzz 8 RED` for the fastest-finger button. Text answers are also sent as `/buzz`, unless 'Send text answers as /textvote' is on. |
| `/textvote {device} {text}` | A text answer from a device, for example `/textvote 8 Paris`. Only with 'Send text answers as /textvote'. |
| `/fastestfinger {device}` | The device that was first in a fastest-finger question. |
| `/screenchanged {screentype}` | The quiz player switched screens: `welcomescreen`, `signonscreen`, `countdownscreen`, `quizscreen` or `finalscorescreen`. Example: `/screenchanged countdownscreen`. |
| `/timeout` | The question timed out without a correct answer. |
| `/startcountdown` | The question countdown started. |
| `/pausecountdown` | The countdown is paused; the system is idle. |
| `/endcountdown` | The countdown stopped; the question is over. |
| `/correct` | An answer to the current question was judged correct. |
| `/incorrect` | An answer to the current question was judged wrong. |
| `/restart` | The quiz was restarted from the final score screen. |
| `/scorechanged {device} {teamname} {old score} {new score}` | A team's score changed. Example: `/scorechanged 10 'John Trivialta' 5 10` means team 'John Trivialta' on device 10 went from 5 to 10 points. In OSC the team name is a string without the quotes. |
| `/claimbingo` | A player claimed Bingo. |
| `/falsebingo` | A claimed Bingo turned out to be false. |
| `/bingo` | A claimed Bingo is valid. |
| `/slideinfo {json}` | The details of the new slide, sent right after `/slidechanged`. Only with 'Send slide details'. |
| `/leaderboard {json}` | All teams in ranking order. Only with 'Send the leaderboard'. |

Example of the messages during a quiz:

![Example outbound messages](../../assets/images/mb-outbound-example-messages.webp){ loading=lazy }

## Slide details and leaderboard

`/slideinfo` and `/leaderboard` carry [JSON](https://www.json.org/) on a single line, which most tools can read directly (Node-RED, Max with `dict.deserialize`, Bitfocus Companion, Python). In OSC the JSON is one string argument. With UDP/ASCII, accented characters are written as `\u` codes, which every JSON reader turns back into the right character.

`/slideinfo` is sent right after `/slidechanged`, for example:

```
/slideinfo {"number":44,"previous":45,"type":"question","question":"Which aircraft type has recently been added?","answers":["A340","A380","B787"],"correctAnswer":"C","category":"Default Category","answerTime":30,"points":10,"class":"","id":""}
```

| Field | Meaning |
|---|---|
| `number`, `previous` | The new and the previous slide number, counted as set by 'Number slides from 1'. |
| `type` | The slide type, the same as in `/slidechanged`. |
| `question`, `answers` | The question text and the answers, in the order of the slide. |
| `correctAnswer` | The correct answer, for example `C` for the third answer. |
| `category`, `answerTime`, `points` | The category, the answer time in seconds and the points for a correct answer. |
| `class`, `id` | The slide class and id from the slide's metadata in Studio. |

!!! warning
    `/slideinfo` contains the correct answer as soon as the slide appears. Don't show it on a screen the players can see before the answer is revealed.

`/leaderboard` is sent after scores change. When many scores change at once, for example at the end of a question, you get one leaderboard after the last change instead of one per team:

```
/leaderboard [{"rank":1,"device":2,"name":"Brainiacs","group":"","score":30},{"rank":2,"device":1,"name":"Zoë's Team","group":"","score":10},{"rank":2,"device":3,"name":"Quizzers","group":"","score":10}]
```

Teams with the same score share a rank, and the next rank is skipped (1, 2, 2, 4). `group` is the team's demographic group, if any.

## Example: a simple UDP listener

This C# console application (.NET Framework 4.8) listens on port 12345 and prints every message it receives. Set the 'Server port' in Message Broker to the same number.

```csharp
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class UDPServer
{
    static void Main(string[] args)
    {
        int port = 12345; // The port to listen on
        UdpClient udpListener = new UdpClient(port);
        Console.WriteLine($"UDP server is listening on port {port}");

        try
        {
            while (true)
            {
                IPEndPoint senderEndPoint = new IPEndPoint(IPAddress.Any, port);
                byte[] receivedBytes = udpListener.Receive(ref senderEndPoint);
                string receivedText = Encoding.UTF8.GetString(receivedBytes);
                Console.WriteLine($"Received: {receivedText}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
        }
        finally
        {
            udpListener.Close();
        }
    }
}
```
