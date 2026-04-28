---
title: "Shogi (将棋)"
area: arts-recreation
type: rulebook
source: Observatory Almanac
source_path: docs/02-universal-rulebook/shogi.md
license: MIT
updated: 2026-04-28
summary: >
  Japanese Chess · 2 players · Ages 8+ · 30 min–3 hours
tags:
  - games
  - strategy
  - play
---

# Shogi (将棋)

**Japanese Chess** · 2 players · Ages 8+ · 30 min–3 hours

Shogi is the Japanese variant of chess, descended from the same Indian ancestor (Chaturanga) but developing independently since at least the 10th century. The defining innovation that separates shogi from all Western chess variants is the **drop rule**: captured pieces are not removed from the game but held in hand and can be re-entered as your own on any subsequent turn. This single rule transforms the game into something far more dynamic—pieces are never truly lost, and the board is always replenishing.

---

## Equipment

- **Board:** 9×9 grid of squares (81 squares total). Unlike chess, all squares are the same color.
- **Pieces:** 40 pieces total (20 per player), each a flat wooden wedge with the piece name written in Japanese characters. The direction the wedge points identifies ownership—both players use the same piece colors.
- **Promotion zone:** The three ranks furthest from a player (ranks 7, 8, 9 from the opponent's perspective, or ranks 1, 2, 3 from the player's perspective).

---

## Pieces and Their Movements

All movements described are from the piece owner's perspective (forward = toward the opponent).

### King (玉将 / 王将 — Gyokushō / Ōshō)
Moves one square in any direction (8 possible squares). The objective of the game.

```
  X X X
  X ♔ X
  X X X
```

### Rook (飛車 — Hisha)
Moves any number of squares orthogonally (as in Western chess). One of the two major pieces.

### Bishop (角行 — Kakugyō)
Moves any number of squares diagonally (as in Western chess). The other major piece.

### Gold General (金将 — Kinshō)
Moves one square in any of six directions: orthogonally (4 directions) plus the two forward diagonals. Cannot move diagonally backward.

```
  X X X
  X ♦ X
  . X .
```

### Silver General (銀将 — Ginshō)
Moves one square diagonally (4 directions) or one square directly forward. Cannot move orthogonally sideways or backward.

```
  X X X
  . ♦ .
  X . X
```

### Knight (桂馬 — Keima)
Jumps to a square two forward and one to the side (two squares forward, one square left or right). The knight can leap over pieces. Unlike Western chess, the shogi knight can ONLY move forward—it has no backward or sideways jump.

```
  X . X
  . . .
  . ♞ .
  . . .
```

### Lance (香車 — Kyōsha)
Moves any number of squares directly forward (cannot move sideways or backward). Similar to a rook restricted to forward movement.

### Pawn (歩兵 — Fuhyō)
Moves exactly one square directly forward. Unlike Western chess, shogi pawns do not capture diagonally—they capture the same way they move (directly forward).

**Two-pawn rule:** You may not have two unpromoted pawns in the same column (file). This is called *nifu* (二歩) and is an immediate loss.

**Pawn drop mate:** You may not drop a pawn to deliver immediate checkmate. You may drop a pawn that creates a threat of checkmate on the NEXT move, but not immediate checkmate. This restriction does not apply to other pieces.

---

## Starting Position

```
  9  8  7  6  5  4  3  2  1
  L  N  S  G  K  G  S  N  L   Row 9 (Black's back rank)
  .  R  .  .  .  .  .  B  .   Row 8
  P  P  P  P  P  P  P  P  P   Row 7
  .  .  .  .  .  .  .  .  .   Row 6
  .  .  .  .  .  .  .  .  .   Row 5
  .  .  .  .  .  .  .  .  .   Row 4
  p  p  p  p  p  p  p  p  p   Row 3 (White's pawns)
  .  b  .  .  .  .  .  r  .   Row 2
  l  n  s  g  k  g  s  n  l   Row 1 (White's back rank)

Uppercase = Black | Lowercase = White
L/l=Lance, N/n=Knight, S/s=Silver, G/g=Gold, K/k=King
R/r=Rook, B/b=Bishop, P/p=Pawn
```

**Note on sides:** In shogi, the two players are called **Black** (先手, Sente — first mover) and **White** (後手, Gote — second mover), though the pieces are not actually colored differently; they are distinguished by orientation.

---

## Promotion

When a piece moves into, out of, or within the **promotion zone** (the 3 ranks closest to your opponent), you MAY promote it. Promotion is optional, with some exceptions.

- **Mandatory promotion exceptions:** A lance or knight that enters the last rank (or last two ranks for the knight) MUST promote, since it would have no legal moves otherwise.

Turn the piece over to reveal its promoted face. Promoted pieces have red or cursive text to distinguish them.

### Promoted Piece Movements

| Original Piece | Promoted Name | Movement |
|----------------|---------------|----------|
| Pawn (歩) | Tokin (と) | Moves like Gold General |
| Lance (香) | Narikyō (成香) | Moves like Gold General |
| Knight (桂) | Narikei (成桂) | Moves like Gold General |
| Silver (銀) | Narigin (成銀) | Moves like Gold General |
| Rook (飛) | Dragon King (龍王) | Moves like Rook + one square diagonally |
| Bishop (角) | Dragon Horse (龍馬) | Moves like Bishop + one square orthogonally |

**Promoted rook (Dragon King):** Rook movement + one step in any diagonal direction. Extremely powerful.

