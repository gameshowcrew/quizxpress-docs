# Descripción general

QuizXpress Mobile permite a los jugadores utilizar su teléfono móvil como dispositivo de entrada. Los jugadores pueden unirse a un quiz accediendo a nuestro sitio web buzzerpad (se requiere conexión a internet) e introduciendo el código PIN que se muestra en pantalla para conectarse.

QuizXpress Mobile también ofrece una forma de jugar con teléfonos móviles sin conexión a internet. En esta solución, los jugadores descargan la aplicación QuizXpress Smart Buzzer, disponible para iOS y Android. Se conecta un router Wi-Fi al ordenador y todos los jugadores se conectan a él con su teléfono. Tras iniciar un quiz, los jugadores pueden conectarse en la aplicación Smart Buzzer pulsando el botón *JOIN Wi-Fi Game*. La aplicación Smart Buzzer también permite jugar a través de internet introduciendo un código PIN.

Con esta incorporación, QuizXpress admite ahora:

| **Escenario** |                                                                | **Internet requerido** | **Router Wi-Fi requerido** | **Dispositivo móvil requerido** | **Instalación de aplicación móvil requerida** |
|--------------|----------------------------------------------------------------|-----------------------|---------------------------|----------------------------|-----------------------------------------|
| 1            | Mandos inalámbricos de radiofrecuencia (RF)                    | No                    | No                        | No                         | No                                      |
| 2            | Dispositivos móviles en buzzerpad.com mediante navegador web   | Sí                    | No                        | Sí                         | No                                      |
| 3            | Dispositivo móvil con la aplicación Smart Buzzer en Wi-Fi local | No                   | Sí                        | Sí                         | Sí                                      |
| 4            | Dispositivo móvil con la aplicación Smart Buzzer en buzzerpad.com mediante PIN | Sí    | No                        | Sí                         | Sí                                      |

Todos los escenarios tienen ventajas e inconvenientes diferentes, y lo que más conviene utilizar depende de sus necesidades específicas.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 39%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Escenario</strong></th>
<th><strong>Ventajas</strong></th>
<th><strong>Inconvenientes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1 Mandos RF inalámbricos</strong></td>
<td><p>Sin dependencias externas de internet, Wi-Fi ni dispositivos móviles.</p>
<p>Sencillo de usar para los jugadores.</p></td>
<td>Sin capacidades de entrada ampliadas (solo ABCDEF y fastest finger). Logística de entregar los mandos a los jugadores y recogerlos después.</td>
</tr>
<tr class="even">
<td><strong>2 Navegador en buzzerpad.com</strong></td>
<td>No es necesario pedir a los jugadores que instalen una aplicación. Para grupos grandes de jugadores (hasta 2000).</td>
<td>Se requiere una conexión a internet</td>
</tr>
<tr class="odd">
<td><strong>3 Aplicación en Wi-Fi local</strong></td>
<td><p>Comunicación rápida y de baja latencia.</p>
<p>Compatible con el modo headless (sin pantalla central).</p>
<p>Compatible con tipos de entrada ampliados.</p></td>
<td>Con una infraestructura básica (router Wi-Fi estándar) solo se admiten grupos pequeños de unos 50 jugadores. Nota: si no hay conexión a internet ni de datos móviles, asegúrese de que los jugadores ya hayan descargado la aplicación con antelación</td>
</tr>
<tr class="even">
<td><strong>4 Aplicación con internet completo</strong></td>
<td><p>Compatible con grupos grandes</p>
<p>Capacidades de entrada ampliadas</p>
<p>No se necesita configuración de Wi-Fi local</p></td>
<td>Se requiere una conexión a internet</td>
</tr>
</tbody>
</table>

El mando móvil (tanto buzzerpad como la aplicación Smart Buzzer) tiene excelentes funciones:

- Las preguntas se presentan íntegramente en el dispositivo móvil, incluidas las imágenes y los efectos.

- Varios tipos de preguntas específicos para el uso de un teléfono móvil:

  - Preguntas numéricas, por ejemplo para pedir el resultado de una fórmula o un año histórico.

  - Preguntas de texto libre (respuesta única o múltiple)

  - Preguntas de primera letra (A-Z)

- Puntos de bonificación personalizables para los 3 equipos más rápidos en responder correctamente.

- Experiencia mejorada para las preguntas de ordenación y las preguntas con varias respuestas correctas. Los usuarios pueden ordenar primero las respuestas en su dispositivo y después enviar el resultado a QuizXpress de una sola vez.

- Funcionalidad de control remoto mediante la aplicación Mobile QuizXpress Director, disponible para iOS y Android. Consulte el apartado 5.2.4.4 para obtener más información.

Además de las funciones anteriores, la aplicación Smart Buzzer ofrece algunas funciones adicionales:

- Branding designer para personalizar la aplicación móvil con logotipos y colores.

- Compatibilidad con el «modo headless» para presentar un quiz sin pantalla central.

- Jingles de equipo seleccionables por el usuario. Si ha configurado el uso de jingles definiendo la carpeta Jingles en los ajustes (consulte [Configuración de los sonidos: la pestaña Sounds](../../setup/configuring-sounds-the-sounds-tab-page.md) ), se mostrará a los jugadores una lista de todos los fragmentos de sonido disponibles. Cada jugador puede elegir un jingle que se utilizará durante la partida en las siguientes situaciones:

<!-- -->

- Puntos de bonificación: el sonido del jugador que fue el primero en dar la respuesta correcta se reproduce cuando se muestra la pantalla de puntos de bonificación.

- Fastest finger: se reproduce el sonido del jugador que pulsó primero, y el nombre del jugador aparece en pantalla en el quiz player.

- Resúmenes de puntuación intermedios: el sonido del jugador que ocupa el primer puesto se reproduce al mostrar la clasificación.

Algunos ejemplos de escenarios admitidos son:

- Un DJ que presenta un quiz en un pub local sin cobertura 4G. Los clientes descargan la aplicación una sola vez y se conectan a un router Wi-Fi local para participar. El pub no tiene televisor, así que el presentador utiliza el modo headless. El DJ ha personalizado la aplicación con el estilo de su propia empresa mediante el QuizXpress Branding Designer.

- Una gran empresa de eventos que presenta un quiz para un grupo numeroso. La empresa no quiere que el público instale una aplicación, por lo que utiliza buzzerpad.com y un código PIN para que la gente participe. El quiz se presenta en una enorme pantalla que muestra vídeos, sonido e imágenes.

- Una empresa de eventos que transmite un quiz por internet a miles de jugadores, utilizando un código PIN en modo servidor. La empresa vendió entradas a los jugadores de antemano; las entradas se validan cuando un jugador se conecta a la partida e introduce su código en la ventana emergente que aparece.
