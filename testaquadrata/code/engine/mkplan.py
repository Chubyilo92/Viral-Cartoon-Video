import json,os
T=520.8;S=[];MISS=[]
FB={'e3_lockin':'e3_quarantine','e3_vigil2':'e1_door_sit','e3_final_roof':'e1_roof_tank','e3_wall_ultima_blank':'e3_wall_ultima_clean'}
def card(t,l): S.append(dict(t=t,card=l))
def sh(t,img,z=(1.0,1.2),c=(.5,.5,.5,.5),**k):
    if not os.path.exists(f'img_all/{img}.jpg'): MISS.append(img); img=FB[img]
    d=dict(t=t,img=img,z=list(z),c=list(c));d.update(k);S.append(d)
# ---------- PARTE 10 ----------
sh(0.0,'giulia_reveal',(1.0,1.3),(.5,.5,.82,.5),fadein=1)
sh(4.0,'giulia_zombie',(1.0,1.3),(.55,.5,.75,.5))
sh(10.7,'e3_eye_gap',(1.0,1.15),(.5,.5,.4,.45))
sh(13.0,'door_gap',(1.0,1.25),(.5,.5,.5,.5))
sh(17.5,'wedge_door',(1.5,1.8),(.45,.75,.45,.82))
sh(19.9,'e3_eye_gap',(1.3,2.3),(.5,.45,.51,.43))
sh(23.6,'wedge_door',(1.9,2.2),(.45,.83,.45,.84),shake=[[.2],.4,4])
sh(25.8,'e3_night_talk',(1.2,1.6),(.7,.55,.8,.5))
sh(30.5,'e3_hands_gap',(1.0,1.9),(.5,.45,.5,.38))
sh(35.1,'e3_ankle_bite',(1.0,1.35),(.5,.5,.5,.6))
sh(37.5,'e3_ankle_bite',(2.0,3.2),(.5,.62,.503,.667),punch=1.5,shake=[[1.5],.4,6])
sh(45.9,'e1_antonelli',(1.0,1.3),(.5,.45,.5,.4))
sh(49.1,'crowd_under',(1.0,1.4),(.6,.4,.55,.7))
sh(51.8,'e3_ostia',(1.1,1.5),(.35,.6,.25,.55))
sh(54.5,'e3_eye_gap',(1.6,2.8),(.51,.45,.51,.43))
# ---------- PARTE 11 ----------
card(58.7,'GIORNO 61')
sh(60.3,'e3_night_talk',(1.0,1.25),(.5,.5,.6,.5),flick=1)
sh(66.4,'e3_ostia',(1.0,1.3),(.3,.6,.7,.45))
sh(70.1,'e3_ankle_bite',(2.2,3.0),(.5,.65,.503,.667),flash=[.3],g=['#401018',.15])
sh(72.8,'e3_van_rescue',(1.0,1.3),(.5,.5,.42,.5))
sh(77.1,'e3_lights',(1.0,1.6),(.5,.45,.43,.52))
sh(83.7,'e3_injection',(1.0,1.3),(.5,.5,.55,.45))
sh(89.3,'e3_injection',(1.6,2.2),(.6,.45,.66,.45))
sh(92.9,'e1_antonelli2',(1.2,1.5),(.5,.5,.75,.45),shake=[[.2],.5,8],punch=.2)
sh(94.9,'giulia_zombie',(1.1,1.4),(.6,.5,.7,.5))
sh(98.4,'e3_night_talk',(1.3,1.6),(.6,.5,.45,.5))
sh(101.3,'vanphone',(1.2,1.6),(.4,.45,.36,.42))
sh(104.6,'wall_acqua',(1.0,1.3),(.5,.5,.5,.5))
sh(110.5,'e3_eye_gap',(2.2,2.8),(.51,.43,.51,.43))
sh(114.0,'e3_ankle_bite',(2.6,3.0),(.503,.667,.503,.667))
sh(115.5,'e3_eye_gap',(1,1),(.5,.5,.5,.5),phone=1,l1=0,l2=2.6,pdate='sabato 15 agosto',ptime='21:52',pago='15 ago')
sh(119.7,'e3_letin',(1.0,1.2),(.5,.5,.45,.5))
sh(121.5,'e3_letin',(1.5,2.0),(.68,.55,.72,.52),punch=.3)
# ---------- PARTE 12 ----------
card(123.6,'GIORNO 62')
sh(126.1,'e3_ankle_bite',(1.2,1.5),(.5,.55,.5,.6))
sh(130.0,'e3_quarantine',(1.0,1.2),(.5,.5,.45,.5))
sh(133.6,'e3_quarantine',(1.8,2.2),(.22,.45,.33,.45))
sh(138.8,'e3_quarantine',(1.4,1.6),(.72,.5,.8,.5))
sh(143.9,'e3_handwash',(1.0,1.3),(.5,.5,.45,.55))
sh(152.4,'e3_handwash',(1.7,2.3),(.45,.55,.42,.6))
sh(158.3,'e3_pen_line',(1.0,1.35),(.5,.5,.5,.65))
sh(163.0,'e3_pen_line',(2.0,2.6),(.5,.72,.5,.74))
sh(171.2,'e3_ankle_bite',(2.4,3.0),(.503,.62,.503,.667),pulse=[1.1,'#ff1010',.25],g=['#2a0006',.12])
sh(177.1,'e3_pen_line',(1.3,1.6),(.45,.6,.5,.7))
sh(180.0,'e3_pulse_v3',(1.0,1.6),(.5,.5,.5,.62))
sh(190.4,'e3_pen_line',(1.6,1.4),(.5,.7,.45,.6))
sh(195.3,'e3_injection',(1.8,2.4),(.62,.45,.66,.45),dim=[0,.35])
# ---------- PARTE 13 ----------
card(197.8,'GIORNO 63')
sh(200.0,'e1_roof_tank',(1.0,1.25),(.5,.5,.6,.5))
sh(205.0,'bottle_cable',(1.0,1.35),(.25,.4,.65,.45))
sh(211.8,'e3_funicular',(1.0,1.25),(.45,.45,.6,.4))
sh(216.3,'e3_pulley',(1.0,1.15),(.5,.5,.45,.5))
sh(221.7,'e1_containers',(1.0,1.3),(.5,.5,.6,.45),flick=1)
sh(225.8,'e3_pulley',(1.5,2.1),(.5,.45,.62,.42))
sh(231.0,'e3_pulley',(1.8,2.0),(.15,.75,.18,.75))
sh(234.1,'e3_pulley',(2.0,2.3),(.62,.72,.62,.74))
sh(237.1,'e3_pulley',(2.0,2.3),(.83,.85,.83,.86))
sh(240.0,'e3_funicular',(1.1,1.6),(.6,.35,.55,.3))
sh(248.6,'e3_funicular',(1.6,2.0),(.52,.32,.56,.28))
sh(254.7,'bottle_cable',(1.2,1.6),(.4,.4,.6,.45))
sh(256.8,'e3_syringe_box',(1.0,1.6),(.6,.5,.58,.5))
sh(265.0,'crowd_under',(1.0,1.5),(.6,.35,.55,.72))
sh(270.4,'e3_funicular',(1.3,1.9),(.5,.6,.47,.72),punch=1.8)
# ---------- PARTE 14 ----------
card(273.8,'GIORNO 66')
sh(275.8,'empty_pantry',(1.0,1.35),(.5,.5,.6,.55))
sh(286.6,'e1_stairs',(1.0,1.35),(.5,.5,.5,.5))
sh(292.9,'key_board',(1.2,1.7),(.55,.42,.6,.45))
sh(296.8,'e1_stairs_shadow',(1.0,1.35),(.5,.5,.5,.55))
sh(300.5,'e3_giulia_down',(1.0,1.2),(.5,.5,.48,.55))
sh(306.2,'e3_ear_floor',(1.0,1.35),(.5,.5,.35,.3))
sh(312.5,'e3_giulia_down',(1.6,2.4),(.47,.6,.45,.62))
sh(316.9,'e3_robe_woman',(1.0,1.4),(.5,.5,.4,.42))
sh(324.0,'fingers_door',(1.8,2.4),(.55,.82,.62,.82))
sh(326.0,'e3_robe_woman',(1.1,1.35),(.55,.5,.55,.5),punch=.2)
# ---------- PARTE 15 ----------
sh(328.3,'e3_robe_woman',(1.6,2.3),(.4,.35,.38,.32),shake=[[2.1,3.9],.35,4])
sh(333.8,'e3_robe_turns',(1.2,1.4),(.5,.5,.5,.45))
sh(339.7,'e3_robe_turns',(1.6,2.1),(.73,.55,.73,.5))
sh(342.9,'e3_walk_among',(1.0,1.4),(.5,.5,.48,.4))
sh(350.1,'e3_rice',(1.0,1.35),(.5,.5,.55,.5))
card(355.0,'GIORNO 70')
sh(356.9,'e1_shutters_night',(1.0,1.4),(.5,.5,.35,.45))
sh(364.0,'e3_basket_night',(1.0,1.5),(.5,.5,.55,.6))
sh(368.3,'e3_note_blank',(1.0,1.4),(.5,.5,.55,.45),flick=1)
sh(378.3,'e3_note_blank',(1.6,1.75),(.56,.45,.56,.45),flick=1,hand=[dict(t0=.2,t1=.95,text='La medicina',x=.47,y=.40,size=.024,rot=-9),dict(t0=1.8,t1=2.65,text='non è medicina.',x=.46,y=.465,size=.024,rot=-9)])
card(381.9,'GIORNO 84')
sh(383.9,'e3_funicular',(1.2,1.25),(.5,.4,.5,.4),dim=[0,.3])
sh(389.7,'e3_quarantine',(1.2,1.5),(.5,.5,.45,.5))
sh(393.9,'e3_wall_ultima_blank',(1.0,1.25),(.45,.45,.4,.45))
sh(400.9,'e3_wall_ultima_blank',(1.15,1.28),(.37,.45,.36,.45),ov=[dict(k='ultima',t0=.2,t1=1.0)],punch=.25,shake=[[.25],.4,7])
# ---------- PARTE 16 ----------
card(402.6,'GIORNO 87')
sh(405.2,'e3_basket_night',(1.3,1.5),(.6,.6,.6,.62),dim=[0,.3])
sh(409.9,'e3_lockin',(1.0,1.25),(.5,.5,.45,.5))
sh(412.9,'wedge_door',(1.6,1.9),(.45,.78,.45,.83))
sh(416.2,'e3_vigil2',(1.0,1.2),(.5,.5,.5,.5))
sh(418.8,'e3_vigil2',(1.5,1.9),(.6,.55,.62,.5))
sh(423.8,'e1_antonelli',(1.3,1.7),(.5,.55,.5,.62))
sh(428.2,'e3_vigil2',(1.1,1.3),(.5,.5,.45,.5))
sh(432.4,'e3_tap',(1.0,1.3),(.5,.5,.5,.6))
sh(434.2,'crowd_under',(1.0,1.3),(.5,.5,.5,.65),g=['#0a1430',.35])
sh(439.3,'e3_vigil2',(1.5,1.8),(.5,.4,.5,.38))
card(442.2,'GIORNO 88')
sh(443.8,'e3_pulse_v3',(1.4,1.8),(.5,.62,.5,.62))
sh(448.2,'e3_pen_line',(1.8,2.2),(.5,.72,.5,.74))
sh(451.0,'e1_door_sit',(1.0,1.3),(.5,.5,.55,.55))
card(456.2,'GIORNO 90')
sh(457.7,'e3_vigil2',(1.2,1.5),(.5,.5,.6,.5))
sh(461.8,'e3_vigil2',(1.5,2.0),(.7,.45,.75,.4))
sh(467.9,'e3_tub',(1.0,1.4),(.5,.5,.45,.62))
sh(474.8,'e3_injection',(1.0,1.3),(.5,.5,.6,.45),dim=[0,.3])
sh(480.8,'vanphone',(1.0,1.35),(.5,.5,.4,.5))
sh(485.9,'e3_robe_turns',(1.3,1.5),(.4,.4,.42,.42))
sh(487.8,'e3_walk_among',(1.0,1.3),(.5,.5,.5,.42))
sh(492.4,'e3_van_rescue',(1.2,1.6),(.4,.45,.42,.45),dim=[0,.25])
sh(499.5,'e3_final_roof',(1.0,1.15),(.35,.5,.3,.45))
sh(501.1,'e3_wall_testaq_clean',(1.0,1.25),(.5,.45,.5,.5))
sh(507.1,'e3_wall_testaq_clean',(1.6,1.75),(.47,.52,.47,.53),swap=dict(img='e3_wall_testaq',t0=.1,t1=.55),punch=.15,shake=[[.15],.4,6])
sh(508.4,'photo_sis',(1.1,1.4),(.5,.5,.5,.48))
sh(511.1,'e3_final_roof',(1.0,1.3),(.5,.5,.6,.55))
sh(515.6,'e3_final_roof',(1.5,2.3),(.6,.55,.6,.58),pulse=[.8,'#401010',.15])
cards=[
 dict(t=0.8,d=3.0,ic='clock',l='GIORNO',v='60'),
 dict(t=46.0,d=2.6,ic='clock',l='ANTONELLI',v='10 MIN'),
 dict(t=49.2,d=2.4,ic='dead',l='LA PIAZZA',v='1 ORA'),
 dict(t=89.4,d=3.4,ic='syr',l='DOSE',v='OGNI 3 GIORNI'),
 dict(t=98.6,d=2.6,ic='syr',l='PROSSIMA DOSE',v='2 GIORNI'),
 dict(t=104.8,d=3.0,ic='drop',l='PREZZO',v='200 L'),
 dict(t=148.6,d=2.8,ic='clock',l='SAPONE',v='',count=[0,20],unit=' SEC'),
 dict(t=186.3,d=2.4,ic='clock',l='POLSO',v='15 SEC × 4'),
 dict(t=189.0,d=2.8,ic='heart',l='BATTITO',v='62'),
 dict(t=248.7,d=1.45,ic='drop',l='GIÙ',v='5 KG'),
 dict(t=250.2,d=2.4,ic='syr',l='SU',v='5 KG'),
 dict(t=254.8,d=2.4,ic='drop',l='BOTTIGLIE GIÙ',v='',count=[0,40],unit=' '),
 dict(t=272.2,d=1.5,ic='dead',l='MORTI IN PIAZZA',v='',count=[60,71]),
 dict(t=284.9,d=2.8,ic='food',l='CIBO',v='8 GIORNI',red=1),
 dict(t=389.9,d=3.4,ic='syr',l='PROSSIMA DOSE',v='GIORNO 87'),
 dict(t=434.3,d=4.4,ic='dead',l='SOTTO LA FINESTRA',v='71'),
 dict(t=445.9,d=2.4,ic='heart',l='BATTITO',v='64'),
 dict(t=451.1,d=1.8,ic='clock',l='RITARDO',v='12 ORE'),
 dict(t=452.9,d=1.5,ic='clock',l='RITARDO',v='24 ORE'),
 dict(t=454.5,d=1.6,ic='clock',l='RITARDO',v='48 ORE',red=1),
 dict(t=458.8,d=2.8,ic='clock',l='SENZA MEDICINA',v='72 ORE',red=1),
]
json.dump(dict(shots=S,cards=cards,total=T),open('plan.json','w'))
print(len(S),'fallback:',sorted(set(MISS)))
