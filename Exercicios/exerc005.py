import cv2 as cv

imagem = cv.imread('imagens/img.png')

#criando várias formas na imagem
imagem[30:50, :] = (0, 0, 0)
imagem[60:160, 50:150] = (0, 255, 255)
imagem[160:260, 150:250] = (255, 255, 0)
imagem[300:400, 50:250] = (0, 0, 255)
imagem[260:360, 50:150] = (255, 0, 0)

cv.imshow("Imagem com Formas", imagem)

cv.waitKey(0)
