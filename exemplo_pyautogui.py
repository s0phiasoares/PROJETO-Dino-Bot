import pyautogui as auto
import os


##Configuração do erro
auto.useImageNotFoundException()


CAMINHO_IMAGENS = ".\\Automacao\\img"


lista_imagens = os.listdir(CAMINHO_IMAGENS) 
caminho_dino = ".\\Automacao\\dino.png"


while True:
    #Pecorre as imagens da pasta img
    for imagem in lista_imagens:
        #Pega o caminho dessas imagens uma a uma
        caminho_imagem = os.path.join(CAMINHO_IMAGENS,imagem)
        #Se a imagem não é encontrada na tela, o pyautogui emite um erro
        #Por isso utilizamos o bloco try
        try:
            posicao_dino = auto.locateOnScreen(caminho_dino, confidence=0.6)
            posicao_cacto = auto.locateOnScreen(caminho_imagem, confidence=0.8)
        #Ao invés do programa quebrar, nós capturamos o erro e
        #Colocamos o valor None em posicao_cacto
        except auto.ImageNotFoundException:
            posicao_cacto = None
            posicao_dino = None
        #Se não houve erro (uma das imagens foi encontrada)
        #Falamos qual imagem foi encontrada e apertamos a tecla espaço.
        else:
            px_dino = posicao_dino.left
            px_cacto = posicao_cacto.left


            if px_cacto - px_dino <= 150:
                auto.press("space")
                auto.keyDown("space")
        
        #TO DO:
        # - Identificar pterodáctilo
        # - Identificar mapa a noite (PENSAMENTO DO PROF: talvez usar GRAYSCALE)