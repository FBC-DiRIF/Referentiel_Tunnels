# Mise à jour de issuesFermetures.csv'
import pandas as pd
issues=pd.read_csv('https://raw.githubusercontent.com/ExploitIdF/IssuesTunnels/main/_static/issuesTunnelsDIRIF.csv')
CorTbFerm=pd.read_csv('https://raw.githubusercontent.com/ExploitIdF/ReferentielTunnels/refs/heads/main/CorTbFerm.csv')
issuesFermetures=issues[['CodeEx', 'PC', 'Tatouage', 'triCode' ,'Sens']] .join(CorTbFerm.set_index(['triCode','Sens'])['Fermeture'],on=['triCode','Sens'])
issuesFermetures.to_csv('issuesFermetures.csv',index=False)