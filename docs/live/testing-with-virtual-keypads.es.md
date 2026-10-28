# Pruebas con mandos virtuales

El mando virtual (Virtual Keypad) es útil para probar su quiz sin ninguna dependencia externa. Es un mando de software que se ejecuta en el mismo equipo que su quiz. Puede iniciar un nuevo mando virtual (VK) desde el menú desplegable External Tools de Studio o desde el menú Inicio de Windows, en la sección QuizXpress. Una vez que una instancia del mando virtual está en ejecución, empieza a intentar conectarse a QuizXpress Live. Hasta que lo consigue, los botones del mando aparecen atenuados.

| ![](../assets/images/image398.webp){ width="107" loading=lazy } | ![](../assets/images/image399.webp){ width="105" loading=lazy } | ![](../assets/images/image400.webp){ width="290" loading=lazy } |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Conectando                                                                      | Conectado                                                                       | Menú contextual del mando virtual                                              |

Una vez conectado, puede cambiar el número del mando sobre la marcha con el selector numérico. Para acceder al menú contextual, haga clic con el botón derecho en la pantalla del mando. El menú contextual ofrece los siguientes comandos:

| Menú          | Descripción                                                                              |
|---------------|------------------------------------------------------------------------------------------|
| Properties    | Abre el cuadro de diálogo Properties, donde puede ver la dirección IP y el puerto del servidor que se están utilizando |
| Clone         | Clona una nueva instancia. El ID del mando se incrementa                                 |
| Always on Top | Mantiene el mando por delante de todas las demás aplicaciones                            |
| Randomizer    | Activa/desactiva un modo en el que el mando envía entradas aleatorias para facilitar las pruebas |
| Exit          | Cierra el mando virtual                                                                  |
