# Configuración de los equipos – la pestaña Teams

Hay dos ‘versiones’ distintas de la pestaña Teams: una cuando se seleccionan pulsadores Sony en la pestaña ‘Buzzers’ y otra cuando se seleccionan pulsadores Fleetwood Reply o QuizXpress (dispositivos numerados).

## Pestaña Teams – pulsadores Sony

A continuación puede ver la pestaña Teams utilizada cuando se seleccionan pulsadores Sony. Sus funciones incluyen:

- Añadir y eliminar equipos

- Indicar si un equipo participa en el quiz.

- Asignar avatares a los equipos. En la parte inferior de la página de ajustes de equipos, puede indicar en qué carpeta se encuentran los avatares utilizados.

En la parte superior de la página puede ver cuántos juegos de pulsadores son necesarios según el número de equipos de la lista que participan.

Otra función es la posibilidad de utilizar equipos anónimos. En este caso, se ignora la lista de equipos/avatares y el proceso de registro se asemeja al de los pulsadores Fleetwood Reply. Esto se utiliza normalmente cuando se emplean grandes cantidades de pulsadores Sony, ya que el procedimiento de registro normal para los pulsadores Sony, que asocia cada pulsador con un equipo de uno en uno, tardaría demasiado.

![](../assets/images/image330.webp){ width="605" loading=lazy }

## Pestaña Teams – mandos QuizXpress

En la pestaña Teams puede definir los nombres de los equipos/jugadores y definir grupos. Esta pestaña no está disponible cuando se utiliza únicamente Mobile; cuando Mobile se utiliza en combinación con mandos o pulsadores, la página sigue mostrándose.

Para todos los tipos de pulsadores excepto los pulsadores Sony, el número de equipos se deriva de la cadena ‘Keypads’ introducida en la pestaña ‘Buzzers’. Por ejemplo, cuando se utiliza la cadena 1-50, la pestaña ‘Teams’ muestra una lista de mandos del 1 al 50 y los nombres de equipo predeterminados *Team 1 … Team 50*. Los nombres de los equipos se pueden cambiar en la segunda columna de la lista.

Como se explicó anteriormente, si desea cambiar el número de equipos, modifique la cadena ‘Keypads’ en la pestaña ‘Buzzers’.

!!! note

    es posible utilizar avatares en combinación con pulsadores Reply/QuizXpress. Para ello, cree imágenes (.jpg o .gif) en la carpeta de avatares predeterminada (c:\program files\game show crew\QuizXpress\Data\IQ\Avatars) con los nombres de los equipos. Por ejemplo, para Team A, cree una imagen llamada ‘Team A.jpg’.

Como se puede ver en la imagen siguiente, hay disponibles otros comandos:

- Generate Names: permite generar rápidamente nombres de equipo utilizando un cierto patrón seguido de un índice. Por ejemplo, podría generar rápidamente nombres como equipo 1…equipo 50, jugador 1…jugador 50, participante 1…participante 50

- Import: importa la lista de nombres de equipo desde Excel o un archivo de texto. Para Excel, coloque los nombres en la primera columna de la primera hoja; para un archivo de texto, coloque cada nombre en una línea nueva.

- Save to PDF: para obtener un resumen de los equipos asignados a cada mando, exporte la lista a PDF pulsando el botón ‘Save to PDF’

- Groups: es posible dividir los equipos en grupos. Puede obtener más información al respecto en la siguiente sección.

> ![](../assets/images/image331.webp){ width="605" loading=lazy }

### Agrupación de mandos

Es posible dividir los equipos en grupos en Quiz Setup (alternativamente, también es posible dividir los equipos en grupos mientras se ejecuta un quiz. Consulte [Demográfico](../live/starting-a-quiz/the-quiz-screen-voting-everybody-answers.md#demographic) en las diapositivas demográficas del quiz para obtener más información al respecto.

Al hacer clic en el botón ‘Groups’, se muestra una lista donde puede introducir los nombres de los grupos y su conjunto de mandos correspondiente. Vea la imagen siguiente:

![](../assets/images/image332.webp){ width="605" loading=lazy }

Al pulsar el botón ‘Add’, aparece una ventana donde puede introducir tanto el nombre del grupo como los mandos correspondientes (introduciendo una cadena de mandos). También puede eliminar grupos.

Al introducir el intervalo de mandos de un grupo (por ejemplo, ‘1, 2, 3, 10-20’), se comprueba que el intervalo esté dentro del intervalo de mandos definido en la pestaña ‘Buzzers’. Si no es así, se muestra un mensaje de error.

Los demás ajustes que puede cambiar aquí son cómo deben comportarse los grupos en las preguntas de fastest finger y de votación.

Las opciones para las preguntas de fastest finger son:

| **Lockout**    | Con esta opción habilitada, solo el primer jugador de un grupo que responda puede contestar la pregunta. Si la respuesta dada es incorrecta, todo el grupo queda bloqueado. |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **No lockout** | Si la primera persona de los grupos responde mal, otra persona del grupo aún puede intentarlo.                                                                 |

Las opciones para las preguntas de votación son:

| **Accept only the first response** | Solo cuenta la primera respuesta recibida del grupo y suma puntos a la puntuación del grupo |
|------------------------------------|--------------------------------------------------------------------------------------------|
| **Sum points**                     | Se aceptan todas las respuestas y se suman los puntos                                      |
| **Average points**                 | Se aceptan todas las respuestas y se calcula la media de los puntos                        |

#### Mostrar las respuestas de los grupos en tiempo real durante el quiz

Cuando habilita el ajuste ‘Show real time group responses’, las respuestas de cada grupo se muestran en pantalla en tiempo real durante el concurso.

![](../assets/images/image333.webp){ width="442" loading=lazy }

Mientras el reloj cuenta hacia atrás, para cada grupo verá el número de jugadores del grupo, así como el número de los que han respondido hasta el momento. Por ejemplo, en la imagen anterior, el grupo HR tiene 15 jugadores, de los cuales 3 han respondido hasta el momento.

Al final de la cuenta atrás, se muestran por grupo el número de respuestas correctas, el número de respuestas incorrectas y el porcentaje de respuestas correctas.

![](../assets/images/image334.webp){ width="463" loading=lazy }

### Asignación de dispositivos Galaxy y marcadores a los participantes

Cuando su licencia de QuizXpress incluye compatibilidad con dispositivos Galaxy o marcadores, verá las siguientes opciones en la pestaña Buzzers de QuizXpress Setup:

![](../assets/images/image335.webp){ width="234" loading=lazy }

Al habilitar la compatibilidad con Galaxy o con marcadores, aparecen columnas adicionales en la lista de la pestaña Teams.

![](../assets/images/image336.webp){ width="504" loading=lazy }

Cada dispositivo Galaxy o marcador tiene un ID. En esta lista puede indicar qué ID de dispositivo Galaxy y/o ID de marcador se utiliza para cada jugador.
