# AI-writing patterns

Condensed from humanizer's catalogue (see `NOTICE.md`), with technical examples. One pattern alone proves little; several together in one passage are the signal.

## Content

1. **Importance inflation.** "pivotal", "a testament to", "plays a crucial role", "marks a shift". State the change.
2. **Name-dropping.** Lists of outlets or follower counts to prove importance. Keep one citation that says something.
3. **Shallow -ing tails.** "…, ensuring consistency", "…, highlighting our commitment". Cut the tail or make it a real claim.
4. **Sales language.** "seamless", "robust", "delightful", "powerful", "best-in-class". Say the effect or cut it.
5. **Vague sources.** "Experts agree", "industry reports". Name the source or drop the claim.
6. **Challenges-and-outlook sections.** "Despite these challenges…", "Looking ahead…". End on the last fact.

## Language

7. **Stock AI words.** additionally, align with, crucial, delve, enhance, foster, garner, intricate, interplay, key (adjective), landscape, leverage, pivotal, showcase, streamline, tapestry, testament, underscore, vibrant.
8. **Avoiding *is* and *has*.** "serves as", "boasts", "features". Use the plain verb.
9. **"Not X but Y".** "It's not just a bug, it's a lesson." Say the one thing.
10. **Forced threes.** "fast, reliable, and secure" when only one was shown.
11. **Synonym cycling and repeated openings.** One name per thing; merge sentences that all start with the same subject.
12. **False ranges.** "from setup to scale" when there is no range.
13. **Missing actor.** "No config needed." → "You do not need a config file." Use active voice when it names who acts.

## Style

14. **Em and en dashes.** Replace with a comma, colon, parentheses or a new sentence.
15. **Bold sprinkled on phrases.** Bold only what a skimmer must not miss.
16. **Bold-label bullets.** `- **Performance:** Performance improved…` → `- Export streams rows instead of loading the file.`
17. **Title Case Headings.** Sentence case.
18. **Decorative emoji** in headings and bullets.
19. **Curly quotes** in Markdown, code and commit messages.

## Chatbot residue

20. **Greetings and offers.** "Certainly!", "I hope this helps", "Let me know if you'd like…".
21. **Knowledge-limit hedges.** "As of my last update", "details are scarce, but it likely…". State what the source lacks, or cut.
22. **Agreeable openers.** "Great question", "You're absolutely right".

## Filler and hedging

23. **Filler phrases.** "In order to" → "To"; "due to the fact that" → "because"; "It is important to note that" → cut.
24. **Stacked qualifiers.** "could potentially possibly". Keep one only when the source is uncertain.
25. **Generic positive endings.** "The future looks bright."
26. **Hyphen pairs after the noun.** "the report is high-quality" → "high quality".
27. **Fake depth.** "At its core", "The real question is".
28. **Announcing the next point.** "Let's dive in", "Here's what you need to know".
29. **Heading echoed in the first sentence.** `## Performance` then "Performance matters." Cut the echo.
30. **Writing about the previous version** in docs that are not a changelog. Describe current behaviour.
31. **Dramatic fragments in a row.** "No config. No setup. Just speed."
32. **Formulaic sayings.** "Tests are the language of trust."
33. **Fake-candid openers.** "Honestly?", "Here's the thing".
34. **Answering objections nobody raised.** "To be clear, this isn't about…".
35. **Rejecting fake alternatives.** "A tempting approach would be…, but". State the real constraint.

## Not a tell

- Polished grammar, dry prose, or one formal word.
- A single *however*, one em dash, curly quotes from an editor, one short emphatic sentence.
- Real limits, safety notes, named objections, and real alternatives in a design doc.
- Words in their technical sense: primary *key*, *robust* regression, *leverage* ratio, *landscape* orientation.
- Text being quoted or discussed rather than used.
