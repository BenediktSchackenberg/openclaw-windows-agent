# SPRINTS.md — Sprint Planning & History

## Current Sprint

### Sprint 1 — 2026-02-07 → 2026-02-14
**Theme: Polish & Stability**

#### Goals
- [ ] Fix remaining UI bugs
- [ ] System Tray integration
- [ ] Auto-reconnect in Service
- [ ] Scheduled inventory push

#### Tasks
| ID | Task | Priority | Status | Notes |
|----|------|----------|--------|-------|
| S1-01 | System Tray Icon + Minimize to Tray | High | 🔲 Todo | Use Hardcodet.NotifyIcon.Wpf |
| S1-02 | Service auto-reconnect on disconnect | High | 🔲 Todo | Exponential backoff |
| S1-03 | Scheduled inventory.push (configurable interval) | High | 🔲 Todo | Default: 30 min |
| S1-04 | Service logging to file | Medium | 🔲 Todo | `C:\ProgramData\OpenClaw\logs\` |
| S1-05 | Test full workflow on clean Windows install | Medium | 🔲 Todo | Document any missing deps |
| S1-06 | Version bump to 0.3.0 | Low | 🔲 Todo | After sprint complete |

#### Sprint Review (2026-02-14)
*To be filled after sprint*

---

## Sprint Template

```markdown
### Sprint X — YYYY-MM-DD → YYYY-MM-DD
**Theme: [One-liner description]**

#### Goals
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

#### Tasks
| ID | Task | Priority | Status | Notes |
|----|------|----------|--------|-------|
| SX-01 | Task description | High/Med/Low | 🔲/🔄/✅ | Notes |

#### Sprint Review
- **Completed**: X/Y tasks
- **Carried over**: [list]
- **Learnings**: [what went well/badly]
```

---

## Sprint History

### Pre-Sprint Work (before 2026-02-07)
- ✅ Initial WPF app (v0.1.0)
- ✅ Gateway WebSocket connection
- ✅ Windows Service implementation
- ✅ Inventory collectors (7 total)
- ✅ FastAPI backend + Next.js frontend
- ✅ Fluent Icons UI overhaul
- ✅ App icon

---

## Labels Reference

| Label | Meaning |
|-------|---------|
| 🔲 Todo | Not started |
| 🔄 In Progress | Currently working on |
| ✅ Done | Completed |
| ⏸️ Blocked | Waiting on something |
| ❌ Cancelled | Won't do |

## Priority Levels

- **High**: Must complete this sprint
- **Medium**: Should complete if time allows
- **Low**: Nice to have, can slip

---
*Updated: 2026-02-07*
