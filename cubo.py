#Atividade 2 N2
#Crie um cubo utilizando opengl com texturas em todas as faces

#EQUIPE:
#Bruno Rocha Sampaio
# Cicero Lucas Silva 
# Rosemelry Mendes da Silva 


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

def carregar_textura(nome_arquivo):
    imagem = Image.open(nome_arquivo)
    imagem = imagem.transpose(Image.FLIP_TOP_BOTTOM)
    dados_imagem = imagem.convert("RGBA").tobytes()
    largura, altura = imagem.size
    
    id_textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id_textura)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, largura, altura, 0, GL_RGBA, GL_UNSIGNED_BYTE, dados_imagem)
    
    return id_textura

def desenhar_cubo(texturas):
    glEnable(GL_TEXTURE_2D)
    # Habilitar texturas antes de desenhar

    # Desenhar cada face do cubo
    faces = [
        (texturas[0], (-1.0, -1.0, 1.0), (1.0, -1.0, 1.0), (1.0, 1.0, 1.0), (-1.0, 1.0, 1.0)),  # Face frontal
        (texturas[1], (-1.0, -1.0, -1.0), (1.0, -1.0, -1.0), (1.0, 1.0, -1.0), (-1.0, 1.0, -1.0)),  # Face traseira
        (texturas[2], (-1.0, 1.0, -1.0), (1.0, 1.0, -1.0), (1.0, 1.0, 1.0), (-1.0, 1.0, 1.0)),  # Face superior
        (texturas[3], (-1.0, -1.0, -1.0), (1.0, -1.0, -1.0), (1.0, -1.0, 1.0), (-1.0, -1.0, 1.0)),  # Face inferior
        (texturas[4], (1.0, -1.0, -1.0), (1.0, 1.0, -1.0), (1.0, 1.0, 1.0), (1.0, -1.0, 1.0)),  # Face direita
        (texturas[5], (-1.0, -1.0, -1.0), (-1.0, 1.0, -1.0), (-1.0, 1.0, 1.0), (-1.0, -1.0, 1.0))   # Face esquerda
    ]

    for textura, v1, v2, v3, v4 in faces:
        glBindTexture(GL_TEXTURE_2D, textura)
        glBegin(GL_QUADS)
        
        # Definir os vértices e coordenadas de textura
        glTexCoord2f(0.0, 0.0); glVertex3f(*v1)
        glTexCoord2f(1.0, 0.0); glVertex3f(*v2)
        glTexCoord2f(1.0, 1.0); glVertex3f(*v3)
        glTexCoord2f(0.0, 1.0); glVertex3f(*v4)
        
        glEnd()  # Finalizar o bloco

    # Desabilitar texturas após desenhar
    glDisable(GL_TEXTURE_2D)  

def main():
    if not glfw.init():
        return
    
    janela = glfw.create_window(640, 480, "Cubo Texturizado", None, None)
    if not janela:
        glfw.terminate()
        return

    glfw.make_context_current(janela)
    glEnable(GL_DEPTH_TEST)

    # Configuração da perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640 / 480, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Carregar texturas
    texturas = []
    try:
        for i in range(1, 7):  # Carregar 6 texturas
            texturas.append(carregar_textura(f"./assets/img/cor{i}.jpg"))

    except Exception as e:

        print(f"Erro ao carregar texturas: {e}")
        glfw.terminate()

        return

    while not glfw.window_should_close(janela):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(glfw.get_time() * 50, 1, 1, 1)

        try:
            desenhar_cubo(texturas)
        except Exception as e:
            
            print(f"Erro ao desenhar o cubo: {e}")

        glfw.swap_buffers(janela)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
