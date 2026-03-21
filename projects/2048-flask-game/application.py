"""
2048 Flask Application

This is the main entry point for the 2048 web application.
It provides routes for:
- Rendering the game page
- Starting a new game
- Making moves
- Leaderboard (submit score, view top 10)

The file is named 'application.py' because AWS Elastic Beanstalk
looks for this filename by default.
"""

from flask import Flask, render_template, jsonify, session, request
from flask_sqlalchemy import SQLAlchemy
from game import Game2048
import secrets

# Create Flask application
application = Flask(__name__)

# Secret key for session management
# In production, use a fixed secret key stored in environment variables
application.secret_key = secrets.token_hex(16)

# Database — SQLite file stored next to application.py
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)


# ---------------------------------------------------------------------------
# Leaderboard model
# ---------------------------------------------------------------------------
class Score(db.Model):
    id      = db.Column(db.Integer,   primary_key=True)
    name    = db.Column(db.String(50), nullable=False)
    score   = db.Column(db.Integer,   nullable=False)
    highest = db.Column(db.Integer,   default=0)
    created = db.Column(db.DateTime,  server_default=db.func.now())


# Create tables on first run (creates leaderboard.db if it doesn't exist)
with application.app_context():
    db.create_all()


# ---------------------------------------------------------------------------
# Game session helpers
# ---------------------------------------------------------------------------
def get_game():
    """
    Get the current game from the session, or create a new one.

    We store the game state in the Flask session so each user
    has their own game instance.
    """
    if 'game_state' not in session:
        game = Game2048()
        session['game_state'] = game.get_state()
        return game

    # Reconstruct game from session state
    game = Game2048.__new__(Game2048)
    game.size = 4
    game.grid = session['game_state']['grid']
    game.score = session['game_state']['score']
    game.game_over = session['game_state']['game_over']
    game.won = session['game_state']['won']
    return game


def save_game(game):
    """Save the current game state to the session."""
    session['game_state'] = game.get_state()
    session.modified = True


# ---------------------------------------------------------------------------
# Game routes
# ---------------------------------------------------------------------------
@application.route('/')
def index():
    """
    Render the main game page.

    This loads the HTML template which contains the game grid,
    score display, and includes the CSS and JavaScript files.
    """
    game = get_game()
    save_game(game)
    top = Score.query.order_by(Score.score.desc()).limit(10).all()
    return render_template('index.html', game_state=game.get_state(), scores=top)


@application.route('/new', methods=['POST'])
def new_game():
    """
    Start a new game.

    This resets the grid, score, and spawns two new starting tiles.
    Returns the new game state as JSON.
    """
    game = Game2048()
    save_game(game)
    return jsonify(game.get_state())


@application.route('/move/<direction>', methods=['POST'])
def move(direction):
    """
    Make a move in the specified direction.

    Args:
        direction: One of 'up', 'down', 'left', 'right' (from URL)

    Returns:
        JSON with updated game state, moved flag, and lists of
        merged_cells / new_cells (flat indices) for animations.
    """
    if direction not in ['up', 'down', 'left', 'right']:
        return jsonify({'error': 'Invalid direction'}), 400

    game = get_game()

    # Snapshot the grid BEFORE the move so we can diff it for animations
    old_grid = [row[:] for row in game.grid]

    moved = game.move(direction)
    save_game(game)

    # Identify which cells merged and which cell is newly spawned
    merged_cells = []
    new_cells = []
    for r in range(4):
        for c in range(4):
            old_val = old_grid[r][c]
            new_val = game.grid[r][c]
            idx = r * 4 + c
            if new_val != 0 and old_val == 0:
                new_cells.append(idx)           # freshly spawned tile
            elif new_val > old_val and old_val != 0:
                merged_cells.append(idx)        # tile doubled (merged)

    response = game.get_state()
    response['moved'] = moved
    response['merged_cells'] = merged_cells
    response['new_cells'] = new_cells
    return jsonify(response)


# ---------------------------------------------------------------------------
# Leaderboard routes
# ---------------------------------------------------------------------------
@application.route('/submit-score', methods=['POST'])
def submit_score():
    """Save a player's final score to the leaderboard."""
    data = request.get_json()
    entry = Score(
        name    = (data.get('name') or 'Anonymous')[:50],
        score   = int(data.get('score', 0)),
        highest = int(data.get('highest', 0))
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify({'ok': True})


@application.route('/leaderboard')
def leaderboard():
    """Render the top-10 leaderboard page."""
    top = Score.query.order_by(Score.score.desc()).limit(10).all()
    return render_template('leaderboard.html', scores=top)


@application.route('/api/leaderboard')
def api_leaderboard():
    """Return top-10 scores as JSON (used by the inline leaderboard refresh)."""
    top = Score.query.order_by(Score.score.desc()).limit(10).all()
    return jsonify([
        {'name': s.name, 'score': s.score, 'highest': s.highest}
        for s in top
    ])


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Debug mode for local development — set debug=False for production
    application.run(debug=True, host='0.0.0.0', port=5000)
