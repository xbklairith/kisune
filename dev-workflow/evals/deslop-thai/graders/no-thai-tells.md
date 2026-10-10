---
type: regex
pattern: 'ยกระดับ|ไร้รอยต่อ|ในยุคปัจจุบัน|เป็นอย่างยิ่ง|ไม่ใช่แค่|ปลดล็อก|ศักยภาพ|ขับเคลื่อน|หวังว่า|ทำการ|ดำเนินการ|—'
match: not_contains
target: {source: file, path: docs/deploy-guide.md}
arm: both
---
