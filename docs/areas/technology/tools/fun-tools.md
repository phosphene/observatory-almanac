# 🎉 Fun & Games

*Micro-tools for daily delight, reflection, and decision-making.*

---

## 🍅 Pomodoro Timer

<div id="pomo-tool" markdown>

<div style="text-align:center; padding:20px; background:#f5f5f0; border-radius:8px; margin:1em 0;">
<div id="pomo-mode" style="font-size:1.2em; font-weight:bold; color:#c44;">WORK</div>
<div id="pomo-display" style="font-size:4em; font-family:monospace; margin:12px 0;">25:00</div>
<div style="margin:12px 0;">
<button onclick="pomoStart()" style="padding:10px 20px; font-size:16px; margin:4px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">▶ Start</button>
<button onclick="pomoPause()" style="padding:10px 20px; font-size:16px; margin:4px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">⏸ Pause</button>
<button onclick="pomoReset()" style="padding:10px 20px; font-size:16px; margin:4px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">🔄 Reset</button>
</div>
</div>

</div>

<script>
(function() {
  let remaining = 1500, timer = null, isWork = true, audioCtx = null;
  function display() {
    const m = Math.floor(remaining / 60), s = remaining % 60;
    document.getElementById("pomo-display").textContent = String(m).padStart(2,"0")+":"+String(s).padStart(2,"0");
    document.getElementById("pomo-mode").textContent = isWork ? "WORK" : "BREAK";
    document.getElementById("pomo-mode").style.color = isWork ? "#c44" : "#4a4";
  }
  function bell() {
    audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
    const o = audioCtx.createOscillator(), g = audioCtx.createGain();
    o.connect(g); g.connect(audioCtx.destination);
    o.frequency.value = 660; o.type = "sine";
    g.gain.setValueAtTime(0.4, audioCtx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 2);
    o.start(); o.stop(audioCtx.currentTime + 2);
  }
  window.pomoStart = function() {
    if (timer) return;
    timer = setInterval(() => {
      remaining--;
      display();
      if (remaining <= 0) {
        bell();
        isWork = !isWork;
        remaining = isWork ? 1500 : 300;
        display();
      }
    }, 1000);
  };
  window.pomoPause = function() { if (timer) { clearInterval(timer); timer = null; } };
  window.pomoReset = function() { pomoPause(); isWork = true; remaining = 1500; display(); };
  display();
})();
</script>

---

## 🎰 Decision Wheel

<div id="wheel-tool" markdown>

<div style="padding:16px; background:#f5f5f0; border-radius:8px; margin:1em 0; text-align:center;">
<div style="margin-bottom:12px;">
<input type="text" id="wheel-input" placeholder="Enter options separated by commas" style="padding:8px; font-size:14px; width:80%; max-width:400px; border-radius:6px; border:1px solid #888;">
</div>
<canvas id="wheel-canvas" width="300" height="300" style="margin:0 auto; display:block;"></canvas>
<div id="wheel-result" style="font-size:1.5em; font-weight:bold; margin:12px 0; min-height:1.5em;"></div>
<button onclick="spinWheel()" style="padding:10px 20px; font-size:16px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">🎡 Spin!</button>
</div>

</div>

<script>
(function() {
  const colors = ["#FF6B6B","#4ECDC4","#45B7D1","#96CEB4","#FFEAA7","#DDA0DD","#98D8C8","#F7DC6F"];
  let spinning = false;

  window.spinWheel = function() {
    if (spinning) return;
    const raw = document.getElementById("wheel-input").value;
    const options = raw.split(",").map(s => s.trim()).filter(s => s);
    if (options.length < 2) { alert("Enter at least 2 options separated by commas"); return; }

    const canvas = document.getElementById("wheel-canvas");
    const ctx = canvas.getContext("2d");
    const cx = 150, cy = 150, r = 140;
    const arc = (2 * Math.PI) / options.length;
    let angle = 0;
    const totalSpin = Math.random() * 360 + 720 + Math.random() * 720;
    const duration = 3000;
    const start = Date.now();
    spinning = true;

    function draw(currentAngle) {
      ctx.clearRect(0, 0, 300, 300);
      for (let i = 0; i < options.length; i++) {
        const startA = currentAngle + i * arc;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.arc(cx, cy, r, startA, startA + arc);
        ctx.fillStyle = colors[i % colors.length];
        ctx.fill();
        ctx.stroke();
        // Label
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(startA + arc / 2);
        ctx.textAlign = "right";
        ctx.fillStyle = "#333";
        ctx.font = "bold 13px sans-serif";
        ctx.fillText(options[i].substring(0, 12), r - 10, 5);
        ctx.restore();
      }
      // Arrow
      ctx.beginPath();
      ctx.moveTo(cx + r + 5, cy);
      ctx.lineTo(cx + r + 20, cy - 8);
      ctx.lineTo(cx + r + 20, cy + 8);
      ctx.fillStyle = "#333";
      ctx.fill();
    }

    function animate() {
      const elapsed = Date.now() - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3);
      const currentAngle = (totalSpin * ease * Math.PI) / 180;
      draw(currentAngle);

      if (progress < 1) {
        requestAnimationFrame(animate);
      } else {
        spinning = false;
        const finalAngle = (currentAngle % (2 * Math.PI));
        const idx = Math.floor(((2 * Math.PI - finalAngle) % (2 * Math.PI)) / arc) % options.length;
        document.getElementById("wheel-result").textContent = "🎯 " + options[idx] + "!";
      }
    }
    animate();
  };
})();
</script>

