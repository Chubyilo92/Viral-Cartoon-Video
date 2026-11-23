// Gemini queue runner with the 5-minute rule. Queue/progress live in localStorage (survive reloads).
window.sleep=ms=>new Promise(r=>setTimeout(r,ms));
window.PD="Generate an image, 16:9 landscape. Same art style and same characters as the character sheets and panels earlier in this chat. Hand-drawn comic illustration, bold ink outlines, muted cinematic colours. The dead: plain pale grey-green SQUARE box heads, two big dark hollow eye sockets with tiny pale pupils, torn dirty grey clothes, no blood. ";
window.RUN5=()=>{const S=window.R5={state:'run',beat:Date.now()};(async()=>{
 const Q=JSON.parse(localStorage.e4q),LIM=5*60*1000;const log=m=>{const l=JSON.parse(localStorage.e4log);l.push(m.concat([new Date().toTimeString().slice(0,8)]));localStorage.e4log=JSON.stringify(l)};
 const stopBtn=()=>document.querySelector('button[aria-label="Stop response"]');
 const clearStop=async()=>{for(let k=0;k<10&&stopBtn();k++){stopBtn().click();await sleep(2000)}return !stopBtn()};
 const one=async(id,p)=>{const t0=Date.now();
  if(!await clearStop())return 'STUCK';
  const ed=document.querySelector('.ql-editor');ed.focus();document.execCommand('selectAll');document.execCommand('delete');document.execCommand('insertText',false,PD+p);
  let b=null;for(let k=0;k<20&&!b;k++){await sleep(1000);b=document.querySelector('button[aria-label="Send message"]')}
  if(!b)return 'STUCK';
  const n0=document.querySelectorAll('model-response').length;b.click();
  while(Date.now()-t0<LIM){await sleep(3000);S.beat=Date.now();const R=document.querySelectorAll('model-response'),L=R[R.length-1];
   if(R.length>n0){const d=L.querySelector('button[aria-label="Download full-sized image"]');
    if(d){d.scrollIntoView({block:'center'});await sleep(1500);d.click();await sleep(9000);return 'IMG'}
    if(/limit/i.test(L.innerText)&&/reset/i.test(L.innerText))return 'LIMIT';
    if(!stopBtn()&&L.innerText.length>40&&Date.now()-t0>30000)return 'NOIMG'}}
  await clearStop();return 'SKIP5'};
 for(let pass=0;pass<2;pass++){
  if(pass===1){const sk=JSON.parse(localStorage.e4skip);if(!sk.length)break;localStorage.e4q=JSON.stringify(sk);localStorage.e4skip='[]';localStorage.e4i='0'}
  const QQ=JSON.parse(localStorage.e4q);
  for(let i=+localStorage.e4i;i<QQ.length;i++){const [id,p]=QQ[i];const st=await one(id,p);log([id,st]);
   if(st==='STUCK'){S.state='STUCK';return} if(st==='LIMIT'){S.state='LIMIT';return}
   if(st!=='IMG'&&pass===0){const sk=JSON.parse(localStorage.e4skip);sk.push(QQ[i]);localStorage.e4skip=JSON.stringify(sk)}
   localStorage.e4i=String(i+1)}}
 S.state='done'})();return 'RUN5 started at '+localStorage.e4i};
RUN5()
