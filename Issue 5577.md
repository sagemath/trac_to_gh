# Issue 5577: [with patch, needs review] typo in tutorial

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-20 18:18:20

Assignee: tba

This is a repeat of #4379, changing one word in the tutorial: the change there was undone, perhaps in the ReST conversion, and this reinstates it.


---

Attachment

Oh, this might depend on #5500.


---

Comment by jhpalmieri created at 2009-03-20 20:18:14

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-03-20 20:18:14

Changing status from new to assigned.


---

Comment by mvngu created at 2009-03-23 02:50:14

REFEREE REPORT



The patch *tut-typo.patch* applies against Sage 3.4, but with some fuzz:

```
sage: hg_sage.apply("/home/mvngu/patch/5577/tut-typo.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5577/tut-typo.patch"
applying /home/mvngu/patch/5577/tut-typo.patch
patching file doc/en/tutorial/tour_help.rst
Hunk #1 succeeded at 120 with fuzz 1 (offset -1 lines).
```

That didn't prevent me from (re)building the tutorial in HTML format. Viewing the updated section "Getting Help" in the tutorial, I see that the patch fixes the problem it meant to fix. I don't know how significant the above fuzz is, but probably it doesn't matter at all, in which case I'd give a positive review to the patch.


---

Comment by jhpalmieri created at 2009-03-23 04:01:49

Okay, it definitely depends on #5500.  (Without applying #5500, you see the fuzz.)


---

Comment by mvngu created at 2009-03-23 04:06:58

Looks good, positive review. So here's the order in which patches should be applied:
 1. First apply patches at #5500.
 1. Then apply *tut-typo.patch*.
This ordering should prevent any fuzz.


---

Comment by mabshoff created at 2009-03-23 18:39:47

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 18:39:47

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
