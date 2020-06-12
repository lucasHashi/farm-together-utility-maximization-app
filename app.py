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
    'cap2_titulo': '2. Filtros e Gráficos',
    'cap2_o_que_ganhar': 'O que quer ganhar',
    'cap2_tipos_ganhos': ['Moedas', 'XP', 'Diamantes'],
    'cap2_para_ganhar': 'Para ganhar',
    'cap2_tipo_colheita': 'Tipo de colheita',
    'cap2_todos': 'Todos',
    'cap2_seu_nivel': 'Seu nivel atual',
    'cap2_mostrar_dados': 'Mostrar tabela de dados',
    'cap2_ganhoxtempo': 'Ganho x Tempo',
    'cap2_melhores': 'Procurar os melhores',
    'tabela_imagem': 'Imagem',
    'tabela_nome': 'Nome',
    'tabela_tempo': 'Tempo',
    'tabela_nivel_min': 'Nivel min.',
    'tabela_1_hora': 'em 1 hora',
    'cap3_titulo': '3. É isso ai.',
    'cap3_texto': '''
        Sou **Lucas Belmonte**, cientista de dados, fotografo, malabrista.\n
        **Obrigado** por dar uma passada por aqui. \n
        Se quiser entender melhor como os dados foram coletador e tratados:\n
        [O link do Post estará aqui, quando estiver pronto.]()\n
        Se quiser os códigos desse web-app:\n
        [Estão disponiveis neste repositório](https://github.com/lucasHashi/farm-together-utility-maximization-app)
    ''',
    'cap3_links': '''
        [Portifólio](http://www.lucasbelmonte.com.br/)\n
        [Linkedin](https://www.linkedin.com/in/lucas-d-belmonte/)\n
        [Github](https://github.com/lucasHashi)\n
        [Portifólio fotografico](https://www.behance.net/lucasbelmonte)\n
        [Insta dos meus cães](https://www.instagram.com/mel_e_petit/)\n
    ''',
    'cap3.1_contato': '3.1 Contato',
    'cap3.2_biblio': '3.2 Principais bibliotecas',
    'cap3.2_texto': '''
        Pandas\n
        Altair, p/ gráficos\n
        Streamlit, p/ criação do web-app
    ''',
    'link_post': 'O link do Post estará aqui, quando estiver pronto.'
}
dict_en = {
    'idioma': 'Idiom',
    'idioma_sub': 'Some columns names are in Portuguese',
    'titulo': 'Farm Together Utility Maximization App',
    'cap1_titulo': '1. "What it is" and "How works" Farm Together',
    'cap1_texto': 'To that here be focused in the pratic results, i wrote the colection and analyses data process in an Medium post',
    'cap2_titulo': '2. Filters and Graphs',
    'cap2_o_que_ganhar': 'What you want to earn',
    'cap2_tipos_ganhos': ['Coins', 'XP', 'Diamonds'],
    'cap2_para_ganhar': 'To gain',
    'cap2_tipo_colheita': 'Harvestable type',
    'cap2_todos': 'All',
    'cap2_seu_nivel': 'Your farm level',
    'cap2_mostrar_dados': 'Show data table',
    'cap2_ganhoxtempo': 'Gain x Time',
    'cap2_melhores': 'Find the bests',
    'tabela_imagem': 'Image',
    'tabela_nome': 'Name',
    'tabela_tempo': 'Time',
    'tabela_nivel_min': 'Min. time',
    'tabela_1_hora': 'in 1 hour',
    'cap3_titulo': '3. That is it.',
    'cap3_texto': '''
        I am Lucas Belmonte, data scientist, photographer, juggler.\n
        Thank you for came here.\n
        If you wish to understand better how i collected and processed the data:\n
        [The link will be here, when it be ready.]()\n
        If you wish the code from this app:\n
        [Get in this repository](https://github.com/lucasHashi/farm-together-utility-maximization-app)
    ''',
    'cap3_links': '''
        [Resume](http://www.lucasbelmonte.com.br/)\n
        [Linkedin](https://www.linkedin.com/in/lucas-d-belmonte/)\n
        [Github](https://github.com/lucasHashi)\n
        [Portfolio fotografico](https://www.behance.net/lucasbelmonte)\n
        [My dogs Instagram](https://www.instagram.com/mel_e_petit/)\n
    ''',
    'cap3.1_contato': '3.1 Contact',
    'cap3.2_biblio': '3.2 Main libs',
    'cap3.2_texto': '''
        Pandas\n
        Altair, for graphs\n
        Streamlit, for web-app
    ''',
    'link_post': 'The link will be here, when it be ready.'
}

