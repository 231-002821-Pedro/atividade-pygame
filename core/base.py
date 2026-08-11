import pygame
import sys

from core.input import Input


class Base(object):
    def __init__(self, screenSize=[512, 512]):
        # inicializa todos os módulos do pygame
        pygame.init()

        # define os detalhes de renderização
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # inicializa os buffers para realizar antialiasing (suavização de bordas)
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLESAMPLES, 4)

        # usa um perfil "core" do OpenGL para compatibilidade entre plataformas
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE)

        # cria e exibe a janela
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # define o texto que aparece na barra de título da janela
        pygame.display.set_caption("Graphics Window")

        # indica se o loop principal está ativo
        self.running = True

        # controla o tempo e opera com dados relacionados a ele (FPS, delta time, etc.)
        self.clock = pygame.time.Clock()

        # processa eventos de entrada (como fechar a janela)
        self.input = Input()

    # deve ser implementado ao estender a classe
    def initialize(self):
        pass

    # deve ser implementado ao estender a classe
    def update(self):
        pass

    def run(self):
        ## inicialização ##
        self.initialize()

        ## loop principal ##
        while self.running:
            ## processa entradas (input) ##
            self.input.update()
            if self.input.quit:
                self.running = False

            ## atualiza ##
            self.update()

            ## renderiza ##
            # exibe a imagem na tela
            pygame.display.flip()

            # pausa se necessário para manter 60 quadros por segundo (FPS)
            self.clock.tick(60)

        ## encerramento ##
        pygame.quit()
        sys.exit()

