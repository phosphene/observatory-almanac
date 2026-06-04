# Cribbage

*The Observatory Almanac — Universal Rulebook*

---

Cribbage is a two-player card game of elegant antiquity, attributed to the English poet Sir John Suckling in the seventeenth century and formalized into essentially its modern form by the mid-1700s. It is unusual among card games in that scoring occurs at multiple stages — during play (pegging) and during counting — and that a wooden board with pegs is used to track the running score rather than pencil and paper. The combination of deal luck, hand evaluation, crib strategy, and pegging skill makes cribbage one of the most tactically rich two-player games ever devised.

---

## The Board

The cribbage board is the game's most distinctive artifact. It serves as both scorekeeper and timer.

```
START                                                    END
  |                                                       |
  0  5  10  15  20  25  30  35  40  45  50  55  60
  ●  ○  ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   → [Player 1 outer]
  ●  ○  ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   → [Player 1 inner]

  ●  ○  ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   → [Player 2 inner]
  ●  ○  ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   ○   → [Player 2 outer]
  0  5  10  15  20  25  30  35  40  45  50  55  60

  [60 → return track → 120/121]
```

Each player has two pegs and two rows of 30 holes (outer and inner tracks). Movement proceeds:
- Up the outer row from 0 to 60
- Then back down the inner row from 60 to 121

The trailing peg marks the previous score; the leading peg marks the current score. To score, the rear peg leapfrogs the front peg. This leap-frog method ensures an accurate running total — if you miscount, the prior peg position provides a reference.

**Standard game:** First to **121 points** wins (the "go to the hole" mark). Some informal games play to 61 (once around).

**Board variants:** Three-track boards for three-player cribbage, four-track boards, travel boards, and track-around boards (continuous oval) all exist. The counting logic is identical.

---

## The Deck and Card Values

Standard 52-card deck. No jokers.

For counting and pegging purposes, **all face cards (J, Q, K) count as 10**. Aces count as 1. Number cards count face value (2 through 10). The numerical value is used only for counting to 31 during pegging and for scoring fifteens. **Rank** (A, 2, 3, ... K) is used for pairs and runs.

---

## The Deal

Traditionally, the player who cuts the lower card deals first. Subsequently, the deal alternates each hand.

**Each player is dealt six cards.** Each player then discards **two cards face down** to the **crib** — a separate four-card hand belonging to the dealer. The crib will be counted by the dealer at the end of the hand as bonus points.

The non-dealer's strategy in discarding to the crib is to give the dealer as little help as possible. The dealer, conversely, tries to throw useful cards.

---

## The Starter Card (The Cut)

After discarding, the non-dealer **cuts the remaining stock**. The dealer lifts the top portion, and the non-dealer takes the bottom card of the top portion and places it face up on top of the stock. This is the **starter card** (also called the "cut card" or "the turn").

**His Nobs (Knobs) at the Cut:** If the starter card is a **Jack**, the dealer immediately pegs **2 points** ("two for his heels" or "heels"). This is scored before pegging begins.

The starter card is used by both players (and the crib) during counting. It is the fifth card in every hand's count.

---

## Pegging

Pegging is the play phase, occurring before hands are counted. It is a running count toward 31.

### Procedure

The non-dealer leads the first card, placing it face up and announcing its value. Players alternate playing cards, each announcing the cumulative total.

**Example:**
- Non-dealer plays 7: announces "7"
- Dealer plays 8: announces "15" — scores 2 points for fifteen
- Non-dealer plays 6: announces "21"
- Dealer plays 4: announces "25"
- Non-dealer plays 5: announces "30"
- Dealer cannot play without exceeding 31. Says "Go."
- Non-dealer plays nothing further. Scores 1 point for Go.

### Scoring During Pegging

Points are pegged immediately when earned.

| Scoring Event | Points |
| --- | --- |
| Reaching exactly **15** | 2 |
| Reaching exactly **31** | 2 |
| **Go** (opponent cannot play without exceeding 31) | 1 |
| Last card played in the round (if not exactly 31) | 1 |
| **Pair** (card of same rank as the just-played card) | 2 |
| **Pair Royal** (third card of same rank) | 6 |
| **Double Pair Royal** (fourth card of same rank) | 12 |
| **Run** (consecutive sequence of 3 cards in any order) | 3 |
| **Run of 4** | 4 |
| **Run of 5** | 5 |

**Runs during pegging:** The run does not need to be played in order — only the last three or more cards played must form a consecutive sequence. Example: 5, 7, 6 scores a run of 3 because 5-6-7 is a consecutive sequence.

### The Go

When a player cannot play without exceeding 31, they call "Go." The opponent continues playing cards until they also cannot play without exceeding 31. The player who played the last card before the "Go" scores 1 point (unless they reached exactly 31, which scores 2 instead of 1).

After a Go, the count resets to 0 and the player who called Go leads the next series, starting fresh.

### End of Pegging

Pegging continues until all eight cards have been played. Any runs, pairs, fifteens, or 31s during the final plays are scored normally.

---

## Counting the Hands

After pegging, hands are counted in this order:
1. **Non-dealer's hand** (four cards + starter)
2. **Dealer's hand** (four cards + starter)
3. **The crib** (four crib cards + starter) — counted by dealer only

