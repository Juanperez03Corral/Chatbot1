# chatbot_streamlit.py

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Chin Chin – Chatbot Particulares", page_icon="🍷")

# Estado de la bodega del usuario
if 'bodega' not in st.session_state:
    st.session_state.bodega = ["Viña Sol", "Marqués de Riscal"]

st.title("🍷 Chin Chin – Tu Asistente de Vino")
st.subheader("¡Hola! ¿En qué puedo ayudarte hoy?")

# Menú principal
opcion = st.selectbox("Selecciona una opción:", [
    "Selecciona...",
    "1. Recomendación de vinos",
    "2. Ver vinos por supermercado y precio",
    "3. Gestionar mi bodega",
    "4. Información sobre el pack mensual",
    "5. Actividades y visitas a bodegas"
])

# Funciones
def recomendar_vino():
    tipo = st.selectbox("¿Qué vas a comer hoy?", ["Carne", "Pescado", "Pasta", "Queso", "Otro"])
    if tipo == "Carne":
        st.success("🍷 Te recomendamos un vino tinto con cuerpo como un Rioja o Ribera del Duero.")
    elif tipo == "Pescado":
        st.success("🥂 Un vino blanco como un Albariño o Verdejo sería perfecto.")
    elif tipo == "Pasta":
        st.success("🍝 Para pastas con salsa roja, prueba un Chianti o Tempranillo.")
    elif tipo == "Queso":
        st.success("🧀 Un vino dulce o un tinto maduro acompaña muy bien al queso.")
    else:
        st.warning("🤔 Aún no tenemos recomendaciones para ese tipo de comida.")

def vinos_por_super():
    supermercado = st.selectbox("Selecciona un supermercado:", ["Mercadona", "Carrefour", "Lidl", "Otro"])
    if supermercado == "Mercadona":
        st.info("🛒 Castillo de Liria (3€), El Coto (6€).")
    elif supermercado == "Carrefour":
        st.info("🛒 Marqués de Cáceres (6€), Viña Albali (5€).")
    elif supermercado == "Lidl":
        st.info("🛒 Cepa Lebrel (3,50€), Aromo (4,20€).")
    else:
        st.warning("⚠️ No tenemos información de ese supermercado aún.")

def gestionar_bodega():
    st.write("📦 Tu bodega actual:")
    for vino in st.session_state.bodega:
        st.write(f"- {vino}")
    
    nuevo_vino = st.text_input("Añade un nuevo vino a tu bodega:")
    if st.button("Agregar vino"):
        if nuevo_vino:
            st.session_state.bodega.append(nuevo_vino)
            st.success(f"✅ '{nuevo_vino}' añadido a tu bodega.")
        else:
            st.warning("Por favor, escribe el nombre del vino.")

def info_pack():
    st.markdown("""
    ### 📦 Pack mensual Chin Chin:
    - 3 vinos sorpresa cada mes.
    - Recomendados según tus gustos.
    - **Precio:** 24,99€/mes.
    ¿Te gustaría recibirlo? ¡Contáctanos a través de la app para suscribirte!
    """)

def actividades():
    st.markdown("""
    ### 🍇 Actividades disponibles:
    - Visita a bodega en La Rioja con cata incluida.
    - Taller de maridaje en Madrid.
    - Evento de vino y música en Barcelona.
    
    **Reserva desde nuestra web o app.**
    """)

# Lógica de selección
if opcion.startswith("1"):
    recomendar_vino()
elif opcion.startswith("2"):
    vinos_por_super()
elif opcion.startswith("3"):
    gestionar_bodega()
elif opcion.startswith("4"):
    info_pack()
elif opcion.startswith("5"):
    actividades()


