# Conectar un asistente de IA

## Activarlo

1. En Quiz Studio, vaya a HOME → Options y abra la pestaña 'AI Completion'.
2. En 'AI assistants (MCP)', marque 'Allow AI assistants to control Quiz Studio' y haga clic en OK.

La página muestra la dirección a la que debe conectarse un asistente: `http://127.0.0.1:8766/mcp`. El ajuste se recuerda, por lo que seguirá activado la próxima vez que inicie Studio. Desmárquelo para desactivarlo de nuevo.

## Conectar su asistente

Añada Quiz Studio como servidor MCP en su asistente de IA, usando la dirección anterior y el transporte HTTP. Cómo hacerlo depende del asistente. Para Claude Code, ejecute este comando una sola vez en un símbolo del sistema:

```
claude mcp add --transport http quizstudio http://127.0.0.1:8766/mcp
```

Otros asistentes que admiten servidores MCP a través de HTTP tienen un ajuste similar donde se introduce un nombre y la dirección.

Quiz Studio debe estar en ejecución mientras trabaja el asistente. Inicie la conversación como de costumbre, por ejemplo: «Abre mi quiz 'Friday night.qx' en Quiz Studio y muéstrame un resumen de las diapositivas».

## Qué verá en Studio

En cuanto el asistente se conecta, aparece una barra debajo de la cinta de opciones: 'An AI assistant is connected to Quiz Studio. Changes it makes cannot be undone with Undo.' Haga clic en 'Turn off' en la barra para desconectar el asistente y desactivar de nuevo el ajuste. Haga clic en la cruz para ocultar la barra.

## Usarlo solo durante una sesión

Si no desea activar el ajuste de forma permanente, inicie Quiz Studio con la opción `-mcp`. El asistente podrá conectarse durante esa sesión y el ajuste seguirá desactivado. Quiz Studio también omite la pantalla de bienvenida, de modo que puede iniciarlo desde un script o hacer que lo inicie un asistente. Puede añadir el quiz que desea abrir:

```
"Quiz Studio.exe" -mcp "C:\Quizzes\Friday night.qx"
```

Para usar otro puerto, por ejemplo cuando ejecuta dos copias de Studio, añada el puerto: `-mcp:8800`. La dirección pasa entonces a ser `http://127.0.0.1:8800/mcp`.

## Solución de problemas

**La barra dice 'AI assistants cannot connect: port 8766 is already in use'.** Otro programa, u otra copia de Quiz Studio, está usando el puerto. Cierre la otra copia o inicie Studio con `-mcp:` y otro número de puerto.

**El asistente dice que Quiz Studio no responde o muestra un cuadro de diálogo.** Quiz Studio no puede recibir comandos mientras hay un cuadro de diálogo abierto. Cierre el cuadro de diálogo (por ejemplo, Options o una pregunta 'Save changes?') y pida al asistente que lo intente de nuevo.

**El asistente no puede conectarse en absoluto.** Compruebe que la opción está marcada, que Quiz Studio está en ejecución y que la dirección en el asistente es exactamente la que se muestra en Options. No necesita cambiar nada en el firewall de Windows: la conexión permanece en su propio ordenador.
