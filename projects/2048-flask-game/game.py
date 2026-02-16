"""
2048 Game Logic Module

This module contains the core game logic for 2048.
The Game2048 class handles:
- Grid initialization and tile spawning
- Movement and tile merging
- Win/lose condition checking
"""

import random
import copy


class Game2048:
    """
    Represents a 2048 game instance.
    
    The game is played on a 4x4 grid where tiles can be moved
    in four directions. When two tiles with the same number collide,
    they merge into one tile with their sum.
    """
    
    def __init__(self):
        """Initialize a new game with an empty grid and spawn two starting tiles."""
        self.size = 4
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.game_over = False
        self.won = False
        
        # Spawn two starting tiles
        self.spawn_tile()
        self.spawn_tile()
    
    def spawn_tile(self):
        """
        Add a new tile (2 or 4) to a random empty cell.
        
        There's a 90% chance of spawning a 2 and 10% chance of spawning a 4.
        Returns True if a tile was spawned, False if the grid is full.
        """
        empty_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    empty_cells.append((row, col))
        
        if not empty_cells:
            return False
        
        row, col = random.choice(empty_cells)
        # 90% chance of 2, 10% chance of 4
        self.grid[row][col] = 2 if random.random() < 0.9 else 4
        return True
    
    def move(self, direction):
        """
        Move all tiles in the specified direction.
        
        Args:
            direction: One of 'up', 'down', 'left', 'right'
        
        Returns:
            True if any tiles moved, False otherwise
        """
        if self.game_over:
            return False
        
        # Save the current grid to check if anything changed
        old_grid = copy.deepcopy(self.grid)
        
        if direction == 'up':
            self._move_up()
        elif direction == 'down':
            self._move_down()
        elif direction == 'left':
            self._move_left()
        elif direction == 'right':
            self._move_right()
        else:
            return False
        
        # Check if the grid changed
        moved = self.grid != old_grid
        
        if moved:
            self.spawn_tile()
            self._check_game_state()
        
        return moved
    
    def _slide_and_merge_row(self, row):
        """
        Slide tiles to the left and merge matching tiles.
        
        This is the core merge logic. Other directions use this
        by rotating/transforming the grid.
        
        Args:
            row: A list of 4 tile values
        
        Returns:
            A new list with tiles slid left and merged
        """
        # Remove zeros (empty cells)
        non_zero = [val for val in row if val != 0]
        
        # Merge adjacent equal tiles
        merged = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                # Merge tiles
                merged_value = non_zero[i] * 2
                merged.append(merged_value)
                self.score += merged_value
                
                # Check for win condition
                if merged_value == 2048:
                    self.won = True
                
                skip = True  # Skip the next tile (it was merged)
            else:
                merged.append(non_zero[i])
        
        # Pad with zeros to maintain grid size
        merged.extend([0] * (self.size - len(merged)))
        return merged
    
    def _move_left(self):
        """Move all tiles to the left."""
        for row in range(self.size):
            self.grid[row] = self._slide_and_merge_row(self.grid[row])
    
    def _move_right(self):
        """Move all tiles to the right (reverse, slide left, reverse)."""
        for row in range(self.size):
            self.grid[row] = self._slide_and_merge_row(self.grid[row][::-1])[::-1]
    
    def _move_up(self):
        """Move all tiles up (transpose, slide left, transpose back)."""
        self._transpose()
        self._move_left()
        self._transpose()
    
    def _move_down(self):
        """Move all tiles down (transpose, slide right, transpose back)."""
        self._transpose()
        self._move_right()
        self._transpose()
    
    def _transpose(self):
        """Transpose the grid (swap rows and columns)."""
        self.grid = [list(row) for row in zip(*self.grid)]
    
    def _check_game_state(self):
        """Check if the game is over (no valid moves remaining)."""
        # Check for empty cells
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    return  # Game continues - there's an empty cell
        
        # Check for possible merges (adjacent equal tiles)
        for row in range(self.size):
            for col in range(self.size):
                current = self.grid[row][col]
                # Check right neighbor
                if col + 1 < self.size and self.grid[row][col + 1] == current:
                    return  # Game continues - there's a possible merge
                # Check bottom neighbor
                if row + 1 < self.size and self.grid[row + 1][col] == current:
                    return  # Game continues - there's a possible merge
        
        # No empty cells and no possible merges
        self.game_over = True
    
    def get_state(self):
        """
        Get the current game state as a dictionary.
        
        This is used to send the game state to the frontend as JSON.
        
        Returns:
            dict with grid, score, game_over, and won status
        """
        return {
            'grid': self.grid,
            'score': self.score,
            'game_over': self.game_over,
            'won': self.won
        }
