from app import Encuesta, Pregunta, Respuesta, Usuario, Grupo

def main():
    # Crea una encuesta
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    print(f"Se ha creado la encuesta: {encuesta.titulo}, fecha: {encuesta.fechaCreacion}")

    # Crea y agrega preguntas a la encuesta
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
    pregunta3 = Pregunta(texto="¿Cómo mejoraría el servicio?")
    
    encuesta.agregar_pregunta(pregunta1)
    encuesta.agregar_pregunta(pregunta2)
    encuesta.agregar_pregunta(pregunta3)

    print(f"La encuesta tiene {len(encuesta.preguntas)} preguntas.")

    # Crea un grupo de usuarios
    grupo = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
    print(f"Se ha creado el grupo: {grupo.nombre} con criterios: {grupo.criterios}")

    # Aplicar la encuesta al grupo
    encuesta.aplicar_a_grupo(grupo)
    print(f"Encuesta aplicada al grupo: {encuesta.grupo.nombre}")

    # Crear un usuario y registrar una respuesta
    usuario = Usuario(nombre="Ana García", email="ana@example.com")
    respuesta = Respuesta(pregunta=pregunta1, usuario=usuario, valor="Excelente")
    print(f"El usuario {usuario.nombre} respondió: {respuesta.valor} a la pregunta: {respuesta.pregunta.texto}")

if __name__ == "__main__":
    main()

