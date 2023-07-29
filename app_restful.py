from flask import Flask
from flask_restful import Resource, Api
import json
from flask import request
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)


desenvolvedores = [
     {
      "id": 0,
      "nome": "Marcos",
      "habilidade": ["Pyton", "Flask", "Html", "CSS", "Java Script"]
      },

     {
      "id": 1,
      "nome": "Silvana",
      "habilidade": ["Excel", "Contabilidade", "Financeiro", "RH"]
      },

     {
      "id": 2,
      "nome": "Mayara",
      "habilidade": ["Matematica", "Dança", "Judô"]
      }
]


class Desenvolvedor(Resource):

    def get(self, id):

        try:
            response = desenvolvedores[id]

            # for desenvolvedor in desenvolvedores:
            #     if desenvolvedor["id"] == id:
            #         response = desenvolvedores[id]
        except IndexError:
            mensagem = "Registro do ID {} não existe".format(id)
            response = {"Status": "Erro",
                        "Mensagem": mensagem
                        }
            # desenvolvedor_id = desenvolvedores[id]
        except Exception:
            mensagem = "Erro desconhecido, Procure o admnistrador da API"
            response = {"Status": "Erro",
                        "Mensagem": mensagem
                        }

        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"Status": "Sucesso",
                "Mensagem": "Registro excluido com sucesso!!"
                }


class Lista_Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/dev/habilidades/')


if __name__ == "__main__":
    app.run(debug=True)
