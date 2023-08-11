from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtenstion
from stories import stories 

app = Flask(__name__)
app.config['SECRET_KEY'] = "cosmowanda"

debug = DebugToolbarExtenstion(app)

@app.route("/")
def ask_story():
    """Show me list-of-stories form."""

    return render_template("select-story.hmtl", stories=stories.value())

@app.route("/questions")
def ask_questions():
    """Generate and Show form to ask words"""

    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("questions.html", story_id=story_id, title=story.title, prompts=prompts)

@app.rout("/story")
def show_story():
    """Shows yours story"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)
    return render_template("story.hmtl",title=story.title,text=text)