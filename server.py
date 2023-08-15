from flask import Flask,request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    first_number = data['first']
    second_number = data['second']
    result = first_number + second_number
    response = {'result': result}
    return jsonify(response), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    first_number = data['first']
    second_number = data['second']
    result = first_number - second_number
    response = {'result': result}
    return jsonify(response), 200
if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
