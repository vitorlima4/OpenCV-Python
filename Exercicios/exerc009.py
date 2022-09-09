import cv2 as cv

imagem = cv.imread('imagens/img.png')

#Redimensionando uma imagem
largura = imagem.shape[1]
altura = imagem.shape[0]
proporcao = float(altura/largura)
largura_nova = 250 #em pixels
altura_nova = int(largura_nova * proporcao)

tamanho_novo = (largura_nova, altura_nova)
redimensionada = cv.resize(imagem, tamanho_novo, interpolation=cv.INTER_AREA)

cv.imshow("Imagem Original", imagem)
cv.imshow("Imagem Redimensionada", redimensionada)

cv.waitKey(0)
