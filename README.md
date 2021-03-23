# noovo

Triple analyse de données pour un article dans [*La Conversation*](). J'y examine le contexte dans lequel est apparu [**Noovo.info**](), service d'information de la chaîne télé généraliste appartenant à Bell Media, le 29 mars 2021.

### Étape 1 - Données d'écoute télé

[J'avais déjà analysé l'évolution de l'écoute de l'information dans la télévision québécoise au début de la dernière décennie](http://jhroy.ca/2014/09/cotes-ecoute-info-pire/). Il s'agissait de faire une mise à jour en allant d'abord chercher des données chez Numeris, l'organisme qui calcule les auditoires radio et télé depuis plus de trois quarts de siècle. Parmi les données librement accessibles, il y a le [palmarès des 30 émissions les plus écoutées chaque semaine au Québec francophone](https://fr.numeris.ca/media-and-events/tv-weekly-top-30). Chaque semaine tient dans un document PDF.

Il fallait donc aller chercher tous les fichiers que je n'avais pas déjà moissonnés en 2014. Comme le site de Numeris est conçu pour compliquer la vie des moissonneurs de données, j'ai commencé par copier-coller le HTML qui contient les URL vers tous les documents PDF contenant les palmarès hebdomadaires d'écoute&nbsp;:[**numeris.html**](numeris.html)

Ce court script ([**pfds.py**](pfds.py)) permettait ensuite de recueillir les URL de tous les documents

### Étape 2 - Données de Facebook et d'Instagram
