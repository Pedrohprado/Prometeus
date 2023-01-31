from serialToExcel import serialToExcel

# Library para o tratamento de dados e plotagem dos gráficos
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import seaborn as sns

# Library para automação e alocação do database dentro do servidor
import pyautogui
import time

serialToExcel = serialToExcel("COM3", 9600)


serialToExcel.setRecordsNumber(30)
serialToExcel.readPort()

nomeColaborador = input('Qual o nome do colaborador?')
card = input('Qual o cartão do colaborador?')

serialToExcel.writeFile(f"Ateste_{nomeColaborador}_{card}.xls")
data = f"Ateste_{nomeColaborador}_{card}.xls"

# Salvando código no servidor necessário
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')
time.sleep(2)
pyautogui.keyDown('winleft')
pyautogui.keyUp('winleft')
time.sleep(1)
pyautogui.write('Meu computador')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(2)
pyautogui.keyDown('D')
pyautogui.keyUp('D')
pyautogui.keyDown('D')
pyautogui.keyUp('D')
pyautogui.keyDown('D')
pyautogui.keyUp('D')
time.sleep(2)
pyautogui.press(['enter'])
pyautogui.keyDown('U')
pyautogui.keyUp('U')
time.sleep(1)
pyautogui.press(['enter'])
pyautogui.keyDown('P')
pyautogui.keyUp('P')
time.sleep(1)
pyautogui.press(['enter'])
pyautogui.keyDown('P')
pyautogui.keyUp('P')
pyautogui.keyDown('P')
pyautogui.keyUp('P')
time.sleep(1)
pyautogui.press(['enter'])
pyautogui.keyDown('P')
pyautogui.keyUp('P')
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.keyDown('A')
pyautogui.keyUp('A')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
time.sleep(1)
pyautogui.keyDown('winleft')
pyautogui.keyUp('winleft')
time.sleep(1)
pyautogui.write('Meu computador')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(2)
pyautogui.keyDown('P')
pyautogui.keyUp('P')
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')

time.sleep(1)
pyautogui.press(['enter'])


# TRATAMENTO DE DADOS E PLOTAGEM DE GRÁFICOS

# Criando um dataframe para começar o tratamento de dados
df = pd.read_excel(data)

# Limpeza de informações e tratamento de dados
df = df.drop([0, 1, 2, 3])
df.columns = ['Data', 'Amperagem', 'Situação']

df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%H:%M:%S')
df['Amperagem'] = df['Amperagem'].astype(float)

# Criando variaveis para plotagem de gráficos
dflimpo = df.loc[df['Amperagem'] < 600]
dfy = dflimpo
dflimpo = dflimpo.reset_index()

situcao = (df['Situação'].value_counts())

# df.plot(title='Oscilação da Corrente')
# plt.show()


# PRECISO INSERIR O CONTEÚDO DO TRATAMENTO DE DADOS E QUAL A UTILIZAÇÃO DA AMPERAGEM
# Testar essa nova função


amp = float(input('Qual a amperagem utilizada?'))

porc = amp * 0.10
linhamax = amp + porc
linhamin = amp - porc

dfy.plot(figsize=(40, 8), color='gray')
# Plotando gráficos de linha
plt.axhline(linhamax, 0, 1, color='r', **{'lw': 1})
plt.axhline(linhamin, 0, 1, color='r', **{'lw': 1})
plt.show()

sns.set_style('darkgrid')  # Plotando gráficos de disperção
sns.relplot(data=dflimpo, x='index', y='Amperagem',
            aspect=3, height=7, hue='Amperagem')

plt.title('Variação da Corrente no Processo de Soldagem')
plt.xlabel('Tempo em segundos')

plt.axhline(linhamax, 0, 1, color='r', **{'lw': 1})
plt.axhline(linhamin, 0, 1, color='r', **{'lw': 1})
plt.show()

situcao.plot(kind='barh', title='Ciclo de Serviço')
plt.show()
