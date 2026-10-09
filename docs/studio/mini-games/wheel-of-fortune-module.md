# Wheel of Fortune module

The wheel of fortune allows you to spin a wheel to draw a prize or points for a team, or just draw a specific team.

![The Wheel of Fortune with prizes and points](../../assets/images/wheel-of-fortune-game.webp){ loading=lazy }

Please find below the configuration screens with their default settings:

| ![](../../assets/images/image140.webp){ width="254" loading=lazy } | ![](../../assets/images/image141.webp){ width="254" loading=lazy } |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

- Participants: selected players play the wheel (selection is done before the wheel starts, on the director screen), the top ranked players play the wheel or a single player of a certain rank can stop the wheel with his or her keypad.

- Draw a prize: prizes (which can also be positive or negative points) are shown in the wheel. By pressing the ‘Setup prizes’ button the prizes can be configured, see [Setting up the prizes](#setting-up-the-prizes).

- Draw a team/player: the selected participants are distributed across the wheel. The number of segments on the wheel can be chosen by selecting a value for ‘Number of segments’. If the checkmark is checked before ‘Show prize’, prizes which can be won (or lost) are shown next to the wheel. While the wheel spins, the prizes highlight one after another. When the wheel stops on a player/team, the highlighted prize is won (or lost, in the case of negative points). Prizes (or points) can be defined by pressing the ‘Setup prizes’ button. This mode does not work in combination with the ‘stop the wheel’ option in the ‘participants’ section, as prizes are required on the wheel for the ‘stop the wheel’ game.

- Draw bonus points: the positive, negative and Kapow! points are distributed across the wheel in the number of segments indicated. For positive and negative points, each segment increases or decreases in value, respectively (for example: positive points of 1 with 5 segments results in the values 1, 2, 3, 4, and 5; negative points of -2 with 4 segments results in the values -2, -4, -6, -8). Kapow! points are negative points that are fixed across the number of segments specified. The Kapow! segments are the ones players do not want to land on! The total number of segments for the ‘Draw bonus points’ section cannot exceed 40.

- Appearance tab: set the title text of the game and the fonts used. Choose a background image as well as the image shown at the center of the wheel. Without a center image, the wheel shows a gold star in the center.

- Other tab: Set the wheel spinning speed as well as the spin time.

## Setting up the prizes

![The ‘Setup prizes’ window](../../assets/images/wheel-of-fortune-setup-prizes.webp){ loading=lazy }

Every row is a prize:

- Prize type: ‘Prize’ for something to win, or ‘Points’ to win points (or lose them, with a negative number).
- Points: the number of points for a ‘Points’ prize. The wheel shows this number.
- Prize name: the text on the wheel and in the message for the winner.
- Repeat: the number of segments the prize gets on the wheel. A prize that appears more than once is spread across the wheel.
- Image: an optional picture, shown on the wheel instead of the name.

The window starts with eight rows. Press ‘Add prize’ for more rows, up to 40 prizes. Empty rows after the first eight are removed when you press ‘OK’. The wheel has room for 40 segments in total, or 24 when prizes have an image.

The same window sets up the prizes shown next to the wheel when you draw a team/player. The ‘Repeat’ column is not used there.

!!! note
    Older versions of QuizXpress support only eight prizes. Play a quiz with more prizes on a computer with the latest version.

## Playing the game

In order to spin the wheel, press the ‘Spin’ button in the left-hand side panel.

![](../../assets/images/image143.webp){ width="142" loading=lazy }

While the wheel spins, the lights around the rim chase along. When the wheel stops, the segment under the pointer flashes and keeps a gold outline, and the result is shown at the bottom of the screen.

![The result after a spin](../../assets/images/wheel-of-fortune-result.webp){ loading=lazy }

When the ‘Stop the wheel’ setting is on, the player that can stop the wheel with his or her keypad is indicated in the ‘Teams’ panel in the game. The buzzer below the name shakes when the player presses his or her keypad. The wheel can also be stopped by pressing the ‘Stop the Wheel!’ button (but typically this is not necessary as the player should stop the wheel).

![The player who can stop the wheel](../../assets/images/wheel-of-fortune-stop-the-wheel.webp){ loading=lazy }

![](../../assets/images/image144.webp){ width="143" loading=lazy }
