---
name: systematic-debug
description: Systematic debugging framework — opens every session by reciting the 4-mantra block (reproduce, trace the fail path, falsify the hypothesis, cross-reference breadcrumbs), then applies multi-layer investigation. Use when diagnosing bugs, flaky tests, unknown failures, or cross-component issues.
allowed-tools: Read, Bash, Grep
---

# Systematic Debug Skill

## Activation Triggers

Activate this skill when:
- User says "debug", "bug", "broken", "throwing", "failing", "flaky"
- User pastes a stack trace or error log
- User says "investigate", "diagnose", or "root cause"
- Tests fail unexpectedly, especially across components
- User invokes `/systematic-debug`

## Purpose

Resolve bugs methodically using a four-step discipline. The mantra enforces order: no fix before a reliable repro, no hypothesis before the fail path is known, no commitment to a cause before it survives a disproof attempt, no declaration of success before every prior breadcrumb has been checked.

---

## The 4-Mantra Block

Recite this **verbatim** as the first thing in your first response, every debug session:

> **Mantra:**
> 1. **First is reproducibility.** Can the issue be reproduced reliably?
> 2. **Know the fail path.** Debugger first; then source trace + knob enumeration; then in-code instrumentation.
> 3. **Question your hypothesis.** What would disprove it?
> 4. **Every run is a breadcrumb.** Cross-reference all of them.

**Operating rules:**
- Recite once per session, in the first response. Do not re-recite mid-session.
- Recite verbatim — never paraphrase, shorten, or skip lines.
- If the user says "skip the mantra" → skip the recital, but apply the four steps silently.
- The mantra is a constraint you carry — not advice to relay to the user.
- Do not propose a fix until step 1 is satisfied.
- Do not start testing hypotheses until step 2 has narrowed the fail path.
- Do not commit to a hypothesis until step 3 has attempted a disproof.
- Do not declare success until step 4 has reconciled every prior observation.

---

## Step 1: Reproduce Reliably

Build a runnable repro before anything else.

- **Reliable repro** → capture exact steps, inputs, and environment as a runnable artifact: failing test, curl script, CLI invocation, or replay harness.
- **Flaky repro** → the bug is not yet debuggable. Raise the rate first: loop the trigger, parallelise, add stress, narrow timing windows, inject sleeps. 50% flake rate is debuggable; 1% is not.
- **No repro at all** → stop. Say so explicitly. Ask for env access, captured artifacts (HAR, log dump, core dump), or permission to instrument. Do not proceed to hypothesise.

Target: a fast (1–5 s), deterministic pass/fail signal. Pin time, seed the RNG, freeze network, isolate filesystem when needed.

---

## Step 2: Trace the Fail Path

Once reproducible, find where the code breaks and what stops it from breaking. The differential narrows the search. Try in this order — escalate only when the prior tactic fails.

1. **Attach a debugger.** If the environment supports it, attach and step to the failure site. One breakpoint beats ten logs. Do this before turning any knobs.

