# Issue 1268: [with spkg] new version of MPFI

Issue created by migration from https://trac.sagemath.org/ticket/1268

Original creator: cwitty

Original creation time: 2007-11-25 15:26:58

Assignee: was

I've built a new MPFI spkg that switches to using the current MPFI CVS.  (They have all the bug fixes from the previous Sage spkg, and more.)  Plus, they've started installing shared and static libraries, so we end up using the shared library version.

The new spkg is at http://sage.math.washington.edu/home/cwitty/mpfi-1.3.4-cvs20071125.spkg

testall passes on 32-bit x86 linux with the new spkg.

By the way, if you're going to test it, you can't just install the new spkg, because the old library will still be statically linked in to the relevant extension modules.  You also need to do:

```
touch devel/sage/sage/rings/mpfi.pxi
sage -b
```



---

Comment by cwitty created at 2007-11-25 17:17:07

As mentioned above, simply installing the new spkg isn't enough; we need to ensure that extensions depending on the library get rebuilt.  One way to do this for upgrades to 2.8.15 is to apply the patch from #1270 (or any other patch that touches mpfi.pxi).


---

Comment by robertwb created at 2007-11-29 22:16:50


```
(cd .libs && rm -f libmpfi.0 && ln -s libmpfi.0.0.0 libmpfi.0)
(cd .libs && rm -f libmpfi && ln -s libmpfi.0.0.0 libmpfi)
ar cru .libs/libmpfi.a  mpfi.o mpfi_io.o mpfi_trigo.o~ranlib .libs/libmpfi.a
ar: mpfi_trigo.o~ranlib: No such file or directory
make[1]: *** [libmpfi.la] Error 1
make: *** [install-recursive] Error 1
An error occurred while building mpfi.

real    0m19.460s
user    0m4.463s
sys     0m8.673s
sage: An error occurred while installing mpfi-1.3.4-cvs20071125
```


OS X 10.4, Intel (core duo)


---

Comment by cwitty created at 2007-11-30 03:28:39

I edited the Description to point at a new version of the spkg, that may fix the above OSX compilation failure.


---

Comment by rlm created at 2007-11-30 05:25:09

Installs fine on Intel OS X 10.5.1.


---

Comment by mabshoff created at 2007-12-01 11:03:23

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:03:23

Resolution: fixed
