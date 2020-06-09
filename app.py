import streamlit as st
import pandas as pd

URL_DADOS_FINAL_FARM_TOGETHER = 'https://raw.githubusercontent.com/lucasHashi/maximizacao-de-utilidade-farm-together/master/final.csv'

dict_pt = {
    'idioma': 'Idioma',
    'titulo': 'Analise de Maximização de utilidade no Farm Together',
    'titulo_descricao_steam': 'Da loja da Steam:',
    'descricao_steam': 'Comece do zero, com um pequeno lote e termine com uma fazenda impressionante que se estende além de onde os seus olhos possam ver!',
    'descricao': 'Então a ideia aqui é analisar os ganhos das categorias de plantações e, idealmente, concluir com uma plantação otimizada',
    'cap1_titulo': '1. O que é Farm Together',
    'tipo_crop': 'Cultivo'
}
dict_en = {
    'idioma': 'Language',
    'titulo': 'Utility Maximization Analysis in Farm Together',
    'titulo_descricao_steam': 'From the Steam shop:',
    'descricao_steam': 'Start from scratch with a small plot and end with an impressive farm that extends beyond where your eyes can see!',
    'descricao': 'So the idea here is to analyze the earnings of the plantation categories and, ideally, conclude with an optimized plantation',
    'cap1_titulo': '1. What is Farm Together'
}

def main():
    dict_atual = dict_pt
    colheita_selecionada = st.selectbox(dict_atual['idioma'],['Portugues'])
    #colheita_selecionada = st.selectbox(dict_atual['idioma'],['English', 'Portugues'])
    dict_atual = dict_pt if(colheita_selecionada == 'Portugues') else dict_en
    st.title(dict_atual['titulo'])

    st.write('## '+dict_atual['cap1_titulo'])

    st.write('#### '+dict_atual['titulo_descricao_steam'])
    st.write('> '+dict_atual['descricao_steam'])

    st.write(' '+dict_atual['descricao'])

    @st.cache
    def carregar_dados_finais():
        df_dados_final = pd.read_csv(URL_DADOS_FINAL_FARM_TOGETHER, sep='?')
        return df_dados_final
    
    st.write(f'''
    ### São 5 categorias de produtos:
    ![alt text](https://vignette.wikia.nocookie.net/farmtogether/images/c/c3/Carrot.png/revision/latest?cb=20190331180358 "CROPS")
    {dict_atual['tipo_crop']}
    ''')





main()