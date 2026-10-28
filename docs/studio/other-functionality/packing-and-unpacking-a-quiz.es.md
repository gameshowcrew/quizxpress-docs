# Empaquetar y desempaquetar un quiz

Cuando crea quizzes grandes con mucho contenido multimedia, como fragmentos de vídeo y audio, el archivo del quiz puede hacerse fácilmente muy grande y engorroso de manejar durante la fase de edición, y puede agotar la memoria interna del PC. Para solucionarlo, QuizXpress le permite mantener los archivos multimedia externos (vinculados). Esto no supone ningún problema mientras construye el quiz, pero cuando el quiz debe trasladarse a otro PC o entregarse a otra persona, todos los archivos vinculados deben ir con él, y olvidar uno provoca problemas durante el espectáculo.

La función ‘Pack’ resuelve esto: guarda una copia del quiz con todos los sonidos y vídeos incluidos, en un único archivo que puede llevar a otro ordenador. También puede hacer que ese archivo sea mucho más pequeño, recortando cada sonido y vídeo a la parte que realmente se reproduce y comprimiéndolos. El quiz que está editando nunca se modifica: al empaquetar siempre se escribe un archivo nuevo.

## Empaquetar un quiz

1. Guarde primero su quiz. Un quiz que nunca se ha guardado no se puede empaquetar.
2. Pulse F1 para ir al menú backstage y haga clic en ‘Pack’.
3. Compruebe el nombre de archivo en ‘Save as’. De forma predeterminada, el quiz empaquetado se guarda junto a su quiz, con ‘(packed)’ añadido al nombre. Haga clic en ‘Browse...’ para elegir otra ubicación u otro nombre.
4. Elija las opciones (véase más abajo) y haga clic en ‘Pack’.

![El cuadro de diálogo Pack quiz](../../assets/images/studio-pack-dialog.webp){ loading=lazy }

La lista muestra todos los sonidos y vídeos del quiz: la diapositiva en la que se encuentran, si están incrustados o vinculados, su tamaño, la parte que se reproduce (‘Plays’) y, en ‘Result’, lo que va a hacer el empaquetado con cada uno, como ‘Trim to 1:19–9:54’.

Durante el empaquetado, el progreso se muestra en la parte inferior y cada fila indica cuánto lleva. Puede seguir el resultado de cada sonido o vídeo a medida que llega. Haga clic en ‘Cancel’ para detenerlo: en ese caso no se guarda nada.

![Empaquetado en curso](../../assets/images/studio-pack-progress.webp){ loading=lazy }

Cuando termina, una barra verde muestra cuánto tiempo ha tardado y qué tamaño tenía el quiz antes y después del empaquetado. Haga clic en ‘Show in folder’ para abrir la carpeta con el quiz empaquetado.

![El resultado del empaquetado](../../assets/images/studio-pack-done.webp){ loading=lazy }

## Recortar sonidos y vídeos

A menudo, durante el quiz solo se reproduce una pequeña parte de una canción o de un videoclip, por ejemplo 20 segundos de una canción de 4 minutos. Con ‘Trim to the part that is played’ (por separado para ‘Sounds’ y ‘Videos’), el quiz empaquetado solo conserva esa parte. Esto puede ahorrar mucho espacio, especialmente en rondas de música y bingos musicales.

- La parte que se conserva va desde el ‘Start’ hasta el ‘End’ del sonido o vídeo, e incluye la parte ‘Replay’ cuando el sonido o vídeo se vuelve a reproducir después de la respuesta.
- ‘Margin’ añade unos segundos antes y después de esa parte (1 segundo de forma predeterminada), de modo que aún tenga un pequeño margen si más adelante desea ajustar los tiempos.
- Los tiempos de inicio, fin y repetición en el quiz empaquetado se ajustan automáticamente, de modo que el quiz se reproduce exactamente igual que antes.
- Un sonido o vídeo que se reproduce hasta el final conserva su final. Un vídeo en bucle que se reproduce hasta el final conserva también su principio, porque vuelve a empezar desde el principio del archivo.
- Los vídeos de fondo se recortan de la misma manera que los demás vídeos.
- Cuando se reproduce (casi) todo el archivo, no hay nada que recortar y el archivo se queda como está.

