# ELIZA-Style Chatbot — College Life Counselor

A classic rule-based chatbot in the style of Joseph Weizenbaum's 1966 ELIZA.
No machine learning, no LLM calls — just regex pattern matching, keyword
detection, and pronoun substitution ("reflection"). Domain: student
counseling / college life.

## Project structure

```
eliza-chatbot/
│
├── eliza.py        # the engine: reflection, matching, chat loop (no domain content)
├── responses.py     # the "script": reflections, patterns, templates (all domain content)
└── README.md
```

Keeping domain content (`responses.py`) separate from the engine (`eliza.py`)
mirrors real ELIZA's design: the same matching engine can be pointed at a
totally different script (e.g. career advice, roommate conflicts) just by
editing `responses.py`.

## How it works

1. **Keyword / pattern detection** — `PATTERNS` in `responses.py` is an
   ordered list of `(regex, [response templates])` pairs. On each turn,
   `respond()` in `eliza.py` scans the list top-to-bottom and uses the
   **first** regex that matches the user's sentence (`re.search`, so the
   keyword can appear anywhere in the sentence).
2. **Reflection (pronoun substitution)** — Some patterns capture the rest
   of the sentence, e.g. `r"\bi(?:'m| am) (.*)"` matches "I am **tired**"
   and captures `"tired"`. Before that fragment is dropped into a response
   template, `reflect()` swaps person/pronouns word-by-word using the
   `REFLECTIONS` table (`i → you`, `my → your`, `am → are`, ...), so
   "I am tired" becomes "Why are you **tired**?" instead of parroting
   "I am tired" back.
3. **Plain keyword rules** — Not every rule needs reflection. Rules like
   `r"\bexam(s)?\b"` just fire a canned response ("Are exams making you
   stressed?") with no capture/substitution needed.
4. **Fallback** — If nothing in `PATTERNS` matches, `respond()` returns a
   random line from `DEFAULT_RESPONSES` (e.g. "Can you tell me more about
   that?"), which is how ELIZA keeps a conversation going even on topics
   it has no script for.
5. **Exit handling** — Typing `bye`, `quit`, `exit`, `goodbye`, or `stop`
   (case-insensitive, whole line) ends the chat with a random farewell.

## Running it

```bash
python3 eliza.py
```

Example session:

```
ELIZA: Hi, I'm ELIZA. I'm here to talk about college life. Type BYE to exit.
You: Hello
ELIZA: Hello! How are you today?
You: I am tired
ELIZA: Why are you tired?
You: I feel stressed
ELIZA: What made you feel stressed?
You: My teacher is strict
ELIZA: Tell me more about your teacher.
You: I have an assignment
ELIZA: Have you started working on it yet?
You: BYE
ELIZA: Take care of yourself. Goodbye!
```

## Extending it

To add a new topic, just add an entry to `PATTERNS` in `responses.py` —
no changes to `eliza.py` are needed:

```python
(r"\broommate(s)?\b", [
    "How are things with your roommate?",
    "Living with someone else can be tricky sometimes.",
]),
```

To add a reflective ("I ___") style rule, use a capturing group `(.*)`
and `{0}` in the template:

```python
(r"\bi worry about (.*)", [
    "Why do you worry about {0}?",
]),
```

**Ordering tip:** more specific/capturing patterns should go *before*
generic keyword patterns, since the first match wins.

## Notes for the lab report

This implementation demonstrates the core computational-linguistics ideas
behind ELIZA without any statistical/ML component:

- **Surface pattern matching** rather than semantic understanding — the
  bot has no idea what "tired" means, it only recognizes the syntactic
  frame `I am ___`.
- **Reflection** as a cheap but effective illusion of understanding —
  swapping `I/you`, `my/your`, `am/are` makes canned responses feel
  personalized.
- **Rule ordering / precedence** as the entire "decision procedure" —
  there's no scoring or ranking model, just first-match-wins over an
  ordered rule list, which is exactly how the original ELIZA's keyword
  ranking (simplified here to list order) worked.
- **Bottom-up fallback** — the `DEFAULT_RESPONSES` set is what makes the
  bot robust to unseen input, a technique sometimes called the
  "non-directive therapist" trick, since Weizenbaum's original script was
  modeled on Rogerian psychotherapy.