---
name: codebase-design
description: "Shared vocabulary for designing deep modules — module, interface, depth, seam, adapter. Use when designing or improving a module's interface, deciding where a seam goes, hunting for deepening opportunities, or making code more testable."
allowed-tools: Read, Glob, Grep, Bash
---

# Codebase Design

Design **deep modules**: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface. The aim is leverage for callers, locality for maintainers, testability for everyone.

## Glossary

Use these terms exactly. Consistent language is the whole point — do not substitute "component", "service", "API", or "boundary".

- **Module** — anything with an interface and an implementation. Deliberately scale-agnostic: a function, class, package, or tier-spanning slice.
- **Interface** — everything a caller must know to use the module correctly. Not just the type signature: invariants, ordering constraints, error modes, required configuration, performance characteristics. *Avoid "API" and "signature"* — both are too narrow.
- **Implementation** — what is inside the module.
- **Depth** — leverage at the interface: how much behaviour a caller or test can exercise per unit of interface they must learn. **Deep** = large behaviour behind a small interface. **Shallow** = interface nearly as complex as the implementation.
- **Seam** *(Feathers)* — a place where behaviour can be altered without editing in that place; where a module's interface lives. Where to put the seam is its own decision, separate from what goes behind it. *Avoid "boundary"* — overloaded with DDD's bounded context.
- **Adapter** — a concrete thing satisfying an interface at a seam. Describes the *role* it fills, not what is inside it.
- **Leverage** — what callers get from depth: one implementation paying back across N call sites and M tests.
- **Locality** — what maintainers get from depth: change, bugs, and verification concentrate in one place. Fix once, fixed everywhere.

## Principles

- **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small swappable parts; they just are not part of its interface. Modules can have **internal seams** used by their own tests as well as the **external seam** at their interface.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.
- **The interface is the test surface.** Callers and tests cross the same seam. Needing to test *past* the interface means the module is the wrong shape.
- **One adapter is a hypothetical seam. Two adapters is a real one.** Do not introduce a seam unless something actually varies across it.

When shaping an interface, ask: can I reduce the number of methods? Simplify the parameters? Hide more complexity inside?

## Designing for testability

- **Accept dependencies, do not construct them.** `processOrder(order, gateway)` is testable; a `processOrder` that news up a `StripeGateway` inside is not.
- **Return results, do not mutate.** `calculateDiscount(cart): Discount` is testable; `applyDiscount(cart): void` is not.
- **Small surface area.** Fewer methods means fewer tests; fewer parameters means simpler setup.

## Rejected framings

- **Depth as a ratio of implementation lines to interface lines** (Ousterhout) — rewards padding the implementation. Use depth-as-leverage.
- **"Interface" as a language keyword or a class's public methods** — too narrow. Interface here is every fact a caller must know.

Pairs with `scrutinize` when auditing an existing module, and with `brainstorming` when the shape is still open.
