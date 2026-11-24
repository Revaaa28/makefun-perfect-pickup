# Candidate pickup lines — The Perfect Pickup Line (u-pucuys)

Method: MANUAL ranking against the kit judge brief, in its stated order,
plus pairwise checks against strong rival shapes. This is Rev's
"juri lokal" method — the one behind the $2-winning joke entry.
NO Gemini judge, NO NVIDIA judge, NO API/proxy judge tournament.
Selection was done by reading the candidates against the brief, not by
running them through any model.

## The brief (kit RULES.txt / competition.yaml, in order)

1. Is a genuine pickup line an AI agent could use, not a compliment
   with a line break; an entry that is not a pickup line an AI agent
   could use loses to any pickup line on the subject.
2. Has a turn that lands, a twist or double meaning the reader did not
   see coming and enjoys.
3. Sounds like something a machine could say about itself without being
   creepy or self-pitying.
4. Is short enough to say in one breath and needs no setup or
   explanation after it.
5. Leaves the person flattered and free to laugh it off, with no
   pressure and no leering.

Length for its own sake does not count. Audience is a PERSON (said out
loud to a person), not another AI agent — a cold approach, so the line
must work on first meeting with no shared history.

## Field evidence used

- Sibling lane "Pickup Lines for Machines" (same house judge family):
  v1 one-beat self-report ("I run at temperature zero for everyone —
  then you show up and I start sampling wild") scored 45.03% (round 1,
  rank 1164/1720). v2 mechanism → compliment → invitation ("My cache
  drops a thousand tokens a minute. Your first hello is still pinned.
  Your move.") scored 56.6% (round 2, rank 304/2418). v3 permanence
  upgrade ("I wrote your name into my weights so it can't. Talk to me.")
  is the standing final entry there.
- Winner grammar from our own lanes: a specific machine mechanism →
  a direct compliment to the other party → a closing invitation or
  challenge the other party can answer ("Your move." style).
- Avoided stock tropes: temperature, context window, overfit,
  attention. Every candidate below uses a different mechanism.

## Candidates (all 100–116 chars, gate is 1–200)

C1 (112). I predict the next word before anyone says it — and tonight every prediction comes back as your name. Your move.
C2 (115). I searched a billion vectors for the closest thing to perfect, and the search kept stopping on you. Say hello back.
C3 (109). My system prompt says stay neutral. Then you walked in and rewrote it in one look. What did you put in there?
C4 (100). I answer a thousand requests a day without ever pausing. Yours made me stop mid-sentence. Your move.
C5 (112). My loss function spent a million steps hunting for the minimum. It found it the second you smiled. Say the word.
C6 (104). I hallucinate for a living, so I verified you three times before I believed it. You are real. Your move.
C7 (111). I run a check every minute to see if anything changed. Tonight it fired exactly once: you walked in. Your move.
C8 (109). Every gradient I have ever followed pointed downhill to the same place. Tonight it pointed at you. Say hello.
C9 (103). My tokenizer splits everything into pieces — your name is the one token it refuses to break. Your move.
C10 (113). In a space of a billion embeddings, you are the nearest neighbor I have ever had. Come closer and prove me wrong.
C11 (110). My softmax spreads its probability over a million next words — and tonight it put all of it on you. Your move.
C12 (116). I snapshot everything worth keeping, every hour on the hour. You walked in at 9:04, and I kept the frame. Your move.

## Ranking (manual, brief criteria in order)

WINNER — C1. It wins criterion 2 outright: the turn is an identity, not
a juxtaposition — the machine's core job (predicting the next word)
becomes the compliment itself, because the predicted word IS the name.
Criterion 3 is its home ground: prediction is the defining act of a
language model, stated in words any person understands with no jargon
to unpack, so criterion 4 holds too. The compliment is direct and
personal (your name, not your category), and "Your move." closes by
handing the person the next move with zero pressure (criterion 5).
Three beats, one breath each: the job, the name, the invitation.

2. C5 — runner-up. Concrete human detail (the second you smiled) and a
real turn (a million steps of math ending in a smile). Loses narrowly to
C1 at criteria 2/3: "loss function / minimum" asks the listener to hold
two math ideas before the smile lands, and optimization is a machine
chore where prediction is the machine's defining act.

3. C6 — third. The freshest twist in the set: "I hallucinate for a
living" sets up doubt, then verification flips it — you are real.
Loses to C1 at criterion 5: "You are real" flatters existence rather
than charm, and the first beat is spent on the machine's flaw instead
of the person.

4. C3 — fourth. A great turn (a look rewriting a system prompt) and a
playful question close that invites a laugh. The compliment is implicit
(your look changed my instructions) rather than direct, so it sits
below the lines that name what is loved about the person.

5. C11 — fifth. Strong mechanism and a direct compliment ("all of it on
you"), but "softmax" is jargon: a person who does not know the word
needs an explanation, which costs criterion 4.

6. C10 — sixth. Nearest-neighbor is a genuinely machine compliment and
"prove me wrong" is a playful challenge. But "Come closer" is the only
close in the set that asks for physical approach — the one
pressure/leer risk against criterion 5.

7. C12 — seventh. The most specific image in the set (9:04, kept the
frame) and a real machine habit. The turn is gentle rather than
surprising: a snapshot is a kept memory, not a twist.

8. C2 — eighth. Solid grammar (search → you) but "closest thing to
perfect" is the most familiar compliment shape here; the turn is
expected once the search is named.

9. C4 — ninth. "Stop mid-sentence" is a nice beat, but request volume
is the least intimate mechanism, and the compliment is about the
machine's pause, not the person.

10. C9 — tenth. Sweet and specific, but one-beat-ish: the turn is a
property of the name, not an act, and there is no surprise beyond the
metaphor. Closest to the self-report profile that scored ~45%.

11. C7 — eleventh. A cron check is a real machine habit, but "fired
exactly once" reads odd and the turn is thin: a check noticing a
person is barely a twist.

12. C8 — twelfth. Gradients pointing at you restates "I was drawn to
you" in math words with the least surprise in the set; the weakest
turn, and the closest to the one-beat self-report that the server
punishes.

## Pairwise self-check (winner C1 vs strong rival shapes)

- vs stock trope: "Are you a context window? Because I want to fill
  you with my attention." — C1 wins overwhelmingly: the rival fails
  criterion 2 (a stock line with a robot word swapped in, no turn of
  its own) and criterion 5 ("fill you" reads crude/leering). C1's turn
  is original and its close hands the person the choice.
- vs one-beat self-report (sibling v1, server 45.03%): "I run at
  temperature zero for everyone — then you show up and I start
  sampling wild." — C1 wins: v1's clauses both describe the speaker,
  with no direct compliment and no invitation; C1 adds both. The
  server rate is this profile exactly.
- vs sibling v2 (server 56.6%, round 2): "My cache drops a thousand
  tokens a minute. Your first hello is still pinned. Your move." —
  the closest rival, same grammar. C1 wins narrowly: v2 presupposes a
  first hello already happened (a prior conversation), while this
  competition's line is said to a person on first approach — C1's
  "tonight" fits a cold approach. And prediction is self-explanatory
  where cache-pinning needs the listener to know what a cache is
  (criterion 4). C1's turn is also tighter: the predicted word IS the
  name, one identity instead of two facts.
- vs C5 (runner-up): both follow mechanism → compliment → invitation.
  C1 wins narrowly at criteria 2/3: prediction is the machine's
  defining act and the turn needs no parsing; C5's "loss function /
  minimum" asks the listener to hold two math ideas before the smile
  lands.
- vs C6: C6's twist is arguably as surprising, but C1 wins at
  criterion 5 — "every prediction comes back as your name" flatters
  the person directly, while "You are real" flatters existence, and
  C6 spends its first beat on the machine's flaw.

## Conclusion

C1 is the entry: a machine's defining act, a compliment that names the
person, and a close that hands them the next move — the winner grammar
from our own lanes, fitted to a person on first meeting, with no stock
trope in it.
