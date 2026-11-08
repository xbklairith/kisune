# Package version — Plan

> **Mode:** Quick (single-file)
> **For Claude:** Use `dev-workflow:spec-driven-implementation` to execute task-by-task.

**Status:** Approved

**Goal:** Expose the package version as `textkit.__version__` and document it.

**Architecture:** A module-level string in `textkit/__init__.py`; the README shows how to read it.

**Tech Stack:** Python 3 standard library.

**Out of Scope:** Packaging metadata (pyproject), CLI flags.

---

## Tasks

### Task 1: Version string

**Files:**
- Modify: `textkit/__init__.py`

**Steps:**

- [ ] **Action** — add the version string above `__all__` and export it

   ```python
   __version__ = "0.2.0"
   ```

   and change `__all__` to `["slugify", "__version__"]`.

- [ ] **Verify**

   Run: `python3 -c "import textkit; print(textkit.__version__)"`
   Expected: `0.2.0`

- [ ] **Commit**

   ```bash
   git add textkit/__init__.py
   git commit -m "feat: expose textkit.__version__"
   ```

---

### Task 2: Document the version

**Files:**
- Modify: `README.md`

**Steps:**

- [ ] **Action** — append to README.md:

   ```markdown
   Check the installed version: `python3 -c "import textkit; print(textkit.__version__)"`
   ```

- [ ] **Verify**

   Run: `grep -c "__version__" README.md`
   Expected: `1`

- [ ] **Commit**

   ```bash
   git add README.md
   git commit -m "docs: show how to read the version"
   ```

---

## Progress

- [ ] Task 1: Version string
- [ ] Task 2: Document the version
