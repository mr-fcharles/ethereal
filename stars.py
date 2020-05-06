import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from PIL import Image
import plotly.graph_objects as go

@st.cache
def cross_tab(df,q_a,q_b):

    temp = pd.crosstab(df[q_a], df[q_b]) / pd.crosstab(df[q_a], df[q_b]).sum()
    #st.write(temp)

    return temp



@st.cache
def load_stars():
    import pandas as pd
    import json

    df = pd.read_csv('data/stars_out.csv', index_col=0)

    with open('data/qname_dictionary.json', 'r') as fp:
        qname_dict = json.load(fp)

    with open('data/count_questions.json', 'r') as fp:
        count_questions = json.load(fp)

    inv_qname_dict = {v: k for k, v in qname_dict.items()}

    return (df, qname_dict, inv_qname_dict, count_questions)

@st.cache
def proportion_visualizer(df, qname_dict, q_a, q_b):

    df_internal = pd.crosstab(df[q_a], df[q_b]) / pd.crosstab(df[q_a], df[q_b]).sum().values

    df_internal = df_internal.round(2)

    x = df_internal.columns.values

    for i, j in enumerate(df_internal.index.values):

        if (i == 0):

            fig = go.Figure(go.Bar(x=x, y=df_internal.loc[j].values, name=j))

        else:

            fig.add_trace(go.Bar(x=x, y=df_internal.loc[j].values, name=j))

    fig.update_layout(barmode='stack', legend_orientation='h', legend=dict(x=0, y=1.3), hovermode='x',

                      xaxis={

                          'title': {

                              'text': qname_dict[q_b],
                              'font': {'size': 12}
                          }
                      },

                      yaxis={

                          'title': {

                              'text': qname_dict[q_a],
                              'font': {'size': 12}
                          }
                      }

                      )
    return fig

@st.cache
def aggregate_plotter(df, question, qname_dict):
    if (question in [1, 2]):
        pass

    else:

        df_temp = pd.Series(name=question, data=df[question].values)
        fig = px.pie(df_temp, 'question', title=qname_dict[question])
        fig.update_traces(textposition='inside', textinfo='percent+label')

        st.plotly_chart(fig, use_container_width=True)


# return fig