def main():
    dict_atual = dict_pt
    idioma_selecionado = st.selectbox(dict_atual['idioma'],['English', 'Portugues'])
    dict_atual = dict_pt if(idioma_selecionado == 'Portugues') else dict_en
    st.write(dict_atual['idioma_sub'])
    st.title(dict_atual['titulo'])

    st.write('## ' + dict_atual['cap1_titulo'])

    st.write(dict_atual['cap1_texto'])
    #st.write("[I'm an inline-style link with title](https://www.google.com 'Google's Homepage')")
    st.write("["+dict_atual['link_post']+"]()")


    st.write('## ' + dict_atual['cap2_titulo'])
    filtro_ganho = st.selectbox(dict_atual['cap2_o_que_ganhar'], dict_atual['cap2_tipos_ganhos'])
    #st.write('### ' + dict_atual['cap2_titulo_dinheiro'])
    st.write('### '+ dict_atual['cap2_para_ganhar'] + ' ' + filtro_ganho)

    @st.cache
    def carregar_dados_finais():
        df_dados_final = pd.read_csv(URL_DADOS_FINAL_FARM_TOGETHER)
        return df_dados_final

    df_dados_final = carregar_dados_finais()
    filtro_colheita = st.selectbox(dict_atual['cap2_tipo_colheita'],[dict_atual['cap2_todos']] + list(df_dados_final['tipo_colheita'].unique()))
    
    df_dados_filtrados = ''
    if(filtro_ganho == 'Moedas' or filtro_ganho == 'Coins'):
        df_dados_filtrados = df_dados_final[df_dados_final['tipo_ganho'] == 'dinheiro_dinheiro']
    elif(filtro_ganho == 'XP'):
        df_dados_filtrados = df_dados_final.copy()
    elif(filtro_ganho == 'Diamantes' or filtro_ganho == 'Diamonds'):
        df_dados_filtrados = df_dados_final[(df_dados_final['tipo_ganho'] == 'diamante_diamante') | (df_dados_final['tipo_ganho'] == 'dinheiro_diamante')]

    if((not filtro_colheita == 'Todos') and (not filtro_colheita == 'All')):
        df_dados_filtrados = df_dados_filtrados[df_dados_final['tipo_colheita'] == filtro_colheita]

    filtro_nivel = st.slider(dict_atual['cap2_seu_nivel'], 1, 100, 80)
    df_dados_filtrados = df_dados_filtrados[df_dados_final['nivel_fazenda'] <= filtro_nivel]

    df_dados_filtrados.reset_index(drop=True, inplace=True)

    if(st.checkbox(dict_atual['cap2_mostrar_dados'])):
        st.write(df_dados_filtrados)
    
    st.subheader(filtro_colheita+ ' - '+ dict_atual['cap2_ganhoxtempo'])
    chart = alt.Chart(df_dados_filtrados).mark_circle().encode(x='ganho_base', y='tempo', size='ganho_por_min', tooltip=['nome', 'ganho_por_min', 'ganho_base', 'tempo'])
    st.altair_chart(chart, use_container_width=True)

    n_melhores = st.slider(dict_atual['cap2_melhores'], 1, 10, 5)
    df_melhores = df_dados_filtrados[['url_img','nome', 'ganho_por_min', 'nivel_fazenda']].sort_values('ganho_por_min', ascending=False)
    df_melhores = df_melhores[:n_melhores]
    df_melhores['em_uma_hora'] = round(df_melhores['ganho_por_min'] * 60, 2)
    df_melhores.reset_index(drop=True, inplace=True)

    str_tabela_melhores = gerar_tabela_melhores(df_melhores, filtro_ganho, dict_atual)
    st.write(str_tabela_melhores)

    st.write('## ' + dict_atual['cap3_titulo'])
    st.write(dict_atual['cap3_texto'])
    st.write('### '+dict_atual['cap3.1_contato'])
    st.write(dict_atual['cap3_links'])

    st.write('### '+dict_atual['cap3.2_biblio'])
    st.write(dict_atual['cap3.2_texto'])

def gerar_tabela_melhores(df_melhores, filtro_ganho, dict_atual):
    str_tabela = '{} | '.format(dict_atual['tabela_imagem'])
    str_tabela += '{} | '.format(dict_atual['tabela_nome'])
    str_tabela += filtro_ganho
    str_tabela += '/{} | '.format(dict_atual['tabela_tempo'])
    str_tabela += '{} | '.format(dict_atual['tabela_nivel_min'])
    str_tabela += filtro_ganho
    str_tabela += ' {} '.format(dict_atual['tabela_1_hora'])
    str_tabela += '\n --- | --- | --- | --- | --- \n'

    for _, linha in df_melhores.iterrows():
        url, nome, ganho_tempo, nivel, uma_hora = linha
        txt_url = '![alt text]({})'.format(url)
        
        txt_linha = '{} | {} | {} | {} | {} \n'.format(txt_url, nome, ganho_tempo, nivel, uma_hora)
        str_tabela += txt_linha

    return str_tabela





main()