# Configuración del sistema

Como se ha comentado anteriormente, existen varias posibilidades con el sistema para distintos escenarios. Para obtener más información sobre cómo configurar QuizXpress para su uso con teléfonos móviles, consulte también [Configuración de la compatibilidad con mandos móviles](../../setup/setting-up-mobile-keypad-support.md).

**Modo servidor**

Al utilizar el sistema en modo servidor, necesita una **conexión a internet fiable** con una velocidad aceptable. El tráfico de datos de QuizXpress no es muy elevado en comparación, por ejemplo, con una transmisión de vídeo, pero una conexión poco fiable o caídas de velocidad importantes afectarán notablemente al sistema y a la experiencia global. Por supuesto, si transmite su quiz por internet al mismo tiempo, es posible que haya requisitos adicionales para la transmisión de vídeo. Siempre es aconsejable conectar su ordenador al router mediante un cable para lograr una conexión más constante y fiable. Su público puede participar en su quiz de dos maneras: mediante el sitio web buzzerpad.com o mediante la aplicación Smart Buzzer. Consulte los capítulos siguientes para obtener más detalles. En [Configuración de la compatibilidad con mandos móviles](../../setup/setting-up-mobile-keypad-support.md) puede leer todo sobre cómo configurar el sistema para el modo servidor en Quiz Setup.

**Modo Wi-Fi independiente**

En una configuración Wi-Fi independiente, conecte su portátil al router mediante un cable de red. El router actúa como punto de acceso Wi-Fi local para los dispositivos móviles de sus jugadores, el dispositivo que ejecuta la aplicación de control remoto y su portátil. Vea a continuación una imagen de dicha configuración:

![](../../assets/images/image355.webp){ width="604" loading=lazy }

El portátil obtiene una dirección IP del router local y no necesita ninguna conexión a internet. Un router estándar y decente admite hasta ~50 jugadores; también existen routers que gestionan más conexiones. Los teléfonos y tabletas deben conectarse al mismo router y, al iniciar la aplicación Smart Buzzer, el botón JOIN WI-FI GAME se habilita cuando el dispositivo encuentra el quiz en ejecución.

Tenga en cuenta que algunos paquetes antivirus incluyen cortafuegos integrados muy estrictos, y estos cortafuegos necesitan una configuración especial para permitir el tráfico de red de QuizXpress. Para añadir una excepción para QuizXpress, permita todo el tráfico del programa *qxserver.exe*, que se encuentra en la carpeta de instalación de QuizXpress. Esto no es necesario con el cortafuegos estándar de Windows.
