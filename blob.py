from flask import Flask, request, jsonify

from Model.Article import *
from Controller.ArticleController import *

app = Flask(__name__)

artcon = ArticleController()


@app.route('/api/articles', methods=['POST'])
def post_article():
    data = request.get_json()
    artc = Article(**data)
    artcon.create_article(artc)
    return "OK 201"  # STUB


@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    return artcon.get_articles()


@app.route('/')
def hello_world():  # put application's code here
    return 'add /api'


@app.route('/api')
def help_route():  # put application's code here
    return 'routes: \'/api\', \'/api/articles\' [GET & POST], \'/api/articles/{id}\' [GET]'


if __name__ == '__main__':
    app.run()