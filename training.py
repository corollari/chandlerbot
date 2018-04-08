from chatterbot import ChatBot
'''
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

'''


from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Chandler",
        read_only=True,
        input_adapter='chatterbot.input.TerminalAdapter',
        output_adapter='chatterbot.output.TerminalAdapter')
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "bot/chatterbot.json"
)

while True:
    try:
     bot_input = chatterbot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
