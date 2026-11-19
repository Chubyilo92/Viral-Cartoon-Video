"""CoupleIn remakes of @lovelee_app's animated reels over 20k views (scanned 19 Nov 2026).
One dict per video: source reel, its exact length, song, exact hashtags, our caption and our questions.
Questions are new (Bond-style: first person, things your partner can actually answer)."""

APP = "more questions for you two on CoupleIn, free on the app store 💕"
FLAT1 = ['#c4677e', '#5d68b3', '#d8893a', '#6b7f3f', '#8a62b8']
FLAT2 = ['#d0784a', '#3f7f86', '#b85a78', '#6a5fb0', '#7a8a3a']
FLAT3 = ['#6a5fb0', '#c98a3a', '#3f8a7a', '#c4677e', '#5a74b8']

def V(n, slug, src, views, target, song, tags, theme, title, sub, items, cap, **kw):
    d = dict(n=n, slug=slug, src=src, views=views, target=target, song=song, hashtags=tags, theme=theme,
             title=title, sub=sub, items=[dict(q=q, opts=o) for q, o in items], caption=cap + "\n\n" + APP + "\n\n" + tags)
    d.update(kw); return d

O = None
VIDEOS = [
V(1, 'ci-01-has-to-answer', 'DehJPbND6_R', '1.4M', 18.219, 'original audio (use source)', '#boyfriend #couples #thisorthat #couplequestions',
  'flat', '5 questions your boyfriend has to answer', '(no "both" allowed)',
  [("my hugs or my kisses?", ['hugs', 'kisses']), ("my cooking or my playlist?", ['cooking', 'playlist']),
   ("a lie-in with me or a day out with me?", ['lie-in', 'day out']), ("my voice notes or my texts?", ['voice notes', 'texts']),
   ("me in your jumper or me dressed up?", ['your jumper', 'dressed up'])],
  '5 questions your boyfriend has to answer (no "both" allowed) 😤 send it to him', label='pick one. no "both".', numbered=True, colors=FLAT1, title_bg='#3f7f86'),

V(2, 'ci-02-nosy', 'Dd1X6u-JpGi', '838K', 18.203, 'original audio (use source)', '#boyfriend #couples #love',
  'flat', 'lowkey nosy questions to ask your boyfriend', '',
  [("what did you tell your mates about me after our first date?", O), ("which of my photos is your lock screen in your head?", O),
   ("what was the first thing you noticed about me?", O), ("when did you know you were done for?", O),
   ("what do you secretly hope i say yes to one day?", O)],
  'nosy questions to ask your bf 👀', label='questions for him', solo=True, colors=['#7a5a4a', '#c4677e', '#5d68b3', '#d8893a', '#3f7f86'], title_bg='#c4677e'),

V(3, 'ci-03-uncomfortable', 'DeQHom3Eavy', '741K', 18.219, 'KLUSTRAK - If You Fall, I\'ll Fall Too', '#boyfriend #couples #couplequestions #questionsforcouples',
  'flat', '5 slightly uncomfortable questions to ask your boyfriend', 'no lying allowed',
  [("what's one thing i do that you pretend not to notice?", O), ("which of my habits have you picked up?", O),
   ("what's the pettiest thing i've ever been right about?", O), ("what did you think of me the first time we argued?", O),
   ("what's something you've never told me because you thought i'd laugh?", O)],
  '5 slightly uncomfortable questions to ask your boyfriend 😬 no lying allowed', label='questions for him', colors=FLAT2, title_bg='#5d68b3'),

V(4, 'ci-04-rate-me', 'De65sohDzLF', '456K', 26.007, 'original audio (use source)', '#girlfriend #couples #rateme #couplequestions',
  'beach', 'let your girlfriend rate you (out of 10)', 'the last one is the best',
  [("rate my driving out of 10", O), ("rate my cooking out of 10", O), ("rate my texting out of 10", O), ("rate my dance moves out of 10", O),
   ("rate how annoying i am out of 10", O), ("rate my rizz out of 10", O), ("rate my hugs out of 10", O), ("rate how lucky you are out of 10", O)],
  'let your girlfriend rate you (out of 10) 🙈 the last one is the best. send it to her and see what she says', kind='rate', sign='rate me out of 10'),

V(5, 'ci-05-aww-eww', 'Dec9YH1iBhp', '322K', 18.219, 'Gold-Tiger - Funny', '#couples #awworeww #couplequestions #boyfriend',
  'flat', 'aww or eww? couples edition', '(comment like 1 aww, 2 eww)',
  [("sharing a straw", ['aww', 'eww']), ("matching pyjamas", ['aww', 'eww']), ("a shared phone wallpaper", ['aww', 'eww']),
   ("reading each other's texts out loud", ['aww', 'eww']), ("a pet name in public", ['aww', 'eww'])],
  'aww or eww? couples edition 😭 comment your answers like 1 aww 2 eww', label='aww or eww?', numbered=True, colors=['#b85a78', '#5a74b8', '#d0884a', '#3f8a7a', '#8a62b8'], title_bg='#3f7f86'),

V(6, 'ci-06-gf-quiz-5', 'Dfc-TcpAv-A', '205K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequiz #couplequestions',
  'beach', 'can your bf pass this girlfriend quiz?', 'pt 5 (he needs 4/5)',
  [("what's my comfort food?", ['pasta', 'pizza', 'chocolate', 'anything you cook']), ("what's my love language?", ['words', 'quality time', 'gifts', 'physical touch']),
   ("what do i do when i'm stressed?", ['go quiet', 'clean', 'call my mum', 'eat']), ("what would i pick for date night?", ['cinema', 'dinner out', 'night in', 'a walk']),
   ("what makes me laugh the most?", ['you', 'tiktoks', 'my friends', 'my own jokes'])],
  'can your bf pass this girlfriend quiz? pt 5 😏 send it to him. he needs at least 4/5', sign='gf quiz'),

V(7, 'ci-07-only-she-knows', 'De7YltNDa-G', '155K', 18.219, 'original audio (use source)', '#girlfriend #couples #couplequestions #cutequestions',
  'beach', 'only your girlfriend can answer these', '(answer like 1A 2C)',
  [("when did you first miss me?", ['day one', 'first week', 'first month', 'still do']), ("my best feature?", ['my smile', 'my eyes', 'my hugs', 'my humour']),
   ("our best date so far?", ['the first one', 'the trip', 'a random night in', 'not had it yet']), ("who said \"i love you\" first?", ['me', 'you', 'at the same time', 'still waiting']),
   ("what would you steal from me?", ['my hoodie', 'my food', 'my side of the bed', 'my heart (again)'])],
  'only your girlfriend can answer these 🤍 send it to her. answer like 1A 2C', sign='only she knows', numbered=True),

V(8, 'ci-08-has-to-pick', 'De9-BTkH80i', '150K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequestions #thisorthat',
  'beach', 'your boyfriend has to pick', 'no skipping',
  [("cuddles or kisses?", ['cuddles', 'kisses']), ("my laugh or my smile?", ['laugh', 'smile']), ("date night in or out?", ['in', 'out']),
   ("my texts or my voice notes?", ['texts', 'voice notes']), ("our first date or our next one?", ['first', 'next'])],
  'your boyfriend has to pick. no skipping 😤 send it to him and make him answer like 1A 2B', sign='no skipping', numbered=True),

V(9, 'ci-09-uncomfortable-4', 'De5T0wVlxmi', '150K', 18.219, 'KLUSTRAK - If You Fall, I\'ll Fall Too', '#boyfriend #couples #couplequestions #questionsforcouples',
  'flat', '5 slightly uncomfortable questions to ask your boyfriend', 'part 4. no lying allowed',
  [("what's one thing i say that you'll never forget?", O), ("which of my friends do you secretly like most?", O),
   ("what's the most dramatic thing i've done that you still think about?", O), ("when do you find me most annoying?", O),
   ("what do you think i'd change about you if i could?", O)],
  '5 slightly uncomfortable questions to ask your boyfriend pt 4 😬 no lying allowed', label='questions for him', colors=FLAT3, title_bg='#c4677e'),

V(10, 'ci-10-gf-quiz-4', 'DfOAgf6CD0z', '145K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequiz #couplequestions',
  'beach', 'can your bf pass this girlfriend quiz?', 'pt 4 (he needs 4/5)',
  [("what do i always order at a restaurant?", ['the same thing', 'whatever you get', 'something new', 'i steal yours']), ("my go-to sleep position?", ['on my side', 'starfish', 'on you', 'stealing the duvet']),
   ("what's my biggest pet peeve?", ['loud chewing', 'being late', 'dry texts', 'messy rooms']), ("which song is \"our song\"?", ['the first one', 'the car one', 'we don\'t have one', 'trick question']),
   ("what would i grab first in a fire?", ['my phone', 'you', 'the dog', 'my skincare'])],
  'can your bf pass this girlfriend quiz? pt 4 😏 send it to him. he needs at least 4/5', sign='gf quiz'),

V(11, 'ci-11-too-shy', 'Dfin7ujmXOc', '136K', 18.219, 'KLUSTRAK - If You Fall, I\'ll Fall Too', '#boyfriend #couples #couplequestions #questionsforhim',
  'beach', '5 questions i\'m too shy to ask my boyfriend', '(especially #5)',
  [("what did you think of me on our first date?", O), ("what's your favourite thing i do without noticing?", O), ("when do you feel closest to me?", O),
   ("what's something about me you'd never change?", O), ("do you think about our future as much as i do?", O)],
  '5 questions i\'m too shy to ask my boyfriend (especially #5) 🙈 so i\'m posting them instead. send it to him', numbered=True),

V(12, 'ci-12-really-likes-you', 'DenSQr9iqBf', '115K', 18.219, 'Olivia Rodrigo - stupid song', '#boyfriend #couples #couplequestions #questionsforcouples',
  'flat', '5 questions to see if your bf REALLY likes you', 'they get more niche',
  [("what's my coffee order?", O), ("what do i do when i'm nervous?", O), ("what's my most-used emoji with you?", O),
   ("what did i wear on our first date?", O), ("what's the one food i'll never share?", O)],
  '5 questions to see if your bf REALLY likes you 👀 they get more niche. send it to him and see what he says', label='questions for him', numbered=True, colors=FLAT2, title_bg='#8a62b8'),

V(13, 'ci-13-know-him', 'DemT2I_lByW', '107K', 18.219, 'NEIKED, Portugal. The Man - Glide', '#boyfriend #couples #couplequiz #couplequestions',
  'flat', 'do you actually know your boyfriend?', '(pick the right options)',
  [("his comfort film?", ['an action one', 'a kids\' film', 'a comedy', 'anything with you']), ("his perfect sunday?", ['footy', 'lie-in', 'gym', 'you, sofa, food']),
   ("what makes him jealous?", ['nothing (he says)', 'your gym guy', 'your ex', 'your phone']), ("his dream holiday?", ['beach', 'city break', 'road trip', 'anywhere with you']),
   ("what he says when he's hungry?", ['"i\'m fine"', '"what\'s for dinner"', 'nothing, just sulks', '"order something"'])],
  'do you actually know your boyfriend? 👀 pick the right options, then make him check', label='know him?', numbered=True, colors=FLAT1, title_bg='#3f8a7a'),

V(14, 'ci-14-gf-quiz-6', 'Dfs6D1uinal', '100K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequiz #couplequestions',
  'beach', 'can your bf pass this girlfriend quiz?', 'pt 6 (he needs 4/5)',
  [("my dream date?", ['a picnic', 'a fancy dinner', 'a trip away', 'a night in']), ("how do i like to be cheered up?", ['food', 'a hug', 'a walk', 'leave me alone']),
   ("my favourite season?", ['spring', 'summer', 'autumn', 'christmas, obviously']), ("what do i call you in my phone?", ['your name', 'a pet name', 'an emoji', 'something embarrassing']),
   ("what's my hidden talent?", ['singing', 'parking', 'remembering everything', 'falling asleep anywhere'])],
  'can your bf pass this girlfriend quiz? pt 6 😏 send it to him. he needs at least 4/5', sign='gf quiz'),

V(15, 'ci-15-nosy-2', 'Dd9K3xvJjxy', '89.1K', 18.203, 'original audio (use source)', '#boyfriend #couples #questionsforcouples',
  'flat', 'more nosy questions to ask your boyfriend', 'part 2',
  [("what's the first thing you'd notice if i changed?", O), ("which of our photos do you look at most?", O), ("what did you say about me to your mum?", O),
   ("what's a moment with me you replay in your head?", O), ("when did you last think \"i'm lucky\"?", O)],
  'more nosy questions to ask your boyfriend 👀 part 2', label='questions for him', solo=True, colors=['#c4677e', '#5d68b3', '#7a5a4a', '#3f7f86', '#d8893a'], title_bg='#8a62b8'),

V(16, 'ci-16-extra-sweet-3', 'De0KPcXlanT', '87.6K', 18.219, 'KLUSTRAK - If You Fall, I\'ll Fall Too', '#boyfriend #couples #couplequestions #sweetquestions',
  'flat', '5 extra sweet questions to ask your boyfriend', 'pt 3',
  [("what's your favourite memory of us so far?", O), ("what made you want to keep texting me?", O), ("what do you love most about our mornings?", O),
   ("what's one thing i do that makes you feel looked after?", O), ("what do you want us to do together this year?", O)],
  '5 extra sweet questions to ask your boyfriend 🥹 pt 3. send it to him tonight', label='questions for him', colors=FLAT3, title_bg='#b85a78'),

V(17, 'ci-17-gf-quiz-flat', 'DeiHfNoAvBV', '71.2K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequiz #couplequestions',
  'flat', 'can your bf pass this girlfriend quiz?', 'send it to him (he needs 4/5)',
  [("my favourite snack?", ['crisps', 'chocolate', 'fruit (lies)', 'whatever you\'re eating']), ("what do i do first when i get home?", ['take my bra off', 'get a snack', 'lie down', 'call you']),
   ("my most used app?", ['tiktok', 'instagram', 'CoupleIn', 'whatsapp']), ("what i'd choose on a free day?", ['shopping', 'sleep', 'a walk', 'you']),
   ("how i take my tea?", ['milk, one sugar', 'just milk', 'no tea, coffee', 'i don\'t'])],
  'can your bf pass this girlfriend quiz? 😏 send it to him. he needs at least 4/5', label='gf quiz', numbered=True, colors=['#b85a78', '#5a74b8', '#c98a3a', '#3f8a7a', '#8a62b8'], title_bg='#c4677e'),

V(18, 'ci-18-nosy-3', 'DeDQklsJRDI', '69.4K', 18.203, 'original audio (use source)', '#boyfriend #couples #questionsforcouples',
  'flat', 'lowkey nosy questions to ask your boyfriend', 'part 3',
  [("what's the cheesiest thing you've thought about me?", O), ("when did you first want to kiss me?", O), ("what do you tell people when they ask about me?", O),
   ("what's your favourite outfit of mine?", O), ("what's the next thing you want to do with me?", O)],
  'lowkey nosy questions to ask your boyfriend 👀 part 3', label='questions for him', solo=True, colors=['#5d68b3', '#d8893a', '#c4677e', '#6b7f3f', '#8a62b8'], title_bg='#d06a7a'),

V(19, 'ci-19-gf-quiz-flat-2', 'DeUxLI7E7-J', '60.6K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequiz #couplequestions',
  'flat', 'can your bf pass this girlfriend quiz?', 'send it to him (he needs 4/5)',
  [("my favourite colour?", ['pink', 'black', 'green', 'it changes weekly']), ("what scares me most?", ['spiders', 'the dark', 'losing you', 'heights']),
   ("my celebrity crush?", ['an actor', 'a singer', 'a footballer', 'you (correct)']), ("my worst habit?", ['phone in bed', 'being late', 'overthinking', 'stealing chips']),
   ("what i'd name our dog?", ['something cute', 'a human name', 'a food', 'we\'re not getting a dog'])],
  'can your bf pass this girlfriend quiz? 😏 send it to him. he needs at least 4/5', label='gf quiz', numbered=True, colors=['#6b7f3f', '#c4677e', '#5d68b3', '#d8893a', '#8a62b8'], title_bg='#5f8a5a'),

V(20, 'ci-20-would-you-rather', 'Dd9vXq3JRr3', '57.1K', 18.203, 'The Two Lips - still love you (todavía)', '#couples #wouldyourather #boyfriend',
  'flat', 'would you rather: couples edition', 'answer in the comments',
  [("never fight again or always make up in 5 minutes?", ['never fight', '5-min makeup']), ("a surprise trip or a surprise party?", ['trip', 'party']),
   ("read my mind for a day or me read yours?", ['read mine', 'i read yours']), ("relive our first date or skip to our wedding?", ['first date', 'wedding']),
   ("a love letter or a playlist?", ['letter', 'playlist'])],
  'would you rather: couples edition 🥹 answer in the comments', label='would you rather', numbered=True, colors=['#8a62b8', '#d0784a', '#3f7f86', '#c4677e', '#5d68b3'], title_bg='#6a5fb0'),

V(21, 'ci-21-uncomfortable-2', 'DecAtCpFdoT', '40.9K', 18.219, 'KLUSTRAK - If You Fall, I\'ll Fall Too', '#boyfriend #couples #couplequestions #questionsforcouples',
  'flat', '5 slightly uncomfortable questions to ask your boyfriend', 'no lying allowed',
  [("what's something i do that reminds you of your mum?", O), ("what did you get wrong about me at first?", O), ("which argument do you think you actually won?", O),
   ("what's the most jealous you've been about me?", O), ("what would you never forgive me for?", O)],
  '5 slightly uncomfortable questions to ask your boyfriend 😬 no lying allowed', label='questions for him', colors=FLAT1, title_bg='#3f7f86'),

V(22, 'ci-22-no-sugarcoating', 'DeE57WkJAnJ', '39.9K', 18.203, 'girl in red - we fell in love in october', '#couples #couplequestions #boyfriend #questionsforcouples',
  'flat', 'ask him this... no sugarcoating', '(answer like 1A 2C)',
  [("when did you know?", ['first date', 'first month', 'first fight', 'not yet (wrong)']), ("my worst trait?", ['stubborn', 'dramatic', 'always late', 'perfect, actually']),
   ("who apologises first?", ['me', 'you', 'whoever\'s hungry', 'nobody']), ("what would you change about us?", ['more dates', 'less phones', 'nothing', 'more sleep']),
   ("where do you see us in 5 years?", ['same place', 'travelling', 'married', 'a dog, at least'])],
  'ask him this... no sugarcoating 👀 send him this, make him answer like 1A 2C', label='no sugarcoating', numbered=True, colors=['#5d68b3', '#c4677e', '#d8893a', '#3f8a7a', '#8a62b8'], title_bg='#7a6fb8'),

V(23, 'ci-23-who-fell-first', 'DfddxR3FId3', '35.7K', 18.219, 'original audio (use source)', '#couples #boyfriend #couplequestions #whofellfirst',
  'beach', 'who caught feelings first?', '5 questions about how it started',
  [("who texted first?", ['you', 'me']), ("who said \"i miss you\" first?", ['you', 'me']), ("who was more nervous on the first date?", ['you', 'me']),
   ("who stalked whose instagram first?", ['you', 'me']), ("who fell harder?", ['you', 'me'])],
  'who caught feelings first? 🥹 5 questions about how it started. send it to him', numbered=True, sign='how it started'),

V(24, 'ci-24-annoy-him', 'DeW2gIWjpHM', '33.2K', 18.219, 'Gold-Tiger - Funny', '#boyfriend #couples #couplequestions #funnyquestions',
  'flat', 'go annoy your boyfriend with these 5 questions', '(he has to answer all of them)',
  [("if i was a worm, would you still love me?", O), ("who would you save first, me or your mum?", O), ("what would you do if i became a cat?", O),
   ("which of my exes was the worst?", O), ("if we met today, would you still text me back?", O)],
  'go annoy your boyfriend with these 5 questions 😈 he has to answer all of them', label='he has to answer', colors=FLAT2, title_bg='#8a62b8'),

V(25, 'ci-25-if-we-had-a-kid', 'DfgCmFEHKuf', '28.6K', 18.219, 'original audio (use source)', '#couples #couplequestions #futureus #boyfriend',
  'beach', 'if we had a kid together...', 'be honest (you or me?)',
  [("who'd be the strict one?", ['you', 'me']), ("who'd cry on the first day of school?", ['you', 'me']), ("who'd be the fun parent?", ['you', 'me']),
   ("who'd do the night feeds?", ['you', 'me']), ("who would they like more?", ['you', 'me'])],
  'if we had a kid together… be honest 👶 comment your answers like 1 you 2 me', numbered=True, sign='future us'),

V(26, 'ci-26-extra-sweet', 'DeMi0a0FGcE', '24.9K', 18.219, 'KLUSTRAK - If You Fall, I\'ll Fall Too', '#boyfriend #couples #couplequestions #questionsforcouples',
  'flat', '5 extra sweet questions to ask your boyfriend', '',
  [("what was your first thought when you saw me?", O), ("what's your favourite way i say your name?", O), ("when do you feel most loved by me?", O),
   ("what's a song that makes you think of me?", O), ("what do you love about us that nobody else sees?", O)],
  '5 extra sweet questions to ask your boyfriend 🥹', label='questions for him', colors=FLAT3, title_bg='#c98a3a'),

V(27, 'ci-27-funny', 'DeVQt3REUmH', '23.6K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequestions #questionsforcouples',
  'flat', '5 funny questions to ask your boyfriend', '(see how well he actually knows you)',
  [("what would i be famous for?", O), ("what's my most dramatic sentence?", O), ("which animal am i when i'm hungry?", O),
   ("what would my villain name be?", O), ("what would i do with a million pounds first?", O)],
  '5 funny questions to ask your boyfriend 😂 see how well he actually knows you', label='questions for him', colors=FLAT1, title_bg='#6a5fb0'),

V(28, 'ci-28-might-cry', 'DfnxpKgk8Sz', '21.2K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequestions #deepquestions',
  'beach', 'ask your boyfriend these 5 questions', '(the last one might make him cry)',
  [("what do you love about us?", O), ("when did you feel proudest of me?", O), ("what's one thing you've never thanked me for?", O),
   ("what do you want our home to feel like?", O), ("what would you say to me if this was our last day?", O)],
  'ask your boyfriend these 5 questions (the last one might make him cry) 🥺 send it to him', numbered=True),

V(29, 'ci-29-insanely-cute', 'DfDmZA9nUfa', '21.2K', 18.219, "Armando Trovajoli - L'amore dice Ciao (Main Titles) (Remastered)", '#boyfriend #couples #couplequestions #cutequestions',
  'beach', 'insanely cute questions to ask your boyfriend', 'he has to answer all 5',
  [("what's your favourite photo of us?", O), ("what nickname would you give me?", O), ("what's the cutest thing i've ever done?", O),
   ("which day with me would you relive?", O), ("what do you miss most when i'm not there?", O)],
  'insanely cute questions to ask your boyfriend 🥹 send it to him and make him answer all 5', numbered=True),

V(30, 'ci-30-gf-quiz-3', 'DezqtWjkXOa', '20K', 18.219, 'original audio (use source)', '#boyfriend #couples #couplequiz #couplequestions',
  'beach', 'can your bf pass this girlfriend quiz?', 'pt 3 (he needs 4/5)',
  [("my go-to karaoke song?", ['a ballad', 'a throwback', 'a rap', 'i\'d never']), ("what's my favourite takeaway?", ['chinese', 'indian', 'pizza', 'nandos']),
   ("what makes me cry every time?", ['films', 'adverts', 'animals', 'onions']), ("how do i say sorry?", ['with food', 'with a hug', 'with a text', 'i don\'t']),
   ("which day of the week is my favourite?", ['friday', 'saturday', 'sunday', 'any day with you'])],
  'can your bf pass this girlfriend quiz? pt 3 😏 send it to him. he needs at least 4/5', sign='gf quiz'),
]
for v in VIDEOS:
    assert len(v['items']) in (5, 8), v['slug']
