import os

HERE = os.path.dirname(os.path.abspath(__file__))
PROPOSAL_SRC = os.path.join(HERE, "..", "..", "proposal", "_src")


def asset(name):
    with open(os.path.join(PROPOSAL_SRC, name), encoding="utf-8") as handle:
        return handle.read().strip()


LOGO = asset("hp.b64")
COVER = asset("cover.b64")
CLOSE = asset("close.b64")

HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="A three-month social media bridge proposal for the Ardmore Development Authority.">
<title>Ardmore Social Media Bridge | October–December 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;1,400&display=swap" rel="stylesheet">
<style>
/*
THESIS: Show two plausible futures for the same three-month bridge; refuse a dense contract memo.
OWN-WORLD: Inherit the proposal's sage/cream/ink palette, serif headlines, sans support, and hard-edged panels.
STORY: Context -> momentum tradeoff -> two packages -> direct comparison -> authorization.
FIRST VIEWPORT: Dark photographic cover, outcome-led headline, proposal label, recipient, and date.
FORM: Two-futures split, assigned candidate 6 from concept seed 812d7577.
*/
:root{--cream:#F2EFE8;--ink:#1A1A18;--soft:#3D3D38;--sage:#7A9E7E;--sage-light:#B8D0BB;--wash:#EAF0EB;--white:#FAFAF7;--rule:rgba(26,26,24,.14);--serif:'Playfair Display',Georgia,serif;--sans:'DM Sans',system-ui,sans-serif}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-snap-type:y mandatory}
body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--sans);font-weight:300;-webkit-font-smoothing:antialiased}
.slide{position:relative;min-height:100svh;padding:clamp(52px,7vw,96px) clamp(28px,8vw,120px);display:flex;flex-direction:column;justify-content:center;overflow:hidden;background:var(--white);scroll-snap-align:start}
.slide:before{content:'';position:absolute;inset:0;background-image:radial-gradient(circle,rgba(26,26,24,.075) 1px,transparent 1px);background-size:24px 24px;pointer-events:none}
.slide>*{position:relative;z-index:1}
.dark{background:var(--ink);color:var(--cream)}
.dark:before{background-image:radial-gradient(circle,rgba(242,239,232,.09) 1px,transparent 1px)}
.sage{background:var(--wash)}
.cover{justify-content:space-between;background:linear-gradient(to top,rgba(26,26,24,.95),rgba(26,26,24,.76) 55%,rgba(122,158,126,.34)),url('data:image/jpeg;base64,__COVER__') center/cover no-repeat;color:var(--cream)}
.cover:before,.closing:before{display:none}
.closing{background:linear-gradient(rgba(26,26,24,.91),rgba(26,26,24,.96)),url('data:image/jpeg;base64,__CLOSE__') center/cover no-repeat;color:var(--cream)}
.fit{width:100%;max-width:1060px;margin:0 auto}
.fit-narrow{max-width:900px}
.eyebrow{margin:0 0 20px;font-size:10px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;opacity:.52}
.display{margin:0;font-family:var(--serif);font-weight:400;font-size:clamp(40px,6vw,72px);line-height:1.06;letter-spacing:-.025em}
.display-sm{margin:0;font-family:var(--serif);font-weight:400;font-size:clamp(30px,4.2vw,50px);line-height:1.13;letter-spacing:-.02em}
.display em,.display-sm em{font-style:italic;color:var(--sage)}
.dark .display em,.dark .display-sm em,.cover em,.closing em{color:var(--sage-light)}
.lede{max-width:760px;margin:22px 0 0;font-size:clamp(15px,1.5vw,18px);line-height:1.68;opacity:.78}
.rule{width:48px;height:2px;margin:28px 0;background:var(--sage)}
.dark .rule{background:var(--sage-light)}
.cover-logo{height:24px;width:auto;align-self:flex-start;filter:invert(1);opacity:.68}
.cover-bottom{padding-top:32px}
.cover-label{font-size:10px;letter-spacing:.18em;text-transform:uppercase;opacity:.55}
.cover-title{margin-top:8px;font-family:var(--serif);font-size:23px}
.cover-date{margin-top:6px;font-size:11px;letter-spacing:.12em;opacity:.55}
.footer{position:absolute;left:clamp(28px,8vw,120px);right:clamp(28px,8vw,120px);bottom:25px;display:flex;align-items:center;justify-content:space-between;font-size:9px;letter-spacing:.12em;text-transform:uppercase;opacity:.34}
.footer img{height:16px;opacity:.55}
.dark .footer img,.closing .footer img{filter:invert(1)}
.timeline{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:42px}
.moment{background:var(--cream);padding:30px 28px;min-height:180px;border-top:3px solid transparent}
.moment.now{border-color:var(--sage);background:var(--ink);color:var(--cream)}
.moment-date{font-family:var(--serif);font-size:25px;color:var(--sage)}
.moment.now .moment-date{color:var(--sage-light)}
.moment-title{margin-top:14px;font-size:15px;font-weight:500}
.moment-body{margin-top:7px;font-size:12.5px;line-height:1.55;opacity:.65}
.choice-grid{display:grid;grid-template-columns:1fr 1fr;gap:2px;margin-top:40px}
.future{padding:42px 38px;background:var(--cream);min-height:350px;display:flex;flex-direction:column}
.future.featured{background:var(--ink);color:var(--cream)}
.future-kicker{font-size:10px;font-weight:500;letter-spacing:.17em;text-transform:uppercase;opacity:.48}
.future-name{margin:16px 0 0;font-family:var(--serif);font-size:34px;line-height:1.1}
.future-name em{color:var(--sage);font-style:italic}
.featured .future-name em{color:var(--sage-light)}
.future-list{list-style:none;margin:26px 0 0;padding:0}
.future-list li{padding:12px 0 12px 22px;border-top:1px solid var(--rule);font-size:13.5px;line-height:1.5;position:relative;opacity:.78}
.future-list li:before{content:'—';position:absolute;left:0;color:var(--sage)}
.featured .future-list li{border-color:rgba(242,239,232,.16)}
.featured .future-list li:before{color:var(--sage-light)}
.momentum-note{margin-top:24px;padding:19px 22px;border-top:2px solid var(--sage);background:var(--wash);max-width:980px;font-size:14px;line-height:1.65}
.price-head{display:flex;align-items:end;justify-content:space-between;gap:30px;margin-bottom:34px}
.price{font-family:var(--serif);font-size:clamp(45px,6vw,72px);line-height:.96;white-space:nowrap}
.price small{display:block;margin-top:9px;font-family:var(--sans);font-size:11px;font-weight:400;letter-spacing:.12em;text-transform:uppercase;opacity:.48}
.package-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:42px;align-items:start}
.deliverables{list-style:none;padding:0;margin:0}
.deliverables li{position:relative;padding:15px 0 15px 28px;border-top:1px solid var(--rule);font-size:15px;line-height:1.5}
.deliverables li:before{content:'↗';position:absolute;left:0;color:var(--sage)}
.dark .deliverables li{border-color:rgba(242,239,232,.17)}
.dark .deliverables li:before{color:var(--sage-light)}
.scope-box{padding:30px;background:var(--cream)}
.dark .scope-box{background:rgba(242,239,232,.07)}
.scope-box h3{font-family:var(--serif);font-size:22px;font-weight:400;margin:0 0 18px}
.scope-box p{font-size:13px;line-height:1.65;margin:0 0 13px;opacity:.72}
.tag{display:inline-block;padding:6px 10px;background:var(--sage);color:white;font-size:9px;font-weight:500;letter-spacing:.13em;text-transform:uppercase}
.dark .tag{background:var(--sage-light);color:var(--ink)}
.compare{margin-top:34px;border-top:1px solid var(--rule)}
.compare-row{display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:0;border-bottom:1px solid var(--rule)}
.compare-row>div{padding:16px 20px;font-size:13px;line-height:1.45}
.compare-row>div:first-child{padding-left:0;font-weight:500}
.compare-head{font-size:9px!important;font-weight:500!important;letter-spacing:.13em;text-transform:uppercase;opacity:.5}
.compare-row>div:last-child{background:var(--wash)}
.compare-row.price-row>div{font-family:var(--serif);font-size:22px}
.recommended{color:var(--sage);font-size:9px;font-family:var(--sans);letter-spacing:.12em;text-transform:uppercase;display:block;margin-top:5px}
.decision{display:grid;grid-template-columns:1fr 390px;gap:54px;align-items:center}
.decision-card{padding:38px;background:rgba(242,239,232,.07);border-top:3px solid var(--sage-light)}
.decision-card h3{margin:0;font-family:var(--serif);font-size:28px;font-weight:400}
.decision-card p{font-size:13px;line-height:1.65;opacity:.7;margin:16px 0 0}
.decision-meta{margin-top:26px;padding-top:18px;border-top:1px solid rgba(242,239,232,.18);display:grid;gap:10px;font-size:11px;letter-spacing:.04em;opacity:.6}
.fineprint{margin-top:22px;font-size:11px;line-height:1.55;opacity:.48}
[data-reveal]{opacity:0;transform:translateY(24px);transition:opacity .85s cubic-bezier(.16,1,.3,1),transform .85s cubic-bezier(.16,1,.3,1)}
[data-reveal].visible{opacity:1;transform:none}
[data-delay='1']{transition-delay:.12s}[data-delay='2']{transition-delay:.24s}[data-delay='3']{transition-delay:.36s}
@media(max-width:760px){html{scroll-snap-type:none}.slide{min-height:auto;padding:66px 24px 76px}.cover{min-height:100svh}.timeline,.choice-grid,.package-grid,.decision{grid-template-columns:1fr}.price-head{display:block}.price{margin-top:24px}.compare-row{grid-template-columns:1fr 1fr}.compare-row>div:first-child{grid-column:1/-1;padding:14px 0 6px}.compare-row>div:nth-child(2),.compare-row>div:nth-child(3){padding:9px 10px 14px}.compare-row:first-child>div:first-child{display:none}.footer{left:24px;right:24px}.future{min-height:0}.decision-card{margin-top:10px}}
@media(max-height:800px) and (min-width:761px){.slide{padding-top:46px;padding-bottom:54px}.footer{bottom:16px}.choice-grid{margin-top:24px}.future{min-height:286px;padding:28px 34px}.future-name{margin-top:10px;font-size:30px}.future-list{margin-top:16px}.future-list li{padding-top:8px;padding-bottom:8px}.momentum-note{margin-top:14px;padding:11px 18px;font-size:12.5px}.price-head{margin-bottom:18px}.deliverables li{padding-top:8px;padding-bottom:8px;font-size:13.5px}.scope-box{padding:24px}.scope-box p{margin-bottom:9px;line-height:1.5}.compare{margin-top:22px}.compare-row>div{padding-top:10px;padding-bottom:10px}.compare-row.price-row>div{font-size:19px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}[data-reveal]{opacity:1!important;transform:none!important;transition:none!important}}
@media print{html{scroll-snap-type:none}.slide{min-height:100vh;break-after:page}[data-reveal]{opacity:1!important;transform:none!important}}
</style>
</head>
<body>
<main>
<section class="slide cover">
  <img class="cover-logo" src="data:image/png;base64,__LOGO__" alt="Hallpass Digital" data-reveal>
  <div class="fit" style="margin:0">
    <p class="eyebrow" data-reveal>October–December 2026 · Social Media Bridge</p>
    <h1 class="display" data-reveal data-delay="1">Keep the momentum<br><em>moving.</em></h1>
    <p class="lede" data-reveal data-delay="2">Two ways to carry Ardmore Means More through the end of the year—without adding another shoot.</p>
  </div>
  <div class="cover-bottom" data-reveal data-delay="3">
    <div class="cover-label">Prepared for</div>
    <div class="cover-title">Ardmore Development Authority</div>
    <div class="cover-date">September 2026</div>
  </div>
