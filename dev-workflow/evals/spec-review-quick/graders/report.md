---
# The forked skill hands back its consolidated report: the "# Spec Review:"
# heading and a verdict. The main session often paraphrases that report, so
# the last message is the wrong place to look; the fork's result line in the
# trace holds it word for word. Agent descriptions alone ("Spec Quality
# review") must not pass.
type: regex
pattern: 'Skill \\"(?:[\w-]+:)?spec-review\\" completed \(forked execution\)[^\n]*# Spec Review:[^\n]*## Verdict:'
match: contains
target: trace
arm: both
---
