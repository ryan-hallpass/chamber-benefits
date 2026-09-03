import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOGO=open(os.path.join(HERE,'hp.b64')).read()
COVER=open(os.path.join(HERE,'cover.b64')).read()
CLOSE=open(os.path.join(HERE,'close.b64')).read()

CSS = """
:root{--cream:#F2EFE8;--ink:#1A1A18;--ink-soft:#3D3D38;--sage:#7A9E7E;--sage-light:#B8D0BB;
--sage-wash:#EAF0EB;--warm-white:#FAFAF7;--rule:rgba(26,26,24,0.12);
--serif:'Playfair Display',Georgia,serif;--sans:'DM Sans',system-ui,sans-serif;}
*{box-sizing:border-box}
body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--sans);font-weight:300;
-webkit-font-smoothing:antialiased}
.deck{width:100%}
.slide{position:relative;width:100%;min-height:100vh;padding:clamp(40px,7vw,96px) clamp(32px,8vw,120px);
margin-bottom:2px;background:var(--warm-white);overflow:hidden;display:flex;flex-direction:column;justify-content:center}
.slide::before{content:'';position:absolute;inset:0;
background-image:radial-gradient(circle,rgba(26,26,24,0.08) 1px,transparent 1px);
background-size:24px 24px;pointer-events:none}
.slide>*{position:relative;z-index:1}
.slide--dark{background:var(--ink);color:var(--cream)}
.slide--dark::before{background-image:radial-gradient(circle,rgba(242,239,232,0.10) 1px,transparent 1px)}
.slide--sage{background:var(--sage-wash)}
.eyebrow{font-size:10px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;opacity:.5;margin-bottom:20px}
.display{font-family:var(--serif);font-size:clamp(38px,5.5vw,64px);font-weight:400;line-height:1.08;letter-spacing:-.02em;margin:0}
.display em{font-style:italic;color:var(--sage)}
.slide--dark .display em{color:var(--sage-light)}
.display-sm{font-family:var(--serif);font-size:clamp(26px,3.5vw,40px);font-weight:400;line-height:1.15;letter-spacing:-.02em;margin:0}
.display-sm em{font-style:italic;color:var(--sage)}
.slide--dark .display-sm em{color:var(--sage-light)}
.body{font-size:15px;line-height:1.7;font-weight:300;max-width:560px;opacity:.8;margin-top:20px}
.body.wide{max-width:760px}
.rule{width:48px;height:2px;background:var(--sage);margin:28px 0}
.slide--dark .rule{background:var(--sage-light)}
.slide-num{position:absolute;top:28px;right:36px;font-size:11px;letter-spacing:.12em;opacity:.35;z-index:2}
.slide-footer{position:absolute;bottom:28px;left:clamp(32px,8vw,120px);right:clamp(32px,8vw,120px);
display:flex;justify-content:space-between;align-items:center;font-size:10px;letter-spacing:.1em;opacity:.35;z-index:2}
.logo-dark{height:18px;opacity:.4}
.logo-light{height:18px;filter:invert(1);opacity:.4}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:40px}
.two-col-tight{display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-top:32px}
.card-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:40px}
.card{background:var(--cream);padding:32px 28px}
.slide--sage .card{background:var(--warm-white)}
.card-num{font-family:var(--serif);font-size:48px;color:var(--sage);opacity:.7;line-height:1;margin-bottom:14px}
.card-title{font-family:var(--serif);font-size:17px;margin-bottom:10px}
.card-body{font-size:13px;line-height:1.6;font-weight:300;opacity:.7}
.init-list{margin-top:36px;max-width:900px}
.init-row{display:grid;grid-template-columns:74px 1fr;align-items:baseline;gap:8px;
padding:20px 0;border-bottom:1px solid var(--rule)}
.slide--dark .init-row{border-bottom-color:rgba(242,239,232,.18)}
.init-row:last-child{border-bottom:none}
.init-n{font-family:var(--serif);font-size:30px;color:var(--sage);opacity:.75;line-height:1}
.init-t{font-family:var(--serif);font-size:26px;line-height:1.2;letter-spacing:-.01em}
.init-bullets{list-style:none;padding:0;margin:36px 0 0;max-width:820px}
.init-bullets li{font-size:19px;line-height:1.5;font-weight:300;opacity:.85;
padding:15px 0 15px 30px;position:relative;border-bottom:1px solid var(--rule)}
.slide--dark .init-bullets li{border-bottom-color:rgba(242,239,232,.18)}
.init-bullets li:last-child{border-bottom:none}
.init-bullets li::before{content:'';position:absolute;left:0;top:26px;width:14px;height:1px;background:var(--sage)}
.slide--dark .init-bullets li::before{background:var(--sage-light)}
@media (max-width:700px){.init-row{grid-template-columns:52px 1fr}.init-t{font-size:20px}.init-bullets li{font-size:16px}}

.why-grid{margin-top:28px}
.why-grid .card{padding:56px 36px 64px}
.why-grid .card-num{font-size:64px;margin-bottom:28px}
.why-grid .card-title{font-size:26px;margin-bottom:0;line-height:1.2}
.problem-list{list-style:none;margin:32px 0 0;padding:0;display:flex;flex-direction:column;gap:16px;max-width:820px}
.problem-list li{display:flex;align-items:flex-start;gap:16px;font-size:15px;line-height:1.5}
.problem-list li::before{content:'\\2014';color:var(--sage);font-family:var(--serif);flex:0 0 auto}
.phase-list{display:flex;flex-direction:column;margin-top:36px}
.phase-item{display:grid;grid-template-columns:150px 1fr;gap:32px;padding:24px 0;border-top:1px solid var(--rule)}
.phase-item:last-child{border-bottom:1px solid var(--rule)}
.phase-label{font-size:10px;letter-spacing:.14em;text-transform:uppercase;opacity:.4}
.phase-title{font-family:var(--serif);font-size:18px;margin-bottom:6px}
.phase-body{font-size:13px;line-height:1.6;font-weight:300;opacity:.7}
.price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:40px}
.price-grid--two{grid-template-columns:repeat(2,1fr)}
.price-card{background:var(--cream);padding:36px 30px;display:flex;flex-direction:column}
.price-card--featured{background:var(--ink);color:var(--cream)}
.price-tier{font-size:10px;letter-spacing:.18em;text-transform:uppercase;opacity:.5;margin-bottom:16px}
.price-amount{font-family:var(--serif);font-size:36px;line-height:1;margin-bottom:4px}
.price-period{font-size:12px;opacity:.5;margin-bottom:20px}
.price-items{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px}
.price-items li{font-size:12.5px;padding-left:16px;position:relative;line-height:1.5;opacity:.8}
.price-items li::before{content:'\\2197';position:absolute;left:0;color:var(--sage);opacity:.9}
.price-card--featured .price-items li::before{color:var(--sage-light)}
.total-bar{display:flex;justify-content:space-between;align-items:baseline;gap:24px;flex-wrap:wrap;
margin-top:2px;background:var(--sage);color:var(--warm-white);padding:26px 30px}
.total-bar .lbl{font-size:10px;letter-spacing:.18em;text-transform:uppercase;opacity:.75}
.total-bar .amt{font-family:var(--serif);font-size:38px;line-height:1}
.total-bar .sub{font-size:12px;opacity:.8}
.feature-block{background:var(--ink);color:var(--cream);padding:40px 44px;margin-top:8px;position:relative;overflow:hidden}
.feature-block::before{content:'';position:absolute;top:-30px;right:-30px;width:180px;height:180px;
border-radius:50%;background:var(--sage);opacity:.15}
.feature-block>*{position:relative;z-index:1}
.feature-label{font-size:10px;letter-spacing:.18em;text-transform:uppercase;opacity:.5;margin-bottom:14px}
.feature-title{font-family:var(--serif);font-size:24px;line-height:1.2}
.feature-title em{font-style:italic;color:var(--sage-light)}
.feature-body{font-size:13.5px;line-height:1.65;opacity:.75;margin-top:14px}
.metric-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:40px}
.metric{background:var(--cream);padding:28px 32px}
.slide--dark .metric{background:rgba(242,239,232,.07)}
.metric-value{font-family:var(--serif);font-size:40px;line-height:1;margin-bottom:6px}
.slide--dark .metric-value{color:var(--sage-light)}
.metric-label{font-size:11px;opacity:.55;line-height:1.4}
.metric.pending{border:1px dashed var(--sage);background:transparent}
.metric.pending .metric-value{color:var(--sage);opacity:.55;font-size:22px;font-style:italic}
.metric.pending .metric-label{opacity:.5}
.flywheel{display:block;margin:8px auto 0;max-width:620px;width:100%;height:auto}
.fly-wrap{margin-top:34px}
.fly-wrap .flywheel{max-width:660px}
.fw-node{fill:var(--cream);stroke:var(--sage);stroke-width:1.5}
.fw-abbr{font-family:var(--serif);font-size:27px;fill:var(--ink);text-anchor:middle}
.fw-sub{font-family:var(--sans);font-size:10px;font-weight:500;letter-spacing:.09em;
text-transform:uppercase;fill:var(--ink);opacity:.55;text-anchor:middle}
.fw-arc{fill:none;stroke:var(--sage);stroke-width:2}
.fw-mid{font-family:var(--serif);font-style:italic;font-size:19px;fill:var(--sage);text-anchor:middle}
.fw-midsub{font-family:var(--sans);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;
fill:var(--ink);opacity:.4;text-anchor:middle}
.chart{display:block;width:100%;height:auto;margin-top:26px}
.ch-title{font-family:var(--sans);font-size:10px;font-weight:500;letter-spacing:.16em;
text-transform:uppercase;fill:var(--ink);opacity:.45;text-anchor:middle}
.ch-val{font-family:var(--serif);font-size:19px;fill:var(--ink);text-anchor:middle}
.ch-val.up{fill:var(--sage)}
.slide--dark .ch-val{fill:var(--cream)} .slide--dark .ch-val.up{fill:var(--sage-light)}
.slide--dark .ch-title{fill:var(--cream)}
.ch-tick{font-family:var(--sans);font-size:10px;letter-spacing:.1em;fill:var(--ink);opacity:.4;text-anchor:middle}
.slide--dark .ch-tick{fill:var(--cream)}
.ch-delta{font-family:var(--sans);font-size:11px;font-weight:500;letter-spacing:.1em;
text-transform:uppercase;fill:var(--sage);text-anchor:middle}
.slide--dark .ch-delta{fill:var(--sage-light)}
.ch-axis{stroke:var(--ink);opacity:.18;stroke-width:1}
.slide--dark .ch-axis{stroke:var(--cream);opacity:.22}
.ch-grid{stroke:var(--ink);opacity:.08;stroke-width:1}
.slide--dark .ch-grid{stroke:var(--cream);opacity:.12}
.bar-before{fill:var(--ink);opacity:.16}
.slide--dark .bar-before{fill:var(--cream);opacity:.2}
.bar-after{fill:var(--sage)}
.slide--dark .bar-after{fill:var(--sage-light)}
.srcnote{font-size:11px;opacity:.45;margin-top:18px;letter-spacing:.02em}
.clarify{border-left:3px solid var(--sage);padding:14px 0 14px 20px;margin-top:26px;max-width:620px;
font-size:13.5px;line-height:1.6;opacity:.75}
.quote-block{border-left:3px solid var(--sage);padding-left:24px;margin-top:36px;max-width:640px}
.quote-text{font-family:var(--serif);font-size:22px;font-style:italic;line-height:1.45;color:var(--ink-soft)}
.slide--dark .quote-text{color:var(--sage-light)}
.quote-attr{font-size:11px;letter-spacing:.12em;text-transform:uppercase;opacity:.4;margin-top:12px}
.hl{background:var(--sage-light);color:var(--ink);padding:1px 7px;border-radius:2px}
.diagram{display:grid;grid-template-columns:1fr auto 1fr;gap:20px;align-items:center;margin-top:40px}
.dbox{border:1px solid rgba(242,239,232,.22);padding:26px 24px}
.dbox .dt{font-family:var(--serif);font-size:19px;margin-bottom:8px}
.dbox .db{font-size:12.5px;line-height:1.55;opacity:.65}
.dgap{font-size:11px;letter-spacing:.14em;text-transform:uppercase;opacity:.45;text-align:center;white-space:nowrap}
.dresult{border-left:3px solid var(--sage-light);padding:22px 26px;margin-top:22px;background:rgba(242,239,232,.05)}
.cover-hero{position:relative;min-height:100vh;background:url('data:image/jpeg;base64,__COVER__') center/cover no-repeat;
display:flex;flex-direction:column;justify-content:space-between;padding:clamp(48px,7vw,96px) clamp(40px,6vw,80px)}
.cover-hero::before{content:'';position:absolute;inset:0;
background:linear-gradient(to top,rgba(26,26,24,.93) 0%,rgba(26,26,24,.82) 30%,rgba(26,26,24,.62) 62%,rgba(122,158,126,.38) 100%);z-index:0}
.cover-hero>*{position:relative;z-index:1}
.cover-headline{font-family:var(--serif);font-size:clamp(40px,5.6vw,68px);color:var(--cream);line-height:1.05;letter-spacing:-.02em}
.cover-headline em{font-style:italic;color:var(--sage-light)}
.cover-sub{color:var(--cream);opacity:.72;font-size:15px;margin-top:22px;max-width:460px;line-height:1.6}
.cover-bottom-label{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--cream);opacity:.5}
.cover-bottom-title{font-family:var(--serif);font-size:22px;color:var(--cream);margin-top:8px}
.cover-bottom-date{font-size:11px;letter-spacing:.12em;color:var(--cream);opacity:.5;margin-top:6px}
.slide--closing{background:linear-gradient(rgba(26,26,24,.9),rgba(26,26,24,.94)),url('data:image/jpeg;base64,__CLOSE__') center/cover no-repeat}
.slide--closing::before{display:none}
.big-arrow{position:absolute;right:clamp(32px,8vw,120px);bottom:96px;font-family:var(--serif);
font-size:clamp(60px,9vw,120px);color:var(--sage-light);opacity:.22;line-height:1}
[data-reveal]{opacity:0;transform:translateY(36px);
transition:opacity 1.1s cubic-bezier(.16,1,.3,1),transform 1.1s cubic-bezier(.16,1,.3,1)}
[data-reveal].is-visible{opacity:1;transform:translateY(0)}
[data-reveal][data-delay="1"]{transition-delay:.15s}[data-reveal][data-delay="2"]{transition-delay:.35s}
[data-reveal][data-delay="3"]{transition-delay:.55s}[data-reveal][data-delay="4"]{transition-delay:.75s}
[data-reveal][data-delay="5"]{transition-delay:.95s}[data-reveal][data-delay="6"]{transition-delay:1.15s}
[data-reveal][data-delay="7"]{transition-delay:1.35s}
.rule[data-reveal]{transform:none;width:0;transition:opacity 1.1s,width .6s cubic-bezier(.16,1,.3,1)}
.rule[data-reveal].is-visible{width:48px}
.phase-item[data-reveal]{transform:translateX(-16px)}
.phase-item[data-reveal].is-visible{transform:translateX(0)}
.card[data-reveal],.price-card[data-reveal],.metric[data-reveal]{transform:translateY(20px) scale(.97)}
.card[data-reveal].is-visible,.price-card[data-reveal].is-visible,.metric[data-reveal].is-visible{transform:translateY(0) scale(1)}
@media (prefers-reduced-motion:reduce){[data-reveal]{opacity:1!important;transform:none!important;transition:none!important}}
@media (max-width:700px){
.slide{padding:56px 26px;min-height:auto}
.card-grid,.price-grid,.metric-strip,.two-col,.two-col-tight,.diagram{grid-template-columns:1fr}
.diagram{gap:14px}.dgap{transform:rotate(90deg);padding:8px 0}
.phase-item{grid-template-columns:1fr;gap:10px}
.display{font-size:32px}.slide-footer{position:static;margin-top:40px}
.big-arrow{display:none}}
""".replace('__COVER__',COVER).replace('__CLOSE__',CLOSE)

