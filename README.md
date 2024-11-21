# Referentiel des Tunnels
Ce **repository** met à disposition des tables de référence sur les dénominations et les codes des tunnels, de leurs parties ou de leurs regroupements.

Ce **repository** fournit notamment la table qui définit les regroupements de sections de tunnels en **fermetures**, pour les visites des issues et des niches.

## Références
`https://github.com/OlivierNalin/CombienTunnels`   
Compte rendu d'un exercice qui propose une classification à 3 niveaux des *tubes* et des tunnels.  

## Constats
Plusieurs applications de la DiRIF (SAGTu, SIRIUS, Sumcombe, CosWin) utilisent des noms et des codes différents pour identifier les tunnels.

Les applications n'utilisent pas toutes les mêmes objets ou les mêmes regroupements de tubes pour identifier les tunnels.
Par exemple, dans Sucombe, la table des prestations comporte le champ **Lieu** qui prend la valeur **Thiais**, mais Sucombe ne connait pas d'objet correspondant au **tunnel du moulin**.

## Sucombe
La table des prestations de application Sucombe comporte un champ **Lieu** dont 21 valeurs correspondent à un tunnel ou à un groupe de tunnels.   
La liste de ces valeurs est la suivante :   
'Ambroise PARE', 'Antony', 'Bellerive', 'Bicêtre', 'Bobigny-Lumen-Norton', 'Boissy-Saint-Léger', 'Champigny', 'Chennevières', 'Fontenay le Fleury', 'Fresnes', 
'Italie', 'La Courneuve', 'Landy', 'Nanterre / La Défense', 'Neuilly', 'Nogent', 'Orly', 'Saint Cloud', 'Sévines', 'Taverny', 'Thiais'

## CosWin
Dans l'application CosWin, certains équipements sont associés à un **tunnel**. 
La table des équipements comporte un champ **tunnel** (26 valeurs différentes) :   
'AMBROISE_PARE', 'ANTONY', 'BELLE-RIVE', 'BICETRE', 'BOBIGNY', 'BOISSY',
       'CHAMPIGNY', 'CHENNEVIERES', 'ECHANGEUR_NANTERRE', 'FONTENAY',       'FRESNES', 'GUY-MOQUET', 'ITALIE', 'LANDY', 'LA_COURNEUVE',
       'LA_DEFENSE', 'LUMEN_NORTON', 'MOULIN', 'NANTERRE_CENTRE', 'NEUILLY', 'NOGENT', 'ORLY', 'SAINT-CLOUD', 'SEVINES', 'TAVERNY', 'TRINITY'

Pour ces équipements, CosWin renseigne également le champ **Axe**. Les valeurs prises par ce champs sont :'A1', 'A115', 'A12', 'A13', 'A14', 'A14XA86', 'A4', 'A6B', 'A86EST',
       'A86NORD', 'A86OUEST', 'A86SUD', 'N1013', 'N1014', 'N12', 'N13', 'N19', 'N192', 'N314', 'N315', 'N7'   
Elles complètent parfois utilement l'information donnée par le champ Tunnel (N1013 ou N192 désignent des bretelles dans le *tunnel* **LA_DEFENSE**).
   
**cosWin** fournit également le champ **sens** : 'E', 'E>W', 'E>Y', 'I', 'I>W', 'W', 'W>I', 'Y', 'Y>E', 'Y>I'

Cette information est particulièrement utile dans le cas du *tunnel* désigné par **ECHANGEUR_NANTERRE**.

Quand on croise ces 3 variables, on obtient 74 possibilités :   
[Table Tunnel x Axe x Sens (Téléchargement 7k)](https://github.com/ExploitIdF/ReferentielTunnels/blob/main/tunnelAxeSens.xlsx)

On constate que certains croisements ne concernent qu'un seul équipement. 
Il peut parfois s'agir d'une anomalie de l'enregistrement dans CosWin :    
['Table des équipements singuliers '](https://github.com/ExploitIdF/ReferentielTunnels/blob/main/equipMalLocalisé.csv)

## Correspondance entre CosWin et Sucombe
Dans Sucombe, 3 lieux sont des regroupements de plusieurs tunnels au sens de CosWin :   
* 'Bobigny-Lumen-Norton',
* 'Nanterre / La Défense',
* 'Thiais'

En outre, même quand les objets sont les mêmes, leurs écritures diffèrent : 
* 'Saint Cloud' / 'SAINT-CLOUD',
* 'Bellerive' / 'BELLE-RIVE',
* 'Ambroise PARE' / 'AMBROISE_PARE',
* ...

On pourra utiliser, pour lier les informations des deux applications, la table de correspondante téléchargeable ici :  
['Table de correspondance CosWin -> Sucombe](https://raw.githubusercontent.com/ExploitIdF/ReferentielTunnels/refs/heads/main/tunnelsCosWinSucombe.csv)

['Code python utilisé pour établir la table'](https://github.com/ExploitIdF/ReferentielTunnels/blob/main/codeCorrCosWinSucombe)

## Regroupements de fermetures
Pour massifier certaines actions de maintenance de nuit, sous fermeture, il est utile d'identifier les sections de tunnels 
qui sont le plus souvent fermées en même temps.   
Environ 30 regroupements de sections de ce type ont été identifiés, en concertation avec les PCTT.

Certaines associations vont de soi comme : 

* Moulin et G. Moquet (Thais),
* Boulogne A. Paré et Saint Cloud (A13).    

D'autres regroupements sont le résultat d'un choix réfléchi, tels que :
* Bobigny Lumen Norton & La Courneuve
* Les deux sens des tunnels des Sévines, de Chennevières, de Taverny
* La Défense (A14-Y) & B5 (ECH W>I)

Cependant, les tunnels de Belle Rive et de Nanterre, qui sont généralement fermés ensemble, n'ont pas été regroupés, 
car ils ne sont pas gérés par le même pôle de maintenance.

Les regroupements sont formalisés dans la table accessible par le lien ci-dessous :   
[Correspondance entre Fermetures & couples (Tunnel, Sens)](https://raw.githubusercontent.com/ExploitIdF/ReferentielTunnels/refs/heads/main/CorTbFerm.csv)

A partir de la table des équipements de CosWin, on peut faire une jointure avec cette table sur les champs Tunnel et Sens, 
pour associer à chaque équipement sa **Fermeture**.   
[Programme de jointure pour les issues de secours]( https://github.com/ExploitIdF/Referentiel_Tunnels/blob/main/LiaisonIssuesFermeture.py)

[Résultat de la jointure pour les issues de secours]( https://raw.githubusercontent.com/ExploitIdF/Referentiel_Tunnels/refs/heads/main/issuesFermetures.csv)



