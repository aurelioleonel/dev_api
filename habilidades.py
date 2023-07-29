from flask_restful import Resource


lista_habilidades = [
    "Python",
    "HTML",
    "CSS",
    "Pascal",
    "Rect"
]
class Habilidades(Resource):
    def get(self):
        return lista_habilidades


