from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompts.db'
db = SQLAlchemy(app)


# Define a model for prompts
class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)


# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def generate_prompt():
    global prompt_text
    random_prompt = Prompt.query.order_by(func.random()).first()  # For SQLite
    prompt_text = random_prompt.text if random_prompt else None
    return render_template('index.html', prompt=prompt_text)
@app.route('/writing', methods=['GET', 'POST'])
def writing():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elapsed_time = 0
    last_input_time = None
    prompt = prompt_text
    if request.method == 'POST':
        last_input_time = request.form.get('last_input_time')
        if last_input_time:
            elapsed_time = (datetime.now() - datetime.strptime(last_input_time, "%Y-%m-%d %H:%M:%S")).seconds
    return render_template('writing.html', prompt=prompt, elapsed_time=elapsed_time, current_time=current_time,last_input_time=last_input_time)



if __name__ == '__main__':
    app.run(debug=True)