def foot(n):
    light = 'logo-light' if n in DARK else 'logo-dark'
    return ('<div class="slide-num">%02d</div>' % n if n>1 else '') + \
      '<div class="slide-footer"><span>Ardmore Chamber of Commerce</span>' \
      '<img class="%s" src="data:image/png;base64,%s" alt="Hallpass Digital"></div>' % (light,LOGO)

DARK={2,4,12,15}
print('module ready')


# ---------------- CHARTS ----------------
def panel(px, title, v1, v2, l1, l2, delta):
    h2 = 145.0
    h1 = 145.0 * v1 / v2
    y1, y2 = 225 - h1, 225 - h2
    return ('<text class="ch-title" x="%d" y="24">%s</text>'
      '<text class="ch-delta" x="%d" y="52">%s</text>'
      '<line class="ch-axis" x1="%d" y1="225" x2="%d" y2="225"/>'
      '<rect class="bar-before" x="%d" y="%.1f" width="54" height="%.1f" rx="3"/>'
      '<rect class="bar-after" x="%d" y="%.1f" width="54" height="%.1f" rx="3"/>'
      '<text class="ch-val" x="%d" y="%.1f">%s</text>'
      '<text class="ch-val up" x="%d" y="%.1f">%s</text>'
      '<text class="ch-tick" x="%d" y="246">Q1</text>'
      '<text class="ch-tick" x="%d" y="246">Q2</text>') % (
      px+104, title, px+104, delta, px+22, px+186,
      px+50, y1, h1, px+124, y2, h2,
      px+77, y1-11, l1, px+151, y2-11, l2, px+77, px+151)

