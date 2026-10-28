# Connecting an AI assistant

## Turn it on

1. In Quiz Studio, go to HOME → Options and open the 'AI Completion' tab.
2. Under 'AI assistants (MCP)', tick 'Allow AI assistants to control Quiz Studio' and click OK.

The page shows the address an assistant has to connect to: `http://127.0.0.1:8766/mcp`. The setting is remembered, so it stays on the next time you start Studio. Untick it to turn it off again.

## Connect your assistant

Add Quiz Studio as an MCP server in your AI assistant, using the address above and the HTTP transport. How you do that depends on the assistant. For Claude Code, run this command once in a command prompt:

```
claude mcp add --transport http quizstudio http://127.0.0.1:8766/mcp
```

Other assistants that support MCP servers over HTTP have a similar setting where you enter a name and the address. For Claude Desktop, see [Using Claude Desktop](claude-desktop.md).

Quiz Studio has to be running while the assistant works. Start the conversation as usual, for example: "Open my quiz 'Friday night.qx' in Quiz Studio and show me an overview of the slides."

## What you see in Studio

As soon as the assistant connects, a bar appears below the ribbon: 'An AI assistant is connected to Quiz Studio. Changes it makes cannot be undone with Undo.' Click 'Turn off' on the bar to disconnect the assistant and switch the setting off again. Click the cross to hide the bar.

## Using it for one session only

If you don't want to switch the setting on permanently, start Quiz Studio with the `-mcp` option. The assistant can connect during that session, and the setting stays off. Quiz Studio also skips the welcome screen, so you can start it from a script or have an assistant start it. You can add the quiz to open:

```
"Quiz Studio.exe" -mcp "C:\Quizzes\Friday night.qx"
```

To use another port, for example when you run two copies of Studio, add the port: `-mcp:8800`. The address then becomes `http://127.0.0.1:8800/mcp`.

## Troubleshooting

**The bar says 'AI assistants cannot connect: port 8766 is already in use'.** Another program, or another copy of Quiz Studio, is using the port. Close the other copy, or start Studio with `-mcp:` and another port number.

**The assistant says Quiz Studio isn't responding or shows a dialog.** Quiz Studio can't take commands while a dialog is open. Close the dialog (for example the Options or a 'Save changes?' question) and ask the assistant to try again.

**The assistant can't connect at all.** Check that the option is ticked, that Quiz Studio is running, and that the address in the assistant is exactly the one shown in the Options. You don't need to change anything in the Windows firewall: the connection stays on your own computer.
