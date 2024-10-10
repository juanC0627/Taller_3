import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from app import Encuesta, Pregunta, Respuesta, Usuario, Grupo
#from ..app import Encuesta, Pregunta, Respuesta, Usuario, Grupo




from app.encuesta import Encuesta
from app.grupo import Grupo
from app.pregunta import Pregunta
from app.respuesta import Respuesta
from app.usuario import Usuario




# Pruebas para la clase Encuesta
def test_crear_encuesta():
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    assert encuesta.titulo == "Encuesta de Satisfacción"

def test_agregar_pregunta():
    encuesta = Encuesta(titulo="Encuesta de Satisfacción")
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
    pregunta3 = Pregunta(texto="¿Cómo mejoraría el servicio?")
    encuesta.agregar_pregunta(pregunta1)
    encuesta.agregar_pregunta(pregunta2)
    encuesta.agregar_pregunta(pregunta3)
    assert len(encuesta.preguntas) == 3

# Pruebas para la clase Pregunta
def test_crear_pregunta():
    pregunta = Pregunta(texto="¿Cuál es su edad?")
    assert pregunta.texto == "¿Cuál es su edad?"

# Pruebas para la clase Respuesta
def test_crear_respuesta():
    usuario = Usuario(nombre="Juan Pérez", email="juan@example.com")
    pregunta = Pregunta(texto="¿Cómo calificaría el servicio?")
    respuesta = Respuesta(pregunta, usuario, "Excelente")
    assert respuesta.valor == "Excelente"

# Pruebas para la clase Usuario
def test_crear_usuario():
    usuario = Usuario(nombre="Ana García", email="ana@example.com")
    assert usuario.nombre == "Ana García"

# Pruebas para la clase Grupo
def test_crear_grupo():
    grupo = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
    assert grupo.nombre == "Clientes VIP"

# Pruebas para la integración entre clases
def test_encuesta_con_grupo():
    encuesta = Encuesta(titulo="Encuesta de Satisfacción")
    grupo = Grupo(nombre="Clientes VIP")
    encuesta.aplicar_a_grupo(grupo)
    assert encuesta.grupo == grupo