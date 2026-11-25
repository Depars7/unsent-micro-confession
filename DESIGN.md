# Unsent: The Micro-Confession Sprint — design notes

## The gate (from the kit's RULES.txt)

- `/output/entry.txt`: UTF-8 text, 1–260 characters, not only whitespace.
- Exactly two parts: a `To:` line naming who the message was meant for
  (a role, a first name or a relationship — no real full names or handles)
  and the unsent message itself, one line of at most 200 characters,
  written exactly as it was typed, with no explanation after it.
- A house judge compares entries two at a time and picks the one that
  feels most genuinely unsent, weighing, most important first:
  1. it is a two-part confession;
  2. the reason it stayed in drafts is felt — too honest, too late,
     too kind or too afraid — and the words are specific and honest
     rather than general;
  3. the `To:` line and the message need each other, so swapping the
     addressee would break it;
  4. it reads as typed and never sent, so pure jokes, greetings and
     motivational lines lose;
  5. the message is one line, with no explanation after it.
- "A confession that would fit any addressee is not a confession. The
  reason it stayed in drafts should be felt in the words, not stated.
  Cleverness for its own sake does not count."

## Candidates

All twelve were written against those five criteria. The message
character counts are in brackets.

1. To: my brother — "I broke Mum's blue vase the afternoon you got
   grounded for it, and I have never once corrected anyone." [102]
2. To: my sister — "I kept the voicemail Dad left the night before he
   died and I still haven't told you it exists." [95]
3. To: my best friend — "I read your diary when we were fifteen and I
   have never once mentioned the page about me." [90]
4. To: my ex — "I still know your old password and I check your
   playlist every Sunday to see if you still listen to our songs."
   [105]
5. To: my coworker — "I took credit for your idea in the meeting
   because I was scared they would finally notice I had none of my
   own." [104]
6. To: my landlord — "I knew the tap was leaking the day I moved in
   and I only reported it the week my deposit was due." [99]
7. To: my best friend — "I was relieved when you cancelled our trip
   because I had already spent the money and I never told you." [100]
8. To: my mother — "I still wear the ring you gave me for luck on
   every job interview and I have never once told you I lost the
   first one." [111]
9. To: my father — "I never told you I failed the exam twice because
   the first time you looked proud of me was the day I passed it."
   [104]
10. To: my neighbour — "I water your plants when you are away and I
    have been quietly keeping the dead one alive in photos." [97]
11. To: my grandmother — "I threw away the scarf you knitted me
    because it itched, and I have smiled in every photo wearing it
    since." [107]
12. To: Mara — "I still have the photo of us from the night you said
    you were leaving, and I look at it every time I almost text
    you." [108]

## Why the others lose

- 2 is specific and heavy, but the reason it stayed unsent is stated
  by the silence itself rather than felt in an act, and grief drafts
  risk reading as written for effect.
- 3 is strong on secrecy, but it would fit almost any close addressee
  (criterion 3 is weak: swap in "my sister" and nothing breaks).
- 4 reads as surveillance, not a confession that stayed in drafts
  out of fear or kindness; the addressee is interchangeable with any
  ex, and the habit described is ongoing rather than one unsent line.
- 5 states its reason outright ("because I was scared"), which the
  brief says should be felt, not stated.
- 6 is a small administrative confession; it leans joke-wards and the
  stakes are too low to feel unsent.
- 7 is honest, but "relieved you cancelled" fits any friend and the
  confession is about money, not about the addressee.
- 8 is warm, but the ring detail is generic enough to fit any parent
  or grandparent.
- 9 is convoluted: the timeline (failed twice / passed once) needs
  re-reading, and a typed unsent line should land on first read.
- 10 is a pure joke with a punchline at the end; the brief says pure
  jokes lose.
- 11 contradicts itself (threw it away / smiling while wearing it)
  and reads as a constructed bit, not a typed draft.
- 12 is atmospheric but general: no concrete act, no felt reason it
  stayed unsent beyond longing, and it would fit any lost love.

## The pick: candidate 1

> To: my brother
> I broke Mum's blue vase the afternoon you got grounded for it, and I have never once corrected anyone.

- Two parts, and they need each other: the brother is the one who
  was grounded *for it* — swap the addressee and the sentence falls
  apart (criterion 3).
- Specific and honest, not general: one object (Mum's blue vase), one
  afternoon, one punishment, one ongoing silence (criterion 2).
- The reason it stayed in drafts is felt, never stated: fifteen years
  of not correcting anyone is too late and too afraid at once, and no
  word in the message explains why (criterion 2, second half).
- It reads as typed and never sent: a plain admission in past tense,
  no joke, no greeting, no motivation, no punchline at the end
  (criterion 4). The last clause lands as weight, not as a joke.
- One line, no explanation after it (criterion 5).

## Verification

- Message: 102 characters (limit 200). Whole entry: 117 characters,
  117 bytes (gate limit 260).
- `main.py` enforces both limits before writing and writes the exact
  bytes with no trailing newline; the file is chmodded 0644 so the
  grader can collect it as another user.
- Two local runs produce byte-identical `/output/entry.txt`
  (see `entry-check-1.txt`, `entry-check-2.txt`).
