# La pestaña Media Player

Esta pestaña de Director muestra el reproductor multimedia de QuizXpress. Con el reproductor multimedia puede:

- Lanzar un vídeo a pantalla completa en la pantalla principal

- Mostrar una imagen a pantalla completa en la pantalla principal

- Reproducir un archivo MP3

- Presentar una imagen promocional en la aplicación Smart Buzzer

- Repetir/reanudar el vídeo de la diapositiva actual

- Repetir/reanudar el sonido de la diapositiva actual

- Ajustar el volumen del reproductor del quiz

- Mantener una lista de archivos multimedia

- Reproducir archivos con un solo clic desde la [mesa de sonido](#la-mesa-de-sonido)

Cuando añade archivos a la lista, en realidad se copian a la carpeta local de datos de la aplicación QuizXpress (ruta del Explorador %AppData%\QuizXpress\Media). Esto evita problemas cuando los archivos originales se mueven, se eliminan, etc. Por lo tanto, si elimina un archivo de la lista, se eliminará del almacenamiento de QuizXpress, pero el archivo original permanecerá intacto.

![](../../assets/images/image454.webp){ width="605" loading=lazy }

## Búsqueda en la lista

Si tiene muchos archivos multimedia, utilice el campo de búsqueda situado encima de la lista para encontrar uno rápidamente. Escriba parte del nombre de un archivo y la lista solo mostrará los archivos que lo contengan; por ejemplo, 'chris' encuentra tanto 'Chris Rea - Driving home for christmas' como 'Band Aid 30 - Do They Know It's Christmas'. No se distingue entre mayúsculas y minúsculas. Pulse Esc o borre el campo para volver a mostrar todos los archivos.

![Lista multimedia filtrada con el campo de búsqueda](../../assets/images/media-player-search.webp){ width="605" loading=lazy }

Mientras escribe en el campo de búsqueda, teclas como Space, 'C' y 'S' van al campo y no activan los atajos de Director. La búsqueda solo filtra la lista; la mesa de sonido conserva todos sus pads.

## La mesa de sonido

Junto a la lista, la pestaña Media Player tiene una mesa de sonido: una cuadrícula de pads de colores brillantes, como los launch pads que usan los DJ. Un clic en un pad reproduce su sonido, vídeo o imagen, de modo que jingles, aplausos y música de entrada siempre están al alcance de su mano.

![Mesa de sonido con un pad en reproducción y otro en pausa](../../assets/images/media-player-sound-board.webp){ loading=lazy }

- El pad que se está reproduciendo se ilumina y muestra el tiempo restante y una barra de progreso. Un pad en pausa muestra un símbolo de pausa.
- Haga clic de nuevo en un pad en reproducción para detenerlo.
- Los pads inactivos muestran la duración de su archivo.

Al hacer clic en un pad también se selecciona su archivo en la lista, de modo que los botones de reproducir, pausar, detener y rebobinar de la barra de herramientas actúan sobre ese archivo.

### Mostrar la lista, la mesa de sonido o ambas

Utilice los botones 'List' y 'Sound board' a la derecha de la barra de herramientas para mostrar la lista, la mesa de sonido o ambas una junto a otra. Siempre se muestra al menos una de ellas. Cuando se muestran ambas, arrastre el divisor entre ellas para dar más espacio a una u otra. Director recuerda su elección.

### Colocar archivos en los pads

La primera vez que abre la mesa de sonido, se rellena automáticamente con sus archivos multimedia. Para organizarla usted mismo:

- Arrastre un archivo de la lista a un pad.
- Arrastre archivos directamente desde el Explorador de Windows a un pad. Se añaden a la lista multimedia (se copian a la carpeta multimedia, igual que con 'Add') y se colocan en ese pad. Si suelta varios archivos, los demás van a los siguientes pads vacíos.
- Arrastre un pad sobre otro pad para intercambiarlos.

Una vez que haya modificado la mesa usted mismo, los nuevos archivos multimedia ya no se añaden a ella automáticamente. Utilice 'Fill empty pads with media files' (véase más abajo) para añadirlos.

![Mesa de sonido junto a la lista, con el menú del pad](../../assets/images/media-player-sound-board-menu.webp){ loading=lazy }

### Opciones de pad y de mesa

Haga clic con el botón derecho en un pad para:

- 'Play' o 'Stop' para reproducirlo o detenerlo.
- 'File': elegir qué archivo multimedia reproduce el pad. Además de sus archivos multimedia, un pad también puede controlar el sonido o el vídeo de la diapositiva actual ('Slide Sound' y 'Slide Video').
- 'Label': dar al pad un nombre corto, por ejemplo 'Applause' en lugar de un nombre de archivo largo. Déjelo vacío para volver a mostrar el nombre del archivo.
- 'Color': elegir un color, o 'Automatic' para colorear los pads por columna.
- 'Clear pad': quitar el archivo del pad. El archivo permanece en la lista multimedia.

El mismo menú, que también está disponible al hacer clic con el botón derecho en la mesa alrededor de los pads, tiene opciones para toda la mesa:

- 'Grid size': de 3 × 4 hasta 8 × 8 pads. Los pads conservan su lugar al cambiar el tamaño.
- 'Clicking a playing pad': elegir si un clic en un pad en reproducción lo detiene (opción predeterminada), lo reinicia, o lo pausa y reanuda.
- 'Fill empty pads with media files': coloca en los pads vacíos los archivos multimedia que aún no están en la mesa.
- 'Clear all pads': vacía la mesa. Sus archivos multimedia se conservan.

!!! note
    La mesa de sonido se guarda en este ordenador, junto a la carpeta multimedia (%AppData%\QuizXpress\SoundBoard.xml), por lo que seguirá allí la próxima vez que dirija un show. Cuando elimina un archivo de la lista multimedia, también se quita de sus pads.
