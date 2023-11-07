import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
pio.templates.default = "plotly_white"
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from streamlit_extras.metric_cards import style_metric_cards

import warnings
warnings.filterwarnings("ignore")


#Apps
st.set_page_config(page_title="App Previsão Assinantes e Recomendações Filmes e Séries NETFLIX", page_icon= "🎥")
st.header("🎬 Analytics Assinantes NETFLIX📊", divider='red')

# Style
with open('style.css')as f:
   st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#load data #### DataFrame Assinantes Trimestrais
@st.cache_data
def load_data():
    data = pd.read_csv("data/Netflix-Subscriptions2.csv")
    return data

df = load_data()

#load data #### DataFrame Dados dos Assinantes 
@st.cache_data
def load_data():
    data = pd.read_csv("data/Netflix-userbase.csv")
    return data

df2 = load_data()


#Sidebar de Opções
st.sidebar.markdown("▶ Selecione uma opção:")
st.sidebar.markdown("")
if st.sidebar.checkbox("❗**Informações**", True, key=0, help="Desmarque essa opção para visualizar outras opções"):
    #Layout da página
    st.subheader("📌 Previsão de Assinaturas trimestrais da Netflix:")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:    
        st.markdown("""<h6 style='text-align: justify;'>Nessa seção iremos analisar dados exploratórios de assinantes trimestral da Netflix, bem como o perfil de cada cliente, país com maior nº de assinantes e outros. Análise consiste em EAD dos dados e previsão utilizando algoritmos de machine learning e Dashboard dos dados.</h6""", unsafe_allow_html=True)
        st.markdown("""<h6 style='text-align: justify;'>Usando técnicas como previsão de séries temporais, a Netflix pode estimar o número esperado de novos assinantes em um determinado período de tempo e entender melhor o potencial de crescimento de seus negócios.</h6""", unsafe_allow_html=True)
    with col2:
        st.image("img/01.jpg", width=400)

    st.markdown("")
    st.markdown("""<h6 style='text-align: right;'>🌍 Fonte: [https://thecleverprogrammer.com]</h6""", unsafe_allow_html=True)
    st.divider()

################### Estudo Análise exploratórias dos dados #####################################

    #tratamento dos dados nulos e ausentes
    df = df.dropna()
    df2 = df2.dropna()

    #if st.sidebar.checkbox("🎲 **Dataset**", False, key=1):
    st.markdown("🎲 **Visualizar Dados Assinantes:**")
    with st.expander("📚 **Assinaturas Trimestrais**"):
        st.dataframe(df, use_container_width=True)
        st.markdown("")    
        st.markdown("Fonte Dataset: https://kaggle.com")

    with st.expander("📚 **Perfil dos Assinantes**"):
        st.dataframe(df2, use_container_width=True)
        st.markdown("")    
        st.markdown("Fonte Dataset: https://kaggle.com")

#Tratar os dados date:
df['Time Period'] = pd.to_datetime(df['Time Period'], format='%d/%m/%Y', dayfirst = True)     

df2['Join Date'] = pd.to_datetime(df2['Join Date'])
df2['Last Payment Date'] = pd.to_datetime(df2['Last Payment Date'])
        
############### Mostrar dados estatisticos ################################################ 

