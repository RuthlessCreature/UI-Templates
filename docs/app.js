const RAW='https://raw.githubusercontent.com/RuthlessCreature/UI-Templates/main/';
const GH='https://github.com/RuthlessCreature/UI-Templates/tree/main/';
const CATEGORY_ORDER=['industrial','internet-us-flat','soe','women-35-45'];
const CATEGORY_NAMES={industrial:'工业类', 'internet-us-flat':'互联网扁平 · 美式', soe:'国企风格', 'women-35-45':'35–45 女性'};
const state={templates:[],category:'all',query:''};

async function getJSON(url){
  const r=await fetch(url,{cache:'no-store'});
  if(!r.ok) throw new Error('fetch failed '+r.status);
  return r.json();
}
function catOf(t){return t.category||'industrial'}
function renderChips(){
  const box=document.querySelector('#categories');
  const counts={all:state.templates.length};
  for(const t of state.templates) counts[catOf(t)]=(counts[catOf(t)]||0)+1;
  const cats=['all',...CATEGORY_ORDER.filter(x=>counts[x])];
  box.innerHTML='';
  for(const c of cats){
    const b=document.createElement('button'); b.className='chip'+(state.category===c?' active':'');
    b.textContent=(c==='all'?'全部':CATEGORY_NAMES[c]||c)+' '+counts[c];
    b.onclick=()=>{state.category=c;renderChips();renderGrid()};
    box.appendChild(b);
  }
}
function hay(t){return [t.id,t.name_zh,t.name_en,t.positioning,...(t.tags||[])].join(' ').toLowerCase()}
function renderGrid(){
  const grid=document.querySelector('#grid'); const tpl=document.querySelector('#cardTemplate'); grid.innerHTML='';
  const q=state.query.trim().toLowerCase();
  const list=state.templates.filter(t=>(state.category==='all'||catOf(t)===state.category)&&(!q||hay(t).includes(q)));
  if(!list.length){grid.innerHTML='<div class="empty">没有匹配模板。</div>';return}
  for(const t of list){
    const node=tpl.content.cloneNode(true);
    const img=node.querySelector('.preview-img');
    img.src=RAW+t.path+'/preview/overview.svg?ts='+Date.now();
    img.alt=(t.name_zh||t.id)+' preview';
    node.querySelector('.category-label').textContent=CATEGORY_NAMES[catOf(t)]||catOf(t);
    node.querySelector('.name').textContent=t.name_zh||t.id;
    node.querySelector('.en-name').textContent=t.name_en||t.id;
    node.querySelector('.version').textContent='v'+(t.version||'—');
    node.querySelector('.summary').textContent=t.positioning||'Brand-neutral UI template';
    const tags=node.querySelector('.tags');
    (t.tags||[]).slice(0,6).forEach(x=>{const s=document.createElement('span');s.className='tag';s.textContent=x;tags.appendChild(s)});
    const repo=node.querySelector('.repo-btn'); repo.href=GH+t.path;
    const preview=()=>openPreview(t);
    node.querySelector('.live-btn').onclick=preview; node.querySelector('.preview-hit').onclick=preview;
    grid.appendChild(node);
  }
}
async function openPreview(t){
  const dlg=document.querySelector('#previewDialog'), frame=document.querySelector('#previewFrame');
  document.querySelector('#dialogTitle').textContent=(t.name_zh||t.id)+' / '+(t.name_en||'');
  frame.srcdoc='<style>body{font-family:system-ui;padding:30px;color:#667085}</style>正在加载 GitHub 中的 demo…';
  dlg.showModal();
  try{
    const r=await fetch(RAW+t.path+'/examples/demo.html?ts='+Date.now(),{cache:'no-store'});
    if(!r.ok) throw new Error('HTTP '+r.status);
    frame.srcdoc=await r.text();
  }catch(e){frame.srcdoc='<style>body{font-family:system-ui;padding:30px}</style><h3>Demo 加载失败</h3><p>'+String(e)+'</p>'}
}
async function boot(){
  document.querySelector('#closeDialog').onclick=()=>document.querySelector('#previewDialog').close();
  document.querySelector('#search').oninput=e=>{state.query=e.target.value;renderGrid()};
  try{
    const reg=await getJSON(RAW+'registry.json?ts='+Date.now());
    state.templates=(reg.templates||[]).map(t=>({...t,positioning:t.positioning||''}));
    document.querySelector('#count').textContent=state.templates.length+' templates';
    renderChips();renderGrid();
  }catch(e){document.querySelector('#grid').innerHTML='<div class="empty">registry.json 加载失败：'+String(e)+'</div>'}
}
boot();
