const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+__dirname+'/anim.html');await p.evaluate(async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px "Noto Color Emoji"');});
const dur=await p.evaluate(()=>TOTAL),fps=30,N=Math.round(dur*fps);
const mk=o=>{const f=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','medium','-c:a','aac','-movflags','+faststart',o]);f.stderr.on('data',d=>process.stderr.write(d));return f;};
const A=mk('when_a_boy_loves_you_captions.mp4'),B=mk('when_a_boy_loves_you_clean.mp4');
const w=(f,buf)=>new Promise(r=>f.stdin.write(buf)?r():f.stdin.once('drain',r));
for(let i=0;i<N;i++){const [x,y]=await p.evaluate(t=>{render(t,true);const a=document.getElementById('c').toDataURL('image/jpeg',.94);render(t,false);return[a,document.getElementById('c').toDataURL('image/jpeg',.94)];},i/fps);
 await w(A,Buffer.from(x.split(',')[1],'base64'));await w(B,Buffer.from(y.split(',')[1],'base64'));if(i%300==0)console.log(i,'/',N);}
const done=f=>new Promise(r=>{f.on('close',r);f.stdin.end();});await Promise.all([done(A),done(B)]);await b.close();})();
