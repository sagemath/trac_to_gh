# Issue 4842: Fix performance regression in eisenstein_submodule.py

Issue created by migration from https://trac.sagemath.org/ticket/4842

Original creator: mabshoff

Original creation time: 2008-12-20 22:54:44

Assignee: robertwb

CC:  craigcitro robertwb

See http://groups.google.com/group/sage-devel/browse_thread/thread/12394b2efb1f6344/59421c4079e00cc5 for details:

```
> That example was with CyclotomicField(12) and CyclotomicField(132) ... 

Ah. I bet the time was spent resolving the roots of CyclotomicField 
(132) to high enough precision to distinguish them. If you don't come   
up with a patch for this, I'll (probably) do it later tonight. 
- Robert 
```


Cheers,

Michael


---

Comment by robertwb created at 2008-12-21 10:28:57

Oh, I should handle the case of 2m -> m for m odd.


---

Attachment


---

Comment by robertwb created at 2008-12-21 13:12:42

This took longer than I expected due to build issues I ran into, but here's the patch. It should cover all cases, and use your fast code when the orders divide each other.


---

Comment by mabshoff created at 2008-12-21 13:53:55

For the record: Patch applies, builds fine and all doctests with -long pass. The performance regression seems to have been fixed, i.e. before:

```
sage -t -long "devel/sage/sage/modular/modform/eisenstein_submodule.py"
	 [73.3 s]
```

After the patch:

```
sage -t -long "devel/sage/sage/modular/modform/eisenstein_submodule.py"
	 [3.4 s]
```


Cheers,

Michael


---

Comment by cremona created at 2008-12-21 21:22:15

This looks very good to me.  The maths is sound, the examples I tried worked, doctests passed and Michael is happy -- what more could we want?  I give this a positive review.


---

Comment by mabshoff created at 2008-12-21 22:00:02

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 22:00:02

Merged in Sage 3.2.3.alpha0
