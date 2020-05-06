import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_stars():

	import pandas as pd
	import json

	df =pd.read_csv('data/stars_out.csv',index_col=0)
	with open('data/qname_dictionary.json', 'r') as fp:
		qname_dict = json.load(fp)

	return (df,qname_dict)


def hypothesis():

    st.title("L'importanza delle ipotesi: sampling, self-selection e omofilia")

    image = Image.open('./pics/polls_everywhere.jpg')
    st.image(image, use_column_width=True)

    st.markdown('''
        Dalla democratizzazione di internet (in particolare dall'avvento dei social network) è diventato molto facile imbattersi 
        in un **sondaggio** online. Le domande poste agli (spesso annoiati) internauti possono essere le più disparate:
        
        * Quale di questi prodotti saresti disponibile a comprare?
        * Cosa ne pensi dell'attuale governo?
        * Esiste la vita dopo la morte?
        * Qu4LE v3rdURa Ti SENTI di raPPresentaRe oGGI?!1?
        
        Insomma un sacco di persone sembrano interessate alla tua opinione. Ad alcuni, in realtà, non frega una turbomazza della tue idee: 
        vogliono profilarti, capire le tue abitudini di consumo e venderti il nuovo *olio di palma al cardamomo bio vegan*.
        
        Per ognuno di questi dentiaguzzi esiste poi un numero aleatorio (compreso tra il 3 e il 5) di tesisti, giornalisti 
        e studenti di materie quantitative allo stato brado genuinamente interessati a capire cosa ne pensi del mondo che 
        ti circonda. Spesso l'obiettivo di queste simpatiche creature è raccogliere le opinioni altrui, sintettizzarle 
        calcolando qualche statistica e fare dei grafici per presentare in modo intuitivo ciò che i dati ottenuti evidenziano.
        
        Fino a qui tutto bene. Non sono apparse formule, non ho ancora tirato fuori uno *stochastics.*
        ''')


    image2 = Image.open('./pics/che_succede.jpg')
    st.image(image2, use_column_width=True)

    st.subheader("Il ruolo delle ipotesi")

    st.markdown('''
        Recentemente ho avuto il piacere di condurre un piccolo sondaggio su un tema un po' insolito per il mio percorso 
        accademico: l'astrologia (non l'astronomia, quella è un'altra cosa, guarda [qui](https://it.wikipedia.org/wiki/Astronomia)).
        ''')

    st.warning("Se non hai fatto il sondagio sei un infame, ma puoi diventare meno infame compilandolo adesso [qui](https://forms.gle/5tteZmUYXwNKCfe59) ")

    st.markdown('''
    Appena la prima cinquantina di responsi sono arrivati mi sono reso conto che, prima di presentare i risultati, 
    avrei dovuto fare quello che ogni statistico un filo navigato fa prima di arrivare a conclusioni che potrebbero rivelarsi 
    errate in futuro: pararsi il deretano con le ipotesi. La maggior parte dei modelli quantitativi (se non tutti) richiedono 
    che alcuni 'requisiti minimi' siano rispettati affinché il passaggio da raccolta dati alle conclusioni sia solido dal 
    punto di vista logico. Possiamo concretizzare questa situauzione nella vita di tutti i giorni con il nostro primo box verde:
    ''')

    st.success('''
        **Ipotesi**: devo andare con una macchina da Mantova a Milano. Una delle ipotesi che deve essere rispettata 
        (chiaramente ce ne sono delle altre) affinché mi sia possibile affrontare il viaggio è che io abbia sufficiente 
        benzina. Possiamo quindi vedere le ipotesi come la benzina del nostro motore, ciò che permette alla nostra macchina 
        funzioni a dovere. No ipotesi rispettate, no viaggio.
        ''')

    st.markdown('''
        "Esiste però un'importante dicotomia rispetto al caso concreto sopra riportato: se non c'è la benzina la macchina 
        non partirà, se le ipotesi non sono rispettate non esiste alcuna legge fisica che impedisca al modello di sputare 
        fuori qualche numero lo stesso. Otterremo comunque dei risultati, ma risultati verosimilmente errati e non attendibili.
        ''')

    st.subheader("Un esempio istruttivo")

    st.markdown('''
        Prima di arrivare al pezzo forte di questo articolo, diventa necessaria una pratica che manderà in bestia il lettore 
        non matematico medio: *ipotizzare una situazione astratta e sconnessa dalla realtà sulla quale ragionare*. 
        Un po' tipo quei problemi delle superiori in cui un tizio compra 200 banane e vuole scambiarle con 1.73 pesci rossi.
        ''')

    image3 = Image.open('./pics/banana.jpg')
    st.image(image3, use_column_width=True, caption='il tizio con le banane')

    st.markdown('''
        Per coaudiuvare la comprensione generale, cercherò di rendere il problema più attuale e concreto di quello sopra citato. 
        Anzi, mi voglio rovinare, la renderò una situazione di *vita o morte*. Considera il seguente contesto:

        *Sei fuori a far aperitivo (e già qui siamo sull'astratto spinto data la situazione attuale). Il tuo amico Kevin 
        ti propone la seguente scommessa: si sceglie testa o croce, si lancia la monetina, chi perde offre un Negroni all'altro.*"

        Spero tu sia d'accordo con me nell'osservare che lo scenario sopra dipinto delinei *nettamente* una situazione di vita 
        o morte. Ora sei disposto a tutto pur di avere quel Negroni gratis.
        
        Ci ricordiamo inoltre che Kevin è fondamentalmente un infame (il classico amico che shoppava su candycrush per dare 
        la merda agli altri). Questa cosa ci fa salire il cospirazionismo all'istante: **Kevin è amico dei poteri forti**, 
        avrà sicuramente una monetina truccata.

        Decidi quindi di accettare la scommessa ad una sola condizione: la possibilità di verificare che la moneta non sia 
        truccata, detta in modo cool, che sia una *fair coin*. Rimane ora il problema di come verificare che la moneta sia 
        effettivamente *fair*, ci tocca fare qualche conto.

        L'idea è la seguente: lanciamo la moneta un numero predefinito di volte (che denoteremo con $N_{tot}$) e vediamo 
        quante volte esce testa rispetto al totale dei lanci ($N_{head}$). Possiamo quindi *stimare* la probabilità che 
        lanciando la moneta esca testa come:

        *Probabilità stimata testa:* $\\hat\\theta = \\frac{N_{head}}{N_{tot}}$
        
        Poichè gli *outcome* possibili (gli esiti) della moneta sono due (testa o croce) avremo che tutti i lanci non testa 
        dovranno necessariamente essere stati croce, quindi la stima della probabilità che esca croce sarà:

        *Probabilità stimata croce:* $1 -\\hat\\theta = 1- \\frac{N_{head}}{N_{tot}}$
        ''')

    st.error('''
        **Nerd note**: osserva come si stia parlando di una *stima della probabilità* e non di probabilità. Facendo tendere 
        $N_{tot}$ verso l'infinito otteniamo la definizione *frequentista* di probabilità 
        $P(testa)=\\lim_{N_{tot} \\rightarrow \\infty} \\frac{N_{head}}{N_{tot}}$. Esistono diverse interpretazioni di 
        probabilità e torneremo su questo tema in futuro.
        ''')

    st.markdown('''
        Visto che lanciare mille volte una moneta potrebbe risultare una pratica time consuming (anche se indubbiamente affascinante), 
        Francis ha programmato un simulatore di lanci di monetine qui sotto, tutto per te.
        ''')

    image4 = Image.open('./pics/future.jpg')
    st.image(image4, use_column_width=True,
             caption='quando dici a Kevin che sei in grado di simulare il lancio di 1000 monetine in una frazione di secondo')

    st.markdown('''
        Il simulatore è basato su un'importantissima **ipotesi**: tutti i lanci delle monetine sono **indipendenti ed 
        identicamente distributiti** (per gli amici, sono **i.i.d.**).
        ''')

    st.success('''
        **Indipendenti ed identicamente distribuiti:** quando affermiamo che due lanci di moneta siano *indipendenti* stiamo 
        assumendo che se il lancio 1 è risultato *testa*, questo non ci dà alcuna informazione sull'outcome dei lanci successivi: 
        sapere che la moneta 1 è risultata testa, se la nostra ipotesi è verificata, non aumenta la probabilità che la 
        seconda moneta risulti nuovamente testa. Ogni lancio della monetina è a sé stante, indipendente appunto.
        Quando invece assumiamo che i lanci siano *identicamente distribuiti* stiamo affermando che la probabilità che 
        ogni moneta risulti testa sia la stessa per ogni lancio.
        ''')

    st.error('''
        "**Nerd note**: osserva come *indipendenti* ed *identicamente distribuiti* non siano la stessa cosa: potremmo avere 
        un numero $N$ di lanci di moneta indipendenti ma con ognuno una probabilità diversa di risultar testa (quindi non identicamente distribuiti).
        ''')

    st.markdown('''
        Prima di avviare questa gloriosa simulazione devi impostare due parmetri:
    
        * **Probabilità testa effettiva**: se la moneta di Kevin non fosse truccata la probabilità di testa sarebbe 0.5 
        (50%). Tutti gli altri valori modellano monete che favoriscono maggiormente un lato rispetto all'altro;
        
        * **Numero di lanci:** prova a giocare con questo parametro e osserva come varia la stima all'aumentare dei lanci.
        
        Daje, tenendo ben a mente queste importanti ipotesi, possiamo impostare i valori e lanciare le monete
    ''')

    prob_head = st.slider('Probabilità testa', min_value=0.01, max_value=1.0, step=0.01)
    n_throws = st.slider('Numero lanci', min_value=1, max_value=2500, step=20)

    if st.button('Lancia le monete!'):

        coin_tosses = np.array([])
        running_mean = np.array([])

        for i in range(n_throws):
            coin_tosses = np.append(coin_tosses, np.random.choice([1, 0], p=[prob_head, 1 - prob_head], size=1))
            running_mean = np.append(running_mean, np.mean(coin_tosses))

        # lanci = np.random.choice([1,0],p=[prob_head,1-prob_head],size=n_throws)

        n_heads = sum(coin_tosses)
        n_tails = n_throws - n_heads

        prob_head_estimate = n_heads / n_throws
        prob_tail_estimate = n_tails / n_throws

        lanci = np.where(coin_tosses == 1, 'Testa', 'Croce')
        st.write(lanci)

        st.write("Numero monete testa:", n_heads, "	Numero monete croce:", n_tails)
        st.write("Stima probabilità testa:", np.round(prob_head_estimate, decimals=2), "	Stima probabilità croce:",
                 np.round(prob_tail_estimate, decimals=2))
        st.write("Probabilità testa effettiva:", prob_head, "Probabilità croce effettiva", 1 - prob_head)

        st.markdown('''
            *Il grafico qui sotto riporta sull'asse orizzontale il numero di monetine lanciate, sull'asse verticale la 
            stima della probabilità corrispondente a quel numero di lanci. Osserva come, all'aumentare del numero di moentine 
            lanciate, la stima converge velocemente verso l'effetiva probabilità di testa (rappresentato dalla linea orizzontale)*
            ''')
        real_value = np.array([prob_head for i in range(len(running_mean))])

        graph_data = pd.DataFrame(columns=['Stima', 'Valore effettivo'])
        graph_data['Stima'] = running_mean
        graph_data['Valore effetivo'] = real_value

        st.line_chart(graph_data)

    st.markdown('''
        Se hai giocato abbastanza con i parametri del simulatore, ti sarai accorto che nella situazione ideale che abbiamo 
        costruito non importa quanto Kevin sia un figlio della mmmerda: indipendentemente da quanto la moneta sia unfair, 
        tu lanciandola come un pazzo te ne accorgerai. Potrai quindi usufruirne per scegliere su che lato della moneta 
        scommettere o decidere di crepare di schiaffi Kevin una volta per tutte.
        ''')

    st.subheader("Random sampling")

    st.markdown("A questo punto dell'articolo la situazione in cui si trova il lettore è probabilmente la seguente:")

    image5 = Image.open('./pics/fry.jpg')
    st.image(image5, use_column_width=True)

    st.markdown('''
    Facciamo un po' di chiarezza! Nell'esempio sopra abbiamo parlato di una unica monetina, proviamo ora a pensare ad uno 
    scenario leggermente diverso ma identico nel contenuto: invece di avere 1 moneta lanciata $N$ volte, abbiamo $N$ 
    monete identiche che possiamo lanciare una sola volta. Riprendendo l'ipotesi che tutti i lanci fossero **i.i.d**, 
    spero tu sia convinto che la situazione sarebbe la medesima.
    
    Siamo ancora interessati a sapere quale sia la la probabilità che una moneta risulti testa. Considerando ora che $N$ 
    potrebbe essere un numero troppo grande anche per il nostro simulatore, dobbiamo scegliere una delle seguenti alternative:
    
    * *ce ne sbattiamo altamente* e lanciamo tutte le $N$ monete, dedicando la nostra vita alla scienza: qualcuno dovrà pur lanciare ste monete;
    * ci inventiamo qualcosa di *smart* usando la statistica.
    
    Potremmo per esempio adottare una procedura di **simple random sampling** (campionamento casuale semplice):
    ''')

    st.success('''
        "**Simple random sampling**: estraiamo un campione di $n$ monete dall'insieme totale delle $N$ monete disponibili. 
        Ogni moneta ha la stessa probabilità di finire nel nostro *campione* e viene *scelta in modo completamente casuale*. 
        Come nell'esempio precedente (grafico che converge alla linea orizzontale), per un $n$ sufficientemente grande la 
        proporzione di testa e croce tra le $n$ monete sarà più o meno la stessa di quella tra le $N$ monete. Ci evitiamo 
        quindi di doverle lanciare tutte le $N$ monete.
        ''')

    st.markdown('''
    Nel processo sopra descritto **due** sono i punti chiave:
    
    * Il fatto che *a priori* ogni moneta abbia la stessa probabilità di finire nel campione;
    * Il fatto che *a posteriori* ogni moneta nel campione sia stata scelta casualmente.
    
    Nota come questi due aspetti siano appunto **ipotesi**: *se* queste ipotesi sono rispettate, *allora* le grandezze 
    calcolate sul campione di $n$ monetine rispecchiano quelle della popolazione $N$.
    ''')

    st.error("**Nerd notes:** Per i più attenti, la proposizione logica *<<se ..., allora ...>>* denota ciò che in matematica è chiamato **teorema**.")

    st.markdown('''
        Nel nostro esempio, l'ipotesi iniziale che le monete siano i.i.d. fa sì che queste due ulteriori ipotesi siano 
        automaticamente soddisfatte: non importa come le scegliamo o chi finisca nel campione, poichè sono tutte identiche. 
        Notiamo quindi come l'ipotesi iniziale implichi direttamente la validità queste ultime ipotesi.
        ''')

    image6 = Image.open('./pics/inception.jpg')
    st.image(image6, use_column_width=True)

    st.subheader("SI', MA QUINDI IL SONDAGGIO?!!?")

    st.markdown('''
    Ok ci siamo, il sondaggio! Ora che abbiamo introdotto tutta questa struttura teorica siamo pronti ad affrontare come si deve il problema iniziale.
    
    Pensiamo ad una domanda a scelta multipla di un form, cosa la rende diversa dal caso della moneta? Beh in realtà poco! 
    Invece di avere due outcome possibili (*testa,croce*), abbiamo un numero $k$ di risposte possibili e siamo interessati 
    a capire quale sia la probabilità che, prendendo una persona per strada, questa ci risponda con una delle alternative.

    Un primo problema risulta evidente: **non possiamo lanciare in aria persone i.i.d.**, per quanto la cosa sarebbe 
    divertente, probabilmente non contribuirebbe al nostro scopo finale. Non possiamo quindi seguire l'approccio adottato con le monete.

    Non possiamo quindi impostare un esperimento in cui la prima ipotesi implichi le altre due e, come abbiamo imparato 
    all'inizio dell'articolo, no ipotesi no conclusioni. Non ci resta quindi che provare a raccogliere un simple random 
    sample di opinioni con un form condiviso su internet, sperando che il campione soddisfi i requisiti elencati.

    Non possiamo quindi impostare un esperimento in cui la prima ipotesi implichi le altre due e, come abbiamo imparato 
    all'inizio dell'articolo, no ipotesi no conclusioni. Non ci resta quindi che provare a raccogliere un simple random 
    sample di opinioni con un form condiviso su internet, sperando che il campione soddisfi i requisiti elencati.
    ''')

    image7 = Image.open('./pics/wrong.jpg')
    st.image(image7, use_column_width=True)

    st.subheader("Guardiamo i dati")

    st.markdown('''
        Quando in precedenza abbiamo parlato *simple random sample* abbiamo detto che tale campione è rappresentativo 
        dell'intera popolazione e che quindi statistiche calcolate sul campione ci permettono di stimare le quantità di 
        interesse nella popolazione, poichè rispecchiano le stesse proporzioni *(a patto che le ipotesi siano verificate)*. 
        Vediamo una statistica interessante del campione raccolto con l'astro-questionario: **il genere dei rispondenti**
        ''')

    df, qname_dict = load_stars()

    labels = df['q_22'].value_counts().index
    sizes = df['q_22'].value_counts().values

    # colors
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()

    st.pyplot()

    st.markdown('''
    **68.1% dei rispondenti sono donne**, wow. Guardando questi numeri si delineano due scenari alternativi:
    
    * La storia di Mendel, delle X e delle Y, dei piselli odorosi *era una cagata pazzesca*, nella società ci sono più donne che uomini;
    * Il campione che ho raccolto non è un *random sample*.
    
    Se è difficile sentire dire da uno statistico 'sono sicuro' rispetto ad una proposizione qualsiasi', è piuttosto verosimile 
    che il nostro campione non sia *random sample*. Individueremo ora due (dei tanti) motivi per i quali un campione raccolto 
    con questa modalità non rappresenti un *random sample*. Forse sarai sorpreso (forse no), ma questi motivi hanno poco 
    a che fare con la matematica, anzi sono piuttosto *umani*
    ''')

    st.subheader("Self-selection")

    st.markdown('''
    In tanti amici mi hanno chiesto come mai mi fosse venuto in mente di effettuare questo sondaggio *(so veramente poco di astrologia)*. 
    Durante quarantena lo sport nazionale è diventato sentirsi su whatsapp e sui social per farsi compagnia 
    (ho una vita sociale molto più attiva di prima in fin dei conti). Dopo un mese di smalltalk e chat con amici mi sono 
    reso conto di come l'oroscopo (ma più in generale l'astrologia) fosse un *tema ricorrente tra le controparti femminili* 
    mentre non venisse mai sfiorato dai maschietti *(qualcuno direbbe: perchè i maschietti sono monotematici)*. 
    E' proprio da questa osservazione che è nata l'idea di realizzare il questionario.
    ''')

    st.markdown('''
    In tanti amici mi hanno chiesto come mai mi fosse venuto in mente di effettuare questo sondaggio *(so veramente poco di astrologia)*. 
    Durante quarantena lo sport nazionale è diventato sentirsi su whatsapp e sui social per farsi compagnia 
    (ho una vita sociale molto più attiva di prima in fin dei conti). Dopo un mese di smalltalk e chat con amici mi sono 
    reso conto di come l'oroscopo (ma più in generale l'astrologia) fosse un *tema ricorrente tra le controparti femminili* 
    mentre non venisse mai sfiorato dai maschietti *(qualcuno direbbe: perchè i maschietti sono monotematici)*. 
    E' proprio da questa osservazione che è nata l'idea di realizzare il questionario.
    
    Va beh ma questo cosa centra con i campioni random? Una sproporzione nel genere dei rispondenti come quella vista sopra 
    suggerisce che il processo sia affetto da un fenomeno conosciuto nelle scienze sociali come: **self-selection bias**:
    ''')

    st.success('''
        **Self-selection bias:** in parole povere, è più probabile che un individuo interessato di astrologia risponda ad 
        un questionario di astrologia rispetto ad una persona non interessata. Questa è l'essenza del *self-selection bias*, 
        facciamo più volentieri quello che ci piace, meno volentieri quello che non ci piace.
        ''')

    st.error('''
        **Nerd note:** quanto evidenziato sopra, tuttavia non è sufficiente dal punto di vista statistico per concludere che 
        le donne si interessino più di astrologia degli uomini. Ci può dire che, **nel campione raccolto**, le donne sono 
        **correlate** maggiormente alla tematica. Discuteremo in futuro della differenza tra **causalità** e **correlazione**.
        ''')

    st.markdown('''
    Ti ricordi la prima condizione necessaria affinchè il campione fosse un random sample?
    
    *'A priori ogni persona (prima moneta) deve avere la stessa probabilità di finire nel campione'*
    
    E' immediato vedere come il *self-selection bias*, faccia saltare questa prima ipotesi: gli individui interessati di 
    astrologia sono rappresentati con probabilità maggiore all'interno del campione. La prossima volta che vedi un sondaggio 
    e pensi *'che cazzata,non mi interessa, non lo farò mai'*, sappi che stai distorcendo una ricerca sociale. **Sei un infame come Kevin, sei un maledetto.**    
    ''')

    image8 = Image.open('./pics/maledetti.jpg')
    st.image(image8, use_column_width=True)

    st.markdown('''
        Gli effetti del self-selection bias vanno ben oltre la distorsione dei sondaggi e la violenza psicologica su chi 
        calcola statistiche, il self-selection bias è ovunque esistano processi di scelta sociale. Questo tipo di bias è 
        spesso alla base dei meccanismi (talvolta involontari) di discriminazione e segregazione sociale. Ci torneremo su.
        ''')

    st.subheader('Omofilia')

    st.markdown('''
    Esiste poi un altro meccanismo, simile alla self-selection, in grado di rovinare un'analisi come quella impostata per 
    l'astro-questionario: **l'omofilia**.
    ''')

    st.success('''
        **Omofilia:** usando un francesismo, l'omofilia è il fenomeno (molto noto nella ricerca sociale) secondo il quale 
        *i coglioni vanno in coppia*. In modo più educato, tendenzialmente, i nostri amici ci assomigliano e condividono con noi molti interessi."
        ''')

    st.markdown('''
    Perchè questo è un problema per il questionario? Perchè compileremo il questionario e, per fare contento Francis, lo 
    inoltreremo a quei due amici che sentiamo ogni 30 secondi della nostra vita e a cui siamo attacati con il cordone ombelicale. Ricordi 
    la seconda assunzione del campione aleatorio?
     
     *'A posteriori ogni persona (prima moneta) nel campione sia stata scelta casualmente'*
     
     A questo punto, unendo omofilia e self-selection bias abbiamo che alcuni individui risponderanno al questionario con 
     alta probabilità rispetto ad altri *(self-selection)*. Questi individui inoltreranno poi il questionario ad altre persone 
     a loro tendenzialmente simili secondo il principio di omomofilia, invalidando l'ipotesi che ogni persona nel campione 
     sia stata scelta in modo casuale. **Et voilà, campione distorto**.
    ''')

    image9 = Image.open('./pics/likeme.jpg')
    st.image(image9, use_column_width=True)

    st.error('''
        **Nerd note:** osserva la direzione dei due effetti: se la *self-selection* porta persone simili a selezionarsi 
        autonomamente in gruppi omogenei, *l'omofilia* porta gruppi omogenei a far scelte simili. I due effetti si rafforzano l'un l'altro.
        ''')

    st.subheader('Conclusioni')

    st.markdown('''
    Un elefante gira ora nella stanza: se sapevi di tutte queste disgrazie, perchè fare il questionario?
    
    **Motivo 1:** sono in quarantena come voi, *anche io sono annoiato*. Per una strana perversione personale amo analizzare dati, 
    volevo quindi provare l'esperienza folle di raccogliere dati personalmente per una volta.
    ''')

    image10 = Image.open('./pics/regret.jpg')
    st.image(image10, use_column_width=True)

    st.markdown('''
    **Motivo 2:** i dati raccolti non sono da buttare via, semplicemente non possono essere usati per trarre conclusioni 
    sull'universo conosciuto, non possono essere usati per **far inferenza sulla popolazione**. Probabilmente sono buoni 
    dati per descrivere **cosa ne pensano i miei amici (e gli amici degli amici)** dell'astrologia.

    **Motivo 3:** spero di averti convito di come sia possibile arrivare a conclusioni sbagliate se non si rispettano 
    **le cazzo di ipotesi dei modelli**. Questo per dire che, tutte le volte che in televisione senti un giornalista dire 
    *<<le previsioni erano errate>>*, rispetto ad un qualsiasi argomento, 99% delle volte non si è trattato di un errore 
    computazionale, non hanno sbagliato i conti, erano le ipotesi del modello predittivo a essere errate.

    **Motivo 4:** gli effetti di self-selection e omofilia condizionano fortemente il modo in cui percepiamo il mondo che ci circonda. 
    Spero tu abbia intuito che pure facendo un sondaggio online sia facile, soprattuto se non si è oggettivi nella formulazione delle 
    domande, confermare le idee con le quali si è partiti e non sondare in maniera rigorosa le opinioni altrui. L'opinione di 
    chi ci è *socialmente vicino* probabilmente somiglia alla nostra, **non giudicare il mondo guardando solo il tuo prato di casa**, 
    pure se abiti in campagna e il tuo giardino ti sembra grande.
    
    Concludo ringraziandoti di aver ha avuto la pazienza di arrivare fino in fondo a questo articolo. E' la prima volta 
    che scrivo così tanto e spero possa esserti utile questa mia riflessione. Per eventuali feedback, osservazioni o 
    richieste di approfondimento scrivetemi su *francis@mrcharles.cool*. **La messa è finita, andate in pace.
    ''')