CHART_GROWTH = ('<svg class="chart" viewBox="0 0 760 262" role="img" aria-label="Quarter one versus quarter two: '
 'video views rose from 391,350 to 813,870, engagements from 20,670 to 42,410, and new followers from about 3,000 to about 6,000.">'
 + panel(0,   'Short-form video views', 391350, 813870, '391,350', '813,870', '&#8593; 108%')
 + panel(253, 'Engagements',            20670,  42410,  '20,670',  '42,410',  '&#8593; 105%')
 + panel(506, 'New followers',          3000,   6000,   '~3,000',  '~6,000',  '&#8593; 100%')
 + '</svg>')

CHART_REACH = ('<svg class="chart" viewBox="0 0 700 118" role="img" '
 'aria-label="Sixty-one percent of reach and engagement comes from outside the immediate Ardmore audience.">'
 '<rect class="bar-after" x="0" y="34" width="426" height="54" rx="3"/>'
 '<rect class="bar-before" x="429" y="34" width="271" height="54" rx="3"/>'
 '<text class="ch-title" x="213" y="22" style="opacity:.55">Outside Ardmore</text>'
 '<text class="ch-title" x="564" y="22" style="opacity:.55">Local audience</text>'
 '<text x="213" y="70" style="font-family:var(--serif);font-size:26px;fill:var(--warm-white);text-anchor:middle">61%</text>'
 '<text x="564" y="70" style="font-family:var(--serif);font-size:26px;fill:var(--ink);opacity:.5;text-anchor:middle">39%</text>'
 '<text class="ch-tick" x="213" y="110" style="opacity:.5">Dallas &#183; Oklahoma City &#183; beyond</text>'
 '</svg>')

