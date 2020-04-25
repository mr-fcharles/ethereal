import streamlit as st


def main():

	from PIL import Image
	import numpy as np
	import pandas as pd

	page = st.sidebar.selectbox("Choose a page", ["Homepage", "Guardando le stelle","Bias","Su di me"])

	####################################### BIO #########################################
	if(page=='Su di me'):
		st.title('About Francis')
		st.markdown('Ed ecco il mio faccione')
		me_image= Image.open('./pics/me.jpg')
		st.image(me_image,use_column_width=True,caption='Io che fingo la padronanza di metodi quantitativi avanzati')


		st.markdown("Mi chiamo Francesco Carli, per gli amici *Francis*, sul playstation network *mrcharles* e sono uno studente"
					" del MSc in Stochastics and Data Science dell'univeristà di Torino. Dopo aver speso gli ultimi due anni della mia vita"
					" a scroccare articoli su *medium* e *towards data science* voglio restiturie qualcosa alla comunità del web lasciando la rete un po' migliore di come l'ho trovata (*chi vuol capire capisce*).")
		st.markdown("In questo piccolo spazio virtuale voglio condividere con voi la mia passione per l'**intelligenza artificale** ed il **machine learning**"
					" pubblicando le visualizzazioni grafiche ed i modelli quantitativi sui quali lavoro/studio. Spero inoltre"
					" di riuscire a convincervi di come la matematica, la statistica e la probabiltà possano essere più *cool* e colorite del temuto metodo di Ruffini imparato alle superiori.")
		st.markdown("Nel Febbraio 2019, insieme ad altri amici, ho vinto il **Milano Critical Care Datathon** a seguito del quale ho dedicato molto tempo allo studio di modelli di machine learning applicabili in campo medico."
					" In particolare ho seguito un progetto finalizzato all'identificazione di pazienti oncologici in una startup legata all'ospedale San Raffaele di Milano e sto collaborando con l'MIT Critical Data Lab alla realizzazione di modelli previsionali per pazienti in cura intensiva. ")
		st.markdown("Non sono sempre stato un **quant**, ho infatti una laurea trienale in Economia e Scienze Sociali all'Università Bocconi di Milano e la mia professoressa di matematica delle superiori"
					", dato il mio coinvolgimento nella rappresentanza studentesca, sosteneva che il mio futuro fosse la politica e non i numeri *(io ve l'ho detto, fate vobis)*.")
		st.markdown("Nel tempo libero amo fare sport, sopratutto correre. Ho anche una passione per la fotografia *(me la cavicchio)* e per la poesia *(sono scarso)*. Ho poi un gruppo di amici intellettuali,"
					" '*I Ragazzi*', che mi sfotteranno a vita per questo blog. Con loro discuto solo di meccanica quantistica e teoria delle stringhe. **Amo i meme**.")

		st.write("\n")

		st.write("\n")

		st.markdown("*Contact me at:*")
		st.markdown("*Mail: francis@mrcharles.cool*")
		st.markdown("*Github: mr-fcharles*")
		st.markdown("*Instagram: mr.francis.charles*")
	#########################################################################################

	##################################### HOME PAGE #########################################
	if(page=='Homepage'):

		st.title('Welcome to the jungle')

		st.markdown("Benvenuto su mrcharles.cool, un posto chad per dank data analysis. Non uscirai qui senza aver rifiutato l'ipotesi nulla che nella tua vita ci sia bisogno di più statistica."
					" Non hai idea di cosa sia un'ipotesi nulla? beh allora sei nel posto giusto.")



		image = Image.open('./pics/kermit.jpg')
		st.image(image,use_column_width=True)

		st.subheader("Cosa potresti/non potresti trovare su mrcharles.cool")
		st.markdown("Questa pagina nasce con l'idea di diffondere in modo *.cool* piccoli articoli divulgativi su Probabilità, Statistica, Machine Learning e Intelligenza Artificiale (rispettivamente ML e AI se sei *swaggy*)")
		st.markdown("\n L'*intensità matematica* degli articoli varierà da post a post, passando da semplici analisi esplorative ai **mega processi stocastici** ai quali l'autore è ormai sentimentalmente legato. "
					"Se la notazione matematica ti spaventa non disperare, in ogni post troverai riquadri verdi come il seguente:")
		st.success(" 'ciao sono un riquadro verde' ")
		st.markdown("dove avrò cura di sintetizzare in lingua corrente i concetti matematici più importanti (*non garantisco di riuscirci ma ci provo*).")
		st.markdown("Indicherò invece con un riqaudro rosso le osservazioni più dettagliate, non strettamente necessarie alla comprensione dei concetti presentati, spunti di riflessione per i più curiosi: **nerd notes**.")
		st.error("'ciao sono un box che contiene roba esoterica'")
		st.markdown("Spesso questi box contengno concetti che verranno affrontati in un apposito post futuro")
		st.markdown("Puoi navigare gli articoli presenti cliccando la freccetta in altro a sinistra e scorrendo le pagine disponibili nel menù a tendina.")
		st.markdown("Dopo questa breve introduzione per settare i vostri *prior* (abbiate pazienza vi spiegherò tutto, se non siete pazienti google è vostro amico) eccovi un piccolo riassunto delle creature nelle quali ci si può imbattere qua dentro.")
		st.markdown("**Cosa puoi trovare:**")
		st.markdown("* Dank data visualization;")
		st.markdown("* Termini inglesi che potevano benissimo essere scritti in italiano (*ma siamo .cool*);")
		st.markdown("* Concetti matematici che non sei pronto ad accogliere nella tua vita, potrebbe non essere amore a prima vista;")
		st.markdown("* Un sacco di informazioni per fare lo sgargiante ad aperitivo ed ai pranzi di famiglia;")
		st.markdown("* **Una marea di meme**")

		image_2 = Image.open('./pics/meme_series.jpg')
		st.image(image_2, use_column_width=True)

		st.markdown("**Cosa non puoi trovare:**")
		st.markdown("* Come contare le carte, diventare ricco a Las Vegas e farti picchiare dal racket dei Casinò;")
		st.markdown("* **Gif animate :( :( :(**, sadly la piattaforma che uso per generare il sito non permette ancora di inserirle;")
		st.markdown("* Un metodo per diventare ricco facendo trading in borsa;")

		image_3 = Image.open('./pics/euforico.jpg')
		st.image(image_3, use_column_width=True)

		st.markdown("Buona lettura")

		st.markdown("*(Ringrazio poi moltissimo Mario Costa. Mario ha avuto la pazienza di seguirmi nella preparazione dell'infrastruttura necessaria alla realizzazione di questo sito, dai DNS alle certificazioni SSL e oltre )*")


	######################################### GUARDANDO LE STELLE ################################
	if (page == 'Guardando le stelle'):

		st.title('Coming soon, really soon')


	######################################## BIAS #############################
	if(page == 'Bias'):

		st.title('Sondaggi, self-selection, confirmation bias, echo chamber')

		image = Image.open('./pics/polls_everywhere.jpg')
		st.image(image,use_column_width=True)

		st.markdown(" Dalla democratizzazione di internet (in particolare dall'avvento dei social network) è diventato molto facile imbattersi "
					" in un **sondaggio** online. Le domande poste agli (spesso annoiati) internauti possono essere le più disparate:")

		st.markdown("* Quale di questi prodotti saresti disponibile a comprare?")
		st.markdown("* Cosa ne pensi dell'auttuale governo? ")
		st.markdown("* Esiste la vita dopo la morte?")
		st.markdown("* Qu4LE v3rdURa Ti SENTI di raPPresentaRe oGGI?!1?")

		st.markdown("Insomma un sacco di persone sembrano interessate tua opinione. Ad alcuni, in realtà, non frega una beata della tue idee: "
					" vogliono profilarti, capire le tue abitudini di consumo e venderti il nuovo *olio di palma al cardamomo bio vegan*.")

		st.markdown(" Per ognuno di questi dentiaguzzi esiste poi un numero aleatorio (compreso tra il 3 e il 5) di tesisti, giornalisti e studenti di materie quantitative allo stato brado "
					"genuinamente interessati a capire cosa ne pensi del mondo che ti circonda. Spesso l'obiettivo di queste simpatiche creature è raccogliere le opinioni altrui, sintettizzarle calcolando qualche statistica"
					", fare dei grafici per presentare in modo intuitivo ciò che i dati ottenuti evidenziano.")

		st.markdown("Fino a qui tutto bene. Non sono apparse formule, non ho ancora tirato fuori uno *stochastics.*")

		image2 = Image.open('./pics/che_succede.jpg')
		st.image(image2, use_column_width=True)

		st.subheader("Il ruolo delle ipotesi")

		st.markdown("Recentemente ho avuto il piacere di condurre un piccolo sondaggio su un tema un po' insolito per il mio percorso accademico: l'astrologia (non l'astronomia, quella è un'altra cosa, guarda [qui](https://it.wikipedia.org/wiki/Astronomia)) ")

		st.warning(" Se non hai fatto il sondagio sei un infame, ma puoi diventare meno infame compilandolo adesso [qui](https://forms.gle/5tteZmUYXwNKCfe59) ")

		st.markdown("Appena la prima cinquantina di responsi sono arrivati mi sono reso conto che, prima di presentare i risultati, avrei dovuto fare quello che ogni statistico un filo navigato fa prima di arrivare a conclusioni che potrebbero rivelarsi errate in futuro: pararsi il deretano con le ipotesi. La maggior parte dei modelli quantitativi (se non tutti) richiedono che alcuni 'requisiti minimi' siano rispettati affinché il passaggio da raccolta dati alle conclusioni sia solido dal punto di vista logico. Possiamo concretizzare questa situauzione nella vita di tutti i giorni con il nostro primo box verde:")
		st.success("**Ipotesi**: devo andare con una macchina da Mantova a Milano. Una delle ipotesi che deve essere rispettata (chiaramente ce ne sono delle altre) affinché mi sia possibile affrontare il viaggio è che io abbia sufficiente benzina. Possiamo quindi vede le ipotesi come la benzina del nostro motore, ciò che permette alla nostra macchina funzioni a dovere. No ipotesi rispettate, no viaggio.")

		st.markdown("Esiste però un'importante dicotomia dal caso concreto sopra riportato: se non c'è la benzina la macchina non partirà, se le ipotesi non sono rispettate non esiste alcuna legge fisica che impedisca al modello di sputare fuori qualche numero lo stesso. Otterremo quindi comunque dei risultati, ma risultati verosimilmente errati e non attendibili. ")

		st.subheader("Un esempio istruttivo")

		st.markdown("Prima di arrivare al pezzo forte di questo articolo, diventa necessaria una pratica che manderà in bestia il lettore non matematico medio: *ipotizzare una situazione astratta e sconnessa dalla realtà sulla quale ragionare*. Un po' tipo quei problemi delle superiori in cui un tizio compra 200 banane e vuole scambiarle con 1.73 pesci rossi")

		image3 = Image.open('./pics/banana.jpg')
		st.image(image3, use_column_width=True,caption='il tizio con le banane')

		st.markdown("Per coaudivare la comprensione generale, cercherò di rendere il problema più attuale e concreto di quello sopra citato. Anzi, mi voglio rovinare, la rendero una situazione di *vita o morte*. Considerate il seguente contesto:")

		st.markdown("*Siete fuori a far aperitivo (e già qui siamo sull'astratto spinto data la situazione attuale). Il vostro amico Kevin vi propone la seguente scommessa: si sceglie testa o croce, si lancia la monetina, chi perde offre un Negroni all'altro.*")

		st.markdown("Spero siate d'accordo con me nell'osservare che lo scenario sopra dipinto delinei *nettamente* una situazione di vita o morte. Ora siete disposti a tutto pur di avere quel Negroni gratis.")

		st.markdown("Ci ricordiamo inoltre che Kevin è un fandamentalmente un infame (il classico amico che shoppava su candycrush per dare la merda agli alti). Questa cosa ci fa salire il cospirazionismo all'istante: **Kevin è amico dei poteri forti**, avrà sicuramente una monetina truccata.")

		st.markdown("Decidete quindi di accettare la scommessa ad una sola condizione: la possibilità di verificare che la moneta non sia truccata, detta in modo cool, che sia una *fair coin*. Rimane ora il problema di come verificare che la moneta sia effettivamente *fair*, ci tocca fare qualche conto.")

		st.markdown("L'idea è la seguente: lanciamo la moneta un numero predefinito di volte (che denoteremo con $N_{tot}$) e vediamo quante volte esce testa rispetto al totale dei lanci ($N_{head}$). Possiamo quindi *stimare* la probabilità che lanciando la moneta esca testa come:")

		st.markdown("*Probabilità stimata testa:* $\\hat\\theta = \\frac{N_{head}}{N_{tot}}$")

		st.markdown("Poichè gli *outcome* possibili (gli esiti) della moneta sono due (testa o croce) avremo che tutti i lanci non testa dovranno necessariamente essere stati croce, quindi la stima della probabilità che esca croce sarà ")

		st.markdown("*Probabilità stimata croce:* $1 -\\hat\\theta = 1- \\frac{N_{head}}{N_{tot}}$")

		st.error("**Nerd note**: osserva si stia parlando di una *stima della probabilità* e non di probabilità. Facendo tendere $N_{tot}$ verso l'infinito otteniamo la definizione *freqeuntista* di probabilità $P(testa)=\\lim_{N_{tot} \\rightarrow \\infty} \\frac{N_{head}}{N_{tot}}$. Esistono diverse interpretazioni di probabilità e torneremo su questo tema in futuro.")


		st.markdown("Visto che lanciare mille volte una moneta potrebbe risultare una pratica time consuming (anche se indubbiamente affascinante), Francis ha programmato un simulatore di lanci di monetine qui sotto, tutto per te.")

		image4 = Image.open('./pics/future.jpg')
		st.image(image4,use_column_width=True,caption='quando dici a Kevin che sei in grado di simulare il lancio di 1000 monetine in una frazione di secondo')

		st.markdown("Prima di avviare questa gloriosa simulazione devi impostare due parmetri:")
		st.markdown("* **Probabilità testa effettiva**: se la moneta di Kevin non fosse truccata la probabilità di testa sarebbe 0.5 (50%). Tutti gli valori favoriscono maggiormente un outcome rispetto all'altro")
		st.markdown("* **Numero di lanci:** prova a giocare con questo parametro e osserva come varia la stima all'aumentare dei lanci")

		prob_head = st.slider('Probabilità testa', min_value=0.01, max_value=1.0, step=0.01)
		n_throws = st.slider('Numero lanci',min_value=1,max_value=2500,step=20)

		if st.button('Lancia le monete!'):

			coin_tosses = np.array([])
			running_mean = np.array([])

			for i in range(n_throws):

				coin_tosses =np.append(coin_tosses,np.random.choice([1,0],p=[prob_head,1-prob_head],size=1))
				running_mean =np.append(running_mean,np.mean(coin_tosses))

			#lanci = np.random.choice([1,0],p=[prob_head,1-prob_head],size=n_throws)

			n_heads = sum(coin_tosses)
			n_tails = n_throws - n_heads

			prob_head_estimate = n_heads / n_throws
			prob_tail_estimate = n_tails / n_throws

			lanci = np.where(coin_tosses==1,'Testa','Croce')
			st.write(lanci)

			st.write("Numero monete testa:",n_heads, "	Numero monete croce:",n_tails)
			st.write("Stima probabilità testa:",np.round(prob_head_estimate,decimals=2),"	Stima probabilità croce:",np.round(prob_tail_estimate,decimals=2))
			st.write("Probabilità testa effettiva:",prob_head,"Probabilità croce effettiva",1-prob_head)

			st.markdown("*Il grafico qui sotto riporta sull'asse orizzontale il numero di monetine lanciate, sull'asse verticale la stima della probabilità corrispondente a quel numero di lanci. Osserva come, all'aumentare del numero"
						"di moentine lanciate, la stima converge velocemente verso l'effetiva probabilità di testa (rappresentato dalla linea orizzontale)*")

			real_value = np.array([prob_head for i in range(len(running_mean))])

			graph_data = pd.DataFrame(columns=['Stima','Valore effettivo'])
			graph_data['Stima'] = running_mean
			graph_data['Valore effetivo'] = real_value

			st.line_chart(graph_data)




		df,qname_dict = load_stars()

		#st.dataframe(df)


@st.cache
def load_stars():

	import pandas as pd
	import json

	df =pd.read_csv('data/stars_out.csv',index_col=0)
	with open('data/qname_dictionary.json', 'r') as fp:
		qname_dict = json.load(fp)

	return (df,qname_dict)


if __name__ == '__main__':
	main()




