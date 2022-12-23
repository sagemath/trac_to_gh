# Issue 4996: OSX64: add proper libcsage build support

Issue created by migration from https://trac.sagemath.org/ticket/4996

Original creator: mabshoff

Original creation time: 2009-01-17 15:37:45

Assignee: mabshoff

Patch coming up: We need to add 

```
## We want the debug and optimization flags, since debug symbols are so useful, etc.
env.Append( CFLAGS="-O2 -g -m64" )
env.Append( CXXFLAGS="-O2 -g -m64" )
env.Append( LINKFLAGS="-m64 -single_module -flat_namespace -undefined dynamic_lookup" )
```

in case we are building in 64 bit mode on OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-17 15:37:51

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-01-23 00:30:47

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 00:30:47

Resolution: fixed


---

Comment by rlm created at 2009-01-23 00:37:15

+1 post-mortem...


---

Comment by mabshoff created at 2009-01-23 00:37:57

Yeah, sorry that I jumped the gun here ;)

Cheers,

Michael