PTS=[(60,252.1),(171.7,214.3),(283.3,205.6),(395,168.3),(506.7,130.6),(618.3,93.4),(730,56.1)]
def pth(a,b): return ' '.join(('M' if i==a else 'L')+'%.1f %.1f'%PTS[i] for i in range(a,b+1))
grid=''.join('<line class="ch-grid" x1="60" y1="%.1f" x2="730" y2="%.1f"/><text class="ch-tick" x="44" y="%.1f" style="text-anchor:end">%dM</text>'
  %(270-(v/5.0)*230,270-(v/5.0)*230,270-(v/5.0)*230+4,v) for v in [1,2,3,4,5])
dots=''.join('<circle cx="%.1f" cy="%.1f" r="5" fill="var(--sage)" stroke="var(--warm-white)" stroke-width="2"/>'%p for p in PTS[:3])

CHART_PROJ = ('<svg class="chart" viewBox="0 0 760 320" role="img" aria-label="Cumulative organic video views: '
 '1.4 million to date, projected to reach roughly 4.65 million over the next twelve months if the current pace holds.">'
 + grid +
 '<path d="%s L 283.3 270 L 60 270 Z" fill="var(--sage)" opacity=".13"/>' % pth(0,2) +
 '<path d="%s" fill="none" stroke="var(--sage)" stroke-width="2.5"/>' % pth(0,2) +
 '<path d="%s" fill="none" stroke="var(--sage)" stroke-width="2.5" stroke-dasharray="7 6" opacity=".75"/>' % pth(2,6) +
 '<line class="ch-axis" x1="283.3" y1="40" x2="283.3" y2="270" stroke-dasharray="3 4"/>'
 '<line class="ch-axis" x1="60" y1="270" x2="730" y2="270"/>'
 + dots +
 '<circle cx="730" cy="56.1" r="5" fill="none" stroke="var(--sage)" stroke-width="2.5"/>'
 '<text class="ch-tick" x="283.3" y="30" style="letter-spacing:.16em">TODAY</text>'
 '<text class="ch-tick" x="60" y="290" style="text-anchor:start">Q1</text>'
 '<text class="ch-tick" x="171.7" y="290">Q2</text>'
 '<text class="ch-tick" x="730" y="290" style="text-anchor:end">+12 MONTHS</text>'
 '<text x="283.3" y="196" style="font-family:var(--serif);font-size:20px;fill:var(--sage);text-anchor:end">1.4M</text>'
 '<text x="722" y="46" style="font-family:var(--serif);font-size:22px;fill:var(--sage);text-anchor:end">&#8776; 4.65M</text>'
 '<text class="ch-tick" x="722" y="310" style="text-anchor:end;opacity:.35">dashed = directional projection at Q2 pace</text>'
 '</svg>')
