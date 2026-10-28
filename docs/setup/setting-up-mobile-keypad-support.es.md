# Configuración de la compatibilidad con mandos móviles

QuizXpress permite utilizar teléfonos móviles y tabletas como dispositivos de entrada. Los jugadores pueden conectarse mediante un navegador web estándar o utilizar nuestra aplicación Smart Buzzer para Android e iOS. Debe disponer de una licencia que admita mandos móviles antes de poder activar esta función.

Para habilitar la compatibilidad con mandos móviles, marque primero la casilla ‘Enable mobile keypad support’. A continuación verá tres secciones para configurar:

## Modo de servidor

Hay dos formas de ejecutar el sistema con mandos móviles:

1)  Mediante uno de nuestros servidores en la nube (se requiere internet para usted y para sus jugadores, que pueden participar desde cualquier lugar del mundo)

2)  Mediante un router Wi-Fi local conectado a su portátil (no se requiere internet, pero todos los jugadores deben estar en un mismo lugar físico para conectarse a su router)

![](../assets/images/image324.webp){ width="455" loading=lazy }

Hay varias opciones:

- **Play in ‘Headless’ mode** – Utilícela cuando no haya una pantalla externa o proyector disponible y desee que los jugadores jueguen únicamente con su móvil. Tenga en cuenta que en este caso no se admiten los minijuegos ni las preguntas de vídeo. Al jugar en modo headless, solo se mostrará la pantalla de Director en el equipo con un reproductor de quiz integrado (consulte [QuizXpress Director](../live/quizxpress-director/index.md) para obtener más información sobre Director).

- **Show pictures on mobile device** – Indica si las imágenes también se envían a la aplicación Smart Buzzer / aplicación de navegador buzzerpad (nota: durante el quiz puede activar o desactivar esto en los Mobile Settings de Director).

- **Enable waiting room** – cuando está activada, todos los jugadores móviles pasan inmediatamente a ‘disabled’ tras registrarse y no pueden participar en el quiz, aunque su dispositivo mostrará las preguntas. El anfitrión debe habilitar primero a cada jugador en Director. Utilícela, por ejemplo, cuando los jugadores deban pagar una entrada antes de poder participar.

- **Enable team name moderation – cuando está habilitada, el servidor buzzerpad analiza los nombres de los jugadores en busca de palabras malsonantes de una lista predefinida (actualmente solo en neerlandés, inglés y francés) y las sustituye por ‘#####’**

- **Allow profile pictures – permite a los jugadores subir sus fotos de perfil al quiz para que aparezcan en las clasificaciones y otros elementos visuales.Recopilación de datos con campos personalizados**

El sistema permite recopilar datos de cada usuario en una pantalla que aparece después de conectarse al quiz. Los campos que se van a recopilar pueden configurarse aquí, en Quiz Setup, y los datos capturados estarán disponibles después del quiz en el archivo de salida de Analyzer.

![](../assets/images/image325.webp){ width="449" loading=lazy }

Para añadir un campo, haga clic en Add e introduzca los detalles en la ventana emergente de campo personalizado:

![](../assets/images/image326.webp){ width="296" loading=lazy }

Cuando el usuario se conecta, se le presenta una pantalla de entrada de datos, como en el siguiente ejemplo:

![](../assets/images/image327.webp){ width="211" loading=lazy }

Al utilizar el modo *Remote server*, puede seleccionar el servidor que aloja su sesión de quiz haciendo clic en el botón *Configure proxy / server*. El servidor predeterminado es [www.buzzerpad.com](http://www.buzzerpad.com). Este servidor está situado en el centro-sur de EE. UU. Si se encuentra en Europa, puede que prefiera cambiar a [www.buzzerpad.eu](http://www.buzzerpad.eu) para obtener una menor latencia.

## Sección de mandos móviles

Aquí se configura el intervalo de mandos que pueden conectarse a su quiz. De forma predeterminada, al habilitar la compatibilidad con mandos móviles, el campo ‘Mobile device range’ se rellena con los identificadores del 1 hasta el número máximo de jugadores permitido por su licencia.

Si dispone de un kit de pulsadores o mandos, puede ampliarlo con jugadores que juegan con mandos móviles. En este caso, al habilitar la compatibilidad con mandos móviles, aparece un ‘Mobile device range’ que comienza con el identificador de mando o pulsador más alto definido en la pestaña Buzzers. El número máximo en este caso es el permitido por su licencia.

Ejemplo: en la pestaña Buzzers, indica que juega con los mandos QuizXpress 1-20. En la pestaña Mobile, habilita la compatibilidad con mandos móviles. Si tiene una licencia Ultimate 50 (que permite hasta 50 jugadores), el campo ‘Mobile device range’ se rellenará con 21-50.

### Jugar en grupos

Cuando desee que su público compita en grupos utilizando dispositivos móviles, debe predefinir una lista de grupos. Cuando un jugador se conecta a su quiz, se le solicita en su dispositivo que seleccione el grupo por el que jugará.

Al hacer clic en el botón ‘Groups’, aparece un formulario donde puede configurar los grupos y su comportamiento:

![](../assets/images/image328.webp){ width="298" loading=lazy }

En la sección inferior se define el comportamiento para las preguntas de fastest finger y de votación.

### Personalización de marca de la aplicación móvil

Al jugar con la aplicación QuizXpress Smart Buzzer, puede configurar su propia marca con el Branding Designer, cambiando los colores, el logotipo y la imagen de bienvenida de la aplicación:

![](../assets/images/image329.webp){ width="549" loading=lazy }

Jugar con grupos predefinidos

**Sección de mando a distancia móvil del anfitrión**

En esta sección se presenta el código QR utilizado para conectar la aplicación de control remoto con su equipo.

La aplicación para controlar el quiz en curso está disponible para Android e iOS. Puede encontrarlas aquí:

| Mobile Director para Android | <https://play.google.com/store/apps/details?id=com.gameshowcrew.quizxpressdirector> |
|-----------------------------|-------------------------------------------------------------------------------------|
| Mobile Director para iOS     | <https://apps.apple.com/us/app/quizxpress-director/id1493187163>                    |

En la aplicación de mando a distancia móvil puede registrar varios equipos para controlarlos. Estos equipos se muestran por su ‘Location name’, que se puede establecer en la sección Mobile remote. El nombre predeterminado es el nombre del equipo.

Para conectar el mando a distancia móvil del presentador al equipo, abra la aplicación Virtual remote y haga clic en el botón ‘más’. Se abre un lector de códigos QR en su dispositivo móvil. Escanee el código QR que se muestra en la sección Mobile remote, y el nombre introducido en el campo ‘Location name’ se añadirá a la lista de equipos de la aplicación de mando a distancia móvil.

!!! warning

    tenga en cuenta que la aplicación tiene un ajuste de servidor que debe corresponder al servidor que seleccionó en Quiz Setup. Además, si utiliza Wi-Fi, debe cambiar el ajuste de la aplicación a ‘Wi-Fi’.**

## Otras opciones – Waiting room

Si ejecuta un quiz con QuizXpress Mobile y desea tener más control sobre quién entra en el juego, puede utilizar el ajuste ‘Waiting Room’. Cuando este ajuste está activo, los jugadores que entran en el juego están inactivos de forma predeterminada.

Para dejar entrar a los jugadores en el juego, habilítelos explícitamente en la pestaña Teams de QuizXpress Director. Un ejemplo es un quiz de bar en el que los jugadores deben pagar una pequeña cuota para participar: al recibir el pago de un jugador, el anfitrión puede habilitar a ese jugador.
