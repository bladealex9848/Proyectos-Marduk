import pandas as pd

# Crear la lista de proyectos con sus detalles
projects = [
    {
        "Ranking": 1,
        "Proyecto": "Sistema de Gestión de Expedientes Electrónicos Judiciales",
        "Descripción": "Sistema para la gestión digital de expedientes judiciales.",
        "Problema que soluciona": "Ineficiencia en el manejo de expedientes físicos y dificultad en el acceso a la información.",
        "Cómo lo soluciona": "Digitaliza y gestiona expedientes, facilitando su acceso, búsqueda y seguimiento.",
        "Análisis respecto a criterios del concurso": "Altamente alineado con los objetivos del concurso. Impacta positivamente en todas las especialidades judiciales y áreas administrativas. Mejora significativa en 'Justicia al día' y 'Justicia basada en datos'."
    },
    {
        "Ranking": 2,
        "Proyecto": "MALLO (MultiAgent LLM Orchestrator)",
        "Descripción": "Sistema avanzado de orquestación de múltiples agentes de Modelos de Lenguaje de Gran Escala.",
        "Problema que soluciona": "Complejidad en el manejo de consultas legales y administrativas que requieren múltiples fuentes de conocimiento.",
        "Cómo lo soluciona": "Coordina varios modelos de IA para proporcionar respuestas precisas y contextuales a consultas complejas.",
        "Análisis respecto a criterios del concurso": "Altamente innovador con potencial de impacto en todas las áreas judiciales y administrativas. Mejora la eficiencia en la respuesta a consultas complejas, alineándose con 'Justicia cercana' y 'Justicia basada en datos'."
    },
    {
        "Ranking": 3,
        "Proyecto": "Consejo Seccional de la Judicatura - Vigilancia Judicial Administrativa",
        "Descripción": "Sistema para automatizar y mejorar el proceso de vigilancia judicial administrativa.",
        "Problema que soluciona": "Ineficiencia en los procesos de vigilancia judicial administrativa.",
        "Cómo lo soluciona": "Automatiza el análisis de solicitudes, realiza control de legalidad y genera proyectos de decisión.",
        "Análisis respecto a criterios del concurso": "Excelente alineación con los objetivos del concurso. Impacta directamente en la eficiencia administrativa y en la supervisión judicial, beneficiando a todas las especialidades."
    },
    {
        "Ranking": 4,
        "Proyecto": "JudiCalc",
        "Descripción": "Calculadora de días hábiles para la Rama Judicial de Colombia.",
        "Problema que soluciona": "Complejidad en el cálculo de plazos judiciales considerando días hábiles y festivos.",
        "Cómo lo soluciona": "Automatiza el cálculo de días hábiles entre fechas, considerando especialidades judiciales y festivos.",
        "Análisis respecto a criterios del concurso": "Impacto significativo en todas las especialidades judiciales y áreas administrativas. Mejora la eficiencia en el cumplimiento de plazos y la programación de actividades."
    },
    {
        "Ranking": 5,
        "Proyecto": "PDFMaster",
        "Descripción": "Herramienta para gestionar documentos PDF, incluyendo conversión, resumen y análisis.",
        "Problema que soluciona": "Dificultad en el manejo y análisis de documentos legales y administrativos en formato PDF.",
        "Cómo lo soluciona": "Ofrece funciones de conversión, resumen y análisis de documentos PDF.",
        "Análisis respecto a criterios del concurso": "Relevante para todas las áreas judiciales y administrativas. Mejora la eficiencia en el manejo de documentos, alineándose con 'Justicia al día' y 'Justicia basada en datos'."
    },
    {
        "Ranking": 6,
        "Proyecto": "ColDisBot",
        "Descripción": "Asistente especializado en Derecho Disciplinario Colombiano.",
        "Problema que soluciona": "Complejidad en la comprensión y aplicación del derecho disciplinario.",
        "Cómo lo soluciona": "Ofrece información precisa sobre legislación disciplinaria, procedimientos y jurisprudencia.",
        "Análisis respecto a criterios del concurso": "Altamente relevante para los Consejos Seccionales y áreas de Talento Humano. Impacto significativo en la eficiencia de procesos disciplinarios."
    },
    {
        "Ranking": 7,
        "Proyecto": "ProcesAI CGP",
        "Descripción": "Aplicación para proporcionar información sobre el Código General del Proceso y la Teoría General del Proceso en Colombia.",
        "Problema que soluciona": "Dificultad en el acceso y comprensión de información procesal.",
        "Cómo lo soluciona": "Utiliza IA para responder consultas sobre procedimientos legales y teoría procesal.",
        "Análisis respecto a criterios del concurso": "Relevante para todas las especialidades judiciales, especialmente civil y familia. Mejora el acceso y comprensión de información procesal."
    },
    {
        "Ranking": 8,
        "Proyecto": "Generador de Turnos Streamlit App",
        "Descripción": "Aplicación para generar programas de turnos basados en fechas seleccionadas.",
        "Problema que soluciona": "Complejidad en la gestión de turnos judiciales y administrativos considerando festivos y fines de semana.",
        "Cómo lo soluciona": "Automatiza la generación de turnos considerando diversos factores temporales.",
        "Análisis respecto a criterios del concurso": "Impacto significativo en la gestión administrativa y organización de despachos judiciales. Mejora la eficiencia en la asignación de recursos humanos."
    },
    {
        "Ranking": 9,
        "Proyecto": "Asesor Legal en Salud Colombiano",
        "Descripción": "Herramienta de IA que proporciona información sobre el marco legal y ético del sector salud en Colombia.",
        "Problema que soluciona": "Dificultad para acceder a información legal especializada en salud.",
        "Cómo lo soluciona": "Utiliza IA para responder consultas sobre responsabilidad médica, normas del sector salud, y cuestiones éticas.",
        "Análisis respecto a criterios del concurso": "Relevante para especialidades como familia y laboral, así como para áreas de Bienestar. Mejora el acceso a información legal especializada en salud."
    },
    {
        "Ranking": 10,
        "Proyecto": "Constitutor Colombiano 1991",
        "Descripción": "Aplicación para proporcionar información sobre la Constitución Política de Colombia de 1991.",
        "Problema que soluciona": "Dificultad en el acceso y comprensión de la información constitucional.",
        "Cómo lo soluciona": "Ofrece consultas interactivas sobre la Constitución utilizando IA.",
        "Análisis respecto a criterios del concurso": "Relevante para todas las especialidades judiciales y áreas administrativas. Mejora la comprensión y aplicación de principios constitucionales en la administración de justicia."
    },
    {
        "Ranking": 11,
        "Proyecto": "Asistente Virtual (multiexperto)",
        "Descripción": "Asistente de IA capaz de ayudar en diversos temas y tareas en español.",
        "Problema que soluciona": "Necesidad de asistencia en múltiples áreas del conocimiento legal y administrativo.",
        "Cómo lo soluciona": "Proporciona respuestas y asistencia en una amplia gama de temas legales y no legales.",
        "Análisis respecto a criterios del concurso": "Potencial impacto en todas las áreas, pero requiere adaptación para especializarse más en temas judiciales y administrativos específicos."
    },
    {
        "Ranking": 12,
        "Proyecto": "Real-Time Emotion Detector",
        "Descripción": "Detector de emociones en tiempo real utilizando la cámara web.",
        "Problema que soluciona": "Dificultad en la interpretación de emociones en interacciones judiciales y administrativas.",
        "Cómo lo soluciona": "Analiza y clasifica emociones en tiempo real a través de video.",
        "Análisis respecto a criterios del concurso": "Potencial uso en audiencias virtuales y procesos de mediación. Requiere adaptación para cumplir con normativas éticas y de privacidad en el contexto judicial."
    },
    {
        "Ranking": 13,
        "Proyecto": "TranscriptorAV",
        "Descripción": "Aplicación para transcribir audio y video a texto.",
        "Problema que soluciona": "Dificultad en la transcripción manual de audiencias y declaraciones.",
        "Cómo lo soluciona": "Utiliza IA para transcribir automáticamente contenido audiovisual.",
        "Análisis respecto a criterios del concurso": "Útil para todas las especialidades judiciales. Mejora la eficiencia en la documentación de procesos orales, alineándose con 'Justicia al día'."
    },
    {
        "Ranking": 14,
        "Proyecto": "UI2HTML",
        "Descripción": "Convierte interfaces de usuario en código HTML.",
        "Problema que soluciona": "Complejidad en la creación de interfaces web para sistemas judiciales.",
        "Cómo lo soluciona": "Automatiza la conversión de diseños de interfaz en código HTML funcional.",
        "Análisis respecto a criterios del concurso": "Potencial para mejorar el desarrollo de herramientas digitales para la administración de justicia. Requiere adaptación para necesidades específicas del sistema judicial."
    },
    {
        "Ranking": 15,
        "Proyecto": "ImageBackgroundRemover",
        "Descripción": "Herramienta para eliminar el fondo de imágenes automáticamente.",
        "Problema que soluciona": "Necesidad de procesar imágenes para su uso en documentos judiciales y administrativos.",
        "Cómo lo soluciona": "Automatiza la eliminación de fondos en imágenes de manera sencilla.",
        "Análisis respecto a criterios del concurso": "Utilidad limitada pero potencial para mejorar la presentación de documentos y evidencias visuales en procesos judiciales."
    },
    {
        "Ranking": 16,
        "Proyecto": "Acortador de URLs de Enki",
        "Descripción": "Servicio para acortar y gestionar enlaces web.",
        "Problema que soluciona": "Dificultad en compartir y gestionar URLs largas en comunicaciones judiciales.",
        "Cómo lo soluciona": "Convierte URLs largas en versiones cortas y fáciles de compartir.",
        "Análisis respecto a criterios del concurso": "Utilidad para mejorar la comunicación interna y externa en el sistema judicial. Impacto menor pero potencialmente útil para 'Justicia cercana'."
    },
    {
        "Ranking": 17,
        "Proyecto": "Creador de Libro de Cuentos",
        "Descripción": "Sistema para crear libros de cuentos infantiles utilizando IA.",
        "Problema que soluciona": "No directamente relacionado con problemas judiciales o administrativos.",
        "Cómo lo soluciona": "Automatiza la creación de contenido literario infantil.",
        "Análisis respecto a criterios del concurso": "Baja relevancia directa para el sistema judicial. Potencial uso en programas de bienestar o educación legal para niños, pero requeriría adaptación significativa."
    },
    {
        "Ranking": 18,
        "Proyecto": "Voice-Assistant-GPT",
        "Descripción": "Asistente de voz inteligente basado en GPT-3.",
        "Problema que soluciona": "Necesidad de interacción por voz con sistemas de información judicial.",
        "Cómo lo soluciona": "Proporciona interfaz de voz para consultas y tareas relacionadas con el sistema judicial.",
        "Análisis respecto a criterios del concurso": "Potencial para mejorar la accesibilidad en el sistema judicial, especialmente para personas con discapacidad visual. Requiere adaptación significativa para uso específico en contexto judicial."
    },
    {
        "Ranking": 19,
        "Proyecto": "Monitoreo de Presión Arterial",
        "Descripción": "Aplicación para el seguimiento de la presión arterial.",
        "Problema que soluciona": "No directamente relacionado con problemas judiciales o administrativos.",
        "Cómo lo soluciona": "Permite el registro y visualización de mediciones de presión arterial.",
        "Análisis respecto a criterios del concurso": "Baja relevancia para el sistema judicial. Potencial uso limitado en programas de bienestar para funcionarios judiciales."
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


