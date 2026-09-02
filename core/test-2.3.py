from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


# desenha duas formas
class Test(Base):

    def initialize(self):

        print("Initializing program...")

        ### inicializa o programa ###
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(
                position.x, position.y, position.z, 1.0);
        }
        """

        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### definições de renderização ###
        # o perfil core do macOS só suporta largura de linha 1.0;
        # valores maiores geram GLError(1281, "invalid value")
        try:
            glLineWidth(4)
        except Exception:
            pass

        ### configura o vertex array object - triângulo ###
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)
        positionDataTri = [[-0.5, 0.8, 0.0],
                           [-0.2, 0.2, 0.0],
                           [-0.8, 0.2, 0.0]]
        self.vertexCountTri = len(positionDataTri)
        positionAttributeTri = Attribute("vec3", positionDataTri)
        positionAttributeTri.associateVariable(
            self.programRef, "position")

        ### configura o vertex array object - quadrado ###
        self.vaoSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSquare)
        positionDataSquare = [[0.8, 0.8, 0.0],
                              [0.8, 0.2, 0.0],
                              [0.2, 0.2, 0.2],
                              [0.2, 0.8, 0.0]]
        self.vertexCountSquare = len(positionDataSquare)
        positionAttributeSquare = Attribute("vec3", positionDataSquare)
        positionAttributeSquare.associateVariable(
            self.programRef, "position")

    def update(self):
        # usa o mesmo programa para renderizar ambas as formas
        glUseProgram(self.programRef)

        # desenha o triângulo
        glBindVertexArray(self.vaoTri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri)

        # desenha o quadrado
        glBindVertexArray(self.vaoSquare)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountSquare)


# instancia esta classe e executa o programa
Test().run()
