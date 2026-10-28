# Analizar los resultados de un quiz con QuizXpress Analyzer

QuizXpress incluye una herramienta de análisis gráfico llamada Analyzer. Analyzer le ayuda a comprender y visualizar los datos recopilados durante el quiz. Puede abrir varios conjuntos de datos, lo que permite comparar los datos recopilados a lo largo del tiempo. Hay tres vistas disponibles:

- Question view

- Team view

- Demographic Groups (si había grupos demográficos durante un quiz)

La vista centrada en las preguntas tiene este aspecto:

![](../assets/images/image471.webp){ width="604" loading=lazy }

1)  La lista de todas las preguntas del conjunto de datos

2)  La pregunta en sí con las posibles respuestas (si el archivo de quiz .qx está disponible en el sistema, se muestra una imagen de la diapositiva; si ya no está disponible, solo verá una representación textual)

3)  Las respuestas y las puntuaciones (de la pregunta seleccionada) por equipo/jugador. Cuando hay grupos demográficos disponibles, se muestra una pestaña ‘Demographic Groups’ en la parte inferior derecha. En esta pestaña se muestra, en una tabla, el número de votos por respuesta de la pregunta seleccionada para cada grupo.

4)  Un gráfico circular que muestra la distribución de las respuestas de la pregunta seleccionada. Cuando hay grupos demográficos disponibles, en la pestaña Demographic Groups se puede mostrar la distribución de respuestas de un grupo seleccionándolo en el cuadro de lista situado encima del gráfico de distribución de respuestas.

La vista por equipos tiene la siguiente disposición:

![](../assets/images/image472.webp){ width="547" loading=lazy }

1)  La lista de nombres de equipos/jugadores. Tenga en cuenta que aquí puede seleccionar varios equipos.

2)  Un gráfico que muestra la evolución de la puntuación a lo largo del tiempo

3)  Las preguntas y respuestas del equipo o equipos seleccionados

La vista de grupos demográficos tiene la misma disposición. En la tabla se muestran, para cada pregunta, todas las respuestas. Para cada grupo seleccionado se muestra el número de votos de cada respuesta. También se muestra la evolución de la puntuación a lo largo del tiempo del grupo o grupos seleccionados.

Todos los datos que muestra Analyzer son almacenados durante un quiz por QuizXpress Live en forma de documentos XML en la carpeta de datos de la aplicación QuizXpress (en Windows 7, la ubicación de esta carpeta es ‘C:\Users\\username>\AppData\Roaming\QuizXpress\Scores’). Tenga en cuenta que puede abrir esta carpeta desde QuizXpress Studio en el menú Tools->Advanced.
