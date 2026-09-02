from OpenGL.GL import *


# métodos estáticos para carregar e compilar shaders OpenGL e ligá-los para criar programas
class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):

        # especifica a versão de OpenGL/GLSL necessária
        shaderCode = '#version 330 \n' + shaderCode

        # cria um objeto shader vazio e devolve o valor de referência
        shaderRef = glCreateShader(shaderType)
        # armazena o código-fonte no shader
        glShaderSource(shaderRef, shaderCode)
        # compila o código-fonte previamente armazenado no objeto shader
        glCompileShader(shaderRef)

        # verifica se a compilação do shader foi bem-sucedida
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)
        if not compileSuccess:
            # obtém a mensagem de erro
            errorMessage = glGetShaderInfoLog(shaderRef)
            # liberta a memória usada para armazenar o programa do shader
            glDeleteShader(shaderRef)
            # converte a byte string numa string de caracteres
            errorMessage = '\n' + errorMessage.decode('utf-8')
            # lança exceção: interrompe o programa e imprime a mensagem de erro
            raise Exception(errorMessage)

        # compilação bem-sucedida; devolve o valor de referência do shader
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        vertexShaderRef = OpenGLUtils.initializeShader(
            vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(
            fragmentShaderCode, GL_FRAGMENT_SHADER)

        # cria um objeto de programa vazio e armazena a referência a ele
        programRef = glCreateProgram()

        # anexa os programas shader previamente compilados
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        # liga o vertex shader ao fragment shader
        glLinkProgram(programRef)

        # verifica se a ligação do programa foi bem-sucedida
        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)
        if not linkSuccess:
            # obtém a mensagem de erro
            errorMessage = glGetProgramInfoLog(programRef)
            # liberta a memória usada para armazenar o programa
            glDeleteProgram(programRef)
            # converte a byte string numa string de caracteres
            errorMessage = '\n' + errorMessage.decode('utf-8')
            # lança exceção: interrompe a aplicação e imprime a mensagem de erro
            raise Exception(errorMessage)

        # ligação bem-sucedida; devolve o valor de referência do programa
        return programRef

    @staticmethod
    def printSystemInfo():
        print("Vendor: "+glGetString(GL_VENDOR).decode('utf-8'))
        print("Renderer: "+glGetString(GL_RENDERER).decode('utf-8'))
        print("OpenGl version supported: " +
              glGetString(GL_VERSION).decode('utf-8'))
        print("GLSL version supported: " +
              glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
