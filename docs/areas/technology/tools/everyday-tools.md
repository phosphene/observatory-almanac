# Everyday Tools

All tools work offline. Data saves to your device.

---

## ðª Coin Flip & Dice Roller

---

## â±ï¸ Stopwatch & Timer

---

## ð¢ Calculator

---

## ð BMI Calculator

---

## ð  Loan / Mortgage Calculator

---

## ð Age Calculator

---

## ð Date Difference

---

## ð Percentage Calculator

---

## ð° Random Number Generator

---



---

## 📝 Scratch Scorepad

<div id="score-tool" markdown>

<div style="padding:16px; background:#f5f5f0; border-radius:8px; margin:1em 0;">
<div style="margin-bottom:12px;">
<input type="text" id="score-name" placeholder="Player name" style="padding:8px; font-size:14px; border-radius:6px; border:1px solid #888;">
<button onclick="addPlayer()" style="padding:8px 16px; margin-left:4px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">Add Player</button>
<button onclick="resetScores()" style="padding:8px 16px; margin-left:4px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fdd;">Reset All</button>
</div>
<div id="score-board" style="display:flex; flex-wrap:wrap; gap:12px;"></div>
</div>

</div>

<script>
(function() {
  let players = [];

  function render() {
    let html = "";
    players.forEach((p, i) => {
      html += `<div style="background:#fff; border-radius:8px; padding:12px; min-width:120px; text-align:center; border:1px solid #ddd;">
        <div style="font-weight:bold; margin-bottom:4px;">${p.name}</div>
        <div style="font-size:2em; font-family:monospace; margin:8px 0;">${p.score}</div>
        <button onclick="changeScore(${i},1)" style="padding:4px 12px; cursor:pointer; border-radius:4px; border:1px solid #888; background:#dfd; margin:2px;">+1</button>
        <button onclick="changeScore(${i},-1)" style="padding:4px 12px; cursor:pointer; border-radius:4px; border:1px solid #888; background:#fdd; margin:2px;">−1</button>
      </div>`;
    });
    document.getElementById("score-board").innerHTML = html;
  }

  window.addPlayer = function() {
    const name = document.getElementById("score-name").value.trim();
    if (!name) return;
    players.push({name, score: 0});
    document.getElementById("score-name").value = "";
    render();
  };

  window.changeScore = function(i, delta) {
    players[i].score += delta;
    render();
  };

  window.resetScores = function() {
    players = [];
    render();
  };
})();
</script>
