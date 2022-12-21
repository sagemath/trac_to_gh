# Issue 1247: cremona-20071116.p0.spkg fails to build on Arch linux, 32bit linux, gcc-4.2.2

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-23 12:50:51

Assignee: mabshoff

*Andrzej Giniewicz reported:

```
 not counting plenty (281) warnings in file curvesort.cc (about
deprecated conversion from string constant to 'char*') I also get
WHOLE lot (about 8000) errors all in one nature:

../g0n/curvesort.cc:106: error: jump to case label
../g0n/curvesort.cc:105: error:   crosses initialization of 'int
<anonymous>[3]'

with different numbers only... problems starts from:

g++ -c -fPIC -g -O2 -DNEW_OP_ORDER -DUSE_PARI_FACTORING -I../include -
DNTL_ALL -I/opt/sage/local/include -I/opt/sage/local/include  tsat3.cc
-o tsat3_n.o
In file included from tsat3.cc:37:
../g0n/curvesort.cc ....... etc etc

I think there is no sense to attach such big report... I'm running
current Arch Linux, that is GCC 4.2.2, gLibc 2.7, kernel 2.6.23.8. Is
there some workaround? 
```


See http://groups.google.com/group/sage-support/t/c2140ece9608358e

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-23 12:51:01

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-23 12:54:53

There is also an issue on OpenSuSE 10.2:

```
You mention that there is an issue with cremona.spkg on Linux/Itanium with
older gcc and also Solaris. My settings are:
- openSUSE 10.2 (X86-64),
- AMD Athlon(tm) 64 Processor 3700+
- gcc-Version 4.2.1; I think this isn't exactly old, or is it? 
```


See http://groups.google.com/group/sage-support/t/8e446357a1d15a8a

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 03:01:59

There is a new cremona.spkg that should work with gcc 4.2.x at 

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 10:54:01

The bundle applied also includes #1238. So close that too when closing this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:37:22

Merged in 2.8.14.rc0. Feedback provided by various people indicates that the problem is fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:37:22

Resolution: fixed
