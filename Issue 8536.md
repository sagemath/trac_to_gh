# Issue 8536: Change SAGE" to "Sage" in output

Issue created by migration from https://trac.sagemath.org/ticket/8536

Original creator: cremona

Original creation time: 2010-03-14 18:01:19

Assignee: was

CC:  jhpalmieri

When quitting we see

```
Exiting SAGE (CPU time 0m0.04s, Wall time 0m0.63s).
```

and there are several other places where "SAGE" is output instead of "Sage".

The patch changes these.  I tested the whole library: no doctests needed changing at all.  But maybe there are other issues which I did not think of.


---

Comment by cremona created at 2010-03-14 18:03:48

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-03-25 05:36:00

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-03-25 05:36:00

This looks good, although I did find some other instances of SAGE in output: `c_lib/src/interrupt.c` near the end of the file has a bunch of SAGEs; see line 138 to the end. With those changes, I'll give this a positive review.


---

Comment by cremona created at 2010-04-01 09:23:10

applies to 4.3.5


---

Attachment

I don't know how to change the file c_lib/src/interrupt.c safely since it is not included in the cloning system.  Can you either tell me how to do that, or do it yourself?

Meanwhile I have added to the patch to deal with file misc/sagedoc.py so that the latex control sequences \sage and \SAGE (and also \Sage) convert to 'Sage' instead of 'SAGE'.  I am not too sure of the reperucssions of this (it will surely change a lot o the documentation, but not affect doctests), so I am cc-ing jpalmieri and hope that he will comment.

I testing the whole sage library and all tests passed.


---

Comment by ddrake created at 2010-04-01 12:32:11

Replying to [comment:3 cremona]:
> I don't know how to change the file c_lib/src/interrupt.c safely since it is not included in the cloning system.  Can you either tell me how to do that, or do it yourself?

I believe that directory is in the same Mercurial repo that the main Sage library is in -- it looks like interrupt.c was last changed by revision 9552:470b9bd4c96e (try "hg annotate" on that file). If you are using queues, you should be able to just make the change and do "hg qref". That worked for me.

I'm running doctests now; it's not finished, but I would be surprised if anything fails.


---

Comment by cremona created at 2010-04-01 13:24:04

same as previous + c_lib/src/interrupt.c edits


---

Comment by cremona created at 2010-04-01 13:24:57

Changing status from needs_work to needs_review.


---

Attachment

You are right.  I updated the patch to include that file, and reinstated "needs review".


---

Comment by ddrake created at 2010-04-02 01:41:21

Everything looks good, and all tests pass. Positive review -- although if John Palmieri finds something fishy with the sagedoc.py, he should revert that. I find it very unlikely that there's any problem, though.


---

Comment by ddrake created at 2010-04-02 01:41:21

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-02 05:26:31

The changes to sagedoc.py look okay to me.


---

Comment by cremona created at 2010-04-02 09:45:20

Replying to [comment:8 jhpalmieri]:
> The changes to sagedoc.py look okay to me.

Thanks, and sorry for the typo.  John


---

Comment by jhpalmieri created at 2010-04-16 18:40:32

Merged "trac_8536-SAGE.2.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 18:40:32

Resolution: fixed
