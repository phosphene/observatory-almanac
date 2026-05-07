# Go (å´æ£ / å²ç¢ / ë°ë)

**The Ancient Way** Â· 2 players Â· Ages 6+ Â· 20 minâ3 hours

Go is the oldest continuously played board game in history, originating in China over 2,500 years ago. Despite rules that can be stated in minutes, Go's strategic depth exceeds chess: the number of possible games is estimated at 10^170. Black and White alternate placing stones on a grid, surrounding territory and capturing enemy stones.

---

## The Board

Go is played on a grid of lines. Stones are placed on intersections, not squares.

* **Standard (19Ã19):** Full competition board. 361 intersections.
* **13Ã13:** Intermediate board, popular for learning.
* **9Ã9:** Beginner board, games last 20â40 minutes.

```
19Ã19 board â corners and star points marked:

   A B C D E F G H J K L M N O P Q R S T
19 . . . . . . . . . . . . . . . . . . .
18 . . . . . . . . . . . . . . . . . . .
17 . . . . . . . . . . . . . . . . . . .
16 . . . * . . . . . * . . . . . * . . .
15 . . . . . . . . . . . . . . . . . . .
14 . . . . . . . . . . . . . . . . . . .
13 . . . . . . . . . . . . . . . . . . .
12 . . . . . . . . . . . . . . . . . . .
11 . . . . . . . . . . . . . . . . . . .
10 . . . * . . . . . * . . . . . * . . .
 9 . . . . . . . . . . . . . . . . . . .
 8 . . . . . . . . . . . . . . . . . . .
 7 . . . . . . . . . . . . . . . . . . .
 6 . . . . . . . . . . . . . . . . . . .
 5 . . . . . . . . . . . . . . . . . . .
 4 . . . * . . . . . * . . . . . * . . .
 3 . . . . . . . . . . . . . . . . . . .
 2 . . . . . . . . . . . . . . . . . . .
 1 . . . . . . . . . . . . . . . . . . .
   A B C D E F G H J K L M N O P Q R S T
```

Note: Column I is omitted in Go notation (replaced by J) to avoid confusion with the number 1.

Star points (hoshi) are marked intersections used for handicap stone placement and visual orientation. On a 19Ã19 board they are at d4, d10, d16, j4, j10, j16, q4, q10, q16.

---

## Equipment

* **Stones:** Black plays 181 stones; White plays 180 stones (though sets often include extra). Black always has more because Black moves first and therefore may have more stones on the board.
* **Bowls:** Stones are kept in covered bowls. Placing the lid upside-down is considered rude (implies your stones are all captured).
* **Board:** Traditional boards are slightly rectangular (taller than wide) to appear square when viewed at an angle.

---

## Core Rules

### Basic Play

1. Black places the first stone.
2. Players alternate placing one stone per turn on any empty intersection.
3. Stones are never moved after placement (unless captured).
4. A player may pass their turn instead of playing.
5. The game ends when both players pass consecutively.

### Liberties and Capture

Every stone and every connected group of same-color stones has **liberties**: the empty intersections directly adjacent (horizontally or verticallyânever diagonally) to the group.

* A stone with no liberties is captured and removed from the board.
* When you place a stone that removes all liberties from an enemy group, you capture that entire group immediately.
* You may not place a stone that would leave your own group with zero liberties (suicide) UNLESS that placement simultaneously captures an enemy group (which restores liberties). Most rulesets prohibit suicide entirely; some (Chinese rules) permit it.

```
Liberties example:
  . B .      The Black stone at center has 4 liberties (up, down, left, right)
  B B B      A connected group's liberties = all empty adjacent points of ALL stones in the group
  . B .
```

```
Capture example:
  . W .      White stone is surrounded on all sides.
  W B W      If Black plays above or below White, White is captured.
  . . .
```

### Groups and Connection

Stones of the same color that are directly adjacent (horizontally or vertically) form a connected **group** (also called a string or chain). All stones in a group share liberties collectively. A group is safe as long as it has at least one liberty.

### Eyes and Life

A **living group** is one that cannot be captured regardless of what the opponent plays. The primary mechanism of life is having **two eyes**: two separate enclosed empty spaces within a group. An opponent cannot fill the last liberty of a group that has two eyes because doing so would be an illegal self-capture.

```
Two-eye life:
  B B B B
  B . B .   <-- Two separate eye spaces; this group cannot be captured
  B B B B
```

**False eye:** An enclosed space that only one side of a group bordersâthe opponent may be able to play into it, denying life.

**Seki:** A situation where two groups are mutually alive without having two eyes, because each player playing into the shared liberties would cause their own group to be captured. Both groups survive; their territory may or may not count depending on ruleset.

---

## The Ko Rule

**Ko** (Japanese: å«, meaning "eternity") prevents infinite loops.

A ko situation arises when a capture would recreate the exact same board position that existed before the previous move. This capture is temporarily forbidden.

**Ko rule:** A player may not make a move that recreates the immediately previous board position.

To "win" a ko, a player makes a **ko threat** elsewhere on the boardâa move that demands an immediate response. The opponent answers the threat, and the ko player returns to capture the ko. The opponent now has the threat-answering obligation elsewhere and cannot immediately recapture.

**Super Ko:** Some rulesets extend this to prohibit any move that recreates ANY previous board position (not just the immediately prior one). Chinese and AGA rules use positional super ko; Japanese rules use situational super ko.

---

## Scoring

