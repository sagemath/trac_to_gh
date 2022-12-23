# Issue 3230: [with patch; needs review] cygwin -- new givaro spkg that works around stupidity in cygwin

Issue created by migration from https://trac.sagemath.org/ticket/3230

Original creator: was

Original creation time: 2008-05-16 22:29:05

Assignee: mabshoff

Cygwin forgot this line in math.h: 

```
extern double logb _PARAMS((double));
```


I put that line in the relevant file (see spkg-install) and now the build works fine. 

The new spkg is here:

http://sage.math.washington.edu/home/was/cygwin/givaro-3.2.10.rc3.p2.spkg


---

Comment by mabshoff created at 2008-05-18 17:12:34

Spkg looks good to me. I added a diff of givtablelimits.h to the patches directory. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 17:12:46

Resolution: fixed


---

Comment by mabshoff created at 2008-05-18 17:12:46

Merged in Sage 3.0.2.alpha1
