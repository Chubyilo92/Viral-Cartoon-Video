const {chromium}=require('/opt/npm-tools/node_modules/playwright');
const {spawn}=require('child_process'); const fs=require('fs');
(async()=>{
 const [f0,f1,out]=process.argv.slice(2);
 const P=JSON.parse(fs.readFileSync('plan.json'));
 const names=[...new Set(P.shots.filter(s=>s.img).map(s=>s.img).concat(P.shots.filter(s=>s.swap).map(s=>s.swap.img)))];
 const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
 const p=await b.newPage({viewport:{width:1920,height:1080}});
 await p.goto('http://127.0.0.1:8768/engine.html');
 await p.evaluate(n=>window.load(n),names);await p.evaluate(()=>document.fonts.load('700 40px Hand'));
 const OVM=JSON.parse(fs.readFileSync('img_all/ov/meta.json'));const ovn=[];for(const s of P.shots)for(const o of (s.ov||[])){for(let k=1;k<=OVM[o.k].n;k++)ovn.push(o.k+'_'+String(k).padStart(2,'0'))}
 await p.evaluate(([n,m])=>{window.OVMETA=m;return window.loadOV(n)},[[...new Set(ovn)],OVM]); await p.evaluate(P=>window.setPlan(P),P);
 if(out==='STILLS'){fs.mkdirSync('st',{recursive:true});for(const t of f0.split(',').map(Number)){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:`st/s_${t}.jpg`,type:'jpeg',quality:70})}await b.close();return}
 const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate','30','-i','-','-vf','scale=1280:720','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out]);
 const a=+f0,z=+f1;
 for(let f=a;f<z;f++){await p.evaluate(t=>window.render(t),f/30);const buf=await p.screenshot({type:'jpeg',quality:90});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));if(f%900==0)console.log(out,f)}
 ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done',out)
})();
