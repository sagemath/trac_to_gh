# Issue 5614: [with patch, not ready for review] add top-of-stack caching for fast_callable

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-26 04:22:58

Assignee: somebody

Top-of-stack caching is a standard optimization for stack interpreters; it typically significantly reduces the number of memory loads/stores.  This patch adds top-of-stack caching for the fast_callable float/RDF interpreter.

Unfortunately, on my machine (32-bit x86, with Debian's gcc-4.3 version 4.3.3-3), this interacts poorly with gcc's register allocation heuristics, so the resulting interpreter is actually slower than before the patch.

Doctests do NOT pass, and the patch is not fully documented.  (I believe the patch works; the doctests that fail are looking at fast_callable internals that changed.)


---

Attachment
