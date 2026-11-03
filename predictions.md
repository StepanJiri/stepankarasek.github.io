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
    This turns on the countdown and the "Add to calendar" button.
    Delete data-date if you want neither.
  - the title (inside <h2>)
  - the small text (inside <p class="prediction-sub">)
  - the box on the right (inside <span class="prediction-date">). Any text works,
    or delete the whole <span> if you don't want a box.
  - the text under it. Write it as normal markdown (bold, links, lists all work).
Keep the blank lines around the text, and keep markdown="1" on the inner div.
-->

<div class="prediction" data-date="2027-11-03">
  <div class="prediction-head">
    <div class="prediction-titles">
      <h2>Next MacBook Air redesign includes touchscreen</h2>
      <p class="prediction-sub"></p>
    </div>
    <div class="prediction-side">
      <span class="prediction-date">3 Nov 2026</span>
    </div>
  </div>
  <div class="prediction-body" markdown="1">

Write your prediction here. This is **normal markdown**, so you can use [links](https://rubiconrevisited.com), lists and more.

  </div>
</div>

<div class="prediction" data-date="2031-11-03">
  <div class="prediction-head">
    <div class="prediction-titles">
      <h2>Second example title</h2>
      <p class="prediction-sub">Another small line</p>
    </div>
    <div class="prediction-side">
      <span class="prediction-date">3 Nov 2026</span>
    </div>
  </div>
  <div class="prediction-body" markdown="1">

Another prediction goes here.

  </div>
</div>

<script>
(function () {
  function pad(n) { return (n < 10 ? '0' : '') + n; }

  function countdown(target) {
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    if (target.getTime() === today.getTime()) return 'Check it today';
    if (target < today) return 'Time to check it';
    var y = target.getFullYear() - today.getFullYear();
    var m = target.getMonth() - today.getMonth();
    var d = target.getDate() - today.getDate();
    if (d < 0) {
      m--;
      d += new Date(target.getFullYear(), target.getMonth(), 0).getDate();
    }
    if (m < 0) { y--; m += 12; }
    var parts = [];
    if (y > 0) parts.push(y + (y === 1 ? ' year' : ' years'));
    if (m > 0) parts.push(m + (m === 1 ? ' month' : ' months'));
    if (y === 0 && d > 0) parts.push(d + (d === 1 ? ' day' : ' days'));
    return parts.slice(0, 2).join(', ') + ' left';
  }

  function icsText(s) {
    return String(s).replace(/\\/g, '\\\\').replace(/;/g, '\\;').replace(/,/g, '\\,').replace(/\r?\n/g, '\\n');
  }

  function icsDate(dt) {
    return dt.getFullYear() + pad(dt.getMonth() + 1) + pad(dt.getDate());
  }

  function calendarHref(title, target) {
    var next = new Date(target.getFullYear(), target.getMonth(), target.getDate() + 1);
    var now = new Date();
    var stamp = now.getUTCFullYear() + pad(now.getUTCMonth() + 1) + pad(now.getUTCDate()) + 'T' +
      pad(now.getUTCHours()) + pad(now.getUTCMinutes()) + pad(now.getUTCSeconds()) + 'Z';
    var lines = [
      'BEGIN:VCALENDAR',
      'VERSION:2.0',
      'PRODID:-//Rubicon Revisited//Predictions//EN',
      'BEGIN:VEVENT',
      'UID:' + icsDate(target) + '-' + Math.abs(hash(title)) + '@rubiconrevisited.com',
      'DTSTAMP:' + stamp,
      'DTSTART;VALUE=DATE:' + icsDate(target),
      'DTEND;VALUE=DATE:' + icsDate(next),
      'SUMMARY:' + icsText('Check my prediction: ' + title),
      'DESCRIPTION:' + icsText('https://rubiconrevisited.com/predictions/'),
      'END:VEVENT',
      'END:VCALENDAR'
    ];
    return 'data:text/calendar;charset=utf-8,' + encodeURIComponent(lines.join('\r\n'));
  }

  function hash(s) {
    var h = 0;
    for (var i = 0; i < s.length; i++) { h = ((h << 5) - h + s.charCodeAt(i)) | 0; }
    return h;
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

    var title = (el.querySelector('h2') || {}).textContent || 'Prediction';
    title = title.trim();

    var count = document.createElement('span');
    count.className = 'prediction-countdown';
    count.textContent = countdown(target);
    side.appendChild(count);

    var cal = document.createElement('a');
    cal.className = 'prediction-cal';
    cal.href = calendarHref(title, target);
    cal.download = 'prediction-' + icsDate(target) + '.ics';
    cal.textContent = 'Add to calendar';
    side.appendChild(cal);
  });
})();
</script>
