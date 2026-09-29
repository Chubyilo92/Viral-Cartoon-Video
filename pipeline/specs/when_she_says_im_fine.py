import sys; sys.path.insert(0,'/home/claude/jj')
import jjlib as J
TITLE = "when she says 'i'm fine'"
BODY_LINES = [
"When she says... \"I'm fine\"... she's not always fine. She's waiting to see if you'll notice.",
"She might go quiet after a long day. Not to punish you. She's just tired of explaining the same hurt twice.",
"She might bring up something small from last week. It's not about the dishes. It's about feeling heard.",
"She doesn't need you to fix it. She needs you to put the phone down... and ask, what's really wrong.",
"If you're the one who goes quiet... send this to the one who keeps asking.",
"But if you only listen when it's easy... one day, she'll stop telling you.",
"Because the girl who still tells you what's wrong... is the girl who still wants to make it work.",
]
SCENES = J.split_scenes(J.SRC2)[:7]
IG_LINE = "The quiet. The dishes. Being asked, what's really wrong. Every girl shows love in her own way... Want to know hers? There's a sixty second test in our bio. Take it together... and see if he knows yours."
IG_CAPS = ["the quiet 🤫","the dishes 🍽️","being asked","what's really wrong 💭","every girl shows","love in her own way 🤍","want to know hers?","60-second test","in our bio 🔗","take it together","and see if he","knows yours 💌"]
IG_RESULT = "Quality Time"
TT_LINE = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."
