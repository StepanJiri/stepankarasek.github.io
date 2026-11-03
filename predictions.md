---
layout: default
title: Predictions
permalink: /predictions/
hide_rss: true
---

# Predictions

<p>My long-term predictions. I'll come back and check how they aged.</p>

<!--
HOW TO ADD A PREDICTION: copy one whole <div class="prediction"> ... </div> block below,
paste it above or below the others, then change:
  - data-date="YYYY-MM-DD" on the first line: the day you want to check it.
    The page shows that date and a countdown in days under the title, automatically.
    Delete data-date if you don't want them.
  - the title (inside <h2>)
  - the small text (inside <p class="prediction-sub">)
  - the text under it. Write it as normal markdown (bold, links, lists all work).
Keep the blank lines around the text, and keep markdown="1" on the inner div.
-->

<div class="prediction" data-date="2027-11-03">
  <div class="prediction-head">
    <div class="prediction-titles">
      <h2>Next MacBook Air redesign includes touchscreen</h2>
      <p class="prediction-sub">this is a test</p>
    </div>
  </div>
  <div class="prediction-body" markdown="1">


  </div>
</div>

<div class="prediction" data-date="2031-11-03">
  <div class="prediction-head">
    <div class="prediction-titles">
      <h2>Second example title</h2>
      <p class="prediction-sub">Another small line</p>
    </div>
  </div>
  <div class="prediction-body" markdown="1">

Another prediction goes here.

  </div>
</div>

<script>
(function () {
  function daysLeft(target) {
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    var days = Math.round((target - today) / 86400000);
    if (days > 1) return days + ' days left';
    if (days === 1) return '1 day left';
    if (days === 0) return 'Check it today';
    return 'Time to check it';
  }

  document.querySelectorAll('.prediction[data-date]').forEach(function (el) {
    var parts = el.getAttribute('data-date').split('-');
    if (parts.length !== 3) return;
    var target = new Date(+parts[0], +parts[1] - 1, +parts[2]);
    if (isNaN(target.getTime())) return;

    var head = el.querySelector('.prediction-head');
    var side = el.querySelector('.prediction-side');
    if (!head) return;
    if (!side) {
      side = document.createElement('div');
      side.className = 'prediction-side';
      head.appendChild(side);
    }

    if (!side.querySelector('.prediction-date')) {
      var when = document.createElement('span');
      when.className = 'prediction-date';
      when.textContent = target.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
      side.appendChild(when);
    }

    var count = document.createElement('span');
    count.className = 'prediction-countdown';
    count.textContent = daysLeft(target);
    side.appendChild(count);
  });
})();
</script>
