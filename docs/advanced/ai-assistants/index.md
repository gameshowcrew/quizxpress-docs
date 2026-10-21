# AI assistants

Quiz Studio can be controlled by an AI assistant such as [Claude](https://claude.ai). You tell the assistant what quiz you want ("make a pub quiz round about the 90s with 10 multiple choice questions and a picture round"), and it opens, builds, edits and saves the quiz in your Quiz Studio window while you watch. Everything it does happens in the Quiz Studio you have open, so you can look at the result, change it yourself and carry on.

This is different from the [AI Quiz Generator](../../studio/quizxpress-and-ai.md), which is a part of Studio that generates questions for you. With an AI assistant you work in a conversation, and the assistant can do almost everything you can do in Studio: create every type of slide, change texts, answers, points, styles and backgrounds, add mini games, check the quiz for mistakes and save it.

## How it works

The connection uses a standard called MCP (Model Context Protocol), which lets AI assistants use other programs. Quiz Studio has a small MCP server built in:

- It is **switched off** until you turn it on in the Options, see [Connecting an AI assistant](connecting-an-ai-assistant.md).
- It only accepts connections from **programs on your own computer**. Nobody on the network or the internet can use it.
- You need an AI assistant that supports MCP, for example Claude Code. The assistant is a separate product with its own subscription: it isn't part of QuizXpress and doesn't use your QuizXpress AI credits.

While an assistant is connected, a bar below the ribbon tells you so.

## Good to know

!!! warning "Changes can't be undone"
    The assistant's changes can't be undone with Undo, and Quiz Studio clears the undo history after each of them. Save your quiz under another name before you let an assistant make large changes, so you can always go back.

- The assistant won't open, create or close a quiz while the quiz in Studio has unsaved changes. It has to ask you first: save the quiz, or tell it to throw the changes away.
- While a dialog is open in Studio (for example the Options), the assistant has to wait. Close the dialog and it can continue.
- Each time the assistant adds a slide, Studio shows it and scrolls the thumbnails to it.
- This only applies to Quiz Studio. Quiz Live, Director and Setup can't be controlled by an assistant.

## In this section

- [Connecting an AI assistant](connecting-an-ai-assistant.md): turn it on and connect your assistant.
- [What an assistant can do](what-an-assistant-can-do.md): the possibilities, with examples of what to ask.
