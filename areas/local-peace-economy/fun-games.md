---
title: "🎉 Fun & Games"
area: local-peace-economy
type: reference
source: Observatory Almanac
source_path: docs/23-practical-tools/fun-tools.md
license: MIT
updated: 2026-04-28
summary: >
  Micro-tools for daily delight, reflection, and decision-making.
tags:
  - tools
  - practical
  - reference
---

# 🎉 Fun & Games

*Micro-tools for daily delight, reflection, and decision-making.*

<div class="wm-tool" id="tool-fortune">

## 🥠 Fortune Cookie

<div class="fortune-cookie-wrap">
  <div class="cookie-container" id="fortune-cookie" onclick="wmFortune.crack()">
    <div class="cookie-half cookie-top"></div>
    <div class="cookie-half cookie-bottom"></div>
    <div class="cookie-fortune-slip" id="fortune-slip"></div>
  </div>
  <p class="fortune-tap-hint" id="fortune-hint">Tap the cookie to reveal your fortune</p>
  <div class="fortune-text" id="fortune-text"></div>
  <div class="fortune-actions" id="fortune-actions" style="display:none">
    <button class="wm-btn" onclick="wmFortune.next()">🥠 Another Fortune</button>
    <button class="wm-btn wm-btn-secondary" onclick="wmFortune.share()">📤 Share</button>
  </div>
</div>

</div>

---

<div class="wm-tool" id="tool-8ball">

## 🎱 Magic 8 Ball

<div class="eightball-wrap">
  <div class="eightball" id="eightball" onclick="wmEightBall.shake()">
    <div class="eightball-inner">
      <div class="eightball-triangle">
        <span class="eightball-answer" id="eightball-answer">🎱</span>
      </div>
    </div>
  </div>
  <p class="eightball-hint">Tap the ball to reveal your answer</p>
</div>

</div>

---

<div class="wm-tool" id="tool-affirmation">

## 💡 Daily Affirmation

<div class="affirmation-wrap">
  <div class="affirmation-card" id="affirmation-card"></div>
  <div class="affirmation-actions">
    <button class="wm-btn wm-btn-secondary" onclick="wmAffirmation.share()">📤 Share</button>
  </div>
  <p class="affirmation-note">✨ Your affirmation for today — the same one all day</p>
</div>

</div>

---

<div class="wm-tool" id="tool-wyr">

## 🤔 Would You Rather

<div class="wyr-wrap">
  <div class="wyr-options" id="wyr-options">
    <div class="wyr-option" id="wyr-a" onclick="wmWYR.choose('a')"></div>
    <div class="wyr-divider">OR</div>
    <div class="wyr-option" id="wyr-b" onclick="wmWYR.choose('b')"></div>
  </div>
  <div class="wyr-stats" id="wyr-stats" style="display:none">
    <div class="wyr-bar-wrap">
      <div class="wyr-bar wyr-bar-a" id="wyr-bar-a"></div>
      <div class="wyr-bar wyr-bar-b" id="wyr-bar-b"></div>
    </div>
    <div class="wyr-pcts" id="wyr-pcts"></div>
  </div>
  <button class="wm-btn" onclick="wmWYR.next()" style="margin-top:1rem">Next Question →</button>
</div>

</div>

---

<div class="wm-tool" id="tool-starters">

## 🗣️ Conversation Starters

<div class="starters-wrap">
  <div class="starters-cats" id="starters-cats">
    <button class="cat-btn active" onclick="wmStarters.setCategory('date',this)">First Date</button>
    <button class="cat-btn" onclick="wmStarters.setCategory('dinner',this)">Dinner Party</button>
    <button class="cat-btn" onclick="wmStarters.setCategory('deep',this)">Deep Talk</button>
    <button class="cat-btn" onclick="wmStarters.setCategory('family',this)">Family</button>
    <button class="cat-btn" onclick="wmStarters.setCategory('work',this)">Work</button>
    <button class="cat-btn" onclick="wmStarters.setCategory('kids',this)">Kids</button>
  </div>
  <div class="starter-card" id="starter-card"></div>
  <button class="wm-btn" onclick="wmStarters.next()">Another Question →</button>
</div>

</div>

---

<div class="wm-tool" id="tool-dadjokes">

## 😂 Dad Jokes

<div class="dadjoke-wrap">
  <div class="dadjoke-setup" id="dadjoke-setup"></div>
  <button class="wm-btn wm-btn-secondary" id="dadjoke-reveal-btn" onclick="wmDadJokes.reveal()" style="margin:0.5rem 0">Tap for punchline 🥁</button>
  <div class="dadjoke-punchline" id="dadjoke-punchline" style="display:none"></div>
  <button class="wm-btn" onclick="wmDadJokes.next()" style="margin-top:0.5rem">Next Joke →</button>
