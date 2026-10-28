# Utiliser Claude Desktop

[Claude Desktop](https://claude.ai/download) est l'application Claude pour Windows et Mac. Elle peut piloter Quiz Studio comme Claude Code, mais elle se connecte d'une autre manière : par un petit programme passerelle appelé `mcp-remote`. Cette page explique comment la configurer, y compris lorsque vous utilisez QuizXpress dans Parallels sur un Mac.

Avant de commencer, activez le réglage des assistants IA dans Quiz Studio, comme décrit dans [Connecter un assistant IA](connecting-an-ai-assistant.md).

## Ce dont vous avez besoin

- **Claude Desktop pour Windows**, installé sur le même ordinateur que Quiz Studio. Il existe aussi une version pour Windows sur ARM.
- **Node.js** (la version LTS sur [nodejs.org](https://nodejs.org)). Le programme passerelle fonctionne avec lui. Pour vérifier qu'il est installé, ouvrez une invite de commandes et tapez `node --version` : un numéro de version doit s'afficher.

!!! note
    N'ajoutez pas Quiz Studio sous 'Settings' → 'Connectors' dans Claude. Ces connecteurs se connectent depuis les serveurs d'Anthropic sur Internet, alors que Quiz Studio n'accepte que les connexions de votre propre ordinateur.

## Ajouter Quiz Studio à Claude Desktop

1. Dans Claude Desktop, allez dans 'Settings' → 'Developer' et cliquez sur 'Edit Config'. Le fichier de configuration `claude_desktop_config.json` s'ouvre.
2. Fermez complètement Claude Desktop. Fermer la fenêtre ne suffit pas : ouvrez le Gestionnaire des tâches, sélectionnez Claude et cliquez sur 'Fin de tâche'. Si Claude est encore en cours d'exécution pendant que vous modifiez le fichier, il peut écraser vos modifications.
3. Ouvrez le fichier dans le Bloc-notes et ajoutez ce bloc juste après la première `{` :

   ```json
     "mcpServers": {
       "quizstudio": {
         "command": "cmd",
         "args": ["/c", "npx", "-y", "mcp-remote", "http://127.0.0.1:8766/mcp"]
       }
     },
   ```

   Laissez le reste du fichier tel quel et enregistrez-le.
4. Démarrez Quiz Studio, puis redémarrez Claude Desktop.
5. Dans 'Settings' → 'Developer', vérifiez que `quizstudio` est indiqué comme en cours d'exécution. La première fois, cela peut prendre environ une minute, le temps de télécharger le programme passerelle.

Lancez maintenant une conversation comme d'habitude, par exemple : « Montre-moi un aperçu des diapositives du quiz ouvert dans Quiz Studio. »

!!! tip
    Utilisez exactement la forme ci-dessus, avec `cmd` et `/c`. Sous Windows, Claude Desktop ne trouve pas toujours `npx` lorsqu'il le lance directement.

## QuizXpress dans Parallels sur un Mac

Quiz Studio n'accepte que les connexions de l'ordinateur sur lequel il tourne. Lorsque QuizXpress tourne sous Windows dans Parallels, le Mac compte comme un autre ordinateur : Claude sur le Mac ne peut donc pas atteindre Quiz Studio.

Installez Claude Desktop **dans Windows**, dans la même machine virtuelle que QuizXpress, et configurez-le comme décrit ci-dessus. Votre compte Claude et vos conversations sont les mêmes que sur le Mac.

## Utiliser l'onglet Code de Claude Desktop

Claude Desktop dispose aussi d'un onglet 'Code', qui exécute Claude Code. Il n'utilise pas `claude_desktop_config.json` : il lit le fichier `.mcp.json` du dossier dans lequel vous travaillez et se connecte directement, sans le programme passerelle :

```json
{
  "mcpServers": {
    "quizstudio": {
      "type": "http",
      "url": "http://127.0.0.1:8766/mcp"
    }
  }
}
```

Claude Code vous demande d'approuver le serveur avant de l'utiliser. Après avoir modifié le fichier, ouvrez une nouvelle session dans l'onglet Code : une session déjà ouverte ne voit pas le serveur.

## Dépannage

**`quizstudio` n'apparaît pas dans 'Settings' → 'Developer', ou vos modifications du fichier ont disparu.** Claude Desktop était encore en cours d'exécution pendant que vous modifiiez le fichier. Fermez-le dans le Gestionnaire des tâches, refaites la modification et démarrez Claude.

**`quizstudio` reste au démarrage, ou affiche une erreur.** Vérifiez que Node.js est installé (`node --version`), que Quiz Studio est en cours d'exécution et que l'option des assistants IA est cochée dans les options de Quiz Studio. Fermez ensuite Claude Desktop dans le Gestionnaire des tâches et redémarrez-le.

**Claude sur le Mac n'arrive pas à se connecter à Quiz Studio dans Parallels.** C'est normal : utilisez Claude Desktop dans Windows, voir [QuizXpress dans Parallels sur un Mac](#quizxpress-dans-parallels-sur-un-mac).
