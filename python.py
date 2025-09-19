# Primeiro, instale o Flask se você não tiver:
# pip install Flask

from flask import Flask, render_template, request

# Cria a aplicação Flask
app = Flask(__name__)

# Define a rota para a página inicial
@app.route('/')
def index():
    """Renderiza a página inicial com o formulário."""
    return render_template('index.html')

# Define a rota que recebe os dados do formulário
@app.route('/enviar', methods=['POST'])
def enviar():
    """Processa os dados recebidos do formulário."""
    # Coleta os dados do formulário
    nome = request.form.get('name')
    email = request.form.get('email')
    mensagem = request.form.get('message')

    # Aqui você faria algo com os dados, como:
    # - Enviar um email
    # - Salvar em um banco de dados
    # Por enquanto, vamos apenas imprimi-los no console para ver que funcionou.
    print("----- NOVA MENSAGEM RECEBIDA -----")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Mensagem: {mensagem}")
    print("---------------------------------")

    # Retorna para a página inicial com uma mensagem de sucesso
    return render_template('index.html', message="Mensagem enviada com sucesso!")

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)