if st.sidebar.checkbox("📝 **Estatística**", False, key=2, help="Estatística de Perfil dos Assinantes"):
    st.subheader("🔎 Análise Estatística do Perfil dos Assinantes:", divider='red')
    
    #Contagem de assinantes por ano e agrupando os dados   
    ano = df['Year'].unique()
    year = st.selectbox('📅 Selecione o ano:', ano)
    filtro = df[df.Year == year]
    total_ass = filtro.Subscribers.sum()
    median_ass = filtro.Subscribers.mean()

    #2 casas decimais
    total = (f"{total_ass:,.2f}")
    median = (f"{median_ass:,.2f}")

    st.markdown("👫**Total de assinantes por ano:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Ano:", value=year) 
    with col2:
       st.metric(label="Total por ano:", value=total) #107.890.000
    with col3:
        st.metric(label="Média anual:", value=median)   
    st.divider()
    
    #### Estatísticas de Perfil dos assinantes Netflix #######################################################

    # A idade dos assinantes mais frequentes
    idade_freq = df2['Age'].value_counts().idxmax()

    # O número de assinantes em cada tipo de assinatura
    #Basic       999
    #Standard    768
    #Premium     733

    basic = df2[df2.SubscriptionType == "Basic"].SubscriptionType.count()
    standard = df2[df2.SubscriptionType == "Standard"].SubscriptionType.count()
    premium = df2[df2.SubscriptionType == "Premium"].SubscriptionType.count()

    # Total de dispositivos por conta
    #Laptop        636
    #Tablet        633
    #Smartphone    621
    #Smart TV      610
    laptop = df2[df2.Device == "Laptop"].Device.count()
    tablet = df2[df2.Device == "Tablet"].Device.count()
    smartphone = df2[df2.Device == "Smartphone"].Device.count()
    smartTV  = df2[df2.Device == "Smart TV"].Device.count()

    # O número de assinantes de ambos os sexos (masculino, feminino)
    male_count = df2[df2.Gender == "Male"].Gender.count()
    female_count = df2[df2.Gender == "Female"].Gender.count() 

    # O país com mais assinantes
    pais_max = df2['Country'].value_counts().idxmax()

    # O país com menor número de assinantes
    pais_min = df2['Country'].value_counts().idxmin()

    # O dispositivo mais usado
    device_max = df2['Device'].value_counts().idxmax()

    #Resultados das variáveis Metrics
    st.markdown("👫**Perfil dos assinantes Netflix:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Feminino:" , value = female_count)
    with col2:
        st.metric(label="Masculino: ", value = male_count)
    with col3:
        st.metric(label = "Total de Assinantes: ", value = male_count+female_count)    


    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Idade assinantes + frequente:" ,value= idade_freq)
    with col2:
        st.metric(label="O dispositivo + usado:" ,value= device_max)       
    with col3:
        st.metric(label="País com + assinantes:" ,value= pais_max)   


    st.divider()
    st.markdown("👫**Nº de assinantes por plano 💳:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Plano Básico:" ,value= basic)
    with col2:
        st.metric(label="Plano Standard:" ,value= standard)       
    with col3:
        st.metric(label="Plano Premium:" ,value= premium)
   

    st.divider()
    st.markdown("💻**Total de Dispositivos:** 📱📺")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Laptop:" ,value= laptop)
    with col2:
        st.metric(label="Total Tablet:" ,value= tablet)       
    with col3:
        st.metric(label="Total Smartphone:" ,value= smartphone)
    with col4:
        st.metric(label="Total Smart TV:" ,value= smartTV)
    
    style_metric_cards(background_color="#831010",border_left_color="#F71938",border_color="#FFC0CB",box_shadow="#F71938")

############ Mostrar Gráficos ########################################################
#### Gráficos de perfil de assinantes:

