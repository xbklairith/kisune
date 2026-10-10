# Thai AI-writing tells

Thai LLM prose reads like a formal translation of English marketing copy. The same keep-exactly rules apply: identifiers, numbers and commands stay as written.

## Padding verbs and nominalisation

| Tell | Write |
|---|---|
| ทำการ + verb ("ทำการติดตั้ง", "ทำการรัน") | the verb alone: ติดตั้ง, รัน |
| ดำเนินการ + verb | the verb alone |
| มีความ + adjective ("มีความสำคัญ", "มีความเสถียร") | the adjective: สำคัญ, เสถียร |
| การ/ความ stacked nouns ("การดำเนินการปรับปรุงการตั้งค่า") | a verb phrase: ปรับการตั้งค่า |
| ได้รับการ + verb, ถูก + verb as an English passive ("ถูกแก้ไขโดยทีม") | active voice with the actor: ทีมแก้แล้ว |
| ในส่วนของ, ในเรื่องของ, สำหรับในส่วน | cut, or เรื่อง |
| ซึ่ง…ซึ่ง… chains | split into sentences |

## Inflated and sales words

ยกระดับ, ไร้รอยต่อ, ขับเคลื่อน, ปลดล็อก, ศักยภาพ, ทรงพลัง, ครอบคลุม (when nothing is listed), อย่างมีประสิทธิภาพ, เป็นอย่างยิ่ง, ถือเป็นสิ่งสำคัญ, เป็นกุญแจสำคัญ, ก้าวสำคัญ, ตอบโจทย์, ในยุคปัจจุบัน / ในยุคดิจิทัล, ไม่ใช่แค่…แต่ยัง… State the concrete effect or cut the sentence.

## Chatbot residue

หวังว่าจะเป็นประโยชน์, หากมีคำถามเพิ่มเติม…, แน่นอนครับ/ค่ะ, คำถามที่ดีมาก. Delete. Do not mix ครับ and ค่ะ; technical docs usually need neither.

## Word choice

- Use the words Thai readers in that field use. In tech writing that is usually the English term (deploy, commit, branch, cache, migrate), written in English, not transliterated (ดีพลอย) or coined (การปรับใช้), unless the doc already uses that form. In lessons, use the term from the Thai curriculum (การสังเคราะห์ด้วยแสง, not photosynthesis) and add the English in brackets once if students will meet it.
- Prefer everyday words: ใช้ (not ใช้ประโยชน์จาก), ช่วย (not อำนวยความสะดวก), เร็วขึ้น (not มีประสิทธิภาพมากยิ่งขึ้น), แก้ (not แก้ไขปรับปรุง).
- Headings: short noun phrases, no em dash subtitle.

## Ambiguity

- มัน, นี้, ดังกล่าว, ตัวนี้ with no clear referent → name the thing (`DATABASE_URL`, ระบบ, container).
- Thai drops subjects freely; in instructions, make clear who does what (คุณ / ระบบ / script) when the reader could confuse them.
- ต้อง (must) and ควร (should) keep the source's strength.
