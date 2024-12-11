from flask import Flask, render_template, request, redirect
import pandas as pd
import os.path

app = Flask(__name__, static_folder='static')

# Rota para exibir o formulário
@app.route('/')
def form():
    return render_template('form.html')

# Rota para lidar com o envio do formulário
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Recebe os dados do formulário
    data_avaliacao = request.form['data_avaliacao']
    nome = request.form['nome']
    idade = request.form['idade']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email']
    endereco = request.form['endereco']
    cep = request.form['cep']
    regiao = request.form['regiao']
    diagnostico_medico = request.form['diagnostico_medico']
    queixa = request.form['queixa']
    antecedentes = request.form['antecedentes']
    hma = request.form['hma']
    inspecao = request.form['inspecao']
    questionario = request.form['questionario']
    questionario_score = request.form['questionario_score']

   
    # Verifica se o arquivo já existe para decidir se cria ou adiciona dados
    if os.path.exists('dados_pacientes.xlsx'):   
   
   # Se existir, carrega o arquivo existente e adiciona uma nova linha com os dados do formulário
        df = pd.read_excel('dados_pacientes.xlsx')
        novo_dado = pd.DataFrame({
            'Data da Avaliação': [data_avaliacao],
            'Nome': [nome],
            'Idade': [idade],
            'CPF': [cpf],
            'Telefone': [telefone],
            'Email': [email],
            'Endereço': [endereco],
            'CEP': [cep],
            'Região Acometida': [regiao],
            'Diagnóstico Médico': [diagnostico_medico],
            'Queixa Principal': [queixa],
            'Antecedentes Pessoais': [antecedentes],
            'História da Moléstia Atual': [hma],
            'Inspeção, Palpação, Força e ADM': [inspecao],
            'Questionário': [questionario],
            'Questionário Score': [questionario_score]
        })
        df = pd.concat([df, novo_dado], ignore_index=True)
    else:
        # Se não existir, cria um novo DataFrame com os dados do formulário
        df = pd.DataFrame({
            'Data da Avaliação': [data_avaliacao],
            'Nome': [nome],
            'Idade': [idade],
            'CPF': [cpf],
            'Telefone': [telefone],
            'Email': [email],
            'Endereço': [endereco],
            'CEP': [cep],
            'Região Acometida': [regiao],
            'Diagnóstico Médico': [diagnostico_medico],
            'Queixa Principal': [queixa],
            'Antecedentes Pessoais': [antecedentes],
            'História da Moléstia Atual': [hma],
            'Inspeção, Palpação, Força e ADM': [inspecao],
            'Questionário': [questionario],
            'Questionário Score': [questionario_score]
        })


    # Salva os dados em um arquivo xlsx
    df.to_excel('dados_pacientes.xlsx', index=False)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
