# Sound

Sound fragments can be used for questions such as “Who wrote this song?”, “What bird is singing here?”, or “What is this noise?”. To make things interesting, you can vary the speed of the sound over time by setting the ‘Speed from’ (playback speed percentage when the sound starts playing) and ‘Speed to’ (playback speed at the end of the sound fragment) properties. Likewise, you can vary the pitch of the sound.

## Inserting a sound file

To add a sound fragment to a quiz slide, select the INSERT ribbon tab and click the ‘Audio’ button, then select an mp3 or wav file and select whether to link or embed the file:

![](../../assets/images/image206.webp){ width="321" loading=lazy }

Linking results in smaller, more manageable quiz files, but you’ll have to make sure all external files remain accessible — either at their original path or in the folder where the quiz file is stored (alternatively, you can keep the files external and pack your quiz before distributing it).

Once the file is inserted, the AUDIO contextual ribbon tab becomes visible to configure the various options.

![The AUDIO ribbon tab](../../assets/images/image207.webp){ width="720" loading=lazy }

## Trimming a sound

Usually you only want to play part of a song or recording: the chorus, the intro, or just the few seconds that give the answer away. The trim editor shows the sound as a waveform, so you can see where the music starts, where it gets loud and where it fades out, and choose the part to play by listening to it.

The trim editor doesn't change the sound file itself. It only sets the sound's start and end time, so you can always go back to the whole track.

### Opening the trim editor

Select the sound icon on the slide, then use one of these:

- Click the ‘Trim’ button in the ‘Timing’ group on the AUDIO ribbon tab, next to the start and stop times. The small arrow in the bottom-right corner of the ‘Timing’ group opens the same editor.

    ![The Trim button on the AUDIO ribbon tab](../../assets/images/sound-ribbon-trim-button.webp){ width="420" loading=lazy }

- Right-click the sound icon on the slide and choose ‘Trim sound...’.

    ![Trim sound in the sound's context menu](../../assets/images/sound-context-menu-trim.webp){ width="240" loading=lazy }

!!! note
    You can't trim Spotify tracks and MIDI files, or a linked sound file that can't be found. The ‘Trim’ button is greyed out for these.

### Choosing the part to play

![The trim editor](../../assets/images/sound-trim-editor.webp){ loading=lazy }

The part that will play is highlighted in blue. To change it:

- **Drag across the waveform** to select a new part, or drag the markers at the start and end of the selection.
- **Type the times** in the ‘Start’ and ‘End’ boxes. You can enter seconds (`75`), minutes and seconds (`1:15`) or hours, minutes and seconds (`0:01:15`), with decimals if you like (`1:15.5`). ‘Length’ shows how long the selected part plays.
- **Set the start or end while listening**: click ‘Set start (I)’ or ‘Set end (O)’, or press I or O on the keyboard, at the exact moment you hear the right spot. When no sound is playing, these buttons use the cursor position instead.
- **‘Whole track’** selects the complete sound again.

Click anywhere in the waveform to place the cursor (the orange line).

To listen:

- ‘Play selection’ (or the Space bar) plays the selected part. Press Space again to stop.
- ‘Play from cursor’ plays from the cursor to the end of the sound.
- While the sound is playing, click the waveform to jump to that spot.

The display next to the buttons shows the current position and the total length of the sound.

For precise work, zoom in with the mouse wheel and use Shift + mouse wheel or the scroll bar under the waveform to move left and right. ‘Zoom to fit’ shows the whole sound again.

Click ‘OK’ to apply the new start and end time, or ‘Cancel’ to leave the sound as it was. You can undo a trim in one step with Undo. If you normalized the sound's volume, QuizXpress measures the new part again so it stays just as loud.

### Setting the replay part

In the same editor you can choose the part that plays again after the answer is revealed (see [Replay](#replay) below). Often that's a different part of the song than the one played during the question, for example the chorus.

![The trim editor showing the replay part](../../assets/images/sound-trim-editor-replay.webp){ loading=lazy }

1. Tick ‘Replay after the answer is revealed’. The editor switches to ‘Replay’ and the selection turns green.
2. Select the replay part in the same way as described above.
3. Optionally, enter a ‘Delay (s)’: the number of seconds to wait after the answer is revealed before the replay starts.

Use the ‘Playback’ and ‘Replay’ buttons at the top left to switch between the two parts. The part you are not editing is shown as a bar along the bottom of the waveform (blue for playback, green for replay), so you can see how the two relate.

!!! note
    Replay isn't available when the sound's ‘Keep playing’ option is on, because the sound then never stops.

## Replay

Often you’ll want to replay (part of) the music after the question has finished, synchronized with revealing the correct answer on the slide. This can be done by enabling the audio replay functionality:

![](../../assets/images/image208.webp){ width="576" loading=lazy }

You can set an initial delay, the song’s start time, and the end time. The easiest way to choose the replay part is on the waveform in the trim editor; see [Setting the replay part](#setting-the-replay-part).

## Spotify ™ playlist import

You can import your Spotify playlists (optionally with album art and a 30 second preview of the songs) and effortlessly create a Trivia Music quiz or a Disco Bingo game. QuizXpress does not interact with Spotify directly but supports a CSV file format produced by the [Exportify](https://watsonbox.github.io/exportify/) website. To use this function, export your playlist to CSV using the site and import the file in QuizXpress. A form will appear for you to make some choices:

![](../../assets/images/image209.webp){ width="224" loading=lazy }

If we create a Bingo game with these options, we get a mix of cells with album art and Artist/Title text, like:

![](../../assets/images/image210.webp){ loading=lazy }

The created slides and game settings can be tweaked after the import.

## Applying sound effects

There are various effects possible when playing sounds:

- **Increase sound speed** – this is accomplished by giving the sound’s ‘speed percentage’ and ‘target speed percentage’ properties the same value in the Property Editor. This value must be greater than 100 to speed up the sound. To show the properties of a sound, left-click the sound icon in the design area.

- **Slow down sound speed** – this is accomplished by giving both properties mentioned above a value smaller than 100. Again, give both properties the same value; you’ll see why below.

- **Slow speed to normal speed** – to accomplish this, enter a value smaller than 100 for the sound’s ‘speed percentage’ property. This ensures the sound starts playing slowed down. Leave the ‘target speed percentage’ property unchanged; its default value is 100, meaning normal speed. As a result, QuizXpress will play the sound slowly at first, but as time progresses, it will reach the target speed of 100 (normal speed).

- **Fast speed to normal speed** – to accomplish this, select a value greater than 100 for the ‘speed percentage’ property. Leave the ‘target speed percentage’ property unchanged.

- **Reverse** – plays the sound fragment in reverse, challenging the players to recognize the song (tick the Reverse audio checkbox in the sound ribbon)

You can listen to these sound effects while creating the question that contains the sound. To listen to the sound and its effects, click the ‘Play’ button in the ribbon, or select ‘Play’ from the sound’s context menu.

If you don’t want the sound to start immediately when the question starts, use the sound’s ‘Intro Pause’ property to delay playback (this gives participants the opportunity to read the question first, or gives the quizmaster the opportunity to read the question aloud first).

!!! note

    other sounds, such as the buzzer sounds, background music, and countdown music, can be configured in Quiz Setup.*
