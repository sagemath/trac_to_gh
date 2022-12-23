# Issue 4798: Update Cython to 0.10.3 (latest stable upstream)

Issue created by migration from https://trac.sagemath.org/ticket/4798

Original creator: mabshoff

Original creation time: 2008-12-14 17:08:53

Assignee: robertwb

This is from #4639:

```
Install cython-0.10.3.spkg at http://sage.math.washington.edu/home/robertwb/cython/ ,
which contains a fix to http://trac.cython.org/cython_trac/ticket/162 and I think is 
the underlying cause here (and probably elsewhere). 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 17:12:22

The spkg looks good, a -ba works fine and doctests pass. This release significantly reduces the leaks from #4639, even though some leak remains to be fixed. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 17:19:57

Merged in Sage 3.2.2.rc0


---

Comment by mabshoff created at 2008-12-14 17:19:57

Resolution: fixed


---

Comment by robertwb created at 2008-12-15 18:29:59

Note: I'd rather not consider this the final 0.10.3 until I finish tracking down that memory leak, which may involve another Cython fix. (If 3.2.2 is released, before then, this should probably be 0.10.2p0)


---

Comment by mabshoff created at 2008-12-15 18:32:45

Ok,

I think we can live with 0.10.2.p0 in tree and will rename it in my 3.2.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 18:37:37

Ok, the renamed spkg is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/rc0/cython-0.10.2.p0.spkg

and is in 3.2.2.rc0.

Cheers,

Michael