The goal is to control more territory than your opponent (plus capturing stones contributes in some rulesets).

### Territory Scoring (Japanese/Korean Rules)

* **Territory:** Empty intersections completely surrounded by one player's living stones.
* **Score = territory + prisoners captured.**
* Dead stones (stones that would inevitably be captured in further play) are removed before scoring and added to the opponent's prisoner count.
* Seki groups: their enclosed empty points do NOT count as territory.
* Komi (compensation for White, who moves second): typically 6.5 points.

### Area Scoring (Chinese Rules)

* **Score = living stones on the board + empty territory surrounded.**
* Captured stones are NOT counted (simplifying record-keeping).
* Dead stones are simply removed; the empty points they occupied become the capturer's territory.
* Komi: typically 7.5 points under Chinese rules.
* Seki groups: enclosed empty points DO count as territory for the surrounding player.

**Practical difference:** The two scoring systems typically produce the same winner. Territory scoring is traditional in Japan and Korea; area scoring is standard in China and increasingly used in international competition.

### Counting Territory

After both players pass, remove all dead stones by agreement (if players disagree on life/death, resume play to settle it). Arrange remaining empty points into rectangles for easy counting. Subtract komi from Black's score or add it to White's.

---

## Komi

Because White plays second (a disadvantage), White receives **komi**âa set number of points added to White's score before comparison. Standard komi:
- Japanese/Korean rules: **6.5 points**
- Chinese rules: **7.5 points**
- The half-point eliminates draws.

Historically komi was 4.5, raised to 5.5, then 6.5 as understanding of the first-mover advantage improved.

---

## Handicap Stones

To equalize games between players of different strength, the weaker player (Black) places extra stones on the board before the game begins. White then goes first.

**Standard handicap placements (19Ã19):**

| Handicap | Stones placed at |
| --- | --- |
| 2 | d4, q16 |
| 3 | d4, q16, q4 |
| 4 | d4, q16, d16, q4 |
| 5 | d4, q16, d16, q4, j10 (center) |
| 6 | d4, q16, d16, q4, d10, q10 |
| 7 | d4, q16, d16, q4, d10, q10, j10 |
| 8 | d4, q16, d16, q4, d10, q10, j4, j16 |
| 9 | All 9 star points |

Under handicap, White typically plays without komi, or with reduced komi.

Go ranks are measured in kyu (beginner, counting down from ~30 kyu) and dan (advanced, counting up from 1 dan). Each rank difference corresponds to approximately one handicap stone.

---

## Basic Strategy Concepts

### Opening (Fuseki)

The opening phase establishes frameworkâlarge-scale influence and territorial claims.

* **Corner priority:** Corners require the fewest stones to enclose territory. Open by approaching corners.
* **Star point (hoshi):** Playing at the 4-4 point (d4, etc.) emphasizes influence over the center.
* **Komoku (3-4 point):** Balances corner control and side influence.
* **Sansan (3-3 point):** Secures the corner quickly but concedes outside influence.
* **Shimari:** A two-stone corner enclosure that secures a corner.
* **Kakari:** An approach move toward an opponent's corner stone, seeking to either live inside or press outward.

### Middle Game (Chuban)

Involves attacking, defending, invading, and building shapes.

* **Tesuji:** A clever tactical moveâthe "right move" in a local situation.
* **Sente and gote:** Sente = a move that demands a reply (you keep initiative). Gote = a move your opponent doesn't need to answer immediately (they keep initiative). Playing sente moves first is generally better.
* **Thickness (Atsumi):** A solid, influential wall of stones with no weaknesses. Thick groups exert influence over a wide area. Do not invade near thickness.
* **Overconcentration:** Too many stones in a small areaâinefficient.
* **Cutting:** Separating enemy stones to prevent them from connecting and forming strong groups.
* **Connection:** Keeping your own stones connected to prevent them from being isolated and killed.

### Fighting

* **Atari:** A move that leaves an enemy group with only one liberty (the equivalent of "check" in chess). Threats of atari often force responses.
* **Ladder (Shicho):** A sequence of atari moves that chases a stone across the board. A stone caught in a ladder cannot escape unless a friendly stone lies along the path.
* **Net (Geta):** A technique that surrounds an enemy stone so it cannot escape even with unlimited moves.
* **Ko fights:** Complex recursive situations where each player makes threats to win the right to resolve a ko capture.

### Endgame (Yose)

The endgame involves closing boundaries and making small but precise moves to maximize territory. Moves are evaluated by their size (how many points they gain or prevent losing). Play the largest endgame moves first. Common endgame sequences:

* Pushing along the edge to reduce opponent territory
* Diagonal moves (hane) at the edge of groups
* Connecting or cutting to settle boundary disputes

### Life and Death Problems (Tsumego)

Practicing life-and-death problems is the fastest way to improve. Tsumego train you to read sequences and recognize patterns of life (two eyes), death (no two eyes), and ko.

---

## Etiquette

* Place stones decisively; do not slide them into position.
* Capture stones by placing them in the lid of your bowl.
* At game end, remove dead stones by mutual agreement before counting.
* Resign when the position is hopeless rather than playing out a lost game.
* In Japan and Korea, the loser typically tips the board (a ritual gesture); in modern play, a simple "thank you for the game" (Japanese: *o-tsukaresama deshita*) is standard.

---

*See also: Chess (abstract strategy), Shogi (captures and drops)*

### ð¯ Scorecard