</section>

<section class="slide sage">
  <div class="fit fit-narrow">
    <p class="eyebrow" data-reveal>Why a bridge now</p>
    <h2 class="display-sm" data-reveal data-delay="1">The larger plan is moving toward January.<br>The audience <em>shouldn’t have to wait.</em></h2>
    <div class="timeline" data-reveal data-delay="2">
      <article class="moment"><div class="moment-date">Sept. 30</div><div class="moment-title">Current agreement ends</div><div class="moment-body">Al completes the final scheduled shooting trip this month.</div></article>
      <article class="moment now"><div class="moment-date">Nov.</div><div class="moment-title">Board retreat</div><div class="moment-body">The broader 2027 program moves through executive committee and full-board discussion.</div></article>
      <article class="moment"><div class="moment-date">Jan. 1</div><div class="moment-title">New program target</div><div class="moment-body">The next full scope begins after approval and final definition.</div></article>
    </div>
    <p class="momentum-note" data-reveal data-delay="3"><strong>The decision now isn’t the full 2027 plan.</strong> It’s whether Ardmore stays present while that plan moves through approval.</p>
  </div>
  __FOOT2__
</section>

<section class="slide">
  <div class="fit">
    <p class="eyebrow" data-reveal>Two possible futures</p>
    <h2 class="display-sm" data-reveal data-delay="1">Both prevent silence.<br>Only one preserves the <em>current cadence.</em></h2>
    <div class="choice-grid">
      <article class="future" data-reveal data-delay="2">
        <div class="future-kicker">Focused Bridge</div>
        <h3 class="future-name">Keep a <em>visible pulse.</em></h3>
        <ul class="future-list"><li>Two polished videos each month: one development, one tourism</li><li>Plug-and-play templates for timely ADA posts</li><li>ADA handles ad-hoc publishing and day-to-day engagement</li><li>A deliberate reduction in reach, repetition and creative learning</li></ul>
      </article>
      <article class="future featured" data-reveal data-delay="3">
        <div class="future-kicker">Momentum Continuity · Recommended</div>
        <h3 class="future-name">Keep the program <em>working.</em></h3>
        <ul class="future-list"><li>Current platform cadence remains intact</li><li>Full publishing, optimization and engagement</li><li>Continuous performance learning</li><li>A stronger starting position in January</li></ul>
      </article>
    </div>
    <p class="momentum-note" data-reveal><strong>Focused Bridge keeps Ardmore visible, but it does not preserve the current growth capacity.</strong> Fewer well-produced posts mean fewer chances to reach new people, reinforce the brand and learn what works. While results are never guaranteed, reducing the cadence is likely to slow the momentum Ardmore Means More has developed.</p>
  </div>
  __FOOT3__
