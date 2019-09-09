# Comparador de Método de Busca

O trabalho consiste em demonstrar uma comparação de tempo de execução entre os métodos de ordenação: Bubble Sort, Shell Sort, Selection Sort e Insetion Sort

## Execute locamente com virtualenv
- Crie um arquivo virtualenv `virtualenv -p python3 env`
- Ative com `source env/bin/activate`
- Instale os requirimentos `pip install -r requirements.txt`
- Execute o servidor web gunicorn `gunicorn app:app --bind 0.0.0.0:5000 --reload`

## Execução
1) Insira o valor máximo do array, a partir desse número serão gerados valores aleatórios para a amostra
2) Insira os 2 métodos de ordenção a serem comparados
3) Visualize a comparação quanto ao tempo de execução de cada método graficamente em microsegundos.