# ReferentielTunnels
Tables de référence sur les dénominations et codes des tunnels

## Référence
`https://github.com/OlivierNalin/CombienTunnels`   
On mentionne cet exercice qui proposait une classification à 3 niveaux des tubes et des tunnels.  

## Constats
Plusieurs applications de la DiRIF utilisent des noms et des codes différents pour identifier les tunnels.

Les applications n'utilisent pas toutes les mêmes objets ou regroupements de tubes pour identifier les tunnels.
Par exemple Sucombe identifie un tunnel par le nom Thiais mais ne connait pas d'objet correspondant au tunnel du moulin.

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

