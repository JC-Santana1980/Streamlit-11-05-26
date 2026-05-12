import streamlit as st
import random 

#sidebar
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma pagina",
    ["Home","Grafico","Descrição"]
)

#Home
if pagina == "Home":

     st.title ("Pagina inicial")

     st.write ("Sistema usando o Streamlit")

    #input
     nome=st.text_input("Digite seu nome")

    #selectbox
     curso = st.selectbox(
        "Escolha um curso",
        ["Python","JS","Banco de Dados"]
    )

     #slider
     nota = st.slider(
         "Escolha sua nota",
         0,
         10,
         5
    )
     
     #checkbox
     mostrar = st.checkbox("Mostrar mensagem")

     if mostrar:
          st.success("Checkbox marcado")

     #botao
     if st.button("Enviar"):
         st.write(f"Nome : {nome}")     
         st.write(f"Curso : {curso}")
         st.write(f"Nota : {nota}")          
    
     st.subheader("Colunas")
     
     col1, col2 = st.columns(2)

     with col1:
         st.info("Informacoes coluna 1")
     with col2:
         st.warning("Informacoes coluna 2")    

elif pagina == "Grafico":
     st.title ("Pagina de grafico")
     valores = []
     for i in range(5):
        valores.append(random.randint(1,100))
     st.bar_chart(valores)   




#Home
if pagina == "Descrição":

    st.title ("Pagina Descrição")

    st.write ("Teste da linguagem python usando a biblioteca streamlit")

    