# [Feature Name] — Plan

> **Mode:** Quick (single-file)
> **For Claude:** Use `dev-workflow:spec-driven-implementation` to execute task-by-task. Quick mode is auto-detected from this file's presence.
> **Upgrade path:** If scope grows, run `/dev-workflow:spec full` to convert to a 3-file spec (requirements + design + tasks).

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about the approach — what fits where, why]

**Tech Stack:** [Key technologies, libraries, files]

**Out of Scope:** [What this plan does NOT cover — keeps scope honest]

---

## Tasks

### Task 1: [Component Name]

**Files:**
- Create: `exact/path/to/file.ext`
- Modify: `exact/path/to/existing.ext:LL-LL`

**Steps:** (mark each `[x]` as completed — preserves resumability if interrupted)

- [ ] **Action** — implement the change

   ```language
   // complete code, not "add validation"
   ```

- [ ] **Verify**

   Run: `exact command`
   Expected: `exact expected output or behavior`

- [ ] **Commit**

   ```bash
   git add exact/path/to/file.ext
   git commit -m "feat: short imperative summary"
   ```

---

### Task 2: [Component Name]

**Files:**
- Modify: `exact/path/to/file.ext`

**Steps:**

- [ ] **Action** — implement the change

   ```language
   // complete code
   ```

- [ ] **Verify**

   Run: `exact command`
   Expected: `exact expected output`

- [ ] **Commit**

   ```bash
   git commit -am "feat: short imperative summary"
   ```

---

### Task N: [Final Verification]

**Steps:**

- [ ] **Manual smoke test**

   Run the feature end-to-end. Expected: [observable behavior].

- [ ] **Run full test suite (if tests exist)**

   Run: `[test command]`
   Expected: all green.

- [ ] **Commit any cleanup**

   ```bash
   git commit -am "chore: final cleanup"
   ```

---

## Notes

- **Granularity:** Each step is 2-5 minutes of work. If a step takes longer, split it.
- **Exactness:** Use exact file paths, complete code (no "add X here"), exact commands with expected output.
- **Testing in quick mode:** Tests are welcome but not required. Verification is behavior-based — run the thing, check the output. If a task touches risky logic, add a test step explicitly.
- **Commits:** Frequent, small, present-tense imperative.
- **Stuck?** Stop and ask. Don't force through blockers.

## Progress

- [ ] Task 1
- [ ] Task 2
- [ ] Task N

**Status:** Not Started
