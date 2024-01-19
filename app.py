#python -m venv env
#cd env/Scripts
#.\activate
#pip install streamlit
#pip install openai
#pip install python-dotenv

#al final poner pip freeze > requirements.txt para que cree el archivo con las dependencias
#levantar en streamlit con streamlit run ..\..\app.py

#deactivate para salir del modo virtual


import streamlit as st
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

# Configura tu clave de API de OpenAI
OpenAIkey = os.getenv("OPENAI_API_KEY") 

client = OpenAI(api_key=OpenAIkey)

def generar_idea_juguete(edad, sexo, materiales):
    prompt = f"Idea de juguete para un niño de {edad} años, {sexo}, utilizando {', '.join(materiales)}: "
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[  
            {"role": "user", "content": prompt}

        ]

        # engine="text-davinci-003",
        # prompt=prompt,
        # max_tokens=100,
        # temperature=0.7,
        # stop=None,
    )
    response = response.choices[0].message.content

    return response

# Interfaz de usuario con Streamlit
st.set_page_config(
    page_title="Making Toys",
    page_icon="🚀",
  
)


st.markdown(
    "<h1 style='text-align: center; color: #FF7F50;'>Generador de Ideas de Juguetes Para Niños</h1>",
    unsafe_allow_html=True
)


# Recopila la información del usuario
edad = st.slider("Edad del niño", 1, 12, 6)
sexo = st.radio("Sexo", ["Masculino", "Femenino"])
materiales_disponibles = st.text_area("Materiales disponibles (separados por comas)").split(",")

# Genera la idea del juguete
if st.button("Generar Idea"):
    if not materiales_disponibles:
        st.warning("Por favor, ingrese al menos un material disponible.")
    else:
        idea = generar_idea_juguete(edad, sexo.lower(), materiales_disponibles)
        st.success(f"Idea generada: {idea}")

