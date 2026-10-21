# Design area

The design area contains a visual representation of what we call a ‘quiz slide’. It shows the ‘quiz slide’ exactly as it will be shown during the game show. A ‘quiz slide’ consists of several items: a question, multiple choice answers, pictures, shapes and text, a video or a sound item etc. Items can be selected individually or as a group after which they can be modified. Also, the quiz slide as a whole can be selected to edit its properties. To select a quiz slide, click on the slide background. See [Quiz slide properties](advanced-properties-grid.md#quiz-slide-properties) for an overview of all properties of a slide.

Slide items can be selected and resized by left-clicking one of the resize handles and dragging it to the desired size. When multiple items are selected, either using the Ctrl key or by dragging a selection box with the mouse, editing properties shown in the property pane (or using ribbon controls) changes the properties for all selected items at once. This is handy, for example, when you want to set the font for all answers in a question at once: first select all the answers, then change the ‘font’ property in the properties pane. While moving objects around, they snap to [smart guides](#smart-guides) and to an invisible grid; hold down the *Ctrl* key while dragging to turn off this snapping.

## Smart guides

While you move or resize items on a slide, Quiz Studio shows smart guides: red lines that show when items line up, and the item snaps into place as soon as it gets close. This makes it easy to build neat, consistent slides without measuring anything.

![Smart guides while moving an answer](../../assets/images/smart-guides-spacing.webp){ loading=lazy }

- **Edges line up**: a red dashed line appears when an edge of the item lines up with an edge of another item, or with the edge of the slide. Small red crosses mark the items that line up.
- **Centres line up**: a red dash-dot line appears when the centre of the item lines up with the centre of another item, or with the centre of the slide.
- **Equal spacing**: when the item is just as far from the item above (or before) it as from the one below (or after) it, or just as far as other items in the same row or column are apart, arrows with the distance in pixels appear in every equal gap. In the picture above, all four answers are 20 pixels apart.
- **Equal size**: while you resize an item, it snaps to the width or height of another item on the slide, and a size marker shows on every item with that size.

![Smart guides while resizing an answer](../../assets/images/smart-guides-size.webp){ loading=lazy }

While you drag, a see-through copy of the item shows where it will go, and a small label shows its position (X and Y) or, while resizing, its size, in slide pixels. Smart guides also work when you move several selected items together.

- Hold down the *Ctrl* key while dragging to place an item freely, without smart guides or grid.
- Press *Esc* while dragging to cancel the move and leave the item where it was.

To turn smart guides off (or on again), right-click the slide background and click ‘Smart guides’. Quiz Studio remembers this setting. Items then snap to the invisible grid only.

![Smart guides in the slide context menu](../../assets/images/smart-guides-menu.webp){ width="200" loading=lazy }

!!! tip
    To line up several items in one go, select them and use the [alignment tools](../other-functionality/home-alignment-size-order.md) on the HOME ribbon.

## Inserting a slide

To insert a new slide, go to the INSERT menu and choose one of the predefined layouts in the ‘Quiz Slides’ section. Dark blue boxes represent placeholders for inserting a picture or video.

![](../../assets/images/image13.webp){ loading=lazy }

By choosing the layouts on the bottom row, you can insert a minigame, a Trivia Board, a Trivia Ladder, a Trivia Feud game, or a Bingo round, respectively.

You can also change the layout of an existing slide from the DESIGN menu by clicking the dropdown arrow in the ‘Change Layout’ section. The same dropdown list shown above appears, letting you choose a new layout. Items from the current layout that fit into the new layout will be copied over. For example, when you go from a layout with a question, a picture, and three answers to a layout with a question, a picture, and four answers, the picture, question, and three answers will all be copied to the new layout.
