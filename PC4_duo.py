# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_duo.py
# ojo: detengo la ejecución con Ctrl + C en el terminal
    # y lo reestablezco con "python -m streamlit run PC4_duo.py" en el terminal 

# Importamos las librerías
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
with st.sidebar:
    opciones = option_menu("Secciones: ",['Presentación', 'Experiencia', 'Gráficos'] , 
        # personalizar los íconos
        # icons (secciones)
        # menu_icons (icono del menú)
        # link de repositorio de iconos: https://icons.getbootstrap.com 
        icons=['people-fill','1-circle', '2-circle'], menu_icon="people-fill", default_index=0)


# contenido de la PRIMERA SECCIÓN ()
if opciones == 'Presentación':
    #encabezado 
    # <h1>: de encabezado
    # 'text align': para centrar
    # unsafe_allow_html=True: permite editar
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Sobre nosotras</h1>", unsafe_allow_html=True)

    # Alumno a: Ariana
    # (2): indica el número de columnas, no posición
    col1, col2 = st.columns(2)
    
    # Caption: Foto y etiqueta debajo de la foto
    col1.image("Foto_Ariana.jpg", caption='Ariana Jáuregui', width=300)

    # 3 comillas para los textos
    texto = """
    Soy Ariana Jáuregui Rojas, estudiante de Publicidad en la PUCP y editora de este blog. 
    Tengo 22 años y voy a mitad de la carrera. Me considero una persona con diferentes intereses y curiosidad por aprender. 
    Por ello, el curso Pensamiento Computacional me interesa, porque el lenguaje de programación es 
    algo que no había aprendido antes. Además de lo académico, uno de mis hobbies es el karate. 
    Deporte que empecé a inicios de año y hoy ya me encuentro como cinturón celeste raya amarilla, un nivel novel aún. 
    Del karate rescato la disciplina y persistencia que este deporte me ayudó a desarrollar. 
    """
    # markdown para personalizar el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;color: black'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b: Adriana
    col1, col2 = st.columns(2)
    
    texto_2 = """
    Soy Adriana Orellana Marquina, estudiante de Publicidad en la PUCP y editora de este blog. Tengo 20 años y vivo en la ciudad de Lima en Perú. 
    Voy en quinto ciclo de la carrera y durante este tiempo he aprendido que la publicidad se encuentra en todos lados y repercute en la 
    toma de decisiones de las personas. Respecto a mi carrera, en un futuro me gustaría trabajar con grandes marcas en el extranjero. 
    Como propósito personal, me gustaría tener un santuario y un refugio de animales. En mis tiempos libres me gusta ver series, 
    escuchar música y manejar autos.
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("Foto_Adriana.jpeg", caption='Adriana Orellana', width=300)

 # SEGUNDA SECCIÓN (Experiencia)   
elif  opciones == 'Experiencia':
    # Nombre a la sección
    # lista de emogis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nuestra experiencia en la programación 💻</h1>", unsafe_allow_html=True)

    # Subtítulo para Ariana
    st.subheader("Ariana")
    
    # Alumno a: Ariana
    texto_3 = """
    El curso “Pensamiento Computacional para las Comunicaciones” es mi primera experiencia aprendiendo a programar.
    Al principio me sentí un poco intimidada por el lenguaje de python, pero con la orientación de la docente fue fácil adaptarse progresivamente.
    La programación me ha enseñado el funcionamiento de una página web detrás de la experiencia de un usuario.
    También, me ha ayudado a encontrar diferentes soluciones ante una misma situación.
    En el futuro me gustaría aprender más sobre programación orientada a Marketing Analytics, justamente orientada al rubro publicitario.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)

    texto_4 = """
    A continuación presento videos explicativos de mi autoría acerca del contenido del curso Pensamiento Computacional para las Comunicaciones:
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)

    
    # Botones de Videos Ariana
    # Video 1 Ariana
        # Formato Google Drive (botón)
        # Para centrar un botón 
        # creamos 3 columnas (col1, col2, col3)
        # ([1, 2, 1]): asigna tamaño a las columnas
    col1, col2, col3 = st.columns([1, 2, 1])

    # contenido del botón 1 Ariana
    with col2:  
        st.link_button("🎥 Operadores booleanos",
                       # link como string
                       "https://drive.google.com/file/d/13ww94f97Xn78QM7iEC6ypONKSaBR2Sop/view?usp=drive_link",
                       use_container_width=True
            )
    # Video 2 Ariana
        # Para centrar el botón
    col1, col2, col3 = st.columns([1, 2, 1])

    # contenido del botón 2 Ariana
    with col2:  
        st.link_button("🎥 Condicionales If-Elif-Else",
                       # link como string
                       "https://drive.google.com/file/d/1xLJIExWq8KcVO6qqdSgiyAQ95Zo0bXHy/view?usp=drive_link",
                       use_container_width=True
            )
   
 # Subtítulo para Adriana
    st.subheader("Adriana")
    
    # Alumno a: Adriana
    texto_5 = """
    Al inicio, el curso “Pensamiento Computacional para las Comunicaciones” fue complicado de entender, pues no tenía experiencia 
    previa usando lenguajes de programación y pensaba que iba a ser bastante complicado e incluso imposible de aprender. 
    No obstante, gracias al asesoramiento de la profesora y los recursos brindados comprendí que era cuestión de práctica. 
    La programación me ha enseñado a resolver los problemas de diversas maneras, pero respetando las reglas establecidas. 
    Asimismo, me enseñó a ser cuidadosa con los códigos y palabras que se usan. De programar me gusta poder crear páginas o blogs 
    desde cero y ver el resultado final. En un futuro me gustaría seguir aprendiendo otros lenguajes de programación para así poder 
    crear herramientas que me permitan tener un emprendimiento propio o aplicarlos al rubro de la publicidad en el que me encuentre.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)

    texto_6 = """
    A continuación presento videos explicativos de mi autoría acerca del contenido del curso Pensamiento Computacional para las Comunicaciones:
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)

    
    # Botones de Videos Adriana
    # Video 1 Adriana
        # Formato Google Drive (botón)
        # Para centrar un botón 
        # creamos 3 columnas (col1, col2, col3)
        # ([1, 2, 1]): asigna tamaño a las columnas
    col1, col2, col3 = st.columns([1, 2, 1])

    # contenido del botón 1 Adriana
    with col2:  
        st.link_button("🎥 Operadores Booleanos",
                       # link como string
                       "https://drive.google.com/file/d/1x1KZ67Sw1NuriexHnWGQS28DgSEn2iUq/view?usp=sharing&t=422.4",
                       use_container_width=True
            )
    # Video 2 Adriana
        # Para centrar el botón
    col1, col2, col3 = st.columns([1, 2, 1])

    # contenido del botón 2 Adriana
    with col2:  
        st.link_button("🎥 Condicionales If-Elif-Else",
                       # link como string
                       "https://drive.google.com/file/d/1E3seXP3L0fppzUmWTKbrJwynP0vRxFX5/view?usp=sharing",
                       use_container_width=True
            )
   


# TERCERA SECCIÓN (gráficos)           
else:
    # encabezado principal
    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nuestra producción de gráfico</h1>", unsafe_allow_html=True)
    
    # 10 gráficos en total (1 nube de palabras + 3 gráficos + 1 mapa) por integrante
    graficos = ['WordCloud de "Paco Yunque"', 'WordCloud de: Reunion en el Restaurante Nostalgia', 'Hisogramas del Real Madrid', 'Histogramas del Levante U.D.', 'Grafico de pastel del Real Madrid', 'Grafico de pastel del Levante U.D.', 'Grafico de barras 1 de Tarjetas amarillas', 'Grafico de barras 2 de Tarjetas amarillas', 'Mapa 1 de Pilotos', 'Mapa 2 de Pilotos'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Nubes de palabras
    if grafico_seleccionado == 'WordCloud de "Paco Yunque"':
        # sibtitulo de gráfico
        st.subheader("Nube de Palabras del primer capitulo del libro Paco Yunque.")
        texto_5 = """
        Interpretación del Gráfico 1
        """
        # formato
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        # para centrar
        col1, col2, col3 = st.columns([1, 9, 1])
        with col2:
                st.image("WordCloud_PacoYunque.png", width=800)
    
    # continuar con más elif (8 elif)
    elif grafico_seleccionado == 'WordCloud de: Reunion en el Restaurante Nostalgia':
        st.subheader("Nube de Palabras del primer capitulo del libro Reunión en el Restaurante Nostalgia")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Wordcloud_Ariana.png", width=800)
    # Histogramas
    elif grafico_seleccionado == 'Hisogramas del Real Madrid':
        st.subheader("📊 Hisograma: goles del Real Madrid anotados como local")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Histograma1_Adriana.png", width=800)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Histograma2_Adriana.png", width=800)
        
    #elif grafico_seleccionado == 'Hisograma2_Real_Madrid':
        #st.subheader("📊 Hisograma: goles del Real Madrid recibidos como visitante")
        #texto_6 = """
        #Interpretación del Gráfico 2
        #"""
        #st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        #col1, col2, col3 = st.columns([1, 7, 1])
        #with col2:
            #st.image("Histograma2_Adriana.png", width=800)

    elif grafico_seleccionado == 'Histogramas del Levante U.D.':
        st.subheader("📊 Histogramas: goles del Levante U.D. anotados como visitante y recibidos como local")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma_Ariana.png", width=800)
    
    # Gráfico de pastel
    elif grafico_seleccionado == 'Grafico de pastel del Real Madrid':
        st.subheader("📊 Gráfico de pastel: resultados del Real Madrid jugando como local en la liga española 2025-2026.")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráfico_pastel_Adriana.png", width=800)

    elif grafico_seleccionado == 'Grafico de pastel del Levante U.D.':
        st.subheader("📊 Gráfico de pastel: resultados del Levante U.D. jugando como local en la liga española 2025-2026.")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráfico_pastel_Ariana.png", width=800)
    # Gráfico de barras
    elif grafico_seleccionado == 'Grafico de barras 1 de Tarjetas amarillas':
        st.subheader("📊 Grafico de barras de las Tarjetas amarillas recibidas por los equipos como visitante durante la Liga española 2025-2026.")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráfico_barras_Adriana.png", width=800)

    elif grafico_seleccionado == 'Grafico de barras 2 de Tarjetas amarillas':
        st.subheader("📊 Grafico de barras de las Tarjetas amarillas recibidas por los equipos como visitante durante la Liga española 2025-2026.")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráfico_barras_Ariana.png", width=800)
    
    # Mapas residencia de pilotos
    elif grafico_seleccionado == 'Mapa 1 de Pilotos':
        st.subheader("🗺️ Mapa del país de origen y datos de los pilotos Lewis Hamilton y Max Verstappen.")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        with open("mapa_pilotos_Adriana.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
             
             components.html(html_content,height=600)
    
    else:
        st.subheader("🗺️ Mapa del país de origen y datos de los pilotos _ y _.")
        texto_7 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
        #  "r", encoding="utf-8": no editar    
        with open("mapa_Ariana.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
     
        components.html(html_content,height=600)
    



