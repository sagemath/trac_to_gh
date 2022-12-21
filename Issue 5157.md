# Issue 5157: if the mwrank interface is interrupted from the notebook (!) it stays broken for the rest of the sage session

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-02 06:09:32

Assignee: was

This has been driving me nuts for a while.  If you do 

```
sage: EllipticCurve(997).gens(use_database=False)
[This is the Trac macro *press control-c* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#press control-c-macro)
sage: EllipticCurve([1,3]).gens(use_database=False)
Traceback (most recent call last):
...
RuntimeError: [Errno 9] Bad file descriptor
Error evaluating [0, 0, 0, 1, 3] in Mwrank
```


This is from the notebook.  The same sequence works correctly from the command line (no bad file descriptor). 

I think the problem is that the notebook sends multiple control-c's and ends up killing sage properly restarting mwrank.  On the command line one has:


```
sage: EllipticCurve(997).gens(use_database=False)
...
KeyboardInterrupt: Restarting Mwrank (WARNING: all variables defined in previous session are now invalid)
sage: EllipticCurve([1,3]).gens(use_database=False)
[(-1 : 1 : 1)]
```


BUT, if you hit control-c twice in rapid succession, then mwrank gets broken even on the command line (I just verified this).

The fix is to make it so the mwrank interface recovers automatically if it gets left in this state. 



---

Comment by mhansen created at 2009-02-02 06:18:45

It seems to be okay, but do we really want the "print '*'*1000" in there?


---

Attachment


---

Comment by cremona created at 2009-02-02 09:55:04

This should be refereed by someone who knows pexpect!


---

Comment by was created at 2009-02-02 10:21:53

> It seems to be okay, but do we really want the "print '*'*1000" in there? 

That's debugging code -- I updated the patch to not have it. 

> This should be refereed by someone who knows pexpect! 

Mhansen does, and he said "it seems to be okay".


---

Comment by mabshoff created at 2009-02-02 18:26:33

Since Mike gave this the heads up and William removed the debug print statement I am changing this to a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 18:53:21

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 18:53:21

Resolution: fixed
