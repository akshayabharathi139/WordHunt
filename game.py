from flask import Flask, render_template, request, jsonify, session
import random
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "wordgame_secret"
CORS(app)

# Sample word list
words_list = ["game", "code", "plan", "mark", "love", "ship", "dare", "fire", "tone", "clap", "bark", "node", "lamp","vibe","dust","mild","rush","chat","perk","gold","mind","snow","jump","pack","bold","wish","jynx","flew","grad"," drag",
"moth",
"buck",
"zips"]

@app.route('/')
def index():
    # Start new game with a random word
    system_word = random.choice(words_list)
    session['system_word'] = system_word
    session['attempts'] = 0
    return render_template('index.html')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    player_word = request.json['guess'].lower()
    system_word = session.get('system_word')
    session['attempts'] += 1

    if len(player_word) != 4 or len(set(player_word)) != 4:
        return jsonify({"error": "Enter a 4-letter word with unique letters."})

    correct_position = sum([1 for i in range(4) if player_word[i] == system_word[i]])
    matched_letters = sum([1 for ch in player_word if ch in system_word])

    if player_word == system_word:
        return jsonify({"success": True, "attempts": session['attempts'], "word": system_word})

    return jsonify({
        "matched": matched_letters,
        "correct_position": correct_position,
        "success": False
    })

if __name__ == '__main__':
    app.run(debug=True)
