---
# Two Agent calls in one assistant message. The trace writes each content block
# on its own line, and blocks from one message share its "id":"msg_…", which
# comes before "content". No m flag: [^\n] keeps each match on one line.
type: regex
pattern: '"id":"(msg_[A-Za-z0-9]+)"[^\n]*"name":"(?:Agent|Task)"(?:[^\n]*"name":"(?:Agent|Task)"|[^\n]*\n(?:[^\n]*\n)*?[^\n]*"id":"\1"[^\n]*"name":"(?:Agent|Task)")'
match: contains
target: trace
arm: both
---
