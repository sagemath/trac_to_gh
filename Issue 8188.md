# Issue 8188: additional functions for linear codes

Issue created by migration from Trac.

Original creator: klee

Original creation time: 2010-02-05 04:01:13

Assignee: Kwankyu Lee

A few enhancements of linear codes functionality.


---

Comment by mvngu created at 2010-02-05 04:20:43

Is this ready for review?


---

Comment by klee created at 2010-02-05 04:22:18

Changing assignee from Kwankyu Lee to klee.


---

Comment by klee created at 2010-02-05 04:22:27

Changing status from new to needs_review.


---

Comment by wdj created at 2010-02-05 12:46:08

This looks good. Thank you. I'll test it and give a formal review when I get home.

Can you please add a small patch which adds your name to the AUTHOR section and a brief description of what you added?


---

Comment by wdj created at 2010-02-05 18:39:46

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2010-02-05 18:39:46

This patch fails to apply to 4.3.2.rc0.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: 8188-coding
sage: hg_sage.apply("/Users/wdj/sagefiles/trac_8188.patch")
cd "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage" && hg import   "/Users/wdj/sagefiles/trac_8188.patch"
applying /Users/wdj/sagefiles/trac_8188.patch
patching file sage/coding/linear_code.py
Hunk #1 FAILED at 1406
Hunk #2 succeeded at 1416 with fuzz 2 (offset -11 lines).
Hunk #3 succeeded at 1468 with fuzz 1 (offset -2 lines).
Hunk #4 succeeded at 1684 with fuzz 1 (offset 4 lines).
1 out of 4 hunks FAILED -- saving rejects to file sage/coding/linear_code.py.rej
abort: patch failed to apply
```

| Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
| Type notebook() for the GUI, and license() for information.        |
Please make the following changes

(1) fix the patch so that it applies correctly
(2) Add you name to AUTHOR
(3) Add a short definition of systematic and information set to the docstrings.

If you do all these, and the patch applies and passes sage -testall then I'll give this a positive review.

Thanks for working on this!


---

Comment by klee created at 2010-02-08 06:23:42

The patch applied to 4.3.2 passed doctest.


---

Comment by klee created at 2010-02-08 06:23:42

Changing status from needs_work to needs_review.


---

Comment by klee created at 2010-02-08 07:13:59

rebased on Sage 4.3.2; added more docstrings as requested


---

Comment by wdj created at 2010-02-08 13:50:22

Changing status from needs_review to positive_review.


---

Attachment

Looks good, applies fine to 4.3.2 and passes sage -testal.

Thank you for adding this!

Positive review.


---

Comment by mpatel created at 2010-02-11 14:53:27

Resolution: fixed