!!! note
    En el quiz empaquetado, no puede mover el inicio de un sonido o vídeo recortado más atrás de la parte que se conservó. Si aun así desea cambiar mucho los tiempos, hágalo en su quiz original y vuelva a empaquetarlo.

## Comprimir sonidos y vídeos

Con ‘Format’ elige cómo se almacenan los sonidos y vídeos en el quiz empaquetado:

| Sonidos | Qué hace |
|---|---|
| ‘Keep the format’ | Los sonidos se quedan como están. El recorte los corta sin convertirlos, por lo que no hay pérdida de calidad. |
| ‘MP3, high quality (about 190 kbps)’ | Convierte los sonidos a MP3. Los archivos WAV se vuelven mucho más pequeños de esta manera. |
| ‘MP3, compact (about 130 kbps)’ | Convierte los sonidos a un MP3 más pequeño, que sigue siendo adecuado para reproducir en una sala. |

| Vídeos | Qué hace |
|---|---|
| ‘Keep the video (cut at keyframes)’ | Los vídeos se quedan como están, sin pérdida de calidad. Un vídeo recortado empieza entonces en el fotograma clave más cercano anterior al corte, como máximo unos segundos antes; los tiempos se ajustan para ello. |
| ‘H.264, high quality’ | Convierte los vídeos a MP4 (H.264), que se reproduce en todas partes y suele ser mucho más pequeño. |
| ‘H.264, compact’ | Convierte los vídeos a un MP4 más pequeño, con cierta pérdida de detalle. |

Junto al formato de vídeo puede limitar el tamaño de la imagen a ‘Up to 1080p’ o ‘Up to 720p’. Los vídeos con una imagen más grande se reducen, lo que ahorra mucho espacio en los vídeos 4K.

QuizXpress solo convierte un archivo cuando merece la pena: un MP3 o un vídeo que ya es compacto se deja como está (‘Already compact’), y un resultado que no fuera más pequeño que el original no se utiliza (‘Would not get smaller’). Esto también mantiene el empaquetado rápido.

Sus elecciones se recuerdan para la próxima vez que empaquete un quiz.

## Instalar ffmpeg

El recorte y la compresión se realizan con ffmpeg, una herramienta gratuita que no forma parte de QuizXpress. En las opciones, el cuadro de diálogo muestra qué versión de ffmpeg utiliza. Cuando ffmpeg no está instalado, una barra en la parte superior del cuadro de diálogo ofrece tres formas de obtenerlo:

![El cuadro de diálogo Pack sin ffmpeg](../../assets/images/studio-pack-no-ffmpeg.webp){ loading=lazy }

- ‘Install with winget’ instala ffmpeg con el administrador de paquetes de Windows. Se abre una ventana de consola; siga sus indicaciones y acepte los términos de winget cuando se le pida. Cuando la ventana se cierra, QuizXpress encuentra ffmpeg por sí mismo y el recorte y la compresión pasan a estar disponibles.
- ‘Download’ abre la página de descarga de ffmpeg en su navegador. Descomprima la descarga en una carpeta de su elección.
- ‘Locate ffmpeg.exe...’ le permite indicar un ffmpeg.exe que ya tenga, por ejemplo en la carpeta ‘bin’ de la descarga. El ffprobe.exe que lo acompaña debe estar en la misma carpeta.

Sin ffmpeg todavía puede empaquetar un quiz: los medios vinculados se incrustan entonces tal como están.

## Archivos que faltan

Cuando no se encuentra un archivo de sonido o vídeo vinculado, su fila se muestra en rojo (‘File not found, stays linked’) y una advertencia en la parte inferior le indica cuántos archivos faltan. Todavía puede empaquetar el quiz, pero esos archivos siguen vinculados y faltarán en otro ordenador. Para incluirlos, localice primero los archivos que faltan en su quiz y vuelva a empaquetar.

## Desempaquetar un quiz

También puede desempaquetar un archivo de quiz empaquetado anteriormente. Esto extrae todos los medios (audio/vídeo) a una carpeta local y vincula los elementos multimedia del quiz a los archivos locales. Esto acelera los tiempos de carga del quiz y reduce el uso de memoria en el reproductor del quiz. Su uso principal es evitar problemas al trabajar con archivos de quiz enormes (~1,5 GB o más). Para desempaquetar un quiz, pulse F1 para ir al menú backstage y haga clic en ‘Unpack’.