</div>

</div>

---

<div class="wm-tool" id="tool-wheel">

## 🎡 Decision Wheel

<div class="wheel-wrap">
  <canvas id="wheel-canvas" width="300" height="300"></canvas>
  <div class="wheel-inputs" id="wheel-inputs">
    <div id="wheel-fields"></div>
    <button class="wm-btn wm-btn-secondary" onclick="wmWheel.addOption()" style="margin-top:0.5rem">+ Add Option</button>
  </div>
  <button class="wm-btn" id="wheel-spin-btn" onclick="wmWheel.spin()">🎡 Spin!</button>
  <div class="wheel-result" id="wheel-result"></div>
</div>

</div>

---

<div class="wm-tool" id="tool-recommend">

## 🍿 What Should I Watch / Read / Cook?

<div class="recommend-wrap">
  <div class="rec-tabs">
    <button class="rec-tab active" onclick="wmRec.setTab('watch',this)">🎬 Watch</button>
    <button class="rec-tab" onclick="wmRec.setTab('read',this)">📚 Read</button>
    <button class="rec-tab" onclick="wmRec.setTab('cook',this)">🍳 Cook</button>
  </div>
  <div class="rec-card" id="rec-card"></div>
  <button class="wm-btn" onclick="wmRec.next()">Another →</button>
</div>

</div>

---

<div class="wm-tool" id="tool-pomodoro">

## ⏱️ Pomodoro Timer

<div class="pomodoro-wrap">
  <div class="pomodoro-label" id="pom-label">Work Time</div>
  <div class="pomodoro-circle-wrap">
    <svg class="pomodoro-svg" viewBox="0 0 120 120">
      <circle class="pom-track" cx="60" cy="60" r="54"/>
      <circle class="pom-progress" id="pom-progress" cx="60" cy="60" r="54"/>
    </svg>
    <div class="pomodoro-time" id="pom-time">25:00</div>
  </div>
  <div class="pomodoro-session" id="pom-session">Pomodoro #1</div>
  <div class="pomodoro-controls">
    <button class="wm-btn" id="pom-start" onclick="wmPomodoro.toggle()">▶ Start</button>
    <button class="wm-btn wm-btn-secondary" onclick="wmPomodoro.reset()">↺ Reset</button>
  </div>
</div>

</div>

---

<div class="wm-tool" id="tool-habits">

## ✅ Habit Tracker

<div class="habits-wrap">
  <div class="habits-add">
    <input type="text" id="habit-input" placeholder="Add a habit..." maxlength="40" class="wm-input" onkeydown="if(event.key==='Enter')wmHabits.add()">
    <button class="wm-btn" onclick="wmHabits.add()">Add</button>
  </div>
  <div class="habits-week-toggle">
    <button class="wm-btn wm-btn-small active" id="hw-this" onclick="wmHabits.showWeek(0,this)">This Week</button>
    <button class="wm-btn wm-btn-small" id="hw-last" onclick="wmHabits.showWeek(-1,this)">Last Week</button>
  </div>
  <div id="habits-grid"></div>
</div>

</div>

---

<div class="wm-tool" id="tool-gratitude">

## 🙏 Gratitude Journal

<div class="gratitude-wrap">
  <div class="gratitude-date" id="grat-date"></div>
  <div class="gratitude-inputs" id="grat-inputs">
    <input type="text" class="wm-input grat-in" id="grat-1" placeholder="1. I'm grateful for..." maxlength="200">
    <input type="text" class="wm-input grat-in" id="grat-2" placeholder="2. I'm grateful for..." maxlength="200">
    <input type="text" class="wm-input grat-in" id="grat-3" placeholder="3. I'm grateful for..." maxlength="200">
  </div>
  <div class="gratitude-actions">
    <button class="wm-btn" onclick="wmGratitude.save()">💾 Save</button>
    <button class="wm-btn wm-btn-secondary" onclick="wmGratitude.toggleHistory()">📖 Past Entries</button>
  </div>
  <div class="grat-msg" id="grat-msg"></div>
  <div class="grat-history" id="grat-history" style="display:none"></div>
</div>

</div>

---

<div class="wm-tool" id="tool-procon">

## ⚖️ Pro/Con List

