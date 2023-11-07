import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from streamlit_extras.metric_cards import style_metric_cards
from sklearn.metrics import accuracy_score
import pycountry
import geopandas
from collections import Counter
import matplotlib.gridspec as gridspec
import matplotlib.font_manager as fm
import time
import warnings
warnings.filterwarnings("ignore")

#Importar fonte para os gráficos
font = fm.FontProperties(fname='data/Anton-Regular.ttf')

#Apps
st.set_page_config(page_title="App Previsão Assinantes e Recomendações Filmes e Séries NETFLIX", page_icon= "🎥")
st.header("📊 Analytics Informações sobre Filmes/Séries NETFLIX", divider='red')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#load data #### DataFrame 
@st.cache_data
def load_data():
    data = pd.read_csv("data/netflix_titles.csv")
    return data

data = load_data()

#Sidebar de Opções
st.sidebar.markdown("▶ Selecione uma opção:")
st.sidebar.markdown("")
if st.sidebar.checkbox("❗**Informações**", True, key=0, help="Desmarque essa opção para visualizar outras opções"):
    #Layout da página
    st.subheader("📌 Informações sobre Filmes e Séries da Netflix:")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:    
        st.markdown("""<h6 style='text-align: justify;'>Nessa seção iremos analisar dados exploratórios sobre filmes,séries, elenco, diretores e países aonde foram produzidos pela Netflix. Análise consiste em EAD dos dados e visualização dos mesmos.</h6""", unsafe_allow_html=True)
        st.markdown("""<h6 style='text-align: justify;'>A Netflix é uma plataforma de streaming por assinatura que permite que os usuários assistam a filmes e programas de TV sem anúncios. .</h6""", unsafe_allow_html=True)
    with col2:
        st.image("img/netflix2.png", width=300)

    st.markdown("")
    st.markdown("""<h6 style='text-align: right;'>🌍 Fonte: [https://thecleverprogrammer.com]</h6""", unsafe_allow_html=True)
    st.divider()

################### Estudo Análise exploratórias dos dados #####################################

#tratamento dos dados nulos e ausentes
    data = data.dropna()

    st.markdown("🎲 Visualizar Dados: Títulos de filmes e séries da Netflix:")
    with st.expander("📚 **Visualizar Dados**"):
        st.dataframe(data, use_container_width=True)
        st.markdown("")    
        st.markdown("Fonte Dataset: https://kaggle.com")

        
############### Mostrar dados estatisticos ################################################ 