def stars():
    import plotly.express as px
    import plotly.graph_objects as go

    st.title('Guardando le stelle')

    image1 = Image.open('./pics/horoscope.jpg')
    st.image(image1, use_column_width=True)

    st.markdown('''
	Dopo aver:
	* raccolto i dati del **sondaggio**;
	* creato un blog per condividere i dati del **sondaggio**;
	* scritto un articolo per facilitare la lettura dei dati del **sondaggio**;
	
	credo sia arrivato il momento di condividere con te i risultati del **sondaggio**! Non pensare però di passarla liscia:
	
	*Il pippone teorico è sempre dietro l'angolo, pronto a colpirti quando meno te lo aspettati.*
	''')

    img = Image.open('./pics/curtain.jpg')
    st.image(img, use_column_width=True, caption='Il pippone sopra citato in agguato')

    st.markdown('''
	In questo articolo vorrei darti delle chiavi di lettura affinchè tu possa orientarti tra i dati raccolti in auotonomia. Cominciamo!
	''')

    st.subheader('Dati demografici')

    st.markdown('''
	Prima di guardare le vere e proprie risposte del sondaggio, è buona pratica analizzzare i pochi dati demografici dei rispondenti.
	Partiamo osservando il **genere** dei partecipanti, ricordando che il sondaggio ha totalizzato un totale di **268 risposte**:
	''')

    df, qname_dict, inv_qname_dict, count_questions = load_stars()

    df = df[df.q_22 != 'Altro']

    df_genere = pd.Series(name='Genere', data=df['q_22'].values)
    fig = px.pie(df_genere, 'Genere', title='Distribuzione genere')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('''
	Come abbiamo già commentato nell'articolo precedente (*'L'importanza delle ipotesi'*, la cui lettura è caldamente consigliata prima di proseguire), 
	il campione è costituito al 68.3% da *femminucce*. I *maschietti*, quindi, sono meno rappresentati nel campione.
	Guardiamo ora **l'età**:
	''')

    df_question = pd.Series(name='Età', data=df['q_23'].values)
    fig = px.pie(df_question, 'Età', title='Distribuzione età')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('''
	Considerando che l'età media in Italia è di 45,7 anni ([fonte istat](https://www.istat.it/it/archivio/238447)), questo dato
	ci dà un ulteriore campanello di allarme su come il campione raccolto non rappresenti la popolazione italiana, ma semplicemente
	i *pischelli amici di Francis*. Analizziamo ora i **titoli di studio** e la **provenienza geografica**:
	''')

    df_question = pd.Series(name='Titolo di studio', data=df['q_24'].values)
    fig = px.pie(df_question, 'Titolo di studio', title='Distribuzione titolo di studio')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)

    df_question = pd.Series(name='Provenienza geografica', data=df['q_25'].values)
    fig = px.pie(df_question, 'Provenienza geografica', title='Distribuzione provenienza geografica')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('''
	L'informazione riguardante la provenienza geografica di chi ha risposto mette la parola fine a qualsiasi speranza di
	rappresentatività nazionale del campione: sono quasi tutti in **Padania**. Eh niente, R.I.P. (*o come va di moda su facebook: R.I.P. in pace*). 
	
	Da qui in poi ricordati perciò che tutti i risultati descrivono
	verosimilmente **gli amici di chi scrive**, non l'universo conosciuto. Non usare quindi le informazioni preziose che
	apprenderai qua dentro per rimorchiare: **potrebbe non funzionare**.
	''')

    st.subheader('''La struttura del questionario e i risultati aggregati''')

    questions = list(qname_dict.values())

    st.markdown('''
	Il questionario che hai compilato era grosso modo diviso in 3 blocchi:
	
	* L'astrologia e l'oroscopo;
	* L'astrologia ed il resto del sapere umano;
	* Il futuro *(che centrava poco, ma sono intrippato con Westworld e ce l'ho buttato dentro)*;
	
	Le domande, se non le ricordi, erano queste:
	''')

    st.write(questions)

    st.markdown('''
	Trovi qui sotto tre menù a tendina che, una volta aperti, ti permettono di graficare al volo tutte le domande presenti nel questionario
	per le tre aree tematiche. Per chiarezza di esposizione (sopratutto per chi legge da cellulare) sotto ogni plot vengono
	riportati gli stessi dati illustrati dai grafici in forma tabellare
	''')

    first_block = questions[0:11]
    second_block = questions[11:14]
    third_block = questions[14:21]

    option = st.selectbox("L'astrologia e l'oroscopo", first_block)

    if (inv_qname_dict[option] in ['q_7', 'q_8']):

        labels = count_questions[inv_qname_dict[option] + '_labels']
        values = count_questions[inv_qname_dict[option] + '_values']

        fig = go.Figure([go.Bar(x=labels, y=values)])
        fig.update_layout(title=option)

        st.plotly_chart(fig, use_container_width=True)

        #st.write(df_temp.value_counts())

    else:
        df_temp = pd.Series(name=str(inv_qname_dict[option]), data=df[str(inv_qname_dict[option])].values)
        fig = px.pie(df_temp, df[inv_qname_dict[option]], title=option)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(legend_orientation='h')

        st.plotly_chart(fig, use_container_width=True)

        st.write(df_temp.value_counts()/df_temp.value_counts().sum())

    st.warning('''
    Nelle tabelle sotto i grafici leggete numeri come 0.3258 e 0.2884, questi vanno letti come 32.58% e 28.84%''')

    ############################ Block 2 ###################################################

    option2 = st.selectbox("L'astrologia e la religione", second_block)

    df_temp = pd.Series(name=str(inv_qname_dict[option2]), data=df[str(inv_qname_dict[option2])].values)
    fig = px.pie(df_temp, df[inv_qname_dict[option2]], title=option2)
    fig.update_traces(textposition='inside', textinfo='percent+label')

    if (inv_qname_dict[option2] == 'q_14'):
        fig.update_layout(legend_orientation='h', title="L'astrologia e la scienza: scientificità da 1 a 5")
    else:
        fig.update_layout(legend_orientation='h')

    st.plotly_chart(fig, use_container_width=True)

    st.write(df_temp.value_counts() / df_temp.value_counts().sum())

    ############################ Block 3 ####################################################

    option3 = st.selectbox("Il futuro", third_block)

    df_temp = pd.Series(name=str(inv_qname_dict[option3]), data=df[str(inv_qname_dict[option3])].values)
    fig = px.pie(df_temp, df[inv_qname_dict[option3]], title=option3)
    fig.update_traces(textposition='inside', textinfo='percent+label')

    if (inv_qname_dict[option3] == 'q_15'):
        fig.update_layout(legend_orientation='h', title="Il futuro è (1=predeterminato - 5=da scrivere)")
    else:
        fig.update_layout(legend_orientation='h')

    st.plotly_chart(fig, use_container_width=True)

    st.write(df_temp.value_counts() / df_temp.value_counts().sum())

    #########################################################################################

    st.markdown('''
	Tutti i grafici che puoi visualizzare sopra rappresentano i **dati aggregati**. Quando parliamo di dati aggregati
	intendiamo la totalità dei responsi, i dati *nudi e crudi*, così come sono stati raccolti. Questi risultati cristallizzano
	come in *una panoramica* l'opinione complessiva di chi si è espresso. Ti evidenzierò ora, per categorie di domande, alcuni spunti
	per riassumere le evidenze trovate:
	
	**L'astrologia e l'oroscopo**
	* Il 75% percento dei rispondenti conosce almeno il proprio segno;
	* Più del 50% dei rispondenti dichiara di consultare l'oroscopo quando capita mentre più del 30% dichiara di non consultarlo mai;
	* Circa il 45% dei rispondenti afferma che l'oroscopo non abbia alcuna funzione/abbia una funzione ricreativa, il 30% una funzione introspettiva;
	* Più del 60% dei rispondenti afferma di non essersi mai interessato di oroscopo/astrologia;
	* Il 48% dei rispondenti afferma che l'astrologia vada considerata come uno svago, mentre il 42% ritiene che sia un punto di vista
	da tenere in considerazioni (con importanza differenziata);
	* Se complessivamente il 14% dei rispondenti afferma di considerare la compatibilità astrologica con il partner tra il 2-3 (in una scala da
	1 a 5), questa percentuale crolla al 6% quando si parla di amici.
	
	**L'astrologia e la religione**
	* Il 42% afferma che religione e astrologia siano due cose diverse mentre il 36,7% ritiene che siano diverse con aspetti comuni.
	In questa domanda si rileva anche una buona quota di persone che rispondono 'Non saprei' (16,3%);
	* Il 25% dei rispondenti afferma di essere credente e praticante, mentre il 50% dichiara di avere una fede/credere in una entità superiore. Il 25%
	rimanente non crede in nulla;
	* Il 63% sostiene che l'astrologia sia una disciplina poco scientifica (tra 1-2 su una scala da 1 a 5), il 37% rimanente afferma invece
	che sia una disciplina al pari delle altre scienze (con un 23,7% che risponde 3).
	
	**Il futuro**
	 * Solo il 10% dei rispondenti afferma che in qualche modo il futuro sia predeterminato (risposte 1-2), ben il 56,7% credono
	 che il futuro sia essenzialmente tutto da scrivere (4-5);
	 * La quasi totalità dei rispondenti crede nella 'libertà di pensiero' (94,4%). Il 4,07% risponde non saprei;
	 * Riguardo la possibilità di poter anticipare *l'immediato futuro* troviamo il 50% dei rispondenti affermare di non essere
	 interessati ad anticipare quello che succederà (1-2), il 25% circa in una posizione intermedia (3) e il restante 25% essere fortemente
	 propensi ad anticipare il futuro (4-5). Le percentuali sono molto simili per quanto riguarda il *medio lungo periodo*, anche se i partecipanti
	 sembrano leggermente più inclini a voler conoscere il futuro lontano rispetto a quello immediato;
	 * L'idea di conoscere in anticipo il futuro farebbe sentire il 27% più sicuro, il 31,5% impotente. Ben il 28,9% dichiara 'non saprei' e
	 il 12,6% risponde 'mi è indifferente'.
	 
	
	
	''')

    st.subheader("Disaggregare i dati")

    st.markdown('''
    Quindi tutto sto casino per qualche grafico a torta?
    ''')

    img = Image.open('./pics/yesno.jpg')
    st.image(img,use_column_width=True)

    st.markdown('''
    Fino ad ora abbiamo osservato **dati aggregati**, come anticipato in precedenza. Possiamo estrarre ulteriori *insights* (informazioni utili)
    **disaggregando** i dati raccolti e stratificando sulle varie dimensioni in analisi. Considerando che probabilmente l'ultima
    frase ti risuonerà in testa come una *supercazzola*, facciamo un esempio di stratificazione: 
    ''')

    plot = proportion_visualizer(df,qname_dict,'q_13','q_22')

    st.plotly_chart(plot,use_container_width=True)

    st.write(cross_tab(df, 'q_13', 'q_22'))

    st.markdown('''
    Nel grafico sopra stiamo *condizionando* la domanda *'il tuo rapporto con la religione'* rispetto al *genere* del rispondente, in parole povere,
    stiamo guardando come siano differenti le risposte delle donne da quelle degli uomini. Le due colonne sommano a 1 (100%) e 
    la dimensione dei rettangoli colorati rappresenta la percentuale di persone in quella categoria *(asse orizzontale)*
    che hanno risposto alla domanda con una delle alternative disponibili (asse verticale). 
    
    Se ti ricordi, uno dei punti emersi dall'analisi
    dei dati aggregati, era che il 25% dei partecipanti affermava di non credere in nulla. Diversificando queste risposposte rispetto al genere ci
    accorgiamo che **nel nostro campione sembra essere molto più probabile** (più del doppio) che un uomo dichiari di non credere in nulla
    rispetto ad una donna. Vediamo quindi come:
    
    * Gli uomini siano tendenzialmente creature semplici orientate al raggiungimento dei bisogni primari *(poi vedremo anche dei diffeti)*;
    * Poichè inoltre che il nostro campione sovra rappresenta il gentil sesso, la **differenza tra dati aggregati e
    disaggregati** appare ancora più netta. 
    ''')


    st.markdown('''
    Considerando di avere 25 domande, non ci resta che graficare le 300 possibili coppie di domande, guardare uno a uno i grafici
    e cercare di capire se esistano delle differenze nelle proporzioni dei vari campioni. **Yeeeeeeee**
    ''')

    img = Image.open('./pics/hidepain.jpg')
    st.image(img, use_column_width=True)

    st.error('''**Nerd note**: perchè 300 possibili coppie? questo numero, per i più attenti è il risultato del *binomial coefficient*
    ${N\\choose k} = \\frac{n!}{k!(n-k)!}$, dove $n!$ denota il *fattoriale* del numero $n$ ossia $n!=n*(n-1)*(n-2)*...*2*1$ .Nel nostro caso ${25\\choose 2}=300$
    ''')

    st.markdown('''
    Osserviamo inoltre il seguente grafico:
    ''')

    plot = proportion_visualizer(df, qname_dict, 'q_3', 'q_17') #pvalue 0.11

    st.plotly_chart(plot, use_container_width=True)

    st.write(cross_tab(df,'q_3','q_17'))

    st.markdown('''
    La situazione in questo caso è ancora più complessa:
    
    * Rispetto al caso del genere *(maschio, femmina)* stiamo ora stratificando su una domanda con 5 possibili risposte;
    * Solo l'ultima colonna sembra, a occhio, essere diversa dalle altre: tra chi desidera maggiormante
    anticipare il futuro *(risposta 5)* c'è una percentuale maggiore di persone che consultano regolarmente e spesso l'oroscopo
    *(un valore del 20% rispetto ad un valore del 7-8% degli altri casi)*.
    
    Possiamo in qualche modo calcolare **una quantità** che ci aiuti ad evidenziare differenze significative tra le proporzioni?
    ''')

    st.subheader("Il solito esempio *improbabile*: Kevin strikes back")

    st.markdown('''
    Eh niente, se te lo stavi aspettando, questo è esattamente il momento in cui la combo **esempio assurdo - pippone teorico** fa il suo ingresso.
    ''')

    img = Image.open('./pics/di_nuovo.jpg')
    st.image(img,use_column_width=True)

    st.markdown('''
    *Immaginiamo anche questa volta di aver a che fare con il nostro amico infame preferito: Kevin. La settimana scorsa, grazie ai tuoi nuovi
     super poteri statistici, se riuscito a scroccargli un Negroni. Questa cosa non gli è andata proprio giù e, deciso a fartela pagare, ti propone
     una nuova sfida: una partita a Risiko.*
     
     Sei perfettamente conscio che questa potrebbe essere la tua ultima sera con Kevin poichè l'evidenza statistica descrive come
     il 99,99% delle partite a Risiko tra amici finiscano nel sangue e nella violenza. Ma è giusto così, **il mondo è un posto spietato**.
    ''')

    img = Image.open('./pics/peace.jpg')
    st.image(img,use_column_width=True)

    st.markdown('''
    Visto che Kevin è rimasto un maledetto, sospetti che ti stia per rifilare un set di 3 dadi truccati per poi *attaccarti la Kamchatka*,
    mettendo fine ai tuoi sogni espansionistici di un'Eurasia prospera e unita. In realtà ormai tu sei studiatissimo e sai 
    che ti *basta* passare le 6 ore prima del gioco a lanciare cose per controllare che nessuno ti stia fregando. 
    
    Questa volta, tuttavia, il setting è leggermente diverso: i dadi sono 3, potrebbero non essere tutti truccati e le differenze
    potrebbero essere minime (l'altra volta l'hai sgamato malamente). Proviamo quindi a impostare un ragionamento diverso da quello dell'ultimo articolo
    partendo da una domanda: *come ci aspettiamo siano distribuiti gli esiti dei lanci di 3 dadi non truccati?*
    
    Ragioniamo insieme. Se tutti e tre i dadi non fossero truccati, ogni faccia del dado, dovrebbe essere equiprobabile!
    Quindi, lanciando 1 solo dado 6 volte ci aspettiamo che ogni faccia salti fuori circa 1 volta. Lanciando 3 dadi identici (*i.i.d*)
    60 volte, ogni faccia dovrebbe saltare fuori circa 30 volte. Qui sotto puoi simulare questo piccolo esperimento.
    ''')

    #random_state = np.random.random_integers(low=1,high=10000,size=1)

    random_state = np.random.choice([2,3,4,7,10])

    np.random.seed(random_state)


    if st.button('Lancia i dadi!',):



        dices = pd.DataFrame(columns=['Dado1','Dado2','Dado3'],data=np.random.random_integers(low=1,high=6,size=(60,3)))


        count_dices = pd.DataFrame(index=[1,2,3,4,5,6],columns=['Dado1','Dado2','Dado3'])
        count_dices['Dado1'] = dices['Dado1'].value_counts(sort=False).values
        count_dices['Dado2'] = dices['Dado2'].value_counts(sort=False).values
        count_dices['Dado3'] = dices['Dado3'].value_counts(sort=False).values

        st.markdown("Qui puoi vedere i lanci nudi e crudi")
        st.write(dices)

        st.markdown("Qui invece puoi vedere vedere quante volte una certa faccia salti fuori per ognuno dei tre dadi. Ricorda che, per adesso, **i dadi sono identici**")
        st.write(count_dices)

        st.markdown("Trovi qui sotto invece il grafico con le proporizioni dei vari outcome per ogni dado")


        count_proportions = (count_dices/count_dices.sum()).round(2)
        x = count_proportions.columns

        for i, j in enumerate(count_proportions.index.values):

            if (i == 0):

                fig = go.Figure(go.Bar(x=x, y=count_proportions.loc[j].values, name=str(j)))

            else:

                fig.add_trace(go.Bar(x=x, y=count_proportions.loc[j].values, name=str(j)))

        fig.update_layout(barmode='stack', legend_orientation='h')#, legend=dict(x=0, y=1.3))

        st.plotly_chart(fig,use_container_width=True)


    st.markdown('''
    Nonostante i dadi non siano truccati, eseguendo l'esperimento sopra più volte possiamo osservare che:
    
    * Molto raramente, in 60 lanci, ogni faccia del dado salti fuori esattamente 10 volte;
    * Pur avendo dadi identici, le proporzioni tra gli outcome variano da dado a dado.
    
    Come mai? Prima di pensare che la tua vita sia *un'unica grande bugia*
    ''')

    img = Image.open('./pics/disperation.jpg')
    st.image(img,use_column_width=True,caption='My life is a lie')

    st.markdown('''
    proviamo per un secondo a ragionare su un concetto fino ad ora trascurato: **cos'è la probabilità?**
    ''')

    st.warning('''
    **Attenzione:** da questo punto in poi l'autore potrebbe parlare di concetti apparentemente deliranti. Valuta attentamente
    se continuare nella lettura del post, potresti invece passare del tempo con i tuoi *congiunti*. 
    ''')

    st.subheader("Probabilistic thinking")

    st.markdown('''
    *"Possibili scenari si contendono le nostre vite mentre noi le stiamo lì a guardare"* 
    
    (Cit. di Cesare Cremonini che fa figo)  
    
    Il concetto di **probabilità** è usato da tutti noi nel linguaggio quotidiano, tuttavia, anche dopo un esame di probabilità e statistica lo 
    studente medio universitario farebbe fatica a definire puntualmente il concetto di probabilità. Ancora più difficile sarebbe
    per lui distinguere la *statistica* dalla *probabilità* che, **plot twist**, non sono la stessa cosa. ''')

    img = Image.open('./pics/probstat.jpg')
    st.image(img,use_column_width=True)

    st.markdown('''
    La distinzione delle due discipline in questo articolo è fuori luogo: l'articolo diventerebbe chilometrico, la quarantena finirebbe 
    prima del tuo arrivo alle conclusioni e mi abbandoneresti come Andy con Woody in Toy Story *(anche Andy bell'infame comunque)*.
    Ti dovrai quindi accontentare di (*una parziale*) definizione di probabiltà. Operativamente, possiamo definire la probabilità come
    ''')



    st.success('''
    **Probabilità**: un numero tra 0 e 1, dove, in termini approssimativi, 0 indica l'impossibilità
    che un evento accada e 1 indica la certezza che lo stesso si verifichi. Più è alta la probabilità di un *evento*, più è verosimile
    che quell'evento accada.
    ''')

    st.markdown('''
    Pensiamo quindi al nostro dado: ha sei facce e, se non è truccato, ogni faccia ha la stessa probabilità. Nei termini sopra definiti
    ogni faccia ha quindi una probabilità di 1/6 di apparire. Chiarito questo punto siamo pronti a ribattezzare il nostro dado con un nome trendy: 
    **random variable** *(se siete nazionalisti: variabile aleatoria. Oltretutto, alea in latino vuol dire proprio dado)*.
    ''')

    st.success('''
    **Random variable** (per gli amici *rv*): variabile il cui valore non è ancora definito: prima di lanciare il dado,
    sappiamo che risulterà un numero tra 1 e 6 ma non siamo in grado di determinare **con certezza** quale numero uscirà. L'esito è
    appunto **random, incerto**.
    ''')

    st.markdown('''
    Il seguente esempio potrebbe aiutarti a capire meglio la natura filosofica della rv: *immagina di aver vinto una scommessa con un amico.
    Il tuo guadagno dipende ora dal lancio di un dado: se esce 1 il tuo amico ti darà 1 euro, se esce 2 ti darà 2 euro, ecc*...
    
    Chiamiamo $X$ l'ammontare di soldi che vinceremo dal lancio del dado. **Prima** di lanciare il dado, $X$ è una variabile aleatoria,
    una quantità random tra gli 1 e i 6 euro. 
    ''')

    img = Image.open('./pics/stonks.jpg')
    st.image(img,use_column_width=True)

    st.markdown('''
    Nota una piccola differenza dall'uso che si fa della parola **random** nella lingua corrente: spesso usiamo il termine *"random"* per 
    indicare una situazione in cui può succedere di tutto (es.: i tanto amati *random party)*. In questo caso, invece, abbiamo un *random* molto più circostanziato: non sappiamo l'esatto esito, ma sappiamo con certezza che
    sarà un numero tra 1-6. Sappiamo inoltre che tutte le facce hanno la stessa probabilità di apparire.
    
    Possiamo collegare quest'ultima osservazione al concetto di random variable introducento un nuovo oggetto matematico: la **distribuzione di probabilità**
    ''')

    st.success('''
    **Distribuzione di probabilità**: legge matematica che lega i valori che una rv puo assumere alla probabilità con cui essi si presentano. Nel caso del nostro
    dado non truccato $P(X=k)=1/6$ dove $k=1,2,3,4,5,6.$
    ''')


    st.markdown('''
    
    Per avere un'infarinatura completa di probabilità, non ci resta che introdurre i concetti di **Expected Value** e **Variance**. Riprendiamo il caso
    sopra in cui abbiamo definito $X$ come la quantità random di soldi vinta dopo aver lanciato il dado. 
    
    A questo punto della lettura
    dovrei averti già infuso il *pessimismo cosmico* derivante dall'incapacità di capire con certezza su che lato cadrà il dado. Detto ciò, possiamo farci un'idea
    di quanto vinceremo? La risposta è **si**! Ed è proprio questo il ruolo dell'**expected value**:
    ''')

    st.success('''
    **Expected value**: Valore medio assunto dalla variabile aleatoria, viene calcolato come la somma di tutti gli esiti possibili, ciascuno moltiplicato per la probabilità
    che la distribuzione assegna a tal valore. Nel nostro caso, quantità di euro che possiamo aspettarci
    di vincere partecipando al gioco $\\frac{1}{6}*1 + \\frac{1}{6}*2 + ... +\\frac{1}{6}*6=3.5$
    ''')

    st.markdown('''
    Piccola nota di stile per gli *inguaribili romantici* tra di voi, in italiano il valore atteso viene anche chiamato
    **speranza matematica**.
    
    Definire invece il concetto di **variance** è più complicato senza indugiare nella notazione matematica. La varianza
    è definita come *la somma delle distanze al quadrato tra i valori possibili e l'expected value pesate per la loro probabilità*.
    ''')

    img = Image.open('./pics/lady.jpg')
    st.image(img,use_column_width=True)

    st.markdown('''
    Per il momento, non ti interessa capire nei dettagli la definizione sopra, ti basta interiorizzare la varianza come segue
    ''')


    st.success('''
    **Variance:** un numero (sempre positivo) che serve a quantificare la variabilità intrinseca di una rv. In particolare,
    (la sua radice quadrata) ci dà informazioni su come i valori di una r.v. siano *dispersi* attorno al suo valore atteso. 
    ''')
    
    st.markdown('''
    Se ricordi, nello scorso paragrafo avevamo osservato come, lanciando i nostri dadi, le frequenze osservate potessero non combaciare
    perfettamente con le nostre attese. La nozione di varianza descrive in qualche modo **questa brutta abitudine** di una quantità
    aleatoria di allontanarsi da dalle nostre aspettattive. Ricorda inoltre che i dadi erano identici: stiamo descrivendo una
    variabilità **intrinseca** nella natura del dado stesso.''')

    img = Image.open('./pics/expectations.jpg')
    st.image(img,use_column_width=True)

    st.subheader('Tornando a Kevin')

    st.markdown('''
    Dopo averti versato addosso una dose di teoria della quale *probabilmente* pesnavi di poter far a meno nella tua vita
    ''')

    img = Image.open('./pics/oil.jpg')
    st.image(img,use_column_width=True)


    st.markdown('''
    cerchiamo di capire il motivo per il quale ci stia girando intorno così tanto. Toriniamo a Kevin, alla *Kamchatka* e al problema
    di capire se i dadi siano truccati.
    
    Alla luce di quanto appreso sopra dovresti aver capito che ai dadi (come alle scale) *piace cambiare*. La nozione di varianza caratterizzante il dado 
    descrive come sia possibile ottenere esiti particolarmente diversi lanciandolo. Se non stiamo attenti, diventa quindi concreto 
    il rischio di **confondere la variabilità intrinseca del dado con lo scenario in cui i dadi sono truccati**.
    
    Per dare una (parziale) soluzione a questo problema possiamo utilizzare ciò che nella letteratura statistica viene definito come **hypothesis testing**.
    Spiegare nel dettaglio come funzioni questa metodologia diventerebbe **molto doloroso** per il lettore. L'idea di fondo di questa procedura,
    tuttavia, è piuttosto semplice:
    ''')

    st.success('''
    **Hypothesis testing**: Vogliamo confrontare due dadi per capire se uno dei due possa essere truccato. Tenendo conto che il cubo a sei facce
    è caratterizzato da una sua variabilità intrinseca (una varianza, una quantità che siamo ora in grado di calcolare) vogliamo verificare
    se il secondo si **discosti eccessivamente** dalle nostre aspettative, andando oltre la  semplice variabilità del primo. Se la differenza è grande,
    risulta ragionevole pensare che il dado sia truccato (ma non ne abbiamo ancora certezza).
    ''')

    st.markdown('''
    Un ulteriore esempio: abbiamo raccolto l'altezza di un campione di persone dalla popolazione italiana. Vogliamo ora capire se la media delle misurazioni
    raccolte si discosti o meno da quella nazionale (175 cm per gli uomini e 162.5 cm per le donne, quindi circa 169 cm). Se l'altezza media nel campione 
    fosse di 172 potremmo avere una distanza (tra 169 cm e 172 cm) **non statisticamente significative**. Se invece l'altezza media del nostro campione fosse 202 cm il discorso
    sarebbe decisamente diverso.
    
    Entrambi i risultati presentati sopra sono contesti *banali*: se Kevin ci frega perdiamo a risiko, se sbagliamo a stimare le altezze avremo
    una descrizione distorta di qualche cm dell'altezza media della popolazione. Immaginiamo però il caso più attuale in cui siamo interessati a capire l'**efficacia di una cura**.
    Spero tu possa intuire come in una situazione del genere risulti letteralmente **vitale** distinguere gli effetti del trattamento medico dall'aleatorietà
    caratterizzante i diversi casi clinici!
    
    ''')

    st.error('''**Nerd note**: per i più puntigliosi una precisazione è richiesta. Osservare una differenza di 3 cm nella popolazione
    potrebbe essere statisticamente significativo qualora avessimo un campione **relativamente grande**. In genereale, avere più dati
    ci permette di ridurre l'incertezza dei nostri calcoli: osservare la stessa differenza di 3 cm un milione di volte non è
    ascrivibile al semplice caso.''')


    st.subheader('''Finalmente le nostre stelle''')

    st.markdown('''
    Lo stesso problema con il quale *ti ho massacrato fino ad adesso* è riscontrabile nel nostro sondaggio: quando disaggreghiamo
    i dati è possibile che le differenze tra le proporzioni nelle varie categorie di risposte (esempio il rapporto con la religione
    visto separatamente per uomini e donne) sia **dovuto al caso**, alla variabilità del campione e non a una vera correlazione tra le due domande.
    
    Una quantità, legata al framework dell'hypotesis testing spiegato sopra, che ci può aiutare nella lettura di questi dati è
    il **p-value**:
    ''')

    st.success('''
    **P-value**: il p-value rappresenta, in un test di ipotesi, la probabilità che l'ipotesi testata sia attribuibile alla
    variabilità intrinseca del processo in analisi. Il p-value è quindi una probabilità, un numero tra 0 e 1! Un valore prossimo allo
    zero ci dice che è poco verosimile che la differenza analizzata sia riducibile ad un evento casuale. Un p-value vicino a 1, invece,
    ci dice che probabilmente le due differenze sono casuali.
    ''')

    st.markdown('''
    Ritrovi qui sotto lo stesso grafico generato sopra per il lancio dei tre dadi di Kevin. Sotto al grafico è riportato il p-value
    del test per verificare che i dadi siano significativamente diversi *(questa volta non lo sono, Kevin è stato onesto)*. Una **rule of thumb**
    (una regola operativa) comunemente adottata in letteratura è considerare **significative** solo le differenze caratterizzate da un p-value inferiore
    a 0.05.
    ''')


    np.random.seed(random_state)

    dices = pd.DataFrame(columns=['Dado1', 'Dado2', 'Dado3'], data=np.random.random_integers(low=1, high=6, size=(60, 3)))

    count_dices = pd.DataFrame(index=[1, 2, 3, 4, 5, 6], columns=['Dado1', 'Dado2', 'Dado3'])
    count_dices['Dado1'] = dices['Dado1'].value_counts(sort=False).values
    count_dices['Dado2'] = dices['Dado2'].value_counts(sort=False).values
    count_dices['Dado3'] = dices['Dado3'].value_counts(sort=False).values

    count_proportions = (count_dices / count_dices.sum()).round(2)
    x = count_proportions.columns

    #temp
    chi2_contingency(count_dices.values)[1]

    for i, j in enumerate(count_proportions.index.values):

        if (i == 0):

            fig = go.Figure(go.Bar(x=x, y=count_proportions.loc[j].values, name=str(j)))

        else:

            fig.add_trace(go.Bar(x=x, y=count_proportions.loc[j].values, name=str(j)))

    fig.update_layout(barmode='stack', legend_orientation='h')  # , legend=dict(x=0, y=1.3))

    st.plotly_chart(fig, use_container_width=True)

    st.write('P-value: ',chi2_contingency(count_dices.values)[1])

    st.markdown('''
    Grazie ai menù a tendina sotto puoi incrociare a coppie tutte le domande del questionario. Per ogni coppia verrà
    automaticamente calcolato il p-value del relativo test statistico: un p-value basso evidenzia la presenza di proporzioni
    statisticamente diverse tra le varie colonne plottate. Arrivato a questo punto puoi **pascolare con gioia**
    nei dati raccolti, buon divertimento.
    ''')

    final_questions = questions.copy()

    final_questions.remove(questions[6])
    final_questions.remove(questions[7])


    option_a = st.selectbox("Domanda", final_questions)
    option_b = st.selectbox("Stratificazione", final_questions)

    plot_cross = proportion_visualizer(df, qname_dict, inv_qname_dict[option_a], inv_qname_dict[option_b])  # pvalue 0.11

    st.plotly_chart(plot_cross, use_container_width=True)

    st.write(cross_tab(df, inv_qname_dict[option_a], inv_qname_dict[option_b]))

    st.write('P-value',chi2_contingency(pd.crosstab(df[inv_qname_dict[option_a]],df[inv_qname_dict[option_b]]).values)[1])

    st.warning('''Se il p-value risultasse un numero terminante con 'e-numero' sappi che ti sei imbattuto nella **notazione scientifica**.
    1e-01 è equivalente a 0.1, 1e-02 a 0.01, ecc... Se dovessi vedere quindi 1.3e-20, stai osservando un numero *molto molto* piccolo.''')

    st.subheader('''Conclusioni''')

    st.markdown('''
    Prima di lasciarvi, vorrei sintetizzare brevemente quanto esposto:
    
    * Abbiamo osservato la differenza tra dati **aggregati e disaggregati**, vedendo come, aggiungere una dimensione all'analisi,
    renda possibile apprezzare meglio le sfumature dei pareri raccolti;
    * Abbiamo visto gli oggetti più importanti studiati dalla **probabilità** e come interpretarli nella vita di tutti i giorni;
    * Abbiamo fatto una riflessione sul come deteminare, attraverso l'**hypothesis testing**, quando le differenze tra le proporzioni
    tra sotto campioni siano abbastanza grandi da essere considerate **significative**;
    * Abbiamo concluso che, forse, **Kevin non è cosi infame come pensavamo**.
    
    Siamo arrivati alla fine del nostro tour. Ti devo confessare che scrivere questo post è stato più difficile di quanto pensassi!
    Spero di essere stato sufficientemente chiaro e accetto volentieri suggerimenti/critiche per il futuro (non essere timido).
    
    Ora che sei un ninja delle random variable, sappi che per il prossimo articolo sto pensando di costruire un **soul mate finder probablity calculator**, stay tuned.
    ''')

    img = Image.open('./pics/finito.jpg')
    st.image(img,use_column_width=True)

    















    #img = Image.open('./pics/curtain.jpg')
    #st.image(img, use_column_width=True, caption='Il pippone sopra citato in agguato')

# st.write(df,inv_qname_dict[option],qname_dict)
