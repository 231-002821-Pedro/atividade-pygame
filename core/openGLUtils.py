from OpenGL.GL import *


# métodos estáticos para carregar e compilar shaders do OpenGL
# e vinculá-los para criar programas
class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        # especifica a versão necessária do OpenGL/GLSL
        shaderCode = '#version 330\n' + shaderCode

        # cria um objeto de shader vazio e retorna o valor de referência
        shaderRef = glCreateShader(shaderType)

        # armazena o código-fonte no shader
        glShaderSource(shaderRef, shaderCode)

        # compila o código-fonte armazenado anteriormente no objeto de shader
        glCompileShader(shaderRef)

        # verifica se a compilação do shader foi bem-sucedida
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)

        if not compileSuccess:
            # recupera a mensagem de erro
            errorMessage = glGetShaderInfoLog(shaderRef)

            # libera a memória usada para armazenar o programa de shader
            glDeleteShader(shaderRef)

            # converte a string de bytes em string de caracteres
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # lança uma exceção: interrompe o programa e exibe a mensagem de erro
            raise Exception(errorMessage)

        # a compilação foi bem-sucedida; retorna o valor de referência do shader
        return shaderRef