if st.sidebar.checkbox("📝 **Estatística**", False, key=1):
    st.subheader("🔎 Análise Estatística de Filmes e Séries:", divider='red')
    
    #Contagem e agrupando os dados  
    data2 = data.copy()
    data2 = data2.dropna(axis=0)
 
    pais = data2['country'].unique()
    Country = st.selectbox('🌎 Selecione o país:', pais)
    filtro = data2[data2.country == Country]

    total_movie_country = filtro[filtro.type == "Movie"].type.count()
    total_serie_country = filtro[filtro.type == "TV Show"].type.count()
    total_director_movie = filtro[filtro.type == "Movie"].director.count()
    total_director_serie = filtro[filtro.type == "TV Show"].director.count()
    
    st.markdown("")
    st.markdown("👫**Totalização de Filmes e Séries produzidos por país:**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
       st.metric(label="Filmes:", value= total_movie_country) 
    with col2:
       st.metric(label="Séries:", value=total_serie_country) 
    with col3:
       st.metric(label="Diretor/Filmes:", value=total_director_movie) 
    with col4:
       st.metric(label="Diretor/Série:", value= total_director_serie)       

    st.divider()

    total_movie = data[data.type == "Movie"].type.count()
    total_serie = data[data.type == "TV Show"].type.count()

    total_director1 = data[data.type == "Movie"].director.count()
    total_director2 = data[data.type == "TV Show"].director.count()
      
    total_elenco1 = data[data.type == "Movie"].cast.count()
    total_elenco2 = data[data.type == "TV Show"].cast.count()

    total_pais1 = data[data.type == "Movie"].country.count()
    total_pais2 = data[data.type == "TV Show"].country.count()

    #2 casas decimais
    #total = (f"{total_ass:,.2f}")
    #median = (f"{median_ass:,.2f}")

    st.markdown("👫**Totalização Filmes e Séries por: Elenco, Diretores e Países:**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Filmes:", value=total_movie) 
    with col2:
       st.metric(label="Série:", value=total_serie) 
    with col3:
        st.metric(label="Diretores/Filmes:", value=total_director1)  #5214
    with col4:
        st.metric(label="Diretores/Séries:", value=total_director2)  #184     
    
    st.markdown("")    
        
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Elenco/Filmes:", value=total_elenco1) 
    with col2:
       st.metric(label="Total Elenco/Séries:", value=total_elenco2) 
    with col3:
        st.metric(label="Total Filmes/Países:", value=total_pais1)  
    with col4:
        st.metric(label="Total Séries/Países:", value=total_pais2)       

    st.divider()
    style_metric_cards(background_color="#831010",border_left_color="#F71938",border_color="#FFC0CB",box_shadow="#F71938")
    


############ Mostrar Gráficos ########################################################

if st.sidebar.checkbox("📊 **Gráficos**", False, key=2):
    st.subheader("🌍 Netflix: Popularidade mundial", divider='red')
    if not st.checkbox('Ocultar gráfico 1', False, key=3):    
        st.markdown("")
        with st.spinner("Aguarde..."):
            time.sleep(20)

    #Gráfico 1 Mundial Mapa
        country = data['country']
        country = list(country)
        total = []
        for i in range(len(country)):
            total+=str(country[i]).split(", ")
        country = Counter(total)
        country = sorted(country.items(), key=lambda x : x[1],reverse=True)
        name = list(map(lambda x : x[0],country))
        count = list(map(lambda x : x[1],country))

        country_name = name[0:3] + name[4:11]
        country_name.reverse()
        country_count = count[0:3] + count[4:11]
        country_count.reverse()

        country_data = pd.DataFrame(name,count).reset_index()
        country_data.columns=['count', 'country']
        country_data = country_data.drop(3)
        country_data = country_data.reset_index(drop=True)
        country_data['country'] = country_data['country'].apply(lambda x : x.replace(",",""))

        not_have = {'South Korea' : 'KOR', 'West Germany' : 'DEU','Soviet Union':'SUN','East Germany':'DEU'}
        for i in range(len(country_data['country'])):
            if country_data.loc[i, 'country'] in not_have.keys():
                country_data.loc[i, 'country'] = not_have[country_data.loc[i, 'country']]

        country_data['country'] = country_data['country'].apply(lambda x : pycountry.countries.search_fuzzy(x)[0].alpha_3)
        country_data = country_data.groupby('country').sum()
        country_data = country_data.reset_index()

        world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
        world2 = world.merge(country_data,left_on ='iso_a3', right_on = 'country')

       
        fig, ax = plt.subplots(figsize=(25,10),facecolor="#363336")
        ax.patch.set_facecolor('#363336')
        world.plot(ax=ax, color ="#363336",edgecolor='black')
        world2.plot(column='count',ax=ax, cmap='OrRd', scheme='quantiles', edgecolor='black')
        plt.text(s="Netflix's global popularity.", x=-100 ,y=110, font=font,color='#F5E9F5', va="center",ha="left",fontsize=50)
        plt.axis('off')
        st.pyplot(fig)
          
        st.info("📌 Distribuição mundial de assinantes da Netflix")
        st.divider()

    ############# Gráfico 2 ################################################################
    if not st.checkbox('Ocultar gráfico 2', False, key=4): 
        st.subheader(" 🔟 10 países com maior nº de assinantes:", divider='red')

        labels = ['United States', 'Other Countries']
        sizes = [count[0], sum(count[1:])]
        explode = (0, 0.15)

        fig, ax = plt.subplots(figsize=(25,10),facecolor="#363336")
        ax.patch.set_facecolor('#363336')

        spec = gridspec.GridSpec(ncols=10, nrows=1, figure=fig)
        ax1 = fig.add_subplot(spec[0, :4],facecolor="#363336")
        ax2 = fig.add_subplot(spec[0, 5:],facecolor="#363336")

        ax1.pie(sizes, explode=explode, shadow=True, startangle=90, colors =['red','#706B70'])
        ax1.text(s=labels[0],x=-0.42,y=0.45, font=font,fontsize=34,va='center',ha='center')
        ax1.text(s=f"{round(sizes[0]/(sizes[0]+sizes[1]) * 100,1)}%",x=-0.42,y=0.2, font=font,fontsize=60,va='center',ha='center')
        ax1.text(s=labels[1],x=0.6,y=-0.05, font=font,fontsize=30,color='#F5E9F5',va='center',ha='center')
        ax1.text(s=f"{round(sizes[1]/(sizes[0]+sizes[1]) * 100,1)}%",x=0.6,y=-0.3, font=font,fontsize=50,color='#F5E9F5',va='center',ha='center')

        ax2.barh(y=country_name, width=country_count, color = 'red', alpha=0.8)
        for i in range(10):
            ax2.text(s=f"{country_name[i]}",x=-100,y=i,font=font,color='#F5E9F5', va="center",ha="right",fontsize=30)
            ax2.text(s=f"{round(country_count[i]/sum(count)*100,1)}%",x=country_count[i]+25,y=i,font=font,color='#F5E9F5', va="center",ha="left",fontsize=30)

        ax2.axis("off")
        ax.axis("off")
        ax.text(s="Quais países que a Netflix é mais popular?", x= 0,y=1.05, font=font,color='#F5E9F5',fontsize=50)
        st.pyplot(fig)
        st.info("📌 Os Estados Unidos possuem 35,5% da totalidade mundial de assinantes.")
        st.divider()

    ############# Gráfico 3 ################################################################
    

    ############# Gráfico 4 ################################################################
    if not st.checkbox('Ocultar gráfico 3', False, key=6): 
        st.subheader("📊 Quais são os gêneros favoritos de filmes e séries?", divider='red')

        movie_genre = []
        TV_genre = []
        for i in range(len(data)):

            genre =  data.loc[i,'listed_in'].split(", ")
            if data.loc[i,'type'] == 'TV Show':
                for j in genre:
                    TV_genre.append(j)
            else:
                for j in genre:
                    movie_genre.append(j)
                    
        movie_genre = Counter(movie_genre)
        TV_genre = Counter(TV_genre)

        movie_genre = pd.DataFrame(movie_genre.items())
        TV_genre = pd.DataFrame(TV_genre.items())

        movie_genre.columns = ['genre','movie_count']
        TV_genre.columns = ['genre','tv_count']

        movie_genre = movie_genre.sort_values(by= 'movie_count').reset_index(drop=True)
        TV_genre = TV_genre.sort_values(by= 'tv_count').reset_index(drop=True)

        movie_genre['per'] = round(movie_genre['movie_count'] / sum(movie_genre['movie_count']) * 100,2)
        TV_genre['per'] = round(TV_genre['tv_count'] / sum(TV_genre['tv_count']) * 100,2)

        fig, ax = plt.subplots(figsize=(25,20),facecolor="#363336")
        ax.patch.set_facecolor('#363336')
        spec = gridspec.GridSpec(ncols=21, nrows=23, figure=fig)
        ax1 = fig.add_subplot(spec[:10, :],facecolor="#363336")
        ax2 = fig.add_subplot(spec[12:,:],facecolor="#363336")

        ax1.barh(y=movie_genre['genre'][-5:], width = movie_genre['movie_count'][-5:], color = 'red',alpha=0.7)
        for i in range(15,20):
            ax1.text(s=movie_genre.loc[i,'genre'], x= movie_genre.loc[i,'movie_count'],y =i-15, va='center', ha='right',font=font, color = "#363336",fontsize=40)
            ax1.text(s=f"{movie_genre.loc[i,'per']}%", x= movie_genre.loc[i,'movie_count']+30,y =i-15, va='center', ha='left',font=font, color = '#F5E9F5',fontsize=40)
        ax1.set_yticks([])
        ax1.set_xticks([])

        ax2.barh(y=TV_genre['genre'][:5], width = TV_genre['tv_count'][-5:],color = '#F5E9F5',alpha=0.7)
        for i in range(17,22):
            ax2.text(s=TV_genre.loc[i,'genre'], x= TV_genre.loc[i,'tv_count'],y =i-17, va='center', ha='right',font=font, color = "#363336",fontsize=40)
            ax2.text(s=f"{TV_genre.loc[i,'per']}%", x= TV_genre.loc[i,'tv_count']+30,y =i-17, va='center', ha='left',font=font, color = '#F5E9F5',fontsize=40)
        ax2.set_yticks([])
        ax2.set_xticks([])

        ax.set_xticks([])
        ax.set_yticks([])

        direct = ['right', 'left','bottom','top']
        for di in direct:
            ax1.spines[di].set_visible(False)
            ax2.spines[di].set_visible(False)
            ax.spines[di].set_visible(False)

        plt.text(s= "Movie's genre", x=1, y= 10.5, font=font, fontsize=60, color = 'red')
        plt.text(s= "TV Show's genre", x=1, y= 4.5, font=font, fontsize=60, color = '#F5E9F5')

        st.pyplot(fig)
        st.info("📌Comparando os gêneros de filmes e séries favoritos do Netflix, temos que o 1º, 2º e 3º são os mesmos que Internacionais, Dramas, Comédias.")
   
        #Gráfico 5
        if not st.checkbox('Ocultar gráfico 4', False, key=7): 
            st.subheader("🌍 País aonde o ator mais atuou nos Filmes e Séries", divider='red')
            
            # dados exploratórios
            each_actor = []
            countries_actor = list(data['country'].value_counts()[:15].index)
            for countries in countries_actor:
                tmp = data[data['country'] == countries].copy()
                tmp = tmp.reset_index(drop=True)
                actors= []
                for i in range(len(tmp)):
                    if tmp.loc[i,'cast'] =='NaN' or type(tmp.loc[i,'cast']) !=str:
                        continue
                    elif "," not in tmp.loc[i,'cast']:
                        actors.append(tmp.loc[i,'cast'])
                    else:
                        for j in tmp.loc[i,'cast'].split(", "):
                            actors.append(j)
                print(countries, " : ",sorted(Counter(actors).items(), key= lambda x :x[1],reverse=True)[0])
                each_actor.append(sorted(Counter(actors).items(), key= lambda x :x[1],reverse=True)[0][0])
                
            countries_actor[0] = 'United States of America'    

            # Gráfico    
            fig, ax = plt.subplots(figsize=(25,15),facecolor="#363336")
            ax.patch.set_facecolor('#363336')
            world.plot(ax=ax, color ="#363336",edgecolor='black')
            world2.plot(column='count',ax=ax, cmap='OrRd', scheme='quantiles', edgecolor='black')
            plt.text(s="The actor who appeared the most", x=-200 ,y=110, font=font,color='#F5E9F5', va="center",ha="left",fontsize=30)
            plt.text(s="Netflix", x=135 ,y=110, font=font,color='red', va="center",ha="left",fontsize=80)

            plt.axis('off')

            for i in range(15):
                x,y = str(world[world['name'] == countries_actor[i]]['geometry'].centroid).split('(')[1].split(')')[0].split(' ')
                x,y = float(x),float(y)
                if i == 3:
                    y+=5
                if i == 4:
                    y-=5
                if i == 7:
                    y+=5
                plt.text(s=f"{each_actor[i]}", x=x ,y=y, font=font,color='#F5E9F5', va="center",ha="center",fontsize=25)
            st.pyplot(fig)
            st.info("📌Países aonde o ator mais atuou nos Filmes e Séries da Netflix.")


#Mensagem de atualização da página web    
st.toast("Página atualizada!", icon='✅')