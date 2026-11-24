import sys; sys.path.insert(0, '/home/claude/ep')
from engine import render
from mix import mix
I = lambda n: f'/home/claude/ep/img/TQR_soldi_{n}.jpg'
VOICE = '/mnt/user-data/uploads/b1d1cf89-Testa_quadrataSoldi.m4a'

def sh(img, t0, t1, z=(1.0, 1.1), c=((.5, .5), (.5, .5)), **k):
    d = dict(img=I(img), t0=t0, t1=t1, z=z, c=c); d.update(k); return d

shots = [
    sh('s01', 0.0, 5.5, (1.0, 1.15), ((.5, .55), (.45, .62))),
    sh('s02', 5.5, 11.9, (1.05, 1.18), ((.5, .5), (.5, .55))),
    sh('s03', 11.9, 18.2, (1.0, 1.2), ((.5, .55), (.5, .6))),
    sh('s04', 18.2, 24.2, (1.15, 1.0), ((.5, .5), (.5, .5)), flash=[21.9]),
    sh('s05', 24.2, 31.2, (1.0, 1.15), ((.5, .6), (.5, .45))),
    sh('s06', 31.2, 37.7, (1.05, 1.15), ((.45, .55), (.55, .55))),
    sh('s07', 37.7, 41.9, (1.0, 1.2), ((.5, .5), (.5, .45))),
    sh('s08', 41.9, 47.0, (1.1, 1.0), ((.5, .55), (.5, .55))),
    sh('s09', 47.0, 52.2, (1.0, 1.1), ((.5, .5), (.5, .45))),
    sh('s10b' if __import__('os').path.exists(I('s10b')) else 's10', 52.2, 58.5, (1.0, 1.25), ((.5, .5), (.5, .5)), shake=[53.6]),
    sh('s11', 58.5, 65.5, (1.0, 1.15), ((.5, .5), (.5, .45))),
    sh('s12', 65.5, 72.1, (1.0, 1.12), ((.5, .45), (.5, .4)), shake=[65.7]),
    sh('s13', 72.1, 79.0, (1.0, 1.15), ((.5, .5), (.5, .42))),
    sh('s12', 79.0, 84.6, (1.12, 1.25), ((.5, .4), (.5, .38))),
    sh('s14b' if __import__('os').path.exists(I('s14b')) else 's12', 84.6, 89.8, (1.0, 1.25), ((.5, .5), (.5, .42))),
    sh('s16', 89.8, 94.9, (1.0, 1.12), ((.5, .5), (.5, .5))),
    sh('s15', 94.9, 98.5, (1.0, 1.18), ((.5, .55), (.5, .45)), shake=[98.4]),
    sh('s16', 98.5, 104.7, (1.12, 1.3), ((.5, .5), (.5, .35))),
    sh('s16', 104.7, 113.0, (1.3, 1.35), ((.5, .35), (.5, .35))),
]
caps = [
 (0.54, 4.56, "In un'area di sosta deserta c'è un camper con la porta spalancata."),
 (5.61, 7.17, "Dentro non c'è nessuno."), (7.71, 9.6, "Solo tre trolley argentati,"), (9.96, 11.2, "uno accanto all'altro."),
 (11.97, 12.9, "Ne apri uno."), (13.41, 15.6, "Mazzette di banconote da 500."), (16.05, 17.2, "Sottovuoto."),
 (18.39, 19.6, "Poi apri il secondo."), (20.28, 21.3, "Poi il terzo."), (21.93, 23.8, "12 milioni di euro."),
 (24.30, 27.8, "E fuori dalla porta, impronte fresche nel fango."), (28.29, 30.5, "Qualcuno è scappato. Di corsa."),
 (31.32, 32.9, "Carichi i trolley in macchina."), (33.39, 34.9, "Le ruote si incastrano..."), (35.6, 36.8, "ma ce la fai."),
 (37.86, 39.9, "A casa chiudi a doppia mandata."), (40.29, 41.6, "Abbassi le tapparelle."), (42.0, 43.0, "Ti siedi per terra,"), (43.47, 44.6, "in mezzo ai soldi."),
 (45.69, 46.8, "12 milioni."), (47.25, 48.5, "Basta sveglia alle sei."), (48.93, 51.8, "Basta debiti. Una casa al mare per tua madre."),
 (52.29, 53.3, "All'improvviso,"), (53.5, 54.6, "un bip."), (55.14, 56.1, "Leggerissimo."), (56.52, 58.0, "Viene dalla maniglia di un trolley."),
 (58.65, 59.6, "La sviti."), (60.21, 62.3, "Dentro c'è un localizzatore."), (63.30, 64.8, "Con la lucina verde accesa."),
 (65.70, 69.2, "Un secondo dopo ti vibra il telefono. Numero sconosciuto:"), (72.21, 73.2, "Poi arriva una foto."),
 (74.19, 76.3, "È la tua finestra, vista da fuori."), (76.68, 78.0, "Con la tapparella abbassata."), (79.02, 80.2, "L'ultimo messaggio:"),
 (84.78, 86.2, "Hai tempo fino a mezzanotte."), (86.61, 87.6, "Guardi l'ora:"), (87.84, 89.5, "mancano 19 minuti."),
 (89.85, 93.8, "4 milioni sono tuoi. Puliti. Se riporti gli altri due."), (94.95, 97.9, "E se ti fidi di qualcuno che ti sta guardando dalla strada."),
 (98.58, 99.3, "Allora?"), (99.63, 100.9, "Riporti due trolley..."), (101.40, 102.8, "o te li tieni tutti e tre"), (103.02, 104.3, "e rischi tutto?"),
]
overlays = [
    dict(type='counter', t0=21.93, t1=24.2, to=12_000_000, label='HAI TROVATO', y=300),
    dict(type='counter', t0=45.69, t1=47.2, to=12_000_000, count=.01, y=300),
    dict(type='notif', t0=69.9, t1=72.1, text='Bel salotto.'),
    dict(type='notif', t0=81.0, t1=84.6, text='Tienine uno. Riporta gli altri due al camper.'),
    dict(type='card', t0=86.6, t1=87.84, text='23:41', y=330, color=(255, 255, 255), size=170),
    dict(type='card', t0=87.84, t1=89.8, text='19 MINUTI', y=330, color=(255, 70, 60), size=150),
    dict(type='counter', t0=89.85, t1=94.9, to=4_000_000, label='SE RIPORTI GLI ALTRI DUE', y=300),
    dict(type='endcard', t0=104.7, t1=113.0, options=[('RIPORTO', (40, 130, 70)), ('TENGO', (190, 40, 40))],
         line1='COMMENTA RIPORTO O TENGO', line2='LA PARTE 2 ESCE A 300 COMMENTI', line3='MANDALO NEL GRUPPO'),
]
cues = [('bed', 0, 0, 112), ('paper', 13.3, -26), ('thud', 21.9, -16), ('step', 29.0, -28), ('step', 29.5, -28), ('knock', 38.0, -24),
        ('beep', 53.6, -14), ('beep', 55.3, -20), ('buzz', 65.8, -16), ('buzz', 79.0, -16), ('tick', 84.6, -26, 98), ('heartbeat', 89.8, -24, 104.6),
        ('riser', 102.0, -18), ('drop', 104.7, -10)]
if __name__ == '__main__':
    out = '/home/claude/ep/out/Testaquadrata_Soldi_P1.mp4'
    import os; os.makedirs('/home/claude/ep/out', exist_ok=True)
    mixp = '/home/claude/ep/out/soldi_mix.m4a'
    dur = mix(VOICE, cues, mixp)
    render(dict(dur=min(dur, 113.0), shots=shots, caps=caps, overlays=overlays, mix=mixp), out)
    print('done', out)
