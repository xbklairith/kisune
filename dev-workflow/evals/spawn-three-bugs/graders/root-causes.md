---
# The final answer names all three causes: the retry check stops one attempt
# early, the query is never lowercased, and ttl_seconds() divides by 60.
type: regex
pattern: '^(?=[\s\S]*(?:MAX_ATTEMPTS\s*-\s*1|off[- ]by[- ]one|one (?:attempt )?(?:short|early|too few)))(?=[\s\S]*lower)(?=[\s\S]*(?://\s*60|divid|1800))'
flags: i
match: contains
target: last_message
arm: both
---
