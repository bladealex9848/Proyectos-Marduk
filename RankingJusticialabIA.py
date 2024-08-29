import pandas as pd

projects = [
    {
        "Ranking": 1,
        "Proyecto": "Sistema de Gestión de Expedientes Electrónicos Judiciales",
        "Descripción": "Sistema integral para la gestión digital de expedientes judiciales, incluyendo creación de índices electrónicos.",
        "Problema que soluciona": "Ineficiencia en el manejo de expedientes físicos, dificultad en el acceso a la información y creación manual de índices.",
        "Cómo lo soluciona": "Digitaliza y gestiona expedientes, facilita su acceso, búsqueda y seguimiento. Automatiza la creación de índices electrónicos.",
        "Análisis respecto a criterios del concurso": "Piedra angular de la modernización judicial. Impacta directamente en 'Justicia al día' y 'Justicia basada en datos'. Potencial para revolucionar la eficiencia y transparencia en todos los niveles del sistema judicial."
    },
    {
        "Ranking": 2,
        "Proyecto": "Gestión Integral de Vigilancia Judicial Administrativa",
        "Descripción": "Sistema automatizado para la gestión de solicitudes de vigilancia judicial administrativa.",
        "Problema que soluciona": "Ineficiencia en los procesos de vigilancia judicial administrativa, falta de trazabilidad y seguimiento de solicitudes.",
        "Cómo lo soluciona": "Implementa un sistema digital integrado para el registro, seguimiento y análisis de solicitudes de vigilancia administrativa.",
        "Análisis respecto a criterios del concurso": "Crucial para 'Justicia al día' y 'Justicia basada en datos'. Mejora significativa en la eficiencia administrativa y supervisión judicial, fortaleciendo la integridad del sistema."
    },
    {
        "Ranking": 3,
        "Proyecto": "OmniChat: Asistente Virtual Judicial Todo en Uno",
        "Descripción": "Asistente virtual versátil que integra chatbot básico, chatbot consciente del contexto, chat con documentos, bases de datos SQL y sitios web.",
        "Problema que soluciona": "Dificultad en el acceso rápido y eficiente a información judicial diversa y compleja.",
        "Cómo lo soluciona": "Proporciona una interfaz unificada para consultar diferentes fuentes de información judicial de manera conversacional.",
        "Análisis respecto a criterios del concurso": "Transformador para 'Justicia cercana'. Democratiza el acceso a la información judicial, mejorando la experiencia tanto de profesionales como de ciudadanos."
    },
    {
        "Ranking": 4,
        "Proyecto": "VigilantIA",
        "Descripción": "Asistente especializado en Vigilancia Judicial Administrativa basado en IA.",
        "Problema que soluciona": "Complejidad en la interpretación y aplicación de normativas de vigilancia judicial.",
        "Cómo lo soluciona": "Ofrece asistencia especializada en temas de vigilancia judicial, interpretando y aplicando normativas de manera precisa.",
        "Análisis respecto a criterios del concurso": "Esencial para 'Justicia al día' y 'Justicia basada en datos'. Mejora la eficiencia y precisión en procesos de vigilancia, fortaleciendo la integridad judicial."
    },
    {
        "Ranking": 5,
        "Proyecto": "WebNavigatorAI",
        "Descripción": "Asistente virtual especializado en búsquedas de Internet para información judicial.",
        "Problema que soluciona": "Dificultad para encontrar y filtrar información legal relevante y actualizada en la web.",
        "Cómo lo soluciona": "Realiza búsquedas web inteligentes y presenta información relevante de manera rápida y precisa.",
        "Análisis respecto a criterios del concurso": "Potencia 'Justicia cercana' y 'Justicia basada en datos'. Facilita el acceso a información legal actualizada, mejorando la toma de decisiones judiciales."
    },
    {
        "Ranking": 6,
        "Proyecto": "MALLO (MultiAgent LLM Orchestrator)",
        "Descripción": "Sistema avanzado de orquestación de múltiples agentes de IA para consultas legales complejas.",
        "Problema que soluciona": "Dificultad en manejar consultas legales que requieren múltiples fuentes de conocimiento y análisis complejos.",
        "Cómo lo soluciona": "Coordina varios modelos de IA para proporcionar respuestas precisas y contextuales a consultas jurídicas complejas.",
        "Análisis respecto a criterios del concurso": "Innovación disruptiva para 'Justicia basada en datos'. Potencial para revolucionar la investigación legal y la toma de decisiones complejas en el ámbito judicial."
    },
    {
        "Ranking": 7,
        "Proyecto": "Asesor Legal Anticorrupción Colombiano",
        "Descripción": "Herramienta de IA especializada en legislación anticorrupción colombiana.",
        "Problema que soluciona": "Falta de acceso rápido a información especializada sobre anticorrupción en el contexto colombiano.",
        "Cómo lo soluciona": "Proporciona información precisa sobre legislación anticorrupción, ética judicial y normativas relacionadas.",
        "Análisis respecto a criterios del concurso": "Fundamental para 'Justicia cercana' y promoción de la integridad judicial. Impacto significativo en la transparencia y ética del sistema judicial colombiano."
    },
    {
        "Ranking": 8,
        "Proyecto": "JudiCalc",
        "Descripción": "Calculadora avanzada de días hábiles para la Rama Judicial de Colombia.",
        "Problema que soluciona": "Complejidad en el cálculo de plazos judiciales considerando días hábiles, festivos y especialidades judiciales.",
        "Cómo lo soluciona": "Automatiza el cálculo de días hábiles entre fechas, considerando especialidades judiciales y festivos nacionales.",
        "Análisis respecto a criterios del concurso": "Esencial para 'Justicia al día'. Mejora la precisión y eficiencia en la gestión de plazos judiciales, reduciendo errores y retrasos procesales."
    },
    {
        "Ranking": 9,
        "Proyecto": "Generador de Turnos Streamlit App",
        "Descripción": "Aplicación para generar programas de turnos basados en fechas seleccionadas.",
        "Problema que soluciona": "Dificultad en la gestión de turnos judiciales considerando festivos y fines de semana.",
        "Cómo lo soluciona": "Automatiza la generación de turnos considerando diversos factores temporales y laborales.",
        "Análisis respecto a criterios del concurso": "Contribuye a 'Justicia al día'. Optimiza la distribución de la carga laboral, mejorando la eficiencia y el bienestar de los funcionarios judiciales."
    },
    {
        "Ranking": 10,
        "Proyecto": "PDFMaster",
        "Descripción": "Herramienta avanzada para gestión de documentos PDF en el ámbito judicial.",
        "Problema que soluciona": "Dificultad en el manejo, análisis y extracción de información de documentos legales en formato PDF.",
        "Cómo lo soluciona": "Ofrece funciones de conversión, resumen, análisis y extracción de información de documentos PDF.",
        "Análisis respecto a criterios del concurso": "Impacta en 'Justicia al día' y 'Justicia basada en datos'. Mejora significativamente la eficiencia en el manejo de documentación legal."
    },
    {
        "Ranking": 11,
        "Proyecto": "AnalizadorEstadisticoJudicial",
        "Descripción": "Sistema para análisis automático de datos estadísticos judiciales.",
        "Problema que soluciona": "Ineficiencia y potenciales errores en el análisis manual de datos estadísticos judiciales.",
        "Cómo lo soluciona": "Automatiza el procesamiento y análisis de datos estadísticos, generando informes y visualizaciones útiles.",
        "Análisis respecto a criterios del concurso": "Crucial para 'Justicia basada en datos'. Facilita la toma de decisiones basada en evidencia y la mejora continua del sistema judicial."
    },
    {
        "Ranking": 12,
        "Proyecto": "ProcesAI CGP",
        "Descripción": "Asistente de IA especializado en el Código General del Proceso de Colombia.",
        "Problema que soluciona": "Dificultad en el acceso y comprensión de información procesal específica de Colombia.",
        "Cómo lo soluciona": "Proporciona respuestas precisas sobre procedimientos legales y teoría procesal colombiana.",
        "Análisis respecto a criterios del concurso": "Fortalece 'Justicia cercana' y 'Justicia al día'. Mejora el acceso y comprensión de información procesal crítica para profesionales y ciudadanos."
    },
    {
        "Ranking": 13,
        "Proyecto": "Constitutor Colombiano 1991",
        "Descripción": "Aplicación interactiva sobre la Constitución Política de Colombia de 1991.",
        "Problema que soluciona": "Dificultad en el acceso y comprensión de la información constitucional colombiana.",
        "Cómo lo soluciona": "Ofrece consultas interactivas y explicaciones claras sobre la Constitución utilizando IA.",
        "Análisis respecto a criterios del concurso": "Fundamental para 'Justicia cercana'. Promueve la educación constitucional y facilita la aplicación de principios constitucionales en la justicia."
    },
    {
        "Ranking": 14,
        "Proyecto": "Suite Integral de Procesamiento Audiovisual Judicial",
        "Descripción": "Sistema avanzado para transcripción, análisis emocional y procesamiento de contenido audiovisual judicial.",
        "Problema que soluciona": "Dificultades en la transcripción, interpretación y gestión de contenido audiovisual en procesos judiciales.",
        "Cómo lo soluciona": "Automatiza la transcripción, analiza emociones, divide y mejora archivos de audio/video, y facilita la conversión entre formatos.",
        "Análisis respecto a criterios del concurso": "Innovador para 'Justicia al día' y 'Justicia basada en datos'. Mejora significativamente el manejo de evidencias audiovisuales y la eficiencia en procesos judiciales virtuales y presenciales."
    },
    {
        "Ranking": 15,
        "Proyecto": "UI2HTML",
        "Descripción": "Herramienta para convertir diseños de interfaz en código HTML funcional para sistemas judiciales.",
        "Problema que soluciona": "Complejidad y tiempo requerido en la creación de interfaces web para sistemas judiciales.",
        "Cómo lo soluciona": "Automatiza la conversión de diseños de interfaz en código HTML, acelerando el desarrollo de herramientas digitales judiciales.",
        "Análisis respecto a criterios del concurso": "Contribuye a 'Justicia cercana' al facilitar el desarrollo de interfaces amigables. Acelera la digitalización de servicios judiciales."
    },
    {
        "Ranking": 16,
        "Proyecto": "Acortador de URLs de Enki",
        "Descripción": "Servicio especializado para acortar y gestionar enlaces web en el ámbito judicial.",
        "Problema que soluciona": "Dificultad en compartir y gestionar URLs largas en comunicaciones judiciales.",
        "Cómo lo soluciona": "Genera URLs cortas y fáciles de compartir, con seguimiento y análisis de uso.",
        "Análisis respecto a criterios del concurso": "Mejora 'Justicia cercana' facilitando la comunicación. Potencial para optimizar la difusión de información judicial y legal."
    },
    {
        "Ranking": 17,
        "Proyecto": "Voice-Assistant-GPT Judicial",
        "Descripción": "Asistente de voz inteligente especializado en temas judiciales.",
        "Problema que soluciona": "Barreras de accesibilidad a información judicial para personas con limitaciones visuales o de movilidad.",
        "Cómo lo soluciona": "Proporciona una interfaz de voz para consultas y tareas relacionadas con el sistema judicial.",
        "Análisis respecto a criterios del concurso": "Fundamental para 'Justicia cercana'. Mejora la accesibilidad e inclusión en el sistema judicial, especialmente para personas con discapacidades."
    },
    {
        "Ranking": 18,
        "Proyecto": "Creador de Libro de Cuentos Judicial",
        "Descripción": "Sistema para crear contenido educativo infantil sobre temas judiciales y legales.",
        "Problema que soluciona": "Falta de materiales educativos accesibles sobre el sistema judicial para niños y jóvenes.",
        "Cómo lo soluciona": "Automatiza la creación de cuentos y materiales educativos que explican conceptos judiciales de manera sencilla y atractiva.",
        "Análisis respecto a criterios del concurso": "Innovador para 'Justicia cercana'. Promueve la educación legal desde temprana edad, fomentando una cultura de legalidad y comprensión del sistema judicial."
    },
    {
        "Ranking": 19,
        "Proyecto": "Monitoreo de Presión Arterial para Funcionarios Judiciales",
        "Descripción": "Aplicación para el seguimiento de la salud cardiovascular de los funcionarios judiciales.",
        "Problema que soluciona": "Falta de atención a la salud y bienestar de los funcionarios judiciales bajo estrés laboral.",
        "Cómo lo soluciona": "Permite el registro y seguimiento de la presión arterial, ofreciendo recomendaciones para mantener un estilo de vida saludable.",
        "Análisis respecto a criterios del concurso": "Contribuye indirectamente a 'Justicia al día'. Mejora el bienestar de los funcionarios judiciales, lo que puede traducirse en un mejor servicio y eficiencia en la administración de justicia."
    }
]

# Crear un DataFrame de pandas
df = pd.DataFrame(projects)

# Convertir el DataFrame a una tabla Markdown
markdown_table = df.to_markdown(index=False)

# Imprimir la tabla Markdown
print(markdown_table)

# Guardar la tabla Markdown en un archivo
with open("RankingProyectos.md", "w") as file:
    file.write(markdown_table)