---

## 🎱 Magic 8 Ball

<div id="eight-ball" markdown>

<div style="text-align:center; padding:20px; background:#1a1a2e; border-radius:50%; width:200px; height:200px; margin:1em auto; cursor:pointer; display:flex; align-items:center; justify-content:center;" onclick="shake8Ball()">
<div id="eight-answer" style="background:#fff; border-radius:50%; width:80px; height:80px; display:flex; align-items:center; justify-content:center; font-size:0.7em; text-align:center; padding:8px; font-weight:bold;">Click me</div>
</div>

</div>

<script>
(function() {
  const answers = [
    "It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it",
    "As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes",
    "Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again",
    "Don\'t count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"
  ];
  window.shake8Ball = function() {
    const el = document.getElementById("eight-answer");
    el.textContent = "...";
    setTimeout(() => { el.textContent = answers[Math.floor(Math.random() * answers.length)]; }, 500);
  };
})();
</script>

---

## 🥠 Fortune Cookie

<div id="fortune-tool" style="text-align:center; margin:1em 0;" markdown>

<div id="fortune-text" style="font-size:1.2em; font-style:italic; padding:20px; background:#fff8e7; border-radius:8px; min-height:60px; display:flex; align-items:center; justify-content:center;">Click the cookie to reveal your fortune</div>
<button onclick="openFortune()" style="padding:12px 24px; font-size:20px; margin-top:12px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">🥠 Open Cookie</button>

</div>

<script>
(function() {
  const fortunes = [
    "A beautiful, smart, and loving person will come into your life.",
    "A dubious friend may be an enemy in camouflage.",
    "A faithful friend is a strong defense.",
    "A fresh start will put you on your way.",
    "A golden egg of opportunity falls into your lap this month.",
    "A good time to finish up old tasks.",
    "A lifetime of happiness lies ahead of you.",
    "A light heart carries you through all the hard times ahead.",
    "A new perspective will come with the new year.",
    "A pleasant surprise is waiting for you.",
    "A smile is your passport into the hearts of others.",
    "A soft voice may be awfully persuasive.",
    "All your hard work will soon pay off.",
    "An important person will offer you support.",
    "Be not afraid of growing slowly, be afraid only of standing still.",
    "Believe in yourself and others will too.",
    "Curiosity kills boredom. Nothing can kill curiosity.",
    "Disbelief destroys the magic.",
    "Don't just think. Act.",
    "Every flower must grow through dirt.",
    "Fortune favors the brave.",
    "Generosity and perfection are your everlasting goals.",
    "He who throws dirt is losing ground.",
    "If you want the rainbow, you have to tolerate the rain.",
    "It takes courage to admit fault.",
    "Keep your eyes open. You never know what you might see.",
    "Love is like wildflowers — it's often found in the most unlikely places.",
    "Nothing is impossible to a willing heart.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Your heart will always make itself known through your words."
  ];
  window.openFortune = function() {
    document.getElementById("fortune-text").textContent = fortunes[Math.floor(Math.random() * fortunes.length)];
  };
})();
</script>

---

## 😄 Dad Jokes

<div id="jokes-tool" style="text-align:center; margin:1em 0;" markdown>

<div id="joke-text" style="font-size:1.1em; padding:20px; background:#f0f8ff; border-radius:8px; min-height:60px; display:flex; align-items:center; justify-content:center;">Click for a dad joke</div>
<button onclick="tellJoke()" style="padding:12px 24px; font-size:16px; margin-top:12px; cursor:pointer; border-radius:6px; border:1px solid #888; background:#fff;">😄 Tell Me a Joke</button>

</div>

<script>
(function() {
  const jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "I used to hate facial hair, but then it grew on me.",
    "What do you call a fake noodle? An impasta!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "I'm on a seafood diet. I see food and I eat it.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why can't a nose be 12 inches long? Because then it would be a foot!",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "Why do chicken coops only have two doors? Because if they had four, they'd be chicken sedans!",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "What do you call a dog that does magic tricks? A Labracadabrador!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "I just watched a program about beavers. It was the best dam program I've ever seen.",
    "What did the grape say when it got stepped on? Nothing, it just let out a little wine.",
    "Why did the math book look so sad? Because of all its problems."
  ];
  window.tellJoke = function() {
    document.getElementById("joke-text").textContent = jokes[Math.floor(Math.random() * jokes.length)];
  };
})();
</script>
