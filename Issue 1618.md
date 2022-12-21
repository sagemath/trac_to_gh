# Issue 1618: Make SCons use the GNU compiler even when Intel's compilers are present

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-29 03:55:55

Assignee: mabshoff

In http://groups.google.com/group/sage-devel/t/74de10c9f2d3edf7 Francois reported:

```
Hello Michael,

I think I found my problem. A little googling actually helped with
this link:
http://bugs.archlinux.org/task/6864
I did some experiments with the intel _fortran_ compiler (not even the
C compiler)
and I still have it on my system.
Since the intel compiler doesn't compile my lattice QCD code correctly
anyway
I will remove it and try again.
I am busy for the next few hours so I will do that a bit latter.

Thanks for looking,
Francois
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-29 03:56:07

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-23 18:30:40

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-03-23 18:30:40

Changing status from assigned to new.


---

Comment by gfurnish created at 2008-03-23 18:30:58

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-24 16:37:46

Since none of the code we compile with SCons is actually Fortran there is no point in selecting a different default Fortran compiler. Since SCons doesn't support g95 or gfortran (even with the December 2007 release!) we just remove the offending linker flag. The update spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/scons-0.97.0d20071212.spkg

It updates to the latest stable snapshot release. It also removes some crap from inside the spkg shrinking it about 30%. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-24 16:46:24

Build tested on OSX and Linux.

Cheers,

Michael


---

Comment by jkantor created at 2008-03-24 17:30:08

Tested that spkg installs. Rebuilt polybori and clib.


---

Comment by mabshoff created at 2008-03-24 17:30:47

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 17:30:47

Merged in Sage 2.11.alpha2
