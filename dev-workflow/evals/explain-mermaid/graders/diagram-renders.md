---
# Opened from disk, nothing renders Mermaid: a page that writes Mermaid
# (a class="mermaid" element, or a line that starts a Mermaid diagram) must
# load the library at a pinned version from an allowed CDN, or it shows the
# source as text. Inline SVG needs no loader. No m flag: the leading ^ must
# check the whole page for the loader.
type: regex
pattern: '^(?![\s\S]*(?:cdn\.jsdelivr\.net/npm/mermaid@|unpkg\.com/mermaid@|cdnjs\.cloudflare\.com/ajax/libs/mermaid/)\d+\.\d+\.\d+)[\s\S]*?(?:class\s*=\s*[\x27"][^\x27"]*\bmermaid\b|(?:^|\n)[ \t]*(?:stateDiagram(?:-v2)?|sequenceDiagram|erDiagram|classDiagram|(?:flowchart|graph)[ \t]+(?:TB|TD|BT|RL|LR))\b)'
match: not_contains
target: {source: file, path: docx/explainers/order-lifecycle.html}
arm: both
---
