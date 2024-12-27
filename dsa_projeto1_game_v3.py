import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
           -
        """
    ]
    return stages[chances]

# Função do jogo
def game():
    while True:
        limpa_tela()
        print("\nBem vindo ao jogo da forca!")
        print("Escolha um nível de dificuldade: 1 - Fácil, 2 - Médio, 3 - Difícil\n")

        nivel = input("Digite o número do nível desejado: ")
        while nivel not in ['1', '2', '3']:
            nivel = input("Escolha inválida. Digite 1, 2 ou 3: ")

        nivel = int(nivel)

        palavras_com_dicas = {
            1: {
                'gato': ["É um animal", "Tem bigodes", "Adora caçar ratos"],
                'casa': ["É um lugar", "Serve como abrigo", "Pode ter muitos cômodos"],
                'bola': ["É redonda", "Usada em esportes", "Pode ser de futebol"]
            },
            2: {
                'abacate': ["É verde por fora", "Tem uma grande semente", "Usado para guacamole"],
                'morango': ["É vermelho", "Tem sementes na superfície", "Usado em sobremesas"],
                'banheiro': ["É um cômodo", "Tem pia e vaso sanitário", "Usado para higiene"]
            },
            3: {
                'astronauta': ["Viaja pelo espaço", "Usa um traje especial", "Trabalha em uma nave espacial"],
                'helicóptero': ["Pode voar", "Tem hélices", "Usado em resgates"],
                'turbulência': ["É sentida em aviões", "Pode causar medo", "Ocorre em áreas de instabilidade"]
            }
        }

        palavras_nivel = palavras_com_dicas[nivel]
        palavra = random.choice(list(palavras_nivel.keys()))
        dicas = palavras_nivel[palavra]

        lista_letras_palavras = [letra for letra in palavra]
        tabuleiro = ["_"] * len(palavra)
        chances = 6
        dicas_usadas = 0
        letras_tentativas = []

        while chances > 0:
            print(display_hangman(chances))
            print("Palavra: ", " ".join(tabuleiro))
            print(f"Chances restantes: {chances}")
            print(f"Dicas disponíveis: {3 - dicas_usadas}\n")

            escolha = input("Digite uma letra ou digite 'dica' para pedir uma dica: ").lower()

            if escolha == 'dica':
                if dicas_usadas < 3:
                    print(f"Dica {dicas_usadas + 1}: {dicas[dicas_usadas]}")
                    dicas_usadas += 1
                    chances -= 1
                else:
                    print("Você já usou todas as suas dicas!")
                continue

            if escolha in letras_tentativas:
                print("Você já tentou essa letra. Escolha outra!")
                continue

            letras_tentativas.append(escolha)

            if escolha in lista_letras_palavras:
                print("Você acertou a letra!")
                for indice in range(len(lista_letras_palavras)):
                    if lista_letras_palavras[indice] == escolha:
                        tabuleiro[indice] = escolha

                if "_" not in tabuleiro:
                    print(f"\nVocê venceu! A palavra era: {palavra}")
                    break
            else:
                print("Ops. Essa letra não está na palavra!")
                chances -= 1

        if "_" in tabuleiro:
            print(f"\nVocê perdeu! A palavra era: {palavra}.")

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("\nObrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    game()
    
