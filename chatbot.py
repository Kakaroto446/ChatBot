##########################################
##					##
##		JONI SCRIPTS		##
##		 APRESENTA		##
##					##
##########################################

# PROJETO:Samanta, uma amiga que nao existe
# VERSAO: V1.0
# AUTOR Joni:
# DATA: 12/12/2018

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import random;

bot = ChatBot('Samantha')

conversa = ['oi', 'ola', 'Como voce esta', 'estou bem', 'que bom', 'e voce como esta', 'estou bem kkk', 'ufa kkkkk', 'qual seu nome', 'Samanta, e o seu', 'o que gosta de fazer', 'conversar com voce', '']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
	pergunta = input('Usuario: ')

	resposta = bot.get_response(pergunta)

	if float(resposta.confidence) > 0.5:
		print('Samanta: ', resposta)
	else:
		respostas = ['ainda nao sei reponder isso', 'vai saber', 'quem sabe', 'vamo falar de outra coisa']
		print ('Samanta: %s' %(random.choice(respostas)))
