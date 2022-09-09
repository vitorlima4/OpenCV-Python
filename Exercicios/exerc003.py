import cv2 as cv

imagem = cv.imread('imagens/img.png')

#modificando a imagem
for altura in range(0, imagem.shape[0]):
    for largura in range(0, imagem.shape[1]):
        imagem[altura, largura] = (largura % 256, altura % 256, altura % 256)

cv.imshow("Imagem Modificada", imagem)

cv.waitKey(0)
