"""foo_post.py.

    Um exemplo de post generico em python usando flask,
    pylint para boas praticas.

Example:
    Para iniciar rode
        $ python fooPost.py
        Metodo Post
            http://127.0.0.1:5000/foo

Attributes:
    Parte destinada a Attributes.

Todo:
    * Lista de todos a fazer, baseado no modelo do guia docstring.


.. _O modelo do guia foi retirado do:
   http://google.github.io/styleguide/pyguide.html

"""
import json
from flask import Flask, make_response, request

APP = Flask(__name__)


@APP.route('/foo', methods=['POST']) #metodo post
def post(): #função post
    """Description a def post"""
    any_array = request.json #request
    response = make_response(json.dumps(any_array))
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*" #controle de premição
    return response


def main(): #função main seguindo as boas práticas
    """Function to good practice"""
    return APP.run()


if __name__ == '__main__':
    main()
