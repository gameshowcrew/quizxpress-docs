# Assistants IA

Quiz Studio peut être piloté par un assistant IA tel que [Claude](https://claude.ai). Vous dites à l'assistant quel quiz vous souhaitez (« crée une manche de quiz de bar sur les années 90 avec 10 questions à choix multiples et une manche d'images »), et il ouvre, construit, modifie et enregistre le quiz dans votre fenêtre Quiz Studio pendant que vous regardez. Tout ce qu'il fait se passe dans le Quiz Studio que vous avez ouvert : vous pouvez donc examiner le résultat, le modifier vous-même et continuer.

C'est différent du [AI Quiz Generator](../../studio/quizxpress-and-ai.md), une partie de Studio qui génère des questions pour vous. Avec un assistant IA, vous travaillez en conversation, et l'assistant peut faire presque tout ce que vous pouvez faire dans Studio : créer tous les types de diapositives, modifier les textes, les réponses, les points, les styles et les arrière-plans, ajouter des mini-jeux, vérifier les erreurs du quiz et l'enregistrer.

## Comment ça marche

La connexion utilise un standard appelé MCP (Model Context Protocol), qui permet aux assistants IA d'utiliser d'autres programmes. Quiz Studio intègre un petit serveur MCP :

- Il est **désactivé** tant que vous ne l'activez pas dans les Options, voir [Connecter un assistant IA](connecting-an-ai-assistant.md).
- Il n'accepte que les connexions de **programmes sur votre propre ordinateur**. Personne sur le réseau ou sur Internet ne peut l'utiliser.
- Vous avez besoin d'un assistant IA qui prend en charge MCP, par exemple Claude Code. L'assistant est un produit distinct avec son propre abonnement : il ne fait pas partie de QuizXpress et n'utilise pas vos crédits IA QuizXpress.

Tant qu'un assistant est connecté, une barre sous le ruban vous l'indique.

## Bon à savoir

!!! warning "Les modifications ne peuvent pas être annulées"
    Les modifications de l'assistant ne peuvent pas être annulées avec Undo, et Quiz Studio efface l'historique d'annulation après chacune d'elles. Enregistrez votre quiz sous un autre nom avant de laisser un assistant effectuer de grosses modifications, afin de pouvoir toujours revenir en arrière.

- L'assistant n'ouvrira, ne créera ni ne fermera un quiz tant que le quiz dans Studio contient des modifications non enregistrées. Il doit d'abord vous demander : enregistrer le quiz, ou lui dire d'abandonner les modifications.
- Tant qu'une boîte de dialogue est ouverte dans Studio (par exemple les Options), l'assistant doit attendre. Fermez la boîte de dialogue et il pourra continuer.
- Chaque fois que l'assistant ajoute une diapositive, Studio l'affiche et fait défiler les miniatures jusqu'à elle.
- Cela ne concerne que Quiz Studio. Quiz Live, Director et Setup ne peuvent pas être pilotés par un assistant.

## Dans cette section

- [Connecter un assistant IA](connecting-an-ai-assistant.md) : l'activer et connecter votre assistant.
- [Utiliser Claude Desktop](claude-desktop.md) : configurer l'application Claude pour Windows, y compris dans Parallels sur un Mac.
- [Ce que peut faire un assistant](what-an-assistant-can-do.md) : les possibilités, avec des exemples de demandes.
