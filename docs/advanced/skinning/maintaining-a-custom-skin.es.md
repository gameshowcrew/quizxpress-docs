# Compartir, actualizar y solucionar problemas de un skin personalizado

## Compartir un skin con otro equipo

Un skin personalizado completo consta de dos cosas, ambas en la carpeta de datos `%appdata%\QuizXpress`:

- `skin.config`
- la carpeta `Skins\<su skin>` con sus imágenes

Copie ambos en la carpeta de datos del otro equipo y seleccione allí el skin en Quiz Setup. Si utilizó el `dir="Skins\<su skin>"` relativo, tal como se describe en [Crear un skin personalizado](creating-a-custom-skin.md#paso-4-anada-la-definicion-de-su-skin), no es necesario cambiar nada. Las fuentes que utiliza el skin también deben estar instaladas en el otro equipo.

## Después de una actualización de QuizXpress

Una actualización sustituye el `skin.config` instalado, pero nunca toca su copia ni la carpeta de su skin, por lo que su skin sigue funcionando. Sin embargo, como un skin 'User.' lee solo su copia, los skins integrados de los que hereda permanecen tal como estaban cuando hizo la copia. Los nuevos ajustes y mejoras que una actualización añade a los skins integrados no los recoge su skin.

Para poner su skin al día después de una actualización:

1. Copie su elemento `<skin>…</skin>` de su `skin.config` en un lugar seguro, por ejemplo un archivo de texto junto a él.
2. Copie el nuevo `skin.config` de la carpeta de instalación en la carpeta de datos, sustituyendo su copia.
3. Pegue de nuevo su elemento `<skin>` justo encima de `</skins>` (y vuelva a añadir `hidden="true"` a los skins integrados si lo utilizaba).

La carpeta de su skin con las imágenes no necesita cambios.

## Solución de problemas

| Síntoma | Causa y solución |
|---|---|
| Mi skin no aparece en Quiz Setup. | Compruebe que editó la copia de `%appdata%\QuizXpress` (no el archivo instalado), que está guardada, que su skin no tiene `hidden="true"` y que reinició Quiz Setup. |
| QuizXpress Live muestra un error sobre el archivo del skin y no se inicia. | El mensaje indica qué ocurre. Causas habituales: un error de XML (unas comillas o un `/>` que faltan, un `&` que debería escribirse como `&amp;`), un 'parent' que no coincide con el 'name' de un skin existente o un valor no válido (para los atributos con un conjunto fijo de valores, el mensaje enumera los valores permitidos). Corrija el archivo e inicie de nuevo. |
| Mi skin está seleccionado, pero el quiz tiene el aspecto de un skin integrado. | Los skins personalizados no están disponibles en la edición Home. Si no es el caso, compruebe que no cambió el 'name' de su skin después de seleccionarlo en Quiz Setup; si lo hizo, selecciónelo de nuevo. |
| Un ajuste no tiene efecto. | Compruebe la ortografía de los nombres de elementos y atributos comparándolos con el skin raíz (distinguen mayúsculas de minúsculas) y compruebe que el elemento está dentro de su elemento `<skin>`. Reinicie el quiz después de guardar. |
| Mi imagen no se muestra. | No se encontró el archivo o no se pudo leer. Compruebe el nombre del archivo (incluida la extensión) y el 'dir' de su skin. El error se escribe en el archivo de registro de QuizXpress como "Skin image … not found, please check skin.config". |
