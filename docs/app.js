const LABEL={replicated:"Replicated",partially_replicated:"Partially replicated",not_reproduced:"Not reproduced",contradicted:"Contradicted",untested:"Untested"};
const el=(t,c,x)=>{const e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
const link=(u,t)=>{const a=el("a",null,t);a.href=u;a.rel="noopener";return a};
let data=[];
function render(){
  const q=document.getElementById("q").value.toLowerCase(),st=document.getElementById("st").value;
  const rows=data.filter(c=>(!st||c.status===st)&&(!q||JSON.stringify(c).toLowerCase().includes(q)));
  document.getElementById("count").textContent=rows.length+" of "+data.length+" claims";
  const list=document.getElementById("list");list.replaceChildren();
  for(const c of rows){
    const card=el("article","card");card.id=c.id;
    const top=el("div","meta");top.append(el("span","pill "+c.status,LABEL[c.status])," ",c.id+" · "+c.method+" · "+c.benchmark);
    card.append(top,el("h3",null,c.title));
    const cl=el("p","claim");cl.append(el("b",null,"Claim: "),c.claim+" ");cl.append(link(c.source.url,"("+c.source.label+")"));card.append(cl);
    const sm=el("p","claim");sm.append(el("b",null,"What independent attempts found: "),c.summary);card.append(sm);
    const ul=el("ul","ev");for(const e of c.evidence){const li=el("li");li.append(link(e.url,e.label));ul.append(li)}card.append(ul);
    const bd=el("details","meta");bd.append(el("summary",null,"Embed this status badge"));bd.append(el("code",null,"[![Claim Ledger "+c.id+"](https://studio-glhf.github.io/claim-ledger/badges/"+c.id+".svg)](https://studio-glhf.github.io/claim-ledger/#"+c.id+")"));card.append(bd);
    card.append(el("p","meta","Last checked "+c.last_checked+". "+c.checked_by+"."));
    list.append(card);
  }
}
fetch("data.json").then(r=>r.json()).then(d=>{data=d.claims;document.getElementById("upd").textContent="Data updated "+d.updated+".";render()});
document.getElementById("q").addEventListener("input",render);
document.getElementById("st").addEventListener("change",render);
