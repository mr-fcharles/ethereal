import streamlit as st
from PIL import Image

def home():


        st.title('Welcome to the jungle')

        st.markdown('''
        Benvenuto su mrcharles.cool, un posto chad per dank data analysis. 
        Non uscirai da qui senza aver rifiutato l'ipotesi nulla che nella tua vita ci sia bisogno di più statistica.
        Non hai idea di cosa sia un'ipotesi nulla? beh allora sei nel posto giusto.
        ''')

        image = Image.open('./pics/kermit.jpg')
        st.image(image, use_column_width=True)

        st.subheader("Cosa potresti/non potresti trovare su mrcharles.cool")

        st.markdown('''
        Questa pagina nasce con l'idea di diffondere in modo *.cool* piccoli articoli divulgativi su Probabilità, Statistica,
        Machine Learning e Intelligenza Artificiale (rispettivamente ML e AI se sei *swaggy*)
        
        L'*intensità matematica* degli articoli varierà da post a post, passando da semplici analisi esplorative ai
        **mega processi stocastici** ai quali l'autore è ormai sentimentalmente legato.
        Se la notazione matematica ti spaventa non disperare, in ogni post troverai riquadri verdi come il seguente:       
        ''')

        st.success(" 'ciao sono un riquadro verde' ")

        st.markdown('''
        dove avrò cura di sintetizzare in lingua corrente i concetti matematici più importanti (*non garantisco di riuscirci ma ci provo*).
        
        Indicherò invece con un riqaudro rosso le osservazioni più dettagliate, non strettamente necessarie alla 
        comprensione dei concetti presentati, spunti di riflessione per i più curiosi: **nerd notes**.
        ''')

        st.error("'ciao sono un box che contiene roba esoterica'")


        st.markdown('''
        Spesso questi box contengno concetti che verranno affrontati in un apposito post futuro
        
        Puoi navigare gli articoli presenti cliccando la freccetta in altro a sinistra e scorrendo le pagine disponibili nel menù a tendina.
        
        Dopo questa breve introduzione per settare i vostri *prior* (abbiate pazienza vi spiegherò tutto, se non siete 
        pazienti google è vostro amico) eccovi un piccolo riassunto delle creature nelle quali ci si può imbattere qua dentro.
        
        **Cosa puoi trovare:**
        
        * Dank data visualization;
        * Termini inglesi che potevano benissimo essere scritti in italiano (*ma siamo .cool*);
        * Concetti matematici che non sei pronto ad accogliere nella tua vita, potrebbe non essere amore a prima vista;
        * Un sacco di informazioni per fare lo sgargiante ad aperitivo ed ai pranzi di famiglia;
        * **Una marea di meme**
        ''')


        image_2 = Image.open('./pics/meme_series.jpg')
        st.image(image_2, use_column_width=True)

        st.markdown('''
        **Cosa non puoi trovare:**
        
        * Come contare le carte, diventare ricco a Las Vegas e farti picchiare dal racket dei Casinò;
        * **Gif animate :( :( :(**, sadly la piattaforma che uso per generare il sito non permette ancora di inserirle;
        * Un metodo per diventare ricco facendo trading in borsa;
        ''')

        image_3 = Image.open('./pics/euforico.jpg')
        st.image(image_3, use_column_width=True)

        st.markdown("Buona lettura")

        st.markdown("*(Ringrazio poi moltissimo Mario Costa. Mario ha avuto un'enorme pazienza nel seguirmi nella preparazione dell'infrastruttura necessaria alla realizzazione di questo sito, dai DNS alle certificazioni SSL e oltre )*")
