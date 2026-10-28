# Enrutamiento de diapositivas

Normalmente, un quiz se desarrolla de forma lineal desde la diapositiva 1 hasta el final. Con el enrutamiento de diapositivas, puede definir distintas ‘rutas’ en sus quizzes. Las rutas pueden ser estáticas (por ejemplo, la diapositiva 10 siempre seguida de la diapositiva 20) o dinámicas, según el resultado de una diapositiva de votación. Con la opción dinámica, puede hacer que sus jugadores decidan adónde ir a continuación según sus votos, por ejemplo, haciéndoles elegir un videoclip o una canción que reproducir, o a qué ronda de preguntas ir.

Un visor integrado ayuda a visualizar el flujo de diapositivas.

Usted define una ruta asignando un Id a la diapositiva a la que desea saltar, en las propiedades de la diapositiva. Puede ser un nombre arbitrario pero único que tenga sentido para usted como autor del quiz:

![](../../assets/images/image281.webp){ loading=lazy }

Después, haga referencia a este Id en la propiedad ‘Next slide’ de la respuesta o imagen de una diapositiva Audience Response/Majority Rules:

![](../../assets/images/image282.webp){ loading=lazy }

El ejemplo anterior muestra una diapositiva Audience Response con 4 imágenes. Cuando la opción A (Paris) obtiene más votos, el sistema salta a la diapositiva con el Id ‘Paris’.

Por supuesto, puede ocurrir que haya un empate en la votación, cuando dos o más respuestas tienen el mismo número de votos. El comportamiento en esa situación se puede definir en las propiedades de la diapositiva (cuando el enrutamiento está activo en ella) con la propiedad ‘Next slide tie mode’. Hay tres opciones:

- Re-vote, la diapositiva se vuelve a cargar y la votación se repite hasta que una respuesta obtiene la mayoría

- Randomize, el sistema elige al azar la ruta de cualquiera de las respuestas más votadas

- Prompt, se presenta un aviso al presentador (en la pantalla principal) para que haga una selección

Cada diapositiva tiene también una propiedad ‘Next slide’ que define la siguiente diapositiva que presentará el sistema. Si se deja vacía, se sigue el flujo predeterminado (pasar a la siguiente diapositiva en orden).

Para saltar a una diapositiva distinta de la siguiente en orden predeterminada, rellene la propiedad ‘Next slide’ de la propia diapositiva. Un ejemplo es cuando se encuentra al final de una ronda y quiere volver a una diapositiva de selección de ronda. Aplicando esto al ejemplo anterior, la última diapositiva de la ronda de Paris puede remitir de nuevo a la diapositiva de votación.

![](../../assets/images/image283.webp){ width="298" loading=lazy } ![](../../assets/images/image284.webp){ width="271" loading=lazy }
