---
title: "Chess"
area: arts-recreation
type: rulebook
source: Observatory Almanac
source_path: docs/02-universal-rulebook/chess.md
license: MIT
updated: 2026-04-28
summary: >
  The Royal Game · 2 players · Ages 6+ · 30 min–∞
tags:
  - games
  - strategy
  - play
---

# Chess

**The Royal Game** · 2 players · Ages 6+ · 30 min–∞

Chess is the most studied abstract strategy game in history. Two armies—White and Black—contest control of a 64-square board. The object is checkmate: placing the enemy king in inescapable attack.

---

## The Board

An 8×8 grid of alternating light and dark squares. Always set up with a light square in each player's bottom-right corner ("light on right").

```
  a  b  c  d  e  f  g  h
8 ♜  ♞  ♝  ♛  ♚  ♝  ♞  ♜  8
7 ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  7
6 .  .  .  .  .  .  .  .  6
5 .  .  .  .  .  .  .  .  5
4 .  .  .  .  .  .  .  .  4
3 .  .  .  .  .  .  .  .  3
2 ♙  ♙  ♙  ♙  ♙  ♙  ♙  ♙  2
1 ♖  ♘  ♗  ♕  ♔  ♗  ♘  ♖  1
  a  b  c  d  e  f  g  h
```

**Starting positions:**
- Rooks on corners (a1, h1 for White; a8, h8 for Black)
- Knights next to rooks
- Bishops next to knights
- Queen on her own color (White queen on d1, a light square; Black queen on d8, a dark square)
- King on the remaining center square
- Pawns fill the second rank for each side

---

## Piece Movements

### King
Moves exactly one square in any direction (orthogonal or diagonal). The king may never move into check. The king may capture an enemy piece on an adjacent square unless doing so would put it in check.

### Queen
Moves any number of squares in any direction (orthogonal or diagonal), provided no piece blocks the path. The most powerful piece on the board.

### Rook
Moves any number of squares orthogonally (horizontally or vertically). Blocked by intervening pieces. Participates in castling.

### Bishop
Moves any number of squares diagonally. Always remains on the same color square. Each side starts with one light-squared and one dark-squared bishop.

### Knight
Moves in an L-shape: two squares in one orthogonal direction then one square perpendicular (or vice versa). The knight is the only piece that can leap over other pieces. From the center, a knight can reach up to 8 squares.

```
  . N . N .
  N . . . N
  . . ♘ . .
  N . . . N
  . N . N .
```

### Pawn
- Moves forward one square (cannot move backward).
- On its very first move, may advance two squares forward (if both squares are unoccupied).
- Captures diagonally one square forward.
- Cannot capture straight ahead.

---

## Special Moves

### Castling
The king and one rook move simultaneously. This is the only move in which two pieces move at once.

**Conditions for castling:**
1. Neither the king nor the chosen rook has previously moved.
2. No pieces stand between the king and rook.
3. The king is not currently in check.
4. The king does not pass through a square that is under attack.
5. The king does not land on a square that is under attack.

**Kingside castling (O-O):** The king moves from e1 to g1 (White) or e8 to g8 (Black); the rook moves from h-file to f-file.

**Queenside castling (O-O-O):** The king moves from e1 to c1 (White) or e8 to c8 (Black); the rook moves from a-file to d-file.

Note: The rook may pass through an attacked square during queenside castling, as only the king's path matters.

### En Passant
When a pawn advances two squares from its starting position and lands beside an enemy pawn, the enemy pawn may capture it as if it had moved only one square. This capture must be made immediately on the very next move; the right expires if not taken.

**Example:** White pawn on e5. Black plays d7-d5. White may capture the Black pawn by moving the White pawn to d6 and removing the Black pawn from d5.

### Pawn Promotion
When a pawn reaches the opponent's back rank (rank 8 for White, rank 1 for Black), it must immediately be promoted. The pawn is replaced by a queen, rook, bishop, or knight of the same color. Promotion to queen is almost always optimal. Promoting to a different piece is called underpromotion and occasionally has tactical purpose.

---

## Check, Checkmate, and Stalemate

**Check:** The king is under immediate attack by one or more enemy pieces. When in check, the player must resolve it by:
1. Moving the king to a safe square.
2. Blocking the attacking piece (if it attacks from range).
3. Capturing the attacking piece.

A player may not make a move that leaves their own king in check.

**Checkmate:** The king is in check and there is no legal move to escape. The game ends; the checkmated player loses.

**Stalemate:** It is a player's turn to move, they are not in check, but they have no legal moves. The game ends immediately as a draw regardless of material imbalance.

