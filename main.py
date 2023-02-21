#https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699

from http.client import responses
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        print("Hello : " + __name__+":")
        return {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
		'Some are born great, some achieve greatness, and some greatness thrust upon them.']
        },
        'Linus': {
            'quote': ['Talk is cheap. Show me the code.']
            }
        }
    @app.route('/greet/<name>')
    def say_hello(name):
        return 'Hello ' + name

    
    def parse_request():
        msg = request.form['message']
        return 'Hello ' + msg
        
    @app.route('/api/posttoapi', methods=['POST'])
    def ProcessResponse():
        apikey = request.form['apikey']
        model = request.form['model']
        temperature = request.form['temperature']
        max_tokens = request.form['max_tokens']
        top_p = request.form['top_p']
        frequency_penalty = request.form['frequency_penalty']
        presence_penalty = request.form['presence_penalty']
        stop = [" Human:", " AI:"]
        return ' '.join({apikey, model,temperature,max_tokens,top_p,frequency_penalty,presence_penalty})
api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)