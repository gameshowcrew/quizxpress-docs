# Trivia Board round

A Trivia Board round enables you to create a Jeopardy®-style question board with topics and questions of varying difficulty/points.

![](../../assets/images/image68.webp){ width="513" loading=lazy }

Just like regular quiz slides, a trivia board can be fully styled (please refer to section [Trivia Board properties](../user-interface-overview/advanced-properties-grid.md#trivia-board-properties) for more details on the options).

During the quiz show, the questions on the board can be chosen (by keyboard, using the mouse or quizmaster remote) or randomly picked in which case a random selector jumps over the screen and chooses one of the tiles.

## How to create a Trivia Board?

To create a trivia board, start by inserting a trivia board slide into the quiz (go to the INSERT menu, click on the dropdown list in the Quiz Slides section and choose the Trivia Board layout). The trivia board will be generated automatically by the questions that follow it.

To categorize the questions into topics and points (or topics only), make sure to set the following properties of the questions following the trivia board:

- The topic

- The points

You can enter both on the QUESTION tab while the question is selected:

![](../../assets/images/image69.webp){ width="604" loading=lazy }

Alternatively, you can also enter the properties on the properties pane (if this is not visible, please show it first by selecting the VIEW tab and setting a checkmark before ‘Properties’).

A Trivia Board can be mixed with other QuizXpress game formats. To create a Trivia Board (round), QuizXpress needs to know where a Trivia Board round ends. A Trivia Board round ends at one of the following slide types:

- an ‘End of round’ slide (please also check 3.4.3)

- another Trivia Board slide

- a Trivia Ladder slide

- the end of the quiz (last round or a Trivia Board only game)

During the quiz show, all slides from a Trivia Board round are processed and grouped per topic. Within a topic, questions are grouped by the number of points. In this way, behind every points tile on the board there can be multiple questions. Once the questions behind a certain tile on the board are exhausted, the tile is greyed out and can no longer be chosen.

Questions that have no points (for example, Audience response, Demographic, Wager) are ignored when creating the Trivia Board.

Alternatively, the Quiz Wizard can help you create a complete Trivia Board round with a few clicks! Start the wizard (HOME tab followed by ‘Quiz Wizard’) and select ‘create a new round’ followed by ‘a Trivia Board round’. Now, fill in the topics, points, and other preferences.

![](../../assets/images/image70.webp){ width="499" loading=lazy }

Choose the question time, points, and style used on the next pages, and press ‘Finish’ to create the board, questions, and closing end-of-round slide for you. Of course, you will still need to fill in the actual questions, but the correct topic and points will already be set for you.

## Preview a Trivia Board

The Trivia Board slide in QuizXpress Studio shows the board as it will look during the show: the real topics and point values of the round, laid out with your design settings (position, spacing, images and text). By setting the styling options of the Trivia Board as well as the background you can determine the looks of the board.

![A designed Trivia Board slide in Studio](../../assets/images/trivia-board-studio-slide.webp){ loading=lazy }

When you want to try the board like it will be played during the game show, press F5 and the board will be automatically generated from the questions present in the Trivia Board round.

## Designing your own board

Besides the classic blue board, you can give a Trivia Board a complete design of its own: a themed background, illustrated topic headers and tiles of your own. A few examples:

![A music board with neon tiles and illustrated topic headers](../../assets/images/trivia-board-custom-music.webp){ loading=lazy }

![A sports board with a title in the background and photo headers](../../assets/images/trivia-board-custom-sports.webp){ loading=lazy }

![A travel board on an illustrated map with coloured topic labels](../../assets/images/trivia-board-custom-world.webp){ loading=lazy }

A design like these is made of a few images:

- **A background** for the slide (1920 × 1080 for a 16:9 quiz), with everything that does not change during the game: the scenery, a title, a frame around the board.
- **One image per topic** for the topic tiles, for example an illustration with the topic name in it, like in the examples above.
- **One tile image** for the point tiles, for example a button or a brush stroke. Save it as PNG with transparent corners, so the background shows around the tile.

All design settings are on the 'Design' page of the properties pane when the board is selected. All images are stored inside the quiz file, so you don't need to copy them along with the quiz.

![The design properties of the music board](../../assets/images/trivia-board-properties-custom.webp){ width="380" loading=lazy }

The music board above, for example, has a custom position, a topic row height of 390% for the tall headers, a topic image over the whole tile for every topic with the topic name switched off (the images already contain it), a transparent topic tile background, and a tile image for the point tiles.

### Position of the board

'Board position' decides where the board appears:

- **Automatic** fills the screen, like the classic board. The tiles then use a fill colour instead of images.
- **Custom** places the board where it is on the slide. Drag and resize the board in Studio to fit it into the frame of your background. The image settings below are only available with a custom position.

Under 'Layout' you can also set:

- **Topic row height**: the height of the topic tiles compared to the point tiles (for example 250% for large illustrated headers).
- **Column spacing** and **Row spacing**: the space between the tiles.

### Tile images

- **Tile image** (in 'Topic tiles' and in 'Question tiles') replaces the fill colour of the tiles by an image.
- **Image scaling** decides how the image is fitted into a tile: 'Stretch' (fill the tile exactly), 'Fit' (keep the shape of the image), 'Fill' (keep the shape and cut off what doesn't fit) or 'Keep corners' (stretch the middle of the image and keep its corners as they are, useful for framed tiles).
- **Vary tiles** mirrors the point tile image differently on every tile, so a tile with for instance paint splatters doesn't look exactly the same everywhere.

### Topic images

Click the button next to 'Topic images' to give every topic of the round its own image. The dialog lists the topics of the questions after the board:

![The Topic images dialog](../../assets/images/trivia-board-topic-images-dialog.webp){ width="600" loading=lazy }


- Click 'Choose…' to pick an image for a topic, or drag an image file onto its row.
- 'Assign from files…' assigns several images in one go: every image goes to the topic with the same name as the file. Upper and lower case, accents, spaces, dashes and underscores don't matter, so `dutch-pop.png` goes to the topic 'Dutch Pop'.
- Images of topics that are no longer in the round are listed at the bottom, so you can remove them.

'Image position' puts the topic image over the whole tile, or left, right or above the topic name. When your images already contain the topic name (like the examples above), switch off 'Show topic name'.

!!! tip
    Topic images belong to a topic by its name. When you rename a topic on the questions, choose its image again.

### Tile text

![The Tile text and Tile states sections of the properties pane](../../assets/images/trivia-board-properties-tile-text.webp){ width="380" loading=lazy }

- **Same text size for all tiles**: when on, all topic names get the same text size and all point values get the same text size: the largest size at which every text fits its tile, but never larger than the font size you set. Long topic names are spread over two lines. When off, every text is made as large as its own tile allows, so short texts end up larger than long ones.
- **Text effect** adds a shadow or an outline around the text of the tiles, in the 'Effect color'.

### Selection and played tiles

- **Selection highlight** decides how the random selection shows the chosen tile: 'Fill' covers the tile with the highlight colour (the classic look), 'Tint' colours it partly, 'Outline' and 'Glow' draw a coloured border and keep your tile image visible.
- **Highlight color** sets the colour of the random selection.
- **Played tiles** decides how a tile looks once its questions have been played: 'Dimmed', 'Hidden', or 'No text' (the tile stays, without its point value).

### Background video

A Trivia Board slide can also have a [background video](../backgrounds.md#background-video). It plays behind the board with the video's own settings (loop, silent, volume) and pauses while a question is shown.

!!! note
    Older versions of QuizXpress can still open a quiz with a designed board, but show it as a classic board.
