#importando a biblioteca
import cv2 as cv

#lendo a imagem
imagem = cv.imread('imagens/img.png')

#mostrando as propriedades e os canais da imagem
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

#mostrando a imagem
cv.imshow("Imagem Original", imagem)

#exibira a janela, até que uma tecla seja pressionada
cv.waitKey(0)
