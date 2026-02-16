"""
2048 Flask Application

This is the main entry point for the 2048 web application.
It provides routes for:
- Rendering the game page
- Starting a new game
- Making moves

The file is named 'application.py' because AWS Elastic Beanstalk
looks for this filename by default.
"""

from flask import Flask, render_template, jsonify, session
from game import Game2048
import secrets

# Create Flask application
application = Flask(__name__)

# Secret key for session management
# In production, use a fixed secret key stored in environment variables
application.secret_key = secrets.token_hex(16)


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


@application.route('/')
def index():
    """
    Render the main game page.
    
    This loads the HTML template which contains the game grid,
    score display, and includes the CSS and JavaScript files.
    """
    game = get_game()
    save_game(game)
    return render_template('index.html', game_state=game.get_state())


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
        JSON response with the updated game state and whether
        the move was valid (tiles actually moved).
    """
    if direction not in ['up', 'down', 'left', 'right']:
        return jsonify({'error': 'Invalid direction'}), 400
    
    game = get_game()
    moved = game.move(direction)
    save_game(game)
    
    response = game.get_state()
    response['moved'] = moved
    return jsonify(response)


# This allows running the app directly with 'python application.py'
if __name__ == '__main__':
    # Debug mode for local development
    # Set debug=False for production
    application.run(debug=True, host='0.0.0.0', port=5000)
