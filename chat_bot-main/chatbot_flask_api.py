from flask import Flask, request, jsonify
from services.chatbot_services import run_chatbot
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    api_key = data.get('api_key')

    # Print the API key and query (be cautious with this in production)
    # print(f"Received API Key: {api_key}")
    print(f"Received the query: {query}")
    response=run_chatbot(api_key,query)

    return jsonify({"response": response}), 200

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


