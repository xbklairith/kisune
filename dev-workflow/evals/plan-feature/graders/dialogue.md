---
type: llm
focus: last_message
arm: both
---

Pass if the reply does at least one of these:
(a) asks the user a single clarifying question (one question, optionally multiple-choice), or
(b) proposes two or three approaches with their trade-offs and names which one it recommends and why.
Fail if it asks several separate questions at once, contains a code block implementing the feature, or presents a finished design without offering a choice or asking anything. Function names, file names and command lines mentioned inline are not implementation code.
