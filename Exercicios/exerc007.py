import cv2 as cv

imagem = cv.imread('imagens/img.png')

#adicionando texto na imagem
fonte = cv.FONT_ITALIC
cv.putText(imagem, 'Ola, Mundo!', (0, 50), fonte, 1, (255, 255, 255), 3, cv.LINE_AA)

cv.imshow("Imagem com texto", imagem)

cv.waitKey(0)
