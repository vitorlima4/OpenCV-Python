import cv2 as cv

imagem = cv.imread('imagens/img.png')

#Cortando uma imagem
recorte = imagem[100:300, 100:300]

cv.imshow("Imagem recortada", recorte)

cv.waitKey(0)
