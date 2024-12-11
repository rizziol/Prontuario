

@echo off
REM Iniciar o servidor Flask
start cmd /k "C:\Python\Python312\python.exe D:\OneDrive\Documentos\Pacientes\prontuarios\app3.py"

REM Esperar alguns segundos para o servidor Flask iniciar
timeout /t 5

REM Abrir o navegador padrão com a página inicial do servidor Flask
start "" http://127.0.0.1:5000

