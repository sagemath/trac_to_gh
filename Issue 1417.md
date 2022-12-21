# Issue 1417: update symmetrica

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-07 09:54:27

Assignee: was

There is an spkg at http://sage.math.washington.edu/home/mhansen/symmetrica-2.0.spkg 


---

Attachment


---

Comment by mhansen created at 2007-12-07 10:27:10

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-07 10:27:10

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-07 10:57:59

Build time has increased. On neron, i.e an Ultra III Sparc:

```
real    61m13.083s
user    60m26.070s
sys     0m35.080s
Successfully installed symmetrica-2.0
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-08 04:26:11

Mike Hansen and I did some more testing and all the following figures are from sage.math:

```
0.3.3:

real    0m51.192s
user    0m46.991s
sys     0m3.044s

2.0 vanilla, i.e. "-O2":

real    31m30.192s
user    30m48.360s
sys     0m35.214s

2.0 "-O0" +pch:

real    4m6.438s
user    3m45.962s
sys     0m15.149s

2.0 "-O0":

real    4m14.650s
user    3m56.743s
sys     0m16.057s

2.0 "-O1":

about 13 minutes
```

Mike Hanson did some benchmarking:  "It looks like O1 is just as fast (and in some cases faster) than O2."

So, "-O1" it ought to be.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 10:09:11

Build tested on Solaris, OSX 10.4 and OSX 10.5.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 10:14:21

Merged in 2.9.alpha2.


---

Comment by mabshoff created at 2007-12-09 10:14:21

Resolution: fixed


---

Comment by was created at 2007-12-10 04:29:21

I just tested this on my osx 10.5.1 laptop and it took 6 minutes to build and everything seems to work.   Thanks guys!!
