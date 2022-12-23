# Issue 3310: sage -b fails after touching sage/libs/mwrank/{mwrank.pyx,wrap.cc}

Issue created by migration from https://trac.sagemath.org/ticket/3310

Original creator: cremona

Original creation time: 2008-05-26 19:26:46

Assignee: mabshoff


   1. Make a fresh clone of a 3.0.2 build.
   2. touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/mwrank.pyx
   3. sage -b
   4. touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/wrap.cc
   5. sage -b

...produces this:


```
----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
running install
running build
running build_py
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.
```

but then after doing again

```
touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/mwrank.pyx
```

sage -br works fine.




---

Comment by mabshoff created at 2008-05-26 20:28:25

Changing priority from minor to blocker.


---

Comment by mabshoff created at 2008-05-26 20:28:25

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2008-08-14 22:49:41

For the record: #3491 is a dupe of this and I closed the other ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-10 08:41:26

Resolution: fixed


---

Comment by mabshoff created at 2008-11-10 08:41:26

This ticket has been fixed via Craig's and Gonzalo's patch at #4480.

Cheers,

Michael