This order matters: if the non-dealer reaches 121 during their count, they win immediately, even if the dealer's count would also cross 121.

### Scoring Categories in Counting

Each hand (or crib) is scored by examining every possible combination of cards.

#### Fifteens — 2 points each

Any combination of two, three, four, or five cards that sums to exactly 15 scores 2 points.

Example hand: 7♠ 8♥ 6♦ 7♣, starter: 2♥
- 7+8 = 15 ✓ (2 pts)
- 7+8 = 15 ✓ (other 7, 2 pts)
- 6+7+2 = 15 ✓ (2 pts)
- 6+7+2 = 15 ✓ (other 7, 2 pts)
= 8 points for fifteens alone.

Face cards count 10. Ace counts 1. 5+J = 15 (2 pts).

#### Pairs — 2 points each

Two cards of the same rank score 2. Three of a kind = three distinct pairs = 6. Four of a kind = six distinct pairs = 12.

#### Runs — 1 point per card

Three consecutive ranks score 3. Four consecutive ranks score 4. Five consecutive ranks score 5. Suit is irrelevant for runs.

**Double runs:** A run with a pair scores the run twice plus the pair.
Example: 4-4-5-6 = two runs of 3 (6 pts) + one pair (2 pts) = 8 pts.

**Triple runs:** Three cards of one rank plus two forming a run.
Example: 4-4-4-5-6 = three runs of 3 (9 pts) + three of a kind (6 pts) = 15 pts.

#### Flush — Points for matching suits

If all four cards in the **hand** are the same suit: 4 points.
If all four cards in the hand **and** the starter are the same suit: 5 points.

**Crib flush:** A flush in the crib scores only if all four crib cards **and** the starter share a suit. A 4-card flush alone in the crib does not score.

#### Nobs (His Nobs) — 1 point

If the hand contains a **Jack of the same suit as the starter card**, score 1 point for "nobs." (Different from "heels," which is scored at the cut.) Nobs counts in both hands and in the crib.

#### The Perfect Hand (29 Points)

The maximum possible hand in cribbage is 29 points: J-5-5-5, starter 5 (where the Jack's suit matches the starter). This produces:
- 8 fifteens (using all four 5s and the J): 16 points
- 4 fives = 6 distinct pairs: 12 points
- Nobs (Jack matches starter suit): 1 point
= 29 points. Extraordinarily rare.

---

## The Muggins Rule

Under the **muggins** rule (used in formal and competitive play), if a player fails to claim all points they are entitled to, their opponent may announce "Muggins!" and claim the overlooked points themselves. Muggins applies to both pegging and hand counting.

Players must declare their count aloud. Opponents must pay attention. Muggins is optional and should be agreed upon before play begins. In casual play it is often omitted; in tournament play it is standard.

---

## The Crib

The crib belongs to the dealer and is scored after both hands. It is counted exactly like a hand: the four crib cards plus the starter are scored for fifteens, pairs, runs, flushes (crib-flush rules apply, as above), and nobs.

**Strategy implications:**
- Non-dealer should avoid throwing powerful cards (pairs, cards forming fifteens) to the crib.
- Dealer should throw cards with combinatorial value.
- Common crib gifts from non-dealer: wide-apart cards of different suits with low synergy (e.g., K and 3 — far apart, unlikely to fifteen, unlikely to pair with other discards).
- Dangerous crib discards for non-dealer: A-2, 5s, pairs of any rank.

---

## Winning and Skunking

**Win:** First player to peg or count to 121 points wins.

**Skunk:** If the loser has not passed the 90-point mark (31 points or more behind), the winner scores a **double game** or simply "skunked" the opponent. In tournament scoring, a skunk counts as 2 games won.

**Double Skunk:** If the loser has not passed 60 points, the winner scores a **triple game** in some rule sets (4 games in others). This is rare and devastating.

---

## Three-Player and Four-Player Cribbage

**Three players:** Each player receives five cards; each discards one to the crib. The crib thus has three cards. A single starter card is cut. The crib goes to the dealer as normal. Play proceeds to 121.

**Four players (partnership):** Two partnerships of two, seated across from each other. Partners share a running total. Each player receives five cards, discards one to the crib. The crib belongs to the dealing partnership. Partners may not communicate hand contents.

---

## Sequence of a Full Hand (Summary)

1. Cut for deal (low card deals first)
2. Deal six cards to each player
3. Each player discards two cards to the crib
4. Non-dealer cuts the stock; starter card revealed
5. "Heels" scored if starter is a Jack (2 pts to dealer)
6. Pegging phase (non-dealer leads)
7. Count non-dealer's hand (four cards + starter)
8. Count dealer's hand (four cards + starter)
9. Count the crib (four crib cards + starter)
10. Advance deal to opponent; repeat
11. First to 121 wins

---

## Cribbage Notation

Experienced cribbage players use shorthand for hands:

* **15-2, 15-4, pair for 6:** Means two fifteens (4 pts) and a pair (2 pts), total 6.
* **15-2, 15-4, 15-6, 15-8, run for 11:** Four fifteens plus a 3-card run.

The "running count" style (15-2, 15-4...) is the standard verbal scoring used in clubs and tournaments.

---

*The Observatory Almanac — rules compiled from the American Cribbage Congress (ACC) official rules and widely accepted standard play.*

### 🎯 Scorecard