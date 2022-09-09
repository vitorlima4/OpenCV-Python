import cv2 as cv

imagem = cv.imread('imagens/img.png')

#modificando a imagem com cores
for altura in range(0, imagem.shape[0]):
    for largura in range(0, imagem.shape[1]):
        imagem[altura, largura] = (0, 255, 255)

cv.imshow("Imagem Amarelada", imagem)

cv.waitKey(0)