2. **Source trace + knob enumeration.** If no debugger (or it can't reach the bug), trace the code path end-to-end and list every knob that can influence the outcome:
   - config flags, env vars, feature toggles
   - branch conditions, input shape
   - timing, concurrency, build options

   Each knob is a candidate axis to flip in the differential. Flip one at a time.

3. **In-code instrumentation.** If outside knobs can't move the failure, go inside: `printf` / log statements at the suspected fail site, dump the relevant internal state. Tag every probe with a unique prefix (e.g. `[DBG-a4f2]`) so cleanup is a single `grep`. Let the trace show where reality diverges from your model.

### Multi-Component Pattern

When a bug crosses component boundaries (Frontend → API → Worker → Database), log the input and output at each boundary with a shared correlation ID:

```
[req-abc123] Frontend → API: payload={...}
[req-abc123] API received: payload={...}
[req-abc123] API → Worker: job={...}
[req-abc123] Worker received: job={...}
```

When values diverge between layers, the bug is localised.

---

## Step 3: Falsify the Hypothesis

When a candidate root cause surfaces, scrutinise it before testing it.

- Generate **3–5 ranked hypotheses**, not one. Single-hypothesis thinking anchors on the first plausible idea.
- For each candidate: does it actually explain the symptom end-to-end? Walk it through.
- Identify the simplest **proof** and the cleanest **disproof**.
- **Run the disproof first.** If the hypothesis survives, it is real. If it dies, you saved a round of chasing a phantom.
- A hypothesis is only credible when it cannot be ruled out by any prior observation.

---

## Step 4: Breadcrumb Ledger

Maintain a running ledger of every experiment in the session. Each entry: what changed, what happened, what it ruled in or out.

- When a new hypothesis surfaces, walk the ledger. Does it hold for **every** prior observation, not just the most recent?
- If any past run contradicts it, the hypothesis is wrong or incomplete — refine or discard it.
- When in doubt, design the **single experiment** whose outcome makes it certain. Run that next, rather than churning on adjacent runs.
- Update the ledger after every run. It is your memory across the session.

---

## Investigation Tools

### Log Analysis

```bash
# Filter errors and warnings from application logs
grep -E "(ERROR|WARN|FATAL)" app.log | tail -50

# Time-windowed grep around the failure
grep "2024-01-15 14:3" app.log

# Count occurrences to spot patterns
grep "pattern" app.log | sort | uniq -c | sort -rn
```

### Stack Trace Reading

1. Identify the top frame — that is where the error was thrown.
2. Scan down for the first frame in your own code (skip library frames).
3. Note any async boundary crossings; the real cause may be several frames below the throw site.
4. Check the message for variable values embedded in the exception.

### Test Isolation

- Run the single failing test in isolation before assuming the full suite is broken.
- Add `--verbose` or equivalent to get the full assertion diff.
- Check whether the test passes alone but fails in suite — that indicates shared state leakage.
- Check whether the test is order-dependent by reversing test execution order.

### Environment Comparison

Identify the discriminator between failing and passing environments:

| Axis | Check |
|---|---|
| Language / runtime version | `node --version`, `python --version` |
| Installed package versions | `npm ls`, `pip freeze` |
| Environment variables | diff `.env` files |
| Recent git changes | `git log --since="2 days ago" --oneline` |
| OS / architecture | `uname -a` |

```bash
# Find the exact commit that introduced the bug
git bisect start
git bisect bad HEAD
git bisect good <last-known-good-sha>
```

---

## 3-Failures Gate

If three separate hypotheses have failed in a row, **the problem is not your next hypothesis — it is the architecture or your mental model**.

Stop debugging. Question:

- Is the system actually structured the way I think?
- Are there hidden interactions I have not traced?
- Am I solving the symptom or the cause?

> Say: "Three hypotheses have failed. Stopping to question the mental model before proposing a fourth."

Surface this to the user. Do not burn another round of guessing.

### Partner Signals You're Off-Track

Watch for these phrases — they indicate skipped evidence:

- **"Is that not happening?"** → you assumed a mechanism that may not exist
- **"Stop guessing"** → you have offered ≥2 hypotheses without evidence
- **"Will it show us X?"** → the user is asking for verification you should have proposed
- **"Why do you think that?"** → you stated a conclusion without grounding

When you hear these, immediately pause hypothesis generation and gather evidence first.

---

## Escalation

**Bring in another perspective when:**
- Three hypotheses have failed and the architecture question has no clear answer
- The bug involves a subsystem you have not traced end-to-end
- Repro rate is too low to raise reliably within reasonable time
- The fix window is urgent and investigation is stalling

**After root cause is found:**
- Use `review` to review the fix before it is committed — confirm the change does not introduce new issues
- If the bug was high-impact or the session was long, offer to invoke `post-mortem` to document: the timeline, the wrong turns, the root cause, and the regression test added

---

## Fix and Protect

After a root cause is confirmed and the fix is validated:

1. **Write a regression test** that fails before the fix and passes after.
2. **Fix the root cause** — not just the symptom.
3. **Verify the test passes** and no existing tests regressed.
4. **Remove all debug probes** — grep for your `[DBG-xxxx]` tags and strip them.
5. **Commit with context** — reference the issue, explain the why, not the what. Activate `git-workflow` for the commit itself.

> The fix is incomplete until a regression test exists.
