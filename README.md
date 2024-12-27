# Jogo da Forca em Python

Este projeto é uma implementação simples do jogo da forca em Python, com opções de níveis de dificuldade e dicas para ajudar o jogador. O jogo é interativo e roda diretamente no terminal.

## Funcionalidades

- **Níveis de dificuldade:**
  - Nível 1: Fácil
  - Nível 2: Médio
  - Nível 3: Difícil

- **Dicas:**
  - Cada palavra possui até 3 dicas relacionadas a ela.
  - Cada dica utilizada reduz o número de chances disponíveis.

- **Interface:**
  - Mostra um desenho da forca atualizado a cada tentativa.
  - Indica as chances restantes e dicas disponíveis.

## Pré-requisitos

- Python 3.6 ou superior.

## Como executar o jogo

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/jogo-da-forca.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd jogo-da-forca
   ```

3. Execute o jogo:
   ```bash
   python forca_com_dicas.py
   ```

## Regras do Jogo

1. Escolha um nível de dificuldade.
2. Tente adivinhar a palavra uma letra por vez.
3. Use a opção de pedir dicas se necessário, mas lembre-se de que cada dica reduz suas chances.
4. Vença adivinhando a palavra antes de perder todas as chances.

## Exemplo de Execução

```plaintext
Bem vindo ao jogo da forca!
Escolha um nível de dificuldade: 1 - Fácil, 2 - Médio, 3 - Difícil

Digite o número do nível desejado: 1

--------
|      |
|      
|      
|      
|      
-

Palavra: _ _ _ _
Chances restantes: 6
Dicas disponíveis: 3

Digite uma letra ou digite 'dica' para pedir uma dica: a
Você acertou a letra!

--------
|      |
|      
|      
|      
|      
-

Palavra: a _ a _
Chances restantes: 6
Dicas disponíveis: 3

...
```

## Estrutura do Código

- O código principal está no arquivo `forca_com_dicas.py`.
- O jogo utiliza funções para limpar a tela, exibir o estado da forca e executar a lógica principal do jogo.
- As palavras e dicas são organizadas por níveis de dificuldade.

## Personalização

- Para adicionar novas palavras e dicas, edite o dicionário `palavras_com_dicas` no código.
- Você pode ajustar o número de dicas disponíveis ou o número de chances.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.




