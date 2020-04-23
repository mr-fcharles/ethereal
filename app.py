import streamlit as st


def main():

	from PIL import Image

	page = st.sidebar.selectbox("Choose a page", ["Homepage", "Guardando le stelle","Su di me"])

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

	#########################################################################################

	##################################### HOME PAGE #########################################
	if(page=='Homepage'):

		st.title('Welcome to the jungle')

		st.markdown("Benvenuto su mrcharles.cool, un posto chad per dank data analysis. Non uscirai qui senza aver rifiutato l'ipotesi nulla che nella tua vita ci sia bisogno di più statistica."
					" Non hai idea di cosa sia un'ipotesi nulla? beh allora sei nel posto giusto.")



		image = Image.open('./pics/kermit.jpg')
		st.image(image,use_column_width=True)

		st.subheader("Cosa potresti/non potresti trovare su mrcharles.cool")
		st.markdown("Questa pagina nasce con l'idea di divulgare in modo *.cool* piccoli articoli divulgativi su Probabilità, Statistica, Machine Learning e Intelligenza Artificiale (rispettivamente ML e AI se sei *swaggy*)")
		st.markdown("\n L'*intensità matematica* degli articoli varierà da post a post, passando da semplici analisi esplorative ai **mega processi stocastici** ai quali l'autore è ormai sentimentalmente legato. "
					"Se la notazione matematica ti spaventa non disperare, in ogni post troverai riquadri verdi come il seguente:")
		st.success(" 'ciao sono un riquadro verde' ")
		st.markdown("dove avrò cura di sintetizzare in lingua corrente i concetti matematici più importanti (*non garantisco di riuscirci ma ci provo*)")
		st.markdown("Puoi navigare gli articoli disponibili cliccando la freccetta in altro a sinistra e scorrendo le pagine disponibili nel menù a tendina.")
		st.markdown("Dopo questa breve introduzione per settare i vostri *prior* (abbiate pazienza vi spiegherò tutto, se non siete pazienti google è vostro amico) eccovi un piccolo riassunto delle creature nelle quali ci si può imbattere quà dentro.")
		st.markdown("**Cosa puoi trovare:**")
		st.markdown("* Dank data visualization;")
		st.markdown("* Termini inglesi che potevano benissimo essere scritti in italiano (*ma siamo .cool*);")
		st.markdown("* Concetti matematici che non sei pronto ad accogliere nella tua vita, potrebbe non essere amore a prima vista;")
		st.markdown("* Un sacco di informazioni per fare lo sgargiante ad aperitivo ed ai pranzi di familgia;")
		st.markdown("* **Una marea di meme**")

		image_2 = Image.open('./pics/meme_series.jpg')
		st.image(image_2, use_column_width=True)

		st.markdown("**Cosa non puoi trovare:**")
		st.markdown("* Come contare le carte, diventare ricco a Las Vegas e farti picchiare dal racket dei Casinò;")
		st.markdown("* **Gif animate :( :( :(**, sadly la piattaforma che uso per generare il sito non permette ancora di inserirle;")
		st.markdown("* Un metodo per diventare ricco facendo trading in borsa;")

		image_3 = Image.open('./pics/euforico.jpg')
		st.image(image_3, use_column_width=True)


	######################################### GUARDANDO LE STELLE ################################
	if (page == 'Guardando le stelle'):

		st.title('Coming soon, really soon')



if __name__ == '__main__':
	main()

