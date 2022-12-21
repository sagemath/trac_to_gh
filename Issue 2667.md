# Issue 2667: transform.pyx calls matrix() with an RDF vector inside of a list instead of a flat list.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-25 21:26:00

Assignee: was


When applying the patch for a overhauled matrix() function at 
#2651, I get doctest failures 
from sage/plot/plot3d/transform.pyx related to calling 
matrix() with a list of rows, but specifying a number of rows that 
conflicts.

You can see these failures by applying the patch and running sage -t 
-long on 
devel/sage/sage/plot/plot3d/shapes2.py (and the same failures make a 
whole bunch of other doctests fail too).

For transform.pyx, the call to matrix on line 44 appears to flatten the 
trans argument (i.e., list(trans)), but many times what is actually 
passed to Sage is a list containing a single RDF vector instead.



---

Attachment

I discussed this solution with robertwb and cwitty.  I added a `__list__()` method to RealDoubleVectorSpaceElement to allow its elements to be converted to a list.  This makes the hand-off between Transform and matrix() work (see transform.pyx line 44).  

However, the vector was still coming into the Transform object wrapped in a one-element list.  The problem was that Graphics3d.translate() allows a variable number of arguments for convenience.  Before, if the first argument was a list or a tuple (note NOT a vector), this sequence was passed directly to self.transform().  As suggested by robertwb, replacing the code

```
        if isinstance(x[0], (tuple, list)):
            x = x[0]
```

with 

```
        if len(x)==1:
            x = x[0]
```

works since a sequence is the only acceptable one-argument input in this case.  This solution also avoids having to check types.

Note that changing the isinstance() call in the scale() method just below DOES NOT work.  I didn't take the time to figure out why; everything seems to be working now.  (The special-case code around line 627 and the fact that scale() is meaningful with only one input argument probably have something to do with it.)


---

Comment by mhansen created at 2008-03-29 21:01:57

I don't think __list__ does anything.  See #2626 .


---

Attachment


---

Comment by mhansen created at 2008-03-31 19:36:09

I've removed __list__.  The patch applies, and sage -t -long on devel/sage/sage/plot/plot3d/shapes2.py passes when #2651 is applied.


---

Comment by jason created at 2008-03-31 19:41:25

apply just 2667.patch; rhinton and mhansen (and maybe robertwb and cwitty?) should all probably get credit.


---

Comment by mabshoff created at 2008-03-31 19:47:27

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-03-31 19:47:27

Resolution: fixed


---

Attachment

Good catch, mhansen.  Apply this patch instead of the previous patch.


---

Comment by rhinton created at 2008-04-01 15:28:07

Sorry, my page must not have refreshed.  Ignore my last patch and use mhansen's instead.
