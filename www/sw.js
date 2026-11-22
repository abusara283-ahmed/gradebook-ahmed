const V='gb-v2';
const CORE=["./", "index.html", "manifest.webmanifest", "fonts/fonts.css", "lib/xlsx.full.min.js", "lib/html2canvas.min.js", "lib/jspdf.umd.min.js", "icons/icon-192.png", "icons/icon-512.png", "fonts/ibm-plex-sans-arabic-arabic-400-normal.woff2", "fonts/ibm-plex-sans-arabic-arabic-500-normal.woff2", "fonts/ibm-plex-sans-arabic-arabic-600-normal.woff2", "fonts/ibm-plex-sans-arabic-arabic-700-normal.woff2", "fonts/ibm-plex-sans-arabic-latin-400-normal.woff2", "fonts/ibm-plex-sans-arabic-latin-500-normal.woff2", "fonts/ibm-plex-sans-arabic-latin-600-normal.woff2", "fonts/ibm-plex-sans-arabic-latin-700-normal.woff2"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request,u=new URL(r.url);
  if(r.method!=='GET'||u.origin!==location.origin)return;
  e.respondWith(caches.open(V).then(async c=>{
    const hit=await c.match(r,{ignoreSearch:true});
    if(r.mode==='navigate'||/\/(index\.html)?$/.test(u.pathname)){try{const res=await fetch(r);if(res&&res.ok){c.put(r,res.clone());return res}}catch(_){}return hit||fetch(r)}
    const net=fetch(r).then(res=>{if(res&&res.ok)c.put(r,res.clone());return res}).catch(()=>hit);
    return hit||net;
  }));
});
