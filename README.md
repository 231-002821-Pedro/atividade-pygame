# janelaPygame

Este projeto foi desenvolvido para a disciplina de **Computação Gráfica** do **Unipac - Barbacena**,
ministrada pelo **Prof. Rodrigo Fernandes dos Santos**.

## Sobre o projeto

Trata-se de um esqueleto de aplicação gráfica usando **Pygame** e **OpenGL**, com uma janela
duplamente bufferizada (double buffer) e suavização de bordas (antialiasing). O projeto fornece uma
estrutura básica (`core/base.py` e `core/input.py`) que é reaproveitada pelos exercícios/checkpoints
da disciplina (como `test-2.1.py`).

## Requisitos

- Python 3.13
- Pygame 2.6.1

## Passo a passo: clonando e executando no PyCharm

Este tutorial assume que você já tem o **PyCharm** e o **Git** instalados no seu computador. Se
ainda não tiver, instale antes de continuar:

- Git: https://git-scm.com/downloads
- PyCharm (Community, que é gratuita, já é suficiente): https://www.jetbrains.com/pycharm/download/

### 1. Clonar o repositório usando o PyCharm

1. Abra o PyCharm.
2. Na tela inicial ("Welcome to PyCharm"), clique em **Get from VCS**.
   - Se o PyCharm já estiver aberto com outro projeto, vá em **File > New > Project from Version
     Control...**.
3. Em **URL**, cole:
   ```
   https://github.com/rodrygofesantos/pygame.git
   ```
4. Escolha a pasta onde o projeto será salvo no seu computador (pode deixar o local sugerido).
5. Clique em **Clone**.
6. O PyCharm vai baixar o projeto e abri-lo automaticamente.

### 2. Configurar o interpretador Python (ambiente virtual)

1. Vá em **File > Settings** (no Windows/Linux) ou **PyCharm > Settings** (no Mac).
2. No menu à esquerda, clique em **Project: pygame > Python Interpreter**.
3. Clique em **Add Interpreter > Add Local Interpreter...**.
4. Selecione **Virtualenv Environment > New**, confirme que a versão do Python é 3.10 ou superior e
   clique em **OK**.
5. Aguarde o PyCharm terminar de criar o ambiente virtual (uma pasta `.venv` vai aparecer no projeto).

### 3. Instalar o Pygame

1. Abra o terminal integrado do PyCharm: menu **View > Tool Windows > Terminal** (ou o atalho
   `Alt+F12`).
2. Confirme que aparece `(.venv)` no começo da linha do terminal — isso indica que o ambiente
   virtual está ativo.
3. Digite o comando abaixo e pressione Enter:
   ```
   pip install pygame
   ```

### 4. Executar o projeto

1. Na árvore de arquivos à esquerda, clique duas vezes em `test-2.1.py` para abri-lo.
2. Clique com o botão direito em qualquer lugar do código e escolha **Run 'test-2.1'**.
   - Alternativamente, clique no ícone de seta verde ▶️ no canto superior direito da janela, ou ao
     lado do número da linha onde está `Test().run()`.
3. Uma janela chamada "Graphics Window" deve abrir na tela.
4. Para fechar o programa, clique no **X** da janela.

### Problemas comuns

- **"ModuleNotFoundError: No module named 'pygame'"** — o interpretador selecionado no PyCharm não é
  o `.venv` do projeto, ou o `pip install pygame` não foi executado nesse ambiente. Repita o passo 2
  e 3 conferindo se o terminal mostra `(.venv)`.
- **A janela não abre ou parece travada** — confira se não há nenhuma outra janela do programa já
  aberta por trás; feche todas e rode de novo. Se estiver usando um notebook/desktop com placa de
  vídeo dedicada, confirme que os drivers de vídeo estão atualizados.
- **Nada acontece ao clicar em Run** — confirme que o arquivo `test-2.1.py` está selecionado/aberto
  como aba ativa antes de clicar em Run.
