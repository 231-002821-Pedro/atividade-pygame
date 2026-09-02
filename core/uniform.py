from OpenGL.GL import *


class Uniform(object):

    def __init__(self, dataType, data):

        # tipo de dados:
        # int | bool | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # dados a enviar para a variável uniform
        self.data = data

        # referência para a localização da variável no programa
        self.variableRef = None

    # obtém e armazena a referência da variável do programa com o nome indicado
    def locateVariable(self, programRef, variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)

    # armazena os dados na variável uniform previamente localizada
    def uploadData(self):

        # se o programa não referenciar a variável, sai
        if self.variableRef == -1:
            return

        if self.dataType == "int":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(self.variableRef,
                        self.data[0], self.data[1], self.data[2])
        elif self.dataType == "vec4":
            glUniform4f(self.variableRef,
                        self.data[0], self.data[1], self.data[2], self.data[3])
