from flask import Flask, render_template, request
# Questão 1, primeiro item


app = Flask(__name__)

# Questao 1, segundo item
# numero_secreto = 

@app.route("/", methods=['GET', 'POST'])
def checar_palpite():
    mensagem = ''
    if request.method == 'POST':
        palpite = request.form['palpite']
        # Questão 2, primeiro item
        

        # Questão 2, segundo item
        

    return render_template('adivinhar_numero.html', mensagem=mensagem)
