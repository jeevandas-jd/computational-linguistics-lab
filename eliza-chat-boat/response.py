"""
responses.py
------------
All the "linguistic knowledge" of the chatbot lives here, separate from the
engine in eliza.py. This is the classic ELIZA design: a reflection table
(for pronoun/person swapping) and an ordered list of (pattern, responses)
rules. The domain is college life / student counseling.

Nothing in this file does any matching or generation - eliza.py does that.
Editing THIS file is how you extend the bot's "personality" and topic
coverage without touching the engine logic.
"""

import re

# ---------------------------------------------------------------------------
# 1. REFLECTIONS
# ---------------------------------------------------------------------------
# When ELIZA echoes part of what you said back at you, it has to swap
# pronouns/person so "I am tired" -> "you are tired" instead of parroting
# "I am tired" back verbatim. This is applied only to text captured by a
# regex group (see reflect() in eliza.py), never to the whole sentence.
REFLECTIONS = {
    "i": "you",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "am": "are",
    "was": "were",
    "i'm": "you are",
    "i've": "you have",
    "i'll": "you will",
    "i'd": "you would",
    "you": "I",
    "you're": "I am",
    "you've": "I have",
    "you'll": "I will",
    "you'd": "I would",
    "your": "my",
    "yours": "mine",
    "yourself": "myself",
    "are": "am",
}

