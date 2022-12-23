# Issue 1594: libm4ri -- in library mode it doesn't work at all on osx -- lots of segfaults

Issue created by migration from https://trac.sagemath.org/ticket/1594

Original creator: was

Original creation time: 2007-12-24 18:15:53

Assignee: was

On all variants of OSX the new libm4ri doesn't work at all.

I just did some poking around and putting my own 


---

Comment by wjp created at 2007-12-24 18:21:47

The backtrace William posted on sage-devel shows m4ri is using a min() defined in a file nu.c instead of the min() in m4ri itself.

This seems to point at symmetrica, which has a file nu.c with a min() defined in it.


---

Comment by mabshoff created at 2007-12-24 21:35:25

I believe this has been fixed in the 2.9.1 release.

Cheers,

Michael


---

Comment by wjp created at 2007-12-25 13:22:08

William worked around this linker issue by adding a line

#define min(x,y) ((x < y)?x:y)

at the top of brilliantrussian.c and packedmatrix.c. I hope there aren't any other subtle things like this that could hurt us elsewhere. Symmetrica defines a lot of 'common' function names like min.


---

Comment by malb created at 2007-12-25 15:04:48

I can confirm that all tests of `make test` pass on bsd (Intel OSX).


---

Comment by malb created at 2007-12-25 15:10:54

Resolution: fixed
