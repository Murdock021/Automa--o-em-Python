import pyautogui
from time import sleep

#Sistema de automoção de cadastor de produtos 

# 1-  digitar meu usuario 
pyautogui.click(955,539, duration = 1)
pyautogui.write('diogo')
# 2 - digitar minha senha 
pyautogui.click(954,563, duration = 1)
pyautogui.write('123456')
# 3 - Clicar em " Entrar "
pyautogui.click(868,598, duration = 1)
# 4 - Extrari Produto  
with open ('produtos.txt','r') as arquivo:
    for linha in arquivo: 
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1 - clicar e digitar produto 
        pyautogui.click(673,525 , duration = 0.5)
        pyautogui.write(produto)
        # 2 - clicar e digitar quantidade
        pyautogui.click(667,553, duration = 0.5 )
        pyautogui.write(quantidade)
        # 3 - clica e registrar preço 
        pyautogui.click(671,583 ,duration = 0.5 )
        pyautogui.write(preco)
        # 4 - clicar em registrar 
        pyautogui.click(593,737 ,duration = 0.5)

sleep(1)