# Issue 2491: Showing source from sloane_functions

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-03-12 14:13:50

Assignee: mhansen

CC:  sage-combinat

From IRC #sage-devel


```
<mhansen> jaap: There's a difference between sloane.A000001?? and sage.combinat.sloane_functions.A000001??
<jaap> mhansen sage: sloane.A000001??
<jaap> Error getting source: arg is not a module, class, method, function, traceback, frame, or code object
<mhansen> jaap: A bit earlier I had said that  sloane.A000001?? doesn't work because of the way the sloane object works.
<jaap> ok, but how about the OEIS user who wants to see how things work?
<mhansen> If it's a bug, then it should be reported.
<jaap> I think so
```





```
sage: sloane.A000045
 Fibonacci numbers with index n >= 0

sage: sloane.A000045?

sage: sloane.A000045??
Error getting source: arg is not a module, class, method, function, traceback, frame, or code object

sage: sage.combinat.sloane_functions.A000045??

works ok.


```




---

Comment by was created at 2008-03-12 15:36:29

> sage: sloane.A000045??
> Error getting source: arg is not a module, class, method, function, traceback, frame, or code object

That this doesn't work should be considered a bug.   The actual introspection is simply some python code I wrote, so it's fixable.  Nick also knows something about it.


---

Attachment


---

Comment by mabshoff created at 2008-08-27 01:57:43

Positive review. Works for me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 02:17:20

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 02:17:20

Merged in Sage 3.1.2.alpha1
