# Importación y exportación de preguntas

En QuizXpress Studio puede importar desde distintas fuentes y exportar a ellas. Para ello, haga clic en la pestaña de cinta FILE y, a continuación, en Import o Export para ver las opciones.

## Importación en formato Excel

QuizXpress Studio permite importar preguntas desde Microsoft Excel. Quizá le resulte más cómodo introducir sus preguntas en Excel (aunque QuizXpress Studio también dispone de una vista de tabla para introducir preguntas rápidamente), o puede que tenga una base de datos de preguntas que se pueda exportar a Excel.

QuizXpress Studio admite el formato de archivo nativo .xlsx de Office 2007 y el formato CSV (archivo de texto separado por comas). Se recomienda el formato .xlsx, ya que presenta menos problemas de localización, caracteres especiales, etc.

Para definir sus preguntas en Excel, abra la plantilla preinstalada *quiztemplate.xlsx* (este archivo se encuentra en la carpeta de instalación de QuizXpress). También puede abrir la plantilla desde el menú backstage, en la sección 'Import'. A continuación se muestra la plantilla rellenada con algunas preguntas de música, cada una con un vídeo de fondo y algunas con un vídeo:

![La plantilla de Excel con preguntas de música de ejemplo](../assets/images/excel-template.webp){ loading=lazy }

La primera fila es obligatoria y debe seguir los nombres de encabezado siguientes:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Columna</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Q</td>
<td>Columna que contiene el texto de la pregunta. Si desea importar un idioma principal y uno secundario, separe el texto de ambos idiomas con || .</td>
</tr>
<tr class="even">
<td>A1-A6</td>
<td><p>Columnas que contienen las respuestas de las preguntas de opción múltiple. La respuesta correcta debe estar en la columna A1; el sistema mezclará las respuestas por usted. Puede dejar vacías todas las columnas A* para una pregunta abierta, o rellenar solo A1 y A2 para una pregunta de opción múltiple con dos respuestas, etc.</p>
<p>También puede marcar explícitamente la respuesta correcta de las preguntas de opción múltiple colocándola entre corchetes (‘[‘ y ‘]’). En este caso, el sistema no mezclará las respuestas. Si desea importar un idioma principal y uno secundario, separe el texto de ambos idiomas con ||.</p></td>
</tr>
<tr class="odd">
<td>CAT</td>
<td>Un nombre de categoría opcional. Las preguntas importadas recibirán automáticamente el formato de esta categoría. Si desea utilizar su propia categoría, debe crearla en el quiz antes de importar.</td>
</tr>
<tr class="even">
<td>P1-P6</td>
<td>Nombre de archivo opcional de una imagen. Puede ser una ruta absoluta (completa) al archivo, o un simple nombre de archivo si la imagen está en el mismo directorio que el archivo XLSX importado. Los formatos de archivo admitidos son <em>jpg, png, bmp, wmf, emf</em> y <em>gif.</em> También puede marcar explícitamente la imagen de la respuesta correcta de las preguntas de opción múltiple colocando el nombre del archivo de imagen entre corchetes (‘[‘ y ‘]’).</td>
</tr>
<tr class="odd">
<td>NOTES</td>
<td>Las notas opcionales del presentador del quiz que se añaden a la pregunta</td>
</tr>
<tr class="even">
<td>SOUND</td>
<td>Una ruta opcional a un archivo de sonido que se añade a la pregunta</td>
</tr>
<tr class="odd">
<td>VIDEO</td>
<td>Una ruta opcional a un archivo de vídeo (WMV, AVI, etc.) que se añade a la pregunta (no puede utilizarse junto con P1-P4). Deje vacíos todos los demás campos para obtener una diapositiva de vídeo a pantalla completa.</td>
</tr>
<tr class="even">
<td>BACKGROUND</td>
<td>Una ruta opcional a una imagen de fondo de la diapositiva (png, jpg, bmp, etc.)</td>
</tr>
<tr class="odd">
<td>BACKGROUND-VIDEO</td>
<td>Una ruta opcional a un vídeo que se reproduce detrás de la diapositiva (consulte <a href="../backgrounds/#video-de-fondo">Vídeo de fondo</a>). No ocupa ningún marcador de posición, por lo que puede combinarse con imágenes (P1-P6) o con un VIDEO. Cuando la pregunta tiene una categoría con vídeo de fondo, el vídeo de esta columna lo sustituye para esta pregunta.</td>
</tr>
</tbody>
</table>