---

## Draw Conditions

1. **Stalemate** — as described above.
2. **Insufficient material** — neither side has enough pieces to force checkmate (e.g., king vs. king; king and bishop vs. king; king and knight vs. king).
3. **Threefold repetition** — the same position occurs three times with the same player to move and the same rights (castling and en passant). Either player may claim the draw.
4. **Fifty-move rule** — 50 consecutive moves (by both players) have been made with no pawn move and no capture. Either player may claim the draw.
5. **Agreement** — both players agree to a draw.
6. **Dead position** — the position is such that neither player can possibly checkmate the other with any sequence of legal moves.

---

## Notation

**Algebraic notation** is the standard for recording chess games.

- Squares are named by file letter (a–h) and rank number (1–8): e.g., e4, g7.
- Pieces are abbreviated: K (King), Q (Queen), R (Rook), B (Bishop), N (Knight). Pawns are unnamed.
- Moves: piece letter + destination square. **Nf3** = knight to f3. **e4** = pawn to e4.
- Capture: piece letter + x + destination. **Bxe5** = bishop captures on e5.
- Castling: O-O (kingside), O-O-O (queenside).
- Check: + appended. **Qh5+**
- Checkmate: # appended. **Qxf7#**
- Promotion: destination square + = + piece. **e8=Q**
- En passant: the capturing square is listed; "e.p." is sometimes appended.
- Disambiguation: when two identical pieces can reach the same square, add the file or rank of the moving piece: **Rad1** (rook on a-file to d1) or **R4d1** (rook on rank 4 to d1).

---

## Basic Opening Principles

These guidelines apply to the first 10–15 moves and form the foundation of sound play regardless of specific opening theory.

**1. Control the center.**
The central squares (d4, d5, e4, e5) are the most important on the board. Pieces placed near the center control more squares. Open with 1.e4 or 1.d4 (White) or respond symmetrically (1...e5, 1...d5) or fight for the center indirectly (1...c5 Sicilian, 1...Nf6 Indian defenses).

**2. Develop pieces rapidly.**
Bring knights and bishops into play before the midgame. Aim to have all pieces developed by move 10–12. Do not move the same piece twice without strong reason. Do not bring the queen out early where it can be harassed.

**3. Castle early.**
Castle to protect the king and connect the rooks. Ideally castle before move 10.

**4. Connect the rooks.**
After castling and developing all pieces, place the rooks on open or half-open files where they have scope.

**5. Do not prematurely attack.**
Attacks launched before development is complete typically fail against accurate defense.

**6. Create and exploit pawn structure.**
Avoid doubled pawns (two pawns of the same color on the same file), isolated pawns (no friendly pawns on adjacent files), and backward pawns where possible. Passed pawns (no enemy pawns blocking or guarding their promotion) are strong in the endgame.

---

## Time Controls

Games may be played with a chess clock limiting each player's total thinking time. Common formats:

- **Bullet:** 1–2 minutes per player
- **Blitz:** 3–5 minutes per player
- **Rapid:** 10–30 minutes per player
- **Classical:** 60 minutes or more per player (often with time increments per move)

A player who runs out of time loses (unless the opponent has insufficient material to force checkmate, in which case the game is a draw).

---

## Piece Values (Approximate)

| Piece  | Value |
|--------|-------|
| Pawn   | 1     |
| Knight | 3     |
| Bishop | 3     |
| Rook   | 5     |
| Queen  | 9     |
| King   | ∞     |

These are guidelines for material calculation, not rigid rules. Positional factors—piece activity, king safety, pawn structure—often outweigh raw material in practical play. Two bishops (the "bishop pair") are generally worth slightly more than bishop + knight or two knights in open positions.

---

## Endgame Essentials

**King and Queen vs. King:** Forced checkmate. Use the queen to confine the enemy king to the edge, bring your king up, then deliver mate.

**King and Rook vs. King:** Forced checkmate. Use the rook to cut off ranks/files, advance your king, and force the enemy king to the edge.

**King and Pawn vs. King:** May or may not be a win depending on pawn position and the opposition (whether the kings are directly facing each other with one square between them). If the defending king can reach the queening square before the pawn, the result is typically a draw.

**Opposition:** When two kings face each other with an odd number of squares between them, the player who does NOT have the move has the opposition. This is a key concept in pawn endgames.

---

*See also: Go (strategy depth), Shogi (piece drops and promotion), Backgammon (luck and skill)*

<div id="scorecard-tool" data-game="chess" data-players="2" class="wm-tool"><h3>🎯 Scorecard</h3></div>
