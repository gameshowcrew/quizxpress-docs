# Opciones de línea de comandos

Las siguientes opciones de línea de comandos están disponibles al iniciar QuizXpress Live:

| Línea de comandos                | Explicación |
|----------------------------------|-------------|
| \-*nosnapshot*                   | Por motivos de recuperación, QuizXpress Live registra todo tipo de datos generados durante un quiz (elecciones de los equipos, puntuaciones, pregunta actual, etc.). Este conjunto de datos se denomina ‘instantánea’ (snapshot). Si un quiz se interrumpe por algún motivo imprevisto, QuizXpress Live lee todos los datos de la instantánea de ese quiz al reiniciarse, de modo que el quiz puede continuar desde el punto en que se interrumpió. La opción –nosnapshot de la línea de comandos no escribe un archivo de instantánea. |
| \-*quickstart*                   | Omite las pantallas de bienvenida y de cuenta atrás |
| *-windowed*                      | Inicia la aplicación en una ventana normal para que pueda seguir utilizando otras aplicaciones |
| *-noborder*                      | Se utiliza junto con –windowed; se ejecuta en modo ventana pero sin barra de título ni borde, por lo que parece el modo exclusivo de pantalla completa aunque en realidad se ejecuta en una ventana normal. También puede activar este modo pulsando la tecla M durante el show. |
| \-*showfps*                      | Muestra el número de fotogramas por segundo (para medir el rendimiento) |
| \-*singleuser*                   | Inicia QuizXpress Live en modo de un solo usuario; esta opción se utiliza al iniciar el show desde QuizXpress Solo |
| \-*scorefile=\<file>*            | Nombre de archivo del archivo de puntuaciones, que almacena todos los datos relevantes del quiz (elecciones por equipo, puntuaciones por equipo, información de tiempos, etc.) |
| *-startwith=\<0..n>*             | Inicia el quiz con la pregunta indicada, p. ej., –startwith=5 para comenzar con la 5.ª pregunta |
| *-autorun*                       | Simula un público |
| *-autoexit*                      | Cierra automáticamente la aplicación después de la pantalla de puntuaciones (se utiliza junto con *–autorun*) |
| *-screen=\<devicename>*          | Inicia la aplicación en el dispositivo de salida indicado |
| *-settingsfile=\<settingsfile>*  | Carga la configuración del archivo de configuración indicado. Esto permite cambiar fácilmente entre diferentes configuraciones (como configuraciones de equipos) |
| *-preload*                       | Opción (avanzada) para precargar y renderizar previamente todas las diapositivas al iniciar. Solo es necesaria si experimenta retrasos durante su quiz y su PC dispone de suficiente memoria |

Por ejemplo, para iniciar QuizXpress Live en modo ventana a pantalla completa, puede utilizar el siguiente comando (iniciado desde un archivo por lotes o una ventana de comandos):

“Quiz Show.exe” –windowed –noborder c:\myquizzes\quiz1.qx
