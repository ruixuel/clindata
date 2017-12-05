from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/query', methods=['GET'])
def query():
    age = request.args['age']
    age_group = request.args['age-group']
    gender = request.args['gender']
    weight = request.args['weight']
    seq_list = request.args.getlist('sequence')
    rxcui_list = request.args.getlist('rxcui')
    reported_roles_list = request.args.getlist('reported-role')
    dechal_list = request.args.getlist('dechal')
    rechal_list = request.args.getlist('rechal')
    indications_list = request.args.getlist('indications')
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
