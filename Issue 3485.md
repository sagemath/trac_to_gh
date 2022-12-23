# Issue 3485: [with patch, request comments, not ready for review] new sage_input function gives a sequence of commands to reproduce sage values

Issue created by migration from https://trac.sagemath.org/ticket/3485

Original creator: cwitty

Original creation time: 2008-06-20 08:18:11

Assignee: cwitty

CC:  ncalexan wstein

This patch creates a new sage_input function, that does things like this:

```
sage: sage_input((polygen(GF(3))+1)^4)

R.<x> = GF(3)[]
x^4 + x^3 + x + 1
```


I am not done writing docstrings and doctests, so the patch is not ready for review; but any comments on the general approach would be appreciated.  (Also, sage_input is implemented for only a few types; but I picked "complicated" types, so I think the underlying framework is ready to go.)

This patch depends on #3484.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-07-06 10:59:54

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-06 10:59:54

I will ping somebody to review this patch and #3484 soon.

Cheers,

Michael


---

Comment by was created at 2008-08-13 09:20:12

REFEREE REPORT:

 * My god, this is some of the most beautiful and well documented systematic code I've ever soon.  I have no problems with any of it.  Damn.  Positive review.


---

Comment by mabshoff created at 2008-08-13 17:59:29

There is some slight problem applying this:

```
sage-3.1.alpha2/devel/sage$ patch -p1 --dry-run < trac_3485-sage_input-v2.patch 
patching file sage/misc/all.py
Hunk #1 succeeded at 65 (offset 2 lines).
patching file sage/misc/sage_input.py
patching file sage/rings/integer.pyx
Hunk #1 succeeded at 2943 (offset 16 lines).
patching file sage/rings/integer_mod.pyx
patching file sage/rings/integer_ring.pyx
Hunk #1 succeeded at 823 with fuzz 2 (offset 8 lines).
patching file sage/rings/polynomial/polynomial_element.pyx
patching file sage/rings/polynomial/polynomial_ring.py
Hunk #1 succeeded at 392 with fuzz 2 (offset 17 lines).
patching file sage/rings/real_mpfr.pyx
Hunk #1 succeeded at 280 (offset 12 lines).
Hunk #2 succeeded at 966 (offset 16 lines).
patching file sage/rings/ring.pyx
Hunk #1 FAILED at 1505.
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/ring.pyx.rej
```

It also seems that only trac3485-sage_input-v2.patch should be applied.

Thoughts?

Cheers,

Michael


---

Comment by cwitty created at 2008-08-13 18:14:06

Yes, only apply -v2.patch.

The patch to ring.pyx only adds a new method, so it should be easy to apply by hand.  But if you don't want to do that, I can rebase the patch against alpha1 tonight.


---

Attachment


---

Comment by mabshoff created at 2008-08-13 18:57:18

Merged trac3485-sage_input-v2.patch and trac3485-sage_input-review-response.patch in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-13 18:57:18

Resolution: fixed
