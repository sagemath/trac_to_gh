# Issue 1698: PolyBoRi doesn't work at all on Itanium Linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-06 01:41:04

Assignee: mabshoff

CC:  burcin


```

Has anybody ever built or used PolyBoRi on Linux *ITANIUM*?  
Because I just tried and the simplest
use of it from Sage segfaults PolyBoRi.   Since Itanium is 
supposed to be supported Sage platform this is very
serious:

sage -t --gdb pbori.pyx

SIGSEGV
boost::intrusive_ptr<polybori::CCuddCore>::operator-> (this=0x0)
   at ...intrusive_ptr.hpp:120
120         return p_;

(this was typed in by me manually just now). 

Any ideas?!   If necessary I can loan you the password I  have to an itanium box, but
hopefully one of you has access to an Itanium Linux machine.
```



---

Comment by mabshoff created at 2008-01-23 23:15:05

Since Kate reported building 2.10 on Linux/Itanium and it passing doctests except #1898 the issue reported above is probably something system specific.

Cheers,

Michael


---

Comment by was created at 2008-02-19 15:17:43

Resolution: fixed
