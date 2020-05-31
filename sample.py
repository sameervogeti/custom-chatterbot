from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
app=Flask(__name__)

sample_bot=ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=[
        {
            'import_path': 'cool_adapter.MyLogicAdapter'
        }
    ])
trainer=ChatterBotCorpusTrainer(sample_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText=request.args.get("msg")
    return str(sample_bot.get_response(userText))
if __name__=='__main__':
    app.run(debug=True)