import cv2 as cv

imagem = cv.imread('imagens/img.png')

verde = (0, 255, 0)
azul = (255, 0, 0)
vermelho = (0, 0, 255)

#criando várias formas na imagem
cv.line(imagem, (60, 50), (160, 150), azul, 10)
cv.line(imagem, (60, 150), (160, 50), vermelho, 10)
cv.rectangle(imagem, (60, 50), (160, 150), verde, 10)

(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
for raio in range(0, 150, 20):
    cv.circle(imagem, (X, Y), raio, verde)

cv.imshow("Imagem com formas", imagem)

cv.waitKey(0)
