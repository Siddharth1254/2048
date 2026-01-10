---
layout: default
title: "Project 0: 2048"
nav_order: 2
---

# Project 0: 2048
{: .no_toc }

[cite_start]**Deadline: Monday, February 3rd, 11:59 PM PT.** [cite: 6]

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Hard Mode Project
[cite_start]If you are a strong programmer, you might be interested in the hard mode version of this project[cite: 7, 8]. [cite_start]In the hard mode version, you'll solve the same problem as the standard version of this project, but there will be no handholding and you'll have to come up with the design yourself[cite: 9]. [cite_start]There is no extra credit for completing the hard mode version instead of the standard version[cite: 10].

## FAQ
[cite_start]Each assignment will have an FAQ linked at the top[cite: 12]. [cite_start]You can also access it by adding `/faq` to the end of the URL[cite: 13]. [cite_start]The FAQ for Project 0 is located here[cite: 14]. 

> Note that this project has limited submission tokens. [cite_start]Please see Submission and Grading for more details[cite: 15].

## Overview
[cite_start]In this mini-project, you'll get some practice with Java by creating a playable game of 2048[cite: 24]. [cite_start]We've already implemented the graphics and user interaction code for you, so your job is to implement the logic of the game[cite: 24]. [cite_start]We've set everything up so that you don't need to open any of the files except for `GameLogic.java`, though you're welcome to browse[cite: 33].

### Using Git
[cite_start]It is important that you commit work to your repository at frequent intervals[cite: 35]. [cite_start]The command `git status` will tell you what files you have modified, removed, or possibly added since the last commit[cite: 38].

| Command | Description |
| :--- | :--- |
| `git status` | [cite_start]To see what needs to be added or committed. |
| `git add <file or folder path>` | [cite_start]To add, or stage, any modified files. |
| `git commit -m "Commit message"` | To commit changes. [cite_start]Use a descriptive message. |
| `git push origin main` | [cite_start]Reflect your local changes on GitHub so Gradescope can see them. |

## 2048 Rules: Basic Rules
* [cite_start]2048 is played on a grid of squares[cite: 46].
* [cite_start]The player chooses a direction (using the arrow keys) to tilt the board: north, south, east, or west[cite: 51].
* [cite_start]All tiles slide in that direction until there is no empty space left[cite: 52].
* [cite_start]As a tile slides, it can possibly merge with another tile with the same number[cite: 53].
* [cite_start]After each tilt, a single randomly generated tile (value 2 or 4) will be added to the board on an empty square[cite: 57, 58].
* [cite_start]The game ends when the player has no available moves or forms a square containing 2048[cite: 61].

## Setup
### File Structure
[cite_start]The `proj0` folder is separated into two packages, `game2048logic` and `game2048rendering`[cite: 74].


* [cite_start]**`game2048logic`**: Contains logic files like `GameLogic.java` and `MatrixUtils.java`[cite: 83, 84, 86].
* [cite_start]**`game2048rendering`**: Contains rendering files like `Board.java`, `Main.java`, `Side.java`, and `Tile.java`[cite: 87, 88, 90, 91, 92].

> [cite_start]**INFO**: You will only need to read and modify the `game2048logic/GameLogic.java` file[cite: 94]. [cite_start]Changes to other files will not be recognized by Gradescope[cite: 95].

### Running the Game
[cite_start]You can run your game by running the `Main.java` file in the `game2048rendering` package[cite: 98]. [cite_start]Right-click the file and select **"Run 'Main.main()'"**[cite: 99].

---

## Task 1: Understanding Tilts
Before implementing, understand the merging rules:
1. [cite_start]Two tiles of the same value merge into one tile containing double the initial number[cite: 152].
2. [cite_start]A tile that is the result of a merge will not merge again on that tilt[cite: 153].
3. [cite_start]When three adjacent tiles of the same number move, the leading two tiles merge, and the trailing tile does not[cite: 156].
4. [cite_start]Four adjacent tiles with the same number form two merged tiles (e.g., [4, 4, 4, 4] becomes [8, 8, X, X])[cite: 161, 162].

## Task 2: Move Tile Up (No Merging)
[cite_start]Implement `moveTileUpAsFarAsPossible(int[][] board, int r, int c, int minR)`[cite: 190].
* [cite_start]Move the tile at `(r, c)` as far up as possible[cite: 192].
* [cite_start]Ignore the `minR` parameter and merges for this task[cite: 193, 195].

## Task 3: Merging Tiles
[cite_start]Modify `moveTileUpAsFarAsPossible` to handle merges[cite: 433].
* [cite_start]If a merge occurs, return $1 + row\_number$ where the merge happened[cite: 436].
* [cite_start]If no merge occurs, return $0$[cite: 437].

## Task 4: Merging Tiles up to MinR
[cite_start]Modify `moveTileUpAsFarAsPossible` so that the tile is not allowed to move any higher than the row given by `minR`[cite: 482].

## Task 5: Tilt Column
[cite_start]Implement `tiltColumn(int[][] board, int x)` to tilt an entire column upwards[cite: 526, 527].
* [cite_start]Use `moveTileUpAsFarAsPossible` as a helper method[cite: 529].
* [cite_start]Use the return value of the helper to update `minR` and avoid double merges[cite: 531].

## Task 6: Tilt Up
[cite_start]Implement `tiltUp(int[][] board)` to tilt the entire board north[cite: 580, 581]. [cite_start]This calls `tiltColumn` for every column on the board[cite: 178].

## Task 7: Tilt in Four Directions
[cite_start]Implement the general `tilt(int[][] board, Side side)` method[cite: 597].
* [cite_start]Instead of writing four separate move functions, use the provided `rotateLeft` and `rotateRight` methods to rotate the board, tilt it up, and rotate it back[cite: 589, 596].

---

## Testing
* [cite_start]**Unit Tests**: Run `TestTask2.java`, `TestTask3.java`, etc., to test functions in isolation[cite: 234, 479, 602].
* [cite_start]**Integration Tests**: Run `TestIntegration.java` to test how different functions interact[cite: 600, 602].

## Style
[cite_start]You must follow the CS 61B Style Guide[cite: 608]. [cite_start]You can check your style locally with the provided plugin[cite: 609].

## Submission and Grading
### Velocity Limiting
{: .warning }
[cite_start]For this project, we will be limiting submissions to the autograder[cite: 616]. [cite_start]You will get **4 submission "tokens"** that each regenerate after **24 hours**[cite: 617].

### Grading Breakdown
| Category | Weight |
| :--- | :--- |
| TestTask2 | [cite_start]15% [cite: 628] |
| TestTask3 | [cite_start]20% [cite: 629] |
| TestTask4 | [cite_start]20% [cite: 630] |
| TestTask5 | [cite_start]8% [cite: 631] |
| TestTask6 | [cite_start]4% [cite: 632] |
| TestTask7 | [cite_start]8% [cite: 633] |
| TestIntegration | [cite_start]25% [cite: 634] |

[cite_start]There are no hidden tests; the score you see on Gradescope is your final score[cite: 637].