print('charts built')

S=[]
def slide(n, cls, inner):
    S.append('<section class="slide %s">%s%s</section>' % (cls, inner, foot(n)))

# 01 COVER
S.append('''<section class="cover-hero">
  <div data-reveal data-delay="1"><img src="data:image/png;base64,%s" alt="Hallpass Digital" style="height:24px;filter:invert(1);opacity:.6"></div>
  <div>
    <h1 class="cover-headline" data-reveal data-delay="2">People are already<br>watching Ardmore.<br>Let&rsquo;s keep building <em>momentum.</em></h1>
    <p class="cover-sub" data-reveal data-delay="3">Where we started, what we&rsquo;ve built, and where we take it over the next twelve months.</p>
  </div>
  <div data-reveal data-delay="4">
    <div class="cover-bottom-label">Prepared for</div>
    <div class="cover-bottom-title">Ardmore Chamber of Commerce</div>
    <div class="cover-bottom-date">September 2026</div>
  </div>
</section>''' % LOGO)

# FLYWHEEL GRAPHIC (slide moved below)
FLY = '''<svg class="flywheel" viewBox="0 -38 720 481" role="img"
 aria-label="A circular flywheel showing the Ardmore Development Authority, the Ardmore Tourism Authority and the Ardmore Chamber of Commerce feeding one another around a shared Ardmore Means More brand.">
<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="var(--sage)"/></marker></defs>
<path class="fw-arc" marker-end="url(#ah)" d="M 460.7 88.9 A 190 190 0 0 1 549.9 243.4"/>
<path class="fw-arc" marker-end="url(#ah)" d="M 449.2 417.8 A 190 190 0 0 1 270.8 417.8"/>
<path class="fw-arc" marker-end="url(#ah)" d="M 170.1 243.4 A 190 190 0 0 1 259.3 88.9"/>
<text class="fw-mid" x="360" y="243">Ardmore</text>
<text class="fw-mid" x="360" y="266">Means More</text>
<text class="fw-midsub" x="360" y="292">One shared brand</text>
<circle class="fw-node" cx="360" cy="60" r="78"/>
<text class="fw-abbr" x="360" y="54">ADA</text>
<text class="fw-sub" x="360" y="74">Development</text><text class="fw-sub" x="360" y="88">Authority</text>
<circle class="fw-node" cx="524.5" cy="345" r="78"/>
<text class="fw-abbr" x="524.5" y="339">ATA</text>
<text class="fw-sub" x="524.5" y="359">Tourism</text><text class="fw-sub" x="524.5" y="373">Authority</text>
<circle class="fw-node" cx="195.5" cy="345" r="78"/>
<text class="fw-abbr" x="195.5" y="339">Chamber</text>
<text class="fw-sub" x="195.5" y="359">of</text><text class="fw-sub" x="195.5" y="373">Commerce</text>
</svg>'''


