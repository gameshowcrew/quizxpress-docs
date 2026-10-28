# Usar Claude Desktop

[Claude Desktop](https://claude.ai/download) es la aplicación de Claude para Windows y Mac. Puede controlar Quiz Studio igual que Claude Code, pero se conecta de otra manera: a través de un pequeño programa puente llamado `mcp-remote`. Esta página explica cómo configurarlo, también cuando usa QuizXpress en Parallels en un Mac.

Antes de empezar, active el ajuste de asistentes de IA en Quiz Studio, como se describe en [Conectar un asistente de IA](connecting-an-ai-assistant.md).

## Qué necesita

- **Claude Desktop para Windows**, instalado en el mismo ordenador que Quiz Studio. También hay una versión para Windows en ARM.
- **Node.js** (la versión LTS de [nodejs.org](https://nodejs.org)). El programa puente funciona con él. Para comprobar que está instalado, abra un símbolo del sistema y escriba `node --version`: debe aparecer un número de versión.

!!! note
    No añada Quiz Studio en 'Settings' → 'Connectors' de Claude. Esos conectores se conectan desde los servidores de Anthropic en Internet, y Quiz Studio solo acepta conexiones de su propio ordenador.

## Añadir Quiz Studio a Claude Desktop

1. En Claude Desktop, vaya a 'Settings' → 'Developer' y haga clic en 'Edit Config'. Se abre el archivo de configuración `claude_desktop_config.json`.
2. Cierre Claude Desktop por completo. No basta con cerrar la ventana: abra el Administrador de tareas, seleccione Claude y haga clic en 'Finalizar tarea'. Si Claude sigue en ejecución mientras edita el archivo, puede sobrescribir sus cambios.
3. Abra el archivo con el Bloc de notas y añada este bloque justo después de la primera `{`:

   ```json
     "mcpServers": {
       "quizstudio": {
         "command": "cmd",
         "args": ["/c", "npx", "-y", "mcp-remote", "http://127.0.0.1:8766/mcp"]
       }
     },
   ```

   Deje el resto del archivo como está y guárdelo.
4. Inicie Quiz Studio y, a continuación, vuelva a iniciar Claude Desktop.
5. En 'Settings' → 'Developer', compruebe que `quizstudio` aparece en ejecución. La primera vez puede tardar alrededor de un minuto, mientras se descarga el programa puente.

Ahora inicie una conversación como de costumbre, por ejemplo: «Muéstrame un resumen de las diapositivas del quiz abierto en Quiz Studio».

!!! tip
    Use exactamente la forma anterior, con `cmd` y `/c`. En Windows, Claude Desktop no siempre encuentra `npx` cuando lo inicia directamente.

## QuizXpress en Parallels en un Mac

Quiz Studio solo acepta conexiones del ordenador en el que se ejecuta. Cuando QuizXpress se ejecuta en Windows dentro de Parallels, el Mac cuenta como otro ordenador, por lo que Claude en el Mac no puede llegar a Quiz Studio.

Instale Claude Desktop **dentro de Windows**, en la misma máquina virtual que QuizXpress, y configúrelo como se describe arriba. Su cuenta de Claude y sus conversaciones son las mismas que en el Mac.

## Usar la pestaña Code de Claude Desktop

Claude Desktop también tiene una pestaña 'Code', que ejecuta Claude Code. No usa `claude_desktop_config.json`: lee el archivo `.mcp.json` de la carpeta en la que trabaja y se conecta directamente, sin el programa puente:

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

Claude Code le pide que apruebe el servidor antes de usarlo. Después de cambiar el archivo, abra una nueva sesión en la pestaña Code: una sesión que ya está abierta no ve el servidor.

## Solución de problemas

**`quizstudio` no aparece en 'Settings' → 'Developer', o sus cambios en el archivo han desaparecido.** Claude Desktop seguía en ejecución mientras editaba el archivo. Ciérrelo en el Administrador de tareas, repita el cambio e inicie Claude.

**`quizstudio` se queda iniciándose o muestra un error.** Compruebe que Node.js está instalado (`node --version`), que Quiz Studio está en ejecución y que la opción de asistentes de IA está marcada en las opciones de Quiz Studio. Después cierre Claude Desktop en el Administrador de tareas y vuelva a iniciarlo.

**Claude en el Mac no puede conectarse a Quiz Studio en Parallels.** Es lo esperado: use Claude Desktop dentro de Windows, consulte [QuizXpress en Parallels en un Mac](#quizxpress-en-parallels-en-un-mac).
