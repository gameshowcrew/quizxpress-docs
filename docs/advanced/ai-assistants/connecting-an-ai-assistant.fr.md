# Connecter un assistant IA

## L'activer

1. Dans Quiz Studio, allez dans HOME → Options et ouvrez l'onglet 'AI Completion'.
2. Sous 'AI assistants (MCP)', cochez 'Allow AI assistants to control Quiz Studio' et cliquez sur OK.

La page affiche l'adresse à laquelle un assistant doit se connecter : `http://127.0.0.1:8766/mcp`. Le réglage est mémorisé : il reste donc activé au prochain démarrage de Studio. Décochez la case pour le désactiver à nouveau.

## Connecter votre assistant

Ajoutez Quiz Studio comme serveur MCP dans votre assistant IA, en utilisant l'adresse ci-dessus et le transport HTTP. La procédure dépend de l'assistant. Pour Claude Code, exécutez cette commande une seule fois dans une invite de commandes :

```
claude mcp add --transport http quizstudio http://127.0.0.1:8766/mcp
```

Les autres assistants qui prennent en charge les serveurs MCP via HTTP disposent d'un réglage similaire où vous saisissez un nom et l'adresse.

Quiz Studio doit être en cours d'exécution pendant que l'assistant travaille. Lancez la conversation comme d'habitude, par exemple : « Ouvre mon quiz 'Friday night.qx' dans Quiz Studio et montre-moi un aperçu des diapositives. »

## Ce que vous voyez dans Studio

Dès que l'assistant se connecte, une barre apparaît sous le ruban : 'An AI assistant is connected to Quiz Studio. Changes it makes cannot be undone with Undo.' Cliquez sur 'Turn off' dans la barre pour déconnecter l'assistant et désactiver à nouveau le réglage. Cliquez sur la croix pour masquer la barre.

## L'utiliser pour une seule session

Si vous ne souhaitez pas activer le réglage de façon permanente, démarrez Quiz Studio avec l'option `-mcp`. L'assistant peut se connecter pendant cette session, et le réglage reste désactivé. Quiz Studio ignore aussi l'écran d'accueil, ce qui permet de le lancer depuis un script ou de le faire démarrer par un assistant. Vous pouvez ajouter le quiz à ouvrir :

```
"Quiz Studio.exe" -mcp "C:\Quizzes\Friday night.qx"
```

Pour utiliser un autre port, par exemple lorsque vous exécutez deux copies de Studio, ajoutez le port : `-mcp:8800`. L'adresse devient alors `http://127.0.0.1:8800/mcp`.

## Dépannage

**La barre indique 'AI assistants cannot connect: port 8766 is already in use'.** Un autre programme, ou une autre copie de Quiz Studio, utilise le port. Fermez l'autre copie, ou démarrez Studio avec `-mcp:` suivi d'un autre numéro de port.

**L'assistant indique que Quiz Studio ne répond pas ou affiche une boîte de dialogue.** Quiz Studio ne peut pas recevoir de commandes tant qu'une boîte de dialogue est ouverte. Fermez la boîte de dialogue (par exemple Options ou une question 'Save changes?') et demandez à l'assistant de réessayer.

**L'assistant n'arrive pas du tout à se connecter.** Vérifiez que l'option est cochée, que Quiz Studio est en cours d'exécution, et que l'adresse saisie dans l'assistant est exactement celle affichée dans les Options. Vous n'avez rien à modifier dans le pare-feu Windows : la connexion reste sur votre propre ordinateur.
