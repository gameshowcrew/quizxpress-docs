# Partager, mettre à jour et dépanner un skin personnalisé

## Partager un skin avec un autre ordinateur

Un skin personnalisé complet se compose de deux éléments, tous deux situés dans le dossier de données `%appdata%\QuizXpress` :

- `skin.config`
- le dossier `Skins\<your skin>` avec ses images

Copiez les deux dans le dossier de données de l'autre ordinateur et sélectionnez-y le skin dans Quiz Setup. Si vous avez utilisé le `dir="Skins\<your skin>"` relatif comme décrit dans [Créer un skin personnalisé](creating-a-custom-skin.md#etape-4-ajouter-la-definition-de-votre-skin), rien ne doit être modifié. Les polices utilisées par le skin doivent également être installées sur l'autre ordinateur.

## Après une mise à jour de QuizXpress

Une mise à jour remplace le `skin.config` installé, mais ne touche jamais à votre copie ni au dossier de votre skin ; votre skin continue donc de fonctionner. Toutefois, comme un skin 'User.' lit uniquement votre copie, les skins intégrés dont il hérite restent tels qu'ils étaient au moment où vous avez fait la copie. Les nouveaux paramètres et améliorations qu'une mise à jour apporte aux skins intégrés ne sont pas pris en compte par votre skin.

Pour mettre votre skin à jour après une mise à jour :

1. Copiez votre élément `<skin>…</skin>` depuis votre `skin.config` vers un endroit sûr, par exemple un fichier texte à côté.
2. Copiez le nouveau `skin.config` du dossier d'installation vers le dossier de données, en remplaçant votre copie.
3. Collez de nouveau votre élément `<skin>` juste au-dessus de `</skins>` (et ajoutez à nouveau `hidden="true"` aux skins intégrés si vous l'aviez fait).

Le dossier de votre skin contenant les images n'a pas besoin d'être modifié.

## Dépannage

| Symptôme | Cause et solution |
|---|---|
| Mon skin n'apparaît pas dans Quiz Setup. | Vérifiez que vous avez modifié la copie dans `%appdata%\QuizXpress` (et non le fichier installé), qu'elle est enregistrée, que votre skin n'a pas `hidden="true"` et que vous avez redémarré Quiz Setup. |
| QuizXpress Live affiche une erreur concernant le fichier de skin et ne démarre pas. | Le message indique ce qui ne va pas. Causes courantes : une erreur XML (un guillemet ou un `/>` manquant, un `&` qui devrait être écrit `&amp;`), un 'parent' qui ne correspond pas au 'name' d'un skin existant, ou une valeur non valide (pour les attributs à ensemble de valeurs fixe, le message indique les valeurs autorisées). Corrigez le fichier et relancez. |
| Mon skin est sélectionné, mais le quiz ressemble à un skin intégré. | Les skins personnalisés ne sont pas disponibles dans l'édition Home. Sinon, vérifiez que vous n'avez pas modifié le 'name' de votre skin après l'avoir sélectionné dans Quiz Setup ; si c'est le cas, sélectionnez-le à nouveau. |
| Un paramètre n'a aucun effet. | Vérifiez l'orthographe des noms d'éléments et d'attributs par rapport au skin racine (ils sont sensibles à la casse) et vérifiez que l'élément se trouve bien dans votre élément `<skin>`. Redémarrez le quiz après l'enregistrement. |
| Mon image ne s'affiche pas. | Le fichier est introuvable ou illisible. Vérifiez le nom du fichier (y compris l'extension) et le 'dir' de votre skin. L'erreur est écrite dans le fichier journal de QuizXpress sous la forme "Skin image … not found, please check skin.config". |
