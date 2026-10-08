# Weinberg QM Notes
Working notebooks, problem solutions, and reading logs for
*Lectures on Quantum Mechanics*, 2nd ed. — Steven Weinberg (Cambridge, 2015).

## Purpose
A one-pass, problem-complete reading of Weinberg as preparation for QFT.
Rule: a section is "done" only when its key results can be stated without looking.

## Repo layout
- `notebooks/chNN_.../` — one notebook per section (or cluster), numbered to match
  the book's equation numbering (e.g. `sec1-1_photons.ipynb` covers Eqs. 1.1.1–1.1.8).
  Each notebook follows the loop: read -> reproduce derivation -> numerics -> summary.
- `problems/` — worked solutions, one file per chapter (`ch01.md` ... `ch12.md`),
  with date + confidence flag per problem.
- `reviews/` — self-quiz sheets per phase and spaced-repetition recaps.
- `progress.md` — section-level checklist.

## The four phases
| Phase | Chapters | Target |
|---|---|---|
| A Foundations & classic systems | 1–2 | fluency, fast |
| B General principles | 3–4 | the hinge — slow down |
| C Approximation machinery | 5–6 | problem-heavy |
| D Scattering & fields | 7–12 | most QFT-adjacent |

## Notebook conventions
1. First cell: what the section claims (bullet summary).
2. Reproduce every numbered derivation symbolically where feasible (SymPy) —
   never just transcribe the book.
3. End with "My summary" cell (own words) + "Gaps" cell (questions for review).
4. Constants live in `notebooks/weinberg_constants.py`, cgs, matching the book's
   un-rationalized electrostatic units.

## Environment
Python 3.11+, `numpy`, `scipy`, `matplotlib`, `sympy`. See `requirements.txt`.
