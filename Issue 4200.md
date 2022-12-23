# Issue 4200: Update numpy to 1.2.0

Issue created by migration from https://trac.sagemath.org/ticket/4200

Original creator: jason

Original creation time: 2008-09-26 04:47:29

Assignee: mabshoff

Numpy 1.2.0 came out today.  An updated spkg is here: http://sage.math.washington.edu/home/jason/numpy-1.2.0.spkg

Crazily, apparently some parts of numpy are deprecated and throw warnings, while other parts still use the deprecated functions.  The upshot is that Sage, upon importing scipy, displays several warnings about deprecated numpy stuff.  Also, using numpy, like in the solve_left function, triggers deprecation warnings about other parts of numpy.



---

Comment by jason created at 2008-09-26 04:51:30

The problem might just be that we have an old version of scipy, which is triggering these deprecation warnings.


---

Comment by mabshoff created at 2008-09-26 04:52:42

Hmm, feel like updating scipy then, too? That will be a littl more work since we monkey with various setup.pys, so this spkg might not make it into 3.1.3 :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 06:46:23

Very nice work Jason, I could not have done better myself :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 06:46:39

Resolution: fixed


---

Comment by mabshoff created at 2008-09-27 06:46:39

Merged in Sage 3.1.3.alpha2
