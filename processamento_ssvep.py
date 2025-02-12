import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy import signal
import matplotlib.pyplot as plt
import plotly.io as pio
from scipy import signal

#Criando dataframe e renomeando as colunas com o nome dos canais...
hz13 = pd.read_csv(r'dados\red13')
hz9 = pd.read_csv(r'dados\red9')
whz13 = pd.read_csv(r'dados\bran13')
whz9 = pd.read_csv(r'dados\bran9')
bl = pd.read_csv(r'dados\bl')

#Visualizando os dados de um canal
#fig = go.Figure()
#fig.add_trace(go.Scatter(x=hz13['Time:500Hz'], y=hz13['Channel 1'], name='FP1'))

#definindo a frequencia de amostragem
fz = 500

def espectro_9(data):
    #Aplicando filtro passa banda de ordem 2 de 8 a 45 Hz.
    b1, a1 = signal.butter(2, [8, 45], btype='bandpass', fs=fz)
    o1_filt = signal.filtfilt(b1, a1, data['Channel 11'])
    o2_filt = signal.filtfilt(b1, a1, data['Channel 12'])

    #Aplicando a transformada de Fourier para visualizar o sinal no dominio da frequência.
    f, p = signal.welch(o1_filt, fz, nperseg=fz*4, noverlap=fz*0.75)
    f2, p2 = signal.welch(o2_filt, fz, nperseg=fz*4, noverlap=fz*0.75)

    #Plotando para visulizar as frequências.
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=f, y=p, name='O1'))
    fig.add_trace(go.Scatter(x=f2, y=p2, name='O2'))

    valores_marcados = [9, 18, 27, 39]
    valores_marcadosb = [13, 26, 39]

    #Função para marcar os pontos de intersse no plot (9, 18, 27 e 39 Hz).
    for valor in valores_marcados:
      fig.add_trace(go.Scatter(x=[valor], y=[p2[valor*4]],
                                mode='markers',
                                name=f'{valor} Hz',
                                marker=dict(symbol='circle', color='green', size=8)))
    for valor in valores_marcados:
      fig.add_trace(go.Scatter(x=[valor], y=[p[valor*4]],
                                mode='markers',
                                marker=dict(symbol='circle', color='green', size=8)))

    #Adicionando legendas ao plot.
    fig.update_layout(
        title="Red light - 9 Hz",
        xaxis=dict(
            range=[0, 45],
            tickfont=dict(
                size=16,
                family="Arial, sans-serif",
                color="black"
            )
        ),
        yaxis=dict(
            tickfont=dict(
                size=16,
                family="Arial, sans-serif",
                color="black"
            )
        ),
        legend=dict(
            font=dict(
                size=18,
                family="Arial, sans-serif",
                color="black"
            )
        ),
        title_font=dict(
            size=24,
            family="Arial, sans-serif",
            color="black"
        )
    )

    fig.update_layout(
        autosize=False,
        width=800,
        height=500
    )

    fig.show()
#Mesma coisa que a função 'espectro9', só que adaptada para mostrar os pontos de intersse no plot (13, 26, 39 Hz).
def espectro(data):
    b1, a1 = signal.butter(2, [8, 45], btype='bandpass', fs=fz)
    o1_filt = signal.filtfilt(b1, a1, data['Channel 11'])
    o2_filt = signal.filtfilt(b1, a1, data['Channel 12'])
    f, p = signal.welch(o1_filt, fz, nperseg=fz*4, noverlap=fz*0.75)
    f2, p2 = signal.welch(o2_filt, fz, nperseg=fz*4, noverlap=fz*0.75)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=f, y=p, name='O1'))
    fig.add_trace(go.Scatter(x=f2, y=p2, name='O2'))

    valores_marcados = [9, 18, 27, 39]
    valores_marcadosb = [13, 26, 39]


    for valor in valores_marcadosb:
      fig.add_trace(go.Scatter(x=[valor], y=[p2[valor*4]],
                                mode='markers',
                                name=f'{valor} Hz',
                                marker=dict(symbol='circle', color='green', size=8)))

    for valor in valores_marcadosb:
      fig.add_trace(go.Scatter(x=[valor], y=[p[valor*4]],
                                mode='markers',
                                marker=dict(symbol='circle', color='green', size=8)))

    fig.update_layout(
        title="Red light - 13 Hz",
        xaxis=dict(
            range=[0, 45],
            tickfont=dict(
                size=16,
                family="Arial, sans-serif",
                color="black"
            )
        ),
        yaxis=dict(
            tickfont=dict(
                size=16,
                family="Arial, sans-serif",
                color="black"
            )
        ),
        legend=dict(
            font=dict(
                size=18,
                family="Arial, sans-serif",
                color="black"
            )
        ),
        title_font=dict(
            size=24,
            family="Arial, sans-serif",
            color="black"
        )
    )

    fig.update_layout(
        autosize=False,
        width=800,
        height=500
    )

    fig.show()

espectro(hz13)
espectro_9(hz9)
espectro(whz13)
espectro_9(whz9)