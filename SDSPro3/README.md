# SDS_Pro3 — split DXL design elements
Source: `SDS_Pro3.xml` (full-database DXL export, 35706940 bytes).
Each file below is a **standalone, valid DXL fragment**: the original `<database>` root attributes are preserved and a single design element is wrapped inside, so any file can be re-imported into Domino Designer on its own.

## Element counts by category
- **_data/** — 1
- **_meta/** — 3
- **agents/** — 43
- **dbscript/** — 1
- **folders/** — 2
- **forms/** — 100
- **framesets/** — 1
- **libraries/** — 152
- **outlines/** — 5
- **pages/** — 5
- **rawnotes/** — 21
- **resources/** — 96
- **sharedfields/** — 17
- **subforms/** — 11
- **views/** — 115

## Full manifest
| Category | Element name | File | Bytes |
|---|---|---|---|
| _data | `agentdata (3270 notes bundled)` | `_data/agentdata.dxl` | 3844570 |
| _meta | `databaseinfo` | `_meta/databaseinfo.dxl` | 783 |
| _meta | `fulltextsettings` | `_meta/fulltextsettings.dxl` | 606 |
| _meta | `launchsettings` | `_meta/launchsettings.dxl` | 555 |
| agents | `(Proposition\CopierCommissions)` | `agents/(Proposition/CopierCommissions).dxl` | 32642 |
| agents | `1RM` | `agents/1RM.dxl` | 2443 |
| agents | `Admin\EditDocument` | `agents/Admin/EditDocument.dxl` | 3036 |
| agents | `Admin\Historique de réplication` | `agents/Admin/Historique de réplication.dxl` | 16347 |
| agents | `Assigner numéro séquentiel` | `agents/Assigner numéro séquentiel.dxl` | 18801 |
| agents | `Assigner numéro séquentiel Immediatement` | `agents/Assigner numéro séquentiel Immediatement.dxl` | 3494 |
| agents | `Commissions\Maj. Statut` | `agents/Commissions/Maj. Statut.dxl` | 9747 |
| agents | `Courriel\Copier mail-in` | `agents/Courriel/Copier mail-in.dxl` | 3846 |
| agents | `Export Opportunities` | `agents/Export Opportunities.dxl` | 3613 |
| agents | `Exporter\Propositions sélectionnées` | `agents/Exporter/Propositions sélectionnées.dxl` | 3835 |
| agents | `Exporter\Toutes les propositions` | `agents/Exporter/Toutes les propositions.dxl` | 3707 |
| agents | `Install locally` | `agents/Install locally.dxl` | 3620 |
| agents | `Installer localement` | `agents/Installer localement.dxl` | 3614 |
| agents | `LEI\Courriel des code de programme` | `agents/LEI/Courriel des code de programme.dxl` | 7829 |
| agents | `Maj geolocalisation` | `agents/Maj geolocalisation.dxl` | 5551 |
| agents | `Maj projeto` | `agents/Maj projeto.dxl` | 4192 |
| agents | `Mises à jour journalières` | `agents/Mises à jour journalières.dxl` | 6578 |
| agents | `Outils\Corriger le statut des produits` | `agents/Outils/Corriger le statut des produits.dxl` | 15091 |
| agents | `Outils\Lien Notes\Base de documents` | `agents/Outils/Lien Notes/Base de documents.dxl` | 2387 |
| agents | `Outils\Lien Notes\Document` | `agents/Outils/Lien Notes/Document.dxl` | 2786 |
| agents | `Outils\Maj FT index` | `agents/Outils/Maj FT index.dxl` | 9754 |
| agents | `Outils\Modifier item` | `agents/Outils/Modifier item.dxl` | 11773 |
| agents | `Outils\Profil personnel\Modifier` | `agents/Outils/Profil personnel/Modifier.dxl` | 4733 |
| agents | `Outils\Profil personnel\Supprimer` | `agents/Outils/Profil personnel/Supprimer.dxl` | 4733 |
| agents | `Outils\Rafraîchir Documents` | `agents/Outils/Rafraîchir Documents.dxl` | 2243 |
| agents | `Outils\Régler les conflits` | `agents/Outils/Régler les conflits.dxl` | 9363 |
| agents | `Outils\Vérifier réplication` | `agents/Outils/Vérifier réplication.dxl` | 7928 |
| agents | `Proposition\Ouvrir` | `agents/Proposition/Ouvrir.dxl` | 3955 |
| agents | `Propositions\Changer le numéro du client` | `agents/Propositions/Changer le numéro du client.dxl` | 2166 |
| agents | `Propositions\Changer statut` | `agents/Propositions/Changer statut.dxl` | 4014 |
| agents | `Propositions\Corriger ordre des sites` | `agents/Propositions/Corriger ordre des sites.dxl` | 11414 |
| agents | `Propositions\Purge` | `agents/Propositions/Purge.dxl` | 8015 |
| agents | `Propositions\Réinitialiser la sécurité` | `agents/Propositions/Réinitialiser la sécurité.dxl` | 5453 |
| agents | `Propositions\Réinitialiser les commissions` | `agents/Propositions/Réinitialiser les commissions.dxl` | 4081 |
| agents | `Propositions\Sync Salesforce Opportunity` | `agents/Propositions/Sync Salesforce Opportunity.dxl` | 5595 |
| agents | `Salesforce\DeleteOpportunityLineItems` | `agents/Salesforce/DeleteOpportunityLineItems.dxl` | 5662 |
| agents | `Salesforce\SyncOpportunities` | `agents/Salesforce/SyncOpportunities.dxl` | 6006 |
| agents | `Suppr Doc Temporaire` | `agents/Suppr Doc Temporaire.dxl` | 10201 |
| agents | `Test Signataire` | `agents/Test Signataire.dxl` | 8897 |
| agents | `Test-TransactionPut` | `agents/Test-TransactionPut.dxl` | 9291 |
| agents | `Test\NomProfilSalesforceAPI` | `agents/Test/NomProfilSalesforceAPI.dxl` | 3794 |
| agents | `Test\UpdateOpportunityInfo` | `agents/Test/UpdateOpportunityInfo.dxl` | 3157 |
| agents | `Workflow\Courriels` | `agents/Workflow/Courriels.dxl` | 12344 |
| dbscript | `databasescript` | `dbscript/databasescript.dxl` | 11796 |
| folders | `D_SICS` | `folders/D_SICS.dxl` | 6806 |
| folders | `D_SICS` | `folders/D_SICS__2.dxl` | 20642 |
| forms | `Admin\Compteurs séquentiels` | `forms/Admin/Compteurs séquentiels.dxl` | 57985 |
| forms | `Admin\Conflit` | `forms/Admin/Conflit.dxl` | 66887 |
| forms | `Admin\Historique de réplication` | `forms/Admin/Historique de réplication.dxl` | 20702 |
| forms | `Admin\Historique de réplication DB` | `forms/Admin/Historique de réplication DB.dxl` | 19348 |
| forms | `Admin\Profil` | `forms/Admin/Profil.dxl` | 83147 |
| forms | `Admin\Profil personnel` | `forms/Admin/Profil personnel.dxl` | 29455 |
| forms | `Base\Classeur Excel type` | `forms/Base/Classeur Excel type.dxl` | 27221 |
| forms | `Base\Courriel type` | `forms/Base/Courriel type.dxl` | 19919 |
| forms | `Base\Exportation` | `forms/Base/Exportation.dxl` | 44151 |
| forms | `Base\Historique` | `forms/Base/Historique.dxl` | 22798 |
| forms | `Base\Historique EN` | `forms/Base/Historique EN.dxl` | 22762 |
| forms | `Base\Historique Ligne` | `forms/Base/Historique Ligne.dxl` | 18509 |
| forms | `Base\Lettre type` | `forms/Base/Lettre type.dxl` | 38848 |
| forms | `Base\Profil DocuSign` | `forms/Base/Profil DocuSign.dxl` | 102045 |
| forms | `Base\Profil OneSpanSign` | `forms/Base/Profil OneSpanSign.dxl` | 106757 |
| forms | `Base\Selection` | `forms/Base/Selection.dxl` | 21461 |
| forms | `Base\Selection EN` | `forms/Base/Selection EN.dxl` | 21331 |
| forms | `Base\Table` | `forms/Base/Table.dxl` | 39449 |
| forms | `Bon de commande\Envoyer Dsg` | `forms/Bon de commande/Envoyer Dsg.dxl` | 35564 |
| forms | `Bon de commande\Envoyer Dsg EN` | `forms/Bon de commande/Envoyer Dsg EN.dxl` | 28393 |
| forms | `Contact\Sans courriel` | `forms/Contact/Sans courriel.dxl` | 15024 |
| forms | `Contact\Sans courriel EN` | `forms/Contact/Sans courriel EN.dxl` | 15059 |
| forms | `DB\Commentaire` | `forms/DB/Commentaire.dxl` | 8739 |
| forms | `DB\Statut` | `forms/DB/Statut.dxl` | 18246 |
| forms | `Document\Attacher` | `forms/Document/Attacher.dxl` | 24487 |
| forms | `Document\Attacher EN` | `forms/Document/Attacher EN.dxl` | 26263 |
| forms | `Document\Envoyer OSsg` | `forms/Document/Envoyer OSsg.dxl` | 35079 |
| forms | `Document\Envoyer OSsg EN` | `forms/Document/Envoyer OSsg EN.dxl` | 27687 |
| forms | `Imprimer\ImprimerEnvoyer Dsg` | `forms/Imprimer/ImprimerEnvoyer Dsg.dxl` | 27112 |
| forms | `Imprimer\ImprimerEnvoyer OSSg` | `forms/Imprimer/ImprimerEnvoyer OSSg.dxl` | 26609 |
| forms | `Paramètres\Formation` | `forms/Paramètres/Formation.dxl` | 281646 |
| forms | `Paramètres\Formation EN` | `forms/Paramètres/Formation EN.dxl` | 281116 |
| forms | `PNav\Description des produits` | `forms/PNav/Description des produits.dxl` | 25945 |
| forms | `PNav\Description des produits EN` | `forms/PNav/Description des produits EN.dxl` | 25946 |
| forms | `PNav\Description des produits LG` | `forms/PNav/Description des produits LG.dxl` | 27972 |
| forms | `PNav\Description des produits LG EN` | `forms/PNav/Description des produits LG EN.dxl` | 27973 |
| forms | `PNav\Produits auto maj` | `forms/PNav/Produits auto maj.dxl` | 20861 |
| forms | `PNav\Produits manuel` | `forms/PNav/Produits manuel.dxl` | 96872 |
| forms | `PNav\Produits manuel EN` | `forms/PNav/Produits manuel EN.dxl` | 96865 |
| forms | `PNav\Produits par département` | `forms/PNav/Produits par département.dxl` | 100077 |
| forms | `PNav\Produits par département EN` | `forms/PNav/Produits par département EN.dxl` | 100138 |
| forms | `Produit` | `forms/Produit.dxl` | 109624 |
| forms | `Produit EN` | `forms/Produit EN.dxl` | 118453 |
| forms | `Produit\Ajout confirmation` | `forms/Produit/Ajout confirmation.dxl` | 16310 |
| forms | `Produit\Ajout confirmation EN` | `forms/Produit/Ajout confirmation EN.dxl` | 13692 |
| forms | `Produit\Ajouter` | `forms/Produit/Ajouter.dxl` | 310653 |
| forms | `Produit\Ajouter EN` | `forms/Produit/Ajouter EN.dxl` | 310677 |
| forms | `Produit\Avertissement import CS` | `forms/Produit/Avertissement import CS.dxl` | 15941 |
| forms | `Produit\Avertissement import CS EN` | `forms/Produit/Avertissement import CS EN.dxl` | 15949 |
| forms | `Produits\Non disponible` | `forms/Produits/Non disponible.dxl` | 13810 |
| forms | `Produits\Non disponible EN` | `forms/Produits/Non disponible EN.dxl` | 13810 |
| forms | `Produits\Recalculer couts` | `forms/Produits/Recalculer couts.dxl` | 23848 |
| forms | `Produits\Recalculer couts EN` | `forms/Produits/Recalculer couts EN.dxl` | 23494 |
| forms | `Proposition` | `forms/Proposition.dxl` | 16009 |
| forms | `Proposition 0.00\Proposition` | `forms/Proposition 0.00/Proposition.dxl` | 551177 |
| forms | `Proposition 0.00\Proposition EN` | `forms/Proposition 0.00/Proposition EN.dxl` | 550464 |
| forms | `Proposition 0.01\Sites` | `forms/Proposition 0.01/Sites.dxl` | 577039 |
| forms | `Proposition 0.01\Sites EN` | `forms/Proposition 0.01/Sites EN.dxl` | 576143 |
| forms | `Proposition 2.00.00\Site` | `forms/Proposition 2.00.00/Site.dxl` | 422246 |
| forms | `Proposition 2.00.00\Site EN` | `forms/Proposition 2.00.00/Site EN.dxl` | 421394 |
| forms | `Proposition 2.00.01\Comptabilité` | `forms/Proposition 2.00.01/Comptabilité.dxl` | 414920 |
| forms | `Proposition 2.00.01\Comptabilité EN` | `forms/Proposition 2.00.01/Comptabilité EN.dxl` | 414478 |
| forms | `Proposition 2.00.02\Ventes` | `forms/Proposition 2.00.02/Ventes.dxl` | 403992 |
| forms | `Proposition 2.00.02\Ventes EN` | `forms/Proposition 2.00.02/Ventes EN.dxl` | 403806 |
| forms | `Proposition 2.00.03\Service` | `forms/Proposition 2.00.03/Service.dxl` | 462036 |
| forms | `Proposition 2.00.03\Service EN` | `forms/Proposition 2.00.03/Service EN.dxl` | 461984 |
| forms | `Proposition 2.00.04\Pièces` | `forms/Proposition 2.00.04/Pièces.dxl` | 417445 |
| forms | `Proposition 2.00.04\Pièces EN` | `forms/Proposition 2.00.04/Pièces EN.dxl` | 417049 |
| forms | `Proposition 2.00.05\Formation` | `forms/Proposition 2.00.05/Formation.dxl` | 880808 |
| forms | `Proposition 2.00.05\Formation EN` | `forms/Proposition 2.00.05/Formation EN.dxl` | 879888 |
| forms | `Proposition 2.00.06\Interfaces` | `forms/Proposition 2.00.06/Interfaces.dxl` | 388980 |
| forms | `Proposition 2.00.06\Interfaces EN` | `forms/Proposition 2.00.06/Interfaces EN.dxl` | 389060 |
| forms | `Proposition 2.00.50\Produits` | `forms/Proposition 2.00.50/Produits.dxl` | 415723 |
| forms | `Proposition 2.00.50\Produits EN` | `forms/Proposition 2.00.50/Produits EN.dxl` | 415858 |
| forms | `Proposition 2.00.51\Résumé` | `forms/Proposition 2.00.51/Résumé.dxl` | 383902 |
| forms | `Proposition 2.00.51\Résumé EN` | `forms/Proposition 2.00.51/Résumé EN.dxl` | 383777 |
| forms | `Proposition 6.00\Contrat` | `forms/Proposition 6.00/Contrat.dxl` | 373498 |
| forms | `Proposition 6.00\Contrat EN` | `forms/Proposition 6.00/Contrat EN.dxl` | 373537 |
| forms | `Proposition 8.00\Produits` | `forms/Proposition 8.00/Produits.dxl` | 404585 |
| forms | `Proposition 8.00\Produits EN` | `forms/Proposition 8.00/Produits EN.dxl` | 404682 |
| forms | `Proposition 8.01\Résumé` | `forms/Proposition 8.01/Résumé.dxl` | 745401 |
| forms | `Proposition 8.01\Résumé EN` | `forms/Proposition 8.01/Résumé EN.dxl` | 744782 |
| forms | `Proposition 8.02\Commissions` | `forms/Proposition 8.02/Commissions.dxl` | 374721 |
| forms | `Proposition 8.02\Commissions EN` | `forms/Proposition 8.02/Commissions EN.dxl` | 374735 |
| forms | `Proposition 8.03\Historique` | `forms/Proposition 8.03/Historique.dxl` | 370633 |
| forms | `Proposition 8.03\Historique EN` | `forms/Proposition 8.03/Historique EN.dxl` | 370522 |
| forms | `Proposition 8.04\Documents` | `forms/Proposition 8.04/Documents.dxl` | 368630 |
| forms | `Proposition 8.04\Documents EN` | `forms/Proposition 8.04/Documents EN.dxl` | 368626 |
| forms | `Proposition 8.05\Modifications` | `forms/Proposition 8.05/Modifications.dxl` | 373296 |
| forms | `Proposition 8.05\Modifications EN` | `forms/Proposition 8.05/Modifications EN.dxl` | 373196 |
| forms | `Proposition\Alerte statut` | `forms/Proposition/Alerte statut.dxl` | 64015 |
| forms | `Proposition\Contact courriel` | `forms/Proposition/Contact courriel.dxl` | 6665 |
| forms | `Proposition\Contact courriel EN` | `forms/Proposition/Contact courriel EN.dxl` | 6708 |
| forms | `Proposition\Image` | `forms/Proposition/Image.dxl` | 18507 |
| forms | `Proposition\Image EN` | `forms/Proposition/Image EN.dxl` | 20200 |
| forms | `Proposition\Modifier ClientNoFmt` | `forms/Proposition/Modifier ClientNoFmt.dxl` | 20797 |
| forms | `Proposition\Signée` | `forms/Proposition/Signée.dxl` | 518515 |
| forms | `Proposition\Signée EN` | `forms/Proposition/Signée EN.dxl` | 518630 |
| forms | `Propositions\Client` | `forms/Propositions/Client.dxl` | 27642 |
| forms | `Propositions\Client EN` | `forms/Propositions/Client EN.dxl` | 27571 |
| framesets | `Agencement Notes` | `framesets/Agencement Notes.dxl` | 2327 |
| libraries | `A_Inst` | `libraries/A_Inst.dxl` | 15927 |
| libraries | `DB_EnvoiDSg` | `libraries/DB_EnvoiDSg.dxl` | 8182 |
| libraries | `DB_EnvoiOSSg` | `libraries/DB_EnvoiOSSg.dxl` | 8513 |
| libraries | `DB_PDep` | `libraries/DB_PDep.dxl` | 14398 |
| libraries | `DB_PFor` | `libraries/DB_PFor.dxl` | 17105 |
| libraries | `DB_PMan` | `libraries/DB_PMan.dxl` | 12853 |
| libraries | `DB_Prod` | `libraries/DB_Prod.dxl` | 14798 |
| libraries | `DB_PropCl` | `libraries/DB_PropCl.dxl` | 5689 |
| libraries | `DB_PropSg` | `libraries/DB_PropSg.dxl` | 17439 |
| libraries | `DB_RCou` | `libraries/DB_RCou.dxl` | 13513 |
| libraries | `DB_SICS` | `libraries/DB_SICS.dxl` | 20549 |
| libraries | `DB_SIGC` | `libraries/DB_SIGC.dxl` | 16993 |
| libraries | `F_Aler` | `libraries/F_Aler.dxl` | 10214 |
| libraries | `F_PNav0.00` | `libraries/F_PNav0.00.dxl` | 190886 |
| libraries | `F_PNav0.01` | `libraries/F_PNav0.01.dxl` | 79601 |
| libraries | `F_PNav2.00.00` | `libraries/F_PNav2.00.00.dxl` | 73756 |
| libraries | `F_PNav2.00.01` | `libraries/F_PNav2.00.01.dxl` | 48540 |
| libraries | `F_PNav2.00.02` | `libraries/F_PNav2.00.02.dxl` | 36542 |
| libraries | `F_PNav2.00.03` | `libraries/F_PNav2.00.03.dxl` | 49400 |
| libraries | `F_PNav2.00.04` | `libraries/F_PNav2.00.04.dxl` | 39678 |
| libraries | `F_PNav2.00.05` | `libraries/F_PNav2.00.05.dxl` | 74550 |
| libraries | `F_PNav2.00.06` | `libraries/F_PNav2.00.06.dxl` | 32666 |
| libraries | `F_PNav2.00.50` | `libraries/F_PNav2.00.50.dxl` | 45266 |
| libraries | `F_PNav2.00.51` | `libraries/F_PNav2.00.51.dxl` | 20901 |
| libraries | `F_PNav2.00.xx` | `libraries/F_PNav2.00.xx.dxl` | 30895 |
| libraries | `F_PNav6.00` | `libraries/F_PNav6.00.dxl` | 41444 |
| libraries | `F_PNav8.00` | `libraries/F_PNav8.00.dxl` | 29162 |
| libraries | `F_PNav8.01` | `libraries/F_PNav8.01.dxl` | 32528 |
| libraries | `F_PNav8.02` | `libraries/F_PNav8.02.dxl` | 27345 |
| libraries | `F_PNav8.03` | `libraries/F_PNav8.03.dxl` | 31491 |
| libraries | `F_PNav8.04` | `libraries/F_PNav8.04.dxl` | 20056 |
| libraries | `F_PNav8.05` | `libraries/F_PNav8.05.dxl` | 28722 |
| libraries | `F_PNav8.xx` | `libraries/F_PNav8.xx.dxl` | 30664 |
| libraries | `F_PrCl` | `libraries/F_PrCl.dxl` | 5805 |
| libraries | `F_Prod` | `libraries/F_Prod.dxl` | 35277 |
| libraries | `F_SIEx` | `libraries/F_SIEx.dxl` | 4018 |
| libraries | `F_SILT` | `libraries/F_SILT.dxl` | 12501 |
| libraries | `F_SIXT` | `libraries/F_SIXT.dxl` | 7151 |
| libraries | `F_Tabl` | `libraries/F_Tabl.dxl` | 15775 |
| libraries | `SDS_ContratsService` | `libraries/SDS_ContratsService.dxl` | 16898 |
| libraries | `SDSP_Alertes` | `libraries/SDSP_Alertes.dxl` | 6574 |
| libraries | `SDSP_BonCommande` | `libraries/SDSP_BonCommande.dxl` | 21032 |
| libraries | `SDSP_CalculsProp` | `libraries/SDSP_CalculsProp.dxl` | 23877 |
| libraries | `SDSP_ChangerNoClient` | `libraries/SDSP_ChangerNoClient.dxl` | 13128 |
| libraries | `SDSP_Commissions` | `libraries/SDSP_Commissions.dxl` | 11978 |
| libraries | `SDSP_DatabaseScript` | `libraries/SDSP_DatabaseScript.dxl` | 15175 |
| libraries | `SDSP_Document` | `libraries/SDSP_Document.dxl` | 17479 |
| libraries | `SDSP_DocuSign` | `libraries/SDSP_DocuSign.dxl` | 32968 |
| libraries | `SDSP_Duplication` | `libraries/SDSP_Duplication.dxl` | 26230 |
| libraries | `SDSP_Exportations` | `libraries/SDSP_Exportations.dxl` | 12422 |
| libraries | `SDSP_Facturation` | `libraries/SDSP_Facturation.dxl` | 28148 |
| libraries | `SDSP_Image` | `libraries/SDSP_Image.dxl` | 74383 |
| libraries | `SDSP_Impression` | `libraries/SDSP_Impression.dxl` | 263985 |
| libraries | `SDSP_MasquePNav` | `libraries/SDSP_MasquePNav.dxl` | 133452 |
| libraries | `SDSP_Navigation` | `libraries/SDSP_Navigation.dxl` | 41190 |
| libraries | `SDSP_OneSpanSign` | `libraries/SDSP_OneSpanSign.dxl` | 45299 |
| libraries | `SDSP_OneSpanSign_Paquet` | `libraries/SDSP_OneSpanSign_Paquet.dxl` | 12002 |
| libraries | `SDSP_Produit` | `libraries/SDSP_Produit.dxl` | 170585 |
| libraries | `SDSP_Projeto` | `libraries/SDSP_Projeto.dxl` | 13814 |
| libraries | `SDSP_Proposition` | `libraries/SDSP_Proposition.dxl` | 100019 |
| libraries | `SDSP_PropositionUI` | `libraries/SDSP_PropositionUI.dxl` | 37182 |
| libraries | `SDSP_Salesforce` | `libraries/SDSP_Salesforce.dxl` | 36695 |
| libraries | `SDSP_Site` | `libraries/SDSP_Site.dxl` | 53514 |
| libraries | `SDSP_Workflow` | `libraries/SDSP_Workflow.dxl` | 65650 |
| libraries | `SI_AgentsTravaux` | `libraries/SI_AgentsTravaux.dxl` | 11065 |
| libraries | `SI_Aide` | `libraries/SI_Aide.dxl` | 6999 |
| libraries | `SI_Arrays` | `libraries/SI_Arrays.dxl` | 20671 |
| libraries | `SI_ClasseursTypes` | `libraries/SI_ClasseursTypes.dxl` | 13625 |
| libraries | `SI_Clients` | `libraries/SI_Clients.dxl` | 17922 |
| libraries | `SI_CompteurSequentiel` | `libraries/SI_CompteurSequentiel.dxl` | 24953 |
| libraries | `SI_Contacts` | `libraries/SI_Contacts.dxl` | 15539 |
| libraries | `SI_CourrielsTypes` | `libraries/SI_CourrielsTypes.dxl` | 57805 |
| libraries | `SI_DatabaseScript` | `libraries/SI_DatabaseScript.dxl` | 19146 |
| libraries | `SI_DocumentsVentes` | `libraries/SI_DocumentsVentes.dxl` | 10860 |
| libraries | `SI_Exportations` | `libraries/SI_Exportations.dxl` | 44609 |
| libraries | `SI_Extractions` | `libraries/SI_Extractions.dxl` | 27620 |
| libraries | `SI_FichierWIN` | `libraries/SI_FichierWIN.dxl` | 14267 |
| libraries | `SI_GestionConflits` | `libraries/SI_GestionConflits.dxl` | 30308 |
| libraries | `SI_GestionErreurs` | `libraries/SI_GestionErreurs.dxl` | 20085 |
| libraries | `SI_Google` | `libraries/SI_Google.dxl` | 21195 |
| libraries | `SI_Historique` | `libraries/SI_Historique.dxl` | 30040 |
| libraries | `SI_Insertions` | `libraries/SI_Insertions.dxl` | 13163 |
| libraries | `SI_Jabber` | `libraries/SI_Jabber.dxl` | 11825 |
| libraries | `SI_LettresTypes` | `libraries/SI_LettresTypes.dxl` | 29778 |
| libraries | `SI_MSExcel` | `libraries/SI_MSExcel.dxl` | 22828 |
| libraries | `SI_MSPowerPoint` | `libraries/SI_MSPowerPoint.dxl` | 8914 |
| libraries | `SI_MSWord` | `libraries/SI_MSWord.dxl` | 36284 |
| libraries | `SI_NotesAPI` | `libraries/SI_NotesAPI.dxl` | 7536 |
| libraries | `SI_NotesDatabase` | `libraries/SI_NotesDatabase.dxl` | 8704 |
| libraries | `SI_NotesDocument` | `libraries/SI_NotesDocument.dxl` | 13872 |
| libraries | `SI_NotesDocumentCollection` | `libraries/SI_NotesDocumentCollection.dxl` | 8260 |
| libraries | `SI_NotesFormula` | `libraries/SI_NotesFormula.dxl` | 7601 |
| libraries | `SI_NotesMail` | `libraries/SI_NotesMail.dxl` | 24887 |
| libraries | `SI_NUIV` | `libraries/SI_NUIV.dxl` | 12926 |
| libraries | `SI_Projeto` | `libraries/SI_Projeto.dxl` | 29301 |
| libraries | `SI_Representants` | `libraries/SI_Representants.dxl` | 9952 |
| libraries | `SI_Selection` | `libraries/SI_Selection.dxl` | 20821 |
| libraries | `SI_Signatures` | `libraries/SI_Signatures.dxl` | 20690 |
| libraries | `SI_tDate` | `libraries/SI_tDate.dxl` | 31523 |
| libraries | `SI_Temp` | `libraries/SI_Temp.dxl` | 3448 |
| libraries | `SI_tNombre` | `libraries/SI_tNombre.dxl` | 24703 |
| libraries | `SI_tRichText` | `libraries/SI_tRichText.dxl` | 34419 |
| libraries | `SI_tString` | `libraries/SI_tString.dxl` | 21409 |
| libraries | `SI_Windows` | `libraries/SI_Windows.dxl` | 6247 |
| libraries | `SISt_Exportation` | `libraries/SISt_Exportation.dxl` | 24197 |
| libraries | `SJ_OneSpanSign` | `libraries/SJ_OneSpanSign.dxl` | 9650 |
| libraries | `SJ_SalesforceAPI` | `libraries/SJ_SalesforceAPI.dxl` | 5569 |
| libraries | `SL_Clipboard` | `libraries/SL_Clipboard.dxl` | 21222 |
| libraries | `SL_DocuSign` | `libraries/SL_DocuSign.dxl` | 51105 |
| libraries | `SL_JSON` | `libraries/SL_JSON.dxl` | 12148 |
| libraries | `SL_JSONWriter` | `libraries/SL_JSONWriter.dxl` | 43678 |
| libraries | `SL_OneSpanSign` | `libraries/SL_OneSpanSign.dxl` | 55013 |
| libraries | `SL_SalesforceAPI` | `libraries/SL_SalesforceAPI.dxl` | 32017 |
| libraries | `SL_SecuriteMasque` | `libraries/SL_SecuriteMasque.dxl` | 6338 |
| libraries | `SL_SendKeys` | `libraries/SL_SendKeys.dxl` | 38836 |
| libraries | `V_AdmS` | `libraries/V_AdmS.dxl` | 13349 |
| libraries | `V_Aler` | `libraries/V_Aler.dxl` | 8851 |
| libraries | `V_Docu` | `libraries/V_Docu.dxl` | 14361 |
| libraries | `V_Prod` | `libraries/V_Prod.dxl` | 15799 |
| libraries | `V_Prop` | `libraries/V_Prop.dxl` | 31829 |
| libraries | `V_SIEx` | `libraries/V_SIEx.dxl` | 5034 |
| libraries | `wsc_LSXSD` | `libraries/wsc_LSXSD.dxl` | 6084 |
| libraries | `x_GDK` | `libraries/x_GDK.dxl` | 37561 |
| libraries | `x_KLSf` | `libraries/x_KLSf.dxl` | 12052 |
| libraries | `x_NAB` | `libraries/x_NAB.dxl` | 13676 |
| libraries | `x_PDSg` | `libraries/x_PDSg.dxl` | 6552 |
| libraries | `x_PJ` | `libraries/x_PJ.dxl` | 23662 |
| libraries | `x_POSSg` | `libraries/x_POSSg.dxl` | 6106 |
| libraries | `x_SDSBB` | `libraries/x_SDSBB.dxl` | 30981 |
| libraries | `x_SDSC3` | `libraries/x_SDSC3.dxl` | 16653 |
| libraries | `x_SDSCS` | `libraries/x_SDSCS.dxl` | 21873 |
| libraries | `x_SDSCSL` | `libraries/x_SDSCSL.dxl` | 15282 |
| libraries | `x_SDSI` | `libraries/x_SDSI.dxl` | 13314 |
| libraries | `x_SDSP3` | `libraries/x_SDSP3.dxl` | 13359 |
| libraries | `x_SDSP3L` | `libraries/x_SDSP3L.dxl` | 17844 |
| libraries | `x_SDSPP` | `libraries/x_SDSPP.dxl` | 22573 |
| libraries | `x_SIAg` | `libraries/x_SIAg.dxl` | 14206 |
| libraries | `x_SIAi` | `libraries/x_SIAi.dxl` | 4061 |
| libraries | `x_SIBDC2` | `libraries/x_SIBDC2.dxl` | 17445 |
| libraries | `x_SIBDT` | `libraries/x_SIBDT.dxl` | 13015 |
| libraries | `x_SICf` | `libraries/x_SICf.dxl` | 31355 |
| libraries | `x_SICg` | `libraries/x_SICg.dxl` | 15089 |
| libraries | `x_SICl` | `libraries/x_SICl.dxl` | 16192 |
| libraries | `x_SICo` | `libraries/x_SICo.dxl` | 18617 |
| libraries | `x_SICT` | `libraries/x_SICT.dxl` | 4668 |
| libraries | `x_SIDocV` | `libraries/x_SIDocV.dxl` | 15738 |
| libraries | `x_SIEm` | `libraries/x_SIEm.dxl` | 29017 |
| libraries | `x_SIEx` | `libraries/x_SIEx.dxl` | 6966 |
| libraries | `x_SILT` | `libraries/x_SILT.dxl` | 12334 |
| libraries | `x_SIRR` | `libraries/x_SIRR.dxl` | 20080 |
| libraries | `x_SIXT` | `libraries/x_SIXT.dxl` | 7833 |
| libraries | `x_Tabl` | `libraries/x_Tabl.dxl` | 16251 |
| outlines | `Banner Menu` | `outlines/Banner Menu.dxl` | 2219 |
| outlines | `Main Menu` | `outlines/Main Menu.dxl` | 5319 |
| outlines | `Menu Admin` | `outlines/Menu Admin.dxl` | 6887 |
| outlines | `Menu Bannière` | `outlines/Menu Bannière.dxl` | 2823 |
| outlines | `Menu Principal` | `outlines/Menu Principal.dxl` | 6029 |
| pages | `Bannière\Menu` | `pages/Bannière/Menu.dxl` | 14691 |
| pages | `Bannière\Titre` | `pages/Bannière/Titre.dxl` | 13250 |
| pages | `Logo` | `pages/Logo.dxl` | 11849 |
| pages | `Menu Admin` | `pages/Menu Admin.dxl` | 12126 |
| pages | `Menu Principal` | `pages/Menu Principal.dxl` | 12067 |
| rawnotes | `filter_55564e` | `rawnotes/filter_55564e.dxl` | 15472 |
| rawnotes | `filter_55566e` | `rawnotes/filter_55566e.dxl` | 24488 |
| rawnotes | `filter_5557c6` | `rawnotes/filter_5557c6.dxl` | 20732 |
| rawnotes | `filter_5557e2` | `rawnotes/filter_5557e2.dxl` | 20087 |
| rawnotes | `filter_555842` | `rawnotes/filter_555842.dxl` | 12842 |
| rawnotes | `filter_55584a` | `rawnotes/filter_55584a.dxl` | 15149 |
| rawnotes | `filter_555852` | `rawnotes/filter_555852.dxl` | 12173 |
| rawnotes | `filter_55591e` | `rawnotes/filter_55591e.dxl` | 47177 |
| rawnotes | `filter_555926` | `rawnotes/filter_555926.dxl` | 19190 |
| rawnotes | `form_162a` | `rawnotes/form_162a.dxl` | 2593 |
| rawnotes | `form_1646` | `rawnotes/form_1646.dxl` | 2935 |
| rawnotes | `form_164a` | `rawnotes/form_164a.dxl` | 2565 |
| rawnotes | `form_1672` | `rawnotes/form_1672.dxl` | 11167 |
| rawnotes | `form_169a` | `rawnotes/form_169a.dxl` | 1937 |
| rawnotes | `form_16d6` | `rawnotes/form_16d6.dxl` | 8872 |
| rawnotes | `form_1776` | `rawnotes/form_1776.dxl` | 2883 |
| rawnotes | `form_180a` | `rawnotes/form_180a.dxl` | 2636 |
| rawnotes | `form_18aa` | `rawnotes/form_18aa.dxl` | 11881 |
| rawnotes | `form_18b6` | `rawnotes/form_18b6.dxl` | 2713 |
| rawnotes | `form_546f8e` | `rawnotes/form_546f8e.dxl` | 1661 |
| rawnotes | `icon_126` | `rawnotes/icon_126.dxl` | 11552 |
| resources | `$DBIcon` | `resources/$DBIcon.dxl` | 4232 |
| resources | `act_Auteur.gif` | `resources/act_Auteur.gif.dxl` | 2347 |
| resources | `act_Blank.gif` | `resources/act_Blank.gif.dxl` | 2704 |
| resources | `act_Crochet.gif` | `resources/act_Crochet.gif.dxl` | 1997 |
| resources | `act_Croix.gif` | `resources/act_Croix.gif.dxl` | 1954 |
| resources | `act_Direction.gif` | `resources/act_Direction.gif.dxl` | 1990 |
| resources | `act_Disquette.gif` | `resources/act_Disquette.gif.dxl` | 1831 |
| resources | `act_DossierAjouter.gif` | `resources/act_DossierAjouter.gif.dxl` | 2020 |
| resources | `act_Eclair.gif` | `resources/act_Eclair.gif.dxl` | 1997 |
| resources | `act_Ecrire.gif` | `resources/act_Ecrire.gif.dxl` | 2026 |
| resources | `act_Envoyer.gif` | `resources/act_Envoyer.gif.dxl` | 2671 |
| resources | `act_Facture.gif` | `resources/act_Facture.gif.dxl` | 3216 |
| resources | `act_FlecheDroite.gif` | `resources/act_FlecheDroite.gif.dxl` | 3125 |
| resources | `act_FlecheGauche.gif` | `resources/act_FlecheGauche.gif.dxl` | 3105 |
| resources | `act_Imprimante.gif` | `resources/act_Imprimante.gif.dxl` | 2663 |
| resources | `act_Jeter.gif` | `resources/act_Jeter.gif.dxl` | 3066 |
| resources | `act_Loupe.gif` | `resources/act_Loupe.gif.dxl` | 2148 |
| resources | `act_Modifier.gif` | `resources/act_Modifier.gif.dxl` | 1871 |
| resources | `act_Nouveau.gif` | `resources/act_Nouveau.gif.dxl` | 1851 |
| resources | `act_Outil.gif` | `resources/act_Outil.gif.dxl` | 1986 |
| resources | `act_Pause.gif` | `resources/act_Pause.gif.dxl` | 3157 |
| resources | `act_PoigneeMains.gif` | `resources/act_PoigneeMains.gif.dxl` | 3300 |
| resources | `act_PouceBas.gif` | `resources/act_PouceBas.gif.dxl` | 1921 |
| resources | `act_PouceHaut.gif` | `resources/act_PouceHaut.gif.dxl` | 1917 |
| resources | `act_Restaurer.gif` | `resources/act_Restaurer.gif.dxl` | 2958 |
| resources | `act_Signer.gif` | `resources/act_Signer.gif.dxl` | 3158 |
| resources | `act_Trier.gif` | `resources/act_Trier.gif.dxl` | 2865 |
| resources | `act_Trombone.gif` | `resources/act_Trombone.gif.dxl` | 3116 |
| resources | `act_Vide.gif` | `resources/act_Vide.gif.dxl` | 2954 |
| resources | `act_ViderCorbeille.gif` | `resources/act_ViderCorbeille.gif.dxl` | 1961 |
| resources | `cb_Blank.gif` | `resources/cb_Blank.gif.dxl` | 2734 |
| resources | `cb_Non.gif` | `resources/cb_Non.gif.dxl` | 2734 |
| resources | `cb_Oui.gif` | `resources/cb_Oui.gif.dxl` | 2748 |
| resources | `Couleur_Bleu` | `resources/Couleur_Bleu.dxl` | 2597 |
| resources | `Couleur_BleuCPA` | `resources/Couleur_BleuCPA.dxl` | 2590 |
| resources | `Couleur_Bourgogne` | `resources/Couleur_Bourgogne.dxl` | 2586 |
| resources | `Couleur_Defaut` | `resources/Couleur_Defaut.dxl` | 2598 |
| resources | `Couleur_Jaune` | `resources/Couleur_Jaune.dxl` | 2598 |
| resources | `Couleur_Noir` | `resources/Couleur_Noir.dxl` | 2592 |
| resources | `Couleur_OrangeCPA` | `resources/Couleur_OrangeCPA.dxl` | 2587 |
| resources | `Couleur_Rose` | `resources/Couleur_Rose.dxl` | 2547 |
| resources | `Couleur_Turquoise` | `resources/Couleur_Turquoise.dxl` | 2602 |
| resources | `Couleur_Vert` | `resources/Couleur_Vert.dxl` | 2577 |
| resources | `Fond_Actions` | `resources/Fond_Actions.dxl` | 8426 |
| resources | `Fond_Menu` | `resources/Fond_Menu.dxl` | 16379 |
| resources | `Fond_NavMenu` | `resources/Fond_NavMenu.dxl` | 3116 |
| resources | `Fond_NavSelection` | `resources/Fond_NavSelection.dxl` | 3120 |
| resources | `Fond_NavSMenu` | `resources/Fond_NavSMenu.dxl` | 3237 |
| resources | `Fond_NavSMenuSel` | `resources/Fond_NavSMenuSel.dxl` | 3226 |
| resources | `Fond_NavVue` | `resources/Fond_NavVue.dxl` | 2699 |
| resources | `Fond_NavVueGris` | `resources/Fond_NavVueGris.dxl` | 2829 |
| resources | `Fond_NavVueSelection` | `resources/Fond_NavVueSelection.dxl` | 2729 |
| resources | `hs_AjouterMoi.gif` | `resources/hs_AjouterMoi.gif.dxl` | 2878 |
| resources | `hs_Annuler.gif` | `resources/hs_Annuler.gif.dxl` | 3186 |
| resources | `hs_Annuler_Orange.png` | `resources/hs_Annuler_Orange.png.dxl` | 2916 |
| resources | `hs_Annuler_Orange_EN.png` | `resources/hs_Annuler_Orange_EN.png.dxl` | 2788 |
| resources | `hs_Copier.gif` | `resources/hs_Copier.gif.dxl` | 3146 |
| resources | `hs_Crayon.GIF` | `resources/hs_Crayon.GIF.dxl` | 2983 |
| resources | `hs_Croix.GIF` | `resources/hs_Croix.GIF.dxl` | 3103 |
| resources | `hs_CS.gif` | `resources/hs_CS.gif.dxl` | 3209 |
| resources | `hs_DerniereEtape.gif` | `resources/hs_DerniereEtape.gif.dxl` | 3176 |
| resources | `hs_Enveloppe.gif` | `resources/hs_Enveloppe.gif.dxl` | 3248 |
| resources | `hs_Envoyer_Orange.png` | `resources/hs_Envoyer_Orange.png.dxl` | 2908 |
| resources | `hs_Envoyer_Orange_EN.png` | `resources/hs_Envoyer_Orange_EN.png.dxl` | 2773 |
| resources | `hs_FlecheDroite.gif` | `resources/hs_FlecheDroite.gif.dxl` | 2915 |
| resources | `hs_FlecheGauche.gif` | `resources/hs_FlecheGauche.gif.dxl` | 2896 |
| resources | `hs_FlecheHautBas.gif` | `resources/hs_FlecheHautBas.gif.dxl` | 2140 |
| resources | `hs_Groupe.gif` | `resources/hs_Groupe.gif.dxl` | 2996 |
| resources | `hs_Info.gif` | `resources/hs_Info.gif.dxl` | 3154 |
| resources | `hs_Loupe.gif` | `resources/hs_Loupe.gif.dxl` | 3032 |
| resources | `hs_Maison.gif` | `resources/hs_Maison.gif.dxl` | 2935 |
| resources | `hs_Moins.gif` | `resources/hs_Moins.gif.dxl` | 2860 |
| resources | `hs_Nord.gif` | `resources/hs_Nord.gif.dxl` | 2962 |
| resources | `hs_Num+` | `resources/hs_Num+.dxl` | 3162 |
| resources | `hs_Num-` | `resources/hs_Num-.dxl` | 2907 |
| resources | `hs_OK.gif` | `resources/hs_OK.gif.dxl` | 3239 |
| resources | `hs_Options.gif` | `resources/hs_Options.gif.dxl` | 2911 |
| resources | `hs_Personne.gif` | `resources/hs_Personne.gif.dxl` | 3170 |
| resources | `hs_Plus.gif` | `resources/hs_Plus.gif.dxl` | 2920 |
| resources | `hs_PP.gif` | `resources/hs_PP.gif.dxl` | 2909 |
| resources | `hs_Prix.gif` | `resources/hs_Prix.gif.dxl` | 2873 |
| resources | `hs_Projeto.GIF` | `resources/hs_Projeto.GIF.dxl` | 2899 |
| resources | `hs_Précédent.gif` | `resources/hs_Précédent.gif.dxl` | 3343 |
| resources | `hs_Rafraîchir.gif` | `resources/hs_Rafraîchir.gif.dxl` | 3074 |
| resources | `hs_Salesforce.png` | `resources/hs_Salesforce.png.dxl` | 2729 |
| resources | `hs_Suivant.gif` | `resources/hs_Suivant.gif.dxl` | 3330 |
| resources | `hs_Zero.gif` | `resources/hs_Zero.gif.dxl` | 3019 |
| resources | `img_CrochetGris.gif` | `resources/img_CrochetGris.gif.dxl` | 2833 |
| resources | `img_Maison` | `resources/img_Maison.dxl` | 2532 |
| resources | `img_Non modifiable.gif` | `resources/img_Non modifiable.gif.dxl` | 3066 |
| resources | `img_Obligatoire.gif` | `resources/img_Obligatoire.gif.dxl` | 3035 |
| resources | `Logo_SDSP3` | `resources/Logo_SDSP3.dxl` | 11849 |
| resources | `Logo_Serti` | `resources/Logo_Serti.dxl` | 4688 |
| resources | `rb_blank.gif` | `resources/rb_blank.gif.dxl` | 1831 |
| resources | `rb_Non.gif` | `resources/rb_Non.gif.dxl` | 2893 |
| resources | `rb_Oui.gif` | `resources/rb_Oui.gif.dxl` | 1877 |
| sharedfields | `SF_FichierNAB` | `sharedfields/SF_FichierNAB.dxl` | 1565 |
| sharedfields | `SF_FichierSDSBB` | `sharedfields/SF_FichierSDSBB.dxl` | 1823 |
| sharedfields | `SF_FichierSDSCS` | `sharedfields/SF_FichierSDSCS.dxl` | 1864 |
| sharedfields | `SF_FichierSDSCSL` | `sharedfields/SF_FichierSDSCSL.dxl` | 1716 |
| sharedfields | `SF_FichierSICl` | `sharedfields/SF_FichierSICl.dxl` | 1721 |
| sharedfields | `SF_FichierSIDV` | `sharedfields/SF_FichierSIDV.dxl` | 1740 |
| sharedfields | `SF_FichierSIRR` | `sharedfields/SF_FichierSIRR.dxl` | 1854 |
| sharedfields | `SF_GDK` | `sharedfields/SF_GDK.dxl` | 1714 |
| sharedfields | `SF_Langue` | `sharedfields/SF_Langue.dxl` | 1737 |
| sharedfields | `SF_Serveur` | `sharedfields/SF_Serveur.dxl` | 1604 |
| sharedfields | `SF_ServeurNAB` | `sharedfields/SF_ServeurNAB.dxl` | 1589 |
| sharedfields | `SF_ServeurSDSBB` | `sharedfields/SF_ServeurSDSBB.dxl` | 1811 |
| sharedfields | `SF_ServeurSDSCS` | `sharedfields/SF_ServeurSDSCS.dxl` | 1852 |
| sharedfields | `SF_ServeurSDSCSL` | `sharedfields/SF_ServeurSDSCSL.dxl` | 1716 |
| sharedfields | `SF_ServeurSICl` | `sharedfields/SF_ServeurSICl.dxl` | 1721 |
| sharedfields | `SF_ServeurSIDV` | `sharedfields/SF_ServeurSIDV.dxl` | 1763 |
| sharedfields | `SF_ServeurSIRR` | `sharedfields/SF_ServeurSIRR.dxl` | 1854 |
| subforms | `Commissions\Calculs EN` | `subforms/Commissions/Calculs EN.dxl` | 48740 |
| subforms | `Commissions\Calculs FR` | `subforms/Commissions/Calculs FR.dxl` | 48243 |
| subforms | `Entete` | `subforms/Entete.dxl` | 10201 |
| subforms | `Historique` | `subforms/Historique.dxl` | 18515 |
| subforms | `Historique EN` | `subforms/Historique EN.dxl` | 18337 |
| subforms | `SF_DescDetaillee_Ecriture` | `subforms/SF_DescDetaillee_Ecriture.dxl` | 12768 |
| subforms | `SF_DescDetaillee_Lecture` | `subforms/SF_DescDetaillee_Lecture.dxl` | 12644 |
| subforms | `Sites` | `subforms/Sites.dxl` | 879897 |
| subforms | `Sites EN` | `subforms/Sites EN.dxl` | 879889 |
| subforms | `Sites\Statut signé` | `subforms/Sites/Statut signé.dxl` | 902886 |
| subforms | `Sites\Statut signé EN` | `subforms/Sites/Statut signé EN.dxl` | 902881 |
| views | `AAAA` | `views/AAAA.dxl` | 20737 |
| views | `Admin\Conflits` | `views/Admin/Conflits.dxl` | 18225 |
| views | `Admin\Documents supprimés` | `views/Admin/Documents supprimés.dxl` | 19960 |
| views | `Admin\Postes de travail` | `views/Admin/Postes de travail.dxl` | 4425 |
| views | `Admin\Tous les documents` | `views/Admin/Tous les documents.dxl` | 18346 |
| views | `Base\ Profil DocuSign` | `views/Base/Profil DocuSign.dxl` | 17610 |
| views | `Base\ Profil OneSpanSign` | `views/Base/Profil OneSpanSign.dxl` | 6362 |
| views | `Base\Classeurs Excel types` | `views/Base/Classeurs Excel types.dxl` | 19749 |
| views | `Base\Courriels types` | `views/Base/Courriels types.dxl` | 18778 |
| views | `Base\Exportations` | `views/Base/Exportations.dxl` | 5584 |
| views | `Base\Lettres types` | `views/Base/Lettres types.dxl` | 4677 |
| views | `Base\Tables` | `views/Base/Tables.dxl` | 14205 |
| views | `Propositions\Alertes Historique` | `views/Propositions/Alertes Historique.dxl` | 9129 |
| views | `Propositions\Alertes à traiter` | `views/Propositions/Alertes à traiter.dxl` | 9057 |
| views | `Propositions\Ouvertes par statut client EN` | `views/Propositions/Ouvertes par statut client EN.dxl` | 12832 |
| views | `Propositions\Ouvertes par statut client FR` | `views/Propositions/Ouvertes par statut client FR.dxl` | 12816 |
| views | `Propositions\Par date EN` | `views/Propositions/Par date EN.dxl` | 14420 |
| views | `Propositions\Par date FR` | `views/Propositions/Par date FR.dxl` | 14410 |
| views | `Propositions\Par représentant/Statut/Date EN` | `views/Propositions/Par représentant_Statut_Date EN.dxl` | 16320 |
| views | `Propositions\Par représentant/Statut/Date FR` | `views/Propositions/Par représentant_Statut_Date FR.dxl` | 16309 |
| views | `Propositions\par statut client EN` | `views/Propositions/par statut client EN.dxl` | 13062 |
| views | `Propositions\par statut client FR` | `views/Propositions/par statut client FR.dxl` | 13083 |
| views | `Propositions\Par statut/Auteur EN` | `views/Propositions/Par statut_Auteur EN.dxl` | 13442 |
| views | `Propositions\Par statut/Auteur FR` | `views/Propositions/Par statut_Auteur FR.dxl` | 13431 |
| views | `Propositions\Par statut/Date EN` | `views/Propositions/Par statut_Date EN.dxl` | 15501 |
| views | `Propositions\Par statut/Date FR` | `views/Propositions/Par statut_Date FR.dxl` | 15501 |
| views | `Propositions\Par statut/Dern. maj/auteur EN` | `views/Propositions/Par statut_Dern. maj_auteur EN.dxl` | 13435 |
| views | `Propositions\Par statut/Dern. maj/auteur FR` | `views/Propositions/Par statut_Dern. maj_auteur FR.dxl` | 13352 |
| views | `Propositions\Par statut/Représentant EN` | `views/Propositions/Par statut_Représentant EN.dxl` | 13374 |
| views | `Propositions\Par statut/Représentant FR` | `views/Propositions/Par statut_Représentant FR.dxl` | 13432 |
| views | `Propositions\Par statut/Représentant/Dern. maj. EN` | `views/Propositions/Par statut_Représentant_Dern. maj. EN.dxl` | 14262 |
| views | `Propositions\Par statut/Représentant/Dern. maj. FR` | `views/Propositions/Par statut_Représentant_Dern. maj. FR.dxl` | 14251 |
| views | `Propositions\Par type/Date EN` | `views/Propositions/Par type_Date EN.dxl` | 13597 |
| views | `Propositions\Par type/Date FR` | `views/Propositions/Par type_Date FR.dxl` | 13591 |
| views | `Propositions\Signées par statut client EN` | `views/Propositions/Signées par statut client EN.dxl` | 12840 |
| views | `Propositions\Signées par statut client FR` | `views/Propositions/Signées par statut client FR.dxl` | 12835 |
| views | `Z\Admin\Historiques de réplication 20` | `views/Z/Admin/Historiques de réplication 20.dxl` | 16958 |
| views | `Z\Base\Classeurs Excel types 10` | `views/Z/Base/Classeurs Excel types 10.dxl` | 30201 |
| views | `Z\Base\Classeurs Excel types 20` | `views/Z/Base/Classeurs Excel types 20.dxl` | 29991 |
| views | `Z\Base\Courriels types 10` | `views/Z/Base/Courriels types 10.dxl` | 14560 |
| views | `Z\Base\Courriels types 20` | `views/Z/Base/Courriels types 20.dxl` | 18312 |
| views | `Z\Base\Exportations 10` | `views/Z/Base/Exportations 10.dxl` | 18060 |
| views | `Z\Base\Exportations 10 EN` | `views/Z/Base/Exportations 10 EN.dxl` | 18062 |
| views | `Z\Base\Exportations 20` | `views/Z/Base/Exportations 20.dxl` | 29981 |
| views | `Z\Base\Lettres types 10` | `views/Z/Base/Lettres types 10.dxl` | 32744 |
| views | `Z\Base\Lettres types 20` | `views/Z/Base/Lettres types 20.dxl` | 32302 |
| views | `Z\Base\Profils DocuSign 10` | `views/Z/Base/Profils DocuSign 10.dxl` | 17322 |
| views | `Z\Base\Profils DocuSign 20` | `views/Z/Base/Profils DocuSign 20.dxl` | 16822 |
| views | `Z\Base\Profils OneSpanSign 10` | `views/Z/Base/Profils OneSpanSign 10.dxl` | 6075 |
| views | `Z\Base\Profils OneSpanSign 20` | `views/Z/Base/Profils OneSpanSign 20.dxl` | 5572 |
| views | `Z\Base\Tables 20` | `views/Z/Base/Tables 20.dxl` | 21636 |
| views | `Z\Images 10 EN` | `views/Z/Images 10 EN.dxl` | 20515 |
| views | `Z\Images 10 FR` | `views/Z/Images 10 FR.dxl` | 21731 |
| views | `Z\Produits 11 EN` | `views/Z/Produits 11 EN.dxl` | 25334 |
| views | `Z\Produits 11 FR` | `views/Z/Produits 11 FR.dxl` | 29178 |
| views | `Z\Produits 12 EN` | `views/Z/Produits 12 EN.dxl` | 16244 |
| views | `Z\Produits 12 FR` | `views/Z/Produits 12 FR.dxl` | 16241 |
| views | `Z\Produits 13 EN` | `views/Z/Produits 13 EN.dxl` | 25639 |
| views | `Z\Produits 13 FR` | `views/Z/Produits 13 FR.dxl` | 26843 |
| views | `Z\Produits 14 EN` | `views/Z/Produits 14 EN.dxl` | 16612 |
| views | `Z\Produits 14 FR` | `views/Z/Produits 14 FR.dxl` | 20450 |
| views | `Z\Produits 15 EN` | `views/Z/Produits 15 EN.dxl` | 24821 |
| views | `Z\Produits 15 FR` | `views/Z/Produits 15 FR.dxl` | 27345 |
| views | `Z\Produits 16 EN` | `views/Z/Produits 16 EN.dxl` | 14987 |
| views | `Z\Produits 16 FR` | `views/Z/Produits 16 FR.dxl` | 14985 |
| views | `Z\Produits 17 EN` | `views/Z/Produits 17 EN.dxl` | 23245 |
| views | `Z\Produits 17 FR` | `views/Z/Produits 17 FR.dxl` | 25767 |
| views | `Z\Produits 18 EN` | `views/Z/Produits 18 EN.dxl` | 16338 |
| views | `Z\Produits 18 FR` | `views/Z/Produits 18 FR.dxl` | 20177 |
| views | `Z\Produits 20` | `views/Z/Produits 20.dxl` | 8869 |
| views | `Z\Produits 21` | `views/Z/Produits 21.dxl` | 16500 |
| views | `Z\Produits 22` | `views/Z/Produits 22.dxl` | 16034 |
| views | `Z\Produits 23` | `views/Z/Produits 23.dxl` | 20376 |
| views | `Z\Produits 24` | `views/Z/Produits 24.dxl` | 16154 |
| views | `Z\Produits 25` | `views/Z/Produits 25.dxl` | 20001 |
| views | `Z\Produits 26` | `views/Z/Produits 26.dxl` | 13132 |
| views | `Z\Produits 27 EN` | `views/Z/Produits 27 EN.dxl` | 19661 |
| views | `Z\Produits 27 FR` | `views/Z/Produits 27 FR.dxl` | 22185 |
| views | `Z\Produits 28` | `views/Z/Produits 28.dxl` | 16117 |
| views | `Z\Produits 30` | `views/Z/Produits 30.dxl` | 16441 |
| views | `Z\Produits 31 EN` | `views/Z/Produits 31 EN.dxl` | 21015 |
| views | `Z\Produits 31 FR` | `views/Z/Produits 31 FR.dxl` | 21015 |
| views | `Z\Produits 32` | `views/Z/Produits 32.dxl` | 20323 |
| views | `Z\Produits 33` | `views/Z/Produits 33.dxl` | 16708 |
| views | `Z\Produits 34` | `views/Z/Produits 34.dxl` | 15834 |
| views | `Z\Produits 40` | `views/Z/Produits 40.dxl` | 3394 |
| views | `Z\Produits 40b` | `views/Z/Produits 40b.dxl` | 3156 |
| views | `Z\Produits 41` | `views/Z/Produits 41.dxl` | 17844 |
| views | `Z\Produits 42` | `views/Z/Produits 42.dxl` | 2806 |
| views | `Z\Produits 43 EN` | `views/Z/Produits 43 EN.dxl` | 18888 |
| views | `Z\Produits 43 FR` | `views/Z/Produits 43 FR.dxl` | 22732 |
| views | `Z\Produits 44 EN` | `views/Z/Produits 44 EN.dxl` | 21090 |
| views | `Z\Produits 44 FR` | `views/Z/Produits 44 FR.dxl` | 21650 |
| views | `Z\Produits 50 EN` | `views/Z/Produits 50 EN.dxl` | 28954 |
| views | `Z\Produits 50 FR` | `views/Z/Produits 50 FR.dxl` | 28949 |
| views | `Z\Produits 51 EN` | `views/Z/Produits 51 EN.dxl` | 28939 |
| views | `Z\Produits 51 FR` | `views/Z/Produits 51 FR.dxl` | 28945 |
| views | `Z\Produits 52 EN` | `views/Z/Produits 52 EN.dxl` | 28945 |
| views | `Z\Produits 52 FR` | `views/Z/Produits 52 FR.dxl` | 28951 |
| views | `Z\Produits 53 EN` | `views/Z/Produits 53 EN.dxl` | 28955 |
| views | `Z\Produits 53 FR` | `views/Z/Produits 53 FR.dxl` | 28950 |
| views | `Z\Produits 54` | `views/Z/Produits 54.dxl` | 17866 |
| views | `Z\Propositions 20` | `views/Z/Propositions 20.dxl` | 15047 |
| views | `Z\Propositions 22` | `views/Z/Propositions 22.dxl` | 4856 |
| views | `Z\Propositions 23` | `views/Z/Propositions 23.dxl` | 4169 |
| views | `Z\Propositions 24` | `views/Z/Propositions 24.dxl` | 12767 |
| views | `Z\Propositions\Alertes 21` | `views/Z/Propositions/Alertes 21.dxl` | 3537 |
| views | `Z\Propositions\Images 20` | `views/Z/Propositions/Images 20.dxl` | 16532 |
| views | `Z\Propositions\SI Clients EN` | `views/Z/Propositions/SI Clients EN.dxl` | 20838 |
| views | `Z\Propositions\SI Clients FR` | `views/Z/Propositions/SI Clients FR.dxl` | 20890 |
| views | `Z\Sites 20` | `views/Z/Sites 20.dxl` | 15832 |
| views | `Z\Sites 21` | `views/Z/Sites 21.dxl` | 17147 |
| views | `Z\Sites 22 EN` | `views/Z/Sites 22 EN.dxl` | 14683 |
| views | `Z\Sites 22 FR` | `views/Z/Sites 22 FR.dxl` | 16243 |
| views | `Z\Sites 23` | `views/Z/Sites 23.dxl` | 13858 |
