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
Dans l'application CosWin, les équipements sont associé à un tunnel : 'AMBROISE_PARE', 'ANTONY', 'BELLE-RIVE', 'BICETRE', 'BOBIGNY', 'BOISSY',
       'CHAMPIGNY', 'CHENNEVIERES', 'ECHANGEUR_NANTERRE', 'FONTENAY',       'FRESNES', 'GUY-MOQUET', 'ITALIE', 'LANDY', 'LA_COURNEUVE',
       'LA_DEFENSE', 'LUMEN_NORTON', 'MOULIN', 'NANTERRE_CENTRE', 'NEUILLY',       'NOGENT', 'ORLY', 'SAINT-CLOUD', 'SEVINES', 'TAVERNY', 'TRINITY'

CosWin renseigne également l'axe :'A1', 'A115', 'A12', 'A13', 'A14', 'A14XA86', 'A4', 'A6B', 'A86EST',
       'A86NORD', 'A86OUEST', 'A86SUD', 'N1013', 'N1014', 'N12', 'N13', 'N19',       'N192', 'N314', 'N315', 'N7'

Et le sens : 'E', 'E>W', 'E>Y', 'I', 'I>W', 'W', 'W>I', 'Y', 'Y>E', 'Y>I'

Quand on croise ces 3 variables, on obtient 74 possibilités : 

.. csv-table::
   :header: Tunnel,Axe,Sens,Nombre d'équipements
   :widths: 40, 20,20,20
   :width: 100%

       AMBROISE_PARE,A13,W,288
       AMBROISE_PARE,A13,Y,275
       ANTONY,A86SUD,E,158
       ANTONY,A86SUD,I,226
       BELLE-RIVE,A86OUEST,E,299
       BELLE-RIVE,A86OUEST,I,236
       BICETRE,A6B,W,198
       BICETRE,A6B,Y,176
       BOBIGNY,A86NORD,E,579
       BOBIGNY,A86NORD,I,606
       BOISSY,N19,W,252
       BOISSY,N19,Y,198
       CHAMPIGNY,A4,W,239
       CHAMPIGNY,A4,Y,259
       CHENNEVIERES,N12,W,75
       CHENNEVIERES,N12,Y,79
       ECHANGEUR_NANTERRE,A14,Y,2
       ECHANGEUR_NANTERRE,A14XA86,E,27
       ECHANGEUR_NANTERRE,A14XA86,E>W,162
       ECHANGEUR_NANTERRE,A14XA86,E>Y,56
       ECHANGEUR_NANTERRE,A14XA86,I,4
       ECHANGEUR_NANTERRE,A14XA86,I>W,50
       ECHANGEUR_NANTERRE,A14XA86,W,3
       ECHANGEUR_NANTERRE,A14XA86,W>I,154
       ECHANGEUR_NANTERRE,A14XA86,Y>E,151
       ECHANGEUR_NANTERRE,A14XA86,Y>I,9
       ECHANGEUR_NANTERRE,A86OUEST,E,1
       ECHANGEUR_NANTERRE,A86OUEST,I,3
       FONTENAY,A12,W,181
       FONTENAY,A12,Y,147
       FRESNES,A86SUD,E,75
       FRESNES,A86SUD,I,191
       GUY-MOQUET,A86EST,E,134
       GUY-MOQUET,A86EST,I,173
       ITALIE,A6B,W,20
       ITALIE,A6B,Y,116
       LANDY,A1,W,427
       LANDY,A1,Y,392
       LANDY,A86NORD,E,1
       LA_COURNEUVE,A86NORD,E,66
       LA_COURNEUVE,A86NORD,I,61
       LA_DEFENSE,A14,W,850
       LA_DEFENSE,A14,Y,973
       LA_DEFENSE,A86OUEST,I,1
       LA_DEFENSE,N1013,W,48
       LA_DEFENSE,N1013,Y,31
       LA_DEFENSE,N1014,W,22
       LA_DEFENSE,N1014,Y,28
       LA_DEFENSE,N192,W,63
       LA_DEFENSE,N192,Y,58
       LA_DEFENSE,N314,W,33
       LA_DEFENSE,N314,Y,42
       LUMEN_NORTON,A86NORD,E,149
       LUMEN_NORTON,A86NORD,I,199
       MOULIN,A86EST,E,260
       MOULIN,A86EST,I,163
       NANTERRE_CENTRE,A86OUEST,E,231
       NANTERRE_CENTRE,A86OUEST,I,270
       NANTERRE_CENTRE,N314,E,1
       NEUILLY,A14,W,1
       NEUILLY,N13,W,117
       NEUILLY,N13,Y,92
       NOGENT,A86EST,E,324
       NOGENT,A86EST,I,560
       ORLY,N7,W,95
       ORLY,N7,Y,136
       SAINT-CLOUD,A13,W,274
       SAINT-CLOUD,A13,Y,281
       SEVINES,N315,W,77
       SEVINES,N315,Y,138
       TAVERNY,A115,W,107
       TAVERNY,A115,Y,85
       TRINITY,N192,W,22
       TRINITY,N192,Y,21


`Table tunnel x Axe x Sens <https://github.com/ExploitIdF/ReferentielTunnels/blob/main/tunnelAxeSens.xlsx>`_



