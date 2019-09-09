from flask import Flask, render_template,request, jsonify, json
from switch_method import switch_method

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    Meth1 = []
    Meth2 = []
    max = []
    value = []

    if request.method == 'POST':
        
        forms = {
            'first': request.form['first'], 
            'second': request.form['second'],
            'max': request.form['max'],
        }

        print(forms['first'])
        print(forms['second'])

        max = int(forms['max'])

        Meth1 = forms['first']
        Meth2 = forms['second']
        
        steps1 = switch_method(forms['first'], max)
        steps2 = switch_method(forms['second'], max)
        
        value.append(round(steps1, 3))
        value.append(round(steps2, 3))

    return render_template("index.html", value=json.dumps(value), Meth1=Meth1, Meth2=Meth2, max=json.dumps(max))


if __name__ == '__main__':
    app.run(debug=True)