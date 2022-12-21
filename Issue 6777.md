# Issue 6777: segfault with univariate polynomial, realfield, complexfield

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-08-19 22:48:53

Assignee: malb

CC:  mjo

Keywords: polynomial segfault

This is with a modified

```
```

| Sage Version 4.1.rc1, Release Date: 2009-07-07                     |
Mac OS X, Intel hardware.


```
sage: RealField(300)['x']( [ 1, ComplexField(300).gen(), 0 ])


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


Process SAGE exited abnormally with code 1
```



---

Comment by SimonKing created at 2011-12-15 17:44:12

I don't obtain a segmentation fault, but this is on Debian GNU/Linux.

On [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/d4807256e57cd843), it is discussed that one gets a rather strange phenomenon: Before the traceback starts, some ERROR is printed.

```
sage: RealField(300)['x']( [ 1, ComplexField(300).gen(), 0 ])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1375, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1375, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

```

I get this with unpatched sage (hence, no segfault), and Michael Orlitzky reports the same after fixing the segfault.

However, with some of my patches applied, one simply gets a straight forward traceback:

```
sage: RealField(300)['x']([ ComplexField(300).gen() ]) 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: Unable to convert x (='1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*I') to real number.
```


Could you test whether #9138 (or perhaps #11900) actually fixes the problem already?


---

Comment by mjo created at 2011-12-15 18:41:58

The fix is in #11900, and it has a positive review, so I'm adding it as a dependency before a doctest can be added.


---

Comment by mjo created at 2011-12-15 18:51:08

Changing status from new to needs_review.


---

Comment by mhansen created at 2011-12-17 20:54:22

Patch to add a doctest expecting a TypeError


---

Attachment

mjo's patch looks good to me.  I updated the formatting slightly.


---

Comment by mhansen created at 2011-12-17 20:55:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-18 08:08:18

Resolution: fixed
