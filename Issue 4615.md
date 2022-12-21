# Issue 4615: [with spkg, needs review] Make boehm_gc a standard spkg

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-25 11:49:34

Assignee: mabshoff

This is part of the project to replace clisp by ecl. The vote was at

http://groups.google.com/group/sage-devel/browse_thread/thread/450bb51e12fab1aa

Since it is already an optional spkg all that needs to be done is to patch deps and so on. Maxima should depend on boehm_gc.

The spkg is at

http://sagemath.org/packages/optional/boehm_gc-7.1.p0.spkg

Cheers,

Michael


---

Comment by was created at 2008-11-27 17:10:04

REFEREE:

I confirmed that src exactly equals upstream from http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/

I checked that the package installs on OS X, and that the spkg-install, etc., looks good.  It took 44 seconds to build on my OS X box, which isn't too bad.

This gets positive review, though of course deps and install must be modified.  Add this to install:


```
BOEHM_GC=`$newest boehm_gc`
export BOEHM_GC
```


Modify deps by adding/changing:

```
$(INST)/$(BOEHM_GC): $(BASE)
	$(SAGE_SPKG) $(BOEHM_GC) 2>&1
```


Boehm is *not* a dependency for Maxima as the ticket description says.  Instead Boehm should be made a dependency for ECL when that is added, and then Maxima depends on ECL.


---

Comment by mabshoff created at 2008-11-29 07:07:49

Yes, it is technically correct that ecl will depend on boehm, but making Maxima depend on it wouldn't hurt anybody.

One thing missing from William's remarks about deps is that additionally `$(INST)/$(BOEHM_GC)` needs to be added to the `all` target in deps.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 07:08:13

Resolution: fixed


---

Comment by mabshoff created at 2008-11-29 07:08:13

Merged in Sage 3.2.1.rc0
