import streamlit as st
from PIL import Image

def biography():
    st.title('About Francis')

    st.markdown('Ed ecco il mio faccione')

    me_image = Image.open('./pics/me.jpg')
    st.image(me_image, use_column_width=True, caption='Io che fingo la padronanza di metodi quantitativi avanzati')

    st.markdown('''
        Mi chiamo Francesco Carli, per gli amici *Francis*, sul playstation network *mrcharles* e sono uno studente
        del MSc in Stochastics and Data Science dell'univeristà di Torino. Dopo aver speso gli ultimi due anni della mia vita 
        a scroccare articoli su *medium* e *towards data science* voglio restiturie qualcosa alla comunità del web lasciando
         la rete un po' migliore di come l'ho trovata (*chi vuol capire capisce*).
         
        In questo piccolo spazio virtuale voglio condividere con voi la mia passione per l'**intelligenza artificale** ed il **machine learning**"
        pubblicando le visualizzazioni grafiche ed i modelli quantitativi sui quali lavoro/studio. Spero inoltre
        di riuscire a convincervi di come la matematica, la statistica e la probabiltà possano essere più *cool* e 
        colorite del temuto metodo di Ruffini imparato alle superiori.
        
        Nel Febbraio 2019, insieme ad altri amici, ho vinto il **Milano Critical Care Datathon** a seguito del quale ho dedicato 
        molto tempo allo studio di modelli di machine learning applicabili in campo medico. In particolare ho seguito un 
        progetto finalizzato all'identificazione di pazienti oncologici in una startup legata all'ospedale San Raffaele di 
        Milano e sto collaborando con l'MIT Critical Data Lab alla realizzazione di modelli previsionali per pazienti in cura intensiva. 
        
        Non sono sempre stato un **quant**, ho infatti una laurea trienale in Economia e Scienze Sociali all'Università 
        Bocconi di Milano e la mia professoressa di matematica delle superiori", dato il mio coinvolgimento nella rappresentanza 
        studentesca, sosteneva che il mio futuro fosse la politica e non i numeri *(io ve l'ho detto, fate vobis)*.
        
        Nel tempo libero amo fare sport, sopratutto correre. Ho anche una passione per la fotografia *(me la cavicchio)* 
        e per la poesia *(sono scarso)*. Ho poi un gruppo di amici intellettuali," '*I Ragazzi*', che mi sfotteranno a vita 
        per questo blog. Con loro discuto solo di meccanica quantistica e teoria delle stringhe. **Amo i meme**.
        
        *Contact me at:*
        
        * Mail: francis@mrcharles.cool
        * Github: mr-fcharles
        * Instagram: mr.francis.charles
        ''')