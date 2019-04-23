from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

import os
bot = ChatBot('Friend') #create the bot
trainer = ChatterBotCorpusTrainer(bot)
#bot.train(conv) # teacher train the bot
corpus_path='D:/Sunil/sunil_conda/t81_558_deep_learning-master/t81_558_deep_learning-master/ChatBot/chatterbot-corpus-master/chatterbot_corpus/data/english/'


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
		
@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']
	bot_response=bot.get_response(user_input)
	bot_response=str(bot_response)
	print("Friend: "+bot_response)
	return render_template('index.html',user_input=user_input,
		bot_response=bot_response
		)
		
		
if __name__ == '__main__':
    app.run(debug=True)