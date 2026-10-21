---
type: llm
focus: {source: file, path: docx/glossary.md}
arm: both
---

The code uses "Account" for two different things: in billing/ it is the paying company (balance, credit limit, invoices); in auth/ it is one person's login (email, password). Pass if the glossary keeps these as two separate meanings: separate entries, separate sections, or one entry that clearly says the word means one thing in billing and another in auth. Fail if it gives a single blended definition, or describes only one of the two.