if st.sidebar.checkbox("📊 **Gráficos Perfil**", False, key=8, help="Perfil de Assinantes"):
    st.subheader("📈 Dashboard Perfil dos Assinantes:", divider='red')
    if not st.checkbox('Ocultar gráfico 1', False, key=9):   

        #calcular a receita mensal por plano 
        Basic = df2.loc[df2['SubscriptionType']=='Basic','Monthly Revenue'].sum()
        Standard = df2.loc[df2['SubscriptionType']=='Standard','Monthly Revenue'].sum()
        Premium  = df2.loc[df2['SubscriptionType']=='Premium','Monthly Revenue'].sum()

        RevData = {'SubscriptionType':['Basic','Standard','Premium'],'Monthly Revenue':[Basic,Standard,Premium]}

        #GRÁFICO Receita mensal por tipo de assinatura
        fig, ax = plt.subplots(figsize = (12,6))
        ax = sns.barplot(x = 'SubscriptionType', y = 'Monthly Revenue', data=RevData)
        ax = plt.title('Receita mensal total de cada tipo de assinatura Netflix')
        plt.style.use('default')
        st.pyplot(fig, use_container_width=True)
        st.info("📌 O plano de assinatura da Netflix mais vendido é o Básico.")
        st.divider()

    if not st.checkbox('Ocultar gráfico 2', False, key=10):
        devices = df2['Device'].value_counts()

        #GRÁFICO Distribuição dos dispositivos utilizados pelos assinantes
        st.markdown("⭕ Distribuição de dispositivos entre os assinantes")
        explode = (0.1, 0, 0, 0)
        colors = ['#780909','#43465e', '#c1071e', '#073763']
        fig, ax = plt.subplots(figsize = (6,6))
        ax = plt.pie(devices,labels=devices.index,autopct='%.2f%%', explode=explode, colors=colors)
        ax = plt.title('Dispositivos que são usados para Netflix')
        plt.style.use(['dark_background'])
        st.pyplot(fig, use_container_width=True)
        st.info("📌 Há um equilibro entre todos os tipos de dispositivos utilizados pelos assinantes da Netflix.")
        st.divider()

    if not st.checkbox('Ocultar gráfico 3', False, key=11):
        gender = df2['Gender'].value_counts()

        #GRÁFICO Distribuição por sexo numeros de assinantes
        st.markdown("⭕ Distribuição por sexo entre os assinantes")
        colors = ['#780909','#43465e']
        explode = (0.2, 0)
        fig, ax = plt.subplots(figsize = (6,6))
        ax = plt.pie(gender,labels=gender.index,autopct='%.2f%%', colors=colors, explode=explode)
        plt.style.use(['dark_background'])
        st.pyplot(fig, use_container_width=True)
        st.info("📌 50,8% dos assinantes da Netflix são do sexo Feminino.")
        st.divider()
  
    if not st.checkbox('Ocultar gráfico 4', False, key=12):
        #Contagens de tipos de assinatura por país
        fig, ax = plt.subplots()
        subscription = df2.groupby(['Country', 'SubscriptionType'])['User ID'].count().unstack()
        colors = ['#DC143C','#43465e','#FFEBCD']

        subscription.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)
        plt.title('Total de Planos de Assinatura por país')
        plt.xlabel('País')
        plt.ylabel('Nº de Assinantes')
        plt.xticks(rotation=45)
        plt.legend(title='Planos de Assinaturas')
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()   
          
        st.info("📌 Os países com maior número de assinantes em todos os planos são: Estados Unidos e Espanha.")
        st.divider()

    if not st.checkbox('Ocultar gráfico 5', False, key=13):    
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df2, x='Device', hue='Gender', palette='Set1')

        plt.xlabel('Dispositivos')
        plt.ylabel('Quant')
        plt.title('Distribuição de dispositivos por sexo')
        plt.legend(title='Gender', loc='upper right')
        plt.tight_layout()
        st.pyplot()   
        
        st.info("📌 Os dispositivos mais usados são: Smartphone: Masculino e Tablet: Feminino.")
        st.divider()

    if not st.checkbox('Ocultar gráfico 6', False, key=14):   
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df2, x='Device', hue='SubscriptionType', palette='Set1')
     
        plt.xlabel('Dispositivos')
        plt.ylabel('Quant')
        plt.title('Distribuição de tipo de assinatura por dispositivo')
        plt.legend(title='Subscription Type', loc='upper right')
        plt.tight_layout()
        st.pyplot() 

        st.info("📌 O plano básico é o mais utilizado em todos os dispositivos.")
        st.divider()

