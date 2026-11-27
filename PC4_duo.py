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
                           
        icons=['people-fill','trophy-fill', 'bar-chart-line-fill'], menu_icon="star-fill", default_index=1)


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
    
    col2.image("Foto2_Adriana.jpeg", caption='Adriana Orellana', width=300)

 # SEGUNDA SECCIÓN (Experiencia)   
elif  opciones == 'Experiencia':
    # Nombre a la sección
    # lista de emogis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nuestra experiencia en la programación 💻</h1>", unsafe_allow_html=True)

    # Subtítulo para Ariana
    st.subheader("Ariana 🩷🐭")
    
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
    
    
    # Videos Ariana
        # Formato Google Drive (botón)
        # Para centrar el botón y la imagen
        # creamos 4 columnas (col1, col2, col3, col4)
        # ([1, 6, 6, 1]): asigna tamaño a las columnas
    col1, col2, col3, col4 = st.columns([1, 6, 6, 1])

    # añadimos una imagen a la columna 2 porque pensamos que se veía simple
    col2.image("rata_ariana.jpg", width=200)
    
    # contenido del botón 1 Ariana en la columna 3
    with col3:  
        st.link_button("🎥 Operadores Booleanos",
                       # link como string
                       "https://drive.google.com/file/d/13ww94f97Xn78QM7iEC6ypONKSaBR2Sop/view?usp=drive_link",
                       use_container_width=True
            )
    # contenido del botón 2 Ariana en la columna 3
    with col3:  
        st.link_button("🎥 Condicionales If-Elif-Else",
                       # link como string
                       "https://drive.google.com/file/d/1xLJIExWq8KcVO6qqdSgiyAQ95Zo0bXHy/view?usp=drive_link",
                       use_container_width=True
            )
   
 # Subtítulo para Adriana
    st.subheader("Adriana 💜🐱")
    
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
        # creamos 4 columnas (col1, col2, col3, col4)
        # ([1, 6, 6, 1]): asigna tamaño a las columnas
    col1, col2, col3, col4 = st.columns([1, 6, 6, 1])

    # añadimos una imagen porque pensamos que se veía simple
    # Caption: Foto y etiqueta debajo de la foto
    col2.image("gato_adriana.jpg", width=200)
    
    # contenido del botón 1 Adriana en la columna 3
    with col3:  
        st.link_button("🎥 Operadores Booleanos",
                       # link como string
                       "https://drive.google.com/file/d/1x1KZ67Sw1NuriexHnWGQS28DgSEn2iUq/view?usp=sharing&t=422.4",
                       use_container_width=True
            )
    
    # contenido del botón 2 Adriana en la columna 3
    with col3:  
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
    graficos = ['WordCloud de "Paco Yunque"', 'WordCloud de "Reunion en el Restaurante Nostalgia"', 'Histogramas del Real Madrid', 
                'Histogramas del Levante U.D.', 'Grafico de pastel del Real Madrid', 'Grafico de pastel del Levante U.D.', 
                'Grafico de barras 1 de Tarjetas amarillas', 'Grafico de barras 2 de Tarjetas amarillas', 'Mapa 1 de Pilotos', 'Mapa 2 de Pilotos'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Nubes de palabras
    if grafico_seleccionado == 'WordCloud de "Paco Yunque"':
        # sibtitulo de gráfico
        st.subheader("📖 Nube de Palabras del primer capitulo del libro Paco Yunque.")
        texto_7 = """
        Para la creación de esta nube de palabras se eligió trabajar con minúsculas para evitar errores de ejecución. 
        Asimismo para que las palabras se vean simétricas. También se eliminaron algunos signos de puntuación, por ejemplo, 
        puntos, comas, guiones, comillas, etc. Para así limpiar y estandarizar la información, es decir, para que el programa 
        logre reconocer las palabras sin el uso de estos signos. Asimismo, para la elección de los stopwords, se priorizaron 
        eliminar los pronombres, preposiciones y artículos. Ya que no aportan información adicional. Todas estas decisiones fueron 
        importantes para que la nube de palabras sea correcta, ya que se muestran palabras que definen el cuento, de esta manera, 
        una persona que vea la nube podrá entender quiénes son los personajes principales y de qué trata la historia.
        """
        # formato
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
        # para centrar
        col1, col2, col3 = st.columns([1, 9, 1])
        with col2:
                st.image("WordCloud_PacoYunque.png", width=800)
    
    # continuar con más elif (8 elif)
    elif grafico_seleccionado == 'WordCloud de "Reunion en el Restaurante Nostalgia"':
        st.subheader("📖 Nube de Palabras del primer capitulo del libro Reunión en el Restaurante Nostalgia")
        texto_8 = """
        Para esta nube de palabras o Wordcloud se trabajó con minúsculas para facilitar la limpieza de palabras stopword, 
        a pesar de que las palabras con más frecuencias eran los nombres de los personajes (Pearl, Ezra, Cody, Jenny y Beck) 
        las cuales se entenderían mejor con sus iniciales en mayúscula. Respecto a los caracteres, se decidió eliminar 
        todos porque ninguno me pareció relevante para el relato. Entre los signos depurados estuvieron signos de exclamación, 
        interrogación, puntos y comas, pero sobre todo, comillas españolas y guiones de diálogo. Acerca de las stopwords, 
        se decidió omitir palabras conectores, prepociones, verbos baúl (hacer, tener, poner, haber) y todas las conjugaciones 
        del verbo decir. Al ser una novela con diálogos, las variaciones del verbo decir eran bastante comunes, por lo que se decidió 
        eliminar ya que no pertenecían a la historia. Así mismo, es pertinente mencionar que el pronombre "él" no fue considerado 
        como Stopword porque en el relato este pronombre es usado para evocar el recuerdo de un personaje, el cual se evita mencionar 
        su nombre; prueba de ello es que esta palabra es de las que más frecuencia tiene. Finalmente, en la parte estética, se seleccionó 
        como color de fondo al lila por ser el color que está en la portada del libro impreso. Así mismo, la paleta de colores es 
        "managua" porque sus tonos azules y naranjas cobran relación con los escenarios más memorables del libro, los cuales transcurren 
        de noche y tarde. Además, el fondo claro contrasta con los colores más vivos de las palabras.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Wordcloud_Ariana.png", width=800)
    # Histogramas
    elif grafico_seleccionado == 'Histogramas del Real Madrid':
        st.subheader("📊 Histograma: goles del Real Madrid anotados como local")
        texto_9 = """
        En resumen, los resultados demuestran que el Real Madrid tiene un gran equipo a nivel defensivo y ofensivo. 
        Esto se demuestra porque en el primer gráfico se observa una tendencia del equipo a marcar entre 2 y 3 goles 
        en sus 8 partidos como local. Mientras que, en el segundo gráfico el mayor patrón es que el equipo mantuvo su 
        portería a cero en ocho de los 19 partidos. Esto demuestra que el Real Madrid suele marcar varios goles cuando 
        juega como local y solamente recibe poco o casi nada de goles cuando juega como visitante.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Histograma1_Adriana.png", width=800)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Histograma2_Adriana.png", width=800)
        
    elif grafico_seleccionado == 'Histogramas del Levante U.D.':
        st.subheader("📊 Histogramas: goles del Levante U.D. anotados como visitante y recibidos como local")
        texto_10 = """
        Se eligió comparar los goles que Levante U.D. anotó como visitante y los que recibió como equipo local. 
        Respecto a sus anotaciones, Levante parece ser un equipo constante en la cantidad de goles.
        Tiende a anotar entre 0 y 1 goles como visitante; de los 19 partidos rara vez anotó más de 2 goles. 
        Respecto a los goles recibidos, los goles tienden a ocilar entre 0 y 2 recibidos, con un notable pico en la 
        barra de 2 goles. En conclusión, comparando ambos gráficos vemos que los equipos rivales tienen mejor 
        desempeño que Levante U.D. cuando se juega como visitante.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_10}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma_Ariana.png", width=800)
    
    # Gráfico de pastel
    elif grafico_seleccionado == 'Grafico de pastel del Real Madrid':
        st.subheader("🍰 Gráfico de pastel: resultados del Real Madrid jugando como local en la liga española 2025-2026.")
        texto_11 = """
        El gráfico circular demuestra que el Real Madrid tuvo una gran temporada en el 2025-2026. 
        Debido a que ganó casi la totalidad de sus partidos como local, con un sólido 84.2%, equivalente 
        a los 16 partidos de los 19 en total. Mientras que solo perdió un 10.5% y apenas empató con un 5.3%.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_11}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráfico_pastel_Adriana.png", width=800)

    elif grafico_seleccionado == 'Grafico de pastel del Levante U.D.':
        st.subheader("🍰 Gráfico de pastel: resultados del Levante U.D. jugando como local en la liga española 2025-2026.")
        texto_12 = """
        Los resultados totales de los 19 partidos que el Levante U.D. jugó como local reflejan el rendimiento 
        medio del equipo. Las categorías de "Ganados" y "Perdidos" tienen el mismo porcentaje (36.8%); mientras
        que "Empatados" se mantiene en 26.3%, un porcentaje cercano a la tercera parte. En conclusión, el grafico 
        del desempeño de Levante U.D. jugando como local nos muestra que jugar en su propio estadio no fue un factor 
        determinante para obtener ventaja en el torneo.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_12}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("GrafPas_Ariana.png", width=800)
    # Gráfico de barras
    elif grafico_seleccionado == 'Grafico de barras 1 de Tarjetas amarillas':
        st.subheader("🧮 Grafico de barras de las Tarjetas amarillas recibidas por los equipos como visitante durante la Liga española 2025-2026.")
        texto_13 = """
        A partir del gráfico de barras se demuestra que durante la temporada 2025-2026 de la 
        Liga Española todos los equipos recibieron en promedio de 2 a 3 tarjetas amarillas por 
        partido cuando jugaban como visitantes. Esto demuestra que es una liga competitiva, 
        pero no tan agresiva, ya que las tarjetas amarillas son inferiores a 5.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_13}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("Gráfico_barras_Adriana.png", width=800)

    elif grafico_seleccionado == 'Grafico de barras 2 de Tarjetas amarillas':
        st.subheader("🧮 Grafico de barras de las Tarjetas amarillas recibidas por los equipos como visitante durante la Liga española 2025-2026.")
        texto_14 = """
        Al revisar el gráfico se observa que todos los equipos han tenido tarjeta amarilla. 
        Predomina un promedio de 2 tarjetas amarillas por partido en 2/3 del total de equipos, 
        mientras la tercera parte restante presenta 3 tarjetas amarillas en promedio. 
        A partir ello podemos concluir que obtener al menos dos tarjetas amarillas son la regla 
        cuando se juega como visitante.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_14}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("GrafBar_Ariana.png", width=800)
    
    # Mapas residencia de pilotos
    elif grafico_seleccionado == 'Mapa 1 de Pilotos':
        st.subheader("🗺️ Mapa del país de origen y datos de los pilotos Lewis Hamilton y Max Verstappen.")
        texto_15 = """
        Elegí presentar la información en la ventana emergente (popup) de acuerdo a lo que solicitaban en la tarea. 
        El orden establecido era nombre del piloto, escudería, fotografía del piloto y el puntaje total. 
        Respecto al contenido del popup interactivo, elegí el color rojo para mostrar los marcadores, ya que es un 
        color distintivo y fácil de reconocer. Por otro lado, seleccioné el icono del carro, ya que la información 
        es sobre pilotos de carreras de autos. Por último, respecto a los elementos HTML, usé las etiquetas b 
        para mostrar el nombre del piloto en negrita y h1 para definir el nombre como título principal. 
        Asimismo, utilicé i para mostrar el puntaje total en cursiva, para que se diferencia del resto de información. 
        También, elegí el color azul para nombrar la escudería, para que así tenga diferentes características que los otros datos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_15}</div>", unsafe_allow_html=True)
    
        with open("mapa_pilotos_Adriana.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
             
        components.html(html_content,height=600)
    
    else:
        st.subheader("🗺️ Mapa del país de origen y datos de los pilotos Sergio Perez y Daniel Ricciardo.")
        texto_16 = """
        Para que en el mapa se pueda ver desde América hasta Oceanía, elejí un zoom inicial de "2" . 
        Respecto al pop-up, este tiene un tamaño de 400 para que el nombre de la escudería, el cual 
        en ambos casos es largo, no se corte en dos línes. Así mismo, este contiene 3 datos y una imagen 
        de cada piloto. Los datos están ordenados en Nombre del piloto (título en negrita), escudería (subtítulo), 
        y puntaje total de temporada 2016 (párrafo). Considero pertinente esta distribución porque visualmente 
        hay una jerarquía, me importa que destaquen el nombre y la escudería, mientras los puntos pueden pasar 
        a segundo plano ya que son de una temporada pasada. La imagen tiene forma redonda, con dimensiones de 170 
        de ancho y 150 de alto; ello para que se pueda ver mejor al piloto y su entorno.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_16}</div>", unsafe_allow_html=True)
        #  "r", encoding="utf-8": no editar    
        with open("mapa_Ariana.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
     
        components.html(html_content,height=600)
    






