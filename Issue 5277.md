# Issue 5277: tachyon.spkg: link against libpng12 instead of libpng

Issue created by migration from https://trac.sagemath.org/ticket/5277

Original creator: mabshoff

Original creation time: 2009-02-15 15:27:42

Assignee: mabshoff

tachyon - in src/unix/Make-config change -lpng to -lpng12:

```
USEPNG= -DUSEPNG
PNGINC= -I$(SAGE_LOCAL)/include
PNGLIB= -L$(SAGE_LOCAL)/lib -lpng12 -lz
```

We can probably set PNGLIB in spkg-install, so we don't have to edit any build system files.

Spkg coming up. Together with some changes via the libpng update at #5217 this will solve a long standing problem when we run into symbol clashes on OSX with its IOKit.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 15:27:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-16 04:55:56

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/tachyon-0.98beta.p8.spkg

implements that change.

Cheers,

Michael


---

Comment by mhampton created at 2009-02-16 11:28:56

This seems to work fine for me, on an intel mac running 10.5.6.


---

Comment by mabshoff created at 2009-02-16 11:31:21

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 11:31:21

Resolution: fixed
