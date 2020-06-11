import streamlit as st
import pandas as pd
import altair as alt

URL_DADOS_FINAL_FARM_TOGETHER = 'https://raw.githubusercontent.com/lucasHashi/maximizacao-de-utilidade-farm-together/master/final.csv'

dict_pt = {
    'idioma': 'Idioma',
    'idioma_sub': 'Os textos estão traduzidos, mas, como coleitei da Fandom.com, os dados estão em ingles',
    'titulo': 'Analise de Maximização de utilidade no Farm Together',
    'cap1_titulo': '1. "O que é" e "Como funciona" Farm Together',
    'cap1_texto': 'Para que aqui seja algo mais focado nos resultados práticos, escrevi todo o processo de coleta, processamento e análise em um post no Medium',
    'tipo_crop': 'Cultivo',
    'cap2_titulo': '2. Filtros e Gráficos',
    'cap3_titulo': '3. É isso ai.'
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
    st.write(dict_atual['idioma_sub'])
    #colheita_selecionada = st.selectbox(dict_atual['idioma'],['English', 'Portugues'])
    dict_atual = dict_pt if(colheita_selecionada == 'Portugues') else dict_en
    st.title(dict_atual['titulo'])

    st.write('## ' + dict_atual['cap1_titulo'])

    st.write(dict_atual['cap1_texto'])
    #st.write("[I'm an inline-style link with title](https://www.google.com 'Google's Homepage')")
    st.write("[O link do Post estará aqui, quando estiver pronto.]()")


    st.write('## ' + dict_atual['cap2_titulo'])
    filtro_ganho = st.selectbox('O que quer ganhar', ['Moedas', 'XP', 'Diamantes'])
    #st.write('### ' + dict_atual['cap2_titulo_dinheiro'])
    st.write('### Para ganhar ' + filtro_ganho)

    @st.cache
    def carregar_dados_finais():
        df_dados_final = pd.read_csv(URL_DADOS_FINAL_FARM_TOGETHER)
        return df_dados_final

    df_dados_final = carregar_dados_finais()
    filtro_colheita = st.selectbox('Tipo de colheita',['Todos'] + list(df_dados_final['tipo_colheita'].unique()))
    
    df_dados_filtrados = ''
    if(filtro_ganho == 'Moedas'):
        df_dados_filtrados = df_dados_final[df_dados_final['tipo_ganho'] == 'dinheiro_dinheiro']
    elif(filtro_ganho == 'XP'):
        df_dados_filtrados = df_dados_final.copy()
    elif(filtro_ganho == 'Diamantes'):
        df_dados_filtrados = df_dados_final[(df_dados_final['tipo_ganho'] == 'diamante_diamante') | (df_dados_final['tipo_ganho'] == 'dinheiro_diamante')]

    if(not filtro_colheita == 'Todos'):
        df_dados_filtrados = df_dados_filtrados[df_dados_final['tipo_colheita'] == filtro_colheita]

    filtro_nivel = st.slider('Seu nivel atual', 1, 100, 80)
    df_dados_filtrados = df_dados_filtrados[df_dados_final['nivel_fazenda'] <= filtro_nivel]

    df_dados_filtrados.reset_index(drop=True, inplace=True)

    if(st.checkbox('Mostrar tabela de dados')):
        st.write(df_dados_filtrados)
    
    st.subheader(filtro_colheita+ ' - Ganho x Tempo')
    chart = alt.Chart(df_dados_filtrados).mark_circle().encode(x='ganho_base', y='tempo', size='ganho_por_min', tooltip=['nome', 'ganho_por_min', 'ganho_base', 'tempo'])
    st.altair_chart(chart, use_container_width=True)

    n_melhores = st.slider('Procurar os melhores', 1, 10, 5)
    df_melhores = df_dados_filtrados[['url_img','nome', 'ganho_por_min', 'nivel_fazenda']].sort_values('ganho_por_min', ascending=False)
    df_melhores = df_melhores[:n_melhores]
    df_melhores['em_uma_hora'] = round(df_melhores['ganho_por_min'] * 60, 2)
    df_melhores.reset_index(drop=True, inplace=True)

    str_tabela_melhores = gerar_tabela_melhores(df_melhores, filtro_ganho)
    st.write(str_tabela_melhores)

    st.write('## ' + dict_atual['cap3_titulo'])
    st.write('''
    Sou **Lucas Belmonte**, cientista de dados, fotografo, malabrista.\n
    **Obrigado** por dar uma passada por aqui. \n
    Se quiser entender melhor como os dados foram coletador e tratados:\n
    [O link do Post estará aqui, quando estiver pronto.]()\n
    Se quiser os códigos desse web-app:\n
    [Estão disponiveis neste repositório](https://github.com/lucasHashi/farm-together-utility-maximization-app)
    ''')
    st.write('### 3.1 Contato')
    st.write('''
    [Portifólio](http://www.lucasbelmonte.com.br/)\n
    [Linkedin](https://www.linkedin.com/in/lucas-d-belmonte/)\n
    [Github](https://github.com/lucasHashi)\n
    [Portifólio fotografico](https://www.behance.net/lucasbelmonte)\n
    [Insta dos meus cães](https://www.instagram.com/mel_e_petit/)\n
    ''')

    st.write('### 3.2 Principais bibliotecas')
    st.write('''
    Pandas\n
    Altair, p/ gráficos\n
    Streamlit, p/ criação do web-app
    ''')

def gerar_tabela_melhores(df_melhores, filtro_ganho):
    str_tabela = 'Imagem | Nome | '+ filtro_ganho +'/Tempo | Nivel min. | '+ filtro_ganho +' em 1 hora \n --- | --- | --- | --- | --- \n'

    for _, linha in df_melhores.iterrows():
        url, nome, ganho_tempo, nivel, uma_hora = linha
        txt_url = '![alt text]({})'.format(url)
        
        txt_linha = '{} | {} | {} | {} | {} \n'.format(txt_url, nome, ganho_tempo, nivel, uma_hora)
        str_tabela += txt_linha

    return str_tabela





main()