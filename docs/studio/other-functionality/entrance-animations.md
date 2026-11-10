# Entrance animations

Since version 8.6, the question and the answers can make an entrance in Quiz Show: instead of simply appearing, they fade in, slide in from the side, pop up, drop and bounce, and so on. You choose an effect for the question and one for the answers, and whether the answers come in one after the other or all together.

## Setting up an entrance

Select the slide in Quiz Studio and open the 'Animation' section of the slide properties (in the [advanced properties grid](../user-interface-overview/advanced-properties-grid.md) you find the same settings under 'Appearance'):

| Setting | What it does |
|---|---|
| 'Question entrance' | How the question enters. Pictures that are not answers enter together with the question. |
| 'Answers entrance' | How the answers enter. On a picture question with several pictures, the answer pictures enter as answers. |
| 'Answer order' | 'One by one': the answers enter one after the other. 'All together': they enter at the same time. Shown when an answers entrance is set. |
| 'Animation speed' | 'Normal', 'Slow' or 'Fast'. Applies to the question and the answers. |
| 'Countdown during animation' | When on, the countdown starts while the question and answers are still entering. When off (the default), the countdown starts as soon as everything is on the screen. |

'Answer order', 'Animation speed' and 'Countdown during animation' only appear once an entrance is set for the question or the answers.

When both the question and the answers have an entrance, the answers start when the question is halfway in, so the two flow into each other.

## Effects

| Effect | What you see |
|---|---|
| 'None' | No animation: the item simply appears (the default). |
| 'Fade in' | The item fades in. |
| 'Slide in from the left' / 'right' / 'top' / 'bottom' | The item slides in from outside the screen. |
| 'Alternate left and right' | The answers come in from the left and the right in turns, starting on the left. Used for the question, it slides in from the left. |
| 'Zoom in' | The item grows from half its size while it fades in. |
| 'Pop' | The item pops up, overshoots slightly and settles. |
| 'Flip' | The item flips open like a card turning. |
| 'Spin' | The item spins into place while it grows. |
| 'Drop and bounce' | The item drops in from the top and bounces before it settles. |

With 'Normal' speed an item takes about 0.6 seconds to enter, with 'Slow' about 0.9 seconds and with 'Fast' about 0.35 seconds. 'Spin' and 'Drop and bounce' take a little longer, so they stay readable.

## Answers shown later

If the answers are not shown straight away, because 'Show answers action' is set to 'Hide and show one by one' or 'Hide and show at once', the 'Answers entrance' is used each time answers appear.

## Which slides support it

Entrance animations work on question slides and the other slide types that show a question and answers. They are not available for Trivia Feud, Bingo rounds, minigames, Trivia Board rounds and Trivia Ladder rounds; for those slides the 'Animation' settings are not shown.

!!! tip
    Entrance animations combine well with [text reveal animations](text-reveal-animations.md): let the question slide in and then reveal its text word by word, or let the answers drop in one by one after the question has been read out.
