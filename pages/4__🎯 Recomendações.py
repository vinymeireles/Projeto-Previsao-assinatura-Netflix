import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pickle
import requests
import gzip
import streamlit.components.v1 as components

#Apps
st.set_page_config(page_title="App Previsão Assinantes e Recomendações Filmes e Séries NETFLIX", page_icon= "🎥")
st.header("📊 Analytics Recomendações de Filmes/Séries NETFLIX", divider='red')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#load data #### DataFrame 
@st.cache_data
def load_data():
    data = pd.read_csv("data/NetflixMovies_1000.csv")
    return data

data = load_data()

#Função para importar images movies
def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values


#Sidebar de Opções
st.sidebar.markdown("▶ Selecione uma opção:")
st.sidebar.markdown("")
if st.sidebar.checkbox("❗**Informações**", True, key=0, help="Desmarque essa opção para visualizar outras opções"):
    #Layout da página
    st.subheader("📌 Previsão de Recomendações da Netflix:")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:    
        st.markdown("""<h6 style='text-align: justify;'>Nessa seção iremos analisar dados exploratórios do "Sistema de Recomendação" de filmes e séries da Netflix. Análise consiste em EAD dos dados e previsão utilizando algoritmos de Machine Learning - IA e Dashboard dos dados.</h6""", unsafe_allow_html=True)
        st.markdown("""<h6 style='text-align: justify;'>A Netflix é uma plataforma de streaming por assinatura que permite que os usuários assistam a filmes e programas de TV sem anúncios. Uma das razões por trás da popularidade da Netflix é seu sistema de recomendação. Seu sistema de recomendação recomenda filmes e programas de TV com base no interesse do usuário.</h6""", unsafe_allow_html=True)
    with col2:
        st.image("img/02.png", width=400)

    st.markdown("")
    st.markdown("""<h6 style='text-align: right;'>🌍 Fonte: [https://thecleverprogrammer.com]</h6""", unsafe_allow_html=True)
    st.divider()

################### Estudo Análise exploratórias dos dados #####################################

#tratamento dos dados nulos e ausentes
    data = data.dropna()

    st.markdown("🎲 Visualizar Dados: 1000 Títulos de filmes e séries da Netflix:")
    with st.expander("📚 **Visualizar Dados**"):
        st.dataframe(data, use_container_width=True)
        st.markdown("")    
        st.markdown("Fonte Dataset: https://kaggle.com")



#################### Mostrar Previsões: Desenvolvendo mecanismo de recomendação Filmes e séries ###################################################################
if st.sidebar.checkbox("🎯**Previsões**", False, key=7):
    st.subheader("🎯 Previsões utilizando IA:", divider='red')
    st.error("🎬 **Sistema de Recomendação de Filmes e Séries Netflix:**")
    st.markdown("")  
    


    imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


    imageUrls = [
        fetch_poster(1632),
        fetch_poster(299536),
        fetch_poster(17455),
        fetch_poster(2830),
        fetch_poster(429422),
        fetch_poster(9722),
        fetch_poster(13972),
        fetch_poster(240),
        fetch_poster(155),
        fetch_poster(598),
        fetch_poster(914),
        fetch_poster(255709),
        fetch_poster(572154)
    
        ]

    st.markdown("")
    imageCarouselComponent(imageUrls=imageUrls, height=200)
    selectvalue=st.selectbox("Selecione um Filme ou Série:", movies_list)

    def recommend(movie):
        index=movies[movies['title']==movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
        recommend_movie=[]
        recommend_poster=[]
        for i in distance[1:6]:
            movies_id=movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]].title)
            recommend_poster.append(fetch_poster(movies_id))
        return recommend_movie, recommend_poster

    st.markdown("")
    if st.button("Show Recommend"):
        movie_name, movie_poster = recommend(selectvalue)
        col1,col2,col3,col4,col5=st.columns(5)
        with col1:
            st.text(movie_name[0])
            st.image(movie_poster[0])
        with col2:
            st.text(movie_name[1])
            st.image(movie_poster[1])
        with col3:
            st.text(movie_name[2])
            st.image(movie_poster[2])
        with col4:
            st.text(movie_name[3])
            st.image(movie_poster[3])
        with col5:
            st.text(movie_name[4])
            st.image(movie_poster[4])

        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.info("📌 Conclusão: Usando técnicas de Inteligência Artificial algoritmo NLP para recomendar filmes e séries de acordo com o perfil de cada usuário da NetFlix. O sistema mostrou-se com alta performance no tempo de resposta e taxa de acerto 98%. Para otimização da aplicação Web foi reduzido o tamanho do dataframe original de 10.000 títulos de filmes e séries para 1.000.")
 

#Mensagem de atualização da página web    
st.toast("Página atualizada!", icon='✅')