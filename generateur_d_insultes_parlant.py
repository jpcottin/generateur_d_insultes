#!/usr/local/bin/python
# This Python file uses the following encoding: utf-8
import os,sys,random,time,copy
import pyttsx

insultes=['Abruti' ,'Ahuri' ,'Aigrefin','Anachorète' ,'Analphabète' ,'Andouille' ,'Anus De Poulpe' ,'Arsouille' ,'Aspirateur A Muscadet' ,'Assisté' ,'Asticot' ,'Attardé' ,'Avorton' ,'Babache' ,\
'Bachibouzouk' ,'Balai de Chiottes' ,'Baltringue' ,'Banane' ,'Bandit' ,'Barjot' ,'Batârd' ,'Betterave' ,'Bigleux' ,'Blaireau' ,'Boloss' ,'Bordel' ,'Bordel à Cul' ,'Boudin','Bouffon' ,'Bougre D’âne' ,\
'Bougre D’imbécile' ,'Bougre De Congre' ,'Bougre De Conne' ,'Boule De Pus' ,'Boulet' ,'Bouricot' ,'Bourique' ,'Bourrin' ,'Boursemolle' ,'Boursouflure' ,'Bouseux' ,'Boutonneux' ,'Branleur' ,\
'Branlotin' ,'Branque' ,'Branquignole' ,'Brigand' ,'Brêle' ,'Brosse à Chiottes' ,'Bubon Puant' ,'Burne' ,'Butor' ,'Bécasse' ,'Bégueule' ,'Bélitre' ,'Béotien' ,'Bête' ,'Cageot' ,'Cagole' ,'Calice' ,\
'Canaille' ,'Canaillou' ,'Cancrelat' ,'Caprinophile' ,'Carburateur à Beaujolais' ,'Caribou' ,'Casse-pieds' ,'Cassos' ,'Catin' ,'Cave' ,'Cervelle D’huitre' ,'Chacal' ,'Chacal Puant' ,'Chafouin' ,\
'Chameau' ,'Chancreux' ,'Chancre puant' ,'Chaoui' ,'Charogne' ,'Chenapan' ,'Chiassard' ,'Chiasse De Caca Fondu' ,'Chieur' ,'Chiure De Pigeon' ,'Cinglé' ,'Clampin' ,'Cloaque' ,'Cloche' ,\
'Clodo' ,'Cloporte' ,'Clown' ,'Cochon' ,'Cocu' ,'Con' ,'Conard' ,'Conchieur' ,'Concombre' ,'Connard' ,'Connasse' ,'Conne' ,'Coprolithe' ,'Coprophage' ,'Cornard' ,'Cornegidouille' ,'Corniaud' ,\
'Cornichon' ,'Couard' ,'Couille De Tétard' ,'Couille Molle' ,'Couillon' ,'Crapaud De Pissotière' ,'Crapule' ,'Crassard','Crasspouillard!' ,'Crevard' ,'Crevure' ,'Crotte De Moineau' ,\
'Cryptorchide' ,'Crâne D’obus' ,'Crétin' ,'Crétin Des Alpes' ,'Crétin Des Iles' ,'Crétin Goîtreux' ,'Cuistre' ,'Cul De Babouin' ,'Cul Terreux' ,\
'Dégueulasse' ,'Don Juan De Pissotière' ,'Ducon' ,'Dugenou' ,'Dugland' ,'Dypterosodomite' ,'Débile' ,'Décamerde' ,'Décérébré' ,'Dégueulis' ,'Dégénéré Chromozomique' ,'Dégénéré Du Bulbe' ,'Dépravé',\
'Détritus' ,'Ecervelé' ,'Ectoplasme' ,'Emmerdeur' ,'Empaffé' ,'Emplâtre' ,'Empoté' ,'Enculeur De Mouches' ,'Enculé' ,'Enflure' ,'Enfoiré' ,'Erreur De La Nature' ,'Eunuque' ,'Face De Cul' ,'Face De Pet' ,\
'Face De Rat' ,'Faquin' ,'Faraud' ,'Faux Jeton' ,'Fesse D’huitre' ,'Fesse De Moule' ,'Fesses Molles' ,'Fiente' ,'Filou' ,'Fini à L’urine' ,'Fion' ,'Fiote' ,'Flaque De Pus' ,'Foireux' ,'Foldingue' ,\
'Fonctionnaire' ,'Fouille Merde' ,'Four à Merde' ,'Fourbe' ,'Foutriquet' ,'Frapadingue' ,'Frappe' ,'Freluquet' ,'Fricoteur' ,'Frigide' ,'Fripouille' ,'Frippon' ,'Frustré' ,'Fumier' ,'Fumiste' ,'Furoncle' ,\
'Félon' ,'Ganache' ,'Gangrène' ,'Garage A Bite' ,'Gibier De Potence' ,'Gland' ,'Glandeur' ,'Glandus' ,'Globicéphale' ,'Gnome' ,'Godiche' ,'Gogol' ,'Goinfre' ,'Gommeux' ,'Gougnafier' ,'Goujat' ,'Goulu' ,\
'Gourdasse' ,'Gourgandine' ,'Grand Cornichon' ,'Grand Dépandeur D’andouilles' ,'Gras Du Bide' ,'Graveleux' ,'Gredin' ,'Grenouille' ,'Gringalet' ,'Grognasse' ,'Gros Caca Poilu' ,'Gros Con' ,'Gros Lard' ,\
'Grosse Merde Puante' ,'Grosse Truie Violette' ,'Grue' ,'Gueulard' ,'Gueule De Fion' ,'Gueule De Raie' ,'Gueux' ,'Gugus' ,'Guignol' ,'Has-been' ,'Hérétique' ,'Histrion' ,'Homoncule' ,'Hostie D’épais' ,\
'Hurluberlu' ,'Hérétique' ,'Iconoclaste' ,'Idiot' ,'Ignare' ,'Illettré' ,'Imbibé' ,'Imbécile' ,'Impuissant' ,'Infâme Raie De Cul' ,'Ironie De La Création' ,'Ivrogne' ,'Jaune' ,'Jean-foutre' ,'Jobard' ,\
'Jobastre' ,'Judas' ,'Kroumir' ,'Kéké' ,'Laideron' ,'Larve' ,'Lavedu' ,'Lépreux' ,'Loboto' ,'Loutre Analphabète' ,'Lèche-cul' ,'Malandrin' ,'Malotru' ,'Malpropre' ,'Manant' ,'Manche à Couille' ,\
'Mange Merde' ,'Maquereau' ,'Maquerelle' ,'Maraud' ,'Marchand De Tapis' ,'Margoulin' ,'Merdaillon' ,'Merdasse' ,'Merde' ,'Merde Molle' ,'Merdophile' ,'Merlan Frit' ,'Microcéphale' ,'Minable' ,'Minus' ,\
'Miteux' ,'Moins Que Rien' ,'Molasson' ,'Mongol' ,'Mononeuronal' ,'Mont De Brin' ,'Morbleu' ,'Morfale' ,'Morille' ,'Morpion' ,'Mortecouille' ,'Morue' ,'Morveux' ,'Motherfucker' ,'Mou Du Bulbe' ,\
'Mou Du Genou' ,'Mou Du Gland' ,'Moudlabite' ,'Moule à Gauffre' ,'Mouton De Panurge' ,'Méchant.' ,'Mécréant' ,'Mérule' ,'Nabot' ,'Nain De Jardin' ,'Nanar' ,'Naze' ,'Nazillon' ,'Necropédophile' ,\
'Neuneu' ,'Nez De Boeuf' ,'Niais, Niaiseux' ,'Nigaud' ,'Niguedouille' ,'Noob' ,'Nounouille' ,'Nécrophile' ,'Obsédé' ,'Oiseau De Mauvaise Augure' ,'Olibrius' ,'Ordure Purulente' ,'Outre à Pisse' ,\
'Outrecuidant' ,'Pachyderme' ,'Paltoquet' ,'Panaris' ,'Parasite' ,'Parbleu' ,'Parvenu' ,'Patate' ,'Paumé' ,'Pauvre Con' ,'Paysan' ,'Peau De Bite' ,'Peau De Vache' ,'Pecore' ,'Peigne-cul' ,'Peine à Jouir' ,\
'Pendard' ,'Pervers' ,'Pet De Moule' ,'Petite Merde' ,'Petzouille' ,'Phlegmon' ,'Pigeon' ,'Pignolo' ,'Pignouf' ,'Pimbêche' ,'Pinailleur' ,'Pine D’ours' ,'Pine D’huitre' ,'Pintade' ,'Pipistrelle Puante' ,\
'Piqueniquedouille' ,'Pisse Froid' ,'Pisse-vinaigre' ,'Pisseuse' ,'Pissure' ,'Piètre' ,'Planqué' ,'Playboy De Superette' ,'Pleutre' ,'Plouc' ,'Poire' ,'Poireau' ,'Poivrot' ,'Polisson' ,'Poltron' ,\
'Pompe A Merde' ,'Porc' ,'Pot de chambre', 'Pouacreux' ,'Pouffe' ,'Pouffiasse' ,'Poufieux' ,'Pouilleux' ,'Pourceau' ,'Pourriture' ,'Pousse Mégot' ,'Punaise' ,'Putassière' ,'Pute Au Rabais' ,'Pute Borgne' ,\
'Putréfaction' ,'Pygocéphale' ,'Pécore' ,'Pédale' ,'Péquenot' ,'Pétasse' ,'Pétassoïde Conassiforme' ,'Pétochard' ,'Quadrizomique' ,'Queutard' ,'Quiche' ,'Raclure De Bidet' ,'Raclure De Chiotte' ,\
'Radasse' ,'Radin' ,'Ramassis De Chiure De Moineau' ,'Rambo De Pacotille' ,'Rastaquouère' ,'Renégat' ,'Roquet' ,'Roublard' ,'Rouge' ,'Roulure' ,'Résidu De Fausse Couche' ,'Résidus De Partouze' ,\
'Sabraque' ,'Sac à Brin' ,'Sac à Foutre' ,'Sac à Gnole' ,'Sac à Merde' ,'Sac à Viande' ,'Sac à Vin' ,'Sacrebleu' ,'Sacrement' ,'Sacripan' ,'Sagouin' ,'Salaud' ,'Saleté' ,'Saligaud' ,'Salopard' ,\
'Salope' ,'Saloperie' ,'Salopiaud' ,'Saltinbanque' ,'Saperlipopette' ,'Saperlotte' ,'Sauvage' ,'Scaphandrier D’eau De Vaiselle' ,'Scatophile' ,'Scelerat' ,'Schnock' ,'Schpountz' ,'Serpillière à Foutre' ,\
'Sinistrose Ambulante' ,'Sinoque' ,'Sodomite' ,'Sombre Conne' ,'Sombre Crétin' ,'Sot' ,'Souillon' ,'Sous Merde' ,'Spermatozoide Avarié' ,'Spermiducte' ,'Suintance' ,'Sybarite' ,'Syphonné' ,'Tabarnak' ,\
'Tabernacle' ,'Tâcheron' ,'Tafiole' ,'Tanche' ,'Tartignole' ,'Taré' ,'Tas De Saindoux' ,'Tasse à Foutre' ,'Thon' ,'Tire Couilles' ,'Tocard' ,'Tonnerre De Brest' ,'Toqué' ,'Trainé' ,'Traîne Savate' ,\
'Tricard' ,'Triple Buse' ,'Tromblon' ,'Tronche De Cake' ,'Trou De Balle' ,'Trou Du Cul' ,'Troubignole' ,'Truand' ,'Trumeaux' ,'Tuberculeux' ,'Tudieu' ,'Tétârd' ,'Tête D’ampoule' ,'Tête De Bite' ,\
'Tête De Chibre' ,'Tête De Con' ,'Tête De Noeud' ,'Tête à Claques' ,'Usurpateur' ,'Va Nu Pieds' ,'Va Te Faire' ,'Vandale' ,'Vaurien' ,'Vautour' ,'Ventrebleu' ,'Vermine' ,'Veule' ,'Vicelard' ,\
'Vieille Baderne' ,'Vieille Poule' ,'Vieille Taupe' ,'Vieux Chnoque' ,'Vieux Con' ,'Vieux Fossile' ,'Vieux Tableau' ,'Vieux Tromblon' ,'Vilain' ,'Vilain Comme Une Couvée De Singe' ,'Vioque' ,\
'Vipère Lubrique' ,'Voleur' ,'Vorace' ,'Voyou' ,'Vérole' ,'Wisigoth' ,'Yéti Baveux' ,'Zigomar' ,'Zigoto' ,'Zonard' ,'Zouave' ,'Zoulou' ,'Zozo' ,'Zéro']

#init pyttsx engine
engine = pyttsx.init()
engine.setProperty('rate', 70)

qc_voice= None 
fr_voice= None

voices = engine.getProperty('voices')
for voice in voices:
#    print voice.languages
    if "fr-FR" in voice.languages:
        fr_voice=copy.deepcopy(voice)
    if "fr-CA" in voice.languages:
        qc_voice=copy.deepcopy(voice)
# TODO : we can also exit this loop when we find a fr-FR voice

if fr_voice == None:
    engine.setProperty('voice', qc_voice.id)
else:
    engine.setProperty('voice', fr_voice.id)
# TODO  Have another fallback if not French voice)


# ex the "print voices[5]" would return :
#<Voice id=com.apple.speech.synthesis.voice.amelie
#          name=Amelie
#          languages=[u'fr-CA']
#          age=35>

engine.setProperty('voice', voices[5].id)

random.shuffle(insultes) # shuffle before print 
for ins in insultes:
	print ins
	engine.say (ins.decode('utf-8'))
	engine.runAndWait()
	time.sleep (.6)