Los libros de trabajo creados con una plantilla anterior, sin la columna BACKGROUND-VIDEO, aún se pueden importar.

Además de este conjunto fijo de columnas, hay una serie de columnas definibles por el usuario que se pueden elegir en la lista desplegable de la plantilla de Excel:

| Columna              | Descripción                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| A7                   | Define la respuesta 7. Para usar en la importación de Trivia Feud                                                                           |
| A8                   | Define la respuesta 8. Para usar en la importación de Trivia Feud                                                                           |
| POINTS-START         | Puntos que se pueden ganar al inicio de la cuenta atrás                                                                                     |
| POINTS-END           | Puntos que se pueden ganar al final de la cuenta atrás                                                                                      |
| PENALTY-POINTS-START | Puntos de penalización al inicio de la cuenta atrás                                                                                         |
| PENALTY-POINTS-END   | Puntos de penalización al final de la cuenta atrás                                                                                          |
| NO-ANSWER-POINTS     | Puntos de penalización cuando no se da respuesta                                                                                            |
| BONUS-POINTS-1       | Puntos de bonificación para el jugador más rápido con respuesta correcta                                                                    |
| BONUS-POINTS-2       | Puntos de bonificación para el segundo jugador más rápido con respuesta correcta                                                            |
| BONUS-POINTS-3       | Puntos de bonificación para el tercer jugador más rápido con respuesta correcta                                                             |
| ANSWER-TIME          | Tiempo de respuesta en segundos                                                                                                             |
| STYLE                | Nombre del estilo de la diapositiva (consulte las descripciones emergentes del selector de estilos de Studio para ver los nombres correctos; por ejemplo: Millionaire, Neon Tubes, etc.) |
| TRANSITION           | El nombre de la transición de la diapositiva. Valores válidos: Default, None, MoveRight, MoveLeft, MoveToFront, PageTurnLeft, ScaleToZero, LiftAndMoveRight, Fade |
| SHUFFLEMODE          |                                                                                                                                             |
| EVALUATION-MODE      |                                                                                                                                             |
| NEAREST-WINS-WINNERS |                                                                                                                                             |
| TEXT-EVALUATION      |                                                                                                                                             |
| TOLERANCE            |                                                                                                                                             |
| END-OF-ROUND-ACTION  |                                                                                                                                             |

Guarde el archivo en Excel y, a continuación, seleccione 'FILE->Import->Import from Excel' en QuizXpress Studio. Aparece un explorador de archivos en el que puede seleccionar el archivo de Excel que desea importar.

En función de las columnas que rellene, QuizXpress selecciona automáticamente un diseño de diapositiva adecuado. Por ejemplo, para obtener una pregunta de opción múltiple con 3 respuestas y un vídeo, rellene las columnas Q, A1, A2, A3 y VIDEO. Para obtener una pregunta abierta con un fragmento de sonido, una imagen y una imagen de fondo, rellene las columnas Q, P1, SOUND y BACKGROUND.

De forma predeterminada, todas las diapositivas se crean como preguntas del quiz. Sin embargo, puede especificar el tipo de diapositiva que se creará anteponiendo al texto de la columna Q uno de los siguientes identificadores:

