---
layout: default
title: "Build the Game"
parent: "2048"
nav_order: 1
---

# Project 0: 2048
{: .no_toc }

**Deadline: Monday, February 3rd, 11:59 PM PT.**

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview
Here we implement the core logic of the game 2048.

## 2048 Rules: Basic Rules
* **The Grid:** Played on a square grid. Each square is empty or contains a numbered tile.
* **Tilting:** The player tilts the board North, South, East, or West. All tiles slide until they hit an edge or another tile.
* **Merging:** When two tiles of the same value collide, they merge into one tile with double the value.
* **Ending:** The game ends when there are no available moves or a tile reaches the value 2048.

## Setup
### File Structure
The project is organized into two packages:
* **`game2048logic`**: Contains `GameLogic.java` (the only file you edit) and `MatrixUtils.java`.
* **`game2048rendering`**: Contains the GUI code (Board, Main, Side, Tile).

---

## Task 1: Understanding Tilts
![2048 Tilting Animation](/img/example-2048.gif)
The animation above shows a few tilt operations. Here are the full rules for when merges occur that are shown in the image above.
1. Two tiles of the same value merge into one tile with double the value.
2. **No Double Merges:** A tile that is the result of a merge will not merge again on that same tilt.
3. **Leading Merge:** If three adjacent tiles have the same value, the leading two tiles merge first.
4. **Double Pairs:** Four identical adjacent tiles will form two separate merged tiles (e.g., [4, 4, 4, 4] → [8, 8, X, X]).

## Task 2: Move Tile Up (No Merging)
In `GameLogic.java` Implement `moveTileUpAsFarAsPossible(int[][] board, int r, int c, int minR)`.
This method moves the tile at `(r, c)` as far North as possible. 

---

### Example 1
**Method call**: `moveTileUpAsFarAsPossible(board, r=3, c=0, minR=0)`

**Before**:
| | | | |
| :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |

**After**:
| | | | |
| :--- | :--- | :--- | :--- |
| 2 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

The tile at `(3, 0)` moves straight up to the top row `(0, 0)`.

---

### Example 2
**Method call**: `moveTileUpAsFarAsPossible(board, r=0, c=2, minR=0)`

**Before**:
| | | | |
| :--- | :--- | :--- | :--- |
| 0 | 0 | 4 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

**After**:
| | | | |
| :--- | :--- | :--- | :--- |
| 0 | 0 | 4 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

The tile at `(0, 2)` is already at the top row, so it does not move.

---

### Example 3
**Method call**: `moveTileUpAsFarAsPossible(board, r=3, c=0, minR=0)`

**Before**:
| | | | |
| :--- | :--- | :--- | :--- |
| 0 | 4 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 2 | 0 | 0 |
| 0 | 0 | 0 | 0 |

**After**:
| | | | |
| :--- | :--- | :--- | :--- |
| 0 | 4 | 0 | 0 |
| 0 | 2 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

The tile at `(2, 1)` moves up until it is just below the `4`, i.e. it lands at `(1, 1)`.

## Task 3: Merging Tiles
Modify `moveTileUpAsFarAsPossible` to handle merges. 
* **Return Value:** If a merge occurs, return $1 + row\_index$ of the merge. If no merge occurs, return $0$.

**Method call**: `moveTileUpAsFarAsPossible(board, r=3, c=0, minR=0)`

**Before**:
| | | | |
| :--- | :--- | :--- | :--- |
| 2 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |

**After**:
| | | | |
| :--- | :--- | :--- | :--- |
| 4 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

Tiles of the same value (2 and 2) merge into 4 at the top of the column. The method should return 1 because a merge occurred in row 0.

---

**Method call**: `moveTileUpAsFarAsPossible(board, r=3, c=0, minR=0)`

**Before**:
| | | | |
| :--- | :--- | :--- | :--- |
| 8 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

**After**:
| | | | |
| :--- | :--- | :--- | :--- |
| 8 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

The `8` at `(2, 0)` cannot merge with `(0, 0)` because there is a `4` in between. The method should return 0 because there was no merge.

## Task 4: Merging Tiles up to MinR
Update the method to respect the `minR` parameter. Tiles cannot move to or merge with a row higher than `minR`. This is helpful in task 5.

## Task 5: Tilt Column
With `moveTileUpAsFarAsPossible` fully implemented, use it to implement `tiltColumn(int[][] board, int x)`. 
* Tilt the entire column `x` upward.
* Use `moveTileUpAsFarAsPossible` as a helper. Update `minR` based on the return value to prevent illegal double merges.

## Task 6: Tilt Up
Implement `tiltUp(int[][] board)` to tilt the entire board up by calling `tiltColumn` for every column.

## Task 7: Tilt in Four Directions
Implement the general `tilt(int[][] board, Side side)` method. 
* Use the provided `rotateLeft` and `rotateRight` methods to rotate the board so that the "Tilt Up" logic can be reused for any direction.

---
*Content adapted from the [UC Berkeley CS 61B Spring 2025 Project 0 Specification](https://sp25.datastructur.es/projects/proj0/).*
