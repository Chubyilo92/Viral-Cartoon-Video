import sys; sys.path.insert(0,'/home/claude/jj')
import jjlib as J
TITLE = "when a boy loves you"
BODY_LINES = [
"When a boy loves you... he won't always say it out loud.",
"He'll show it in small ways. He saves you the last bite... even when he's hungry.",
"He might tease you all day. Not to annoy you. It's because your smile is his favourite thing to see.",
"He might act tough... around everyone else.",
"But with you, he's soft. Because you're the one place he doesn't have to be strong.",
"He might go quiet when something's wrong. Not because he's pulling away. He just needs you close... not a hundred questions.",
"He remembers the little things. How you take your tea. The song you hum. The bad day you mentioned once.",
"But if you always have to ask... if he only shows up when it's easy... maybe he's not the one.",
"Because when a boy truly loves you... you'll never have to wonder.",
]
SCENES = [x[:-1] if x.endswith('}}]') else x for x in J.split_scenes(J.SRC1)[:9]]
IG_LINE = "The last bite. The tea. Sitting close when it's hard. Every boy shows love in his own way... Want to know his? There's a sixty second test in our bio. Take it together... and see if he knows yours."
IG_CAPS = ["the last bite 🦴","the tea ☕","sitting close","when it's hard 🫂","every boy shows","love in his own way 🤍","want to know his?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