| Prefijo | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {Q}    | Crea una pregunta normal. Puede utilizar los siguientes calificadores adicionales para especificar cómo se crea la pregunta: **EA** – Everyone Answers (todos responden), **FF** – Fastest Finger, **NUM** – crea una pregunta numérica, **LET** – crea una pregunta de letra, **TXT** – crea una pregunta de texto completo, **CA** – Countdown Automatically (cuenta atrás automática), **CM** – Countdown Manual (cuenta atrás manual). Por ejemplo, **{Q, EA, CM}** crea una pregunta en la que todos pueden responder (votación), con inicio manual del temporizador de cuenta atrás. |
| {T}    | Crea una pregunta de test                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| {W}    | Crea una diapositiva de apuesta (también debe especificar dos o más porcentajes en las respuestas, como '20%')                                                                                                                                                                                                                                                                                                                                                               |
| {B}    | Crea una diapositiva billboard (estática)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| {A}    | Crea una diapositiva de respuesta del público                                                                                                                                                                                                                                                                                                                                                                                                                                |
| {D}    | Crea una diapositiva demográfica                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| {L}    | Crea una diapositiva de last-man-standing                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| {E}    | Crea una diapositiva de fin de ronda (End-of-Round)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {M}    | Crea una diapositiva de Majority Rules                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| {J}    | Crea una diapositiva de Trivia Board                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| {TL}   | Crea una diapositiva de Trivia Ladder                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| {TF}   | Crea una diapositiva de Trivia Feud (use A1..A8 para las entradas de la encuesta)                                                                                                                                                                                                                                                                                                                                                                                            |
| {SR}   | Crea una diapositiva de Speed Round (debe terminar con una diapositiva de fin de ronda)                                                                                                                                                                                                                                                                                                                                                                                      |

Así, por ejemplo, el texto “{A}¿Le gusta esta noche de quiz?” importa una diapositiva de respuesta del público con el texto “¿Le gusta esta noche de quiz?”

El sonido y el vídeo insertados en la diapositiva mediante las columnas SOUND, VIDEO y BACKGROUND-VIDEO normalmente se incrustan, es decir, todo el contenido del archivo de sonido o vídeo se almacena dentro del archivo de quiz. Esto puede dar lugar a archivos de quiz muy grandes. Para evitarlo, puede anteponer '{L}' a los valores de estas columnas para indicar que desea vincular los archivos multimedia. Por ejemplo: “{L} C:\Users\Public\Videos\Sample Videos\Wildlife.wmv”. Tenga en cuenta que los archivos vinculados deben seguir estando presentes en su sistema al ejecutar el quiz. Cuando varias preguntas utilizan el mismo archivo de vídeo de fondo, este se almacena una sola vez en el quiz.

Puede añadir ajustes a un vídeo de la columna VIDEO o BACKGROUND-VIDEO colocándolos entre llaves después del nombre del archivo, separados por punto y coma. Por ejemplo: “intro.mp4{loop=false;sync-with-quiz=true}”. Los ajustes que omita conservan su valor predeterminado.

| Ajuste         | Descripción                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
| start-at       | Dónde empieza el vídeo, por ejemplo 00:00:05                                                                              |
| stop-at        | Dónde termina el vídeo, por ejemplo 00:00:20                                                                              |
| loop           | true o false: reproducir el vídeo de nuevo cuando termina. Valor predeterminado: true para un vídeo de fondo, false para un vídeo en un marcador de posición |
| silent         | true o false: reproducir sin sonido. Valor predeterminado: true para un vídeo de fondo, false para un vídeo en un marcador de posición |
| volume         | Volumen de 0 a 100 (predeterminado 100)                                                                                   |
| speed          | Velocidad de reproducción en porcentaje, de 25 a 250 (predeterminado 100)                                                 |
| effect         | Un efecto de vídeo, como Blur o Mosaic                                                                                    |
| intro-pause    | Solo VIDEO: segundos de espera antes de que empiece el vídeo (predeterminado 1)                                           |
| sync-with-quiz | Solo BACKGROUND-VIDEO: true para pausar el vídeo de fondo junto con el quiz (predeterminado false)                        |

Puede crear rondas en su quiz añadiendo varias hojas de cálculo al libro de Excel. Por cada hoja de cálculo se inserta en el quiz una diapositiva de tipo 'billboard' que contiene el nombre de la hoja para anunciar la siguiente ronda. Por ejemplo, suponga que tiene dos hojas, 'Round 1' y 'Round 2', cada una con diez preguntas. Al importar el archivo de Excel en QuizXpress Studio, obtiene un quiz que contiene: un billboard con el texto 'Round 1', seguido de diez preguntas, seguido de un billboard con el texto 'Round 2', de nuevo seguido de diez preguntas.

## Exportación a Excel

