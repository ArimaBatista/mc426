import os
import bot_comando

def test_comparar_arquivos():
    input_dir = 'in'
    output_dir = 'out'

    for filename in os.listdir(input_dir):
        # Construir os caminhos completos para o arquivo de entrada e saída correspondente
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Ler o arquivo de entrada
        with open(input_path, 'r') as input_file:
            entrada = input_file.read()

        # Executar lógica ou função que gera a saída
        saida = bot_comando.comando(entrada, 1)

        # Ler o arquivo de saída esperado
        with open(output_path, 'r') as expected_output_file:
            saida_esperada = expected_output_file.read()

        # Comparar a saída com a saída esperada
        assert saida == saida_esperada