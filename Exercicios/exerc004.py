import cv2 as cv

imagem = cv.imread('imagens/img.png')

#modificando a imagem com quadrados pretos
for altura in range(0, imagem.shape[0], 10):
    for largura in range(0, imagem.shape[1], 10):
        imagem[altura: altura + 5, largura: largura + 5] = (0, 0, 0)

cv.imshow("Imagem com quadrados", imagem)

cv.waitKey(0)
