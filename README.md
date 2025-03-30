✍️ Disappearing Text Writing App

 🌟 Overview
A Flask-based web application that challenges writers to keep typing or lose their work. Features a prompt generator and a writing interface that resets after 5 seconds of inactivity.

 🚀 Features
- **Random Writing Prompts**: Generates creative prompts from a database
- **Writing Challenge**: Text disappears after 5 seconds of inactivity
- **Simple Interface**: Clean, distraction-free writing environment
- **Timer Display**: Shows elapsed writing time
- **Responsive Design**: Works on desktop and mobile devices

 🛠️ Technologies Used
- **Python** (Flask backend)
- **SQLite** (Prompt database)
- **HTML5** & **CSS3** (Frontend)
- **JavaScript** (Timer functionality)

 ⚙️ Setup Instructions

 Prerequisites
- Python 3.8+
- Flask
- Flask-SQLAlchemy

 Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/disappearing-text.git
cd disappearing-text
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask flask-sqlalchemy
```

4. Initialize the database:
```bash
python init_db.py  # Create this file to add sample prompts
```

 Running the Application
```bash
python app.py
```
Then open `http://localhost:5000` in your browser.

 📂 Project Structure
```
disappearing-text/
├── app.py                # Main Flask application
├── static/
│   └── styles.css        # CSS styles
├── templates/
│   ├── index.html        # Prompt generator
│   └── writing.html      # Writing interface
└── prompts.db            # SQLite database
```

 🎮 How to Use
1. Generate a random writing prompt
2. Click "Start writing" to begin
3. Keep typing continuously
4. If you stop for more than 5 seconds, your text resets to the original prompt

 📝 Adding Prompts
To add more writing prompts to the database:
```python
from app import db, Prompt

new_prompt = Prompt(text="Your new writing prompt here")
db.session.add(new_prompt)
db.session.commit()
```

**Happy writing!** Keep those fingers moving or watch your words disappear!
