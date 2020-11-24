all_btn = [ 'PROGRAMATION', 'PROFESSORAT', 'DIRECTION', 'ANIMATION', 'AUTRES']
all_success = [
"Travailler en tant que développeur,", 
"Finir ma formation de développeur Python/Django,", 
"Vivre un an dans une base militaire,",
"Réaliser un Poitiers - Kaunas(Lituanie) à vélo,", 
"Réussir mes oraux de licence devant un jury russophone,",
"Devenir directeur de centre de vacances,",
"Apprendre à danser,", 
"Obtenir mon <a href='https://www.nageur-sauveteur.com/BNSSA'>BNSSA,</a>",
"Traverser la France à moto,"
]
exp_prof = [
{
'category': 'cat4',
'job': "Intérimaire (FR24)",
'url': 'https://www.proman-emploi.fr/agences/bergerac' ,
'employer': 'Proman Bergerac', 
'period': 'en cours depuis octobre 2019' ,
'description': '''Toutes sortes de missions ne demandant pas de qualifications, que je tiens à faire pour gagner ma vie sans avoir recours aux prestations sociales. Je les ai cumulées avec les heures de formation en développement d'application. <span class="imp"> Cela me permet de gader un contact avec la réalité et de me rappeler d'où je viens.</span>''' },
{
'category': 'cat0',
'job': "Développeur d'App Python Django (FR24)",
'url': 'https://www.spa24bergerac.org/' ,
'employer': 'Spa de Bergerac', 
'period': 'juillet - octobre 2020' ,
'description': '''Expérience de développeur d'applications Python/Django. J'ai démarché par téléphone des clients,  jusqu'à avoir un rendez-vous. Pendant l'entretien j'ai analysé les besoins du clients. Je me suis entendu avec celui-ci sur un produit à concevoir. Je suis resté en contact pendant la conception en organisant des appels et des rencontres. J'ai livré de manière hebdomadaire mon travail à la fin de chaque sprint.<span class="imp"> L'interaction avec le client a été la partie la plus difficile mais aussi la plus formatrice.</span>''' },
{
'category': 'cat1',
'job': 'Professeur de Français Langue Etrangère (Ge)' ,
'url': 'https://ge.ambafrance.org/' ,
'employer': 'Ambassade de france en Géorgie', 
'period': 'octobre 2018 - juillet 2019' ,
'description': '''Expérience de vie en Géorgie en base militaire. Langue parlée au quotidien : anglais ou russe. Emploi en qualité de professeur de langue dans trois bases avec des niveaux différents pour chaque classe. Le poste m'a demandé de m'adapter à un environnement militaire avec un emploi du temps évolutif. J'ai aussi fait passer des examens de langues de niveau A1 à B2. <span class="imp"> J'en retiens l'importance de la probité dans la vie à plusieurs et la camaraderie d'une base militaire.</span>'''
},
{
'category': 'cat0',
'job': 'Concepteur Pédagogique (FR38)' ,
'url': 'https://www.afgrenoble.org/fr/' ,
'employer': 'Alliance Française de Grenoble', 
'period': 'mars 2018 - juin 2018' ,
'description': '''Stage de conception pédagogique. J'ai mis en place un parcours pédagogique pour un niveau faux débutant intermédiaire (A2). Il m'a été demandé de former les agents à l'utilisation d'une plateforme (<a href='https://apolearn.com/'>Apolearn</a>), de créer un parcours avec eux et d'utiliser mes compétences en programmation pour faire des "compléments d'apprentissage" sous forme de petits jeux.<span class="imp"> J'en ai gardé une très bonne impression et l'envie de continuer à m'investir dans le rôle de technicien.</span>'''
},
{
'category': 'cat4',
'job': 'Agent de service de restauration (FR38)' ,
'url': 'https://www.crous-grenoble.fr/restaurant/ru-diderot/' ,
'employer': 'Restauration Universitaire CROUS', 
'period': 'février 2018 - juin 2018' ,
'description': '''Emploi en qualité d'agent de service de restauration. Service des plats, gestion de l'approvisionnement, plonge, caisse, préparation des boissons J'en garde une bonne capacité d'accueil et de bienveillance envers les clients ainsi qu'une grande polyvalence.'''
}, 
{
'category': 'cat2' ,
'job': 'Directeur adjoint de centre de vacances (FR63)' ,
'url': 'https://www.gocolo.fr/"' ,
'employer': 'GoColo' ,
'period': 'août 2017' ,
'description': '''Directeur adjoint sur un centre d'environ 80 enfants (6-12 ans), avec une équipe encadrante de 6 personnes. Mes attributions étaient la gestion de mon équipe, la logistique, le suivi du projet d'animation et des règles de sécurité.<span class="imp"> J'en retire une amélioration de ma capacité de résolution de conflits dans une équipe.</span>
''' 
},
{
'category': 'cat2',
'job': 'Directeur adjoint/Assistant Sanitaire(FR33)' ,
'url': 'https://www.ccgpfcheminots.com/',
'employer': "Colo SNCF",
'period': 'Juillet 2017',
'description': '''80% directeur adjoint / 20% assistant sanitaire. Mes attributions sur ce poste étaient majoritairement d'ordre sanitaire que ce soit pour les enfants ou adultes avec la gestion de l'infirmerie et la réalisation de commande de matériel non alimentaire pour le centre. Mon rôle de directeur adjoint a consisté ici à accompagner la directrice et à mener certaines réunions.<span class="imp"> J'ai développé au cours de cette expérience une capacité à alterner entre des postures d'autorité, pédagogique, amusante ou rassurante pour répondre aux situations.</span>'''
},
{
'category': 'cat1' ,
'job': 'Professeur de Français Langue Etrangère (Ru)' ,
'url': 'http://www.afrus.ru/fr/saratov' ,
'employer': 'Alliance française de Saratov' ,
'period': 'octobre 2016 - juin 2017' ,
'description': '''Première réelle prise de poste en tant que professeur de langue dans un contexte russophone. J'ai organisé mes cours moi-même sans formation préalable et j'ai appris de mes erreurs et des retours que j'ai demandé sur mon travail. J'ai participé à des conférences sur ce métier et n'ai pas hésité à aller demander de l'aide à mes pairs plus expérimentés. L'absence de ressources pédagogiques récentes m'a amené à créer mes propres outils en utilisant mes premières connaissances du web : HTML, CSS, Javascript. <span class="imp"> J'ai apris pendant cette expérience à planifier mes cours sur plusieurs mois et à créer des ressources pédagogiques numériques.</span>'''
},
{
'category': 'cat2' ,
'job': 'Directeur centre de vacances (FR89)' ,
'url': 'https://avl.fr/' ,
'employer': 'Animation Vacances Loisir' ,
'period': 'Juillet 2016' ,
'description': '''Premier poste de direction, je me suis occupé de tout sur le centre, à l'exception de la livraison des denrées alimentaires, ce qui signifie : anticipation du séjour, montage du centre (hébergement marabout), recrutement de l'équipe, élaboration du projet pédagogique, location véhicule, prise de contact avec les services locaux (médecin, pharmacie, mairie ...), gestion du matériel pédagogique,	gestion du budget alloué, gestion de l'équipe, du contact avec les parents, ... 4 semaines sans sommeil, de loin l'expérience professionnelle la plus difficile mais aussi la plus formatrice.<span class="imp"> J'ai développé au cours de cette expérience une capacité à avoir une vision globale pour prendre des décisions et à organiser mon temps sans me laisser surprendre.</span>'''
},
{
'category': 'cat4' ,
'job': 'Barman (FR63)' ,
'url': 'http://www.le1513.com/' ,
'employer': 'Crêperie le 1513' ,
'period': 'septembre 2015 - novembre 2015' ,
'description': '''Poste de barman dans une crêperie, j'ai préparé des commandes et j'ai aussi fait du service. L'équipe était assez restreinte et les commandes devaient être réalisées très rapidement. <span class="imp"> J'ai appris à garder la tête froide dans les situations de stress.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur moto (FR27)' ,
'url': 'href="https://www.telligo.fr/a-fond-les-manettes"' ,
'employer': 'Telligo' ,
'period': 'Août 2015' ,
'description': '''Poste d'animateur en séjour spécialisé sport mécanique où j'ai assisté le prestataire sport mécanique pendant ses séances. Mon rôle a aussi été de préparer les enfants en amont en les aidant à anticiper la difficulté mais aussi à gérer leurs peurs. Cela demandait de prendre en compte leur rythme. De plus étant l'animateur le plus expérimenté j'ai dû prendre sous mon aile un stagiaire.<span class="imp"> J'ai amélioré ma compréhension du rythme de chacun et j'ai découvert le mentorat pendant un mois.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur itinérance (FR64)' ,
'url': 'www.laligue38.org/nos-colonies-de-vacances' ,
'employer': "La ligue de l'enseignement" ,
'period': 'Juillet 2015' ,
'description': '''Poste d'animateur en séjour en itinérance avec une vingtaine d'adolescents, 2 vans et des tentes. Le séjour s'est déroulé dans le pays Basque. La directrice a fait appel à moi dans plusieurs situations délicates me donnant envie de devenir directeur à mon tour. <span class="imp"> J'ai pris conscience qu'il était temps de regarder vers la direction.</span>'''
},
{
'category': 'cat4' ,
'job': 'Employé agricole (All)' ,
'url': 'https://wwoof.de/' ,
'employer': 'Wwoofing Allemagne' ,
'period': 'Juin 2015' ,
'description': '''J'ai travaillé dans une ferme agricole biologique en Allemagne près de Hanovre. J'ai fait du maraîchage et des travaux de construction. J'ai passé un mois avec des personnes très différentes de celui que j'étais, je m'y suis adapté et cela m'a amené à prendre conscience de mon mode de vie.<span class="imp"> J'en ai gardé l'habitude de me lever de bonne heure et de travailler tous les jours .</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur Ski (FR74)' ,
'url': 'www.montreuil.fr/education-jeunesse/sejours-de-vacances' ,
'employer': 'Ville de Montreuil' ,
'period': 'Février 2015' ,
'description': '''Poste d'animateur spécialisé ski pour jeunes issus de milieu défavorisé. Le directeur avait pris le parti de poser un cadre souple, pour une équipe qui avait besoin d'être accompagnée.<span class="imp"> J'ai pu expérimenter qu'une situation où le cadre est fixé avant la prise en compte de l'équipe crée rapidement des difficultés.</span>'''
},
{
'category': 'cat4' ,
'job': 'Agent service restauration (FR63)' ,
'url': 'https://usine.crous-clermont.fr/restauration/' ,
'employer': 'Restaurant Universitaire Crous',
'period': 'septembre 2014 - décembre 2014',
'description': '''Poste de plongeur au sein des cuisine du Restaurant Universitaire de Clermont-Ferrand. <span class="imp"> J'ai pu vivre une situation d'auto gestion ratée en l'absence de chef.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur Roller (FR33)' ,
'url': 'http://www.laligue33.org/' ,
'employer': "La Ligue de l'Enseignement" ,
'period': 'Juillet 2014' ,
'description': '''Poste d'animateur spécialisé qui m'a demandé de préparer des cours pratiques mais aussi d'arriver à intégrer les adultes accompagnateurs. Colo assez spéciale avec beaucoup plus de problèmes de vie en collectivité que précédemment.<span class="imp"> J'en retiens l'importance d'une direction cohérente et unie lorsque la situation s'envenime.</span>'''
},
{
'category': 'cat4' ,
'job': 'Agent service de restauration (FR31)' ,
'url': 'https://www.crous-toulouse.fr/restauration//' ,
'employer': 'Restaurant Universitaire Crous' ,
'period': 'mars 2014 - juillet 2014' ,
'description': '''Mon premier poste dans une cuisine, j'y ai fait de la plonge et du nettoyage.<span class="imp"> J'y ai développé des compétences sanitaires et une exigence de la propreté.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur Ski (FR38)' ,
'url': 'http://www.laligue38.org/' ,
'employer': "La Ligue de l'Enseignement" ,
'period': 'février 2014' ,
'description': '''Poste d'animateur spécialisé ski pour jeunes issus de milieu défavorisé. Colo demandant un fort investissement physique : 6h de ski par jours avec seulement 4h de sommeil par nuit sur un mois.<span class="imp"> J'ai pris conscience que mes capacités physiques étaient bien meilleures que ce que j'imaginais.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur colo adaptée (FR73)' ,
'url': 'https://www.anae.asso.fr/qui-sommes-nous/association-anae-vacances-accessibles/' ,
'employer': 'Association ANAE' ,
'period': 'Décembre 2013' ,
'description': '''Poste d'animateur spécialisé handicap pour la période de Noël. J'ai passé ce séjour hivernal à apporter bonheur et réconfort à des personnes handicapées moteur le plus souvent sans famille.<span class="imp"> J'ai découvert la prise en charge du handicap et que ce n'était pas pour moi.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur (FR85)' ,
'url': 'http://www.gentiane-en-piste.fr/' ,
'employer': 'Gentiane en piste' ,
'period': 'août 2013' ,
'description': '''Poste d'animateur dans un grand centre au bord de la mer près de la presqu'île de Noirmoutier. J'y ai réalisé mes premiers convoyages (partir seul généralement pour récupérer des enfants à l'autre bout de la France et les amener au centre). C'était un séjour où les enfants et les équipes changeaient chaque semaine mais j'appartenais à l'équipe permanente	qui assurait la continuité. <span class="imp"> J'ai beaucoup appris sur l'animation et sur la relation animateur - prestataire.</span>'''
},
{
'category': 'cat4' ,
'job': 'Employé de grande distribution (FR33)' ,
'url': 'https://www.carrefour.fr/magasin/market-bordeaux-ferryv' ,
'employer': 'Carrefour Market' ,
'period': 'mai 2011 - août 2013' ,
'description': '''Poste d'employé chez carrefour en contrat étudiant pendant mes années de licence de psychologie.<span class="imp"> J'y ai appris à m'auto-discipliner et à me lever chaque matin le week-end de bonne heure.</span>'''
},
{
'category': 'cat3' ,
'job': 'Animateur (FR43)' ,
'url': 'http://www.lepetitprince.asso.fr/' ,
'employer': 'Association le Petit Prince' ,
'period': 'août 2012' ,
'description': '''Premier poste en animation et première fois que je quittais la Gironde seul. Colo basée sur la communication non violente et la mixité sociale.<span class="imp"> J'en retiens une grande partie de mes compétences de communication mais aussi mon goût prononcé pour la colo.</span>'''
},
]

