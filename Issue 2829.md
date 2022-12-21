# Issue 2829: [with patch, needs review] PyLint cleanup of crypto.mq.sr

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-06 13:27:09

Assignee: cwitty

Keywords: pylint

The attached patch fixes a couple issues reported by [PyLint](http://www.logilab.org/857):
 * "a,b" -> "a, b"
 * remove unused variables
 * remove unused imports
 * avoid overwriting built-in names


---

Attachment


---

Comment by mabshoff created at 2008-04-06 15:25:28

Patch looks good to me, but I have reject issues against my 3.0.alpha2 merge tree:

```
patching file sage/crypto/mq/sr.py
Hunk #25 FAILED at 599.
Hunk #26 FAILED at 615.
Hunk #28 succeeded at 655 with fuzz 2.
Hunk #48 FAILED at 1191.
Hunk #75 FAILED at 1776.
4 out of 95 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej
```

One those issues are fixed I will apply.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 15:43:22

Ok, the first three rejects are due to `#random` and Carl Witty's randgen fix. 

Cheers,

Michael


---

Attachment

the good hunks from malb's patch


---

Attachment

The four missing hunks that were in the previous patch


---

Comment by mabshoff created at 2008-04-06 16:25:54

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 16:25:54

Merged trac_2829_pylint_crypto_mq_sr__py-good_hunks.patch and trac_2829_pylint_crypto_mq_sr__py-rebased_hunks.patch in Sage 3.0.alpha2. Doctests pass.