# 03 WHAT WE'VE BUILT — GROWTH (dark)
slide(2,'slide--dark',u'''<p class="eyebrow" data-reveal>What We&rsquo;ve Built</p>
<h2 class="display-sm" data-reveal data-delay="1">Every number roughly<br><em>doubled</em> in a single quarter.</h2>
<div class="rule" data-reveal data-delay="2"></div>
<div data-reveal data-delay="3">%s</div>
<p class="body wide" data-reveal data-delay="4">Not a spike from one lucky video. Views, engagement and audience growth all moved together, quarter over quarter, which is what sustained momentum looks like rather than a fluke.</p>
<p class="srcnote" data-reveal data-delay="5">Ardmore Means More channels, Q1 vs Q2 2026.</p>''' % CHART_GROWTH)

# 04 CUMULATIVE + REACH
slide(3,'slide--sage',u'''<p class="eyebrow" data-reveal>The Audience</p>
<h2 class="display-sm" data-reveal data-delay="1">1.4 million views &mdash; and most<br>of them <em>aren&rsquo;t from here.</em></h2>
<div class="rule" data-reveal data-delay="2"></div>
<div class="metric-strip" style="margin-top:28px">
<div class="metric" data-reveal data-delay="3"><div class="metric-value">1.4M</div><div class="metric-label">Cumulative organic video views to date</div></div>
<div class="metric" data-reveal data-delay="4"><div class="metric-value">100K</div><div class="metric-label">Cumulative engagements</div></div>
<div class="metric" data-reveal data-delay="5"><div class="metric-value">~2,000</div><div class="metric-label">New followers added in July alone &mdash; a slow month for approvals</div></div>
</div>
<div data-reveal data-delay="6">%s</div>
<p class="body wide" data-reveal data-delay="7">Roughly six in ten of the people engaging with Ardmore content have never been part of the local audience. The reach is extending into Dallas and Oklahoma City &mdash; which means this isn&rsquo;t Ardmore talking to itself. It&rsquo;s Ardmore being discovered.</p>''' % CHART_REACH)

# 04 MOMENTUM (dark)
slide(4,'slide--dark',u'''<p class="eyebrow" data-reveal>The Momentum</p>
<h2 class="display-sm" data-reveal data-delay="1">Hold this pace and the audience<br><em>triples</em> in twelve months.</h2>
<div class="rule" data-reveal data-delay="2"></div>
<div data-reveal data-delay="3">%s</div>
<div class="metric-strip" style="margin-top:24px">
<div class="metric" data-reveal data-delay="4"><div class="metric-value">3.25M</div><div class="metric-label">Additional video views over the next twelve months</div></div>
<div class="metric" data-reveal data-delay="5"><div class="metric-value">24,000</div><div class="metric-label">Additional followers at the current monthly pace</div></div>
<div class="metric" data-reveal data-delay="6"><div class="metric-value">0</div><div class="metric-label">Of that happens if the content stops</div></div>
</div>
<p class="srcnote" data-reveal data-delay="7">Projection assumes the Q2 pace holds. Directional, not guaranteed.</p>''' % CHART_PROJ)

# 05 WHY IT WORKS (three boxes)
slide(5,'',u'''<p class="eyebrow" data-reveal>Why This Has Worked</p>
<div class="card-grid why-grid">
<div class="card" data-reveal data-delay="1"><div class="card-num">01</div>
<div class="card-title">An outsider perspective</div></div>
<div class="card" data-reveal data-delay="2"><div class="card-num">02</div>
<div class="card-title">Engaging storytelling</div></div>
<div class="card" data-reveal data-delay="3"><div class="card-num">03</div>
<div class="card-title">Consistency</div></div>
</div>''')


print('1-6 staged')

slide(6,'slide--sage',u'''<p class="eyebrow" data-reveal>How This Proposal Is Structured</p>
<h2 class="display-sm" data-reveal data-delay="1">Three distinct organizations.<br>The actions of one <em>benefit all.</em></h2>
<div class="fly-wrap" data-reveal data-delay="2">%s</div>''' % FLY)

# 07 PROPOSED INITIATIVES
slide(7,'',u'''<p class="eyebrow" data-reveal>Proposed Initiatives for the Coming Year</p>
<div class="init-list">
<div class="init-row" data-reveal data-delay="1"><div class="init-n">01</div><div class="init-t">Ardmore Means More Social</div></div>
<div class="init-row" data-reveal data-delay="2"><div class="init-n">02</div><div class="init-t">Tourism Card Measurement &amp; Reporting</div></div>
<div class="init-row" data-reveal data-delay="3"><div class="init-n">03</div><div class="init-t">Event Promotion Email Campaign</div></div>
<div class="init-row" data-reveal data-delay="4"><div class="init-n">04</div><div class="init-t">Chamber Member Learning Library</div></div>
<div class="init-row" data-reveal data-delay="5"><div class="init-n">05</div><div class="init-t">Employment in Ardmore Email</div></div>
</div>''')