educ= [
{

'category' : 'cat5',
'degree' : "Développeur d'applications Python/Django",
'url': 'https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python',
'text_url': "OpenClassrooms",
'thematic': "Programmation", 
'level': "Diplôme niveau 6 (Bac+3/4)",
'description': """ <ul class="projects">
	<span class="">Voici mes projets (retouvables sur github)</span>

	<li class=""><a href="#">projet13 - site pour la SPA</a></li>
	<li class="">projet12 - Construction d'un outil de veille</li>
	<li class="">projet11 - Amélioration + Tests de mon App du projet 8 </li>
	<li class="">projet10 - Déploiement de mon App du projet 8</li>
	<li class="">projet9 - Documentation d'une application fictive</li>
	<li class=""><a href="#">projet8 - Site web avec Django</a></li>
	<li class=""><a href="#">projet7 - Chat avec Flask</a></li>
	<li class="">projet6 - Rédaction dossier spécifications techniques</li>
	<li class="">projet5 - Importer des données d'une api dans une base de données <br>relationnelle</li>
	<li class="">projet4 - Rédaction dossier spécification fonctionnelle, diagramme UML</li>
	<li class="">projet3 - Mini jeu en pygame (POO)</li>
	<li class="">projet2 - Découverte github</li>
	<li class="">projet1 - Projet de bienvenue</li></ul>""", 
'period': "mai 2019 - oct 2020",
},
{
'category' : 'cat6',
'degree' : "Diplôme de Concepteur Pédagogique Numérique " ,
'url': "http://formations.univ-grenoble-alpes.fr/fr/catalogue/master-XB/arts-lettres-langues-ALL/master-didactique-des-langues-program-master-didactique-des-langues/parcours-didactique-des-langues-et-ingenierie-pedagogique-numerique-dilipem-subprogram-parcours-didactique-des-langues-et-ingenierie-pedagogique-numerique.html",
'text_url': 'Université Grenoble Alpes',
'thematic': "DILIPEM" , 
'level': "Maîtrise",
'description': """<p class="text">Durant cette année j'ai réalisé des projets de conception pédagogique pour l'Université mais aussi dans le cadre d'un stage à l'Alliance Française de Grenoble. Lors de l'un d'eux j'ai conçu un site web en html, css, javascript et php qui hébergeait des ressources et exercices pédagogiques.</p>
<p class="text">L'enseignement universitaire ne me m'apportant pas ce dont j'avais besoin j'ai préféré ne pas continuer en Master 2.</p>""", 
'period': "2017 - 2018",
},
{
'category' : 'cat7',
'degree' : "Diplôme de langue Russe",
'url': "https://lcc.uca.fr/formation/licence/licence-langues-litteratures-civilisations-etrangeres-et-regionales/licence-llcer-parcours-russe--36306.kjsp",
'text_url': 'Université Clermont-Ferrand - Blaise Pascal',
'thematic': "Linguistique", 
'level': "Licence",
'description': """<p class="text">Pendant cette licence j'ai appris à parler russe courrament, à étudier une culture et une langue.J'ai aussi participé à des cours sur l'enseignment du français langue étrangère.</p> <p class="text">La troisième année je suis parti en Russie pour y rester 10 mois.</p>""" , 
'period': "2014 - 2017",
},
{
'category' : "cat8",
'degree' : "Diplôme de Psychologue",
'url': "https://ufr-psycho.univ-tlse2.fr/accueil/navigation/l-ufr-de-psychologie/presentation-de-l-ufr/",
'text_url': 'Université Toulouse 2 - Jean Jaurès',
'thematic': "Psychologie", 
'level': "Licence",
'description': """<p class="text">De cette dernière années en Psychologie j'ai retenu des connaissances pycho-sociales, pycho-conitives et neurobiologiques (mémoire et motivation), que je mobilise encore dans mon quotidien, que ce soit pour mes cours ou pour mon développement personnel.</p>""", 
'period': "2013 - 2014",
},
{
'category' : "cat8",
'degree' : "Diplôme de Psychologue",
'url': "https://jechoisis.u-bordeaux.fr/Choisir/Sciences-humaines-et-sociales/Licence-de-Psychologie",
'text_url': 'Université Bordeaux 2 - Victor Segalen',
'thematic': "Psychologie" , 
'level': "Licence",
'description': """<p class="text">J'ai découvert l'Université, l'autonomie et l'organisation du travail personnel, mais aussi comment raisonner, argumenter, rédiger et chercher des informations en croisant mes sources.</p>""" , 
'period': "2011 - 2013",
},
]
skills =[ 
{
"id" : "js", 
"title": "Javascript", 
"level": "6", 
"done": "Je peux lire et écrire du code en Javascript, gérer des frameworks, je connais et j'utilise JQuery, je comprends et sais utiliser AJAX.", 
"to_do": "Je veux apprendre ReactJS et mieux comprendre le fonctionnement de NodeJS.",
}, 
{
"id" : "python", 
"title": "Python", 
"level": "8", 
"done": "Je peux faire à peu près tout ce que je veux avec python car je sais chercher l'information, me former et appliquer. ", 
"to_do": "Arrêter de tout faire 'from scratch' et réinventer sans cesse la roue, pour cela je dois améliorer ma connaissances des librairies existantes.",
}, 
{
"id" : "django", 
"title": "Django", 
"level": "8", 
"done": "J'ai une vision globale de ce framework au sens où j'ai compris les settings, comment déployer mes apps, comment utiliser le 'matériel' à disposition.", 
"to_do": "Apprendre à modifier le 'matériel' à disposition, ou encore à en créer de nouveau. ",
}, 
{
"id" : "deployment", 
"title": "Déploiement", 
"level": "4", 
"done": "Je me considère encore débutant même si je connais suffisamment AWS pour déployer mes apps, de même pour Heroku. J'ai aussi compris comment utiliser Nginx, Gunicorn, Travis, Sentry, Git. Je débute avec Docker mais j'ai compris son intérêt.", 
"to_do": "Me développer avec Docker et améliorer ma compréhension d'AWS. Déployer une app sur un autre cloud, DigitalOcean par exemple.",
}, 
{
"id" : "sql", 
"title": "SQL", 
"level": "8", 
"done": "Je maîtrise le fonctionnement des bases de données de manières générale, je connais les fonctionnalités avancées pour organiser ses tables mais aussi créer des profils utilisateurs avec des règles précises. Les deux que j'utilise le plus sont MySQL et PostgreSQL.", 
"to_do": "Je dois encore découvrir le NoSQL en faisant un projet avec pour me familiariser.",
}, 
{
"id" : "sass", 
"title": "HTML/CSS/SASS", 
"level": "6", 
"done": "Je connais bien ces trois technologies. Je continue à me former sur SASS même si je connais les fonctionnalités de base, je sais comment utiliser les variables, les mixins, passer du SCSS en SASS.",
"to_do": "Je cherche à rendre mon travail plus fluide en ajoutant des amélioration.",
}]
ten_spans = """
<span>&nbsp;</span>
<span>&nbsp;</span>
<span>&nbsp;</span>
<span>&nbsp;</span>
<span>&nbsp;</span>     
<span>&nbsp;</span>
<span>&nbsp;</span>
<span>&nbsp;</span>
<span>&nbsp;</span>
<span>&nbsp;</span>"""
"""templates 
	exp >>
	{
		'category': '' ,
		'job': '' ,
		'url': '' ,
		'employer': '' ,
		'period': '' ,
		'description': ''''''
	},
	educ >>
	{
		'degree' : ,
		'url': ,
		'text_url': '',
		'thematic': , 
		'level': ,
		'description': , 
		'period': ,
	},
	skill >>
	{
		"id" : "", 
		"title": "", 
		"level": "", 
		"done": "", 
		"to_do": "",
	}
"""