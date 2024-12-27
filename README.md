Aqui está o README atualizado com todas as alterações realizadas no código, incluindo a implementação de orientação a objetos, exibição de letras erradas e o uso do bloco `try-except`:

---

# Jogo da Forca em Python

Este projeto é uma implementação do jogo da forca em Python utilizando Programação Orientada a Objetos (POO). O jogo oferece opções de níveis de dificuldade, permite o uso de dicas e exibe as letras erradas já tentadas, proporcionando uma experiência mais interativa e fluída.

## Funcionalidades

- **Níveis de dificuldade:**
  - Nível 1: Fácil
  - Nível 2: Médio
  - Nível 3: Difícil

- **Dicas:**
  - Cada palavra possui até 3 dicas relacionadas a ela.
  - Cada dica utilizada reduz o número de chances disponíveis.

- **Letras erradas:**
  - O jogo exibe as letras que o jogador já tentou e que estão erradas, ajudando a evitar tentativas repetidas.

- **Interface:**
  - Mostra um desenho da forca atualizado a cada tentativa.
  - Indica as chances restantes, as dicas disponíveis e as letras erradas tentadas.
  
- **Manejo de erros:**
  - O jogo utiliza blocos `try-except` para garantir que o jogador insira entradas válidas, como uma letra única, ou um número de nível válido.

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

1. Escolha um nível de dificuldade (Fácil, Médio ou Difícil).
2. Tente adivinhar a palavra, uma letra por vez.
3. Use a opção de pedir dicas se necessário, mas lembre-se de que cada dica reduz suas chances.
4. Vença ao adivinhar a palavra antes de perder todas as chances.
5. O jogo também mostrará as letras que você já tentou e que estão erradas.

## Exemplo de Execução

```plaintext
Bem-vindo ao jogo da forca!
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
Letras erradas: 

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
Letras erradas: 

Digite uma letra ou digite 'dica' para pedir uma dica: z
Ops. Essa letra não está na palavra!

--------
|      |
|      O
|      
|      
|      
-

Palavra: a _ a _
Chances restantes: 5
Dicas disponíveis: 3
Letras erradas: z

Digite uma letra ou digite 'dica' para pedir uma dica: dica
Dica 1: É um animal

...
```

## Estrutura do Código

- O código foi reestruturado para utilizar Programação Orientada a Objetos. As principais classes são:
  - **`Tabuleiro`**: Responsável pela representação da palavra oculta e atualização do estado do tabuleiro.
  - **`Forca`**: Controla a lógica do jogo, incluindo a escolha da palavra, o controle das chances, e a interação com o jogador (incluindo letras erradas e dicas).
  
- O código principal está no arquivo `forca_com_dicas.py`.
- O jogo utiliza funções para limpar a tela, exibir o estado da forca, gerenciar a entrada do jogador e executar a lógica principal do jogo.
- As palavras e dicas são organizadas por níveis de dificuldade no dicionário `palavras_com_dicas`.

## Personalização

- Para adicionar novas palavras e dicas, edite o dicionário `palavras_com_dicas` no código.
- Você pode ajustar o número de dicas disponíveis ou o número de chances alterando os valores dentro da classe `Forca`.
- A lista `letras_erradas` pode ser acessada para modificar a forma como as letras erradas são exibidas ou manipuladas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

Esse README reflete as modificações feitas no código, como o uso de POO, a adição das letras erradas e o uso do `try-except` para melhor gerenciamento de erros.
