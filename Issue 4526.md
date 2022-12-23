# Issue 4526: Can't multiply symmetric functions by 0

Issue created by migration from https://trac.sagemath.org/ticket/4526

Original creator: jbandlow

Original creation time: 2008-11-14 20:00:43

Assignee: mhansen

CC:  jbandlow sage-combinat

Keywords: symmetric functions

The following, which should just return 0 in SFASchur(QQ), is really nasty:

sage: s = SFASchur(QQ)
sage: 0 * s([1])
sage.bin: : Unknown error 155689240

and sage quits.


---

Comment by jbandlow created at 2008-11-14 20:03:39

arg... I meant

sage: s = SFASchur(QQ)

sage: 0 * s([1])

of course.


---

Comment by mabshoff created at 2008-11-14 20:08:49

FYI: the error message comes out of symmertrica. And:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sage-ipython
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
[Thread debugging using libthread_db enabled]
[New Thread 47664905056096 (LWP 26555)]
Python 2.5.2 (r252:60911, Nov 10 2008, 22:40:35) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

sage: s = SFASchur(QQ)
sage: 0 * s([1]) 
/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/python: OWER_symmetrica: Operation not permitted

Program exited with code 0341.
(gdb) bt
No stack.
```


Cheers,

Michael


---

Comment by mhansen created at 2008-11-15 02:15:27

Changing status from new to assigned.


---

Attachment


---

Comment by jbandlow created at 2008-11-15 03:30:32

Works for me.  Thanks Mike!


---

Comment by mabshoff created at 2008-11-15 04:48:42

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-15 04:48:42

Resolution: fixed
