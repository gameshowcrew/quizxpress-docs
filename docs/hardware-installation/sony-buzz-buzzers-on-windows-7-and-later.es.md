# Pulsadores Sony Buzz en Windows 7 y posteriores

La última revisión de los pulsadores Sony Buzz™ requiere un procedimiento especial para que funcionen con QuizXpress en Windows Vista o Windows 7. Este apéndice describe los pasos para instalar correctamente el receptor USB de Sony Buzz™ en estos sistemas operativos.

Puede reconocer esta nueva revisión por el texto “Manufactured by Logitech…” en el receptor USB. Los pulsadores no tienen el botón de encendido en el lado derecho y falta el LED azul presente en las revisiones anteriores. Este modelo de pulsador se enciende pulsando una vez el botón rojo grande.

Conecte el receptor a un puerto USB del ordenador. Pasado un rato, aparece un mensaje indicando que no se pudo instalar el dispositivo:

Vaya al menú Inicio y seleccione Equipo->Propiedades:

![](../assets/images/image485.webp){ width="330" loading=lazy }

En la ventana que aparece, seleccione *Administrador de dispositivos*:

![](../assets/images/image486.webp){ width="360" loading=lazy }

En la ventana del Administrador de dispositivos, expanda el nodo Controladoras de bus serie universal:

![](../assets/images/image487.webp){ width="364" loading=lazy }

Seleccione el nodo que indica un error, haga clic con el botón derecho y seleccione Actualizar software de controlador en el menú:

![](../assets/images/image488.webp){ width="365" loading=lazy }

En el asistente, seleccione “Buscar software de controlador en el equipo”:

![](../assets/images/image489.webp){ width="362" loading=lazy }

En la siguiente pantalla, seleccione ‘Permitirme elegir…’ y seleccione Siguiente:

![](../assets/images/image490.webp){ width="397" loading=lazy }

En la siguiente pantalla, seleccione “Dispositivo de entrada USB” y pulse Siguiente:

El receptor Buzz™ ya está instalado correctamente y listo para usar.

![](../assets/images/image491.webp){ width="317" loading=lazy }

Cierre la ventana; en el Administrador de dispositivos, el receptor inalámbrico de pulsadores aparecerá ahora como “Dispositivo de entrada USB”.

![](../assets/images/image492.webp){ width="317" loading=lazy }

Para localizar el dispositivo de pulsadores *después* de instalarlo, por ejemplo para desinstalarlo, deberá abrir las propiedades de cada una de las entradas *Dispositivo de entrada USB* (clic con el botón derecho; Propiedades)

![](../assets/images/image493.webp){ width="291" loading=lazy }

A continuación, en la ventana *Propiedades de Dispositivo de entrada USB*, seleccione la pestaña ‘Detalles’ y cambie la lista desplegable ‘Propiedad’ a *Descripción del dispositivo notificada por el bus*. Si el campo ‘Valor’ muestra el texto *Logitech Trebek(tm) controllerV1*, ha encontrado el dispositivo de pulsadores Sony.

![](../assets/images/image494.webp){ width="289" loading=lazy }
