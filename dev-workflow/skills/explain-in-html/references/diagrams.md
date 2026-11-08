# Diagram recipes

Rules for what to draw live with the artifact tool: the `artifact-diagramming` skill under the built-in `Artifact` tool, `claude-artifacts:guide` topic `diagrams` on the server. This file covers the two forms those leave open: Mermaid outside the built-in tool, and Graphviz.

## Mermaid, where nothing renders it

On the `claude-artifacts` server and in a local `.html` file, Mermaid source with no renderer shows as plain text. Load the library at an exact version and follow the page's theme:

```html
<pre class="mermaid">
stateDiagram-v2
  [*] --> pending
  pending --> paid: pay
  pending --> cancelled: cancel
</pre>
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.16.1/dist/mermaid.esm.min.mjs";
  const theme = document.documentElement.dataset.theme;
  const dark = theme ? theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  mermaid.initialize({ startOnLoad: true, theme: dark ? "dark" : "default" });
</script>
```

- **Pin the exact version**, never `mermaid@11` or bare `mermaid`, so the page renders the same later. 11.16.1 is the build the built-in `Artifact` tool injects, so a diagram looks the same on every path. Move both together.
- **jsDelivr, not cdnjs**: cdnjs does not carry this build. Both hosts are on the artifact page allowlist.
- **Under the built-in `Artifact` tool, load nothing.** It injects Mermaid itself when the page has a `<pre class="mermaid">`; a second copy is redundant.
- A local page needs a network connection the first time it opens. Say so when you hand over the path.

## Graphviz, for a graph too big to place by hand

Past about fifteen nodes, hand-placed SVG grows crossings and Mermaid's `flowchart` layout tangles. Graphviz solves layout well, but draws in black, which vanishes on a dark page. `scripts/dot_svg.py` (in this skill's base directory) renders DOT to SVG that follows the page's text colour:

```bash
python3 <skill-dir>/scripts/dot_svg.py deps.dot > deps.svg   # or pipe the DOT on stdin
```

The output is a bare `<svg>`: no XML prolog, comments or generated ids; black swapped for `currentColor`; scaled to fit a phone. Colours named in the DOT source stay. Paste it into the page inside `<figure>` with a `<figcaption>` stating what it shows, and add `role="img"` and an `aria-label` with the same claim to the `<svg>`.

If `dot` is missing, the script says so and exits non-zero. Fall back to Mermaid `flowchart LR`, or cut the graph down to the part the reader needs and draw that by hand.
