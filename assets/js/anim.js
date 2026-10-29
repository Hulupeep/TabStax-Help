// Plays .hs-anim figures once when they scroll into view. Reduced motion: never plays.
(function () {
  var figures = document.querySelectorAll('[data-hs-anim]');
  if (!figures.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function play(fig) {
    fig.classList.remove('is-playing');
    void fig.getBoundingClientRect();
    fig.classList.add('is-playing');
  }
  figures.forEach(function (fig) {
    fig.classList.add('has-js');
    var btn = fig.querySelector('.hs-anim__replay');
    if (btn) btn.addEventListener('click', function () { play(fig); });
  });
  if (reduce) return;
  if (!('IntersectionObserver' in window)) { figures.forEach(play); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { play(e.target); io.unobserve(e.target); }
    });
  }, { threshold: 0.35 });
  figures.forEach(function (fig) { io.observe(fig); });
})();