**Promoted bishop (Dragon Horse):** Bishop movement + one step in any orthogonal direction. Extremely powerful.

Gold Generals and Kings do not promote.

### Demotion
When a promoted piece is captured, it reverts to its original unpromoted form and goes into the capturer's hand.

---

## The Drop Rule

Captured pieces are placed in front of you (in your "hand" or "komadai" — the piece stand). On any turn instead of moving a piece on the board, you may **drop** a piece from your hand onto any empty square.

**Drop restrictions:**
1. A dropped piece is unpromoted, regardless of its promoted state when captured.
2. A lance may not be dropped on the last rank (it would have no moves).
3. A knight may not be dropped on the last two ranks.
4. A pawn may not be dropped in a file that already contains one of your unpromoted pawns (two-pawn rule).
5. A pawn may not be dropped to deliver immediate checkmate (drop-pawn-mate prohibition).
6. All other drops are legal—you may drop into check threats, create forks, and deliver check with drops.

The drop rule means:
- Material is never permanently lost.
- Defense requires considering both the opponent's hand and their board pieces.
- The pace of attack can accelerate dramatically when pieces are dropped directly near the opponent's king.

---

## Check and Checkmate

**Check (王手, Ōte):** Announcing that the king is under attack is traditional but not required. The king must escape by moving, blocking with another piece, or capturing the attacking piece.

**Checkmate (詰み, Tsumi):** The king is in check with no legal move to escape. The game ends; the checkmated player loses.

**Stalemate:** Does not occur in practice in shogi due to the drop rule; if a player has no legal moves (extremely rare), it is a loss.

---

## Draw Conditions

**Perpetual check (千日手, Sennichite):** If the same position (with the same player to move and the same pieces in hand) occurs four times, the game is declared a draw. Play restarts from the initial position or the draw is settled by other means in tournament play (usually replaying).

**Impasse / Entering King (入玉, Nyūgyoku):** If both kings advance into the opponent's promotion zone and neither can be checkmated, the game may end in an impasse. Under the standard Jishogi rule: if one player has their king in the promotion zone plus 10 or more major and minor pieces there, they win; if both qualify, the game is a draw.

**Declaration win:** A player whose king has entered and established itself in the opponent's camp may declare a win if they have enough material (24+ points counting gold/silver as 5 points each, and all other pieces except king as 1 point each, with at least 10 pieces in the promotion zone).

---

## Notation

Shogi uses a coordinate system: columns numbered 9 to 1 (right to left from Black's perspective), rows numbered 1 to 9 (top to bottom from Black's perspective).

A move is notated as: piece abbreviation + destination + movement type.

Example: **P-7f** = Pawn to 7f
**Bx8h+** = Bishop captures on 8h and promotes
**P*5e** = Pawn dropped to 5e (asterisk indicates a drop)

---

## Basic Strategy

### Opening (Joseki)
Unlike chess, shogi openings focus heavily on king safety and castle formation before central conflict.

**Common castles:**

**Mino Castle (美濃囲い):** Compact and easy to build. King shifts to the knight's position. Standard against ranging rook formations.

**Yagura Castle (矢倉囲い):** Solid, central castle with the king protected by gold generals and a pawn wall. The classical fortress against static rook openings.

**Anaguma Castle (穴熊):** "Bear in the hole." The king retreats to the corner behind maximum fortifications. Takes many moves to build but nearly impregnable.

### Rook Formations
The rook's starting position largely determines the opening system:

**Static rook (居飛車, Ibisha):** Keep the rook on the right side (8th file). Common with Yagura and other solid castles.

**Ranging rook (振り飛車, Furibisha):** Move the rook to the left side. More aggressive, favors Mino or Anaguma castles.

**Double ranging rook:** Both players adopt ranging rook—a mirror game.

### The Drop Threat
Always calculate what pieces your opponent holds in hand. A single pawn drop near your castle can break open defenses. A rook drop is nearly always decisive. Count your exposed squares.

### Piece Exchange
Unlike chess, exchanging pieces in shogi feeds your opponent's hand. Avoid unnecessary exchanges, especially giving up gold generals (they become powerful drops).

### Tsumeshogi (詰将棋)
Shogi checkmate puzzles—equivalent to chess puzzles. Practice solving tsumeshogi to improve tactical vision and checkmate pattern recognition. Even 1-move and 3-move problems provide significant benefit for beginners.

### Classic Checkmate Patterns

**King-Gold-Silver net:** Crowd the king with gold and silver generals. A gold in front of the king plus a rook on the same file often forces forced mate sequences.

**Rook-drop mate:** Drop a rook on a file adjacent to the king, with support from above or below, forcing the king into a corner.

**Pawn sacrifice:** Sacrifice a pawn drop to open a file for a rook or create a forced sequence.

---

## Etiquette

- Hold the piece you wish to move until you release it. Once released, the move is made.
- Place pieces firmly; do not hover pieces over squares.
- Captured pieces are placed in front of you in an organized manner.
- In formal play, announce "Otemae" when giving check (optional in casual play).
- Resign (*kōsan* — 降参) gracefully when the position is hopeless.

---

*See also: Chess (Western chess origin), Go (abstract territory game), Xiangqi (Chinese chess)*

<div id="scorecard-tool" data-game="shogi" data-players="2" class="wm-tool"><h3>🎯 Scorecard</h3></div>
