# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
import numpy as np

# Para calcular a trajetoria e' necessario uma politica

def Q2pol(Q, eta=5):
	pol = np.zeros(Q.shape)

	for line,values in enumerate(Q):
		idx = np.argmax(values)
		pol[line, idx] = 1

	return pol


# Para isso implementar o algoritmo Q-learning que a partir de uma trajetoria
# recebida calcule os valores Q para cada
# gamma = discount factor 0 < gamma < 1
# alpha = learning rate   0 < alpha < 1
class myRL:

	def __init__(self, nS, nA, gamma):
		self.nS = nS  # numero de linhas - numero de estados
		self.nA = nA  # numero de colunas - numero de accoes
		self.gamma = gamma
		self.Q = np.zeros((nS,nA))

	# Calcular os valores de Q para cada accao
	# Trace e' uma matriz
	def traces2Q(self, trace):
		self.Q = np.zeros((self.nS, self.nA))
		tempQ  = np.zeros((self.nS, self.nA))

		alpha = 0.1
		#Vai convergir para um numero
		while True:
			for ele in trace:
				state  = int(ele[0])
				action = int(ele[1])
				next_state = int(ele[2])
				reward = ele[3]

				tempQ[state, action] += alpha * (reward + self.gamma * max(tempQ[next_state, :]) - tempQ[state, action])

			err = np.linalg.norm(self.Q-tempQ)
			self.Q = np.copy(tempQ)
			if err<1e-2:
				break

		return self.Q