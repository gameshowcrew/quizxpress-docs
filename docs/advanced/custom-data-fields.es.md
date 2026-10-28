# Campos de datos personalizados

Ahora puede definir su propio diccionario de datos en un quiz y almacenar datos arbitrarios junto con las diapositivas del quiz. Al interactuar con QuizXpress, los datos pueden recuperarse mediante el canal TCP (comandos getslide o getquiz) y pueden utilizarse para controlar lógica externa, como efectos de luz, efectos de sonido, hardware personalizado u otras funcionalidades. Esta lógica residiría en una capa de integración alrededor de QuizXpress que se comunica con QX mediante el canal TCP de entrada de MessageBroker.

Usted define los campos personalizados en su quiz en el cuadro de diálogo File->Options, pestaña Metadata:

![](../assets/images/image478.webp){ width="271" loading=lazy }

Aquí puede añadir campos de tipo: string, int o float

![](../assets/images/image479.webp){ width="462" loading=lazy }

Cuando los campos están definidos, aparecen en la cuadrícula de propiedades de cada diapositiva:

![](../assets/images/image480.webp){ width="235" loading=lazy }

La capa de integración puede recuperar los datos de la diapositiva actual para obtener los campos personalizados:

![](../assets/images/image481.webp){ width="485" loading=lazy }

El comando getslide devuelve los datos de una sola diapositiva en formato XML legible por personas. También puede usar getquiz para obtener los datos de todas las diapositivas en una sola llamada.