#### Gráficos de Assinaturas Trimestrais
if st.sidebar.checkbox("📊 **Gráficos Trimestral**", False, key=3, help="Assinanturas Trimestral"):
    st.subheader("📈 Dashboard Assinanturas Trimestrais:", divider='red')
    if not st.checkbox('Ocultar gráfico 1', False, key=5):    
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Time Period'],
                         y=df['Subscribers'],
                         mode='lines', name='Subscribers'))
        fig.update_layout(title='Netflix: Crescimento trimestral de assinaturas', xaxis_title='Date', yaxis_title='Netflix Subscriptions')
        
        st.plotly_chart(fig)
        st.info("📌 Há um crescimento exponencial de novos assinantes da Netflix desde 2013 até 2023.")
        st.divider()

    if not st.checkbox('Ocultar gráfico 2', False, key=6): 
        
        #Exibir taxa de crescimento trimestral dos assinantes da Netflix
        df['Quarterly Growth Rate'] = df['Subscribers'].pct_change() * 100

        #Crie uma nova coluna para a cor da barra (verde para crescimento positivo, vermelho para crescimento negativo)
        df['Bar Color'] = df['Quarterly Growth Rate'].apply(lambda x: 'green' if x > 0 else 'red')

        # Trace a taxa de crescimento trimestral usando gráficos de barras
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Time Period'],
            y=df['Quarterly Growth Rate'],
            marker_color=df['Bar Color'],
            name='Taxa de crescimento trimestral'
        ))
        fig.update_layout(title='Taxa de crescimento de assinaturas trimestrais da Netflix',
                        xaxis_title='Periodo de Tempo',
                        yaxis_title='Taxa de crescimento trimestral (%)')
        st.plotly_chart(fig)
        st.info("📌 Há um declínio de números de novos assinantes no 1º trimestre de 2022.")
        st.divider()

    if not st.checkbox('Ocultar gráfico 3', False, key=7): 
        #  taxa de crescimento anual
        df['Year'] = df['Time Period'].dt.year
        yearly_growth = df.groupby('Year')['Subscribers'].pct_change().fillna(0) * 100

        # Create a new column for bar color (green for positive growth, red for negative growth)
        df['Bar Color'] = yearly_growth.apply(lambda x: 'green' if x > 0 else 'red')

        # Plot the yearly subscriber growth rate using bar graphs
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Year'],
            y=yearly_growth,
            marker_color=df['Bar Color'],
            name='Taxa de crescimento anual'
        ))
        fig.update_layout(title='Taxa anual de crescimento de assinantes da Netflix',
                        xaxis_title='Ano',
                        yaxis_title='Taxa de crescimento anual (%)')
        
        st.plotly_chart(fig)
        st.info("📌 O maior índice registrado no crescimento de novos assinantes da Netflix foi no ano de 2014, ao contrário houve uma queda no ano de 2022.")
        st.divider()


#################### Mostrar Previsões ###################################################################


if st.sidebar.checkbox("🎯**Previsões**", False, key=4, help="Previsões utilizando Inteligência Artificial"):
    st.subheader("🎯 Previsões utilizando IA:", divider='red')
    st.error("👫**Prever número total de assinantes trimestrais:**")
      
    ####### Previsões utilizando machine learning #########################################################################################
    
    #PREPARAÇÃO DOS DADOS
    #USANDO ARIMA PARA PREVER ASSINATURAS TRIMESTRAIS DA NETFLIX
    time_series = df.set_index('Time Period')['Subscribers']
    
    differenced_series = time_series.diff().dropna()

    #Calcular valores séries temporais
    p, d, q = 1, 1, 1
    model = ARIMA(time_series, order=(p, d, q))
    results = model.fit()
       
    #Fazer previsões usando o modelo treinado para prever o número de assinantes para os próximos x trimestres:
    future_steps = st.slider("Selecione um período trimestral:", 1, 20, 5)

    #future_steps = 5
    predictions = results.predict(len(time_series), len(time_series) + future_steps - 1)
    predictions = predictions.astype(int)

    with st.expander("📈**Visualizar a Série Temporal Prevista**"):
        st.table(predictions)
    st.divider()

    #Visualizar os resultados da Previsão de Assinaturas da Netflix para os próximos x trimestres:
    # Create a DataFrame with the original data and predictions
    forecast = pd.DataFrame({'Original': time_series, 'Predictions': predictions})

    # Plot the original data and predictions
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=forecast.index, y=forecast['Predictions'],
                            mode='lines', name='Previsão'))

    fig.add_trace(go.Scatter(x=forecast.index, y=forecast['Original'],
                            mode='lines', name='Atual'))

    fig.update_layout(title='Previsões de assinatura trimestral da Netflix',
                    xaxis_title='Período de Tempo',
                    yaxis_title='Assinantes',
                    legend=dict(x=0.1, y=0.9),
                    showlegend=True)

    st.plotly_chart(fig)
   
    st.info("📌 Usando técnicas de Inteligência Artificial como previsão de séries temporais ARIMA, a Netflix pode estimar o número esperado de novos assinantes em um determinado período de tempo e entender melhor o potencial de crescimento de seus negócios. Com base nos resultados apresentados nos próximos trimestres, a tendência que o [Nº de novos assinantes] da NetFlix aumentem com o tempo, melhorando a eficiência operacional, o planejamento financeiro, a competividade e a estratégia de conteúdo.")
 

#Mensagem de atualização da página web    
st.toast("Página atualizada!", icon='✅')