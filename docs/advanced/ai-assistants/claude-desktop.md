# Using Claude Desktop

[Claude Desktop](https://claude.ai/download) is the Claude app for Windows and Mac. It can control Quiz Studio just like Claude Code, but it connects in a different way: through a small bridge program called `mcp-remote`. This page explains how to set it up, also when you run QuizXpress in Parallels on a Mac.

Before you start, turn on the AI assistant setting in Quiz Studio, as described in [Connecting an AI assistant](connecting-an-ai-assistant.md).

## What you need

- **Claude Desktop for Windows**, installed on the same computer as Quiz Studio. There is also a version for Windows on ARM.
- **Node.js** (the LTS version from [nodejs.org](https://nodejs.org)). The bridge program runs with it. To check that it is installed, open a command prompt and type `node --version`: it should show a version number.

!!! note
    Don't add Quiz Studio under 'Settings' → 'Connectors' in Claude. Those connectors connect from Anthropic's servers on the internet, and Quiz Studio only accepts connections from your own computer.

## Adding Quiz Studio to Claude Desktop

1. In Claude Desktop, go to 'Settings' → 'Developer' and click 'Edit Config'. This opens the configuration file `claude_desktop_config.json`.
2. Close Claude Desktop completely. Closing the window is not enough: open the Task Manager, select Claude and click 'End task'. If Claude is still running while you edit the file, it can overwrite your changes.
3. Open the file in Notepad and add this block right after the first `{`:

   ```json
     "mcpServers": {
       "quizstudio": {
         "command": "cmd",
         "args": ["/c", "npx", "-y", "mcp-remote", "http://127.0.0.1:8766/mcp"]
       }
     },
   ```

   Keep the rest of the file as it is, and save it.
4. Start Quiz Studio, then start Claude Desktop again.
5. In 'Settings' → 'Developer', check that `quizstudio` is shown as running. The first time it can take about a minute, while the bridge program is downloaded.

Now start a conversation as usual, for example: "Show me an overview of the slides of the quiz that is open in Quiz Studio."

!!! tip
    Use exactly the form above, with `cmd` and `/c`. Claude Desktop on Windows doesn't always find `npx` when it is started directly.

## QuizXpress in Parallels on a Mac

Quiz Studio only accepts connections from the computer it runs on. When QuizXpress runs in Windows in Parallels, the Mac counts as another computer, so Claude on the Mac can't reach Quiz Studio.

Install Claude Desktop **inside Windows**, in the same virtual machine as QuizXpress, and set it up as described above. Your Claude account and conversations are the same as on the Mac.

## Using the Code tab of Claude Desktop

Claude Desktop also has a 'Code' tab, which runs Claude Code. It doesn't use `claude_desktop_config.json`. Instead it reads the file `.mcp.json` in the folder you work in, and connects directly, without the bridge program:

```json
{
  "mcpServers": {
    "quizstudio": {
      "type": "http",
      "url": "http://127.0.0.1:8766/mcp"
    }
  }
}
```

Claude Code asks you to approve the server before it uses it. After you change the file, start a new session in the Code tab: a session that is already open doesn't see the server.

## Troubleshooting

**`quizstudio` doesn't appear in 'Settings' → 'Developer', or your changes to the file are gone.** Claude Desktop was still running while you edited the file. Close it in the Task Manager, make the change again and start Claude.

**`quizstudio` stays on starting, or shows an error.** Check that Node.js is installed (`node --version`), that Quiz Studio is running and that the AI assistant option is ticked in Quiz Studio's options. Then close Claude Desktop in the Task Manager and start it again.

**Claude on the Mac can't connect to Quiz Studio in Parallels.** That is expected: run Claude Desktop inside Windows, see [QuizXpress in Parallels on a Mac](#quizxpress-in-parallels-on-a-mac).
