import sys,json,numpy as np,soundfile as sf
sys.path.insert(0,'/home/claude/tq'); import sfxlib as L
SR=48000;TOT=520.8;N=int(TOT*SR)
fx=np.zeros(N);sting=np.zeros(N)
def add(x,t,db,room=None,wet=.3,buf=None):
    buf=fx if buf is None else buf
    x=np.asarray(x,dtype=float); x=x.mean(1) if x.ndim>1 else x
    if room: x=L.verb(x,room,wet)
    i=max(0,int(t*SR)); x=x[:max(0,N-i)]; buf[i:i+len(x)]+=x*10**(db/20)
def fade(x,a=.5,r=.8):
    n=len(x); e=np.ones(n); fa=min(int(a*SR),n//2); fr=min(int(r*SR),n//2); e[:fa]=np.linspace(0,1,fa); e[n-fr:]=np.linspace(1,0,fr); return x*e
def cicadas(d,seed=0):
    n=L.secs(d); t=L.tt(n); x=L.filt(L.noise(n,seed),4200,7500); am=(0.5+0.5*np.sin(2*np.pi*23*t))**3*(0.6+0.4*np.sin(2*np.pi*.13*t+seed)); return x*am*.6
BED=-46
def bed(a,b,loc,db=0):
    d=b-a+.6; add(fade(L.room_tone(d,seed=int(a*3)),.4,.6),a-.2,BED+db)
    if loc=='landing': add(fade(L.elec_hum(d,False,seed=3),.4,.6),a,-56+db)
    if loc in('heat','piazza'): add(fade(cicadas(d,seed=int(a)),1.0,1.0),a,-50+db)
    if loc=='night': add(fade(L.wind(d,seed=int(a),bright=500),1.5,1.5),a,-64+db)
    if loc=='rain': add(fade(L.rain(d,seed=int(a)),1.5,1.5),a,-42+db)
v,_=sf.read('work/voice48.wav'); v=v.mean(1) if v.ndim>1 else v; v=np.pad(v,(0,max(0,N-len(v))))[:N]
nz,_=sf.read('/home/claude/tq/reel2/noise.wav'); nz=nz.mean(1) if nz.ndim>1 else nz; nz=L.norm(nz,.7)
P=json.load(open('plan.json'))
for s in P['shots']:
    if 'card' in s: add(nz,s['t'],-4,buf=sting)

# ---- beds ----
bed(0,58.7,'landing');bed(60.3,66.4,'landing',-2);bed(66.4,72.8,'piazza',-4);bed(72.8,123.6,'night')
bed(126.1,158.3,'landing');bed(158.3,197.8,'landing',-2)
bed(200.0,273.8,'piazza',-2)
bed(275.8,300.5,'landing');bed(300.5,355.0,'landing',2)
bed(356.9,381.9,'night');bed(383.9,402.6,'piazza',-3)
bed(405.2,442.2,'night',2);bed(443.8,499.5,'landing');bed(499.5,520.8,'night',2)
# ---- horror drone under tense passages (quiet) ----
def dr(a,b,root,db=-50): add(fade(L.drone(b-a,root,seed=int(a)),1.5,1.5),a,db)
for a,b,r in [(0,58.7,55),(30.5,58.7,49),(300.5,342.9,52),(405.2,442.2,46),(456.2,520.8,49),(110.5,123.6,58)]: dr(a,b,r)
# ---- spot sfx ----
add(L.groan(2.0,58,1,seed=1),5.4,-44,'stairs',.5)               # whatever came out of flat 7
add(L.heartbeat(8,72),20.0,-40)
add(L.scrape(.5,seed=2),23.8,-40,'flat',.2)                      # touching near wedge
add(L.scrape(.9,seed=3),30.8,-40,'flat',.2)                      # hands slide through gap
add(L.riser(2.2),36.5,-44);add(L.sub_drop(),39.0,-26);add(L.boom(.6),39.0,-36,'flat',.3)   # "un morso"
add(L.groan(1.4,62,1,seed=4),46.2,-42,'stairs',.4)
for k,t in enumerate([49.3,50.1,50.8]): add(L.groan(1.4,58+k*3,1,seed=10+k),t,-46,'out',.5)
add(L.riser(3.0),54.5,-44);add(L.sub_drop(),57.9,-24)             # P10 end
for t in [66.6,67.8]: add(L.water_run(1.2,seed=int(t)),t,-50,'out',.4)   # waves
add(L.groan(1.6,60,1,seed=20),68.4,-44,'out',.4)
add(L.boom(.5),70.3,-38,'out',.3)
add(L.thud(.8),75.8,-38,'street',.5)                               # van doors
add(L.whoosh(.6),83.6,-44)
add(L.sub_drop(),93.0,-30);add(L.groan(1.2,70,1,seed=21),93.0,-38,'stairs',.4)   # "ti trasformi"
add(L.phone_buzz(1.0),115.7,-40)
add(L.thud(.5),119.9,-36,'flat',.2)                                # door opens
add(L.sub_drop(),122.8,-26)                                        # P11 end
add(L.water_run(5.0,seed=3),144.0,-46,'flat',.2)
add(L.pencil(1.2),159.8,-38);add(L.pencil(1.0),161.4,-40)
add(L.heartbeat(6,78),171.4,-38)
add(L.clock_tick(6),186.3,-44)
add(L.riser(2.0),195.3,-44);add(L.sub_drop(),197.1,-24)            # P12 end
for k in range(4): add(L.scrape(.35,seed=30+k),226.5+k*.8,-44,'out',.3)   # pulley squeak
add(L.whoosh(.8),240.2,-42,'out',.3)
for k in range(6): add(L.whoosh(.4),254.8+k*.3,-48,'out',.3)
add(L.paper(),257.0,-40)
for k,t in enumerate([265.2,266.4,267.5,268.6,269.6]): add(L.groan(1.6,56+k*3,1,seed=40+k),t,-44,'out',.5)
add(L.boom(.7),272.2,-30,'out',.4);add(L.sub_drop(),273.2,-24)    # 71 / P13 end
add(L.can_clink(seed=5),277.5,-42,'flat',.2)
add(L.handle_rattle(.6),293.2,-40,'flat',.2)
add(L.groan(2.0,60,1,seed=50),297.2,-42,'stairs',.5)
for j,t in enumerate([309.9,310.6,311.3,312.6,313.6]): add(L.step_concrete(.9,False,seed=60+j),t,-44-j,'stairs',.7)
add(L.heartbeat(14,70),314.9,-38)
add(L.groan(1.6,64,1,seed=51),319.5,-42,'stairs',.5)
add(L.riser(2.0),326.0,-44);add(L.sub_drop(),327.6,-24)            # P14 end
for t in [330.4,332.2]: add(L.breath(.9,1,seed=int(t)),t,-38,'stairs',.4)   # sniff
add(L.groan(1.8,58,1,seed=52),335.2,-44,'stairs',.5)
for j in range(6): add(L.step_concrete(.9,False,seed=70+j),350.4+j*.6,-46,'stairs',.6)
add(L.handle_rattle(.5),359.2,-40,'out',.4)
for k in range(3): add(L.scrape(.35,seed=80+k),364.3+k*.9,-44,'out',.3)
add(L.paper(),371.1,-38);add(L.paper(),371.8,-40)
add(L.riser(1.5),378.4,-44);add(L.sub_drop(),380.9,-28)
for t in [396.4,397.2,398.6,399.4]: add(L.hiss(.45),t,-42)         # spray
add(L.boom(.8),401.1,-33,'out',.4);add(L.sub_drop(),401.2,-28)     # ULTIMA / P15 end
add(L.thud(.7),410.2,-38,'flat',.2)
add(L.thud(.9),413.1,-34,'flat',.2);add(L.handle_rattle(.5),414.8,-40,'flat',.2)
for t in [432.6,433.4,434.1,435.9,437.6,439.2]: add(L.drip(1.0,seed=int(t*3)),t,-36,'flat',.3)
for k,t in enumerate([434.5,436.2,437.9]): add(L.groan(1.8,52+k*4,1,seed=90+k),t,-46,'out',.5)
add(L.breath(3.0,2,seed=7),428.6,-44,'flat',.3)
add(L.clock_tick(5.5),451.0,-44)
add(L.sub_drop(),458.8,-30)
add(L.thud(.5),468.1,-38,'flat',.2)
add(L.riser(3.0),504.0,-42);add(L.boom(.9),507.2,-34,'out',.4);add(L.sub_drop(),507.25,-30)   # "Il tuo."
for k,t in enumerate([512.0,513.5,515.0,516.6,518.0]): add(L.groan(1.8,54+k*3,1,seed=100+k),t,-44,'out',.5)
add(L.heartbeat(5,84),515.6,-36)
add(L.sub_drop(),519.4,-22)
# ---- ducking: everything under the voice drops 12 dB while it speaks (stings 6 dB) ----
hop=int(.02*SR);fr=len(v)//hop
rms=np.sqrt(np.mean(v[:fr*hop].reshape(fr,hop)**2,axis=1));act=(20*np.log10(rms+1e-9)>-48).astype(float)
hold=int(.25/.02);a2=act.copy()
for i in range(len(act)):
    if act[i]: a2[i:i+hold]=1
g=np.zeros_like(a2);cur=0.
for i,x in enumerate(a2):
    k=.5 if x>cur else .06   # fast attack, slow release
    cur+=k*(x-cur);g[i]=cur
gs=np.repeat(g,hop);gs=np.pad(gs,(0,N-len(gs)),'edge')
fxd=fx*10**(-12*gs/20);std=sting*10**(-20*gs/20)
m=np.tanh(v*1.05+fxd*1.13+std)
sf.write('work/master_mix.wav',m,SR);sf.write('work/fx_only.wav',fxd+std,SR)
print('peak',np.abs(m).max())
