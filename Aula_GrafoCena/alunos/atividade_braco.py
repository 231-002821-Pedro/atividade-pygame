# ATIVIDADE: braço robótico com grafo de cena.
# Leia ATIVIDADE.md e complete os trechos marcados com TODO.
# ESC fecha. P salva capturas/resultado.png para a entrega.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.object3D import Object3D
from formas import caixa

CINZA = [0.6, 0.62, 0.66]
LARANJA = [0.98, 0.45, 0.2]
AZUL = [0.25, 0.5, 0.95]
VELOCIDADE = 1.5  # radianos por segundo


class Braco(Base):

    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 1.9, 4.2])
        self.camera.rotateX(-0.2)

        chao = caixa(6, 0.1, 6, [0.8, 0.82, 0.85])
        chao.setPosition([0, -0.05, 0])
        self.scene.add(chao)

        # base: caixa de altura 0.4, apoiada no chão
        self.base = caixa(1.0, 0.4, 1.0, CINZA)
        self.base.setPosition([0, 0.2, 0])
        self.scene.add(self.base)

        # TODO 1: crie self.ombro = Object3D(), filho da base, no TOPO da base.
        #         Crie o braço: caixa(0.3, 1.2, 0.3, LARANJA), filho do ombro,
        #         posicionado para que a ponta de BAIXO fique no ombro.

        # TODO 2: crie self.cotovelo = Object3D(), filho do ombro, na ponta de CIMA do braço.
        #         Crie o antebraço: caixa(0.25, 1.0, 0.25, AZUL), filho do cotovelo,
        #         com a ponta de baixo no cotovelo.

        # TODO 3: crie a garra: caixa(0.5, 0.15, 0.5, CINZA), na ponta do antebraço.

    def update(self):
        angulo = VELOCIDADE * self.deltaTime
        # TODO 4: A e D giram a base em torno do eixo Y.
        # TODO 5: W e S giram o ombro e I e K giram o cotovelo, ambos em torno do eixo Z.
        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Braco(title='Atividade: braço robótico').run(args.frames, args.screenshot)