<div class="procon-wrap">
  <input type="text" class="wm-input procon-title" id="procon-title" placeholder="Should I... ?" maxlength="100">
  <div class="procon-columns">
    <div class="procon-col procon-pros">
      <h4>✅ Pros</h4>
      <div id="pros-list"></div>
      <div class="procon-add">
        <input type="text" class="wm-input" id="pro-input" placeholder="Add a pro..." maxlength="80" onkeydown="if(event.key==='Enter')wmProCon.add('pro')">
        <div class="star-row" id="pro-stars">
          <span onclick="wmProCon.setStar('pro',1)" class="star" data-v="1">★</span>
          <span onclick="wmProCon.setStar('pro',2)" class="star" data-v="2">★</span>
          <span onclick="wmProCon.setStar('pro',3)" class="star" data-v="3">★</span>
        </div>
        <button class="wm-btn wm-btn-small" onclick="wmProCon.add('pro')">Add</button>
      </div>
    </div>
    <div class="procon-col procon-cons">
      <h4>❌ Cons</h4>
      <div id="cons-list"></div>
      <div class="procon-add">
        <input type="text" class="wm-input" id="con-input" placeholder="Add a con..." maxlength="80" onkeydown="if(event.key==='Enter')wmProCon.add('con')">
        <div class="star-row" id="con-stars">
          <span onclick="wmProCon.setStar('con',1)" class="star" data-v="1">★</span>
          <span onclick="wmProCon.setStar('con',2)" class="star" data-v="2">★</span>
          <span onclick="wmProCon.setStar('con',3)" class="star" data-v="3">★</span>
        </div>
        <button class="wm-btn wm-btn-small" onclick="wmProCon.add('con')">Add</button>
      </div>
    </div>
  </div>
  <button class="wm-btn" onclick="wmProCon.verdict()" style="margin-top:1rem">⚖️ Verdict</button>
  <div class="procon-verdict" id="procon-verdict"></div>
</div>

</div>

---

<div class="wm-tool" id="tool-mood">

## 🌅 Mood Tracker

<div class="mood-wrap">
  <div class="mood-date" id="mood-date"></div>
  <div class="mood-faces" id="mood-faces">
    <span class="mood-face" onclick="wmMood.set(1,'😢')" data-v="1">😢</span>
    <span class="mood-face" onclick="wmMood.set(2,'😐')" data-v="2">😐</span>
    <span class="mood-face" onclick="wmMood.set(3,'🙂')" data-v="3">🙂</span>
    <span class="mood-face" onclick="wmMood.set(4,'😊')" data-v="4">😊</span>
    <span class="mood-face" onclick="wmMood.set(5,'🤩')" data-v="5">🤩</span>
  </div>
  <input type="text" class="wm-input" id="mood-note" placeholder="Optional note..." maxlength="100">
  <button class="wm-btn wm-btn-small" onclick="wmMood.saveNote()">Save Note</button>
  <div class="mood-history" id="mood-history"></div>
</div>

</div>

---

<div class="wm-tool" id="tool-notes">

## 📝 Quick Notes

<div class="notes-wrap">
  <div class="notes-toolbar">
    <button class="wm-btn wm-btn-small" onclick="wmNotes.newNote()">+ New Note</button>
    <button class="wm-btn wm-btn-small wm-btn-secondary" onclick="wmNotes.toggleList()">📋 My Notes</button>
  </div>
  <div class="notes-list" id="notes-list" style="display:none"></div>
  <div class="notes-editor" id="notes-editor">
    <div class="notes-meta" id="notes-meta"></div>
    <textarea class="wm-input notes-textarea" id="notes-area" placeholder="Start typing..." oninput="wmNotes.autoSave()"></textarea>
  </div>
</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof wmFortune !== 'undefined') wmFortune.init();
  if (typeof wmEightBall !== 'undefined') wmEightBall.init();
  if (typeof wmAffirmation !== 'undefined') wmAffirmation.init();
  if (typeof wmWYR !== 'undefined') wmWYR.init();
  if (typeof wmStarters !== 'undefined') wmStarters.init();
  if (typeof wmDadJokes !== 'undefined') wmDadJokes.init();
  if (typeof wmWheel !== 'undefined') wmWheel.init();
  if (typeof wmRec !== 'undefined') wmRec.init();
  if (typeof wmPomodoro !== 'undefined') wmPomodoro.init();
  if (typeof wmHabits !== 'undefined') wmHabits.init();
  if (typeof wmGratitude !== 'undefined') wmGratitude.init();
  if (typeof wmProCon !== 'undefined') wmProCon.init();
  if (typeof wmMood !== 'undefined') wmMood.init();
  if (typeof wmNotes !== 'undefined') wmNotes.init();
});
</script>
