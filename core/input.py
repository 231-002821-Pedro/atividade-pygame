import pygame

class Input(object):
    def __init__(self):
        # indica se o usuário fechou a aplicação
        self.quit = False

    def update(self):
        # percorre todos os eventos de entrada do usuário (como teclado ou
        # mouse) que ocorreram desde a última vez que os eventos foram verificados
        for event in pygame.event.get():
            # o evento de "quit" ocorre ao clicar no botão de fechar a janela
            if event.type == pygame.QUIT:
                self.quit = True