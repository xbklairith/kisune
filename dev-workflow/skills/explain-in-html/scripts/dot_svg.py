#!/usr/bin/env python3
"""Render Graphviz DOT as inline SVG that follows the page's text colour.

Usage: dot_svg.py [graph.dot] > figure.svg   (reads stdin when no file is given)

Graphviz draws in black, which vanishes on a dark page. This runs `dot -Tsvg`,
swaps black for currentColor, makes unfilled text inherit it, and strips the
XML prolog, DOCTYPE, comments and generated ids, so the output pastes into an
HTML page as it is. Colours named in the DOT source are kept.
"""
import re, shutil, subprocess, sys

FONT = "Helvetica,Arial,sans-serif"
INSTALL = "brew install graphviz, or apt install graphviz"


def inline(svg):
    svg = svg[svg.index("<svg"):]
    svg = re.sub(r"<!--.*?-->\s*", "", svg, flags=re.S)
    svg = re.sub(r'\b(fill|stroke)="(?:black|#000000)"', r'\1="currentColor"', svg)
    svg = re.sub(r'\s+id="(?:graph|node|edge|clust)\d+"', "", svg)
    return svg.replace("<svg", '<svg fill="currentColor" style="max-width:100%;height:auto"', 1)


def main(argv):
    if len(argv) > 2 or argv[1:] in (["-h"], ["--help"]):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    dot = shutil.which("dot")
    if not dot:
        print(f"dot_svg: Graphviz is not installed (no `dot` on PATH). Install it ({INSTALL}) "
              "or draw the diagram as inline SVG by hand.", file=sys.stderr)
        return 1
    src = open(argv[1]).read() if len(argv) == 2 else sys.stdin.read()
    r = subprocess.run([dot, "-Tsvg", "-Gbgcolor=transparent", f"-Gfontname={FONT}",
                        f"-Nfontname={FONT}", f"-Efontname={FONT}"],
                       input=src, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(r.stderr)
        return r.returncode
    sys.stdout.write(inline(r.stdout))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
