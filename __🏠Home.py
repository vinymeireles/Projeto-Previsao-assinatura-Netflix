import streamlit as st

#Apps
st.set_page_config(page_title="App Previsão Assinantes e Recomendações Filmes e Séries NETFLIX", page_icon= "🎥")
st.header("🎬NETFLIX: Assinantes e Recomendações", divider='red')

st.sidebar.image("img/logoNetflix.jpg", width=300)

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#Textos na página
st.markdown("""<h6 style='text-align: justify; line-height: 1.5'>Essa aplicação demonstra uma análise exploratória dos dados de previsão de assinaturas trimestrais e recomendações de filmes e séries no NETFLIX, o conjunto de dados está disponível no kaggle. Essa aplicação utiliza Machine Learning - IA tem o intuito de demonstrar graficamente as correlações e previsões futuras da empresa, bem como recomendações para os seus clientes. </h6""", unsafe_allow_html=True) 

st.markdown("""<h6 style='text-align: justify; line-height: 1.5;'>A empresa NETFLIX é um serviço de streaming que oferece uma ampla variedade de séries, filmes e documentários premiados em milhares de aparelhos conectados à internet. Você pode assistir a quantos filmes e séries quiser, quando e onde quiser - tudo por um preço mensal acessível. Aqui você sempre encontra novidades. A cada semana, adicionamos novas séries e filmes. </h6""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("img/netflixtv.png", width= 350)
with col2:    
    st.markdown("""<h6 style='text-align: justify; line-height: 1.1'>A missão perspectivas e aproximam as pessoas. A missão da Netflix é entreter o mundo, e é por isso que levamos até você as melhores séries, documentários, filmes e jogos para celulares e dispositivos móveis. Nossos assinantes controlam o que querem ver e quando, com uma única assinatura.</h6""", unsafe_allow_html=True)
    st.markdown("""<h6 style='text-align: justify; line-height: 1.1'>Visão e valores: Os nove valores são: Julgamento, Comunicação, Impacto, Curiosidade, Inovação, Coragem, Paixão, Honestidade e Altruísmo. A Netflix valoriza os resultados que as pessoas apresentam.</h6""", unsafe_allow_html=True)

st.markdown("""<h6 style='text-align: right;'> 🌍 Fonte: [https://www.netflix.com/br/]</h6""", unsafe_allow_html=True) 
st.markdown("")

st.subheader("📋 Objetivos da Aplicação:", divider='red')
st.markdown("""<h6 style='text-align: justify; line-height: 1.5;'> Prever o número de assinaturas que a Netflix alcançará em um período de tempo é uma prática de negócios vital que permite planejar, criar estratégias e tomar decisões baseadas em dados. Ele melhora a eficiência operacional, o planejamento financeiro e a estratégia de conteúdo, contribuindo para seu sucesso e crescimento na indústria de streaming altamente competitiva. Utilizando Inteligência artificial Machine leaning, a aplicação poderá prever quantitativos de novos assinantes trimestrais, bem como recomendações e estatísticas de filmes e séries da empresa.</h6""", unsafe_allow_html=True)

st.markdown("""<h5 style='text-align: justify;'> ❎ Previsão de novas assinaturas Netflix:</h5""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<h6 style='text-align: justify;'> 1️⃣ Etapas da técnica de previsão de Séries Temporais: </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Explorar os dados históricos de crescimento de assinaturas da Netflix. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Pré-processar e limpar os dados. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Explorar e analisar padrões de séries temporais. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Escolha um modelo de previsão de séries temporais - ARIMA. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Treinar o modelo usando os dados de treinamento. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Prever futuras contagens de assinaturas da Netflix. </h6""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<h5 style='text-align: justify;'> 2️⃣ Etapas da técnica do sistema de recomendação: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Explorar os dados históricos de recomendação de filmes e séries da Netflix </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Analisar histórico de visualização de outros usuários com gostos e preferências semelhantes aos seus. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Analisar gêneros, categoria, descrição e mais informações sobre o conteúdo que você assistiu no passado. </h6""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<h5 style='text-align: justify;'> 3️⃣ Etapas da análise de dados da Netflix: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Explorar os dados históricos dos títulos, diretores, elenco, duração, avaliação. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Entender quais conteúdos estão disponíveis. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Entender as semelhanças entre os conteúdos. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Entender a rede entre atores e diretores. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Entender no que exatamente a Netflix está se concentrando. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔺 Análise de sentimentos dos conteúdos disponíveis na Netflix. </h6""", unsafe_allow_html=True)
st.divider()
st.markdown("""<h6 style='text-align: justify;'> 🌍 Fonte de dados: [https://flixable.com/] e [https://kaggle.com/] </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🌍 Fonte pesquisa: [https://thecleverprogrammer.com/] </h6""", unsafe_allow_html=True)

st.toast("Página atualizada!", icon='✅')