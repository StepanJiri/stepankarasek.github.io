---
layout: default
title: Filming Map
permalink: /map/
hide_rss: true
---

<h1>Filming Map</h1>

<p>Places I've recorded a video. Tap a pin to see which one.</p>

<div id="filming-map" class="filming-map"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
<script>
(function () {
  var spots = {{ site.data.filming_spots | jsonify }};
  var container = document.getElementById('filming-map');
  if (!container || !window.L || !spots || !spots.length) return;

  var map = L.map(container).setView([spots[0].lat, spots[0].lng], 6);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors'
  }).addTo(map);

  var bounds = [];

  spots.forEach(function (spot) {
    var marker = L.circleMarker([spot.lat, spot.lng], {
      radius: 9,
      color: '#ff9640',
      weight: 2,
      fillColor: '#ff9640',
      fillOpacity: 0.9
    }).addTo(map);

    bounds.push([spot.lat, spot.lng]);

    var fetched = false;
    marker.bindPopup('Loading…');

    marker.on('click', function () {
      if (fetched) return;
      fetched = true;

      fetch('https://www.youtube.com/oembed?url=' + encodeURIComponent(spot.youtube) + '&format=json')
        .then(function (res) { return res.json(); })
        .then(function (data) {
          var html = '<div class="map-popup">' +
            (data.thumbnail_url ? '<img src="' + data.thumbnail_url + '" alt="">' : '') +
            '<p class="map-popup-title">' + data.title + '</p>' +
            (data.author_name ? '<p class="map-popup-author">' + data.author_name + '</p>' : '') +
            '<a href="' + spot.youtube + '" target="_blank" rel="noopener">Watch on YouTube</a>' +
            '</div>';
          marker.setPopupContent(html);
        })
        .catch(function () {
          marker.setPopupContent('<a href="' + spot.youtube + '" target="_blank" rel="noopener">Watch on YouTube</a>');
        });
    });
  });

  if (bounds.length > 1) {
    map.fitBounds(bounds, { padding: [30, 30] });
  }
})();
</script>
