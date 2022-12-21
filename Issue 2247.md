# Issue 2247: [with patch, needs wildly trivial review] comment out long doctest in totallyreal_rel.py

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-21 18:15:39

Assignee: craigcitro

There's a really long doctest in sage/rings/number_field/totallyreal_rel.py. We can't just `# long` it, because it also needs to use `# 32-bit`/`# 64-bit`, and these two don't play nicely together. This patch makes it into a `# no doctest` for now to avoid timeouts.


---

Attachment


---

Comment by mabshoff created at 2008-02-21 18:29:02

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 18:29:51

Merged in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-21 18:29:51

Resolution: fixed
