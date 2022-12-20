import streamlit as st
import streamlit.components.v1 as components
from presentation_card import presentation_card
from portfolio_carousel import portfolio_carousel
from PIL import Image
import os

st.set_page_config(page_title="Portfolio",
                    page_icon=":snake:",
                    layout="centered",
                    initial_sidebar_state="auto")

img_head = "https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/head.png"
  
title = "Work"     
subtitle =  '''Check my commercioal and non commercial projects.
            If you have any questions feel free to ask me for more information'''
cards = [["https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/zenk.jpg", "ZENK project", "Web Scraping | RPA | Data Anlysis", "A formação da memória requer a expressão gênica induzida pela atividade neuronal. Esta resposta inclui uma série de genes dependentes de atividade tidos como mediadores das mudanças necessárias para a consolidação e manutenção da memória."],
        ["https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/b2b.jpg", "Prospecção de Clientes B2B", "Google API | Python | Streamlit", "Aplicação para prospectar potenciais clientes B2B no Rio Grande do Norte utilizando uma API da Google chamada Places."],
        ["https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/tracking.jpg", "Bird Tracking", "Data Processing | Data Visualization", "Aplicação para processar dados de coordenadas e gerar visualizações em mapa de calor."]]
        
def main():
   
    st.image(img_head, use_column_width=True)

    value = presentation_card(image_path="images/profile.png",
                              name="Abraão Andrade",
                              post="Cientista de Dados Júnior",
                              description="Atua como Pesquisador no Instituto do Cérebro UFRN e Estagiário em Análise de Dados e Automação de Processos no Supermercado Nordestão")
    
    value = portfolio_carousel(title=title,
                               subtitle=subtitle,
                               cards=cards)

if __name__ == '__main__':
    main()