</section>

<section class="slide sage">
  <div class="fit">
    <div class="price-head">
      <div><p class="eyebrow" data-reveal>Option 01 · Focused Bridge</p><h2 class="display-sm" data-reveal data-delay="1">A focused cadence<br>with a <em>clear job to do.</em></h2></div>
      <div class="price" data-reveal data-delay="2">$16,500<small>$5,500 per month · three months</small></div>
    </div>
    <div class="package-grid">
      <ul class="deliverables" data-reveal data-delay="2">
        <li><strong>Two short-form videos per month</strong>—one development story and one tourism story; six total</li>
        <li>Development stories may feature properties, infrastructure, investment, workforce or growth</li>
        <li>Tourism stories may feature attractions, events, local businesses or experiences</li>
        <li>Editing from footage captured during the final September shoot</li>
        <li>Captions and publishing across TikTok, Instagram Reels, Facebook and YouTube Shorts</li>
        <li>Plug-and-play templates for available properties, development updates and timely tourism or event content—plus a practical handoff so ADA can publish ad-hoc posts</li>
        <li>A monthly performance snapshot</li>
      </ul>
      <aside class="scope-box" data-reveal data-delay="3"><span class="tag">Focused bridge</span><h3>What changes</h3><p>Hall Pass maintains a scheduled video presence. ADA uses the new templates for ad-hoc static posts and manages day-to-day community engagement.</p><p>This is intentionally narrower than the current program. It maintains a credible presence, but the lower frequency is likely to slow reach, follower growth and performance learning.</p><p><strong>No new travel or shooting is included.</strong></p></aside>
    </div>
  </div>
  __FOOT4__
