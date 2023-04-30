from flask import Flask, request, jsonify
from llama_index import GPTSimpleVectorIndex
import os
from flask_cors import CORS

os.environ["OPENAI_API_KEY"] = 'YOUR_API_KEY_HERE'

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    # extract query text from POST request body
    query = request.json['query']

    # load index from disk
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

    # query index and return response
    response = index.query(query)
    return jsonify({'response': response.response})

if __name__ == '__main__':
    app.run(port=9876)
