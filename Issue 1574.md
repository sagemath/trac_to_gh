# Issue 1574: dependencies for non pyx files aren't properly tracked

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-20 12:14:49

Assignee: was

CC:  craigcitro tornaria

When applying a patch to a non `pyx|pxi|pxd` file (mwrank.cc in this case) and running `sage -b` odd things happen:

```

running install
running build
running build_py
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.

running install
running build
running build_py
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.
```

Touching a pyx file that the particular file depends upon (mwrank.pyx) in this case fixes the issue and everything is properly recompiled.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 09:07:46

This one just bit me in the ass again:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
running install
running build
running build_py
running build_ext
building 'sage.schemes.hyperelliptic_curves.hypellfrob' extension
error: unknown file type '.pyx' (from 'sage/schemes/hyperelliptic_curves/hypellfrob.pyx')
sage: There was an error installing modified sage library code.


real    0m1.540s
user    0m1.124s
sys     0m0.416s
```

Anybody willing to fix this? It seems that all that needs to be done is to add C/C++ files linked extensions to the list of dependencies to track.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-02 01:45:48

Resolution: fixed


---

Comment by mabshoff created at 2008-12-02 01:45:48

This has been fixed in Sage 3.2/3.2.1 due to the work done by Craig Citro and Gonzalo Tornaria


---

Comment by craigcitro created at 2008-12-02 04:06:47

And Robert Bradshaw. :)
