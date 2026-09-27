const RAW='https://raw.githubusercontent.com/RuthlessCreature/UI-Templates/main/';
const GH='https://github.com/RuthlessCreature/UI-Templates/tree/main/';
const CATEGORY_ORDER=['industrial','internet-us-flat','soe','women-35-45'];
const CATEGORY_NAMES={industrial:'工业类','internet-us-flat':'互联网扁平 · 美式',soe:'国企风格','women-35-45':'35–45 女性'};
const state={templates:[],category:'all',query:'',compare:new Set()};
const styleCache=new Map();

async function hydratePage(t,path){
 let html=await fetchText(RAW+t.path+'/'+path+'?ts='+Date.now());
 if(!html.includes('page-system.css')) return html;
 let styles=styleCache.get(t.id);
 if(!styles){
  const [tokens,pageCss]=await Promise.all([
    fetchText(RAW+t.path+'/tokens/tokens.css?ts='+Date.now()),
    fetchText(RAW+t.path+'/pages/page-system.css?ts='+Date.now())
  ]);
  styles=tokens+'\n'+pageCss.replace(/@import[^;]+;/g,'');
  styleCache.set(t.id,styles);
 }
 html=html.replace(/<link[^>]+page-system\.css[^>]*>/g,'');
 html=html.replace('</head>','<style>'+styles+'</style></head>');
 return html;
}

async function fetchText(url){const r=await fetch(url,{cache:'no-store'});if(!r.ok)throw new Error('HTTP '+r.status);return r.text()}
async function getJSON(url){const r=await fetch(url,{cache:'no-store'});if(!r.ok)throw new Error('fetch failed '+r.status);return r.json()}
function catOf(t){return t.category||'industrial'}
function renderChips(){const box=document.querySelector('#categories');const counts={all:state.templates.length};for(const t of state.templates)counts[catOf(t)]=(counts[catOf(t)]||0)+1;const cats=['all',...CATEGORY_ORDER.filter(x=>counts[x])];box.innerHTML='';for(const c of cats){const b=document.createElement('button');b.className='chip'+(state.category===c?' active':'');b.textContent=(c==='all'?'全部':CATEGORY_NAMES[c]||c)+' '+counts[c];b.onclick=()=>{state.category=c;renderChips();renderGrid()};box.appendChild(b)}}
function hay(t){return [t.id,t.name_zh,t.name_en,t.positioning,t.visual_signature,t.layout_archetype,t.core_motif,t.showcase_level,...(t.tags||[])].join(' ').toLowerCase()}
function updateCompare(){document.querySelector('#compareCount').textContent=state.compare.size;document.querySelector('#openCompare').disabled=state.compare.size<2}
function toggleCompare(t,btn){if(state.compare.has(t.id)){state.compare.delete(t.id);btn.textContent='＋比较';btn.classList.remove('selected')}else{if(state.compare.size>=4){alert('一次最多比较 4 套');return}state.compare.add(t.id);btn.textContent='✓ 已选';btn.classList.add('selected')}updateCompare()}
function renderGrid(){const grid=document.querySelector('#grid'),tpl=document.querySelector('#cardTemplate');grid.innerHTML='';const q=state.query.trim().toLowerCase();const list=state.templates.filter(t=>(state.category==='all'||catOf(t)===state.category)&&(!q||hay(t).includes(q)));if(!list.length){grid.innerHTML='<div class="empty">没有匹配模板。</div>';return}
 for(const t of list){const node=tpl.content.cloneNode(true);const img=node.querySelector('.preview-img');img.src=RAW+(t.high_fidelity_preview||t.path+'/preview/showcase.jpg')+'?ts='+Date.now();img.alt=(t.name_zh||t.id)+' preview';node.querySelector('.category-label').textContent=CATEGORY_NAMES[catOf(t)]||catOf(t);node.querySelector('.name').textContent=t.name_zh||t.id;node.querySelector('.en-name').textContent=t.name_en||t.id;node.querySelector('.version').textContent='v'+(t.version||'—');node.querySelector('.signature').textContent=t.visual_signature||t.layout_archetype||'';node.querySelector('.summary').textContent=t.positioning||'';node.querySelector('.motif').textContent=t.core_motif||'';node.querySelector('.page-count').textContent=(t.page_count||12)+' PAGES';const tags=node.querySelector('.tags');(t.tags||[]).slice(0,5).forEach(x=>{const s=document.createElement('span');s.className='tag';s.textContent=x;tags.appendChild(s)});node.querySelector('.repo-btn').href=GH+t.path;const preview=()=>openShowcase(t);node.querySelector('.live-btn').onclick=preview;node.querySelector('.preview-hit').onclick=preview;const cb=node.querySelector('.compare-btn');if(state.compare.has(t.id)){cb.textContent='✓ 已选';cb.classList.add('selected')}cb.onclick=()=>toggleCompare(t,cb);grid.appendChild(node)}}

