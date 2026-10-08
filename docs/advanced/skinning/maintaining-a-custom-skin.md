# Sharing, updating and troubleshooting a custom skin

## Sharing a skin with another computer

A complete custom skin consists of two things, both in the data folder `%appdata%\QuizXpress`:

- `skin.config`
- the folder `Skins\<your skin>` with its images

Copy both to the data folder on the other computer and select the skin in Quiz Setup there. If you used the relative `dir="Skins\<your skin>"` as described in [Creating a custom skin](creating-a-custom-skin.md#step-4-add-your-skin-definition), nothing needs to be changed. Fonts used by the skin must also be installed on the other computer.

## After a QuizXpress update

An update replaces the installed `skin.config`, but never touches your copy or your skin folder, so your skin keeps working. However, because a 'User.' skin reads only your copy, the built-in skins it inherits from stay as they were when you made the copy. New settings and improvements that an update adds to the built-in skins are not picked up by your skin.

To bring your skin up to date after an update:

1. Copy your `<skin>…</skin>` element from your `skin.config` to a safe place, for example a text file next to it.
2. Copy the new `skin.config` from the installation folder to the data folder, replacing your copy.
3. Paste your `<skin>` element back just above `</skins>` (and add `hidden="true"` to the built-in skins again if you used that).

Your skin folder with images doesn't need to change.

## Troubleshooting

| Symptom | Cause and solution |
|---|---|
| My skin doesn't appear in Quiz Setup. | Check that you edited the copy in `%appdata%\QuizXpress` (not the installed file), that it is saved, that your skin doesn't have `hidden="true"`, and that you restarted Quiz Setup. |
| QuizXpress Live shows an error about the skin file and doesn't start. | The message tells you what is wrong. Common causes: an XML error (a missing quote or `/>`, an `&` that should be written as `&amp;`), a 'parent' that doesn't match the 'name' of an existing skin, or an invalid value (for attributes with a fixed set of values, the message lists the allowed values). Correct the file and start again. |
| My skin is selected, but the quiz looks like a built-in skin. | Custom skins are not available in the Home edition. Otherwise, check that you didn't change the 'name' of your skin after selecting it in Quiz Setup; if you did, select it again. |
| A setting has no effect. | Check the spelling of the element and attribute names against the root skin (they are case-sensitive), and check that the element is inside your `<skin>` element. Restart the quiz after saving. |
| My image is not shown. | The file wasn't found or couldn't be read. Check the file name (including the extension) and the 'dir' of your skin. The error is written to the QuizXpress log file as "Skin image … not found, please check skin.config". |
