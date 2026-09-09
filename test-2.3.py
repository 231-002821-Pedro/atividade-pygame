from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


# desenha seis pontos dispostos em hexágono
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

        ### definições de renderização (opcional) ###
        # o perfil core do macOS só suporta largura de linha 1.0;
        # valores maiores geram GLError(1281, "invalid value")
        try:
            glLineWidth(4)
        except Exception:
            pass

        ### configura o vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### configura o atributo de vértice ###
        positionData = [[0.8, 0.0, 0.0], [0.4, 0.6, 0.0],
                        [-0.4, 0.6, 0.0], [-0.8, 0.0, 0.0],
                        [-0.4, -0.6, 0.0], [0.4, -0.6, 0.0]]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(
            self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


# instancia esta classe e executa o programa
