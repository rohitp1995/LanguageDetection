import flask
from model import languagePrediction

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))
    if flask.request.method == 'POST':
        user_sentence= flask.request.form['Sentence']
        language_pred = languagePrediction(user_sentence)
        return (flask.render_template('index.html',predicted_language=language_pred[0]))
        
    
if __name__=='__main__':
    app.run()       