---
layout: post
title: "Dylan"
date: 2026-09-30 19:57:00 +0200
---

In case you don't know, I am a huge Dylan fan. If you aren't familiar with his work, this is the [place](https://music.apple.com/cz/album/highway-61-revisited/201281514) to start.

<iframe 
  id="dylan-album-embed"
  height="150" 
  style="width: 100%; max-width: 660px; border-radius: 12px; border: none;" 
  allow="autoplay *; encrypted-media *;">
</iframe>

<script>
(function() {
  const baseUrl = "https://embed.music.apple.com/cz/album/highway-61-revisited/201281514";
  const frame = document.getElementById('dylan-album-embed');
  const mq = window.matchMedia('(prefers-color-scheme: dark)');

  function setTheme(isDark) {
    frame.src = baseUrl + (isDark ? '?theme=dark' : '?theme=light');
  }

  setTheme(mq.matches);
  mq.addEventListener('change', e => setTheme(e.matches));
})();
</script>