# 08 INITIATIVE 01
slide(8,'slide--sage',u'''<p class="eyebrow" data-reveal>01 &mdash; Ardmore Means More Social</p>
<h2 class="display-sm" data-reveal data-delay="1">Continue to grow our reach on<br><em>Ardmore Means More</em> social media.</h2>
<ul class="init-bullets">
<li data-reveal data-delay="2">Continue to highlight Ardmore businesses and organizations</li>
<li data-reveal data-delay="3">Create more content about economic development</li>
<li data-reveal data-delay="4">Opportunities for storytelling around CORI and Paradise Alley</li>
</ul>''')

# 09 INITIATIVE 02
slide(9,'',u'''<p class="eyebrow" data-reveal>02 &mdash; Tourism Card Measurement &amp; Reporting</p>
<h2 class="display-sm" data-reveal data-delay="1">Turn the tourism card into<br>a channel we can <em>measure.</em></h2>
<ul class="init-bullets">
<li data-reveal data-delay="2">Track scans, offer claims and referral traffic business by business</li>
<li data-reveal data-delay="3">Separate visitor spending from resident spending</li>
<li data-reveal data-delay="4">Report real numbers back to each participating business</li>
</ul>''')

# 10 INITIATIVE 03
slide(10,'slide--sage',u'''<p class="eyebrow" data-reveal>03 &mdash; Event Promotion Email Campaign</p>
<h2 class="display-sm" data-reveal data-delay="1">A weekly <em>What&rsquo;s Happening<br>Around Ardmore</em> email.</h2>
<ul class="init-bullets">
<li data-reveal data-delay="2">Events collected automatically from venues and public calendars</li>
<li data-reveal data-delay="3">One email, segmented for residents and for visitors</li>
<li data-reveal data-delay="4">Member events promoted alongside community events</li>
</ul>''')

# 11 INITIATIVE 04
slide(11,'',u'''<p class="eyebrow" data-reveal>04 &mdash; Chamber Member Learning Library</p>
<h2 class="display-sm" data-reveal data-delay="1">On-demand training every<br>member can <em>actually use.</em></h2>
<ul class="init-bullets">
<li data-reveal data-delay="2">Twelve modules &mdash; search, reviews, social media, practical AI</li>
<li data-reveal data-delay="3">A digital readiness score for every member business</li>
<li data-reveal data-delay="4">Re-scored quarterly, so improvement is visible and reportable</li>
</ul>''')

# 12 INITIATIVE 05
slide(12,'slide--dark',u'''<p class="eyebrow" data-reveal>05 &mdash; Employment in Ardmore Email</p>
<h2 class="display-sm" data-reveal data-delay="1">Every job open in Ardmore,<br><em>in one place.</em></h2>
<ul class="init-bullets">
<li data-reveal data-delay="2">A weekly hiring email plus a searchable Chamber-owned job board</li>
<li data-reveal data-delay="3">Openings collected automatically &mdash; no member posts anything</li>
<li data-reveal data-delay="4">Surfaces which hiring businesses are not Chamber members yet</li>
</ul>
<div class="metric-strip">
<div class="metric" data-reveal data-delay="5"><div class="metric-value">180+</div><div class="metric-label">Open positions found in a single week of testing</div></div>
<div class="metric" data-reveal data-delay="6"><div class="metric-value">41</div><div class="metric-label">Employers hiring, from Mercy and Valero to Dollar General</div></div>
<div class="metric" data-reveal data-delay="7"><div class="metric-value">Built</div><div class="metric-label">Working prototype, live and ready to demonstrate today</div></div>
</div>''')

# 13 IMPLEMENTATION
slide(13,'slide--sage',u'''<p class="eyebrow" data-reveal>Implementation</p>
<h2 class="display-sm" data-reveal data-delay="1">Nothing pauses.</h2>
<div class="rule" data-reveal data-delay="2"></div>
<div class="phase-list">
<div class="phase-item" data-reveal data-delay="3"><div class="phase-label">Phase 01<br>Days 1&ndash;30</div>
<div><div class="phase-title">Setup, without a gap in publishing</div><p class="phase-body">Content continues uninterrupted while the CRM and automation platform are stood up, the measurement framework and dashboard are built, the training library is first recorded, and the job collection pipeline goes in. Pre-production on the first shoot.</p></div></div>
<div class="phase-item" data-reveal data-delay="4"><div class="phase-label">Phase 02<br>Days 31&ndash;90</div>
<div><div class="phase-title">Activation</div><p class="phase-body">Property and workforce content in rotation. First <em>What&rsquo;s Happening</em> emails out. Offer tracking running. First monthly dashboard delivered. Shoot one executed. Training library published with its first scorecard run, and the weekly hiring email in production.</p></div></div>
<div class="phase-item" data-reveal data-delay="5"><div class="phase-label">Phase 03<br>Ongoing</div>
<div><div class="phase-title">Growth &amp; optimization</div><p class="phase-body">Shoots two and three. Monthly reporting and optimization. Quarterly library additions and scorecard re-runs. Weekly hiring collection. Per-business engagement data delivered into the Annual Visibility Report and the Chamber rollup.</p></div></div>
</div>''')