async function openShowcase(t){
 const dlg=document.querySelector('#showcaseDialog'),nav=document.querySelector('#showcaseNav'),stage=document.querySelector('#showcaseStage');
 document.querySelector('#showcaseTitle').textContent=t.name_zh+' · '+t.visual_signature;
 nav.innerHTML='<div class="showcase-loading">读取页面目录…</div>';stage.innerHTML='<div class="showcase-loading">准备 12 个真实页面…</div>';dlg.showModal();
 try{
  const manifest=await getJSON(RAW+t.path+'/pages/pages.json?ts='+Date.now());
  nav.innerHTML='';
  const all=document.createElement('button');all.className='page-nav active';all.innerHTML='<b>ALL PAGES</b><span>'+manifest.pages.length+' live screens</span>';all.onclick=()=>showAllPages(t,manifest.pages,all);nav.appendChild(all);
  for(const p of manifest.pages){const b=document.createElement('button');b.className='page-nav';b.innerHTML='<b>'+String(p.index).padStart(2,'0')+' · '+p.name+'</b><span>'+p.kind+' · '+p.device+'</span>';b.onclick=()=>showPage(t,p,b);nav.appendChild(b)}
  await showAllPages(t,manifest.pages,all);
 }catch(e){stage.innerHTML='<div class="showcase-error">完整页面目录加载失败：'+String(e)+'</div>'}
}
function activatePageButton(btn){document.querySelectorAll('#showcaseNav .page-nav').forEach(x=>x.classList.remove('active'));btn.classList.add('active')}
async function showAllPages(t,pages,btn){
 activatePageButton(btn);
 const stage=document.querySelector('#showcaseStage');
 stage.innerHTML='<figure class="showcase-hero"><img src="'+RAW+(t.high_fidelity_preview||t.path+'/preview/showcase.jpg')+'?ts='+Date.now()+'" alt="'+t.name_zh+' high fidelity showcase"></figure><div class="live-wall"></div>';
 const wall=stage.querySelector('.live-wall');
 for(const p of pages){
  const tile=document.createElement('article');tile.className='live-tile '+(p.device==='mobile'?'mobile':'desktop');
  tile.innerHTML='<div class="live-tile-head"><b>'+String(p.index).padStart(2,'0')+' · '+p.name+'</b><span>'+p.kind+'</span></div><div class="thumb-shell"><iframe title="'+p.name+'" tabindex="-1"></iframe></div>';
  tile.onclick=()=>{const button=[...document.querySelectorAll('#showcaseNav .page-nav')].find(x=>x.textContent.includes(p.name));showPage(t,p,button)};
  wall.appendChild(tile);
  hydratePage(t,p.path).then(html=>{tile.querySelector('iframe').srcdoc=html}).catch(()=>{tile.querySelector('.thumb-shell').innerHTML='<div class="thumb-error">加载失败</div>'});
 }
}
async function showPage(t,p,btn){if(btn)activatePageButton(btn);const stage=document.querySelector('#showcaseStage');stage.innerHTML='<div class="showcase-loading">加载 '+p.name+'…</div>';try{const html=await hydratePage(t,p.path);stage.innerHTML='<div class="single-page-shell '+(p.device==='mobile'?'mobile':'desktop')+'"><iframe class="showcase-frame" title="'+p.name+'"></iframe></div>';stage.querySelector('iframe').srcdoc=html}catch(e){stage.innerHTML='<div class="showcase-error">页面加载失败：'+String(e)+'</div>'}}

async function openPreview(t){const dlg=document.querySelector('#previewDialog'),frame=document.querySelector('#previewFrame');document.querySelector('#dialogTitle').textContent=t.name_zh;frame.srcdoc='';dlg.showModal();try{const manifest=await getJSON(RAW+t.path+'/pages/pages.json?ts='+Date.now());frame.srcdoc=await hydratePage(t,manifest.pages[0].path)}catch(e){frame.srcdoc='<p>加载失败</p>'}}
function openCompare(){const list=state.templates.filter(t=>state.compare.has(t.id));const box=document.querySelector('#compareGrid');box.innerHTML='';for(const t of list){const d=document.createElement('article');d.className='compare-item';d.innerHTML='<div class="compare-name">'+t.name_zh+'</div><div class="compare-sig">'+(t.visual_signature||'')+'</div><img src="'+RAW+t.path+'/preview/overview.svg?ts='+Date.now()+'" alt=""><div class="compare-motif">'+(t.core_motif||'')+' · 12 pages</div>';d.onclick=()=>openShowcase(t);box.appendChild(d)}document.querySelector('#compareDialog').showModal()}
async function boot(){document.querySelector('#closePreview')?.addEventListener('click',()=>document.querySelector('#previewDialog').close());document.querySelector('#closeDialog').onclick=()=>document.querySelector('#previewDialog').close();document.querySelector('#closeShowcase').onclick=()=>document.querySelector('#showcaseDialog').close();document.querySelector('#closeCompare').onclick=()=>document.querySelector('#compareDialog').close();document.querySelector('#openCompare').onclick=openCompare;document.querySelector('#search').oninput=e=>{state.query=e.target.value;renderGrid()};try{const reg=await getJSON(RAW+'registry.json?ts='+Date.now());state.templates=reg.templates||[];document.querySelector('#count').textContent=state.templates.length+' templates';renderChips();renderGrid();updateCompare()}catch(e){document.querySelector('#grid').innerHTML='<div class="empty">registry.json 加载失败：'+String(e)+'</div>'}}
boot();