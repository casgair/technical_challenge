## Requirements

Please run `pip install -r requirements.txt` which installs Flask for the API.

## Prefix and Infix calculator

To run through all test cases for both prefix and infix calculator run `python calc.py`.

## RESTful API

To use the web app first run `python web_app.py`.

The API only has one function which takes requests in JSON format.
The format is {"type": "input"} where "type" is either "prefix" or "infix", and "input" is the correponding input to be calculated. Example requests:

* `curl -d '{"prefix": "- / 10 + 1 1 * 1 2"}' -H 'Content-Type: application/json' http://127.0.0.1:5000`
* `curl -d '{"infix": "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"}' -H 'Content-Type: application/json' http://127.0.0.1:5000`
