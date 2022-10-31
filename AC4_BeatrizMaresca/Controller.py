from flask import Flask
from AC4_Beatriz_Maresca.Produto_Model import produto_Model


app = Flask(__name__)

@app.route('/v1/aula/consultar/', methods=["GET"])
def consultar():
    return produto_Model.produtos()


if __name__ == '__main__':
    app.run(debug=True,port= 5000)