# 14 INVESTMENT
slide(14,'',u'''<p class="eyebrow" data-reveal>Investment</p>
<h2 class="display-sm" data-reveal data-delay="1">Five initiatives. <em>One program.</em></h2>
<div class="price-grid price-grid--two">
<div class="price-card price-card--featured" data-reveal data-delay="2"><p class="price-tier">The Program</p>
<div class="price-amount">$199,200</div><p class="price-period">$16,600 per month</p>
<ul class="price-items"><li>Ardmore Means More Social</li><li>Tourism Card Measurement &amp; Reporting</li><li>Event Promotion Email Campaign</li><li>Chamber Member Learning Library</li><li>Employment in Ardmore Email</li></ul></div>
<div class="price-card" data-reveal data-delay="3"><p class="price-tier">The Program + Campaign Video</p>
<div class="price-amount">$214,200</div><p class="price-period">$17,850 per month</p>
<ul class="price-items"><li>All five initiatives, unchanged</li><li>Two 2&ndash;5 minute campaign videos</li></ul></div>
</div>
<div class="total-bar" data-reveal data-delay="4">
<div><span class="lbl">Agreement term</span><div class="amt" style="font-size:24px">Twelve months</div></div>
<div class="sub">October 1, 2026 through September 30, 2027</div></div>
<p class="body wide" data-reveal data-delay="5" style="font-size:13px">Separate from and additive to the Member Engagement &amp; Visibility Agreement dated May 12, 2026, which remains in full force. Membership collateral, lifecycle email, business profiles, the member directory, the Annual Visibility Report and testimonial video are scoped there and are not re-billed here.</p>''')

# 15 CLOSING
slide(15,'slide--dark slide--closing',u'''<p class="eyebrow" data-reveal>Next Step</p>
<h2 class="display" data-reveal data-delay="1">The cameras are<br><em>already booked.</em></h2>
<div class="rule" data-reveal data-delay="2"></div>
<p class="body" data-reveal data-delay="3">Last year across the two organizations: <strong>$150,000</strong> with ADA plus the <strong>$46,800</strong> tourism engagement &mdash; <strong>$196,800</strong>. This ask: <strong>$199,200</strong>. Essentially flat, restructured.</p>
<p class="body" data-reveal data-delay="4">The next production trip is on the calendar at Andrea&rsquo;s encouragement &mdash; before this agreement would even begin. The audience is already built. The only open question is what we point it at over the next twelve months.</p>
<p class="body" data-reveal data-delay="5">Let&rsquo;s walk through the hiring board while we&rsquo;re together &mdash; it already works, and thirty minutes with it open will say more than this deck can.</p>
<p class="body" data-reveal data-delay="6" style="opacity:1;margin-top:30px">
<strong style="font-family:var(--serif);font-size:20px;font-weight:400">Ryan McNeill</strong><br>
<span style="font-size:13px;opacity:.7">Hall Pass Digital, LLC &middot; ryan@hallpassdigital.com</span></p>
<div class="big-arrow">&rarr;</div>''')

HTML = ('<title>Ardmore Chamber of Commerce — Marketing, Content &amp; Community Engagement Program</title>\n'
 '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">\n'
 '<style>%s</style>\n<div class="deck">\n%s\n</div>\n'
 '<script>(function(){var els=document.querySelectorAll("[data-reveal]");if(!els.length)return;'
 'var c=document.querySelectorAll(".cover-hero [data-reveal]");'
 'setTimeout(function(){c.forEach(function(e){e.classList.add("is-visible")})},120);'
 'var o=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){'
 'e.target.classList.add("is-visible");o.unobserve(e.target)}})},{threshold:0.08,rootMargin:"0px 0px -40px 0px"});'
 'els.forEach(function(e){if(e.closest(".cover-hero"))return;o.observe(e)})})();'
 '(function(){var sl=[].slice.call(document.querySelectorAll(".cover-hero,.slide"));'
 'function cur(){var y=window.scrollY+window.innerHeight*.3,i=0;'
 'sl.forEach(function(s,k){if(s.offsetTop<=y)i=k});return i}'
 'document.addEventListener("keydown",function(ev){'
 'if(ev.metaKey||ev.ctrlKey||ev.altKey)return;var k=ev.key,d=0;'
 'if(k==="ArrowRight"||k==="PageDown"||(k===" "&&!ev.shiftKey))d=1;'
 'else if(k==="ArrowLeft"||k==="PageUp"||(k===" "&&ev.shiftKey))d=-1;'
 'else return;ev.preventDefault();'
 'var i=Math.max(0,Math.min(sl.length-1,cur()+d));'
 'sl[i].scrollIntoView({behavior:"smooth"})})})();</script>') % (CSS, '\n'.join(S))
open('proposal.html','w').write(HTML)
i=HTML.find('<style>')
open(os.path.join(HERE,'..','index.html'),'w').write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width,initial-scale=1">\n'+HTML[:i]+
 '<meta name="description" content="Where we started, what we built, and where we take it next — Hall Pass Digital for the Ardmore Chamber of Commerce.">\n' '<meta name="robots" content="noindex,nofollow">\n'
 '</head>\n<body>\n'+HTML[i:]+'\n</body>\n</html>')
print('slides:',len(S),'| KB',round(len(HTML)/1024,1),'-> ../index.html')
