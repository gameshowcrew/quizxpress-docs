# Packing and unpacking a quiz

When you create large quizzes with lots of multimedia content, such as video and audio fragments, the quiz file can easily become large and tedious to work with during the edit phase, and can exhaust the PC’s internal memory. To deal with this, QuizXpress lets you keep media files external (linked). That is fine while you build the quiz, but when the quiz needs to be moved to another PC or given to someone else, all linked files have to go with it, and forgetting one leads to problems during the show.

The ‘Pack’ function solves this: it saves a copy of the quiz with all sounds and videos inside, as one file you can take to another computer. It can also make that file a lot smaller, by trimming every sound and video to the part that is actually played and by compressing them. The quiz you are editing is never changed: packing always writes a new file.

## Packing a quiz

1. Save your quiz first. A quiz that has never been saved cannot be packed.
2. Press F1 to go to the backstage menu and click ‘Pack’.
3. Check the file name under ‘Save as’. By default the packed quiz is saved next to your quiz, with ‘(packed)’ added to the name. Click ‘Browse...’ to choose another place or name.
4. Choose the options (see below) and click ‘Pack’.

![The Pack quiz dialog](../../assets/images/studio-pack-dialog.webp){ loading=lazy }

The list shows every sound and video in the quiz: the slide it is on, whether it is embedded or linked, its size, the part that is played (‘Plays’) and, under ‘Result’, what packing is going to do with it, such as ‘Trim to 1:19–9:54’.

While packing, the progress is shown at the bottom and each row shows how far it is. You can keep an eye on the result per sound or video as it comes in. Click ‘Cancel’ to stop: nothing is saved then.

![Packing in progress](../../assets/images/studio-pack-progress.webp){ loading=lazy }

When it is done, a green bar shows how long it took and how large the quiz was before and after packing. Click ‘Show in folder’ to open the folder with the packed quiz.

![The result of packing](../../assets/images/studio-pack-done.webp){ loading=lazy }

## Trimming sounds and videos

Often only a small part of a song or video clip is played during the quiz, for example 20 seconds of a 4-minute song. With ‘Trim to the part that is played’ (separately for ‘Sounds’ and ‘Videos’), the packed quiz only keeps that part. This can save a lot of space, especially in music rounds and music bingos.

- The part that is kept runs from the ‘Start’ to the ‘End’ of the sound or video, and includes the ‘Replay’ part when the sound or video replays after the answer.
- ‘Margin’ adds a few seconds before and after that part (1 second by default), so you still have a little room if you want to adjust the times later on.
- The start, end and replay times in the packed quiz are adjusted automatically, so the quiz plays exactly the same as before.
- A sound or video that plays to the end keeps its end. A looping video that plays to the end keeps its beginning too, because it starts again from the beginning of the file.
- Background videos are trimmed in the same way as other videos.
- When (almost) the whole file is played, there is nothing to trim and the file stays as it is.

!!! note
    In the packed quiz, you can’t move the start of a trimmed sound or video further back than the part that was kept. If you still want to change the times a lot, do that in your original quiz and pack it again.

## Compressing sounds and videos

With ‘Format’ you choose how sounds and videos are stored in the packed quiz:

| Sounds | What it does |
|---|---|
| ‘Keep the format’ | The sounds stay as they are. Trimming cuts them without converting them, so there is no loss of quality. |
| ‘MP3, high quality (about 190 kbps)’ | Converts the sounds to MP3. WAV files become a lot smaller this way. |
| ‘MP3, compact (about 130 kbps)’ | Converts the sounds to a smaller MP3, still fine for playing in a room. |

| Videos | What it does |
|---|---|
| ‘Keep the video (cut at keyframes)’ | The videos stay as they are, without loss of quality. A trimmed video then starts at the nearest keyframe before the cut, a few seconds earlier at most; the times are adjusted for that. |
| ‘H.264, high quality’ | Converts the videos to MP4 (H.264), which plays everywhere and is usually much smaller. |
| ‘H.264, compact’ | Converts the videos to a smaller MP4, with some loss of detail. |

Next to the video format you can limit the picture size to ‘Up to 1080p’ or ‘Up to 720p’. Videos with a larger picture are made smaller, which saves a lot of space for 4K videos.

QuizXpress only converts a file when that is worthwhile: an MP3 or a video that is already compact is left as it is (‘Already compact’), and a result that would not be smaller than the original is not used (‘Would not get smaller’). That also keeps packing fast.

Your choices are remembered for the next time you pack a quiz.

## Installing ffmpeg

Trimming and compressing are done with ffmpeg, a free tool that is not part of QuizXpress. Under the options, the dialog shows which version of ffmpeg it uses. When ffmpeg is not installed, a bar at the top of the dialog offers three ways to get it:

![The Pack dialog without ffmpeg](../../assets/images/studio-pack-no-ffmpeg.webp){ loading=lazy }

- ‘Install with winget’ installs ffmpeg with the Windows package manager. A console window opens; follow it, and accept the terms of winget when it asks for that. When the window closes, QuizXpress finds ffmpeg by itself and trimming and compressing become available.
- ‘Download’ opens the download page of ffmpeg in your browser. Unpack the download to a folder of your choice.
- ‘Locate ffmpeg.exe...’ lets you point to an ffmpeg.exe you already have, for example in the ‘bin’ folder of the download. The ffprobe.exe that comes with it must be in the same folder.

Without ffmpeg you can still pack a quiz: the linked media are then embedded as they are.

## Missing files

When a linked sound or video file can’t be found, its row is shown in red (‘File not found, stays linked’) and a warning at the bottom tells you how many files are missing. You can still pack the quiz, but those files stay linked and will be missing on another computer. To include them, locate the missing files in your quiz first and pack again.

## Unpacking a quiz

You can also unpack a previously packed quiz file. This extracts all media (audio/video) to a local folder and links the media elements in the quiz to the local files. This speeds up quiz loading times and reduces memory usage in the quiz player. Its primary use is preventing issues when dealing with huge quiz files (~1.5GB or higher). To unpack a quiz, press F1 to go to the backstage menu and click ‘Unpack’.
