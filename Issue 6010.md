# Issue 6010: [with patch, needs review] implement various invariants for genus 2 hyperelliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/6010

Original creator: ncalexan

Original creation time: 2009-05-08 21:58:26

Assignee: was

CC:  kohel

Keywords: genus 2 hyperelliptic igusa invariants

Patch says it best -- Igusa and related invariants for hyperelliptic curves of genus 2 (equivalently, quintic/sexitc binary forms).


---

Comment by was created at 2009-05-09 15:27:34

Wow, awesome that you did this! Thanks!!


---

Comment by was created at 2009-05-12 05:46:44

Can you rebase this against 3.4.2.  I get:

```
patching file sage/schemes/hyperelliptic_curves/all.py
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/all.py.rej
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py
Hunk #1 FAILED at 6
Hunk #2 FAILED at 25
2 out of 3 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py.rej
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py
Hunk #1 FAILED at 62
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej
file sage/schemes/hyperelliptic_curves/invariants.py already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/invariants.py.rej
abort: patch failed to apply

```



---

Attachment


---

Comment by was created at 2009-05-12 06:31:13

(apply only trac_6010-genus-2-invariants-2.2.patch )


---

Comment by mabshoff created at 2009-05-12 06:42:00

Merged trac_6010-genus-2-invariants-2.2.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 06:42:00

Resolution: fixed
