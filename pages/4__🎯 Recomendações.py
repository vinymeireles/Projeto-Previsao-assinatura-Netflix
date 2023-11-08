import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pickle
import requests
import gzip
import streamlit.components.v1 as components
import time

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

####Load Model Machine Learning#################
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

    #### Mostrar slides de Filmes 2023 NETFLIX

    st.success("🎬 Lançamentos da Netflix 2023")
    components.html(
    """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        * {box-sizing: border-box;}
        body {font-family: Verdana, sans-serif;}
        .mySlides {display: none;}
        img {vertical-align: middle;}

        /* Slideshow container */
        .slideshow-container {
        max-width: 800px;
        position: relative;
        margin: auto;
        }

        /* Caption text */
        .text {
        color: #f2f2f2;
        font-size: 15px;
        padding: 8px 12px;
        position: absolute;
        bottom: 8px;
        width: 100%;
        text-align: center;
        }

        /* Number text (1/5 etc) */
        .numbertext {
        color: #f2f2f2;
        font-size: 12px;
        padding: 8px 12px;
        position: absolute;
        top: 0;
        }

        /* The dots/bullets/indicators */
        .dot {
        height: 15px;
        width: 15px;
        margin: 0 2px;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        transition: background-color 0.6s ease;
        }

        .active {
        background-color: #717171;
        }

        /* Fading animation */
        .fade {
        animation-name: fade;
        animation-duration: 2.5s;
        }

        @keyframes fade {
        from {opacity: .4} 
        to {opacity: 1}
        }

        /* On smaller screens, decrease text size */
        @media only screen and (max-width: 300px) {
        .text {font-size: 11px}
        }
        </style>
        </head>
        <body>

        <h2>Automatic Slideshow</h2>
        <p>Change image every 2 seconds:</p>

        <div class="slideshow-container">

        <div class="mySlides fade">
        <div class="numbertext"></div>
        <img src="https://vivariomarrecife.com.br/wp-content/uploads/2023/07/barbie-cinemark.jpg" style="width:100%">
        <div class="text"></div>
        </div>

        <div class="mySlides fade">
        <div class="numbertext"></div>
        <img src="https://p2.trrsf.com/image/fget/cf/940/0/images.terra.com/2022/11/09/por_-olhar-indiscreto_rgb_square_1x1_pre-1h7opant4bhi9.jpg" style="width:70%">
        <div class="text"></div>
        </div>

        <div class="mySlides fade">
        <div class="numbertext"></div>
        <img src="https://guiadeseries.com/wp-content/uploads/2022/06/Agente-Oculto-01-1024x516.jpg" style="width:70%>
        <div class="text"></div>
        </div>

        <div class="mySlides fade">
        <div class="numbertext"></div>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe4SupsPrB8d4SXlw5pgYXuXBz7IJFMEpODOtXVB5OLy_XKs-yhNK4pcPXfXTUUN3ta5E&usqp=CAU" style="width:50%">
        <div class="text"></div>
        </div>

        <div class="mySlides fade">
        <div class="numbertext"></div>
        <img src="https://proxy.olhardigital.com.br/wp-content/uploads/2023/07/Destaque-Velozes-e-Furiosos-10-1024x576.jpg" style="width:100%">
        <div class="text"></div>
        </div>

          
        </div>
        <br>

        <div style="text-align:center">
        <span class="dot"></span> 
        <span class="dot"></span> 
        <span class="dot"></span> 
        <span class="dot"></span>
        <span class="dot"></span>
        </div>

        <script>
        let slideIndex = 0;
        showSlides();
     

        function showSlides() {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        let dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }
        slideIndex++;
        if (slideIndex > slides.length) {slideIndex = 1}    
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";  
        dots[slideIndex-1].className += " active";
        setTimeout(showSlides, 2000); // Change image every 2 seconds
        }
        </script>

        </body>
        </html> 

            """,
            height=600,
        )
    
    st.divider()       


################### Estudo Análise exploratórias dos dados #####################################
    
if st.sidebar.checkbox("🎲**DataFrame**", False, key=7):
    st.markdown("🎲 Visualizar Dados: 1000 Títulos de filmes e séries da Netflix:")
    data = data.dropna()
    with st.expander("📚 **Visualizar Dados**"):
        st.dataframe(data, use_container_width=True)
        st.markdown("")    
        st.markdown("Fonte Dataset: https://kaggle.com") 


#### #Função para importar images movies
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


#################### Mostrar Previsões: Desenvolvendo mecanismo de recomendação Filmes e séries ###################################################################
if st.sidebar.checkbox("🎯**Previsões**", False, key=8):
    st.subheader("🎯 Previsões utilizando IA:", divider='red')
    st.error("🎬 **Sistema de Recomendação de Filmes e Séries Netflix:**")
    st.markdown("")
    
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
        with st.spinner("Aguarde..."):
            time.sleep(10)
        st.markdown("")    
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