from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def inputs():
    prompts = story.prompts
    return render_template('inputs.html', prompts = prompts)

@app.route('/story')
def show_story():
    text = story.generate(request.args)
    return render_template('story.html', text = text)
    
