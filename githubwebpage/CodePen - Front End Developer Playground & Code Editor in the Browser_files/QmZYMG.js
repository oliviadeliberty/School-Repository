;(function(){

  console.log('made by the @keyframers');
  console.log('http://twitter.com/keyframers');
  console.log('http://twitch.tv/keyframers');

  var el = document.querySelector('[data-keyframers-credit]');

  if ( el ) {

    el.insertAdjacentHTML('beforeend', `
<div class="kf_credit">
<span>Watch the @keyframers</span>
<div class="kf_faces">
<svg class="kf_face -shaw" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 356">
<path fill="#bf3c26" d="M323.5 177.8L172 19.6 20.4 177.8 172 336l151.5-158.2z"/>
<clipPath id="a">
<path d="M323.5 177.8L172 19.6 20.4 177.8 172 336l151.5-158.2z"/>
</clipPath>
<g clip-path="url(#a)">
<circle cx="173" cy="135.9" r="100" fill="#f7bb9a"/>
<path fill="#bf3c26" d="M.1-29h343.7v152.7H.1z"/>
<circle cx="203.4" cy="176.9" r="14"/>
<circle cx="140.5" cy="176.9" r="14"/>
<path fill="#fff" fill-opacity=".1" d="M293 177.8L173 52.6V303l120-125.2z"/>
</g>
<path fill="none" stroke="#000" stroke-width="21.6" d="M323.5 177.8L172 19.6 20.4 177.8 172 336l151.5-158.2z"/>
</svg>

<svg class="kf_face -david" viewBox="230 0 340 356">
<path fill="#e1b39a" d="M555.6 177.8L404 19.6 252.5 177.8 404 336l151.6-158.2z"/>
<clipPath id="b">
<path d="M555.6 177.8L404 19.6 252.5 177.8 404 336l151.6-158.2z"/>
</clipPath>
<g clip-path="url(#b)">
<circle cx="404" cy="134.9" r="100" fill="#f7bb9a"/>
<path fill="#3e3430" d="M230.5-29h343.7v152.7H230.5z"/>
<ellipse cx="433.8" cy="176.9" rx="14" ry="14"/>
<ellipse cx="370.9" cy="176.9" rx="14" ry="14"/>
<path fill="#fff" fill-opacity=".1" d="M524 177.8L404 52.6V303l120-125.2z"/>
</g>
<path fill="none" stroke="#000" stroke-width="21.6" d="M555.6 177.8L404 19.6 252.5 177.8 404 336l151.6-158.2z"/>
</svg>
</div>
<span>code this pen live!</span>
</div>`);

    document.head.insertAdjacentHTML('beforeend',`<style>
.kf_credit {
position: fixed;
bottom: 0.5em;
left: 0;
right: 0;
z-index: 999;
font-size: 10px;
width: 100%;
visibility: hidden;
display: flex;
justify-content: center;
align-items: center;
font-family: monospace;
text-align: center;
transition: all 0.4s cubic-bezier(.84,.01,.14,.98);
animation: kf_slide-in 0.8s cubic-bezier(.06,.44,0,.98) 0.4s both;
}
@keyframes kf_slide-in { from { transform: translateY(100%); opacity: 0; } }
.kf_credit > * { visibility: visible; }

.kf_faces { 
position: relative;
width: 6em;
height: 3em;
perspective: 400px;
transform-style: preserve-3d;
}

.kf_face {
width: 50%;
position: absolute;
top: 0; right: 0.5em; bottom: 0; left: 0.5em;
margin: auto;
transition: transform 0.4s cubic-bezier(.84,.01,.14,.98);
}
.kf_face.\-shaw { right: auto; }
.kf_face.\-david { left: auto; transition-delay: 0.1s; z-index: 4; transform: translateZ(10px) rotateY(0deg) ; }

.kf_credit:hover .kf_face {
transform: rotateY(360deg);
}
.kf_credit:hover .kf_face.\-david {
transform: translateZ(10px) rotateY(360deg);
}
</style>`); 

    el.onclick = function(){
      if ( ga ) {
        var url = this.getAttribute('href');
        ga('send', 'event', 'keyframers', 'click', url, {
          'transport': 'beacon',
          'hitCallback': function(){ window.open(url); }
        });
        return false;
      }
    };

  }

})();


(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-6412794-6', 'auto');
ga('send', 'pageview');
ga('send', 'event', 'keyframers');