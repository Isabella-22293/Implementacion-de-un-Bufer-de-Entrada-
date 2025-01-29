#Carga de un fragmento en la entrada del bufer
def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

#Procesa el bufer y extrae los lexemas
def procesar_buffer(buffer, avance, lexema_parcial):
    lexema = lexema_parcial  # Recuperar lexema parcial del fragmento anterior
    while avance < len(buffer):
        char = buffer[avance]
        avance += 1
        
        if char == " " or char == "eof":
            if lexema:  # Procesa Si hay contenido en el lexema
                print("Lexema procesado:", "".join(lexema))
                lexema = []
            if char == "eof":
                break  # Fin del procesamiento
        else:
            lexema.append(char)
    return avance, lexema

# Configuración inicial
entrada = list("Esto es un ejemplo eof")
inicio = 0
tamano_buffer = 10
lexema_parcial = []  # Guardar lexemas divididos entre fragmentos

# Procesar la entrada en fragmentos
while True:
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    avance = 0
    avance, lexema_parcial = procesar_buffer(buffer, avance, lexema_parcial)
    
    # Detener el procesamiento si se llega al marcador "eof"
    if "eof" in buffer:
        break
    
    # Actualizar el puntero de inicio para cargar el siguiente fragmento
    inicio += tamano_buffer

# Procesar cualquier lexema parcial que quede después del último fragmento
if lexema_parcial:
    print("Lexema procesado:", "".join(lexema_parcial))