'FILE->Export->Export to Excel' guarda las preguntas de su quiz en el mismo formato, como un archivo CSV que se abre en Excel y que se puede volver a importar. Las imágenes, los sonidos y los vídeos se guardan junto al archivo CSV. Los sonidos y los vídeos conservan el nombre de su archivo original, y un archivo compartido por varias preguntas, como el vídeo de fondo de una categoría, se guarda una sola vez. En el caso de los vídeos, solo se escriben los ajustes que difieren del valor predeterminado.

## Importación desde PowerPoint

QuizXpress Studio también permite importar preguntas desde PowerPoint. En este caso, las diapositivas de PowerPoint se importan como imágenes y se colocan en diapositivas Billboard. Si desea convertir diapositivas en preguntas, es necesario un posprocesado: primero establezca el tipo de diapositiva en 'Question' y, si hay respuestas de opción múltiple, cambie el diseño de la diapositiva para incluir el mismo número de respuestas, establezca el estilo de la diapositiva en 'Just Text' y elimine los textos de pregunta y respuesta en QuizXpress Studio.

## Importación desde Spotify™

Con esta función puede convertir sus listas de reproducción favoritas en un quiz de música de QuizXpress o en un bingo musical con muy poco esfuerzo. Spotify expone unos 30 segundos de la pista de música (predefinidos) y una imagen de la carátula del álbum. Hay dos pasos sencillos: primero exporta su lista de reproducción a un archivo separado por comas (csv) con Exportify, un sitio web público que se encuentra en: <https://exportify.app/> . Después importa este archivo csv en QuizXpress Studio mediante la función de importación de Excel. El sistema reconocerá el formato y le presentará el siguiente formulario de opciones:

![](../assets/images/image255.webp){ width="270" loading=lazy }

Aquí especifica qué crear, junto con varias opciones. En este ejemplo creamos un bingo musical con 75 diapositivas: la mitad de las casillas del bingo estarán formadas por carátulas de álbum, y el resto será texto con Artista/Canción. Tras la importación, los fragmentos de música de 30 segundos estarán en las diapositivas, y un cartón de bingo de ejemplo tendrá este aspecto:

![](../assets/images/image256.webp){ loading=lazy }

Del mismo modo, puede crear un quiz de preguntas sobre música.

![](../assets/images/image257.webp){ loading=lazy }

!!! note

    asegúrese de no infringir ningún derecho de autor al utilizar esta función.*

## Importación desde QuizXpress

Si desea añadir preguntas de un quiz de QuizXpress existente a un quiz que está creando, haga clic en el botón *Import from QuizXpress* y seleccione un archivo de QuizXpress. Como alternativa, puede abrir dos instancias de QuizXpress Studio y copiar y pegar diapositivas entre ellas.

## Exportación a PDF

QuizXpress Studio le permite exportar sus preguntas en formato PDF. Este archivo PDF se puede imprimir o enviar a sus clientes para ofrecerles una vista previa del quiz. Es posible que su presentador del quiz también desee recibir una copia impresa antes del espectáculo. La exportación a PDF está disponible en 'FILE->Export->Export to PDF'. *(Nota: esta opción no está disponible en la edición Home).* La exportación a PDF ofrece las siguientes opciones:

![](../assets/images/image258.webp){ width="370" loading=lazy }

| Campo                     | Descripción                                                          |
|---------------------------|----------------------------------------------------------------------|
| Target PDF File           | El archivo PDF de salida. Use el botón \[…\] para buscar una carpeta o archivo |
| Logo on first page        | El logotipo que se mostrará en la primera página del PDF             |
| Include slides            | Active para incluir imágenes de las diapositivas                     |
| Include questions as text | Incluye un resumen en texto de las preguntas y respuestas            |
| Show correct answers      | Incluye las respuestas correctas en la salida.                       |
| Include question numbers  | Incluye los números de pregunta en la exportación a PDF              |
| Page options              | Permite combinar varias diapositivas en una página                   |

!!! note

    para poder leer documentos PDF en su ordenador necesita el lector Adobe PDF, disponible para su descarga en <http://get.adobe.com/reader/>*

## Exportación a HTML

Puede exportar un quiz a HTML para ejecutarlo en un sitio web. Tenga en cuenta que esta funcionalidad es muy básica: entre otras cosas, no se admiten los efectos de audio, vídeo e imagen y, aunque se muestra una puntuación, no hay anuncio de la puntuación final.
