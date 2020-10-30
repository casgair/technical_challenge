from flask import Flask, request
import json
import calc

app = Flask(__name__)


@app.route('/', methods=['POST'])
def calculator_post():
    """
    Simple post request function, uses json for input and response.
    """
    data = request.data
    if not data:
        return {"result": "Please provide input in format {'type': 'input'}"}
    json_data = json.loads(data)
    if "prefix" in json_data:
        result = calc.prefix_calculator(json_data["prefix"])
    if "infix" in json_data:
        result = calc.infix_calculator(json_data["infix"])
    return json.dumps({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
