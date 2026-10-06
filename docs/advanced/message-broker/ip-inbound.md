# IP inbound channel

With the inbound channel, external applications send text commands to QuizXpress, for example to advance to the next slide, judge an answer or change a score. Commands can arrive over UDP, TCP or Telnet.

Configure it on the 'IP Inbound' tab of the [Message Broker settings](index.md#opening-the-message-broker-settings):

![The IP Inbound tab](../../assets/images/mb-ip-inbound-tab.webp){ width="320" loading=lazy }

## Settings

**On/Off**
:   Turns inbound messages on or off.

**Protocol**
:   Endpoints for UDP, TCP and Telnet. You can enable all three at the same time, but each needs its own port number. The default Telnet port is 23.

**Settings**
:   Shows this computer's IP address, which the sending side needs. 'Diagnostics' opens a window that prints every incoming message.

!!! warning
    The diagnostics window is for testing only. Don't leave it on during a live show.

## Commands

These commands work over both Telnet and a TCP socket:

| Command | What it does |
|---|---|
| `next` | Advance, for example to the next slide. |
| `showleaderboard` | Show the general scoreboard. |
| `showresponsechart` | Show the response chart after a multiple-choice question. |
| `judgecorrect` | Judge an open or manual question as correct. |
| `judgeincorrect` | Judge an open or manual question as incorrect. |
| `pausetimer` | Pause the countdown timer. |
| `resumetimer` | Resume the countdown timer. |
| `endquiz` | End the quiz and go to the final score screen. |
| `goto` | Go to a slide by number or by slide id, for example `goto 10` or `goto #banner1`. The id is a unique text value you can set on a slide. |
| `enableallplayers` | Enable all registered players. |
| `selectplayer` | Enable the player on the given device number and exclude all others. |
| `selectplayers` | Enable a range of players, such as `1-5` or `1,2,10`, and exclude everyone else. |
| `addplayer` | Add a player with a device number and name, for example `addplayer 1 "John Trivialta"`. |
| `addscore` | Add points to a player's score. |
| `setscore` | Set a player's score. |
| `setteamname` | Set the team name for a device, for example `setteamname 1 "John Trivialta"`. |
| `setvolume` | Set the quiz player volume (0–100). |
| `buzz` | Send a vote for a player, for example `buzz 1 FF`. |
| `buzzwithtext` | Send a text vote, for numeric, letter or full-text questions. |
| `getcurrentscreen` | Return the current screen: `WelcomeScreen`, `SignOnScreen`, `CountdownScreen`, `QuizScreen` or `FinalScoreScreen`. |
| `getplayers` | Return all players with their attributes (score, name, device and so on). Use the `-f` switch to choose the format: `json` or `ocs`. |
| `getquiz` | Return a full export of the quiz in XML, without pictures, sound or video. This can be a lot of data. |
| `getslide` | Return the details of one slide in XML, without pictures, sound or video, for example `getslide 10`. |

Example output of `getplayers`:

![Example output of getplayers](../../assets/images/mb-getplayers-example.webp){ loading=lazy }

Example output of `getslide 10`:

![Example output of getslide](../../assets/images/mb-getslide-example.webp){ loading=lazy }

## Trying commands with Telnet

Telnet is the easiest way to try commands by hand or to debug. Windows doesn't include the Telnet client by default; to install it:

1. Open 'Control Panel'.
2. Open 'Programs'.
3. Select 'Turn Windows features on or off'.
4. Tick 'Telnet Client'.
5. Click 'OK'. Windows searches for the required files and installs the client.

Then open a command prompt and type `telnet localhost` (assuming QuizXpress uses the default port 23). A Telnet window opens with the prompt `qx>`. Type `help` to see all commands, or `help <command>` for help on one command:

![Telnet session with the help command](../../assets/images/mb-telnet-help.webp){ loading=lazy }