# ---------------------------------------------------------------------------
# 2. PATTERNS
# ---------------------------------------------------------------------------
# Each entry is (regex, [template, template, ...]).
# - If a template contains "{0}", the rule MUST have a capturing group in
#   its regex; whatever that group captures gets reflected (see REFLECTIONS)
#   and substituted in.
# - If a template has no "{0}", the regex can be a plain keyword and no
#   capture group is needed.
#
# ORDER MATTERS: eliza.py walks this list top to bottom and uses the first
# match. So specific, capturing "I feel ___" style rules go first, then
# domain keyword rules, then generic greeting/small-talk rules, with the
# broadest catch-alls last.
PATTERNS = [

    # --- reflective "I ___" patterns (capture + pronoun swap) ---------------
    (r"\bi need (.*)", [
        "Why do you need {0}?",
        "Would getting {0} really help?",
        "What would happen if you didn't have {0}?",
    ]),
    (r"\bi want (.*)", [
        "Why do you want {0}?",
        "What would it mean for you to have {0}?",
    ]),
    (r"\bi feel (.*)", [
        "Why do you feel {0}?",
        "What made you feel {0}?",
        "Do you often feel {0}?",
        "How long have you felt {0}?",
    ]),
    (r"\bi(?:'m| am) (.*)", [
        "Why are you {0}?",
        "How long have you been {0}?",
        "Do you enjoy being {0}?",
        "What makes you {0} right now?",
    ]),
    (r"\bi can'?t (.*)", [
        "What's stopping you from {0}?",
        "Why can't you {0}?",
        "Have you tried to {0} before?",
    ]),
    (r"\bi think (.*)", [
        "Why do you think {0}?",
        "Are you sure that {0}?",
    ]),
    (r"\bi (?:hate|dislike) (.*)", [
        "Why do you dislike {0}?",
        "What is it about {0} that bothers you?",
    ]),
    (r"\bi like (.*)", [
        "Why do you like {0}?",
        "What is special about {0}?",
    ]),
    (r"\bbecause (.*)", [
        "Is that the real reason?",
        "What other reasons come to mind?",
    ]),

    # --- domain keyword patterns (college life / student counseling) -------
    (r"\bexam(s)?\b", [
        "Are exams making you stressed?",
        "Which subject worries you the most?",
        "How is your exam preparation going?",
    ]),
    (r"\b(assignment|homework)s?\b", [
        "Assignments can be difficult.",
        "Have you started working on it yet?",
        "What subject is the assignment for?",
    ]),
    (r"\bdeadline(s)?\b", [
        "Deadlines can be a lot of pressure.",
        "How much time do you have left before the deadline?",
    ]),
    (r"\bgrade(s)?\b", [
        "How do you feel about your grades this term?",
        "Are your grades what you expected?",
    ]),
    (r"\bteacher(s)?|professor(s)?\b", [
        "Tell me more about your teacher.",
        "Do you enjoy that class?",
        "How does your teacher make you feel?",
    ]),
    (r"\bfriend(s)?\b", [
        "Friends are important in college.",
        "Would you like to talk about them?",
        "How do your friends support you?",
    ]),
    (r"\broommate(s)?\b", [
        "How are things with your roommate?",
        "Living with someone else can be tricky sometimes.",
    ]),
    (r"\b(mom|dad|mother|father|family|parents)\b", [
        "Tell me more about your family.",
        "How does your family feel about your college life?",
    ]),
    (r"\bhomesick\b", [
        "Homesickness is very common. When do you feel it most?",
        "What do you miss most from home?",
    ]),
    (r"\bmoney|broke|afford|budget\b", [
        "Financial stress is common in college. What's worrying you most?",
        "Have you looked into student financial support?",
    ]),
    (r"\bsleep|tired|exhausted|insomnia\b", [
        "How many hours have you been sleeping lately?",
        "Lack of sleep can affect everything else. What's keeping you up?",
    ]),
    (r"\bstress(ed)?|anxious|anxiety|overwhelmed\b", [
        "What do you think is causing your stress?",
        "How long have you been feeling this way?",
        "What usually helps you calm down?",
    ]),
    (r"\blonely|alone\b", [
        "Loneliness can be really hard. When do you notice it most?",
        "Have you been able to talk to anyone about feeling this way?",
    ]),
    (r"\bhappy|great|good|excited\b", [
        "That's good to hear! What's making you feel that way?",
        "I'm glad to hear that. Tell me more.",
    ]),
    (r"\bsad|depressed|down\b", [
        "I'm sorry you're feeling that way. What's been going on?",
        "How long have you felt down?",
    ]),

    # --- small talk / greetings ---------------------------------------------
    (r"^\s*(hi|hello|hey)\b", [
        "Hello! How are you today?",
        "Hi! Tell me about your college life.",
        "Hey there! What's on your mind?",
    ]),
    (r"\bthank(s| you)\b", [
        "You're welcome. Is there anything else on your mind?",
    ]),
    (r"\byes\b", [
        "I see. Can you tell me more about that?",
    ]),
    (r"\bno\b", [
        "Why not?",
        "Are you sure?",
    ]),
    (r"\bmaybe|not sure|don'?t know\b", [
        "Take your time. What makes it hard to be sure?",
    ]),
    (r"\bsorry\b", [
        "There's no need to apologize.",
    ]),
]

# ---------------------------------------------------------------------------
# 3. DEFAULT (fallback) RESPONSES
# ---------------------------------------------------------------------------
# Used when nothing in PATTERNS matches. Classic ELIZA leans heavily on
# these open-ended, non-committal prompts to keep the conversation going.
DEFAULT_RESPONSES = [
    "Can you tell me more about that?",
    "Interesting... please continue.",
    "Why do you say that?",
    "How does that make you feel?",
    "What do you think that means?",
    "Let's explore that a bit more.",
]

# ---------------------------------------------------------------------------
# 4. GREETING / FAREWELL / EXIT
# ---------------------------------------------------------------------------
OPENING_LINE = "ELIZA: Hi, I'm ELIZA. I'm here to talk about college life. Type BYE to exit."
FAREWELL_RESPONSES = [
    "Goodbye. Take care!",
    "Bye! Remember, it's okay to ask for help when you need it.",
    "Take care of yourself. Goodbye!",
]

# Any of these (typed alone, case-insensitive) end the conversation.
EXIT_WORDS = {"bye", "bye bye", "quit", "exit", "goodbye", "stop"}