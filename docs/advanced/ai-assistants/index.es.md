# Asistentes de IA

Quiz Studio puede ser controlado por un asistente de IA como [Claude](https://claude.ai). Usted le dice al asistente qué quiz desea («crea una ronda de quiz de bar sobre los años 90 con 10 preguntas de opción múltiple y una ronda de imágenes»), y él abre, construye, edita y guarda el quiz en su ventana de Quiz Studio mientras usted observa. Todo lo que hace ocurre en el Quiz Studio que tiene abierto, de modo que puede revisar el resultado, modificarlo usted mismo y continuar.

Esto es distinto del [AI Quiz Generator](../../studio/quizxpress-and-ai.md), una parte de Studio que genera preguntas por usted. Con un asistente de IA trabaja en una conversación, y el asistente puede hacer casi todo lo que usted puede hacer en Studio: crear todos los tipos de diapositivas, cambiar textos, respuestas, puntos, estilos y fondos, añadir minijuegos, comprobar si el quiz tiene errores y guardarlo.

## Cómo funciona

La conexión utiliza un estándar llamado MCP (Model Context Protocol), que permite a los asistentes de IA usar otros programas. Quiz Studio incorpora un pequeño servidor MCP:

- Está **desactivado** hasta que lo active en Options, consulte [Conectar un asistente de IA](connecting-an-ai-assistant.md).
- Solo acepta conexiones de **programas de su propio ordenador**. Nadie en la red o en Internet puede usarlo.
- Necesita un asistente de IA compatible con MCP, por ejemplo Claude Code. El asistente es un producto aparte con su propia suscripción: no forma parte de QuizXpress y no utiliza sus créditos de IA de QuizXpress.

Mientras hay un asistente conectado, una barra debajo de la cinta de opciones se lo indica.

## Conviene saber

!!! warning "Los cambios no se pueden deshacer"
    Los cambios del asistente no se pueden deshacer con Undo, y Quiz Studio borra el historial de deshacer después de cada uno de ellos. Guarde su quiz con otro nombre antes de dejar que un asistente haga cambios importantes, para poder volver siempre atrás.

- El asistente no abrirá, creará ni cerrará un quiz mientras el quiz en Studio tenga cambios sin guardar. Primero tiene que preguntarle: guardar el quiz o indicarle que descarte los cambios.
- Mientras hay un cuadro de diálogo abierto en Studio (por ejemplo, Options), el asistente tiene que esperar. Cierre el cuadro de diálogo y podrá continuar.
- Cada vez que el asistente añade una diapositiva, Studio la muestra y desplaza las miniaturas hasta ella.
- Esto solo se aplica a Quiz Studio. Quiz Live, Director y Setup no pueden ser controlados por un asistente.

## En esta sección

- [Conectar un asistente de IA](connecting-an-ai-assistant.md): actívelo y conecte su asistente.
- [Qué puede hacer un asistente](what-an-assistant-can-do.md): las posibilidades, con ejemplos de qué pedir.