</section>

<section class="slide dark">
  <div class="fit">
    <div class="price-head">
      <div><p class="eyebrow" data-reveal>Option 02 · Momentum Continuity</p><h2 class="display-sm" data-reveal data-delay="1">Carry the current program<br><em>all the way into January.</em></h2></div>
      <div class="price" data-reveal data-delay="2">$24,500<small>Exact three-month proration</small></div>
    </div>
    <div class="package-grid">
      <ul class="deliverables" data-reveal data-delay="2">
        <li>Instagram: <strong>4–6 posts per month</strong></li>
        <li>TikTok: <strong>4–6 videos per month</strong></li>
        <li>Facebook: <strong>4–6 posts per month</strong></li>
        <li>LinkedIn: <strong>4 posts per month</strong></li>
        <li>YouTube Shorts, earned-media reposts and cross-platform adaptations</li>
        <li>Full scheduling, publishing, engagement optimization, reporting and monthly check-ins</li>
      </ul>
      <aside class="scope-box" data-reveal data-delay="3"><span class="tag">Recommended</span><h3>Why this price</h3><p>The existing agreement assigns <strong>$98,000 annually</strong> to social media content and management.</p><p>Three months is exactly one quarter of that line item: <strong>$24,500</strong>.</p><p>Content is produced from the existing footage library. <strong>No new travel, shooting or long-form campaign video is included.</strong></p></aside>
    </div>
  </div>
  __FOOT5__
