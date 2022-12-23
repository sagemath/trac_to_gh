# Issue 3523: [with spkg; needs review] upgrade flint to 1.0.10

Issue created by migration from https://trac.sagemath.org/ticket/3523

Original creator: was

Original creation time: 2008-06-27 14:45:08

Assignee: mabshoff

Among other things, this fixes a MAJOR bug in flint-1.0.6 (in getting coefficients of polys) which would make that version of flint pretty useless.


---

Comment by was created at 2008-06-27 18:37:54

WARNING: current version of package doesn't copy libflint.so over correctly after build on linux, but does on OS X.  On linux you must do

```
   sage -f -m flint-1.0.10.spkg
   then copy spkg/build/flint-1.0.10/src/... ?? libflint.so to SAGE_ROOT/local/lib
```



---

Comment by craigcitro created at 2008-07-01 00:38:16

I tested the most recent spkg available at the URL listed above, and it works on Mac OSX. I also watched over William's shoulder as he tested it on Linux, so I can say that I've seen it work on two platforms. Note that this ticket is an absolute necessity for both #2357 and #3502, so we should get this merged ASAP.


---

Comment by craigcitro created at 2008-07-01 00:38:28

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-07-01 02:57:46

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-01 02:57:46

Resolution: fixed


---

Comment by burcin created at 2008-07-01 08:10:49

The package linked from #2357 modifies the Makefile in FLINT to install the NTL interface. Does this package include those changes? 

It might be a good idea to check this package with the patch from #2357.


---

Comment by craigcitro created at 2008-07-01 14:37:54

No worries -- I've already done that. It works fine.
