# Personalizar la imagen del sitio web buzzerpad

Hay tres maneras de crear una apariencia personalizada del sitio web buzzerpad de QuizXpress:

1)  Podemos comprar un dominio personalizado para usted y crear una versión con su marca detrás de ese dominio. Póngase en contacto con nosotros en info@gameshowcrew.com para obtener detalles y precios.

2)  Puede pasar parámetros en la URL para personalizar la apariencia y enlazar a ella desde su propio sitio web (no conviene que sus clientes tengan que trabajar con el enlace largo) o utilizar un sitio web como https://tinyurl.com/ para ocultar los parámetros de la URL. Si muestra un código QR en pantalla (pulse Q cuando el quiz se esté ejecutando en el reproductor de quiz) para que los jugadores accedan fácilmente al pulsador web, puede indicar los parámetros de personalización del código QR en QuizXpress Director. En la pestaña Mobile, pulse Settings y, en el cuadro de diálogo de configuración que aparece, introduzca los parámetros en el campo URL Extension. Consulte el apartado 5.7.8.3 para obtener más información.

3)  Incruste el sitio web buzzerpad en un iFrame y pase los parámetros desde el iFrame

> de referencia. Esto también le permite añadir su emisión en directo (como YouTube) en la misma
>
> página. Si necesita más información al respecto, no dude en ponerse en contacto con nosotros en info@gameshowcrew.com.

Personalización con parámetros de URL

Puede pasar varios parámetros al sitio web buzzerpad para personalizar su apariencia según sus necesidades. Los parámetros son:

| **Nombre**  | **Descripción**                                                                                           | **Ejemplo**                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| name        | Pasa el nombre del jugador                                                                                | name=John                                                   |
| fname       | Pasa el nombre del jugador y hace que el campo de entrada sea de solo lectura                             | fname=Peter                                                 |
| themecolor  | El color principal del sitio                                                                              | themecolor=FE5602                                           |
| about       | El texto “acerca de” que se muestra en la página de inicio de sesión (asegúrese de utilizar el escape HTML para el carácter de espacio, etc.) | about=About%20QuizXpress                                    |
| abouturl    | La URL a la que debe enlazar el texto “acerca de”                                                         | abouturl=https://www.quizxpress.com                         |
| gotext      | El texto del botón GO                                                                                     | gotext=ENTER (nota: asegúrese de codificar correctamente la cadena) |
| compact     | Pase 1 para que el diseño de la pantalla de inicio de sesión sea más compacto                             | compact=1                                                   |
| logo        | URL de su propio logotipo. Asegúrese de que el logotipo tenga 120 píxeles de alto y un fondo transparente | logo=https://www.quizxpress.com/logo.png                    |
| pin         | Pase el código PIN para que el jugador no tenga que introducirlo                                          | pin=12345                                                   |
| ticket      | Pase el código de la entrada                                                                              | ticket=AG1234F                                              |
| uid         | Pase una identidad de usuario fija como GUID (el formato hexadecimal es XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX) | uid=aed6373a-db53-499d-9428-a7ad22289272                    |
| autoconnect | Al pasar *fname*, *pin* y *autoconnect*=1, el mando iniciará sesión automáticamente                       | pin=12345&fname=Player1&autoconnect=1                       |

Por ejemplo:

[https://buzzerpad.eu/?compact=1&logo=https://quizxpress.com/files/quiztime.png&themecolor=E46C0A&about=About%20Quiz%20Time](https://buzzerpad.eu/?compact=1&logo=https://quizxpress.com/files/quiztime.png&themecolor=E46C0A&about=About%20Quiz%20Time%20)

Tendrá el siguiente aspecto:

![](../../assets/images/image397.webp){ width="286" loading=lazy }

La imagen del logotipo ‘quiz time’ se cargó en el sitio web quizxpress.com para poder utilizarla como logotipo personalizado. Su logotipo debe estar almacenado en algún lugar de su propio sitio web.
