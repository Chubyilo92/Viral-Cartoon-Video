import sys, os; sys.path.insert(0, '/home/claude/ep')
from engine import render
from mix import mix
I = lambda n: f'/home/claude/ep/img/TQR_calcio_{n}.jpg'
VOICE = '/mnt/user-data/uploads/410b58a4-Testaquadrata_calcio.m4a'

def sh(img, t0, t1, z=(1.0, 1.1), c=((.5, .5), (.5, .5)), **k):
    d = dict(img=I(img), t0=t0, t1=t1, z=z, c=c); d.update(k); return d

shots = [
    sh('c01', 0.0, 3.3, (1.0, 1.15), ((.5, .5), (.5, .45))),
    sh('c02', 3.3, 8.6, (1.0, 1.15), ((.5, .5), (.5, .45)), shake=[6.7]),
    sh('c03', 8.6, 17.0, (1.0, 1.2), ((.5, .5), (.5, .42))),
    sh('c04', 17.0, 21.2, (1.0, 1.12)),
    sh('c05', 21.2, 26.4, (1.0, 1.15), ((.5, .55), (.5, .5))),
    sh('c06', 26.4, 32.8, (1.0, 1.22), ((.5, .55), (.5, .5))),
    sh('c04', 32.8, 38.0, (1.12, 1.2)),
    sh('c07', 38.0, 43.0, (1.0, 1.12)),
    sh('c08', 43.0, 47.3, (1.0, 1.15)),
    sh('c09', 47.3, 52.4, (1.0, 1.1)),
    sh('c10', 52.4, 57.2, (1.0, 1.12)),
    sh('c11', 57.2, 60.7, (1.0, 1.15), ((.5, .55), (.5, .45))),
    sh('c12', 60.7, 65.2, (1.2, 1.35), ((.45, .72), (.45, .68))),
    sh('c12', 65.2, 67.1, (1.35, 1.6), ((.45, .68), (.5, .35))),
    sh('c13', 67.1, 70.5, (1.0, 1.2), ((.5, .5), (.5, .42)), shake=[67.2]),
    sh('c14', 70.5, 74.6, (1.0, 1.12)),
    sh('c16', 74.6, 77.8, (1.0, 1.2), shake=[75.0]),
    sh('c15', 77.8, 83.5, (1.0, 1.25)),
    sh('c11', 83.5, 92.0, (1.15, 1.2), ((.5, .45), (.5, .45))),
]
caps = [
 (0.84, 2.6, "Ultima giornata di Serie C."), (3.36, 4.5, "Ultimo minuto."), (5.01, 6.0, "Uno a uno."), (6.72, 7.9, "Rigore per voi."),
 (8.79, 11.0, "Se segni, la squadra si salva."), (11.52, 12.6, "Se sbagli,"), (12.81, 13.8, "retrocedete."), (14.13, 15.2, "E il rigore"), (15.4, 16.6, "tocca a te."),
 (17.31, 19.3, "Guadagni 80.000 euro l'anno."), (19.86, 20.9, "Lordi."),
 (21.42, 25.5, "Ieri sera, fuori dall'albergo, uno sconosciuto ti ha dato una busta."), (26.52, 27.9, "Con dentro un biglietto:"),
 (33.15, 34.5, "Cinque milioni."), (35.10, 37.6, "Più di 60 anni del tuo stipendio."), (38.13, 40.0, "Il mutuo, chiuso."),
 (40.47, 42.8, "Il futuro di tuo figlio, sistemato."), (43.26, 44.6, "Non lo saprà mai nessuno."), (44.94, 46.8, "Un rigore sbagliato capita a tutti."),
 (47.46, 50.0, "Ma se retrocedete, la società fallisce."), (50.46, 51.9, "I tuoi compagni restano a casa."),
 (52.53, 53.9, "Anche il magazziniere,"), (54.27, 56.6, "che lavora qui da più di 30 anni."),
 (57.39, 60.5, "Vai verso il dischetto. Alzi gli occhi verso la tribuna."), (60.87, 62.4, "Fila dodici: tuo padre."),
 (62.79, 64.8, "Non si è perso una partita in vent'anni."), (65.34, 66.8, "E due file dietro di lui..."), (67.14, 68.5, "l'uomo della busta."), (68.76, 69.9, "Ti saluta."),
 (70.65, 72.1, "Il portiere sulla linea."), (72.42, 74.2, "Lo stadio ammutolisce."), (74.73, 76.6, "L'arbitro fischia."),
 (78.12, 79.2, "Cosa scegli?"), (79.68, 80.6, "Lo sbagli..."), (80.91, 81.8, "o lo segni?"), (82.26, 83.3, "Dimmi la verità."),
]
overlays = [
    dict(type='card', t0=3.36, t1=8.6, text="90'   1 - 1", y=260, size=130, color=(255, 214, 64)),
    dict(type='counter', t0=17.31, t1=21.2, to=80_000, fmt='{:,.0f} €/anno', label='IL TUO STIPENDIO', y=300, size=100),
    dict(type='card', t0=28.71, t1=32.8, text='"5.000.000 €. BASTA CHE LO SBAGLI."', y=300, size=88),
    dict(type='counter', t0=33.15, t1=38.0, to=5_000_000, label='IN UNA BUSTA', y=300),
    dict(type='card', t0=60.87, t1=65.2, text='FILA 12', y=300, size=120),
    dict(type='endcard', t0=83.5, t1=92.0, options=[('LO SBAGLIO', (190, 40, 40)), ('LO SEGNO', (40, 110, 200))],
         line1='DIMMI LA VERITÀ NEI COMMENTI', line2='LA PARTE 2 ESCE A 300 COMMENTI', line3='MANDALO AI TIFOSI PIÙ SFEGATATI'),
]
cues = [('crowd', 0, -30, 57.0), ('bed', 0, 0, 91), ('whistle', 6.6, -22), ('paper', 26.6, -24), ('thud', 33.1, -18),
        ('crowd', 57.2, -26, 72.4), ('heartbeat', 57.2, -24, 83.4), ('drop', 67.1, -14), ('whistle', 74.8, -12),
        ('riser', 80.5, -20), ('drop', 83.5, -10)]
if __name__ == '__main__':
    os.makedirs('/home/claude/ep/out', exist_ok=True)
    out = '/home/claude/ep/out/Testaquadrata_Calcio_P1.mp4'; mixp = '/home/claude/ep/out/calcio_mix.m4a'
    dur = mix(VOICE, cues, mixp)
    render(dict(dur=min(dur, 92.0), shots=shots, caps=caps, overlays=overlays, mix=mixp), out)
    print('done', out)
