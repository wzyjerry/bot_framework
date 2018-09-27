from flask import Flask
from apis.entities import entities_apis
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'bot_framework'
}
db = MongoEngine(app)
app.register_blueprint(entities_apis, url_prefix='/v1/entities/')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()