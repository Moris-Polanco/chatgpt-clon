import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

# Inicializar el modelo GPT-3 de OpenAI y configurar la API
model_engine = "text-davinci-002"

# Crear una función para enviar una solicitud de compleción de texto al modelo GPT-3 y obtener una respuesta
def get_response(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Agregar una caja de texto y un botón en la aplicación Streamlit para que el usuario pueda ingresar un mensaje y enviarlo al modelo GPT-3
st.title("ChatGPT")

conversation_log = st.empty()

input_text = st.text_input("Ingresa tu mensaje:")

if input_text:
    # Añadir el mensaje del usuario al registro de la conversación
    conversation_log.markdown(f"Usuario: {input_text}")

    # Obtener la respuesta del modelo GPT-3
    response = get_response(input_text)

    # Añadir la respuesta del modelo al registro de la conversación
    conversation_log.markdown(f"Bot: {response}")
