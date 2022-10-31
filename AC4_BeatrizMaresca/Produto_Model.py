from flask import Flask, request, jsonify, make_response
import json

tasks = [
    {
        'id_produto': 1,
        'name_produto': 'Biscoito de povilho'
    },
    {
        'id_produto': 2,
        'name_produto': 'Club Social'
    },
    {
        'id_produto': 3,
        'name_produto': 'Oreo'
    }
]

listprodutos = json.dumps(tasks)

class produto_Model:
    def produtos():
        return listprodutos

