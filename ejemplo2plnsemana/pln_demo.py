import spacy  
from textblob import TextBlob 

# Carga el modelo en español de spaCy para que detecte entidades como personas, fechas, etc.
nlp = spacy.load("es_core_news_sm")

# Le pido al usuario que ingrese el texto, línea por línea
print("Escribí o pegá el texto a analizar (ENTER dos veces para terminar):")
lineas = []
while True:
    linea = input()

    if linea.strip() == "":
        break
    lineas.append(linea)

# Uno todas las líneas en una sola cadena para analizarla completa
texto = "\n".join(lineas)


print("\nAnálisis de Sentimientos por Oración")
blob = TextBlob(texto)  # Paso el texto a TextBlob para poder trabajar con oraciones y sentimientos
oraciones = blob.sentences  # se Divide el texto en oraciones

# Contadores para llevar la cuenta de oraciones positivas, negativas y neutras(esto se lo añadi yo 

positivas = 0
negativas = 0
neutras = 0


for i, oracion in enumerate(oraciones, start=1):
    polarity = oracion.sentiment.polarity  # Valor que indica si es positivo (>0), negativo (<0) o neutro (~0)
    print(f"Oración {i}: {oracion}")
    print(f"  Sentimiento (polarity, subjetividad): {oracion.sentiment}")
    
    # Clasifico la oración según el valor de polarity
    if polarity > 0.1:
        positivas += 1
    elif polarity < -0.1:
        negativas += 1
    else:
        neutras += 1


print("\nReconocimiento de Entidades")
doc = nlp(texto)  # Paso el texto por spaCy para identificar entidades nombradas
entidades = list(doc.ents)  # Guardo la lista de entidades detectadas

# Imprimo cada entidad y su tipo (persona, organización, fecha, etc.)
for ent in entidades:
    print(f"{ent.text} → {ent.label_}")

# ===== RESUMEN SIMULADO =====
print("\nResumen Simulado")
# Selecciono oraciones que mencionen palabras clave que me interesan para el resumen
oraciones_clave = [
    oracion for oracion in oraciones
    if "Apple" in oracion or "Tim Cook" in oracion or "Apple Music" in oracion
]

# Imprimo las oraciones clave como si fueran un resumen manual
for oracion in oraciones_clave:
    print("•", oracion)

# ===== PREGUNTA Y RESPUESTA BÁSICA =====
print("\nPregunta: ¿Quién adquirió Beats?")
respuesta = None
# Busco entre las entidades si aparece "Beats" y asumo que "Apple" es quien lo adquirió
for ent in entidades:
    if "Beats" in ent.text:
        respuesta = "Apple"

# Imprimo la respuesta o que no se encontró nada si no está en el texto
print(f"Respuesta: {respuesta if respuesta else 'No encontrado'}")

# ===== RESUMEN FINAL DEL ANÁLISIS =====
print("\nResumen del Análisis")
print(f"Cantidad de oraciones analizadas: {len(oraciones)}")
print(f"Cantidad de oraciones positivas: {positivas}")
print(f"Cantidad de oraciones negativas: {negativas}")
print(f"Cantidad de oraciones neutras: {neutras}")
print(f"Cantidad de entidades encontradas: {len(entidades)}")
print(f"Oraciones clave seleccionadas como resumen: {len(oraciones_clave)}")
