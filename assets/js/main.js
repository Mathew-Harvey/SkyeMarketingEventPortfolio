/* Skye Harvey — portfolio. No dependencies, no build step. */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  /* --- page-load sequence: hand each staggered element its index --- */
  var steps = document.querySelectorAll('.stagger');
  for (var i = 0; i < steps.length; i++) {
    steps[i].style.setProperty('--i', steps[i].getAttribute('data-step') || i + 1);
  }

  /* --- footer year --- */
  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  /* --- mobile nav --- */
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('site-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* --- feed filter by content pillar --- */
  var filters = document.querySelectorAll('.filter');
  var gridEl = document.getElementById('feed-grid');
  var status = document.getElementById('feed-status');

  if (filters.length && gridEl) {
    var tiles = Array.prototype.slice.call(gridEl.querySelectorAll('.tile'));

    Array.prototype.forEach.call(filters, function (button) {
      button.addEventListener('click', function () {
        var want = button.getAttribute('data-filter');
        var shown = 0;

        tiles.forEach(function (tile) {
          var match = want === 'all' || tile.getAttribute('data-pillar') === want;
          tile.classList.toggle('is-hidden', !match);
          if (match) shown++;
        });

        Array.prototype.forEach.call(filters, function (other) {
          var on = other === button;
          other.classList.toggle('is-on', on);
          other.setAttribute('aria-pressed', on ? 'true' : 'false');
        });

        if (status) {
          status.textContent = shown + (shown === 1 ? ' post' : ' posts') + ' shown.';
        }
      });
    });
  }

  /* --- mark the section currently in view in the nav --- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.site-nav a[href^="#"]'));
  if (!links.length || !('IntersectionObserver' in window)) return;

  var byId = {};
  var targets = [];

  links.forEach(function (link) {
    var id = link.getAttribute('href').slice(1);
    var section = document.getElementById(id);
    if (!section) return;
    byId[id] = link;
    targets.push(section);
  });

  var visible = {};

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      visible[entry.target.id] = entry.isIntersecting;
    });

    var current = null;
    for (var j = 0; j < targets.length; j++) {
      if (visible[targets[j].id]) { current = targets[j].id; break; }
    }

    links.forEach(function (link) { link.removeAttribute('aria-current'); });
    if (current && byId[current]) byId[current].setAttribute('aria-current', 'true');
  }, { rootMargin: '-88px 0px -55% 0px', threshold: 0 });

  targets.forEach(function (section) { observer.observe(section); });
})();
