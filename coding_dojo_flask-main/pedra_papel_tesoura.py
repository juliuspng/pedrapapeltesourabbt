from flask import Flask, render_template
# Questão 1, primeiro item
import random
app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template('pedra_papel_tesoura.html', mensagem='', opcao_computador='', opcao_jogador='')

@app.route("/<opcao_jogador>")
def checar_opcao(opcao_jogador):
    mensagem = ''

    # Questão 1, segundo item
    opcao_computador = random.randint(0,2)

    # Questão 1, terceiro item
    match opcao_computador:
      case 0:
        opcao_computador = "pedra"
      case 1:
        opcao_computador = "papel"
      case 2:
        opcao_computador = "tesoura"


    # Questão 2, primeiro item
    print(opcao_jogador)

    # Questão 2, segundo item
    if ((opcao_jogador == "pedra" and
    opcao_computador == "tesoura") or
        (opcao_jogador == "papel" and
    opcao_computador == "pedra") or
        (opcao_jogador == "tesoura" and
    opcao_computador == "papel")
    ):
      mensagem = 'Jogador venceu!'
    else:
      mensagem = 'Computador venceu!'

    # # Questão 2, terceiro item
    if opcao_computador == opcao_jogador:
      mensagem = 'EMPATE'
      
  
    return render_template('pedra_papel_tesoura.html', mensagem=mensagem, opcao_computador=opcao_computador, opcao_jogador=opcao_jogador)

@app.route("/extra")
def acessar_extra():
  return render_template('extra.html')