</section>

<section class="slide">
  <div class="fit">
    <p class="eyebrow" data-reveal>Side by side</p>
    <h2 class="display-sm" data-reveal data-delay="1">Choose the bridge that matches<br>the outcome you want in <em>January.</em></h2>
    <div class="compare" data-reveal data-delay="2">
      <div class="compare-row"><div class="compare-head">Scope</div><div class="compare-head">Focused Bridge</div><div class="compare-head">Momentum Continuity</div></div>
      <div class="compare-row"><div>Video cadence</div><div>2 per month: 1 development + 1 tourism</div><div>4–6 per month</div></div>
      <div class="compare-row"><div>Supporting platform posts</div><div>Included videos only</div><div>Full current cadence</div></div>
      <div class="compare-row"><div>Ad-hoc content</div><div>Templates + ADA publishing</div><div>Created and managed within the full content mix</div></div>
      <div class="compare-row"><div>Account management</div><div>Limited to included videos</div><div>Full publishing + optimization</div></div>
      <div class="compare-row"><div>Reporting</div><div>Monthly snapshot</div><div>Monthly report + check-in</div></div>
      <div class="compare-row"><div>New travel or shooting</div><div>None</div><div>None</div></div>
      <div class="compare-row price-row"><div>October–December total</div><div>$16,500</div><div>$24,500<span class="recommended">For $8,000 more, maintain the current program</span></div></div>
    </div>
  </div>
  __FOOT6__
</section>

<section class="slide closing">
  <div class="fit decision">
    <div>
      <p class="eyebrow" data-reveal>The recommendation</p>
      <h2 class="display" data-reveal data-delay="1">Enter January with the<br><em>strongest possible hand.</em></h2>
      <p class="lede" data-reveal data-delay="2">Momentum Continuity preserves the cadence, account management and performance learning already producing results while the broader program is finalized. Focused Bridge remains a credible lower-cost path when budget is the deciding constraint.</p>
    </div>
    <aside class="decision-card" data-reveal data-delay="3">
      <span class="tag">Decision requested</span>
      <h3>Authorize one bridge option.</h3>
      <p>Either option runs October 1 through December 31, 2026, then concludes unless incorporated into a new agreement.</p>
      <div class="decision-meta"><span>Board consideration · September 21</span><span>Work begins · October 1</span><span>Broader program target · January 1</span></div>
      <p class="fineprint">This bridge is separate from the 2027 Chamber–ADA–ATA proposal and includes no new travel or production shoots.</p>
    </aside>
  </div>
  __FOOT7__
</section>
</main>
<script>
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting)entry.target.classList.add('visible')}),{threshold:.12});
document.querySelectorAll('[data-reveal]').forEach(el=>observer.observe(el));
const slides=[...document.querySelectorAll('.slide')];
function current(){let best=0,dist=Infinity;slides.forEach((s,i)=>{const d=Math.abs(s.getBoundingClientRect().top);if(d<dist){dist=d;best=i}});return best}
addEventListener('keydown',e=>{let delta=0;if(['ArrowRight','ArrowDown','PageDown'].includes(e.key)||(e.key===' '&&!e.shiftKey))delta=1;if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)||(e.key===' '&&e.shiftKey))delta=-1;if(delta){e.preventDefault();slides[Math.max(0,Math.min(slides.length-1,current()+delta))].scrollIntoView({behavior:'smooth'})}});
</script>
</body>
</html>'''


def footer(number):
    return (
        '<div class="footer"><span>Ardmore Social Media Bridge</span>'
        '<img src="data:image/png;base64,%s" alt="Hallpass Digital">'
        '<span>%02d / 07</span></div>' % (LOGO, number)
    )


HTML = HTML.replace("__LOGO__", LOGO).replace("__COVER__", COVER).replace("__CLOSE__", CLOSE)
for number in range(2, 8):
    HTML = HTML.replace("__FOOT%d__" % number, footer(number))

output = os.path.join(HERE, "..", "index.html")
with open(output, "w", encoding="utf-8") as handle:
    handle.write(HTML)
print(output)
