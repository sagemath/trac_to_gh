# Issue 3694: Update FLINT to the 1.0.13 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-21 17:58:02

Assignee: tbd

Several issues were fixed, among them a bug that could in some rather unlikely cases cause random memory to be accessed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 18:12:32

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/flint-1.0.13.spkg

Make sure to rebuild the following extension by running

```
touch devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx
./sage -b
```

Otherwise Sage will complain about an import error. The fix is non-trivial and needs to be coordinated with the packaging teams for Debian and Gentoo, so it is post 3.0.6 material.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 18:12:47

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-07-21 18:12:47

Changing assignee from tbd to mabshoff.


---

Comment by mabshoff created at 2008-07-21 18:12:47

Changing component from algebra to build.


---

Comment by mabshoff created at 2008-07-21 18:34:57

Also make sure to 

```
touch devel/sage/sage/libs/flint/fmpz_poly.pyx
./sage -b
```

I knew there were *two* of those suckers to rebuild.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 22:20:39

Resolution: fixed


---

Comment by mabshoff created at 2008-07-21 22:20:39

Merged in Sage 3.0.6.rc0
