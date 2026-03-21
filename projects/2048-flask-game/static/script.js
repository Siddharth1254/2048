/**
 * 2048 Game JavaScript
 * 
 * Handles keyboard input and communicates with the Flask backend
 * via AJAX calls to update the game state without page reloads.
 */

document.addEventListener('DOMContentLoaded', function () {
    // Track if we've already shown the win screen this game
    let winShown = false;

    /**
     * Send a move request to the server and update the UI
     * @param {string} direction - 'up', 'down', 'left', or 'right'
     */
    async function makeMove(direction) {
        try {
            const response = await fetch(`/move/${direction}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                console.error('Move request failed');
                return;
            }

            const gameState = await response.json();
            updateUI(gameState);
        } catch (error) {
            console.error('Error making move:', error);
        }
    }

    /**
     * Start a new game
     */
    async function newGame() {
        try {
            const response = await fetch('/new', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                console.error('New game request failed');
                return;
            }

            const gameState = await response.json();
            winShown = false;  // Reset win tracking for new game
            updateUI(gameState);
        } catch (error) {
            console.error('Error starting new game:', error);
        }
    }

    /**
     * Update the game UI based on the current game state
     * @param {Object} gameState - The game state from the server
     */
    function updateUI(gameState) {
        // Update score
        document.getElementById('score').textContent = gameState.score;

        // Update grid
        const grid = document.getElementById('grid');
        grid.innerHTML = '';

        for (let row = 0; row < gameState.grid.length; row++) {
            for (let col = 0; col < gameState.grid[row].length; col++) {
                const value = gameState.grid[row][col];
                const cell = document.createElement('div');
                cell.className = `cell cell-${value}`;
                if (value !== 0) {
                    cell.textContent = value;
                }
                grid.appendChild(cell);
            }
        }

        // Update game over overlay
        const gameOverOverlay = document.getElementById('game-over');
        if (gameState.game_over) {
            gameOverOverlay.classList.remove('hidden');
            document.getElementById('final-score').textContent = gameState.score;
        } else {
            gameOverOverlay.classList.add('hidden');
        }

        // Update win overlay (only show once per game)
        const winOverlay = document.getElementById('win');
        if (gameState.won && !winShown) {
            winOverlay.classList.remove('hidden');
            winShown = true;
        }
    }

    /**
     * Handle keyboard events for arrow keys
     */
    document.addEventListener('keydown', function (event) {
        const keyDirections = {
            'ArrowUp': 'up',
            'ArrowDown': 'down',
            'ArrowLeft': 'left',
            'ArrowRight': 'right'
        };

        if (keyDirections[event.key]) {
            event.preventDefault();  // Prevent page scrolling
            makeMove(keyDirections[event.key]);
        }
    });

    // New Game button click handler
    document.getElementById('new-game-btn').addEventListener('click', newGame);

    // Try Again button (on game over screen)
    document.getElementById('try-again-btn').addEventListener('click', newGame);

    // Keep Playing button (on win screen)
    document.getElementById('keep-playing-btn').addEventListener('click', function () {
        document.getElementById('win').classList.add('hidden');
    });

    // New Game button on win screen
    document.getElementById('new-game-after-win-btn').addEventListener('click', newGame);

    // =========================================================
    // Dark Mode Toggle
    // =========================================================
    const darkBtn = document.getElementById('dark-mode-btn');

    // Restore saved preference on load
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        darkBtn.textContent = '☀️';
    }

    darkBtn.addEventListener('click', function () {
        const isDark = document.body.classList.toggle('dark-mode');
        this.textContent = isDark ? '☀️' : '🌙';
        localStorage.setItem('darkMode', isDark);
    });

    // =========================================================
    // Mobile Swipe Gestures
    // =========================================================
    let touchStartX = null;
    let touchStartY = null;
    const MIN_SWIPE_PX = 30; // minimum distance to register as a swipe

    document.addEventListener('touchstart', function (e) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
    }, { passive: true });

    document.addEventListener('touchend', function (e) {
        if (touchStartX === null || touchStartY === null) return;

        const dx = e.changedTouches[0].clientX - touchStartX;
        const dy = e.changedTouches[0].clientY - touchStartY;

        touchStartX = null;
        touchStartY = null;

        // Ignore taps (movement too small)
        if (Math.abs(dx) < MIN_SWIPE_PX && Math.abs(dy) < MIN_SWIPE_PX) return;

        // Determine dominant direction
        if (Math.abs(dx) > Math.abs(dy)) {
            makeMove(dx > 0 ? 'right' : 'left');
        } else {
            makeMove(dy > 0 ? 'down' : 'up');
        }
    }, { passive: true });
});
