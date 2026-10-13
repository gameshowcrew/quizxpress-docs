# Rock Paper Scissors

In the Rock Paper Scissors minigame, the audience plays against a virtual opponent.
Players choose rock, paper or scissors on their buzzer, keypad or phone. The computer's
hand moves up and down three times before revealing its choice.

![Rock Paper Scissors voting screen with the white hand style](../../assets/images/rock-paper-scissors-voting.webp){ loading=lazy }

## Playing a round

1. Start the game. The studio appears and the background music starts.
2. Use 'Next' to open voting.
3. Players press **A for rock**, **B for paper** or **C for scissors**. Only their first
   valid choice counts in each round; further votes are ignored.
4. Use 'Next' to close voting and play the hand animation. The music stops, and sound
   effects accompany the three movements and the reveal.
5. After the reveal, use 'Next' to show the round results and eliminate losing players.
   Their tiles disappear with an animation and sound effect. The remaining tiles move
   into a new layout.
6. Use 'Next' to open the following round, or finish the game when the selected game
   mode has reached its end.

The usual rules apply: rock beats scissors, scissors beats paper, and paper beats rock.
Players who choose the same gesture as the computer stay in the game, but do not earn
the points for a correct answer. Players who lose, or do not submit a valid choice
before voting closes, are eliminated.

!!! tip
    For example, if the computer reveals rock, players who chose paper win the round,
    players who chose rock tie, and players who chose scissors are eliminated.

![Round results with the neon hand style and the remaining players](../../assets/images/rock-paper-scissors-results.webp){ loading=lazy }

## Game mode and scoring

![Rock Paper Scissors settings with hand previews and voting colors](../../assets/images/rock-paper-scissors-settings.webp){ width="600" loading=lazy }

Open the game's settings to choose a game mode:

- **'Rounds'**: play a set number of rounds. 'Number of rounds' must be at least **1**.
- **'Last man standing'**: continue until exactly one player remains, or everyone has
  been eliminated. 'Number of rounds' is disabled in this mode.

'Points for survivors' sets the bonus awarded to players who survive the game.
'Points for every right answer' sets the points awarded for beating the computer in
a round. A tied answer keeps the player in the game without awarding these round points.

### The finger surprise

'Chance for the finger to appear' sets the percentage chance of the computer revealing
a middle finger instead of rock, paper or scissors. This is a playful fake elimination:
the audience appears to be out, but their tiles return and the game continues.

Set the chance to **0** to disable this surprise.

## Appearance

### Hand style

Choose a hand style using the picture previews in the settings:

- **White**: a classic white cartoon glove.
- **Neon**: a glowing purple hand with cyan and pink accents.
- **Comic**: a bold red comic-style hand.
- **Robot**: an angular robotic hand.

The selected style is used for the main animation, the rock/paper/scissors choice
pictures and the player choice icons. The choice panels and player tiles also match
the hand style.

### Background

The default background is an animated neon gameshow studio. Use the 'Background image'
picker to select your own still image. Clear the custom image to return to the default
studio.

### Player voting colors

Choose the colors for rock, paper and scissors under 'Player voting colors'. The
defaults are gray, light green and red.

Enable 'Show player voting colors while voting' to show each player's choice while
voting is still open. When this is disabled, tiles indicate that the player has voted,
and their choice is shown after the computer reveals its hand.

## Player tiles and large groups

The player area adapts automatically to the number of remaining players:

- Small groups show player numbers and names. Longer names use up to two lines.
- Larger groups use compact tiles with player numbers.
- For very large groups, tiles show player status without a number if the number would
  be too small to read.

The number display depends on the available space and the size of the game window,
so there is no fixed player count at which numbers appear. As players are eliminated,
the layout is recalculated and numbers reappear when there is enough room. Names and
choice icons return as the group becomes smaller.

Eliminated players are automatically removed after the elimination animation. There
is no separate player display mode or 'Hide expelled players' setting to select.

## Sound

The game includes background music and effects for the hand movements, the reveal
and the disappearance of eliminated players. The background music starts when the
game opens and plays during voting. It stops when the hand animation begins.

Under 'Sound', use 'Music during voting' to choose your own music. The play button
previews your selection; the clear button restores the game's default music.

!!! note
    The standard music and sound effects are included with the game. No separate
    sound files need to be installed.

## Custom messages

Enable 'Use custom texts' to replace the default messages:

- **'Voting text'**: the heading displayed while players choose.
- **'Winner'**: the message displayed when one player remains.
- **'All out'**: the message displayed when everyone has been eliminated.

Use the reset button to restore the default messages.
