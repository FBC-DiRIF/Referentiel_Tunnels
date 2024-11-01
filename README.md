# ReferentielTunnels
Tables de référence sur les dénominations et codes des tunnels

## Référence
`https://github.com/OlivierNalin/CombienTunnels`   
Compte rendu d'un exercice qui proposait une classification à 3 niveaux des tubes et des tunnels.  

## Constats
Plusieurs applications de la DiRIF utilisent des noms et des codes différents pour identifier les tunnels.

Les applications n'utilisent pas toutes les mêmes objets ou regroupements de tubes pour identifier les tunnels.
Par exemple Sucombe identifie un tunnel par le nom Thiais mais ne connait pas d'objet correspondant au tunnel du moulin.

## Sucombe
L'application Sucombe comporte un champ **Lieu** dont 21 valeurs correspondent à un tunnel ou à un groupe de tunnels.   
La liste des valeurs est la suivante :   
'Ambroise PARE', 'Antony', 'Bellerive', 'Bicêtre', 'Bobigny-Lumen-Norton', 'Boissy-Saint-Léger', 'Champigny', 'Chennevières', 'Fontenay le Fleury', 'Fresnes', 'Italie', 'La Courneuve', 'Landy', 'Nanterre / La Défense', 'Neuilly', 'Nogent', 'Orly', 'Saint Cloud', 'Sévines', 'Taverny', 'Thiais'



## CosWin
Dans l'application CosWin, les équipements sont associé à un tunnel (26 valeurs différentes) :   
'AMBROISE_PARE', 'ANTONY', 'BELLE-RIVE', 'BICETRE', 'BOBIGNY', 'BOISSY',
       'CHAMPIGNY', 'CHENNEVIERES', 'ECHANGEUR_NANTERRE', 'FONTENAY',       'FRESNES', 'GUY-MOQUET', 'ITALIE', 'LANDY', 'LA_COURNEUVE',
       'LA_DEFENSE', 'LUMEN_NORTON', 'MOULIN', 'NANTERRE_CENTRE', 'NEUILLY',       'NOGENT', 'ORLY', 'SAINT-CLOUD', 'SEVINES', 'TAVERNY', 'TRINITY'

CosWin renseigne également l'axe :'A1', 'A115', 'A12', 'A13', 'A14', 'A14XA86', 'A4', 'A6B', 'A86EST',
       'A86NORD', 'A86OUEST', 'A86SUD', 'N1013', 'N1014', 'N12', 'N13', 'N19',       'N192', 'N314', 'N315', 'N7'

Et le sens : 'E', 'E>W', 'E>Y', 'I', 'I>W', 'W', 'W>I', 'Y', 'Y>E', 'Y>I'

Quand on croise ces 3 variables, on obtient 74 possibilités :   
['Table Tunnel x Axe x Sens (Téléchargement 7k)'](https://github.com/ExploitIdF/ReferentielTunnels/blob/main/tunnelAxeSens.xlsx)

On constate que certains croisements ne cnocernent qu'un seul équipement. 
Il peut parfois s'agit d'une anomalie de l'enregistrement dans CosWin :    
['Table des équipements singuliers '](https://github.com/ExploitIdF/ReferentielTunnels/blob/main/equipMalLocalisé.csv)

## Correspondance entre CosWin et Sucombe
Dans Sucombe, 3 lieux sont des regroupements de plusieurs tunnels au sens de CosWin :   
'Bobigny-Lumen-Norton', 'Nanterre / La Défense',  'Thiais'

En outre, même quand les objets sont les mêmes, leurs écritures diffèrent.

On pourra utiliser la table de correspondante téléchargeable ici :  
['Table de correspondance CosWin -> Sucombe](https://raw.githubusercontent.com/ExploitIdF/ReferentielTunnels/refs/heads/main/tunnelsCosWinSucombe.csv)

['code utilisé pour établir la table'](https://github.com/ExploitIdF/ReferentielTunnels/blob/main/codeCorrCosWinSucombe)

## Regroupements de fermetures
Pour massifier certaines actions de maintenance de nuit sous fermeture, il est utile d'identifier les sections de tunnels 
qui sont le plus souvent fermées en même temps.   
Environ 30 regroupements de ce type ont été identifiés en concertation avec les PCTT.

Certaines associations vont de soi comme : 

* Moulin et G. Moquet (Thais),
* Boulogne A. Paré et Saint Cloud (A13).    

D'autres regroupements sont le résultat d'un choix réfléchi tels que :
* bobigny Lumen Norton & La Courneuve
* Les deux sens des tunnels des Sévines, de Chennevières, de Taverny
* La Défense (A14-Y) & B5 (ECH W>I)

Cependant, les tunnels de Belle Rive et de Nanterre, qui sont généralement fermés ensemble, n'ont pas été regroupés 
car ils ne sont pas gérés par le même pôle de maintenance.

Les regroupements sont formalisés dans la table accessible par le lien ci-dessous :   
['Correspondance entre Fermetures & couples (Tunnel, Sens)'](https://raw.githubusercontent.com/ExploitIdF/ReferentielTunnels/refs/heads/main/CorTbFerm.csv)

A partir de la table des équipements de CosWin, on peut faire une jointure avec cette table sur les champs Tunnel et Sens, 
pour associer à chaque équipement sa **Fermeture**




