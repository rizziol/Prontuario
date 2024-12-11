Este é um projeto simples, feito como um exercício simples de programação em Python, mais especificamente utilizando o flask.
A intenção foi construir um formulário em HTML e, ao inserir os valores nos campos, esses valores alimentariam uma planilha no formato .xlsx. Esse código é altamente customizável,
podendo a saída ser alterada para outros formatos. A idéia é o código ser rodado localmente.

* app3.py : toda a lógica POST e GET está contida ali, bem como os códigos para salvar os dados na planilha;
* PRONTUÁRIO.bat : é um arquivo executável que inicializa os códigos e abre o formulário em um browser;

* templates
    * form.html : é o arquivo de frontend do prontuário;
    * teste.html : este era um arquivo de experimentação, não sendo necessário para o projeto. Usei esse arquivo para gerar as alterações visuais que desejava antes de transferir
 para o arquivo form.html;
* static
    * R3.png : logo da empresa Riscienza;
    * Rubik-Medium.ttf: fonte do formulário;
    * style.css : arquivo contendo dados da estética do formulário.
