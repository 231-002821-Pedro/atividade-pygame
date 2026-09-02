import pygame
import sys
from core.input import Input


class Base(object):
    def __init__(self, screenSize=[512, 512]):

        # inicializa todos os módulos do pygame
        pygame.init()
        # indica os detalhes de renderização
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # inicializa buffers para realizar antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # usa um perfil core do OpenGL para compatibilidade entre plataformas
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        # cria e mostra a janela
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        # define o texto que aparece na barra de título da janela
        pygame.display.set_caption("Graphics Window")

        # determina se o loop principal está ativo
        self.running = True
        # gere dados e operações relacionadas com o tempo
        self.clock = pygame.time.Clock()

        # gere a entrada do utilizador
        self.input = Input()

        # número de segundos que a aplicação está em execução
        self.time = 0

    # implementar através de extensão da classe
    def initialize(self):
        pass

    # implementar através de extensão da classe
    def update(self):
        pass

    def run(self):
        ## arranque ##
        self.initialize()

        ## loop principal ##
        while self.running:
            ## processa entrada ##
            self.input.update()
            if self.input.quit:
                self.running = False

            # segundos desde a última iteração do loop principal
            self.deltaTime = self.clock.get_time() / 1000
            # incrementa o tempo que a aplicação está em execução
            self.time += self.deltaTime

            ## atualização ##
            self.update()

            ## renderização ##
            # mostra a imagem no ecrã
            pygame.display.flip()

            # pausa se necessário para atingir 60 FPS
            self.clock.tick(60)

        ## encerramento ##
        pygame.quit()
        sys.exit()
